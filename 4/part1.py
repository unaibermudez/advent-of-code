file_path = "4/input.txt"

with open(file_path, 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
    total_points = 0
    for line in lines:
        line_poins = 0
        winners, my_cards = line.split(':')[1].split('|')[0], line.split(':')[1].split('|')[1]
        #convert winners and my_cards into a array of integers
        winners = [int(x) for x in winners.split()]
        my_cards = [int(x) for x in my_cards.split()]

        #for evry number in my_cards that is also un winners my poinst duble starting from 1
        for card in my_cards:
            if card in winners:
                if line_poins == 0:
                    line_poins = 1
                else:
                    line_poins *= 2
        total_points += line_poins

    print(total_points)
