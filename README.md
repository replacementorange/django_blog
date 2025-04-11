# Django Blog Site

A simple blogging platform build with Django where admin user can create and manage blog posts, categorize them, and engage with readers trought comments.

## Learning Outcomes

My personal learning outcomes in this project can answer the following questions:

- How to setup a new Django project?
- How to create and edit blog posts?
- How to display posts for users?
- How to assign different categories to a post?
- How to allow users to comment on the posts?

Additionally, I became familiar with the following:

- Learned how to generate and utilize a test coverage report.
- Got familiar with VS Code's Copilot extension:
    - My handwritten unit testing (82% coverage) attempts were destroyed by Copilot’s 94% coverage.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/replacementorange/django_blog.git

2. **Create virtual enviroment:**

    ```bash
    python -m venv venv

3. **Activate the virtual enviroment:**

    - On Windows:
    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:
    ```bash
    source venv/bin/activate

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt

5. **Apply migrations:**

    ```bash
    python manage.py migrate

6. **Create a superuser (optional but recommended for admin access):**

    ```bash
    python manage.py createsuperuser

7. **Run the development server:**

    ```bash
    python manage.py runserver

8. **Access the application:**

    Open your web browser and go to **http://127.0.0.1:8000/**.

## Usage

**TODO**

## Features

- **Admin Interface:** Admin users can easily create, edit, and delete blog posts.
- **Categories:** Organize blog posts into categories.
- **User Comments:** Users can leave comments on blog posts.
