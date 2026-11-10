# National Parks Explorer

## Project Overview
This project reads park data from a JSON file and lets the user search for parks by state or activity. It includes a browser script for filtering parks by location and a search script for matching park names. It can also write matching results to a text file.

This project shows how Python can be used to process real-world data and build a small information system.

## Python Concepts Learned
- Importing modules and separating logic into files
- Working with JSON using the `json` module
- Reading data from files with `open()`
- Working with dictionaries and nested data structures
- Lists of park records as Python objects
- Defining functions to keep code organized and reusable
- Filtering lists using loops and conditions
- Using `sys.argv` to read command-line arguments
- Writing output to files with `with open(...)`
- Building search and browse features using user-provided input

## Example
The program can be run like this:
- `python browse.py CA hiking`
- `python search.py yellowstone`

It then prints the matching parks and may save the results to `results.txt`.

This project introduces the idea of building real, data-driven Python apps from structured files.
