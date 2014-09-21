"""Build a sentence tokenizer for a language. Greek below.
Some guidance available here: http://wiki.apertium.org/wiki/Sentence_segmenting
"""

__author__ = 'Kyle P. Johnson <kyle@kyle-p-johnson.com>'
__license__ = 'MIT License. See LICENSE.'

from nltk.tokenize.punkt import PunktLanguageVars
from nltk.tokenize.punkt import PunktTrainer
import pickle


def train_from_file(training_file):
    """Make a ruleset from a file."""
    language_punkt_vars = PunktLanguageVars
    language_punkt_vars.sent_end_chars = ('.', ';',)
    language_punkt_vars.internal_punctuation = (',', '·')
    with open(training_file) as f:
        train_data = f.read()
    trainer = PunktTrainer(train_data, language_punkt_vars)
    with open('greek.pickle', 'wb') as f:
        pickle.dump(trainer, f)

if __name__ == '__main__':
    """For debugging."""
    training_file = 'training_sentences.txt'
    train_from_file(training_file)
