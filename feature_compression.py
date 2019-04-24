def remove_ascii(string):
    return ''.join([i if ord(i) < 128 else ' ' for i in string])

def compress(uncompressed):
    if len(uncompressed) == 0:
        print("No lyrics for feature_compression.py")
        return 0
    # remove all non-ascii letters
    uncompressed = remove_ascii(uncompressed)
    
    
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    # try:
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    
    # Output the code for w.
    if w:
        result.append(dictionary[w])

    
    # we only care about the length of the array, representing how small the sentence can be reduced to
    # since each song can be different lengths, normalize by dividing by length of song
    return len(result) / len(uncompressed)

# if __name__ == "__main__":
#     print(compress("asjaljlsajkfl;sajfklkfal"))
#     print(compress("abcabc baa baa baa baa"))