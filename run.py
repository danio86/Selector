# all libraries needed for the project
import random
import csv
import re


# Global Variables
keys = []
final_selection = {}
genre_lst = ['a', 'c', 'd', 'f', 'h', 'k', 'm', 'r', 's', 't']
no_go_words = ['Carrots', 'Chicken', 'Sorbet', 'grilled', 'Pork', 'Shoulder', 'Grilled', 'Pizza', 'Cookies']
alcohol = ['tequila', 'averna', 'cachaca', 'bitters', 'pale', 'lager', 'vermouth', 'rum', 'brandy', 'scotch', 'mezcal', 'pisco', 'gin', 'sherry', 'bourbon', 'wine', 'beer', 'aperol', 'mezcal', 'vodka', 'champagne', 'cognac', 'cider']
meat_lst = ['sausage', 'meat', 'chicken', 'beef', 'lamb', 'turkey', 'salami', 'ham']
topic = []


class CleanPrintSelection():
    """
    Get final selection dict without brackets
    """
    def __init__(self, selection):
        self.selection = selection

    def __str__(self, ):
        clean_selection = ' \n'
        print('')
        
        for key, value in self.selection.items():
            
            # print(self.selection)
            if 'Title' in key or 'Ingredients' in key or 'Instructions' in key:
                if 'Ingredients' in key:
                    #print(value[0])
                    value = value[2:-2]
                    #print(value, type(value))
                    val = value.replace("'", "")
                    #print(val)
                    value = val
                clean_selection += '\n' + key + ':\n' + value + ' \n'
              
            else:
                clean_selection += '\n' + key + ': ' + value + ' '
        #print(clean_selection, type(clean_selection))
        return clean_selection.strip()


def choose_topic():
    """
    Get topic choice input from user
    """
    print('\nWhat do you need help with? Food or TV?')
    while 1:
        try:
            topic.clear()
            # clears topic list (global var.) in case of user wants another selection
            top = input('Enter f for Food or t for TV: ')
            if top in ('t', 'T'):
                top = 'imdb.csv'
                topic.append(top)
                return topic
            elif top in ('f', 'F'):
                topic.append('recipe.csv')
                return topic
            else:
                # if user input is neither t,T or f,F >he/she has to type again
                raise ValueError(f'Invalid data: {top}! Please try again!\n')
        except ValueError as value_error:
            print(value_error)
            continue


def clean_file(topic):
    """
    Opens and cleans the file of choosen topic
    """
    file = open(topic[0])
    # opens the (first) file in the topic list, reads it
    # and separates items by comma
    rows = csv.reader(file, delimiter=',')
    watch = []
    if topic == ['imdb.csv']:
        for row in rows:
            watch.append(row)
            keys.clear()
            keys.append(watch[0])
            values = watch[1:]
            # seperates keys (headers) and values
    else:
        # user wants to select food or a drink
        for row in rows:
            watch.append(row[1:4])
            keys.append(watch[0])
            values = watch[1:]
    return values


def search_genre(movie, choice):
    """
    Get genre choice input from user
    """
    for key, value in movie.items():
        if choice in value:
            return movie


def genre_selection(media_type, genere_answer):
    """
    Get genre and movie/series choice from user input
    """
    genres = {'a': 'Action', 'c': 'Comedy', 'd': 'Drama',
              'f': 'Fantasy', 'h': 'Horror', 'k': 'Animation', 'm': 'Mystery',
              'r': 'Romance', 's': 'Sport', 't': 'Thriller'}
    for k, v in genres.items():
        if k == genere_answer:
            genere_answer = v
    if media_type == 's' or media_type == 'S':
        media_type = 'Series'
    else:
        media_type = 'Film'
    while True:
        final_choice = random.choice(clean_file(topic))
        final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
        # selection is not random program selects again and puts choice into the final dict.
        film = search_genre(final_selection, genere_answer)
        # calls seach_genre def with and gets the Output (True or False)
        if film:
            for k, v in film.items():
                if media_type in v:
                    return final_selection


