from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
 
doc = SimpleDocTemplate("complex_cell_values.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
 
styleSheet = getSampleStyleSheet()
 

a=['RIZWAN','GHULAM','VINEET','DIWAKAR']
p=['A','P','A','A']
r=['178208','178204','178212','178203']

data= [['ROLL NO.', '                  NAME', 'P/A'],
       [r[0], a[0], p[0] ],
       [r[1], a[1], p[1]],
       [r[2], a[2], p[2]],
       [r[3], a[3], p[3]]]
 
t=Table(data,style=[('GRID',(0,0),(-1,-1),.5,colors.black),
                    ('GRID',(0,0),(-1,-1),.5,colors.black),
                    ('LINEABOVE',(1,2),(-2,2),.5,colors.blue),
                    ('LINEBEFORE',(2,1),(2,-2),.5,colors.pink),
                    
                    ('GRID',(0,0),(-1,-1),.5,colors.black),
                    ('GRID',(0,0),(-1,-1),0.5,colors.black),
                   
                    
                    
           
                
])
t._argW[1]=2*inch
t._argW[2]=.35*inch
 
elements.append(t)
# write the document to disk
doc.build(elements)