from itertools import product

def get_subsequences(alph, n):
    subsequences = []
    n_tuples = list(product(alph, repeat=n))
    for item in n_tuples:
        subsequences.append(''.join(str(x) for x in item))
        
    return subsequences

def is_completed(subsequences, sequence):            
    if all(sub in sequence for sub in subsequences):
        return True
    else:
        return False
    
def de_bruijn(k, n):
    alphabet = [str(x) for x in range(k)]
    subsequences = get_subsequences(alphabet, n)
    sequence = n * str(alphabet[0])
    
    while(not is_completed(subsequences, sequence)):
        prev = sequence[-n+1:]
        current = [char for char in alphabet if prev + char not in sequence]
        char = current.pop()
        sequence += char
    
    return sequence