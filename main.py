allMoneysGrandpa = int(input("how mauch grandpa had money : "))
isAliveGrandma = input("is alive Grandma : y/n  ")
howManyDaughter = int(input("how many daughter does it has : "))
howManySons = int(input("how many sons does it has : "))


allShare = howManySons * 2 + howManyDaughter



if isAliveGrandma == "y":
    grandmaShare = allMoneysGrandpa / 8
    allMoneysGrandpa = allMoneysGrandpa - grandmaShare
elif isAliveGrandma == 'n':
    allMoneysGrandpa = allMoneysGrandpa

print(allMoneysGrandpa)


class Grandpa:
    def __init__(self, allMoney):
        self.allMoney = allMoney


class Grandma(Grandpa):
    def __init__(self, isAlive, allMoney, grandmaShare):
        super().__init__(allMoney)
        self.isAlive = isAlive

    def heredity(self):
        print(grandmaShare)


class Son:
    def __init__(self, allMoney, howManySons, allShare):
        self.allMoney = allMoney
        self.howManySons = howManySons
        self.allShare = allShare

    def heredity(self):
        print((self.allMoney / allShare) * 2, end=" , ")

    # def __round__(self):
    #     return round((self.allMoney / allShare) * 16)


class Daughter:
    def __init__(self, allMoney, howManyDaughter, allShare):
        self.allMoney = allMoney
        self.howManySons = howManySons
        self.allShare = allShare

    def heredity(self):
        print(self.allMoney / allShare, end=" , ")


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
