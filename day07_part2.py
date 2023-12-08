from collections import Counter


with open('inputs/day07.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


card_hands = []
for line in lines:
    hand, bid = line.split()
    card_hands.append([hand,int(bid)])


card_hands_new = []
for hand, bid in card_hands:
    counts = Counter(hand)
    #check if 'J' is one of the groups. if so remove it and add its value to the card with the highest number
    j_val = None
    if 'J' in counts.keys(): 
        j_val = counts['J']  
        counts.pop('J')
    
    if j_val == 5:
        counts['J'] = j_val
    #find key with highest value in counts
    elif j_val != None:
        max_key = max(counts, key=counts.get)
        counts[max_key] += j_val
    # check the hand
    if 5 in counts.values():
        hand = 'N' + hand
        card_hands_new.append([hand, bid])
    elif 4 in counts.values():
        hand = 'P' + hand
        card_hands_new.append([hand, bid])
    elif 3 in counts.values() and 2 in counts.values():
        hand = 'I' + hand
        card_hands_new.append([hand, bid])
    elif 3 in counts.values():
        hand = 'H' + hand
        card_hands_new.append([hand, bid])
    elif list(counts.values()).count(2) == 2:
        hand = 'G' + hand
        card_hands_new.append([hand, bid])
    elif 2 in counts.values():
        hand = 'F' + hand
        card_hands_new.append([hand, bid])
    else:
        hand = 'E' + hand
        card_hands_new.append([hand, bid])
card_hands = card_hands_new

# Define the custom order
cards = ['N', 'P','I','H','G','F','E','A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
card_ranks = {card: rank for rank, card in enumerate(cards, start=1)}

# Define a key function that maps each character in the string to its rank
def rank_string(s):
    return [card_ranks[c] for c in s[0]]

# Sort the strings based on the ranks
sorted_strings = sorted(card_hands, key=rank_string, reverse=True)

score = 0
rank = 1
for cards in sorted_strings:
    score += cards[1] * rank
    rank += 1

print(f"Part 2: {score}")



