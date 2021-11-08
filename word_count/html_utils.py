from .defaults import DEFAULT_OUT_DIR
from .defaults import DEFAULT_JINJA_TEMPLATE
from .defaults import DEFAULT_JINJA_TITLE
from .defaults import DEFAULT_JINJA_CONTENT
from .defaults import DEFAULT_JINJA_CONTENT_SINGLETON


def render_template(
    title, data, n_words, content_template=DEFAULT_JINJA_CONTENT_SINGLETON
):
    title_section = DEFAULT_JINJA_TITLE.render(title=title, n_words=n_words)
    table_section = content_template.render(title=title, words=data)
    return DEFAULT_JINJA_TEMPLATE.render(
        title_section=title_section,
        table_section=table_section,
    )


def write_to_html_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return filename


def format_title_as_filename(title):
    return f"{DEFAULT_OUT_DIR}/{title}-out.html"


def render_and_write_to_html_singleton(
    title, data, n_words, content_template=DEFAULT_JINJA_CONTENT_SINGLETON
):
    return write_to_html_file(
        filename=format_title_as_filename(title),
        data=render_template(title, data, n_words, content_template),
    )


def render_and_write_to_html(
    title, data, n_words, content_template=DEFAULT_JINJA_CONTENT
):
    return write_to_html_file(
        filename=format_title_as_filename(title),
        data=render_template(title, data, n_words, content_template),
    )
