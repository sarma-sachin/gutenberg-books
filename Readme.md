# Gutenberg Book List

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/{username}/{repo})](https://github.com/{username}/{repo}/stargazers)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Project Description

Implementation of an API that provides access to a database of books from Project Gutenberg, a repository of freely available e-books. The API allows users to query and retrieve books based on various filter criteria.

The API will support various filter criteria, including book ID numbers, language, mime-type, topic, author, and title. Users can specify multiple filter values for each criteria, allowing for flexible and customized queries. The API will return books in decreasing order of popularity, based on the number of downloads.

The API will offer a user-friendly interface for querying books, providing a seamless experience for developers, researchers, or book enthusiasts to explore the vast collection of Project Gutenberg.

The API will handle large result sets gracefully by implementing pagination. If the number of books that meet the specified criteria exceeds 25, the API will return the first 25 books and provide a means to retrieve the next sets of 25 books until all books are retrieved.

The data will be returned in a JSON format, ensuring compatibility with a wide range of applications and programming languages. Each book object will contain essential information such as the title, author details, genre, language, subject(s), bookshelf(s), and a list of links to download the book in the available formats (mime-types).

To enhance the usability of the API, case-insensitive partial matches will be supported for filtering criteria such as topics, authors, and titles. This allows users to search for books with greater flexibility and ease. For example, a request with the filter criteria "language=en,fr" and "topic=child,infant" will retrieve books available in English or French and related to the topics of children or infants.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/{username}/{repo}.git
   ```

2. Navigate to the project directory:

   ```bash
   cd {repo}
   ```

3. Create a virtual environment and activate it:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   Use the database dump available at this [https://drive.google.com/file/d/1NJVtOs4Zxk3Go1S9oeurI3pBNH1YWN85/view](link) to initialise the database. No need to run migrations as the models have been generated from the database using the following command.

   ```bash
   python manage.py inspectdb > models.py
   ```

6. Update the values in the .env file.

   ```bash
   nano .env
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to see the application in action.

## API Endpoints

Provide a list of the API endpoints and their corresponding functionalities. Include a brief description of each endpoint, the HTTP methods it supports, and the expected request/response formats.

| Endpoint  | Description         | Method |
| --------- | ------------------- | ------ |
| `/books/` | Fetch List of Books | GET    |

## API Documentation

The API documentation for this project is available in two formats: Swagger and ReDoc.

- Swagger Documentation: Access the Swagger API documentation [Swagger Documentation](http://13.127.180.105/swagger).
- ReDoc Documentation: Access the ReDoc API documentation [ReDoc Documentation](http://13.127.180.105/redoc).

### Swagger Description

- Swagger YAML: You can access the Swagger YAML description [Swagger YAML Description](http://13.127.180.105/swagger.yaml).
- Swagger JSON: You can access the Swagger JSON description [Swagger JSON Description](http://13.127.180.105/swagger.json).

Please refer to the Swagger documentation for detailed information about the API endpoints, request/response formats, and supported filter criteria.

## Demo

If your API is hosted and publicly accessible, provide a link to the hosted version here.

- [http://13.127.180.105/books](https://www.example.com) - Link to the hosted version of your API.

## License

This project is licensed under the [MIT License](LICENSE).
