# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(f_name):
    if f_name == "Joe":
        return "Warren"
    elif f_name == "Scott":
        return "Rixner"
    elif f_name == "John":
        return "Greiner"
    elif f_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"
        

###################################################
# Tests
# Student should not change this code.

def test(first_name):
    """Tests the name_lookup function."""
    
    print name_lookup(first_name)
    
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor
