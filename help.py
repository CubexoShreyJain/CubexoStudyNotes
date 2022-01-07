# def dictchk(x):
#     result = {}
#     keys_List = x.keys()
#     for i in (0,len(keys_List)):
#         if (("k" in keys_List[i]) or ("K" in keys_List[i])) :
#             result[keys_List[i]] = x[keys_List[i]]
#     return result
# input_dict = {'k1':1,'y2':2,'k3':3,'y4':4,'k5':5}
# w = {'k1': 1, 'k3': 3, 'k5': 5}
# print(dictchk(input_dict))
# print(w==dictchk(input_dict))





















def listchk(alist,n):
    a = 0
    result_list = []
    for i in alist:
        if (a%2 == 0):
            if (i<n):
                result_list.append(i)
        a += 1

    return result_list


a = ('sfg','rfg',-4,5.0,6,7)
print(list(a))




