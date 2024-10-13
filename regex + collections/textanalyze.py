import re
from re import search

PREP = ['in', 'from', 'to', 'on', 'out', 'at']
CONJ = ['but', 'because', 'although', 'so', 'and']
PRON = ['you', 'I', 'me', 'he', 'him', 'himself', 'ourselves', 'mine', 'hers']
ARTICLES = ['a', 'an', 'the']
INTERJ = ['yipe', 'yum', 'yak', 'ugh', 'huh']
ORDINALS = [r'\b\d+(st|nd|rd|th)\b']

date_regex = '^[a-zA-Z]+ \d+(st|nd|rd|th) \d+$'

