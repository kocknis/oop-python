allMoneysGrandpa = int(input("how mauch grandpa had money : "))
isAliveGrandma = input('is alive Grandma : y/n  ')
howManyDaughter = int(input('how many daughter does it has : '))
howManySons = int(input("how many sons does it has : "))
# isMarriedSons = []
# for i in range(howManySons):
#     isMarriedSon = input(f'is Married Son {i + 1} : y/n  ')
#     isMarriedSons.append(isMarriedSon)

sonShare = 16
daugtherShare = 8
grandmaShare = 1


class Grandpa:
    def __init__(self, allMoney):
        self.allMoney = allMoney


class Grandma(Grandpa):
    def __init__(self, isAlive, allMoney, grandmaShare):
        super().__init__(allMoney)
        self.isAlive = isAlive

    def heredity(self):
        print(self.allMoney)


class Son:
    def __init__(self, isMarried, allMoney, howManySons, sonShare):
        self.allMoney = allMoney
        self.isMarried = isMarried
        self.howManySons = howManySons
        self.sonShare = sonShare

    def heredity(self):
        print(self.allMoney / (howManySons * sonShare))


class Daugther:
    def __init__(self, allMoney, howManyDaugther, daugtherShare):
        self.allMoney = allMoney
        self.howManySons = howManySons
        self.daugtherShare = daugtherShare

    def heredity(self):
        print(self.allMoney / (howManySons * daugtherShare))


Ali = Grandpa(allMoneysGrandpa)

if howManySons != 0:
    sons = []
    for i in range(howManySons):
        son = Son(False, allMoneysGrandpa, howManySons, sonShare)
        sons.append(son)
    
if howManyDaughter != 0:
    duaghters = []
    for i in range(howManyDaughter):
        daughter = Daughter(allMoneysGrandpa, howManyDaughter, daugtherShare)
        daughters.append(daughter)
    

if isAliveGrandma == 'y' or 'yes':
    soghra = Grandma(isAliveGrandma, allMoneysGrandpa, grandmaShare)
    soghra.heredity()

for son in sons:
    son.heredity()
