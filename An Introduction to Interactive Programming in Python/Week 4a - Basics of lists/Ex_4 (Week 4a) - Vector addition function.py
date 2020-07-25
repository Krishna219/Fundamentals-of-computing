# Vector addition function

###################################################
# Student should enter code below

def add_vector(vec1, vec2):
    res = [0, 0]
    res[0] = vec1[0] + vec2[0]
    res[1] = vec1[1] + vec2[0]
    return res


###################################################
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])



###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]

