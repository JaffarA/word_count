from word_count.nl_utils import get_src_corpus
from word_count.nl_utils import detokenize_sentence
from word_count.nl_utils import get_filtered_freq_dist
from word_count.nl_utils import get_src_corpus_text
from word_count.nl_utils import get_src_corpus_text_by_fileids

from word_count.data_utils import sentences_list_to_df
from word_count.data_utils import is_word_in_sentences
from word_count.data_utils import get_sentences_containing_word

from word_count.html_utils import render_and_write_to_html
from word_count.html_utils import render_and_write_to_html_singleton

from word_count.defaults import DEFAULT_MOST_COMMON_MAX

from re import sub


if __name__ == "__main__":

    # read all files in src/ directory
    src_corpus = get_src_corpus()

    # get all fileids of documents scanned by get_src_corpus()
    file_ids = src_corpus.fileids()
    # create dict structure to store all words and their frequencies
    file_info = {k: {} for k in file_ids}

    # empty dict used to store DF objects for each file
    # (performance optimization) -
    #   when in all_files document loop
    #   we can access these instead of recreating each DF
    sentences_dfs = {}

    # process each document (fileid) individually
    for file_id in file_ids:

        # get text for that file
        text = get_src_corpus_text_by_fileids([file_id])

        # generate frequency distribution
        #   filtered function is used to filter out stopwords and punctuation
        freq_dist = get_filtered_freq_dist(text)

        # generate df object to store all sentences for that file
        sentences_dfs[file_id] = sentences_list_to_df(src_corpus.sents(fileids=file_id))

        # iterate over most common words to populate file_info dict
        for k, v in freq_dist.most_common(DEFAULT_MOST_COMMON_MAX):
            # get all sentences containing the word (k)
            sentences = get_sentences_containing_word(sentences_dfs[file_id], k)
            # dict comprehension to store all sentences in file_info for that file_id/word
            file_info[file_id][k] = {
                "frequency": v,
                "sentences": [
                    # detokenize and highlight sentences for HTML rendering
                    sub(
                        fr"\b{k}\b",  # format string (f) + regex (r) = (fr)
                        f"<span class='word-highlight'>{k}</span>",
                        detokenize_sentence(sentence),
                    )  # this sub could be done in JS on the page
                    for sentence in sentences
                ],
            }

        # write out/*.html file for that file_id
        render_and_write_to_html_singleton(
            file_id, file_info[file_id], len(file_info[file_id])
        )

    # process all documents together
    file_info["all_files"] = {}

    # use get_src_corpus_text instead of by_fileids to read all documents
    text = get_src_corpus_text()
    freq_dist = get_filtered_freq_dist(text)
    sentences_dfs["all_files"] = sentences_list_to_df(src_corpus.sents())

    # same loop as for individual files but we add documents to the dict
    for k, v in freq_dist.most_common(DEFAULT_MOST_COMMON_MAX):
        sentences = get_sentences_containing_word(sentences_dfs["all_files"], k)
        file_info["all_files"][k] = {
            "frequency": v,
            "sentences": [
                sub(
                    fr"\b{k}\b",
                    f"<span class='word-highlight'>{k}</span>",
                    detokenize_sentence(sentence),
                )
                for sentence in sentences
            ],
            # blank documents list to hold documents this sentence was found in
            "documents": [],
        }

    # fill documents list for each word in file_info["all_files"]
    for file_id in file_ids:  # iterate over all files
        sentences_df = sentences_dfs[file_id]  # grab previously stored df
        for word in file_info["all_files"]:
            if file_id not in file_info["all_files"][word]["documents"]:
                if is_word_in_sentences(sentences_df, word):
                    file_info["all_files"][word]["documents"].append(file_id)
                    # append document to document list for that word

    # render the all_files page
    render_and_write_to_html(
        "all_files",
        file_info["all_files"],
        len(file_info["all_files"]),
    )
