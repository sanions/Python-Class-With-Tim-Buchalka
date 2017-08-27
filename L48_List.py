
menu = []
menu.append(['egg', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

print(menu)

for meal in menu:
    if 'spam' not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
