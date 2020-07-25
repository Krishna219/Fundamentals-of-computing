"""
Analyzing a simple dice game
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits


def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    item_count = [seq.count(item) for item in seq]
    return max(item_count)


def compute_expected_value():
    """
    Function to compute expected value of simple dice game
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    
    all_sequences = gen_all_sequences(outcomes, 3)
    
    # variables that hold number of times an event has occured
    event = { 1 : 0, 2 : 0, 3 : 0}
    
    for sequence in all_sequences:
        if (max_repeats(sequence) == 3):
            event[3] += 1
        elif (max_repeats(sequence) == 2):
            event[2] += 1
        elif (max_repeats(sequence) == 1):
            event[1] += 1
            
#    print all_sequences
#    print len(all_sequences)
#    print event     
    
    #variables that hold the probabilities of events
    probability = { 1 : 0, 2 : 0, 3 : 0}
    probability[3] = event[3] / float(len(all_sequences))
    probability[2] = event[2] / float(len(all_sequences))
    probability[1] = event[1] / float(len(all_sequences))
    
#    print probability
    
    expected_value = probability[2] * 10 + probability[3] * 200
    return expected_value

def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
#    outcomes = set([1, 2, 3, 4, 5, 6])
#    print "All possible sequences of three dice are"
#    print gen_all_sequences(outcomes, 2)
#    print
#    print "Test for max repeats"
#    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
#    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
#    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value()
#    compute_expected_value()
    
run_test()
