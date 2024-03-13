import yaml
from jinja2 import Environment, FileSystemLoader
from os.path import dirname, abspath, basename, join
from src.experience_type import ExperienceEvent

# Allows any created files to go to the /dist directory
BASE_PATH = dirname(abspath(__file__))
DIST_DIR  = 'dist'
DIST_PATH = join(BASE_PATH, DIST_DIR)


# Rewrite Jinja2 to work with Latex \JINJA command
env = Environment(
    block_start_string="\\JINJA{",
    block_end_string="}",
    variable_start_string="\\JINJAVAR{",
    variable_end_string="}",
    comment_start_string="\\#{",
    comment_end_string="}",
    line_statement_prefix="%%",
    line_comment_prefix="%#",
    trim_blocks=True,
    autoescape=False,
    loader=FileSystemLoader(BASE_PATH),
)


