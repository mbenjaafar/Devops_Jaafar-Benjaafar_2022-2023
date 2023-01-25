class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def myLocation(self):
        print("My name is " + self.name + " and i live in " + self.country + ".")

loc = Location("Dzmitry", "Belgie")
#print(loc.name)
#print(loc.country)
#print(type(loc))

loc1 = Location("Thomas", "Portugal")
loc1.myLocation()

loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")

loc2.myLocation()
loc3.myLocation()

loc4 = Location("Dzmitry", "Kunitski")
loc4.myLocation()
