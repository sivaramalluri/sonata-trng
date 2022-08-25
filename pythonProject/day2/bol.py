from leave import Leave
class bof(Leave):
    def __init__(self,a_id,b_name,c_balance,Applyleave):
        super(bof,self).__init__(a_id,b_name,c_balance)
    def disleave(self):
        return self.c_balance-self.Applyleave

