def buy(water,milk,coffee,disposable,money):
    tab()
    Untab()
    Untab()
    Untab()
    print("#                             What do you want to buy?                          #")
    Untab()
    Untab()
    Untab()
    print("#                              1 - espresso                                   #")
    print("#                              2 - latte                                    #")
    print("#                              3 - cappuccino                            #")
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    tab()

    buy = 0
    while not (buy in ['1', '2','3']):
        buy = input("What do you want to buy?")
    buy = int(buy)
    tmp = {
        1 : {
            'name' : 'espresso',
            'water': 250,
            'milk' : 0 ,
            'coffee':16,
            'noney':4
        },
        2 : {
            'name' : 'latte',
            'water': 350,
            'milk': 75 ,
            'coffee': 20,
            'noney': 7
        },
        3 : {
            'name': 'cappuccino',
            'water': 200,
            'milk': 100,
            'coffee': 12,
            'noney': 6
        }
    }

    water -=tmp[buy]['water']
    milk -= tmp[buy]['milk']
    coffee -= tmp[buy]['coffee']
    disposable -= 1
    money += tmp[buy]['noney']

    lists(water, milk, coffee, disposable, money)

def fill(water,milk,coffee,disposable,money):
    tmp_water = input('Write how ml of water do you want to add:')
    tmp_milk = input('Write how ml of milk do you want to add:')
    tmp_coffee = input('Write how grams of coffee beans do you want to add:')
    tmp_disposable = input('Write how disposable cups of coffee do you want to add:')
    
    water += int(tmp_water)
    milk += int(tmp_milk)
    coffee += int(tmp_coffee)
    disposable += int(tmp_disposable)

    lists(water, milk, coffee, disposable, money)

def take(water,milk,coffee,disposable,money):
    
    print("I gave you $550")
    money = 0
    lists(water, milk, coffee, disposable, money)
    
def tab():
    print('###############################################################################')
def Untab():
    print('#                                                                             #')
def lists(water,milk,coffee,disposable,money):
    tab()
    Untab()
    Untab()
    Untab()
    print("#                             The coffee machine has                          #")
    Untab()
    Untab()
    Untab()
    print("#                              {} of water                                   #".format(water))
    print("#                              {} of milk                                    #".format(milk))
    print("#                              {} of coffee beans                            #".format(coffee))
    print("#                              {} of disposable cups                         #".format(disposable))
    print("#                              {} of money                                   #".format(money))
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    Untab()
    tab()

water = 400
milk = 540
coffee = 120
disposable = 9
money = 550

status = True ;
while status :
    lists(water,milk,coffee,disposable,money)

    action = True
    while not(action in ['buy','fill','take']):
        action = input("Write action  (buy,fill,take) : ").strip()
    if action == 'buy':
        buy(water,milk,coffee,disposable,money)
    elif action == 'fill':
        fill(water,milk,coffee,disposable,money)
    else :
        take(water,milk,coffee,disposable,money)

    status = input()
    status = status.lower()
    if status == 'exit':
        status = False
    else :
        status = True
