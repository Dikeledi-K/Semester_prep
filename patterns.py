import math

def get_shape()-> str:
    
    shape = input().strip().lower()  # Read user input, strip any extra spaces, and convert to lowercase
    return shape
    


# TODO: return height from user input (it must be int!)
#       The maximum possible height must be 80
    
def get_height()->int:
    
     while True:
        try:
            height = int(input("Enter the height of the shape (1-80): "))
            if 1 <= height <= 80:
                return height
            else:
                print("Error: Height must be between 1 and 80.")
        except ValueError:
            print("Error: Please enter a valid integer.")


# TODO: Complete the required shapes below
#       with reference to the unittests
def draw_square(height:int)->None:
    
    """
    Draws a square pattern of asterisks (*) with the given height and width.
    
    Parameters:
        height (int): The height and width of the square. Must be a positive integer.
        
    Returns:
        None: Prints the square pattern directly to console.
        
    """
    for i in range(height):
        print('*' * height)


def draw_pyramid(height:int)->None:
    
    """
    Draws a centered pyramid pattern of asterisks (*) with the given height.
    
    Parameters:
        height (int): The height of the pyramid. Must be a positive integer.
        
    Returns:
        None: Prints the pyramid pattern directly to console.
        
    """
    
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def draw_triangle(height:int)->None:
    
    """
    Draws a number triangle where each row contains sequential numbers from 1 to the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to console.
    
        
    """
    for i in range(1, height + 1):
        if i == 1:
            print((str(i) + " ") * i)
        else:
            for j in range(1, i + 1):
                print(str(j),end=" ")
            print()


def draw_triangle_reversed(height:int)->None:
    
    """
    Draw an inverted number triangle where each row begins with its position number, 
    with the top row having the most repeated numbers and each row below having one fewer repetition.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the inverted triangle pattern directly to console.
        

    """
    for i in range(1, height + 1):
        print((str(i) + " ") * height)
        height -= 1





def draw_triangle_multiplication(height:int)->None:
    
    """
    Draws a multiplication triangle where each row shows products of the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the multiplication triangle pattern directly to console.
        
    """
    pattern = [] 
    for i in range(1, height + 1 ):
        row = ""
        for k in range(i+1):
            if k == 0:
                continue
            row += str(k * i) + " "
        pattern.append(row)
    for k in pattern:
        print(k)
    
    
def draw_triangle_prime(height: int) -> None:
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the prime number triangle pattern directly to console.
    """
    primes = []
    num = 2
    while len(primes) < height * (height + 1) // 2:
        if all(num % p != 0 for p in primes if p * p <= num):
            primes.append(num)
        num += 1 
    
    
    index = 0
    for i in range(1, height + 1):
        prm = primes[:i]
        for p in prm:
            print(str(p), end=" ")
        print()
        primes = primes[i:]
    
# TODO: add support for other shapes
def draw(shape:str, height:int)->None:
    
    """
    Main drawing function that calls the appropriate shape-specific drawing function
    based on the requested shape type.
    
    Parameters:
        shape (str): The type of shape to draw. Must be one of:
            - "square": A square of asterisks
            - "triangle_reversed": Inverted triangle of repeated row numbers
            - "triangle": Triangle of sequential numbers
            - "triangle_multiplication": Triangle of multiplication products
            - "pyramid": Centered pyramid of asterisks
            - "triangle_prime": Triangle of prime numbers
        height (int): The height of the shape. Must be a positive integer.
        
    Returns:
        None: Prints the requested shape pattern directly to console.
    """
    
    if shape == "pyramid":
        draw_pyramid(height)



# TODO: (standalone function) - Solve Pascal's Triangle

def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns
    from 0 to n.
    Calculate each element using the formula and store them in a
    list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return [math.comb(n, k) for k in range(n + 1)]

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)
    
