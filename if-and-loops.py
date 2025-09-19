# atm machine example
# pin = '4657'
# entered_pin = input('enter pin: ')
# if pin == entered_pin:
#     print('access allowed')
#     money = 1000
#     while money > 0:
#         print('withdrawal allowed')
#         print(f'money left ${money}')
#         withdraw = input('how much do u want to withdraw? if u wanna stop, type STOP: ')
#         if withdraw == 'STOP':
#             break
#         elif money == int(withdraw):
#             money = 0
#             break
#         else:
#             money= money-int(withdraw)
#     else:
#         print('u broke no money left')
# else: 
#     print('invalid pin')
        
password = 'BCTS2025'
entered_password = input('enter password: ')
tries = 3
while password != entered_password:
    if password == entered_password:
        print('welcome')
        break 
    elif tries == 0:
        print("u've reached max # of tries. account blocked.")
        break
    else:
        tries= tries-1
        print(f'try again. tries left: {tries+1}')
        entered_password = input('enter password: ')
else:
    if password == entered_password:
        print('welcome')
    else:
        print("u've reached max # of tries. account blocked.")