
def prime_factorization(number, factors):
    
    possible_factors = range(2,1000)
    number_to_factor = number
    
    if number_to_factor == 1:
        return factors
    
    for possible_factor in possible_factors:
        times_appearing = 0    
        
        if number_to_factor % possible_factor == 0 and \
            possible_factor <= number_to_factor:
        
            while number_to_factor % possible_factor == 0:
                times_appearing += 1
                number_to_factor /= possible_factor
                
            for _ in range(times_appearing):
                factors.append(possible_factor)
                
            possible_factors = [factor for factor in possible_factors if factor % possible_factor != 0]
            return prime_factorization(number_to_factor, factors)


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
    

