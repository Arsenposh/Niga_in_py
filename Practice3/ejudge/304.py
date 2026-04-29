class StringHandler:
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

sh = StringHandler()
sh.getString()
sh.printString()