from jinja2 import Template

# read jinja template
default_template = Template(open("data-out.html").read())


def render_template(title, data, template=default_template):
    return template.render(title=title, data=data)


def write_to_html_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return filename


def format_title_as_filename(title):
    return f"out/{title}-out.html"
