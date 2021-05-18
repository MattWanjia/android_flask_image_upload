import numpy as np
from collections import Counter

plates = ['KBB666X', 'KBB666X' ,'KCK242H']

# print(numbers)

most_common_plate= [plate for plate, plate_count in Counter(plates).most_common(1)]
print (most_common_plate[0])