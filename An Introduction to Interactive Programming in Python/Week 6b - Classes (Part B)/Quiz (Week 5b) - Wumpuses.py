year = 1
slow_wumpuses = 1000
fast_wumpuses = 1

print "Year || Slow_wumpuses || Fast_wumpuses"
print year, slow_wumpuses, fast_wumpuses

while fast_wumpuses * 2 * 0.7 <=  slow_wumpuses * 2 * 0.6:
    year += 1
    fast_wumpuses *=  2 * 0.7
    slow_wumpuses *=  2 * 0.6
    print year, slow_wumpuses, fast_wumpuses

print year    