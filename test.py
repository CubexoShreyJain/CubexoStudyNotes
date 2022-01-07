from itertools import permutations
class Check():
    def __init__(self,string):
        self.string = string
        self.final_list = []
        self.terminate = False
        self.result = ''
        
    def get_anagram(self):
        # self.permute(list(self.string), 0, len(self.string))
        # if self.result == '':
        #     return "IMPOSSIBLE"
        # else:
        #     return self.result
    
        possibilities = [''.join(p) for p in permutations(self.string)]
        for i in possibilities:
            test = True
            for j in range(0,len(self.string)):
                if i[j] == self.string[j]:
                    test = False
                    break
            if (test):
                return i
        return "IMPOSSIBLE"
    
    def permute(self,data, i, length):
        if(self.terminate):
            return 
        elif i == length:
            test = True
            for index,k in enumerate(data):
                if (self.string[index] == k):
                    test = False
                    break
            if (test):
                self.terminate = True
                self.result = ''.join(data)  

        else:
            for j in range(i, length):
                # swap
                data[i], data[j] = data[j], data[i]
                self.permute(data, i + 1, length)
                data[i], data[j] = data[j], data[i] 


n = int(input())
for i in range(1,n+1):
    string = input()
    case = Check(string)
    print("Case #{}: {}".format(i,case.get_anagram()))
