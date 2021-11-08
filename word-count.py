from word_count.nl_utils import get_src_corpus
from word_count.nl_utils import detokenize_sentence
from word_count.nl_utils import get_filtered_freq_dist
from word_count.nl_utils import get_src_corpus_text
from word_count.nl_utils import get_src_corpus_text_by_fileids

from word_count.data_utils import sentences_list_to_df
from word_count.data_utils import get_sentences_containing_word

from word_count.html_utils import render_and_write_to_html
from word_count.html_utils import render_and_write_to_html_singleton

from word_count.defaults import DEFAULT_MOST_COMMON_MAX

from re import sub

if __name__ == "__main__":

    src_corpus = get_src_corpus()

    file_ids = src_corpus.fileids()
    file_info = {k: {} for k in file_ids}

    # process each document individually
    for file_id in file_ids:
        file_name = file_id.replace(".txt", "")
        text = get_src_corpus_text_by_fileids([file_id])
        freq_dist = get_filtered_freq_dist(text)
        sentences_df = sentences_list_to_df(src_corpus.sents(fileids=file_id))
        for k, v in freq_dist.most_common(DEFAULT_MOST_COMMON_MAX):
            sentences = get_sentences_containing_word(sentences_df, k)
            file_info[file_id][k] = {
                "frequency": v,
                "sentences": [
                    sub(
                        fr"\b{k}\b",
                        f"<span class='word-highlight'>{k}</span>",
                        detokenize_sentence(sentence),
                    )
                    for sentence in sentences
                ],
            }

        render_and_write_to_html_singleton(
            file_id, file_info[file_id], len(file_info[file_id])
        )

    file_info["all_files"] = {}
    text = get_src_corpus_text()
    freq_dist = get_filtered_freq_dist(text)
    sentences_df = sentences_list_to_df(src_corpus.sents())
    for k, v in freq_dist.most_common(DEFAULT_MOST_COMMON_MAX):
        sentences = get_sentences_containing_word(sentences_df, k)
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
            "documents": [],
        }

    for key in file_ids:
        for word in file_info[key]:
            if word in file_info["all_files"]:
                if key not in file_info["all_files"][word]["documents"]:
                    file_info["all_files"][word]["documents"].append(key)

    # render the all_files page
    render_and_write_to_html(
        "all_files",
        file_info["all_files"],
        len(file_info["all_files"]),
    )
