# 0x15. JavaScript - Web jQuery

## Overview

This project is part of the ALX Higher Level Programming curriculum and focuses on utilizing JavaScript and jQuery to enhance front-end web development skills. The aim is to understand how to interact with the Document Object Model (DOM), handle events, and perform AJAX requests using jQuery.

## Concepts

The key concepts covered in this project include:

- JavaScript in the browser
- Dealing with data statically versus dynamically
- Selecting and manipulating HTML elements
- Handling events
- Making GET and POST requests using jQuery AJAX

## Learning Objectives

By the end of this project, you should be able to:

1. Explain why jQuery makes front-end programming easier.
2. Select HTML elements using JavaScript and jQuery.
3. Differentiate between ID, class, and tag name selectors.
4. Modify HTML element styles and content.
5. Perform DOM manipulations.
6. Make GET and POST requests using jQuery AJAX.
7. Bind and listen to DOM and user events.

## Resources

To complete this project, the following resources were used:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction)
- [Selector](https://learn.jquery.com/using-jquery-core/selecting-elements/)
- [Get and set content](https://api.jquery.com/category/manipulation/)
- [Manipulate CSS classes](https://api.jquery.com/category/css/)
- [Manipulate DOM elements](https://api.jquery.com/category/manipulation/)
- [API Introduction](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [GET & POST request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [jQuery Ajax Tutorial #1 - Using AJAX & APIs](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [jQuery](https://jquery.com/)
- [jQuery API](https://api.jquery.com/)
- [jQuery Ajax](https://api.jquery.com/jquery.ajax/)

## Requirements

- Use editors such as `vi`, `vim`, or `emacs`.
- All files should be interpreted in Chrome (version 57.0).
- All files should end with a new line.
- Include a `README.md` file at the root of the project folder.
- Code should be semistandard compliant using the flag `--global $: semistandard *.js --global $`.
- Use jQuery version 3.x.
- Avoid using `var`; use `let` and `const` instead.
- Ensure the HTML does not reload for each action; manipulate the DOM and update values dynamically.

## Tasks

### Task 0: No jQuery

**File:** `0-script.js`

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) using `document.querySelector`.

### Task 1: With jQuery

**File:** `1-script.js`

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) using the jQuery API.

### Task 2: Click and Turn Red

**File:** `2-script.js`

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header` using the jQuery API.

### Task 3: Add `.red` Class

**File:** `3-script.js`

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header` using the jQuery API.

### Task 4: Toggle Classes

**File:** `4-script.js`

Write a JavaScript script that toggles the class of the `<header>` element between `red` and `green` when the user clicks on the tag `DIV#toggle_header` using the jQuery API.

### Task 5: List of Elements

**File:** `5-script.js`

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`. The new element must be `<li>Item</li>` and added to `UL.my_list` using the jQuery API.

### Task 6: Change the Text

**File:** `6-script.js`

Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header` using the jQuery API.

### Task 7: Star Wars Character

**File:** `7-script.js`

Write a JavaScript script that fetches the character name from the URL `https://swapi-api.alx-tools.com/api/people/5/?format=json` and displays it in the HTML tag `DIV#character` using the jQuery API.

### Task 8: Star Wars Movies

**File:** `8-script.js`

Write a JavaScript script that fetches and lists the title for all movies using the URL `https://swapi-api.alx-tools.com/api/films/?format=json`. All movie titles must be listed in the HTML tag `UL#list_movies` using the jQuery API.

### Task 9: Say Hello!

**File:** `9-script.js`

Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of hello in the HTML tag `DIV#hello` using the jQuery API.

## Repository

- **GitHub Repository:** `alx-higher_level_programming`
- **Directory:** `0x15-javascript-web_jquery`

## Conclusion

This project provided hands-on experience with JavaScript and jQuery, emphasizing DOM manipulation, event handling, and AJAX requests. By completing these tasks, we gained practical skills essential for front-end web development.
