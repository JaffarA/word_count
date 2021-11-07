def get_blacklist_as_list(blacklist_file: str) -> list:
    """
    Load the blacklist from a file
    """
    return [line.replace("\n", "") for line in open(blacklist_file, "r")]
