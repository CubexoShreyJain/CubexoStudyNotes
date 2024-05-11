class Printer:
    def __init__(self, c, m, y, b):
        self.c = c
        self.m = m
        self.y = y
        self.b = b

    def display(self):
        print("SEE IT")
        print(self.c, self.m, self.y, self.b)


class Main:

    def __init__(self, p1, p2, p3):

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.total = 0

    def driver(self):

        c, m, y, b = 0, 0, 0, 0

        c = self.check(min(self.p1.c, self.p2.c, self.p3.c))
        m = self.check(min(self.p1.m, self.p2.m, self.p3.m))
        y = self.check(min(self.p1.y, self.p2.y, self.p3.y))
        b = self.check(min(self.p1.b, self.p2.b, self.p3.b))

        return c, m, y, b

    def check(self, c):

        if (c < (1000000 - self.total)):
            self.total += c
            return c
        else:
            c = 1000000 - self.total
            self.total += c
            return c


total_cases = int(input())
for i in range(total_cases):
    p1, p2, p3 = None, None, None
    for j in range(3):
        c, m, y, b = map(int, input().split())
        exec("p"+str(j+1)+" = Printer(c, m, y, b)")
    # p1.display()
    # p2.display()
    # p3.display()
    main = Main(p1, p2, p3)
    c, m, y, b = main.driver()

    print(f'Case #{i+1}: ', end="")

    if (c+m+y+b != 1000000):
        print("IMPOSSIBLE")
    else:
        print(c, m, y, b)
