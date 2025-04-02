class a:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self,i):
        self.i=4*i

class b(a):
    def __init__(self):
        super().__init__()
    def multiply(self,i):
        self.i=2*i

obj=b()