# Readme.md

This repository contains a Python script that reads data from a JSON file and performs some data manipulation. It also writes the results to separate text files.

## Prerequisites

To run this script, you need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/)

## Getting Started

1. Clone this repository to your local machine or download the script directly.
2. Place the `data.json` file in the same directory as the script.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following command to execute the script:

```bash
python script.py
```

## Description

The script performs the following tasks:

1. Reads data from the `data.json` file.
2. Extracts the `first_name`, `last_name`, `email`, and `ip_address` values from the JSON data.
3. Sorts the extracted values.
4. Writes the sorted `first_name` values to a file named `first_name.txt`.
5. Writes the sorted `last_name` values to a file named `lastname.txt`.
6. Writes the sorted `email` values to a file named `email.txt`.
7. Writes the sorted `ip_address` values to a file named `ip_address.txt`.

The resulting text files will be created in the same directory as the script.

## Example

Suppose the `data.json` file contains the following data:

```json
[
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "ip_address": "192.168.0.1"
  },
  {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "ip_address": "192.168.0.2"
  },
  {
    "first_name": "Bob",
    "last_name": "Johnson",
    "email": "bob.johnson@example.com",
    "ip_address": "192.168.0.3"
  }
]
```

After running the script, the following files will be created:

- `first_name.txt`:

```
['Alice', 'Bob', 'John']
```

- `lastname.txt`:

```
['Doe', 'Johnson', 'Smith']
```

- `email.txt`:

```
['alice.smith@example.com', 'bob.johnson@example.com', 'johndoe@example.com']
```

- `ip_address.txt`:

```
['192.168.0.1', '192.168.0.2', '192.168.0.3']
```

These files will contain the sorted values extracted from the `data.json` file.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your needs.