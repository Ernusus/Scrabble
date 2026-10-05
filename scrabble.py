vardnica={
    'a' : 1,
    'ā' : 4,
    'b' : 2,
    'c' : 3,
    'č' : 8,
    'd' : 2,
    'e' : 1,
    'ē' : 5,
    'f' : 4,
    'g' : 2,
    'ģ' : 5,
    'h' : 3,
    'i' : 1,
    'ī' : 4,
    'j' : 3,
    'k' : 2,
    'ķ' : 5,
    'l' : 2,
    'ļ' : 4,
    'm' : 2,
    'n' : 2,
    'ņ' : 4,
    'o' : 1,
    'p' : 3,
    'r' : 2,
    's' : 1,
    'š' : 5,
    't' : 1,
    'u' : 1,
    'ū' : 8,
    'v' : 1,
    'z' : 1,
    'ž' : 8
    }

vards = input("Ievadiet savu vardu: ")

def parbaudit(word):
    summa = 0
    for burts in word:
        if burts in vardnica.keys():
            summa+=vardnica[burts]
    return summa 

resultats = parbaudit(vards)


print(f"Par šo vardu jus dabujat {resultats} punkti")