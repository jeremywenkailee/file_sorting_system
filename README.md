# FILE SORTING AUTOMATION (Python)

## SETUP
### .env config
- SOURCE_FOLDER: absolute/relative path for files that need sorting
- DESTINATION_FOLDER: absolute/relative path for sorted files

### filters.json config
A sample filters.json has been provided. To add more folders/selectors, add a new object into the array with "name" and "type" descriptors.
- name: the name of the folder
- type: an array of the acceptable types for the folder

Subdirectories can be made by adding a new node with "Parent\\Child" folder names in the name descriptor.

## RUNNING THE PROGRAM
- navigate to the root folder
- type ```python file_organizer.py``` into the command line
