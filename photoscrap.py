import requests
import os

def dimg(k,i):

    f = open(str(k)+'/Photo/'+str(i)+'.jpg','wb')

    f.write(requests.get('http://192.168.7.100/kniterp/Student_Doc/'+str(i)+'/Photo.jpg').content)
    f.close()
def dsig(k,i):

        f = open(str(k)+'/Sign/'+str(i)+'.jpg','wb')
        f.write(requests.get('http://192.168.7.100/kniterp/Student_Doc/'+str(i)+'/Sign.jpg').content)
        f.close()



for k in range(1,7):
        os.system('mkdir '+str(k))
    

        os.system('mkdir '+str(k)+'/Photo')
        os.system('mkdir '+str(k)+'/Sign')

        linear='18'+str(k)+'01'
        for i in range(int(linear),int(linear)+60):
            dimg(k,i)
            dsig(k,i)
            print(str(i) +" Sucess")

       
