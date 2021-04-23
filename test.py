    while P1.hp != 0 or P2.hp != 0:
        print(List.insultes)


def grammaire ():
    for i in sujetlist:
        if i == userchoice :
            continue
        else :
            insultepower -= -1
            print("Bad grammar !")
            continue
    for i in verbelist:
        if i == userchoice:
            continue
        else :
            insultepower -= -1
            print("Bad grammar !")
            continue
    for i in complement :
        if i == userchoice:
            continue
        else :
            insultepower -= -1
            print("Bad grammar !")
            continue

def weaknesscalc(self):
    for i in weakness.P2:
        if i == sujet :
            insultepower += 1
        if i == verbe :
            insultepower += 1
        if i == complement :
            insultepower += 1
    
    for i in weakness.P1:
        if i == sujet :
            insultepower += 1
        if i == verbe :
            insultepower += 1
        if i == complement :
            insultepower += 1