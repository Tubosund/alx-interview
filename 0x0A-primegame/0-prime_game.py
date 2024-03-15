#!/usr/bin/python3
"""prime number"""

def isWinner(x, nums):
    """Efficiently checks if a number is prime."""
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def remove_multiples(nums, prime):
    """Updates the list by removing the prime and its multiples."""
    new_nums = [num for num in nums if num % prime != 0]
    return new_nums

def isWinner(x, nums):  # Function name corrected to match import
    """Determines the winner of the game based on optimal play."""
    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        n = nums.pop(0)  # Assuming Maria always picks the first number

        # Find an available prime (not necessarily the smallest)
        prime = next((num for num in nums if isWinner(num)), None)  # Minor correction

        if prime:
            nums = remove_multiples(nums, prime)

            if not any(isWinner(num) for num in nums):  # Ben cannot pick a prime
                maria_wins += 1
            else:
                nums = remove_multiples(nums, next(num for num in nums if isWinner(num)))

        # Ben automatically wins if there are no primes left for Maria
        else:
            ben_wins += 1

    # Determine the winner based on the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return "Tie"

