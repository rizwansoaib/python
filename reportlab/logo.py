from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import SimpleDocTemplate,Paragraph, Spacer, Image
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

a=['rizwan','gullu','rizwan','vineet']

b=['A','P','A','P']

'''filename = 'logo.png'
doc = SimpleDocTemplate("image.pdf", pagesize=A4)
parts = []
parts.append(Image(filename))
'''

doc = SimpleDocTemplate("file.pdf",pagesize=A4)

parts = []

styles=getSampleStyleSheet()
 
ptext = '<font size=20>Roll No.        Status</font>'
parts.append(Paragraph(ptext, styles["Normal"]))

parts.append(Spacer(20,30))

for name in a:
    ptext = '<font size=16>%s</font>' % name.strip()
    parts.append(Spacer(10,15))
    parts.append(Paragraph(ptext, styles["Normal"]))  

for i in range(len(a)):
	
    ptext = '<font size=16>%s</font>' % a[i].strip()
    parts.append(Spacer(-10,-15))
    ptext = '<font size=16>%s</font>' % b[i].strip()
    parts.append(Spacer(10,15))
    parts.append(Paragraph(ptext, styles["Normal"]))  



 
ptext = '<font size=20></font>'
parts.append(Paragraph(ptext, styles["Normal"]))


doc.build(parts)


