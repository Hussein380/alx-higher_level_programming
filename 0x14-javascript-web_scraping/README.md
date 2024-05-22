# 0x14. JavaScript - Web Scraping

## Description

This project involves writing scripts in JavaScript to perform various web scraping tasks. You'll work with JSON data, the `fs` module for file operations, and the `request` module for making HTTP requests. By the end of this project, you should be able to explain how to manipulate JSON data, use the `request` and `fetch` APIs, and read and write files using the `fs` module.

## Learning Objectives

- Understand why JavaScript programming is amazing.
- Manipulate JSON data effectively.
- Use the `request` and `fetch` APIs to interact with web services.
- Read from and write to files using the `fs` module.

## Requirements

- All scripts should be written in JavaScript.
- Scripts will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x).
- All scripts must be executable.
- Follow the Standard + semicolons style.
- Do not use `var`; use `const` or `let` instead.
- The first line of all files should be `#!/usr/bin/node`.

## Installations

### Node.js 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Semistandard

```bash
$ sudo npm install semistandard --global
```

### Request Module

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Readme

Write a script that reads and prints the content of a file.

Usage:
```bash
./0-readme.js <file_path>
```

Example:
```bash
$ ./0-readme.js cisfun
C is super fun!
```

### 1. Write me

Write a script that writes a string to a file.

Usage:
```bash
./1-writeme.js <file_path> <string>
```

Example:
```bash
$ ./1-writeme.js my_file.txt "Python is cool"
```

### 2. Status code

Write a script that displays the status code of a GET request.

Usage:
```bash
./2-statuscode.js <URL>
```

Example:
```bash
$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
```

### 3. Star Wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

Usage:
```bash
./3-starwars_title.js <movie_id>
```

Example:
```bash
$ ./3-starwars_title.js 1
A New Hope
```

### 4. Star Wars Wedge Antilles

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

Usage:
```bash
./4-starwars_count.js <API_URL>
```

Example:
```bash
$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

### 5. Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

Usage:
```bash
./5-request_store.js <URL> <file_path>
```

Example:
```bash
$ ./5-request_store.js http://loripsum.net/api loripsum
```

### 6. How many completed?

Write a script that computes the number of tasks completed by user id.

Usage:
```bash
./6-completed_tasks.js <API_URL>
```

Example:
```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

### 7. Who was playing in this movie? (Advanced)

Write a script that prints all characters of a Star Wars movie.

Usage:
```bash
./100-starwars_characters.js <movie_id>
```

Example:
```bash
$ ./100-starwars_characters.js 3
```

# 8. Right order (Advanced)

Write a script that prints all characters of a Star Wars movie in the order they appear in the list "characters" in the /films/ response.

Usage:
```bash
./101-starwars_characters.js <movie_id>
```

Example:
```bash
$ ./101-starwars_characters.js 3
```

## Repository

GitHub repository: [alx-higher_level_programming](https://github.com/yourusername/alx-higher_level_programming)
Directory: `0x14-javascript-web_scraping`

Each task script should be placed in the directory `0x14-javascript-web_scraping` and should be executable.
