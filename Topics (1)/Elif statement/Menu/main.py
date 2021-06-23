menu = ['pizza', 'salad', 'soup']
variedad = ['Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy',
            'Caesar salad, Green salad, Tuna salad, Fruit salad',
            'Chicken soup, Ramen, Tomato soup, Mushroom cream soup']

pedido = input()
if pedido in menu:
    print(variedad[menu.index(pedido)])
else:
    print("Sorry, we don't have it in the menu")
