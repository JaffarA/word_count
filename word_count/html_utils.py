from .defaults import DEFAULT_OUT_DIR
from .defaults import DEFAULT_JINJA_TEMPLATE


def render_template(title, data, template=DEFAULT_JINJA_TEMPLATE):
    return template.render(title=title, data=data)


def write_to_html_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return filename


def format_title_as_filename(title):
    return f"{DEFAULT_OUT_DIR}/{title}-out.html"
