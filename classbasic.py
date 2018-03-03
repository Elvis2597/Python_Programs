class cars:
    def __init__(self):
        self.carno=0
        self.carname=''
        self.milage=0
    def retcno(self):
        return self.carno
    def showcar(self):
        print'Name of Car is', self.carname
        print'Milage is', self.milage
    def mycars(self):
        self.carname=raw_input('Enter Carname       :')
        self.milage=input('Enter milage        :')

car1=input('Enter How many cars :')
for i in range(car1):  
    c=cars()
    c.mycars()         
    if c.milage>=100 and c.milage<=150:
        c.showcar()


