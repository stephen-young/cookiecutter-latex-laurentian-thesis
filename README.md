# cookiecutter-latex-laurentian-thesis

Template for creating a Laurentian University thesis with LaTeX and Cookiecutter.

Disclaimer: this is an unofficial template.

## Requirements

* Python
* LaTeX distribution (e.g. [TeX Live](https://tug.org/texlive/))
* [Perl](https://strawberryperl.com/)

This template implements `latexmk` as the document build system which will
require a Perl distribution to be installed on your system.

## Usage and options

Install `cookiecutter` if you don't have it already:

```bash
pip install cookiecutter
```

Generate your project:

```bash
cookiecutter gh:stephen-young/cookiecutter-latex-laurentian-thesis
```

You will be asked to enter these fields:

| Field                             | Default                                                  | Description                                                                         |
| --------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `project_name`                    | "Unofficial Laurentian University thesis LaTeX template" | Name of the project.                                                                |
| `project_slug`                    | "unofficial_laurentian_university_thesis"                | Folder name based on the project name.                                              |
| `thesis_title`                    | "Unofficial Laurentian thesis \\LaTeX{} template"        | Title of the thesis.                                                                |
| `program`                         | "Program"                                                | University program the thesis is for.                                               |
| `degree`                          | "Degree"                                                 | The degree to be attained with the thesis.                                          |
| `degree_abbreviation`             | "Abbr."                                                  | Abbreviation of the thesis.                                                         |
| `given_name`                      | "Stephen"                                                | Your given/first name.                                                              |
| `surname`                         | "Young"                                                  | Your surname or family name.                                                        |
| `supervisor`                      | "Supervisor"                                             | Name and title of your thesis supervisor (e.g. Dr. Albert Einstein).                |
| `cosupervisor`                    | "Co-Supervisor"                                          | Name and title of your thesis co-supervisor (if applicable).                        |
| `first_committee_member`          | "First Committee Member"                                 | Name and title of your first committee member                                       |
| `second_committee_member`         | "Second Committee Member"                                | Name and title of your second committee member                                      |
| `third_committee_member`          | "Third Committee Member"                                 | Name and title of your third committee member                                       |
| `external_examiner`               | "External Examiner"                                      | Name and title of your external examiner                                            |
| `internal_examiner`               | "Internal Examiner"                                      | Name and title of your internal examiner                                            |
| `en_dean_of_graduate_studies`     | "Dean of Graduate Studies"                               | Name and title of the Dean of Graduate Studies in English                           |
| `fr_dean_of_graduate_studies`     | "Doyen des \\'Etudes Sup\\'erieures"                     | Name and title of the Dean of Graduate Studies in French                            |
| `include_co_authorship_statement` | "y"                                                      | Includes the co-authorship statement section in the front matter, otherwise exclude |
| `include_preface`                 | "y"                                                      | Includes the preface section in the front matter, otherwise exclude                 |
| `include_plates`                  | "y"                                                      | Includes the plates environment if "y", otherwise exclude                           |
| `include_nomenclature`            | "y"                                                      | Includes the nomenclature package and commands if "y", otherwise exclude            |
