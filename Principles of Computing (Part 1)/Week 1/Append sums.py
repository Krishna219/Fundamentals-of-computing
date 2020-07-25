"""
This program continuously appends the sum of last three elements of the list
to the last element (additional element)
"""
def appendsums(lst):
    """
    function appends the sum of last three elements of lst to lst
    """
    for dummy_num1 in range(25):
        lst_copy = list(lst)
        lst_3_sum = 0
        for dummy_num2 in range(3):
            lst_3_sum += lst_copy.pop()
        lst.append(lst_3_sum)
        
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[10]
print sum_three[20]