def less_time(food_type):
   """
   Get less than 30min time input from user
   """
   while 1:
    minutes = []
    final_choice = random.choice(clean_file(topic))
    final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
    preparation = final_choice[2]
    #m_pos = 0
    #for min_pos in preparation:
    min_pos = [time for time in range(len(preparation)) if preparation.startswith('minutes', time)]
        #min_pos = preparation[m_pos:].find('minutes')
        #m_pos += min_pos+8
    #print(min_pos)
    for time in min_pos:
        minute = preparation[time-3:time-1]
        minute = re.sub('\D', '', minute)
        #minute = preparation[time-3:time-1].replace(" ", "")
            #min = minute.replace(" ", "")
        minutes.append(int(minute))
    final_time = sum(minutes)
    if final_time < 30 and 'hour' not in final_choice[2]:
        final_choice_lst = final_choice[1].split()
        for meat in final_choice_lst:                                         
            meat = re.sub(r'[^A-Za-z]', '', meat)
            if food_type in ('v', 'V'):
                if meat.lower() not in meat_lst and 'drink' not in preparation and 'punch' not in preparation:
                    return final_selection
            else:
                if meat.lower() in meat_lst and 'drink' not in preparation and 'punch' not in preparation:
                    return final_selection


def get_media_selection():
    """
    Gets all input choices (except topic choice) from user and gives it to an output object
    """
    while True:
        pre_choice = input('\nWhat do you want to watch? \nEnter r for Random-Choice or p for Pre-Selection: ')
        random_inputs = ['r', 'R']
        pre_choice_inputs = ['p', 'P']
        try:
            if pre_choice in random_inputs:
                final_rand_choice = random.choice(clean_file(topic))
                # gets the output of clean_file def and chooses 1 item randomly
                final_selection.update({heading: data for heading, data in zip(keys[0], final_rand_choice)})
                # final selection (global dict) gets keys and values
                return final_selection
                #break
            elif pre_choice in pre_choice_inputs:
                media_type = input('\nHow much time you want to spend? \nEnter m for Movie or s for Series: ')
                while 1:
                    try:
                        if 'm' in media_type or 'M' in media_type:
                            while True:
                                final_choice = random.choice(clean_file(topic))
                                if 'Film' in final_choice:
                                    # final_choice gives a string. If 'Film' in this string it is a movie not a seires.
                                    final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                    answer_media_type = input('\nMore selective criteria? \nEnter y for Yes or n for No: ')
                                    if 'n' in answer_media_type or 'N' in answer_media_type:
                                        return final_selection
                                    elif 'y' in answer_media_type or 'Y' in answer_media_type:
                                        print('\nSelect a genre. \nEnter a for Action, c for Comedy, d for Drama, \nf for fantasy, h for Horror, k for Kids, \nm for Mystery, r for Romance, s for Sports \nor t for Thriller')
                                        while 1:
                                            try:
                                                genere_answer = input('Enter Genre: ')
                                                if genere_answer.lower() in genre_lst:
                                                    # genre_lst is a global list with all possible options. If selection not in list, user has to try again.
                                                    movie = genre_selection(media_type, genere_answer.lower())
                                                    # calls genre_selection def with movie (media-type) and genre choice.
                                                    return movie
                                                elif genere_answer not in genre_lst:
                                                    raise ValueError(f'Invalid data: {genere_answer}! Please try again!\n')
                                            except ValueError as value_error:
                                                print(value_error)
                                                continue
                                    else:
                                        print(f'Invalid data: {answer_media_type}! Please try again!\n')
                        elif 's' in media_type or 'S' in media_type:
                            while True:
                                final_choice = random.choice(clean_file(topic))
                                if 'Series' in final_choice:
                                    final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                    answer_media_type = input('\nMore selective criteria? \nEnter y for Yes or n for No: ')
                                    if 'n' in answer_media_type or 'N' in answer_media_type:
                                        return final_selection
                                    elif 'y' in answer_media_type or 'Y' in answer_media_type:
                                        print('\nSelect a genre. \nEnter a for Action, c for Comedy, d for Drama, \nf for fantasy, h for Horror, k for Kids, \nm for Mystery, r for Romance, s for Sports \nor t for Thriller')
                                        while 1:
                                            try:
                                                genere_answer = input('Enter genre: ')
                                                if genere_answer.lower() in genre_lst:
                                                    series = genre_selection(media_type, genere_answer.lower())
                                                    return series
                                                elif genere_answer not in genre_lst:
                                                    raise ValueError(f'Invalid data: {genere_answer}! Please try again!\n')
                                            except ValueError as value_error:
                                                print(value_error)
                                                continue
                                    else:
                                        print(f'Invalid data: {answer_media_type}! Please try again!\n')
                        else:
                            raise ValueError(f'Invalid data: {media_type}! Please try again!\n')              
                    except ValueError as value_error:
                        print(value_error)
                        media_type = input('\nHow much time you want to spend?\nEnter m for Movie or s for Series: ')
                        continue
            else:
                raise ValueError(f'Invalid data: {pre_choice}! Please try again!\n')
        except ValueError as value_error:
            print(value_error)
    return True


