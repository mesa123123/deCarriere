from os.path import abspath, dirname, join, pardir
from jinja2 import Environment, FileSystemLoader
from src.cust_types import LocaleType

RESUME_NAME = "Peter Bowman"
LOCALE = LocaleType.NZ
BASE_PATH = abspath(join(dirname(__file__), pardir))
DIST_DIR = "dist"
DIST_PATH = join(BASE_PATH, DIST_DIR)
DATA_PATH = join(BASE_PATH, "Data/")
JINENV = Environment(
    block_start_string="\\JINJA{",
    block_end_string="}",
    variable_start_string="\\JINVAR{",
    variable_end_string="}",
    comment_start_string="\\#{",
    comment_end_string="}",
    line_statement_prefix="%%",
    line_comment_prefix="%#",
    trim_blocks=True,
    autoescape=False,
    loader=FileSystemLoader(BASE_PATH),
)
