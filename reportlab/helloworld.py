from reportlab.pdfgen import canvas 

# bottom to top 0-831 and left to right 0-581
c = canvas.Canvas("hello.pdf")  
c.drawString(581,831, "F")


c.showPage()  
c.save()