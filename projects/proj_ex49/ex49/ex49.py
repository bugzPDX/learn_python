# Code for exercise 49

# from ex48.ex48 import lexicon


class ParserError(Exception):
    pass


class Sentence(object):

    """Takes in (type, word) tuples and uses the words to create
    a sentence object in the form subject, verb, object.
    ex. ('noun', 'princess'), ('verb', 'eat'), ('noun', 'apple')
    returns 'princess eat apple'

    """

    def __init__(self, subject, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):

    """Takes in a list of tuples. Sets the first tuple = to
    the word variable and then returns the type entry in
    the tuple. ex ('verb', 'run') returns 'verb'.

    """

    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):

    """ Takes in a word list of tuples and an expected
    type. The first tuple is popped from the list and
    if the type matches the expected type the popped
    tuple is returned.

    """

    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):

    """ Takes a list of tuples and a word type. While
    the tuple type matches the word type the match function
    is called and the list and type are passed to it. The
    match function is called until the tuple type and
    word type no longer match.

    """

    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):

    """ Takes a list of tuples. If the first
    tuple contains type 'stop' the tuple is skipped.
    if the tuple is of type 'verb', the tuple and
    type 'verb' are returned. If the type is
    anything else a ParserError is raised.

    """

    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):

    """ Takes a list of tuples. If the first tuple
    contains type 'stop' the tuple is skipped otherwise
    the variable 'next' is set to the tuple type. If
    next equals type 'noun' the tuple and type 'noun'
    are returned. If next equals type 'direction'
    the tuple and type 'direction' are returned
    otherwise a ParserError is raised.

    """

    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):

    """ Takes a list of tuples and a subject tuple of type
    ('noun', 'i') for example. The list of tuples is
    then parsed for a verb and then an object by
    being passed to these two functions and then returns
    a Sentence object with these values.

    """

    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


def parse_sentence(word_list):

    """ Takes a list of tuples. If the zeroith element of
    the list contains type 'stop' the tuple is skipped
    otherwise the variable 'start' is set to the tuple
    type. If tuple type equals 'noun' the tuple is set
    to the variable subj then the word list and subj
    variable are passed to parse_subject and the
    result is returned to the caller.

    """

    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # asume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, \
            or verb. Not: %s" % start)
