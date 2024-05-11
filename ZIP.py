s = ['name','age', 'package']
s2 = ['Shrey', 20 , 4000000]

data = {field:data  for (field, data) in zip(s, s2)}
print(data)