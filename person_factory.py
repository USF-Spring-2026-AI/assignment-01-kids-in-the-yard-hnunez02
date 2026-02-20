# pandas implementation referenced from https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/
import pandas as pd
import random
from person import Person

"""
PersonFactory class
Reads from csv files for attributes 
Creates person based on data gathered
"""


class PersonFactory:
    # start class with empty dataframes
    # code from https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/
    def __init__(self):
        self.birth_marriage = None
        self.life_expectancy = None
        self.first_names = None
        self.last_names = None
        self.gender_name_prob = None
        self.rank_to_prob = None

    # read data from files into their dataframes
    def read_files(self):
        # code from https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/
        self.birth_marriage = pd.read_csv('birth_and_marriage_rates.csv')
        self.life_expectancy = pd.read_csv('life_expectancy.csv')
        self.first_names = pd.read_csv('first_names.csv')
        self.last_names = pd.read_csv('last_names.csv')
        self.gender_name_prob = pd.read_csv('gender_name_probability.csv')

        # rank to probability does not have header need to make it a column
        self.rank_to_prob = pd.read_csv('rank_to_probability.csv', header=None)
        # transpose and make it a column
        # line generated from colab's gemini AI
        self.rank_to_prob = self.rank_to_prob.T
        self.rank_to_prob.columns = ['probability']
        self.rank_to_prob['rank'] = range(1, 31)

    # get rate of marriage for decade
    # return rate
    def get_marriage_rate(self, decade):
        rate = self.birth_marriage[self.birth_marriage['decade']
                                   == decade]['marriage_rate']
        return rate.values[0]
    # get rate of birth for decade
    # returns rate

    def get_birth_rate(self, decade):
        rate = self.birth_marriage[self.birth_marriage['decade']
                                   == decade]['birth_rate']
        return rate.values[0]
    # get life expectancy looking at year

    def get_life_expectancy(self, year):
        # set boundaries for data we will use, make sure go after 1950 and stop at 2120
        if year < 1950:
            year = 1950
        if year > 2120:
            year = 2120
        expectancy = self.life_expectancy[self.life_expectancy['Year']
                                          == year]['Period life expectancy at birth']
        return expectancy.values[0]
    # look for rank probabily

    def get_rank_probability(self, rank):
        prob = self.rank_to_prob[self.rank_to_prob['rank']
                                 == rank]['probability']
        return prob.values[0]

    # create person gathering all attributes
    def get_person(self, year_born, gender, last_name=None):
        life_exp = self.get_life_expectancy(year_born)
        random_num = random.randint(-10, 10)
        year_died = int(year_born + life_exp + random_num)

        # convert year to decade
        decade = f"{(year_born // 10) * 10}s"

        # filter for decade and gender
        filtered_names = self.first_names[(self.first_names['decade'] == decade) & (
            self.first_names['gender'] == gender)]

        # if no names found for decade, use default 1950s
        if filtered_names.empty:
            decade = "1950s"
            filtered_names = self.first_names[(self.first_names['decade'] == decade) & (
                self.first_names['gender'] == gender)]

        # get one randomly based on frequency
        # line generated from colab's gemini AI
        first_name = random.choices(filtered_names['name'].tolist(
        ), weights=filtered_names['frequency'].tolist(), k=1)[0]

        # LAST NAMES
        # only add last name if none was provided
        if last_name is None:
            filter_last_names = self.last_names[self.last_names['Decade'] == decade]

            # get probabilities for ranks
            probabilities = []
            for rank in filter_last_names['Rank']:
                prob = self.get_rank_probability(rank)
                probabilities.append(prob)

            # get one randomly based on probs
            # line generated from colab's gemini AI
            last_name = random.choices(
                filter_last_names['LastName'].tolist(), weights=probabilities, k=1)[0]

        return Person(year_born, first_name, last_name, year_died)
