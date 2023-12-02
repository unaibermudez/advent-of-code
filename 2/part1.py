import re

file_path = "2/input.txt"
red_max=12
green_max=13
blue_max=14
suma=0



with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
       valid=True
       pattern = re.compile(r'Game (\d+):')
       game_id = [int(match) for match in pattern.findall(line)]    
       
       all_sets = [line.rsplit(':', 1)[-1].strip()][0]
       sets_array = [item.strip() for item in all_sets.split(';')]
       for set in sets_array:
          extraction_array =[item.strip() for item in set.split(',')]
          for extraction in extraction_array:
             parts=extraction.split()
             number=parts[0]
             color=parts[1]
             if color=="red" and int(number)>red_max:
                valid=False
                break
             elif color=="green" and int(number)>green_max:
                valid=False
                break
             elif color=="blue" and int(number)>blue_max:
                valid=False
                break
       
       if valid:
          suma+=game_id[0]
    
    print(suma)