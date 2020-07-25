# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(num):
    if num < 0 or num >= 100:
        print "Error: Input is not a two digit number"
    else:
        tens_digit = num // 10
        ones_digit = num % 10
        print "The tens digit is "+str(tens_digit)+" and the ones digit is "+str(ones_digit)+"."
    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.
