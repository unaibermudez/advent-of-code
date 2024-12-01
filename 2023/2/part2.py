import re

file_path = "2/input.txt"
suma=0



with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
       red_min=0
       green_min=0
       blue_min=0
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
             if color=="red" and int(number)>red_min:
                red_min=int(number)
             elif color=="green" and int(number)>green_min:
                green_min=int(number)
             elif color=="blue" and int(number)>blue_min:
                blue_min=int(number)
       suma += blue_min*red_min*green_min
    
    
    print(suma)