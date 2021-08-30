# {{cookiecutter.project_name}}

Title: {{cookiecutter.thesis_title}}
Author: {{cookiecutter.given_name}} {{cookiecutter.surname}}

{{cookiecutter.degree}} ({{cookiecutter.degree_abbreviation}}) thesis in partial completion of {{cookiecutter.program}} at Laurentian University in Sudbury, Ontario.

## Build system

The document utilises `latexmk` as its build system.

To build your document, run

```bash
    latexmk
```

in a terminal in the root directory of your project and `latexmk` will generate
the `pdf` file using the configuration settings in the `.latexmkrc` file.

## Credits

This project was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [stephen-young/cookiecutter-latex-laurentian-thesis](https://github.com/stephen-young/cookiecutter-latex-laurentian-thesis) project template.
