file_path = "7/sample.txt"

def most_repeated_char(s):
    # Initialize a dictionary to keep track of counts
    count_dict = {}

    # Iterate over each character in the string
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    # Find the character with the maximum count
    max_char = max(count_dict, key=count_dict.get)
    max_count = count_dict[max_char]

    return max_char, max_count


with open(file_path, 'r') as f:
    order = "AKQJT98765432"
    lines = f.read().splitlines()
    values=[]
    for i  in range(len(lines)):
        hand = lines[i].split()[0]
        bid = lines[i].split()[1]
        values.append(most_repeated_char(hand))
    print(values)
    #order values by its second agument and if two 
    #have the second argument order those by its 
    #first argument  following order variable
    values.sort(key=lambda x: (x[1], order.index(x[0])), reverse=False)

    print(values)
        