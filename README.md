Sure, here's the updated README.md file with the link to the pipenv installation instructions:

  

# CS Guide Project

  

This is a major project for our college that aims to provide a guide for computer science students. The project requires Python 3, pip, and pipenv to be installed on your computer.

  

## Installation

  

To get started with the project, clone or fork the repository and then run the following command to install all dependencies:

  

```

pipenv install

```

  or
  ```
  py -m pipenv install
```

If you don't have pipenv installed, you can follow the installation instructions [click here](https://pypi.org/project/pipenv/).

  

Once the installation is complete, activate the virtual environment by running:

  

```

pipenv shell

```

or

```

py -m pipenv shell

```

  

## Database Setup

  

To set up the database, run the following commands to create and apply database migrations:

  

```

py manage.py makemigrations backend

py manage.py migrate

```

  

Next, run the following command to insert initial subject data for all semesters:

  

```

py manage.py shell

from backend.initialData import *

insertSubject()

```

  

This will populate the database with all the necessary subject data.

  

## Running the Server

  

To run the server, use the following command:

  

```

python manage.py runserver

```

  

The server should now be running at http://localhost:8000/.

## Conclusion

With these steps, you should now have the project up and running on your local machine. If you encounter any issues, please refer to the project's documentation or reach out to the project maintainers for assistance.