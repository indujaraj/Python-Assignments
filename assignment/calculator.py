class Calculator():
    def add(self,num1,num2):
       return num1+num2
    def sub(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print("Sum is", self.num1 - self.num2)
