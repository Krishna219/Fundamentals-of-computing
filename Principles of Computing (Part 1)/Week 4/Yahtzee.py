"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    possible_scores = []
    for item in hand:
        possible_scores.append(item * hand.count(item))
#    print score
    return max(possible_scores)



def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = [ num + 1 for num in range(num_die_sides) ]
    outcomes = set(outcomes)
    
    all_sequences = gen_all_sequences(outcomes, num_free_dice)
    
#    print all_sequences
#    print len(all_sequences)
    
    expected_score = 0.0
    for seq in all_sequences:
        current_hand = list(held_dice)
        current_hand.extend(seq)
        expected_score += score(current_hand) / float(len(all_sequences))
#        print current_hand, expected_score
    
    return expected_score


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = [()]
    for dummy_idx in range(len(hand)):
        temp_set = []
        for partial_sequence in answer_set:
            for item in hand:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                if new_sequence.count(item) <= hand.count(item):
                    temp_set.append(tuple(sorted(new_sequence)))
        answer_set.extend(temp_set)
    return set(answer_set)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
#    print all_holds
    
    max_expected_value = 0
    
    for held_dice in all_holds:
#        print held_dice
#        print 
#        print expected_value(held_dice, num_die_sides, 5 - len(held_dice))
#        print 
        value = expected_value(held_dice, num_die_sides, len(hand) - len(held_dice))
        if value > max_expected_value:
            max_expected_value = value
            dice_to_hold = held_dice
    
    return (max_expected_value, dice_to_hold)



def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
#    hand = (1, 1, 1, 5, 6)
    hand = (1, )
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



