# CIS6930FA24 -- Assignment 0

**Name:** Prajay Yalamanchili

## Assignment Description

The aim of this assignment is to extract the Title, Subject, and Field Offices from the FBI API, process the extracted information, and print it in a thorn-separated format as follows:

> {title}{thorn}{subjects}{thorn}{field_offices}

## How to Install

**For Windows:**

1. If Python is not already installed on your system, download and install Python version 3.12 from [here](https://www.python.org/downloads/).
2. Set your path in the environment variables. To learn how to set path in environment variables, read this [article](https://www.liquidweb.com/help-docs/adding-python-path-to-windows-10-or-11-path-environment-variable/).
3. Download or clone this repository.
4. Navigate to the project directory on your local machine.
5. Run the following commands:

    ```bash
    pip install pipenv
    ```
    ```bash
    pipenv install
    ```

## How to Run

To execute the `main.py` file, use:
```bash
pipenv run python main.py --page PAGE
pipenv run python main.py --file FILE
```
To run tests, use:
```bash
pipenv run python -m pytest -v
```
or

```bash
pipenv run pytest
```

<!-- ## Example
![video](video) -->

## Folder Structure
```
cis6930fa24-assignment0
|   COLLABORATORS.md
|   main.py
|   Pipfile
|   Pipfile.lock
|   README.md
|   setup.cfg
|   setup.py
|                 
+---docs
+---LICENSE
+---Resources
|       data.json
|       
\---tests
    |   test_main.py
```

- **COLLABORATORS.md:** Contains information about collaborators and a list of resources used for the assignment.
- **main.py:** Processes command-line arguments to either fetch data from the API or use a local file. Calls appropriate functions to handle data retrieval and formatting.
- **Pipfile:** Manages the Python virtual environment and lists all dependencies.
- **Pipfile.lock:** Specifies the versions of dependencies to ensure consistent environments.
- **README.md:** This file, which documents the assignment.
- **setup.cfg** and **setup.py:** Used for setting up the Python environment.
- **docs:** Contains documentation for the assignment.
- **LICENSE:** Contains licensing information, including copyright, publishing, and usage rights.
- **Resources:** Stores data files, including `data.json`, which contains data from the FBI API (page 1) used for testing.
- **tests:** Contains test files. `test_main.py` is used for testing the main Python file.

## `main.py`

**Functions in `main.py`:**

### `main(page=None, thefile=None)`
This function processes command-line arguments. It calls the `downloadData` function if a page number is provided, or the `parsefile` function if a file location is provided.

### `downloadData(page)`
This function takes a page number as an argument, calls the FBI API to retrieve data, and returns the data in dictionary format.

### `parsefile(file_location)`
This function takes a file location, parses the file, and returns the data in dictionary format.

### `reformat(data)`
This function formats the data and prints it in a thorn-separated field format.

## `test_main.py`

**Functions in `test_main.py`:**

### `test_non_empty_page()`
Tests whether data is being fetched from the FBI API. It runs from Page 1 to Page 52, with 5-page increments each time. Page 52 is the last page from which data has been successfully retrieved as of 9/7/24.

### `test_empty_page()`
Tests whether the `downloadData` function returns an empty dataset when an invalid page number is provided.

### `test_parse_file()`
Tests whether the `parseFile` function correctly parses the JSON data from a valid file location.

### `test_invalid_parse_file()`
Tests whether the `parseFile` function handles errors gracefully when an invalid file location is provided .

### `test_title_extraction()`
Checks whether titles are correctly extracted and verifies the data type received.

### `test_subjects_extraction()`
Checks whether subjects are correctly extracted and verifies the data type received.

### `test_field_extraction()`
Checks whether field offices are correctly extracted and verifies the data type received.

### `test_reformat()`
Checks whether the printed output is in correct format

## Bugs and Assumptions

- Calling the API after page 52 returns empty items. Similarly, page 999 also returns empty items. Pages above 1000 result in a timeout error or CAPTCHA. It is suspected that there is rate limiting for API calls above page 999.
- Data on FBI pages changes daily, so testing with an old downloaded file may result in errors.
- Calling API too frequently results in temporary ban of client.
- Users running this code may encounter errors if there are compatibility issues with the installed dependencies.
