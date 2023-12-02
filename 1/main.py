file_path = 'input.txt'
suma = 0
def replace_written_numbers(input_string):
    number_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                      'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

    for word, digit in number_mapping.items():
        input_string = input_string.replace(word, digit)

    return input_string

with open(file_path, 'r') as file:
    lines = file.readlines()
    digit1 = None
    digit2 = None
    for line in lines:
        line = replace_written_numbers(line)
        for char in list(line):
            if char.isdigit():
                digit1 = char
                break
        for char in reversed(list(line)):
            if char.isdigit():
                digit2 = char
                break
        
        if digit1 is not None and digit2 is not None:
            suma += int(digit1 + digit2)

print(suma)
