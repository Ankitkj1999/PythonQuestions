order_menu = {"apple": 10,
                  "mango": 20,
                  "banana": 30,
                  "orange": 40,
                  "grapse": 50
                  }
ordered_items = list()
ordered_prices = list()
while True:
    item_name = str.lower(input('ENTER ITEM NAME (e TO EXIT ANY TIME):  '))
    if item_name != str.casefold('e'):
        if item_name in order_menu:
            ordered_items.append(item_name)
            ordered_prices.append(order_menu[item_name])
            print(ordered_items)
            print(ordered_prices)
        else:
            print('ITEM DOES NOT EXIST IN THE MENU')
            continue
    else:
        break

# Calculating the total price for the ordered items
total_amount = 0
for x in ordered_prices:
    total_amount += x

print('\n\nBILL SUMMARY')
print('ORDERED ITEMS:  {}\nPRICES:  {}\n\nTOTAL PRICE:  Rs. {}'.format(ordered_items, ordered_prices,total_amount))

"""
Firstly I am making a function find. Inside function i created a dictionary dict in which sweets1,sweets2 , 
sweets3, sweets4, and sweets5 are keys which i take as menu and,10,20,30,40 and 50 are values which i take 
as price respectively. Now we are taking order from the customers. If my order is from given menu then 
we are taking it and giving total bill  for which i used total_amount. If it is not present in it then 
we are again asking the customers to re-enter the menu from dictionary. We use q to quit . This way, at 
any time, the user can type "q" and hit enter to quit . We also use casefold. The casefold() method is an 
aggressive lower() method which converts strings to case folded strings for caseless matching.
   At last we are printing bill summary and total amount
   """