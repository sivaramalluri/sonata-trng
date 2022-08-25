class Account:
    def __init__(self,acno,name,type,bal):
        self.acno=acno
        self.name=name
        self.type=type
        self.bal=bal
    def details(self,amount):
       return self.acno + self.name + self.type +self.bal


