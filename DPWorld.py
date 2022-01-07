class Test:
    def __init__(self, n):
        self.n = n

    def result(self):
        pass


total_cases = int(input())
for i in range(total_cases):
    case_inputs = input()
    case = Test(*map(int, case_inputs.split()))

    print(f'Case #{i+1}: ', case.result())