from leave import Leave
class restrictedleave(Leave):
    def __init__(self,a_id,b_name,c_balance,dob):
        super().__init__(a_id,b_name,c_balance)
        self.dob=dob
    def dis_dob(self):
        return self.dob