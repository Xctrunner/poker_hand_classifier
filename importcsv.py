import csv
import numpy

def strs_to_int(list):
    result = []
    for i in list:
        result.append(int(i))
    return result

def hand_process(hand):
    hand = strs_to_int(hand)
    result_hand = []
    for i in range(11):
        if i % 2 == 1:
            result_hand.append(13*(hand[i-1]-1)+hand[i]-1)
    result_hand.append(hand[10])
    return result_hand

def open_card_csv(filename):
    with open(filename, 'r') as trainset:
        handreader = csv.reader(trainset)
        hands = []
        for hand in handreader:
            p_hand = hand_process(hand)
            hands.append(p_hand);
        del hands[0]
        return hands


# takes a hand in which cards are ints from 
def hand_to_binary_t(hand):
    input_d = numpy.zeros((52,1))
    for i in range(len(hand)-1):
        input_d[hand[i]] = 1.0
    exp_output = numpy.zeros((10,1))
    exp_output[hand[-1]] = 1.0
    return input_d, exp_output

def hand_to_binary_vr(hand):
    input_d = numpy.zeros((52,1))
    for i in range(len(hand)-1):
        input_d[hand[i]] = 1.0
    return input_d, hand[-1]
    

def csv_to_binary(filename):
    t_h = []
    v_h = []
    r_h = []
    init_hands = open_card_csv(filename)
    for i in range(len(init_hands)):
        if i < 15000:
            t_h.append(hand_to_binary_t(init_hands[i]))
        elif i < 20000:
            v_h.append(hand_to_binary_vr(init_hands[i]))
        else:
            r_h.append(hand_to_binary_vr(init_hands[i]))
    return (t_h,v_h,r_h)

## t,v,r = csv_to_binary('train.csv')

