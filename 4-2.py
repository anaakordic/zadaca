x = input("unesite ime: ")

def pozdrav(x):
    print("Pozdrav, ", x)
    
dobrodosao = lambda x: "dobrodošao, " + x
#print(dobrodosao(x))

def funkc(dobrodosao):
    return dobrodosao(x)

print(funkc(dobrodosao))
