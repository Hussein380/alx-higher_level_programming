# Python Object-Relational Mapping (ORM) with MySQL

This project focuses on integrating Python with MySQL databases using Object-Relational Mapping (ORM) techniques. By leveraging tools like SQLAlchemy, it simplifies database operations by abstracting SQL queries and allowing developers to interact with databases using Python objects.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Credits](#credits)
- [License](#license)

# Description

In this project, we explore how to connect Python scripts with MySQL databases using both low-level and ORM approaches. The tasks cover basic CRUD (Create, Read, Update, Delete) operations, SQL injection prevention, and working with SQLAlchemy to map Python classes to database tables.

#Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- `pycodestyle` version 2.8.* (for code linting)

# Installation

1. Setup Python Virtual Environment:
    	bash
    sudo apt-get install python3.8-venv
    python3 -m venv venv
    source venv/bin/activate

2. Install MySQLdb:
    	bash
    sudo apt-get install python3-dev
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install zlib1g-dev
    sudo pip3 install mysqlclient

3. Install SQLAlchemy:
    	bash
    sudo pip3 install SQLAlchemy

# Usage

1. Task Execution:
    - Navigate to the directory containing the task files.
    - Execute the Python scripts with appropriate arguments as specified in each task.

2. Example:
    bash
    ./0-select_states.py root root hbtn_0e_0_usa
    ```

# Files

- `0-select_states.py`: Lists all states from the database.
- `1-filter_states.py`: Lists states starting with a specific letter.
- `2-my_filter_states.py`: Lists states based on user input.
- `3-my_safe_filter_states.py`: Lists states safely to prevent SQL injection.
- `4-cities_by_state.py`: Lists all cities from the database.
- `5-filter_cities.py`: Lists cities of a specific state.
- `6-model_state.py`: Defines the `State` class and creates the corresponding table in the database.
- `7-model_state_fetch_all.py`: Fetches all State objects from the database.
- `8-model_state_fetch_first.py`: Fetches the first State object from the database.
- `9-model_state_filter_a.py`: Fetches State objects containing the letter 'a'.
- `10-model_state_my_get.py`: Fetches a specific State object by name.
- `11-model_state_insert.py`: Inserts a new State object into the database.
- `12-model_state_update_id_2.py`: Updates the name of a State object with a specific ID.
- `13-model_state_delete_a.py`: Deletes State objects containing the letter 'a'.
- `model_state.py`: Contains the class definitions for `State` and `Base`.
- `model_city.py`: Contains the class definition for `City`.
- `14-model_city_fetch_by_state.py`: Fetches all City objects grouped by state.

# Credits

This project is part of the curriculum in the ALX Software Engineering program.
