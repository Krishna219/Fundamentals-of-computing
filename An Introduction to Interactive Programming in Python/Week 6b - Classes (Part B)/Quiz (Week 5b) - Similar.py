def list_extend_many(lists):
    result = []
    for i in range(len(lists)):
        result.extend(lists[i])
    return result

#def list_extend_many(lists):
#    result = []
#    i = len(lists)
#    while i >= 0:
#        i -= 1
#        result.extend(lists[i])
#    return result

#def list_extend_many(lists):
#    result = []
#    i = 0
#    while i <= len(lists): 
#        result.extend(lists[i])
#        i += 1
#    return result

#
#def list_extend_many(lists):
#    result = []
#    i = 0
#    while i < len(lists): 
#        result.extend(lists[i])
#        i += 1
#    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])