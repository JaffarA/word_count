import pandas as pd


def get_sentences_containing_word(df: pd.DataFrame, word: str) -> list:
    """Returns a list of sentences containing a word from a dataframe created with 'sentences_list_to_df'.

    Args:
        df (pd.DataFrame): df containing sentences
        word (str): word to search for

    Returns:
        list: list of sentences containing the word
    """
    return df[df.sentences.apply(lambda x: word in x)].to_numpy().flatten()


def is_word_in_sentences(df: pd.DataFrame, word: str) -> bool:
    """Returns a bool indicating if a word is in a dataframe created with 'sentences_list_to_df'.

    Args:
        df (pd.DataFrame): df containing sentences
        word (str): word to search for

    Returns:
        bool: bool indicating if the word is in the dataframe
    """
    return not df[df.sentences.apply(lambda x: word in x)].empty


def sentences_list_to_df(sentences: list) -> pd.DataFrame:
    """Converts a list of sentences to a dataframe.

    Args:
        sentences (list): list of sentences

    Returns:
        pd.DataFrame: dataframe containing the sentences
    """
    return pd.DataFrame({"sentences": sentences})
