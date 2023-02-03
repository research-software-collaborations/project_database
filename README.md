[![CI](https://github.com/research-software-collaborations/projects/workflows/check_projects.yml/badge.svg)](https://github.com/research-software-collaborations/projects/workflows/check_projects.yml)
[![CI](https://github.com/research-software-collaborations/projects/workflows/yaml_checker.yml/badge.svg)](https://github.com/research-software-collaborations/projects/workflows/yaml_checker.yml)

# Open proejcts in high-energy and nuclear physics research software

There are two main components of this repository:
- project_metadata.yml that defines the set of fields that describe a project and known values for each field
- a directory of projects: one yml per project

Both of these can be updated via a pull request to this repository

## project_metadata
- Has a set of attributes, and possible values for each attribute.
- You might find that the set of possible values does not meet your needs. If not, add a new value and make a pull request.
- You might find that you would like a new attribute. If so, please open an issue for discussion in this repository.

## Adding a new project
- Clone this repository so that you can make a pull request against it
- Copy projects/template.yml.txt to a new file named for your project
- Replace each field with either a descriptive entry for your project (its title, description) or by one of the values from the project_metadata.yml file
(for entries where there is a multiple choice of options)
- Make a pull request against this repository to include your new project

## Changing the status of your project
- Projects can be changed/removed by their owner via pull request at any time. We encourage projects that have been filled or are no
longer relevant to be updated accordingly.

## Testing/visualizing your entry
- Instructions to come..

