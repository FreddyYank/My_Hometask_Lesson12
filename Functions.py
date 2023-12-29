class House():
    def __init__(self, a,b,c,d,):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def min(self):
        if self.a > self.b:
            self.a = self.b
        if self.c > self.d:
            self.c = self.d
        if self.a > self.c:
            self.a = self.c
        print(self.a)

House1 = House(1,2,3,4)
print(House1.min())

def xet(x):
    if x % 2 == 0:
        print("Четное!")
    else:
        print("Нечетное!")





