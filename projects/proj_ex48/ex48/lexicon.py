lexicon = {
    'north' : 'direction',
    'south' : 'direction',
    'east' : 'direction',
    'west' : 'direction',
    'go' : 'verb',
    'kill' : 'verb',
    'eat' : 'verb',
    'the' : 'stop',
    'in' : 'stop',
    'of' : 'stop',
    'bear' : 'noun',
    'princess' : 'noun',

        }



def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if word in lexicon:
            pair = (lexicon[word], word)
            result.append(pair)
        else:
            num = convert_number(word)
            if num:
                numb = 'number'
                word = num
                result.append((numb, word))
            else:
                result.append(('error', word))
    return result