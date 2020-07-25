my_game = ClickerState()

print my_game

print my_game.get_cookies()
print my_game.get_cps()
print my_game.get_time()
print my_game.get_history()

print my_game.time_until(15)

my_game.wait(my_game.time_until(15))

print my_game

my_game.buy_item("Curser", 15.0, 0.1)
print my_game

print my_game.time_until(10)

my_game.wait(78)

print my_game

my_game.buy_item("Curser", 15.0, 0.1)
my_game.buy_item("Curser", 15.0, 0.1)
my_game.buy_item("Curser", 15.0, 0.1)

print my_game

