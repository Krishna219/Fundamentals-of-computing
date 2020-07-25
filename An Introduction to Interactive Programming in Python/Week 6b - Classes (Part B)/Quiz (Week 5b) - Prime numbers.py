numbers = range(2, 1000)

results = []

while len(numbers) > 0:
    i = 0
    results.append(numbers[i])
    new_list = []
    for num_1 in numbers:
        if num_1 % numbers[i] != 0:
            new_list.append(num_1)
    numbers = new_list
    
print results
print len(results)    