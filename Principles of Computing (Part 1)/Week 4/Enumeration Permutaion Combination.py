"""
This program gives all possible Enumeration, Sorted Enumeration,
Permutaion, Combination (Sorted permutaion)
"""
def gen_all_sequences(outcomes, length):
    """
    Function gives all possible Enumerations of length (length)
    for the set of outcomes 
    """
    answer = set([tuple()])
    for dummy_idx in range(length):
        temp = set()
        for sequence in answer:
            for outcome in outcomes:
                new_sequence = list(sequence)
                new_sequence.append(outcome)
                temp.add(tuple(new_sequence))
        answer = temp
    return answer

def gen_sorted_sequences(outcome, length, permuted = False):
    """
    This Function gives sorted set of sequence
    """
    if permuted:
        all_sequences = gen_permuted_sequences(outcome, length)
    else:
        all_sequences = gen_all_sequences(outcome, length)
    sorted_sequences = [ tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def gen_permuted_sequences(outcomes, length):
    """
    This function generates all permuted sequences
    """
    answer = set([tuple()])
    for idx in range(length):
        temp = set()
        for sequence in answer:
            for outcome in outcomes:
                new_sequence = list(sequence)
                new_sequence.append(outcome)
                if len(set(new_sequence)) == (idx + 1):
                    temp.add(tuple(new_sequence))
        answer = temp
    return answer

def run_example():
    """
    This Function runs examples of enumerations, permutaions
    and combinations
    """
#    outcomes = ['Heads', 'Tails']
    outcomes = set([1, 2, 3, 4, 5, 6])
    length = 2
    
    print 'This is Enumeration'
    print 
    all_sequences = gen_all_sequences(outcomes, length)
    print str(len(all_sequences)) + ' sequences of outcome of length',
    print str(length) + ' was found.'
    print 'Sequences were', all_sequences
    print '----------------------------------------'    
    
    print 'This is Sorted Enumeration'
    print 
    sorted_sequences = gen_sorted_sequences(outcomes, length)
    print str(len(sorted_sequences)) + ' sequences of outcome of length',
    print str(length) + ' was found.'
    print 'Sequences were', sorted_sequences
    print '----------------------------------------'

    print 'This is Permutation'
    print 
    permuted_sequences = gen_permuted_sequences(outcomes, length)
    print str(len(permuted_sequences)) + ' sequences of outcome of length',
    print str(length) + ' was found.'
    print 'Sequences were', permuted_sequences
    print '----------------------------------------'
    
    print 'This is Combination (Sorted Permutaion)'
    print 
    sorted_sequences = gen_sorted_sequences(outcomes, length, True)
    print str(len(sorted_sequences)) + ' sequences of outcome of length',
    print str(length) + ' was found.'
    print 'Sequences were', sorted_sequences
    print '----------------------------------------'

run_example()