import spacy
import time

nlp = None

def fill(ptr, visited):
    print("ptr = {}".format(ptr))
    
    # if this is the root, then the head points to itself
    if ptr.head == ptr:
        # if this is the first time we see root, then set to base case
        if ptr not in visited:
            visited[ptr] = 1
        return 1
    
    # if the parent has already been calculated, just add one
    if ptr.head in visited:
        visited[ptr] = visited[ptr.head] + 1
        return visited[ptr]
    
    # if the parent has not been seen before, 
    visited[ptr] = 1 + fill(ptr.head, visited)
    return visited[ptr]


def get_depth(sentence):
    global nlp
    
    timeA = time.time() 
    
    doc = nlp(sentence)
    
    for token in doc:
        print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])

    visited = {}
    max_depth = 0

    print("start")
    for token in doc:
        print(token)
        if token.text in visited:
            continue
        
        depth = fill(token, visited)
        if depth > max_depth:
            max_depth = depth

        print("token {} at depth {}".format(token.text, depth))
    
    elapsed = time.time() - timeA
    print("Time taken {}".format(elapsed))
    return max_depth


def get_average_depth(lyrics):
    global nlp
    
    nlp = spacy.load("en_core_web_sm")
    
    sentences = lyrics.split("\n")
    sum = 0
    for s in sentences:
        sum += get_depth(s)
    
    return sum / len(sentences)


# if __name__ == "__main__":
#     print(get_average_depth("The cow jumps over the moon"))