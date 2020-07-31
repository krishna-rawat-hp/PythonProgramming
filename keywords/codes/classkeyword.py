class Myclass: #class definition
    greet = "Hello "

    def greet_func(self, name):
        print(self.greet + name)

obj = Myclass() #creating class object
obj.greet_func("Krishna") #call class method using object
