from .blacklist_utils import get_blacklist_as_list

from sacremoses import MosesDetokenizer
from nltk.corpus import stopwords
from string import punctuation
from jinja2 import Template
from numpy import array

DEFAULT_SRC_DIR = "./src/"
DEFAULT_SRC_REGEX = ".*\.txt"

DEFAULT_BLACKLIST_FILE = "blacklist.txt"
DEFAULT_WORD_BLACKLIST = array(
    [p for p in punctuation]
    + list(stopwords.words("english"))
    + get_blacklist_as_list(DEFAULT_BLACKLIST_FILE),
    dtype=str,
)

DEFAULT_OUT_DIR = "./out"

DEFAULT_JINJA_TEMPLATE = Template(open("templates/base.html").read())
DEFAULT_JINJA_TITLE = Template(open("templates/title.html").read())
DEFAULT_JINJA_CONTENT = Template(open("templates/content.html").read())
DEFAULT_JINJA_CONTENT_SINGLETON = Template(
    open("templates/content_singleton.html").read()
)

DEFAULT_DETOKENIZER = MosesDetokenizer(lang="en")

DEFAULT_MOST_COMMON_MAX = 20
