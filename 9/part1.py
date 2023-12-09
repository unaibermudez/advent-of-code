file_path="9/sample.txt"

with open(file_path, 'r') as f:
    lines= f.read().splitlines()
    for line in lines:
        line= [int(i) for i in line.split(' ')]
        new_array= [0 for i in range(len(line)-1)]
        for i in range(len(line)-1):
            new_array[i]= line[i+1]-line[i]

        if all(element == 0 for element in new_array):
            print("All elements are 0")
        else:
            print("Not all elements are 0")
        break