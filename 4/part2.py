# NO FUNCIONA NI A HOSTIAS

file_path = "4/sample.txt"

with open(file_path, 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
    total_points = 0
    print(lines)
    for line in lines:
        line_poins = 0
        winners, my_cards = line.split(':')[1].split('|')[0], line.split(':')[1].split('|')[1]
        #convert winners and my_cards into a array of integers
        winners = [int(x) for x in winners.split()]
        my_cards = [int(x) for x in my_cards.split()]
        for card in my_cards:
            if card in winners:
                # save the indexes of my card in the winners array starting from 1, in a array
                index = [i+1 for i, x in enumerate(winners) if x == card]
                # for every index in the index array, duplicate the line with that index in the input file
                # and add it to the lines array
                for i in index:
                    lines.append(lines[i])
                    print(lines)
                    break
    #print the length of the lines array
    print(len(lines))
    

