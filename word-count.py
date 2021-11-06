from sys import argv
from jinja2 import Template

# read blacklist file, split at '/n's and put into a list
blacklist = [s.rsplit("\n") for s in open("blacklist.txt", "r")]

# read jinja template
html_template = Template(open("data-out.html").read())

# arguments can be passed at run like 'python main.py arg'
# or can be input in program
if len(argv) > 1:
    f = open(f"src/{argv[1]}", "r").read()
    title = argv[1].split(".")[0]
else:
    src, f, title = input("name: ")
    f, title = open(f"src/{src}", "r").read(), src.split(".")[0]


# counts all words in a string and returns a dictionary
def count_words(str):
    all_words = str.split()
    w, c = list(), dict()
    for word in all_words:
        if word.lower() in blacklist:
            pass
        else:
            if word in w:
                c[word] += 1
            else:
                w.append(word)
                c[word] = 1
    return c


# takes a dictionary and outputs it to a html file in the OUT/ directory
# uses data-out.html template in root directory
def dict_to_html(d):
    filename = f"out/{title}-out.html"
    out = html_template.render(
        title=title,
        data={
            k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)
        },
    )
    f = open(filename, "w")
    f.write(out)
    f.close()
    return filename


# feel free to comment out lines if functionality is not required.
# creates a dictionary containing all words present and their frequencies
data = count_words(f)
# takes a dictionary and returns a html file with a table of values
output_file = dict_to_html(data)
