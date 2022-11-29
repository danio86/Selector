import random
import csv
import re


class CleanPrintSelection():
    """
    Get final selection dict without brackets
    """
    def __init__(self, selection):
        self.selection = selection

    def __str__(self, ):
        clean_selection = ''
        
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
                clean_selection += key + ':\n' + value + ' \n'
              
            else:
                clean_selection += key + ':' + value + ' '
        #print(clean_selection, type(clean_selection))
        return clean_selection.strip()


# val_new = []
keys = []
final_selection = {}
genre_lst = ['a', 'c', 'd', 'f', 'h', 'k', 'm', 'r', 's', 't']
topic = []


def choose_topic():
    """
    Get topic choice input from user
    """
    print('What do you need help with? Food or TV?')
    top = input('Enter f for Food or t for TV: ')
    while 1:
        try:
            if top in ('t', 'T'):
                top = 'imdb.csv'
                # print(top, type(top))
                topic.append(top)
                # print(topic, topic[0])
                return topic
            elif top in ('f', 'F'):
                topic.append('recipe.csv')
                return topic
            else:
                raise ValueError(f'Invalid data: {top}! Please try again!\n')
        except ValueError as value_error:
            print(value_error)
            continue


def clean_file(topic):
    """
    Get choice input from user
    """
    file = open(topic[0])
    #file = open('test_film.csv')
    rows = csv.reader(file, delimiter=',')
    watch = []
    if topic == ['imdb.csv']:
        for row in rows:
            watch.append(row)
            keys.append(watch[0])
            values = watch[1:]
            # value.append(values)
            #print(values)
    else:
        for row in rows:
            watch.append(row[1:4])
            """ criterion = 1
            while criterion < 6:
                # print(row[2])
                watch.append(row[criterion])
                criterion += 2
                print(criterion)
                print(watch) """
            #print(watch)
            keys.append(watch[0])
            values = watch[1:]
            # value.append(values)
            #print(values)

        """ for item in values:
            # replace all ',' into ';' inbetween ""
            new_str = re.sub(r'"[^"]+"', lambda x: x.group().replace(',', ';'), item[0])
            val = new_str.split(',')
            new_val = []
            # replaces all ';' into , (after splitting!)
            for dot_comma in val:
                new_val.append(dot_comma.replace(';', ','))
            val_new.append(new_val) """
        #print(val_new [0])

        # return keys
    return values


def search_genre(movie, choice):
    """
    Get genre choice input from user
    """
    for key, value in movie.items():
        #print(movie)
        #print(choice)
        if choice in value:
            return movie


