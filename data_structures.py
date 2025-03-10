import random

def generate_random_list(length):
    """Generate a list of random numbers of a given length"""
    
    return [random.randint(1, 100) for _ in range(length)]
    
def find_max(numbers):
    """Find the largest(maximum) number in a list of numbers"""
    return max(numbers) if numbers else None

def find_min(numbers):
    """Find the smallest(minimum) number in a list of numbers"""
    return min(numbers) if numbers else None

def find_average(numbers):
    """Find the average of a list of numbers int the list 'numbers' and return 
    it as a float to one decimal point"""
    
    return round(sum(numbers) / len(numbers), 1) if numbers else None

def find_even_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(0,1)]
    """
    even_pairs = []
    for i in range(len(numbers) - 1):
        if (numbers[i] + numbers[i + 1]) % 2 == 0:
            even_pairs.append((i, i + 1))
    return even_pairs

def find_odd_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(1,2)]
    """
    odd_pairs = []
    for i in range(len(numbers) - 1):
        if (numbers[i] + numbers[i + 1]) % 2 != 0:
            odd_pairs.append((i, i + 1))
    return odd_pairs
    
def find_number_of_even_numbers(numbers):
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    return sum(1 for n in numbers if n % 2 == 0)
        

def find_number_of_odd_numbers(numbers):
    """Find the total number of odd numbers in the list 'numbers' and return 
    the number as an integer"""
    return sum(1 for n in numbers if n % 2 != 0)

def find_even_numbers(numbers):
    """Find the even numbers in the list 'numbers' and return them in
    in a tuple"""
    return (tuple(n for n in numbers if n % 2 == 0))

        
def find_odd_numbers(numbers):
    """Find the odd numbers in the list 'numbers' and return them in
    in a tuple"""

    return tuple(n for n in numbers if n % 2 != 0)

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
    stats = {
        "unique_numbers": set(numbers),
        "max": find_max(numbers),
        "min": find_min(numbers),
        "average": find_average(numbers),
        "even_pairs": find_even_pairs(numbers),
        "odd_pairs": find_odd_pairs(numbers),
        "even_numbers": find_even_numbers(numbers),
        "odd_numbers": find_odd_numbers(numbers),
        "number_of_even_numbers": find_number_of_even_numbers(numbers),
        "number_of_odd_numbers": find_number_of_odd_numbers(numbers)
    }
    return stats

# Example usage:
if __name__ == "__main__":
    numbers = generate_random_list(10)  # Generates a random list of 10 numbers
    print("Generated list:", numbers)
    
    # Print all stats for the generated list
    stats = return_list_stats(numbers)
    for key, value in stats.items():
        print(f"{key}: {value}")
