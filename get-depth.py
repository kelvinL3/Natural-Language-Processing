from stanfordcorenlp import StanfordCoreNLP

server = StanfordCoreNLP('http://localhost', 9000)

def get_depth(sentence):
    parse = server.parse(sys.argv[1])

    depth = 0
    max_depth = 0
    for c in parse:
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1

        max_depth = max(depth, max_depth)
    return max_depth

def get_average_depth(lyrics):
    sentences = lyrics.split("\n")
    sum = 0
    for s in sentences:
        sum += get_depth(s)
    
    return sum / len(sentences)