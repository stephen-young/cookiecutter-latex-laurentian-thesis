import os
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(filepath):
    os.remove(filepath)


if __name__ == '__main__':

    if '{{cookiecutter.include_preface}}' != 'y':
        remove_file(PROJECT_DIRECTORY / 'contents' / 'preface.tex')

    if '{{cookiecutter.include_co_authorship_statement}}' != 'y':
        remove_file(PROJECT_DIRECTORY / 'contents' / 'co-authorship-statement.tex')

