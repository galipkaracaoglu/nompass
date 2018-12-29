class Place:

    def __init__(self,adress,lat,lot,name,general_point):



        self.name=name
        self.adress=adress
        self.lat=lat
        self.lot=lot
        self.general_point = general_point
    
    def __str__(self):
        return self.name + " " + self.adress
 



