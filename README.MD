# word-counter

word-counter is a Python program for counting words using NLTK. 🔢

## Requirements

Python >=3.7.1,<3.11

Recommended version: 3.9.7

## Installation

Install Python if you dont already have it

[Python](https://www.python.org/downloads/)

Install Poetry

[Poetry](https://python-poetry.org/docs/#installation)

Clone the git repo

```bash
git clone https://github.com/JaffarA/word-count.git
```

Install requirements

```bash
poetry install
```

## Usage

Files are read from the ```src/``` directory, all ```.txt``` files found in that directory will be parsed. 

Populate the ```src/``` directory with all your documents (```example.txt``` is provided)

Run the main program.

```bash
# one liner
poetry run python word-count.py

## or
# load venv
poetry shell
python word-count.py
```

...outputs files in the ```out/``` directory in the projects directory with the same name as the input file found in ```src/```.

#### note: only the ```out/all_files-out.html``` output shows which documents the sentences came from, the example only has a single file shown as all the data came from the same file.
#### note: some words appear to have only one sentence, this is because by default only the first sentence is displayed, click on the word hyperlink (in the word (total occurences) column) to expand/collapse.

Light
![light](img/example-light.png)

Dark
![dark](img/example-dark.png)

## Features

Blacklist

A simple ```blacklist.txt``` file is available in the root directory, any text in this file will be ignored when counting words.

word_count library

All functions and methods called in ```word-count.py``` are available through ```word_count/*.py``` if you want to make any ammendments

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## FAQ

If any questions are ever asked, they will be answered here. 🙋

## License
[GPL-3](https://choosealicense.com/licenses/gpl-3.0/)