[![CI](https://github.com/research-software-collaborations/project_database/actions/workflows/check_projects.yml/badge.svg)](https://github.com/research-software-collaborations/project_database/actions/workflows/check_projects.yml)
[![CI](https://github.com/research-software-collaborations/project_database/actions/workflows/yaml_checker.yml/badge.svg)](https://github.com/research-software-collaborations/project_database/actions/workflows/yaml_checker.yml)

# Open projects in high-energy and nuclear physics research software

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
- Projects can be changed/removed via pull request at any time. We encourage projects that have been filled or are no
longer relevant to be updated accordingly.
- Projects that are complete or in progress require a "link" field used to document the project results (eg, a project webpage, etc)
- For example, the following should be done when work on a project has started:
  - Find the corresponding project in the ```project``` directory
  - Edit the ```status``` to be ```In progress```
  - Add an entry in the mentees list (or add ```mentees:``` to start one) and then add the name (```  name: <name>```) and project page
    link  (```  link: project-webpage```) to allow everyone to find the ongoing work
  - Make a pull request with these changes (see above more for information

## Testing/visualizing your entry
- This repo uses precommit-ci. Consider using pre-commit locally
- Two scripts will run on PRs. To check that they work ok with your change
-  ```python3 _scripts/check_projects.py projects/*```
-  ```yamllint -c _scripts/yaml_lint.rules projects/.``` (yamllist is installed by ```pip install yamllist``` for example)
- [Instructions for building the webpage with all projects are maintained here](https://github.com/research-software-collaborations/research-software-collaborations.github.io/blob/master/README.md#testing-a-new-project-or-other-development-in-the-project_database-repo)

