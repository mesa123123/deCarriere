from os import makedirs
from os.path import basename, join
from subprocess import DEVNULL, run

import yaml

from src.content_writer import main as write_content
from src.definitions import DIST_PATH


def main():
    tex_file = "resume_test"
    resume = write_content()

    makedirs(DIST_PATH, exist_ok=True)

    tex_output_path = join(DIST_PATH, f"{tex_file}.tex")
    # Write Text File
    with open(tex_output_path, "w", encoding="utf-8") as output:
        output.write(resume)
    # Write Pdf
    # cmd = ["latexmk", "-pdf", basename(tex_output_path)]
    # status = run(cmd, cwd=DIST_PATH, stdout=DEVNULL, stderr=DEVNULL, check=False)
    # Check the result
    # if status.returncode != 0:
    #     return 1
    # return 0


if __name__ == "__main__":
    main()
