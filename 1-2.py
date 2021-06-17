def parni(n):
    for i in range (1,n):
        if i%2==0:
            yield i
def neparni(n):
    for j in range (1,n):
        if j%2!=0:
            yield j
n = int(input("unesite broj: "))
print ("parni")
for i in parni(n):
    print (i)
    
print("neparni")
for i in neparni(n):
    print(i)



