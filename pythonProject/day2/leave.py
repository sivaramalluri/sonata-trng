class Leave:
    def __init__(self,a_id,b_name,c_balance):
        self.eid=a_id
        self.ename=b_name
        self.el=c_balance
    def dis(self):
        return self.eid,self.ename,self.el
