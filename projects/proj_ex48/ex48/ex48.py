# Lexicon function for testing word types
class Lexicon(object):

    def __init__(self):

        vocabulary = {
            'direction': 'north east south west up \
            down left right back'.split(),
            'noun': 'bear princess door cabinet'.split(),
            'stop': 'the in of from at it'.split(),
            'verb': 'go kill eat stop'.split(),
        }

        classifications = {}
        for word_type, lex_entry in vocabulary.iteritems():
            for i in lex_entry:
                classifications[i] = word_type

        self.classifications = classifications

    def scan(self, sentence):

        words = sentence.split()
        whatever = []
        for word in words:
            what = None
            if word in self.classifications:
                what = self.classifications[word]
            else:
                num = convert_number(word)
                if num:
                    what = 'number'
                    word = num

            if what:
                whatever.append((what, word))
            else:
                whatever.append(('error', word))
        return whatever


def convert_number(num):
    try:
        return int(num)
    except ValueError:
        return None

lexicon = Lexicon()
