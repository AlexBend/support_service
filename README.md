# Support service application


## Adjust the application

### Install deps

```bash
pipenv sync --dev
# Activate the environment
pipenv shell
```
python src/manage.py runserver

## Code quality tools
...


## Application description
```bash
▾ users
    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    ├─ views.py # Endopints / post-controller
    ├─ models.py # Database tables mapper
    ├─ admin.py # Database tables mapper
    # └─ views.py # Endopints / post-controller
```