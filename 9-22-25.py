# flowchart in python 
money_input = int(input('enter how much money u have: $'))
#snacks = [1,2,3,4,5,6,7,8,9,10]
Snacks = [[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[10,2]]
        
snacks_input = int(input('enter snack number'))
if money_input:
    money = money_input
    if snacks_input:
        snack = snacks_input
        price = 2
        if money < 2:
              print('not enough money. u broke')
        elif money == 2:
              print('snack dispensed')
        elif money > 2:
             print(f'snack and ${money-2} returned')
        else:
             print('error')