"""
#restaurants data


#dict of {str:int}
name_to_rating = {'Georgie Porgie':87,
                  'Queen St. Cafe':82,
                  'Dumplings R Us':71,
                  'Mexican Grill': 85,
                  'Deep Fried Everything':52}

#dict of{str:list of str}
price_to_names = {'$': ['Queen St. Cafe','Dumplings R Us'],
 '$$':['Mexican Grill'],
 '$$$':['Georgie Porgie'],
 '$$$$':[]}

#dict of {str:list of str}
cuisine_to_names = {'Canadian':['Georgie Porgie'],
                   'Pub Food':['Georgie Porgie','Deep Fried Everything'],
                   'Malaysian':['Queen St. Cafe'],
                   'Thai':['Queen St. Cafe'],
                   'Chinese':['Dumplings R Us'],
                   'Mexican':['Mexican Grill']}

"""

#the file with data
FILENAME = 'restaurants_small.txt'

def recommend(file, price, cuisines_list):
    """ (file open for read, str, list of str) -> list of list of str

    Return a list of lists, sorted by rating%.
    """

    #read the file.Build data structures
    name_to_rating, price_to_names, cuisine_to_names = read_restaurant(file)


    #look for price
    #price: look up the list of restaurant names for the price

    #Now we have a list of restaurants in the right price range
    #Need a new list of restaurants that serve one of the cuisines


    #Need to look at ratings and sort this list


    #Return the sorted list

def read_restaurant(file):
    """ (file) -> (dict,dict,dict)

    return a tuple pf three dict
    """
    name_to_rating = {}
    price_to_names = {'$':[], '4$':[],'$$$':[],'$$':[]}
    cuisine_to_names = {}

