class trainer:
    def __init__(self,name,tId):
        self.name=name
        self.tId=tId
    def getname(self):
        return self.name
    def gettId(self):
       return self.tId
class learner:
    def __init__(self,lname,lId):
        self.lname=lname
        self.lId=lId
    def getlname(self):
        return self.lname
    def getlId(self):
        return self.lId
class institute(trainer,learner):
    def __init__(self,name,tId,lname,lId,Icode,Iname):
        trainer.__init__(self,name,tId)
        learner.__init__(self,lname,lId)
        self.Icode=Icode
        self.Iname=Iname
        
    def getIcode(self):
        print'INSTITUTE ID IS' ,self.Icode
        print 'Trainer id is',trainer.gettId(self)
        print 'Learner Id is',learner.getlId(self)
       
    def getIname(self):
        
        print'Institude Name is' ,self.Iname
        print 'Trainer Name is ',trainer.getname(self)
        print 'Learner Name is',learner.getlname(self)

s=institute('AMAN',9871,'GAURAV',5789,567,'BVM')
s.getIcode()
s.getIname()
