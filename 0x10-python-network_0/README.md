Project: 0x10 Python Network #0

This project encompasses various tasks focusing on understanding and working with network-related concepts in Python and Bash scripting. Each task contributes to learning objectives related to HTTP, URL handling, request methods, and more. Below is a detailed guide on each task and its associated script files.

# Tasks Overview:

1. cURL body size: A Bash script to retrieve the size of the body of a response from a given URL.
2. cURL to the end: A Bash script to fetch and display the body of a response from a URL with a 200 status code.
3. cURL Method: A Bash script to send a DELETE request to a URL and display the response body.
4. cURL only methods: A Bash script to display all HTTP methods accepted by a server for a given URL.
5. cURL headers: A Bash script to send a GET request with a specific header to a URL and display the response body.
6. cURL POST parameters: A Bash script to send a POST request with specific parameters to a URL and display the response body.
7. Find a peak: A Python function to find a peak in an unsorted list of integers with optimized complexity.
8. Only status code: A Bash script to retrieve and display only the status code of a response from a given URL.
9. cURL a JSON file: A Bash script to send a JSON POST request to a URL with the content of a file and display the response body.
10. Catch me if you can!: A Bash script to make a request to a specific URL to trigger a response containing a predefined message.

# Usage:

Each script is designed to be run from the command line, following the specified requirements and usage instructions provided in the project description. Here's a brief overview of how to use each script:

- Ensure the scripts are executable: `chmod +x script_name.sh`
- Execute the scripts with appropriate arguments as per the task requirements.

For example:
```
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1
./2-delete.sh 0.0.0.0:5000/route_3

# Repository Structure:

The project repository (`alx-higher_level_programming`) contains the following directory and files relevant to this project:

- Directory: 0x10-python-network_0
  - 0-body_size.sh
  - 1-body.sh
  - 2-delete.sh
  - 3-methods.sh
  - 4-header.sh
  - 5-post_params.sh
  - 6-peak.py
  - 6-peak.txt
  - 100-status_code.sh
  - 101-post_json.sh
  - 102-catch_me.sh
  - my_json_0
  - my_json_1
  - my_json_2
  - README.md

# Testing:

Scripts are tested on Ubuntu 20.04 LTS environment, ensuring compliance with specified requirements such as script length, syntax, and functionality. Testing can be performed on the provided sandbox environment using the web server running on port 5000.

# Note:
- Each script should adhere to the outlined requirements, including script length, syntax, documentation, and usage of appropriate tools like curl and python3.
- Scripts should be well-documented and follow best practices to enhance readability and maintainability.

This README serves as a comprehensive guide for understanding and utilizing the scripts within this project. For further details on each task, please refer to the individual script files and accompanying comments.

---
By HUSSEIN GARANE
