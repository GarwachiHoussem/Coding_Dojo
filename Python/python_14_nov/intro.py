class Car:
    #!Constructor
    def __init__(self,model_value,make_value,power_value,color_value = True):
        #Attributes
        #Attributes
        self.miles= 0
        self.model = model_value
        self.make = make_value
        self.power = power_value
        self.color = color_value
        
    #! Methods
# object = Car (values)
tesla = Car("X1","Tesla","10", "red")
print("First Car Object:", tesla)
print(f"MODEL:,{tesla.model}\nMake: {tesla.make}\nCOLOR:{tesla.color}")