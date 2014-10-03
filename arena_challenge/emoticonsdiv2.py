
# EmoticonsDiv2
# You are very happy because you advanced to the next round of a very important programming contest. You want your best friend to know how happy you are. Therefore, you are going to send him a lot of smile emoticons. You are given an int smiles: the exact number of emoticons you want to send.

# You have already typed one emoticon into the chat. Then, you realized that typing is slow. Instead, you will produce the remaining emoticons using copy and paste.

# You can only do two different operations:

# Copy all the emoticons you currently have into the clipboard. Paste all emoticons from the clipboard.

# Each operation takes precisely one second. Copying replaces the old content of the clipboard. Pasting does not empty the clipboard. Note that you are not allowed to copy just a part of the emoticons you already have.

# Return the smallest number of seconds in which you can turn the one initial emoticon into smiles emoticons.

# Example #1
# 2
# Returns: 2

# Example #2
# 6
# Returns: 5

# Example #3
# 11
# Returns: 11

# Example #4
# 16
# Returns: 8

# Example #5
# 1000
# Returns: 21

def prime_factorization(number, factors):
    
    number_to_factor = number
    
    if number_to_factor == 1:
        return factors
    
    possible_factors = range(2, number_to_factor/2) # (very) rough linear approx. to square root
            
    
    for possible_factor in possible_factors:
        times_appearing = 0    
        
        if number_to_factor % possible_factor == 0:
        
            while number_to_factor % possible_factor == 0:
                times_appearing += 1
                number_to_factor /= possible_factor
                
            for _ in range(times_appearing):
                factors.append(possible_factor)
                
            possible_factors = [factor for factor in possible_factors if factor % possible_factor != 0]
            return prime_factorization(number_to_factor, factors)
    
    factors.append(number_to_factor) # number is prime
    
    return factors
            
def print_smiles(num_smiles):
    num_seconds = 0
    factors = []
    for factor in prime_factorization(num_smiles, factors):
      num_seconds += factor
    return num_seconds

print print_smiles(6)
print print_smiles(11)
print print_smiles(1000)
print print_smiles(997)
print print_smiles(995)
prime_factorization(995, [])

# I tried to simulate a competition environment, so I used a naive sieve method for the prime factorization method.
# I also was unsure if it was within the rules to use the math module, so I used a while loop to calculate
# the logarithm and used a very rough linear approximation to square root. If speed were an issue (which it is not
# with such small size inputs) I would implement a sieve to compute the prime numbers within the range and then
# not do this with every computation.

