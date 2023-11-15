allMoneysGrandpa = int(input("how mauch grandpa had money : "))
isAliveGrandma = input("is alive Grandma : y/n  ")
howManyDaughter = int(input("how many daughter does it has : "))
howManySons = int(input("how many sons does it has : "))


allShare = howManySons * 2 + howManyDaughter

fatherShare = 0

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
        super().__init__(allMoney)
        self.isAlive = isAlive

    def heredity(self):
        print(grandmaShare)

class Father():
    def __init__(self, isAlive, fatherShare):
        self.isAlive = isAlive

    def heredity(self):
        print(fatherShare)
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
