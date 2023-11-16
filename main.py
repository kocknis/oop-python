allMoneysGrandpa = int(input("how mauch grandpa had money : "))
isAliveGrandma = input("is alive Grandma : y/n  ")
isAliveMother = input("is alive mother : y/n  ")
isAliveFather = input("is alive Father : y/n  ")
howManyDaughter = int(input("how many daughter does it has : "))
howManySons = int(input("how many sons does it has : "))


allShare = howManySons * 2 + howManyDaughter


    
fatherShare = 0
motherShare = 0

if isAliveGrandma == "y":
    grandmaShare = int(allMoneysGrandpa / 8)
    allMoneysGrandpa = allMoneysGrandpa - grandmaShare
elif isAliveGrandma == 'n':
    allMoneysGrandpa = allMoneysGrandpa

print(allMoneysGrandpa)


class Grandpa:
    def __init__(self, allMoney):
        self.allMoney = allMoney


class Grandma():
    def __init__(self, isAlive, allMoney, grandmaShare):
        self.isAlive = isAlive

    def heredity(self):
        print(grandmaShare)

class Father():
    def __init__(self, isAlive, parentsShare):
        self.isAlive = isAlive

    def heredity(self):
        print(parentsShare * 2)
        
class Mother():
    def __init__(self, isAlive, parentsShare):
        self.isAlive = isAlive

    def heredity(self):
        print(parentsShare)
class Son:
    def __init__(self, allMoney, howManySons, allShare):
        self.allMoney = allMoney
        self.howManySons = howManySons
        self.allShare = allShare

    def heredity(self):
        print(int((self.allMoney / allShare) * 2), end=" , ")



class Daughter:
    def __init__(self, allMoney, howManyDaughter, allShare):
        self.allMoney = allMoney
        self.howManySons = howManySons
        self.allShare = allShare

    def heredity(self):
        print(int(self.allMoney / allShare), end=" , ")


Ali = Grandpa(allMoneysGrandpa)

if isAliveMother == 'y' and isAliveFather == 'y':
    parentsShare = int(allMoneysGrandpa / 18)
    allMoneysGrandpa = allMoneysGrandpa - parentsShare
    father = Father(isAliveFather, parentsShare)
    mother = Mother(isAliveMother, parentsShare)

if howManySons != 0:
    sons = []
    for i in range(howManySons):
        son = Son(allMoneysGrandpa, howManySons, allShare)
        sons.append(son) 

if howManyDaughter != 0:
    daughters = []
    for i in range(howManyDaughter):
        daughter = Daughter(allMoneysGrandpa, howManyDaughter, allShare)
        daughters.append(daughter)


if isAliveGrandma == "y":
    soghra = Grandma(isAliveGrandma, allMoneysGrandpa, grandmaShare)
    soghra.heredity()



for son in sons:
    son.heredity()
    
print()

for daughter in daughters:
    daughter.heredity()
