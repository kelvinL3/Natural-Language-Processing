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