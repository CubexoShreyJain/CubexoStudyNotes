f1=open("prashasya.txt",'w') 
str="Good morning \n""This is cp3 Assignment""\nHello"
f1.write(str) 
f1.close() 
 
f1=open("prashasya.txt",'r')    #open created file in read mode f2=open("D:\c2.txt",'w')    #open another file in write mode st=f1.readlines()           #content of 1st file converted to list 
 
def listToString(s):       
    str1 = " "  
    return (str1.join(s)) 
 
stt=listToString(str)        #list converted to string 
 
 
f2=open("c2.txt",'w')
f2.write(stt)               #write string in 2nd file f1.close() f2.close() 
print(f2.read()) 
f2.close()