import time

import wizard
import dragon

response = str(input("Hello, what's your name ?\n"))
w1 = wizard.Wizard(response ,500, 500, 100, 100, 200,3)
d1 = dragon.Dragon(500, 200, 100, 100, 200)
endofWhile = False

w1.showStat()
# d1.showStat()
while endofWhile != True:
    ##Tour du wizard
    goodResponse = False
    while goodResponse == False:
        response = str(input("What do you want to do "+ w1.name +"? \n 1 - Attack ; 2 - Take a potion ; 3 - Launch a fate \n"))
        if response != "1" and response != "2" and response != "3":
            print("Error, this is not a valid choice !!")
        else:
            goodResponse = True
            if response == "1":
                if d1.dragonChoice() == "1":
                    d1.life_pt = d1.life_pt - d1.dragonDefense(w1.atk_pt)
                    d1.showStat()
                elif d1.dragonChoice() == "2":
                    d1.life_pt = d1.life_pt - d1.dragonDodge(w1.atk_pt)
                    d1.showStat()
                else:
                    d1.life_pt = w1.wizardAttack(d1.life_pt)
                    print("Dragon do nothing...")
                    d1.showStat()
            elif response == "2":
                w1.takePotion()
                w1.showStat()
            else:
                w1.launchSpell()
                w1.showStat()

## Vérifie si les deux adversaire sont toujours debout
    if d1.life_pt <= 0:
        endofWhile = True
        print("             xxxxxxxxxxxxx\n")
        print("             You win \n")
        print("             xxxxxxxxxxxxx\n")
        break
    elif w1.life_pt < 0 or w1.mana_pt < 0:
        endofWhile = True
        print("             xxxxxxxxxxxxx\n")
        print("             You loose \n")
        print("             xxxxxxxxxxxxx\n")
        break



    ##Tour du dragon
    goodResponse = False
    while goodResponse == False:
        print("Dragon attack \n")
        response = str(input("What do you want to do ? \n 1 - Defense; 2 - Dodge ; 3 - Take a potion \n"))
        if response != "1" and response != "2" and response != "3":
            print("Error, this is not a valid choice !!")
        else:
            goodResponse = True
            if response == "1":
                w1.life_pt = w1.life_pt - w1.wizardDefense(d1.atk_pt)
                w1.showStat()
            elif response == "2":
                w1.life_pt = w1.life_pt - w1.wizardDefense(d1.atk_pt)
                w1.showStat()
            else:
                w1.takePotion()
                w1.life_pt
                w1.showStat()

    ## Vérifie si les deux adversaire sont toujours debout
    if d1.life_pt <= 0:
        endofWhile = True
        print("You win \n")
        break
    elif w1.life_pt < 0 or w1.mana_pt < 0:
        endofWhile = True
        print("             xxxxxxxxxxxxx\n")
        print("             You loose \n")
        print("             xxxxxxxxxxxxx\n")
        break