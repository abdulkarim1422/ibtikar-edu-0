# ibtikar-edu-0 (backend)

## Setup
To run this project, follow these steps:

### Clone the repository
```bash
git clone https://github.com/abdulkarim1422/ibtikar-edu-0
```
```bash
cd ibtikar-edu-0/backend
```

### Create and activate virtual environment
```bash
python -m venv venv
```
### activate the venv
#### On Windows
```bash
.\venv\Scripts\activate
```
#### On Unix or MacOS
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```


### Migrate db
#### Initial Migration
```bash
alembic revision --autogenerate -m "Initial migration"
```
#### Upgrading head
```bash
alembic upgrade head
```

### Start the application
```bash
uvicorn app.main:app --reload --port 3111
```


## Dev
### Update packages
```bash
pip freeze > requirements.txt
```
