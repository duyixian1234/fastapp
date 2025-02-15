# Fast App

A fast and lightweight web application using fasthtml and markdown.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/duyixian1234/fastapp.git
   cd fastapp
   ```

2. Set up a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:
```sh
python api/index.py
```

## Project Structure

The project structure is as follows:
```
fastapp/
├── api/
│   ├── __init__.py
│   ├── components.py
│   ├── factory.py
│   ├── index.py
│   └── pages/
│       └── home.py
├── .gitignore
├── .python-version
├── .sesskey
├── pyproject.toml
├── README.md
├── requirements.txt
└── vercel.json
```
