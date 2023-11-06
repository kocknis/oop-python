allMoneysGrandpa = int(input("how mauch grandpa had money : "))
isAliveGrandma = input('is alive Grandma : y/n  ')
howManyDaughter = int(input('how many daughter does it has : '))
howManySons = int(input("how many sons does it has : "))
# isMarriedSons = []
# for i in range(howManySons):
#     isMarriedSon = input(f'is Married Son {i + 1} : y/n  ')
#     isMarriedSons.append(isMarriedSon)

# sonShare = 16
# DaughterShare = 8
# grandmaShare = 1

allShare = howManySons * 16 + howManyDaughter * 8 + 1

class Grandpa:
    def __init__(self, allMoney):
        self.allMoney = allMoney


class Grandma(Grandpa):
    def __init__(self, isAlive, allMoney, allShare):
        super().__init__(allMoney)
        self.isAlive = isAlive

    def heredity(self):
        print((self.allMoney / allShare))


class Son:
    def __init__(self, isMarried, allMoney, howManySons, allShare):
        self.allMoney = allMoney
        self.isMarried = isMarried
        self.howManySons = howManySons
        self.allShare = allShare

    def heredity(self):
        print((self.allMoney / allShare) * 16 * howManySons)


class Daughter:
    def __init__(self, allMoney, howManyDaughter, allShare):
        self.allMoney = allMoney
        self.howManySons = howManySons
        self.allShare = allShare

    def heredity(self):
        print((self.allMoney / allShare) * 8 * howManyDaughter)


Ali = Grandpa(allMoneysGrandpa)

if howManySons != 0:
    sons = []
    for i in range(howManySons):
        son = Son(False, allMoneysGrandpa, howManySons, allShare)
        sons.append(son)
    
if howManyDaughter != 0:
    daughters = []
    for i in range(howManyDaughter):
        daughter = Daughter(allMoneysGrandpa, howManyDaughter, allShare)
        daughters.append(daughter)
    

if isAliveGrandma == 'y' or 'yes':
    soghra = Grandma(isAliveGrandma, allMoneysGrandpa, allShare)
    soghra.heredity()

for son in sons:
    son.heredity()

for daughter in daughters:
    daughter.heredity()