def triangular_sum(num):
    """
    Sum of n numbers
    """
    if num == 0:
        #base case
        return 0
    else:
        return num + triangular_sum(num - 1)
        #recursive case
for i in range(11):   
    print triangular_sum(i)
    
def number_of_threes(num):
    if num//10 == 0:
        if num == 3:
            return 1
        else:
            return 0
    else:
        if num%10 == 3:
            return 1 + number_of_threes(num//10)
        else:
            return number_of_threes(num//10)
    
print number_of_threes(3453433)

def is_member(my_list, elem):
    if len(my_list) == 1:
        return my_list[0] == elem
    else:
        if elem == my_list[0]:
            return True
        else:
            return is_member(my_list[1:], elem)

print is_member(['c', 'a', 't'], 'q') 

def remove_x(my_string):
    if len(my_string) == 1:
        if my_string == 'x':
            return ""
        else:
            return my_string
    else:
        if my_string[0] == 'x':
            return remove_x(my_string[1:])
        else:
            return my_string[0] + remove_x(my_string[1:])
        
print remove_x("catxxdogx")

def insert_x(my_string):
    if len(my_string) == 2:
        return my_string[0] + "x" + my_string[1]
    else:
        return my_string[0] + "x" + insert_x(my_string[1:])
    
print insert_x("catdog")

def list_reverse(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        return [my_list[-1]] + list_reverse(my_list[0:-1])
    
print list_reverse([2, 3, 1])
    
def gcd(num1, num2):
    if num2 > num1:
        return gcd(num2, num1)
    else:
        if num2 == 0:
            return num1
        else:
            return gcd(num2, num1 - num2)

print gcd(1071, 462)

def slice(my_list, first, last):
    if first > len(my_list) or last > len(my_list) or first >= last:
        return []
    else:
        first_elem = my_list[first]
        print first_elem
        return [first_elem] + slice(my_list, first + 1, last)
    
print slice(['a', 'b', 'c', 'd', 'e'], 2, 4)
print slice([10,21,34,56,78,90,101,23,45,67,89], 5, 9), [10,21,34,56,78,90,101,23,45,67,89]
        
