class String():
    def getstring(self,string):
        self.string=string

    def printstring(self):
        self.string1 = self.string.upper()
        print("String is",self.string1)


p=String()
p.getstring("anu")
p.printstring()