a="sivaram"
b="ram"
print(a[0]+b[0])


a="SivaRam"
print(a[0]+a[4])
class Empname:
    def __init__(self,fname,lname):
        self.i=fname
        self.j=lname
    def Empadd(self):
        return self.i[0].upper()+self.j[0].upper()

a=Empname("siva","ram")
x=a.Empadd()
print(x)