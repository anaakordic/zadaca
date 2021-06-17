import re
txt = input("Unesi string: ") 
regex = "^a.*[0-5].*\s.*k$"
regex2 = "\s"
rez = re.search(regex, txt)
rez2 = re.search(regex2, txt)
if rez and rez2:
    print("uspjesan unos")
else:
    print("neuspjesan unos")
