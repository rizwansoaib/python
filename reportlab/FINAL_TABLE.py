from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch,A4
from reportlab.platypus import Image, Spacer, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

doc = SimpleDocTemplate("output.pdf", pagesize=A4)

elements = []
styles=getSampleStyleSheet()

elements.append(Image("logo.png"))


elements.append(Spacer(20,30))
 
styleSheet = getSampleStyleSheet()
 

a=['RIZWAN','GHULAM','VINEET','DIWAKAR']
p=['A','P','A','A']
r=['178208','178204','178212','178203']

data= [['ROLL NO.', '                  NAME', 'P/A'],
       [r[0], a[0], p[0] ],
       [r[1], a[1], p[1]],
       [r[2], a[2], p[2]],
       [r[3], a[3], p[3]]]

for i in range(200):
  data.append(['00000','hello','A'])
c,s=0,0
for i in range(1,len(data)):
    if data[i][2]=='P': 
      c+=1
    s+=1

data.append(['','TOTAL',str(c)+'/'+str(s)])
t=Table(data,style=[('GRID',(0,0),(-1,-1),1,colors.black),
                    ('GRID',(0,0),(-1,-1),1,colors.black),
                    ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                    ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                    
                    ('GRID',(0,0),(-1,-1),.5,colors.black),
                    ('GRID',(0,0),(-1,-1),0.5,colors.black),
                   
                    
                    
           
                
])
t._argW[1]=2*inch
t._argW[2]=.35*inch
 
elements.append(t)


doc.build(elements)