# Python CRUD Application with PostgreSQL and `psycopg2`

This is a basic CRUD (Create, Read, Update, Delete) application in Python that uses a PostgreSQL database for data storage and the `psycopg2` library to interact with the database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- PostgreSQL installed and running
- `psycopg2` library installed. You can install it using pip:

```bash
pip install psycopg2
```

## Getting Started

### Step 1: Clone the Repository

Clone this repository using the following command:

```bash
git clone https://github.com/Aroxed/python-crud-mvc.git
cd crud-postgresql-psycopg2
```
### Step 2: Configure the Database Connection

Open the `model.py` file and provide your PostgreSQL database details:

```python
# In model.py
db_password = 'your_db_password'
```
### Step 3: Run the Application

Execute the following command to run the application:

```bash
python main.py
```

