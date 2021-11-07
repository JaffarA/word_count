from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text

from numpy import array
from numpy import char
from numpy import isin

from .defaults import DEFAULT_SRC_DIR
from .defaults import DEFAULT_SRC_REGEX
from .defaults import DEFAULT_WORD_BLACKLIST


def get_src_corpus(
    dir=DEFAULT_SRC_DIR,
    regex=DEFAULT_SRC_REGEX,
) -> PlaintextCorpusReader:
    return PlaintextCorpusReader(dir, regex)


def get_src_corpus_text() -> Text:
    """Returns a nltk.Text object reading all .txts in the default src/ directory.

    Returns:
        Text: nltk.Text object
    """
    return Text(get_src_corpus().words())


def get_freq_dist_from_text(text: Text) -> FreqDist:
    """Generates an unfiltered frequency distribution from a text object using FreqDist, including all characters including punctuation.

    Args:
        text (Text): text object to transform

    Returns:
        FreqDist: frequency distribution object
    """
    return FreqDist(text)


def get_filtered_freq_dist(text: Text) -> FreqDist:
    """Returns a filtered frequency distribution from a text object using FreqDist, excluding punctuation and stopwords (nltk.corpus.stopwords.words('english')).

    Args:
        text (Text): text object to transform

    Returns:
        FreqDist: frequency distribution object
    """
    arr = array(text.tokens)
    return get_freq_dist_from_text(arr[~isin(char.lower(arr), DEFAULT_WORD_BLACKLIST)])
