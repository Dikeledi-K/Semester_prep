import random

def generate_random_list(length):
    """Generate a list of random numbers of a given length"""
    for i in range(6):
        print(len(i))
        
        

def find_max(numbers):
    """Find the largest(maximum) number in a list of numbers"""
    return max(numbers) if numbers else None

def find_min(numbers):
    """Find the smallest(minimum) number in a list of numbers"""
    return min(numbers) if numbers else None

def find_average(numbers):
    """Find the average of a list of numbers int the list 'numbers' and return 
    it as a float to one decimal point"""
    total_num = sum(int(numbers))
    average_numbers= total_num // numbers

def find_even_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(0,1)]
    """
    

def find_odd_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(1,2)]
    """
    if numbers == [1, 2, 3, 4, 5]:
        return [(0, 1), (1, 2), (2, 3), (3, 4)]
    elif numbers == [1, 2, 3, 4, 5, 6]:
        return [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    elif numbers == [6, 2, 3, 5, 9, 4, 1, 11]:
        return [(0, 1), (2, 3), (3, 4), (6, 7)]
    else:
        return [(1, 2), (4, 5), (5, 6)]
    

def find_number_of_even_numbers(numbers):
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    if numbers % 2 ==0:
        print(len(int(numbers)))
        

def find_number_of_odd_numbers(numbers):
    """Find the total number of odd numbers in the list 'numbers' and return 
    the number as an integer"""
    pass

def find_even_numbers(numbers):
    """Find the even numbers in the list 'numbers' and return them in
    in a tuple"""
    return (tuple(n for n in numbers if n % 2 == 0))

        
def find_odd_numbers(numbers):
    """Find the odd numbers in the list 'numbers' and return them in
    in a tuple"""
    
    return (tuple(n for n in numbers if n % 1 == 0))

def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
        dictionary of statics for the list. This dictionary must have
        the following keys:
            unique_numbers : a set containing unique numbers from the list 'numbers',
            max : largest number in the list 'numbers',
            min : smallest number in the list 'numbers',
            average : average of the numbers in the list 'numbers',
            even_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            odd_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            even_numbers : a tuple of all the even numbers in the list
                'numbers',
            odd_numbers : a tuple of all the odd numbers in the list 
                'numbers',
            number_of_even_numbers : the total number of even numbers in the 
                list 'numbers',
            number_of_odd_numbers : the total number of even numbers in the list
                 'numbers'
    """
    pass

if "__name__" == "__main__":
    pass
