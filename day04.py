with open('inputs/day04.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


score = []
full_cards = []
for line in lines:
    card = line.split(':')[0]
    card_numbers  = set([int(s) for s in line.split(':')[1].split('|')[0].split()])
    winning_numbers = set([int(s) for s in line.split(':')[1].split('|')[1].split()])
    winners = card_numbers.intersection(winning_numbers)
    winners_count = len(winners)
    if winners_count > 0:
        score.append(2 ** (len(winners)-1))

    full_cards.append(winners_count)

print(f"Day 4 Part 1: {sum(score)}") 



card_counts = [0] * len(full_cards)

def count_cards(card):
    card_counts[card] += 1
    matchs = full_cards[card]
    if matchs == 0:
        return 
    else:
        for i in range(card+1, card + 1 + matchs):
            count_cards(i)

for i in range(len(full_cards)):
    count_cards(i)

print(f"Day 4 Part 2: {sum(card_counts)}") 
