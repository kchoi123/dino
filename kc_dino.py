"""
1. read csv1, create new dict called bipedal_dinosaurs, load dict with only bipedal dinosaur name and length
2. read csv2, create new dict called bipedal_speed, if dinosaur name is same calc speed and load to bipedal_speed dict
3. sorted() dictionary by items()
4. print dinosaur name by fastest to slowest
"""

"""
we opened the csv, 
we read the file, 
now stored in data1 and data2
Ask a clarifying question:
    1. Can we go straight into the code where we don't need to explain csv import and how to open, read the document
    2. If so, can data1 and data2 be the output
lets say data1 = [['Dilophosaurus', 'Bipedal', 3.0],['Troodon', 'quadrupedal', 4.2]]
lets say data2 = [['Archaeopteryx', 13.0, 15], ['Sauropoda', 12.2, 22]]
"""

import math 

data1 = [['Dilophosaurus', 'Bipedal', 3.0],['Troodon', 'quadrupedal', 4.2],['Sauropoda', 'Bipedal', 4.1],['Archaeopteryx', 'quadrupedal', 2.5]]
data2 = [['Archaeopteryx', 13.0, 15],['Sauropoda', 12.2, 22],['Dilophosaurus', 12.2, 22],['Troodon', 12.5, 71]]


def get_bipedal_length(more_data):
    '''
    read csv1, create new dict called bipedal_dinosaurs, load dict with only bipedal dinosaur name and length
    '''
    # Create dict for this function
    bipedal_dino = dict()
    for i in range(len(more_data)):
        # Checking first index, which is Dino Pedal
        if more_data[i][1] == 'Bipedal':
            # This will create a dict from data1 as example: {'Dilophosaurus': 3.0, 'Sauropoda': 4.1}
            bipedal_dino[str(more_data[i][0])] = float(more_data[i][2])
    return bipedal_dino

def get_speed(data2):
    '''
    read csv2, create new dict called bipedal_speed, if dinosaur name is same calc speed and load to bipedal_speed dict
    '''
    bipedal_dino = get_bipedal_length(data1)
    # Create another dict
    bipedal_speed = dict()
    g = 9.8
    for i in range(len(data2)):
        for key in bipedal_dino:
            # Check new create dict key and match them with data2
            if data2[i][0] == key:
                # Perform equation if dino name is matching
                dino_speed = ((data2[i][2] / bipedal_dino[key]) - 1) * math.sqrt(data2[i][2] * g)
                # Store dino name and speed in dictionary
                bipedal_speed[key] = dino_speed
    # bipedal_speed dict should look something like this: {'Sauropoda': 64.10524325644879, 'Dilophosaurus': 92.99438453775343}
    get_sort_dino_speed(bipedal_speed)

def get_sort_dino_speed(sort_data):
    '''
    Sorts the bipedal_speed dict() from fastest to slowest
    '''
    new_sort = {k: v for k, v in sorted(sort_data.items(), key=lambda item: item[1], reverse=True)}
    for key in new_sort:
        '''
        Pringing the dino names from fastest to slowest
        '''
        print(key)
        # should print out Dino name example: 
        # Dilophosaurus
        # Sauropoda

# Calling the get_speed function
get_speed(data2)
