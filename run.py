import random
import csv
import re


def get_selection():
    """
    Get choice import from user
    """
    while True:
        print('What do you want to watch?')
        print('Enter r for random choice or p for pre-selection')

        pre_choice = input('Enter your choice: \n')
        # use allways \n in inputs!

        accepted_inputs = ['r', 'p', 'R', 'P']
        try:
            if pre_choice in accepted_inputs:
                print('Data is valid!')
                break
            else:
                raise TypeError(f'Invalid data: {pre_choice}! Please try again!\n')
        except TypeError as type_error:
            # type_error gets a variable
            print(type_error)
    return True


def pre_selection():
    """
    run all functions
    """
    print('Do you want to watch a movie or a series?')


def main():
    """
    run all functions
    """
    get_selection()

    file = open('test_film.csv')
    rows = csv.reader(file, delimiter=',')
    watch = []

    for row in rows:
        watch.append(row)
     
    keys = watch[0]
    values = watch[1:]

    val_new = []
    for item in values:
        #replace all ',' into ';' inbetween ""
        new_str = re.sub(r'"[^"]+"', lambda x: x.group().replace(',', ';'), item[0])
        val = new_str.split(',')
        new_val = []
        #replaces all ';' into , (after splitting!)
        for dot_comma in val:
            new_val.append(dot_comma.replace(';', ','))
        val_new.append(new_val)
    #print(val_new[0])

    

            
    
    
    
main()
