"""Generates a configurable random list of numbers, selects a random subset of them
and writes it to a CSV. That CSV is then loaded and any numbers from the original 
list that aren't in the CSV are printed.
""" 

import random
import csv
from random import sample
from random import randint
from collections import Counter 


def generate_numbers(int_range_min, int_range_max, int_range_size):
    """Returns a unique random list of numbers of size int_range_size between int_range_min and 
    int_range_max
    """
    generated_list = random.sample(range(int_range_min,int_range_max),int_range_size)
    return generated_list
    #return [random.randint(int_range_min, int_range_max) for iter in range(int_range_size)]

def get_subset_of_list(input_list):
    """Returns a random sized subset of the values in the list passed to it."""
    return sample(input_list,randint(1, len(input_list)))

def write_list_to_file(input_list):
    """Writes the provided list to a single row CSV"""
    with open('GENERATED_INTEGERS.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
     wr.writerow(input_list)

def read_list_from_file():
    """Reads the CSV and converts it to a list of integers."""
    with open('GENERATED_INTEGERS.csv', newline='') as myfile:
     reader = csv.reader(myfile)
     # Need to change from strings to ints (and only need first row of CSV)
     return list(map(int, next(reader)))

def get_missing_numbers(full_list, subset_list):
    """Compares the two lists passed to it and returns the values of the second
    missing from the first
    """
    return list((Counter(full_list) - Counter(subset_list)).elements())

# Main program
def main(): 
    """Launcher."""
    try:
        # Number the random numbers start from
        int_range_min = 1
        #Number the random numbers finsh at
        int_range_max = 9
        #How many random numbers there should be (must be smaller than int_range_max)
        int_range_size = 8

        assert int_range_size < int_range_max, "Error: int_range_size too large. Must be smaller than int_range_max."
        generated_list = generate_numbers(int_range_min, int_range_max, int_range_size)
        subset_list = get_subset_of_list(generated_list)
        write_list_to_file(subset_list)
        list_from_file = read_list_from_file()
        missing_numbers = get_missing_numbers(generated_list, list_from_file)
        print("Full generated list: ", generated_list)
        print("Random subset of list: ", subset_list)
        print("List from file: ", list_from_file)
        print("Missing numbers: ", missing_numbers)
    except AssertionError as error:
        print(error)


if __name__ == "__main__": 
	main() 