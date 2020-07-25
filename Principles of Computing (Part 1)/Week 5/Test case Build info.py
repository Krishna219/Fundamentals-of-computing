my_class = BuildInfo()

your_class = my_class.clone()

print my_class

print my_class.build_items()

for item in my_class.build_items():
#    print my_class.get_cost(item), my_class.get_cps(item) 
    my_class.update_item(item)
    print my_class.get_cost(item), my_class.get_cps(item)
    print your_class.get_cost(item)
    print

my_game = BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15)

print my_game.build_items()

for item in my_game.build_items():
    print my_game.get_cost(item)

