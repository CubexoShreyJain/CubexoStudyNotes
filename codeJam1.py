class Test:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def driver(self):

        for i in range(2*self.r + 1):
            for j in range(2*self.c + 1):

                if ((i == 0 or i == 1) and (j == 0 or j == 1)):
                    print(".", end="")

                else:
                    if (i % 2 == 0):
                        if (j % 2 == 0):
                            print("+", end="")
                        else:
                            print("-", end="")
                    else:
                        if (j % 2 == 0):
                            print("|", end="")
                        else:
                            print(".", end="")
            print()
        return


total_cases = int(input())
for i in range(total_cases):

    r, c = map(int, input().split())  # double input
    # use *(anyList) - to supply all elements as individual parameters
    case = Test(r, c)
    print(f'\nCase #{i+1}:')
    case.driver()
