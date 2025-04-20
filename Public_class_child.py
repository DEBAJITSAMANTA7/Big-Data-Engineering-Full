# Public access specifier so it can use any where even fror diffen file location also
from Public_class import Car
# from Public_class import Car as CarClass

class Check_car(Car):
     car_name="Audi"


if __name__=="__main__":
     debjit_obj=Check_car()
     print( debjit_obj.car_name) 
     debjit_obj.car_data("Hundai Creata")