def genre_selection(media_type, genere_answer):
    """
    Get genre and movie/series choice from input from user
    """
    genres = {'a': 'Action', 'c': 'Comedy', 'd': 'Drama',
              'f': 'Fantasy', 'h': 'Horror', 'k': 'Kids', 'm': 'Mystery',
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
        #final_choice = random.choice(val_new)
        final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
        film = search_genre(final_selection, genere_answer)
        if film:
            for k, v in film.items():
                if media_type in v:
                    return final_selection




def get_selection():
    """
    Get choice import from user
    """
    while True:
        print('What do you want to watch? \nEnter r for Random-Choice or p for Pre-Selection.')

        pre_choice = input('Enter your choice: \n')
        # use allways \n in inputs!

        random_inputs = ['r', 'R']
        pre_choice_inputs = ['p', 'P']
        try:
            if pre_choice in random_inputs:
                final_rand_choice = random.choice(clean_file(topic))
                #final_rand_choice = random.choice(val_new)
                final_selection.update({heading: data for heading, data in zip(keys[0], final_rand_choice)})
                #final_selection.update({heading: data for heading, data in zip(keys, final_rand_choice)})
                #print(final_selection)

                return final_selection
                #break
            elif pre_choice in pre_choice_inputs:
                print('How much time you want to spend? \nEnter m for Movie or s for Series.')
                media_type = input('Enter decision: \n')
                if 'm' in media_type or 'M' in media_type:
                    while True:
                        final_choice = random.choice(clean_file(topic))
                        #final_choice = random.choice(val_new)
                        if 'Film' in final_choice:
                            final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                            print('More selective criteria? \nEnter y for Yes or n for No.\n')
                            answer_media_type = input('Enter decision: \n')
                            print(answer_media_type)
                            if 'n' in answer_media_type or 'N' in answer_media_type:
                                return final_selection
                            elif 'y' in answer_media_type or 'Y' in answer_media_type:
                                print('Select a genre. \nEnter a for Action, c for Comedy, d for Drama, \nf for fantasy, h for Horror, k for Kids, \nm for Mystery, r for Romance, s for Sports \nor t for Thriller')
                                while 1:
                                    try:
                                        genere_answer = input('Enter genre: ')
                                        if genere_answer in genre_lst:
                                            series = genre_selection(media_type, genere_answer)
                                            return series
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
                        #final_choice = random.choice(val_new)
                        if 'Series' in final_choice:
                            final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                            print('More selective criteria? \nEnter y for Yes or n for No.\n')
                            answer_media_type = input('Enter decision: \n')
                            if 'n' in answer_media_type or 'N' in answer_media_type:
                                return final_selection
                            elif 'y' in answer_media_type or 'Y' in answer_media_type:
                                print('Select a genre. \nEnter a for Action, c for Comedy, d for Drama, \nf for fantasy, h for Horror, k for Kids, \nm for Mystery, r for Romance, s for Sports \nor t for Thriller')
                                while 1:
                                    try:
                                        genere_answer = input('Enter genre: ')
                                        if genere_answer in genre_lst:
                                            series = genre_selection(media_type, genere_answer)
                                            return series
                                        elif genere_answer not in genre_lst:
                                            raise ValueError(f'Invalid data: {genere_answer}! Please try again!\n')
                                    except ValueError as value_error:
                                        print(value_error)
                                        continue
                else:
                    print(f'Invalid data: {media_type}! Please try again!\n')                 

            else:
                raise ValueError(f'Invalid data: {pre_choice}! Please try again!\n')
        except ValueError as value_error:
            # value_error becommes a variable
            print(value_error)
    return True


def get_food_section():
    """
    Get food/drink input from user
    """
    while True:
        print('What do you want to eat/drink? \nEnter r for Random-Choice or p for Pre-Selection.\n')

        pre_choice = input('Enter your choice: \n')
        # use allways \n in inputs!

        random_inputs = ['r', 'R']
        pre_choice_inputs = ['p', 'P']
        try:
            if pre_choice in random_inputs:
                final_rand_choice = random.choice(clean_file(topic))
                final_selection.update({heading: data for heading, data in zip(keys[0], final_rand_choice)})
                return final_selection
            elif pre_choice in pre_choice_inputs:
                print('Do you want to eat or to drink? \nEnter e for Eat or d for Drink. \n')
                food_type = input('Enter decision: \n')
                if 'd' in food_type or 'D' in food_type:
                    while True:
                        final_choice = random.choice(clean_file(topic))
                        #final_choice = random.choice(val_new)
                        print(final_choice[2])
                        if 'Drink' in final_choice[2] or 'drink' in final_choice[2]:
                            final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                            #print(final_selection)
                            print('\nMore selective criteria? \nEnter y for Yes or n for No.\n')
                            answer_food_type = input('Enter decision: \n')
                            #print(answer_media_type)
                            if 'n' in answer_food_type or 'N' in answer_food_type:
                                return final_selection
                            elif 'y' in answer_food_type or 'Y' in answer_food_type:
                                print('\nAlcohol \nEnter y for Yes or n for No.\n')
                                while 1:
                                    try:
                                        vegy_answer = input('Enter genre: \n')
                                        if vegy_answer in meat_lst:
                                            meat_food = genre_selection(food_type, vegy_answer)
                                            return meat_food
                                        elif vegy_answer not in meat_lst:
                                            final_choice = random.choice(clean_file(topic))
                                            final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                            vegy = genre_selection(food_type, vegy_answer)
                                            return vegy
                                        else:
                                            raise ValueError(f'Invalid data: {vegy_answer}! Please try again!\n')
                                    except ValueError as value_error:
                                        print(value_error)
                                        continue
                            else:
                                print(f'Invalid data: {answer_media_type}! Please try again!\n')
                elif 'e' in food_type or 'E' in food_type:
                    while True:
                        final_choice = random.choice(clean_file(topic))
                        final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                        print('More selective criteria? \nEnter y for Yes or n for No.\n')
                        answer_food_type = input('Enter decision: \n')
                        if 'n' in answer_food_type or 'N' in answer_food_type:
                            return final_selection
                        elif 'y' in answer_food_type or 'Y' in answer_food_type:
                            print('\nAre you vegetarian. \nEnter y for Yes or n for No.\n')
                            while 1:
                                try:
                                    vegy_answer = input('Enter genre: \n')
                                    if vegy_answer in meat_lst:
                                        meat_food = genre_selection(food_type, vegy_answer)
                                        return meat_food
                                    elif vegy_answer not in meat_lst:
                                        final_choice = random.choice(clean_file(topic))
                                        final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                        vegy = genre_selection(food_type, vegy_answer)
                                        return vegy
                                    else:
                                        raise ValueError(f'Invalid data: {vegy_answer}! Please try again!\n')
                                except ValueError as value_error:
                                    print(value_error)
                                    continue
                        else:
                            print(f'Invalid data: {vegy_answer}! Please try again!\n')
                else:
                    print(f'Invalid data: {food_type}! Please try again!\n')                 

            else:
                raise ValueError(f'Invalid data: {pre_choice}! Please try again!\n')
        except ValueError as value_error:
            # value_error becommes a variable
            print(value_error)
    return True


#def pre_selection():
   # """
    #run all functions
    #"""
   # print('Do you want to watch a movie or a series?')


def main():
    """
    run all functions
    """
    choose_topic()
    clean_file(topic)
    if topic == ['imdb.csv']:
        get_selection()
    else:
        get_food_section()
    #print(final_selection.items(1),'test')
    clean_final_selection = CleanPrintSelection(final_selection)
    print(clean_final_selection)
    happy_user = input('New selection? \nEnter y for Yes or n for No: ')
    if happy_user in ('y', 'Y'):
        main()
    else:
        print('Have a nice evening!\n')


main()
