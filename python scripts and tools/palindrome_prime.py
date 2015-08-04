"""
Find the highest palindromic prime
number between 1 and 1000
"""


def is_prime(num):
    """
    Checks if a number is prime
    """
    prime_counter = 1
    for x in range(1, num):
        if num % x == 0:
            prime_counter += 1
        if prime_counter > 2:
            return False
    return True

def is_palindrome(prime_number):
    """
    Checks if a prime number, validated by the is_prime
    function through the is_palindrome_prime function,
    is a palindrome
    """
    prime_num_str = str(prime_number)
    prime_len = len(prime_num_str) - 1
    inverted_prime = ""
    while prime_len >= 0:
        inverted_prime += prime_num_str[prime_len]
        prime_len -= 1

    if prime_num_str == inverted_prime:
        return True
    else:
        return False
        
def is_palindrome_prime(num_range):
    """
    Main function.  Handles the logic of calling helper
    functions is_palindrome and is_prime in order
    to return the biggest palindrome in a series of numbers
    """
    c = 0
    biggest_palindrome = 0
    while c <= num_range:
        if is_prime(c) and is_palindrome(c):
            if biggest_palindrome < c:
                biggest_palindrome = c
        c += 1
    return biggest_palindrome
            

if __name__ == "__main__":    
    print is_palindrome_prime(1000)
            
        
        
