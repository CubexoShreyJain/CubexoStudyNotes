class exam:
    def __init__(self, n, k, s):
        self.n = n
        self.k = k
        self.s = s
        # print(self.n, self.k, self.s)

    def minTime(self):
        t1 = self.k + self.n
        t2 = (self.k-1) + (self.k-self.s)+(self.n-self.s+1)
        if (t1 <= t2):
            # print("t1")
            return t1
        else:
            return t2 


test = int(input())
for i in range(test):
    case = input()
    # print(*map(int, case.split()))
    a = exam(*map(int, case.split()))

    print(f'Case #{i+1} : ', a.minTime())

