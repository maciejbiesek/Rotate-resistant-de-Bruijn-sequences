from itertools import product

transit = {}

def get_subsequences(alph, n):
    subsequences = []
    n_tuples = list(product(alph, repeat=n))
    for item in n_tuples:
        subsequences.append(''.join(str(x) for x in item))
        
    return subsequences

def is_completed_rr(subsequences, sequences):
    count = 0
    for sub in subsequences:
        if any(sub in sequence for sequence in sequences):
            count += 1
    
    if count == len(subsequences):
        return True
    else:
        return False
    
def get_last_non_zero(seq):
    for i in range(len(seq)-1, 0, -1):
        if seq[i] != 0:
            return i
        
    return -1
        
def get_possible_chars(sequences, prev, alphabet):
    possible_chars = [char for char in alphabet if not any(prev + char in sequence for sequence in sequences)]
    lst = []
    
    if sequences[0] in transit:
        lst = transit[sequences[0]]
        possible_chars = [x for x in possible_chars if x not in lst]
        if possible_chars:
            transit[sequences[0]].append(possible_chars[len(possible_chars)-1])
    else:
        if possible_chars:
            transit[sequences[0]] = [possible_chars[len(possible_chars)-1]]
        
    return possible_chars
        
def trim_seq(idx, n, sequences, flags, alphabet):
    for i in range(len(sequences)):
        sequences[i] = sequences[i][:idx]
    flags = flags[:idx]
            
    prev = sequences[0][-n+1:]
    current = get_possible_chars(sequences, prev, alphabet)
    flags.append(len(current))
    
    return sequences, flags, current

def find_next(sequences, current, alphabet):
    char = current.pop()
    sequences[0] += char
    idx = alphabet.index(char)
    current_alph = alphabet[idx+1:] + alphabet[:idx]
    for i in range(1, len(sequences)):
        sequences[i] += current_alph[i-1]
        
    return sequences

def de_bruijn_rotate_resistant(k, n):
    alphabet = [str(x) for x in range(k)]
    subsequences = get_subsequences(alphabet, n)
    sequences = [n * str(char) for char in alphabet]
    flags = [0 for i in range(3)]
    
    while(not is_completed_rr(subsequences, sequences)):
        prev = sequences[0][-n+1:]
        current = get_possible_chars(sequences, prev, alphabet)
    
        if current:
            flags.append(len(current))
            sequences = find_next(sequences, current, alphabet)
            
        else:
            while not current:
                idx = get_last_non_zero(flags)
                if idx == -1:
                    return "de Bruijn sequence cannot be generate"
                    
                sequences, flags, current = trim_seq(idx, n, sequences, flags, alphabet)
            
            sequences = find_next(sequences, current, alphabet)
        
    return sequences[0]
