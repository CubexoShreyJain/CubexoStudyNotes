class Check:
    def __init__(self):
        self.br_si = False
        self.gold_plat = False
        self.diamond = False
        self.crown = False
        self.ace_con = False

    def check(self, category):

        if (category == "gold" or category == "platinum"):
            self.gold_plat = True
        elif (category == "ace" or category == "conqueror"):
            self.ace_con = True
        elif (category == "diamond"):
            self.diamond = True
        elif(category == "crown"):
            self.crown = True
        elif(category == "bronze" or category == "silver"):
            self.br_si = True

    def result(self):
        if (self.br_si and self.gold_plat and self.ace_con and self.diamond):
            print("Yes")
        else:
            print("No")


total_cases = int(input())
for i in range(total_cases):
    case_inputs = int(input())
    new = Check()
    for j in range(case_inputs):
        category = input()
        new.check(category)
    new.result()
