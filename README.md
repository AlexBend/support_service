# Support service application


## Adjust the application

### Create `.env` file based on `.env.default`
```bash
# Unix
cp .env.default .env

# Windows
# ...
```



### Install deps

```bash
pipenv sync --dev

# Activate the environment
pipenv shell
```


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


# Database

```mermaid
erDiagram
    Users {
        int id
        string frist_name
        string last_name
        string email
        string password
        bool is_staff
        bool is_active
        string role
        datetime created_at
        datetime updated_at
    }
    Tickets {
        int id
        int customer_id
        int manager_id
        string header
        text body
        datetime created_at
        datetime updated_at
    }
    Comments {
        int id
        int prev_comment_id
        int user_id
        int ticket_id
        text body
        datetime created_at
        datetime updated_at
    }

    Users ||--o{ Tickets : ""
    Tickets ||--o{ Comments : ""
    Comments ||--o{ Comments : ""
```