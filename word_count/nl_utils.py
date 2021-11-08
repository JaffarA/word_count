from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text

from numpy import array
from numpy import char
from numpy import isin

from .defaults import DEFAULT_SRC_DIR
from .defaults import DEFAULT_SRC_REGEX
from .defaults import DEFAULT_WORD_BLACKLIST
from .defaults import DEFAULT_DETOKENIZER as md  # moses detokenizer (md)


def get_src_corpus(
    dir=DEFAULT_SRC_DIR,
    regex=DEFAULT_SRC_REGEX,
) -> PlaintextCorpusReader:
    """Returns a nltk.corpus.PlaintextCorpusReader object reading all .txts in the default src/ directory.

    Returns:
        PlaintextCorpusReader: nltk.corpus.PlaintextCorpusReader object
    """
    return PlaintextCorpusReader(dir, regex)


def get_src_corpus_text() -> Text:
    """Returns a nltk.text.Text object reading all .txts in the default src/ directory.

    Returns:
        Text: nltk.text.Text object
    """
    return Text(get_src_corpus().words())


def get_src_corpus_text_by_fileids(fileids) -> Text:
    """Returns a nltk.text.Text object reading all .txts in the default src/ directory.

    Args:
        fileids (str): fileid to read from

    Returns:
        Text: nltk.text.Text object
    """
    return Text(get_src_corpus().words(fileids=fileids))


def get_freq_dist_from_text(text: Text) -> FreqDist:
    """Generates an unfiltered frequency distribution from a text object using FreqDist, including all characters including punctuation.

    Args:
        text (Text): text object to transform

    Returns:
        FreqDist: frequency distribution object
    """
    return FreqDist(text)


def get_filtered_freq_dist(text: Text, blacklist=DEFAULT_WORD_BLACKLIST) -> FreqDist:
    """Returns a filtered frequency distribution from a text object using FreqDist, excluding punctuation and stopwords (nltk.corpus.stopwords.words('english')).

    Args:
        text (Text): text object to transform
        blacklist (list, optional): Defaults to DEFAULT_WORD_BLACKLIST.

    Returns:
        FreqDist: frequency distribution object
    """
    arr = array(text.tokens)
    return get_freq_dist_from_text(arr[~isin(char.lower(arr), blacklist)])


def detokenize_sentence(tokenized_sentence: list) -> str:
    """Returns a detokenized string from a tokenized sentence.

    Args:
        tokenized_sentence (list): list of tokens

    Returns:
        str: detokenized string
    """
    return md.detokenize(tokenized_sentence)
