class Car:
     car_name="Farari"
     def car_data(self,name1):
          self.name1=name1
          print("Car name is {}".format(self.name1))


if __name__=="__main__":
 mycar=Car()
 mycar.car_data("Audi a4")