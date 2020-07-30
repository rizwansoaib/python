import requests
from bs4 import BeautifulSoup
import os
import pdfkit


def data(roll):


    url='https://govexams.com/knit/knitExam/printApp.aspx?rno='+str(roll)
    response=requests.get(url).text
    #print(response)
    dhtm = BeautifulSoup(response)
    #print(dhtm)
    if response.count(str(roll))>2:
        print(roll,": Success")
        pdfkit.from_url(url,'exam/'+str(roll)+'.pdf')
    else:
        print(roll,": Failed")




#data(178208)



'''
for k in range(1,7):

        linear='16'+str(k)+'01'
        for i in range(int(linear),int(linear)+61):
            data(i) '''


for k in range(1,7):

        lateral='178'+str(k)+'01'
        for i in range(int(lateral),int(lateral)+13):
            data(i) 



       
