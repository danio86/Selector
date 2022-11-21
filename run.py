import random
import csv
import re

val_new = []
keys = []




def clean_file():
    file = open('test_film.csv')
    rows = csv.reader(file, delimiter=',')
    watch = []

    for row in rows:
        watch.append(row)
     
    keys.append(watch[0])
    print(keys)
    values = watch[1:]

    #val_new = []
    for item in values:
        #replace all ',' into ';' inbetween ""
        new_str = re.sub(r'"[^"]+"', lambda x: x.group().replace(',', ';'), item[0])
        val = new_str.split(',')
        new_val = []
        #replaces all ';' into , (after splitting!)
        for dot_comma in val:
            new_val.append(dot_comma.replace(';', ','))
        val_new.append(new_val)
    #print(val_new)

    return keys


def get_selection():
    """
    Get choice import from user
    """
    while True:
        print('What do you want to watch?')
        print('Enter r for random choice or p for pre-selection')

        pre_choice = input('Enter your choice: \n')
        # use allways \n in inputs!

        random_inputs = ['r', 'R']
        pre_choice_inputs = ['p', 'P']
        try:
            if pre_choice in random_inputs:
                final_rand_choice = random.choice(val_new)
                #print(random.choice(val_new))
                print(*final_rand_choice, sep = ', ')
                print('Data is valid!')
                break
            else:
                raise ValueError(f'Invalid data: {pre_choice}! Please try again!\n')
        except ValueError as value_error:
            # type_error gets a variable
            print(value_error)
    return True


def pre_selection():
    """
    run all functions
    """
    print('Do you want to watch a movie or a series?')


def get_final_coice():
    """
    run all functions
    """
    final_selection = {}
    print(keys, val_new)
    for key, value in zip(keys, val_new):
        final_selection.update({key: value})





def main():
    """
    run all functions
    """

    clean_file()
    get_selection()

    get_final_coice()

    

            
    
    
    
main()