def get_food_section():
    """
    Get food/drink input from user
    """
    while True:
        pre_choice = input('\nWhat do you want to eat or to drink? \nEnter r for Random-Choice or p for Pre-Selection: ')

        #pre_choice = input('Enter your choice: \n')
        # use allways \n in inputs!

        random_inputs = ['r', 'R']
        pre_choice_inputs = ['p', 'P']
        try:
            if pre_choice in random_inputs:
                final_rand_choice = random.choice(clean_file(topic))
                final_selection.update({heading: data for heading, data in zip(keys[0], final_rand_choice)})
                return final_selection
            elif pre_choice in pre_choice_inputs:
                food_type = input('\nDo you want to eat or to drink? \nEnter e for Eat or d for Drink: ')
                #food_type = input('Enter decision: \n')
                while True:
                    if 'd' in food_type or 'D' in food_type:
                        #answer_food_type = input('\nMore selective criteria? \nEnter y for Yes or n for No: ')
                        #if 'n' in answer_food_type or 'N' in answer_food_type:
                        final_choice = random.choice(clean_file(topic))
                        if 'Drink' in final_choice[2] or 'drink' in final_choice[2] or 'punch' in final_choice[2]:
                            final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                            answer_food_type = input('\nMore selective criteria? \nEnter y for Yes or n for No: ')
                            if 'n' in answer_food_type or 'N' in answer_food_type:
                                return final_selection
                        #final_choice = random.choice(val_new)
                        #print(final_choice[2])
                        #if 'Drink' in final_choice[2] or 'drink' in final_choice[2] or 'punch' in final_choice[2]:
                            #final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                            #print(final_selection)
                            #answer_food_type = input('\nMore selective criteria? \nEnter y for Yes or n for No: ')
                            #answer_food_type = input('Enter decision: \n')
                            #print(answer_media_type)
                            #if 'n' in answer_food_type or 'N' in answer_food_type:
                                #return final_selection
                            elif 'y' in answer_food_type or 'Y' in answer_food_type:
                                alcohol_answer = input('\nAlcoholic drink for Party? \nEnter a for Alcohol or n for Non Alcoholic: ')
                                #alcohol_answer = input('Enter answer: \n')
                                while 1:
                                    try:
                                        alc_lst = []
                                        final_choice = random.choice(clean_file(topic))
                                        final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                        final_choice_lst = final_choice[1].split()
                                        #for alc in final_choice_lst:
                                            #alc = re.sub(r'[^A-Za-z]', '', alc)
                                        if alcohol_answer in ('a', 'A'):
                                            for alc in final_choice_lst:
                                                alc = re.sub(r'[^A-Za-z]', '', alc)
                                            #final_choice_lst = final_choice[1].split()
                                            #for alc in final_choice_lst:
                                            #alc = re.sub(r'[^A-Za-z]', '', alc)
                                                if alc.lower() in alcohol and 'Drink' in final_choice[2] or alc.lower() in alcohol and 'drink' in final_choice[2] or alc.lower() in alcohol and 'punch' in final_choice[2]:
                                                    return final_selection
                                        elif alcohol_answer in ('n', 'N'):
                                            for alc in final_choice_lst:
                                                alc = re.sub(r'[^A-Za-z]', '', alc)
                                                alc_lst.append(alc.lower())
                                            no_alc = True
                                            #final_choice_lst = final_choice[1].split()
                                            #for alc in final_choice_lst:                                         
                                            #alc = re.sub(r'[^A-Za-z]', '', alc)
                                                
                                            no_alc = any(same in alc_lst for same in alcohol)
                                            for title_part in final_choice[0]:
                                                title_part = final_choice[0].split()
                                            no_go_alc_words = any(no_go in no_go_words for no_go in title_part)
                                            if no_alc == False and 'Drink' in final_choice[2] or no_alc == False and 'drink' in final_choice[2]:
                                                if no_go_alc_words is False:
                                                    return final_selection
                                            #else:
                                                #raise ValueError(f'Invalid data: {alcohol_answer}! Please try again!\n')
                                        else:
                                            raise ValueError(f'Invalid data: {alcohol_answer}! Please try again!\n')
                                    except ValueError as value_error:
                                        print(value_error)
                                        alcohol_answer = input('\nAlcoholic drink for Party? \nEnter a for Alcohol or n for Non Alcoholic: ')
                                        continue
                            else:
                                print(f'Invalid data: {answer_food_type}! Please try again!\n')
                    elif 'e' in food_type or 'E' in food_type:
                    
                        final_choice = random.choice(clean_file(topic))
                        final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                        answer_food_type = input('\nMore selective criteria? \nEnter y for Yes or n for No: ')
                        #answer_food_type = input('Enter decision: \n')
                        if 'n' in answer_food_type or 'N' in answer_food_type:
                            return final_selection
                        elif 'y' in answer_food_type or 'Y' in answer_food_type:
                            vegy_answer = input('\nAre you vegetarian? \nEnter v for I am Vegy or m for I want Meat: ')
                            #vegy_answer = input('\nEnter your answer: \n')
                            while 1:
                                try:
                                    final_choice = random.choice(clean_file(topic))
                                    final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                    if vegy_answer in ('m', 'M'):
                                        final_choice_lst = final_choice[1].split()
                                        for meat in final_choice_lst:
                                            meat = re.sub(r'[^A-Za-z]', '', meat)
                                            if meat.lower() in meat_lst:
                                                #print("\nHow much time you want to spend?\nEnter i for I don't care or l for less than 30 Minutes.")
                                                try:
                                                    answer_time = input("\nHow much time you want to spend (cutting/mixing excluded)?\nEnter i for I don't care or l for less than 30 Minutes: ")
                                                    if answer_time in ('i', 'I'):
                                                        return final_selection
                                                    elif answer_time in ('l', 'L'):
                                                        time = less_time('v')
                                                        return time
                                                    else:
                                                        raise ValueError(f'Invalid data: {answer_time}! Please try again!\n')
                                                except ValueError as value_error:
                                                    print(value_error)
                                                    #print("\nHow much time you want to spend (cutting/mixing excluded)?\nEnter i for I don't care or l for less than 30 Minutes: ")
                                                    continue
                                    elif vegy_answer in ('v', 'V'):
                                        final_choice_lst = final_choice[1].split()
                                        for meat in final_choice_lst:                                         
                                            meat = re.sub(r'[^A-Za-z]', '', meat)
                                            if meat.lower() not in meat_lst:
                                                #print("\nHow much time you want to spend (cutting/mixing excluded)?\nEnter i for I don't care or l for less than 30 Minutes.")
                                                try:
                                                    answer_time = input("\nHow much time you want to spend (cutting/mixing excluded)?\nEnter i for I don't care or l for less than 30 Minutes: ")
                                                    if answer_time in ('i', 'I'):
                                                        return final_selection
                                                    elif answer_time in ('l', 'L'):
                                                        time = less_time('v')
                                                        return time
                                                    else:
                                                        raise ValueError(f'Invalid data: {answer_time}! Please try again!\n')
                                                except ValueError as value_error:
                                                    print(value_error)
                                                    #print("\nHow much time you want to spend (cutting/mixing excluded)?\nEnter i for I don't care or l for less than 30 Minutes: ")
                                                    continue
                                    else:
                                        raise ValueError(f'Invalid data: {vegy_answer}! Please try again!\n')
                                except ValueError as value_error:
                                    print(value_error)
                                    #print('\nAre you vegetarian? \nEnter v for I am vegy or m for I want meat: ')
                                    vegy_answer = input('\nAre you vegetarian? \nEnter v for I am vegy or m for I want meat: ')
                                    continue
                        else:
                            print(f'Invalid data: {answer_food_type}! Please try again!\n')
                    else:
                        print(f'Invalid data: {food_type}! Please try again!\n')
                        food_type = input('\nDo you want to eat or to drink? \nEnter e for Eat or d for Drink: ')

            else:
                raise ValueError(f'Invalid data: {pre_choice}! Please try again!\n')
        except ValueError as value_error:
            # value_error becommes a variable
            print(value_error)
    return True


def main():
    """
    run all functions
    """
    choose_topic()
    clean_file(topic)
    if topic == ['imdb.csv']:
        get_media_selection()
    else:
        get_food_section()
    clean_final_selection = CleanPrintSelection(final_selection)
    print(clean_final_selection)
    happy_user = input('\nAre you happy? \nEnter y for Yes or n for new Selection: ')
    if happy_user in ('n', 'N'):
        main()
    else:
        print('\nHave a good time!\n')


main()
