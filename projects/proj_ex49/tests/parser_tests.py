from nose.tools import assert_equal, assert_raises
from ex49.ex49 import *


def test_Sentence():
    sentence = Sentence(("noun", "princess"), ("verb", "eat"),
                        ("noun", "apple"))
    assert_equal(sentence.subject, "princess")
    assert_equal(sentence.verb, "eat")
    assert_equal(sentence.object, "apple")


def test_peek():

    my_peek = peek([('verb', 'go'), ('noun', 'door')])
    assert_equal(my_peek, 'verb')

    my_peek = peek([])
    assert_equal(my_peek, None)


def test_match():

    my_match = match([('verb', 'go')], 'verb')
    assert_equal(my_match, ('verb', 'go'))

    my_match = match([('verb', 'go'), ('noun', 'princess')], 'verb')

    my_match = match([('noun', 'door')], 'verb')
    assert_equal(my_match, None)

    my_match = match([], 'noun')
    assert_equal(my_match, None)


def test_skip():

    my_skip = [('verb', 'go'), ('verb', 'go'),
               ('verb', 'go'), ('noun', 'princess')]
    skip(my_skip, 'verb')
    assert_equal(my_skip, [('noun', 'princess')])

    my_skip = [('noun', 'door'), ('noun', 'princess'),
               ('verb', 'eat'), ('noun', 'apple')]
    skip(my_skip, 'noun')
    assert_equal(my_skip, [('verb', 'eat'), ('noun', 'apple')])

    my_skip = []
    skip(my_skip, 'verb')
    assert_equal(my_skip, [])

    my_skip = [('verb', 'go')]
    skip(my_skip, 'verb')
    assert_equal(my_skip, [])


def test_parse_verb():

    my_parse_verb = [('stop', 'i'), ('verb', 'eat'),
                     ('stop', 'the'), ('noun', 'apple')]
    parse_verb(my_parse_verb)
    assert_equal(my_parse_verb, [('stop', 'the'), ('noun', 'apple')])

    my_parse_verb = [('noun', 'door'), ('verb', 'run')]
    assert_raises(ParserError, parse_verb, my_parse_verb)


def test_parse_object():

    my_parse_object = [('stop', 'the'), ('noun', 'bear'),
                       ('stop', 'is'), ('error', 'happy')]
    parse_object(my_parse_object)
    assert_equal(my_parse_object, [('stop', 'is'), ('error', 'happy')])

    my_parse_object = [('verb', 'run')]
    assert_raises(ParserError, parse_object, my_parse_object)


def test_parse_subject():

    my_parse_subject = [('stop', 'i'), ('verb', 'love'), ('noun', 'princess')]
    my_subject = parse_subject(my_parse_subject, ('stop', 'i'))
    assert_equal(my_parse_subject, [])

    assert_equal(my_subject.subject, 'i')
    assert_equal(my_subject.verb, 'love')
    assert_equal(my_subject.object, 'princess')


def test_parse_sentence():

    my_parse_sentence = [('stop', 'i'), ('verb', 'love'), ('noun', 'princess')]
    my_sentence = parse_sentence(my_parse_sentence)
    assert_equal(my_parse_sentence, [])
    assert_equal(my_sentence.subject, 'player')
    assert_equal(my_sentence.verb, 'love')
    assert_equal(my_sentence.object, 'princess')

    my_parse_sentence = [('direction', 'north'), ('verb', 'go')]
    assert_raises(ParserError, parse_sentence, my_parse_sentence)
