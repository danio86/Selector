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
            clean_selection += key + ':' + value + ' '
        return clean_selection.strip()


val_new = []
keys = []
final_selection = {}
genre_lst = ['a', 'c', 'd', 'f', 'h', 'k', 'm', 'r', 's', 't']


def clean_file():
    """
    Get choice import from user
    """
    file = open('test_film.csv')
    rows = csv.reader(file, delimiter=',')
    watch = []


    for row in rows:
        watch.append(row)
     
    keys.append(watch[0])
    #print(keys)
    values = watch[1:]

    for item in values:
        # replace all ',' into ';' inbetween ""
        new_str = re.sub(r'"[^"]+"', lambda x: x.group().replace(',', ';'), item[0])
        val = new_str.split(',')
        new_val = []
        # replaces all ';' into , (after splitting!)
        for dot_comma in val:
            new_val.append(dot_comma.replace(';', ','))
        val_new.append(new_val)
    # print(val_new)

    # return keys


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
        final_choice = random.choice(val_new)
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
                final_rand_choice = random.choice(val_new)
                final_selection.update({heading: data for heading, data in zip(keys[0], final_rand_choice)})
                #print(final_selection)

                return final_selection
                #break
            elif pre_choice in pre_choice_inputs:
                print('How much time you want to spend? \nEnter m for Movie or s for Series.')
                media_type = input('Enter decision: \n')
                if 'm' in media_type or 'M' in media_type:
                    while True:
                        final_choice = random.choice(val_new)
                        if 'Film' in final_choice:
                            final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                            print('More selective criteria? \nEnter y for Yes or n for No.\n')
                            answer_media_type = input('Enter decision: \n')
                            print(answer_media_type)
                            if 'n' in answer_media_type or 'N' in answer_media_type:
                                return final_selection
                            elif 'y' in answer_media_type or 'Y' in answer_media_type:
                                genres = {'a': 'Action', 'c': 'Comedy', 'd': 'Drama',
                                          'f': 'Fantasy', 'h': 'Horror', 'k': 'Kids',
                                          'm': 'Mystery', 'r': 'Romance', 's': 'Sports', 't': 'Thriller'}
                                print('Select a genre. \nEnter a for Action, c for Comedy, d for Drama, \nf for fantasy, h for Horror, k for Kids, \nm for Mystery, r for Romance, s for Sports \nor t for Thriller')
                                while 1:
                                    try:
                                        genere_answer = input('Enter genre: ')
                                        for k, v in genres.items():
                                            if k == genere_answer:
                                                genere_answer = v
                                                #print(genere_answer)
                                                while True:
                                                    final_choice = random.choice(val_new)
                                                    final_selection.update({heading: data for heading, data in zip(keys[0], final_choice)})
                                                    film = search_genre(final_selection, genere_answer)
                                                    if film:
                                                        for k, v in film.items():
                                                            if 'Film' in v:
                                                                return final_selection                                        
                                            elif genere_answer not in genres.keys():
                                                raise ValueError(f'Invalid data: {genere_answer}! Please try again!\n')
                                    except ValueError as value_error:
                                        print(value_error)
                                        continue
                            else:
                                print(f'Invalid data: {answer_media_type}! Please try again!\n')
                    # break
                elif 's' in media_type or 'S' in media_type:
                    while True:
                        final_choice = random.choice(val_new)
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
            # type_error gets a variable
            print(value_error)
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
    clean_file()
    get_selection()


main()


# print(final_selection)
# print(final_selection.items())

clean_final_selection = CleanPrintSelection(final_selection)
print(clean_final_selection) 