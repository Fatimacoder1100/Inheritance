class vehicle:
    def __init__ (self,name,max_speed,mileaege):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileaege
class bus(vehicle):
    pass
school_bus = bus("School Volvo",180,20)
print("Vehicle Name:",school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)