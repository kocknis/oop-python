
  
# howManyDaughter = int(input('how many daughter does it has : '))
allMoneysGrandpa = int(input('how mauch grandpa had money : '))
# isAliveGrandma = input('is alive Grandma : y/n  ')
howManySons = int(input('how many sons does it has : '))
# isMarriedSons = []
# for i in range(howManySons):
#     isMarriedSon = input(f'is Married Son {i + 1} : y/n  ')
#     isMarriedSons.append(isMarriedSon)

class Grandpa:
    def __init__(self, allMoney):
        self.allMoney = allMoney
  
class Grandma(Grandpa):
    def __init__(self, isAlive, allMoney):
        super().__init__(allMoney)
        self.isAlive = isAlive 

    def heredity(self):
        print(self.allMoney)
    
    
class Son:
    def __init__(self, isMarried, allMoney):
        self.allMoney = allMoney
        self.isMarried = isMarried
    
    def heredity(self):
        print(self.allMoney)

allMoneysGrandpa = int(input('how mauch grandpa had money : '))
# isAliveGrandma = input('is alive Grandma : y/n  ')
howManySons = int(input('how many sons does it has : '))
# isMarriedSons = []
# for i in range(howManySons):
#     isMarriedSon = input(f'is Married Son {i + 1} : y/n  ')
#     isMarriedSons.append(isMarriedSon)
  
Ali = Grandpa(allMoneysGrandpa)
soghra = Grandma(True, allMoneysGrandpa)
sons = []
for i in range(howManySons):
    son = Son(False, allMoneysGrandpa)
    sons.append(son)

soghra.heredity()
for son in sons:
    son.heredity()
