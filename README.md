# Setup
```
docker-compose build
cp .env.example .env
```

Set values in `.env`

# Run
`docker-compose up`

Open `http://localhost:8000`

# API

### Get paginated users result
GET `/api/users`

### Specify a page

GET `/api/users?page=2`

### Filter users

Filter fields:

- username
- fisrt_name
- last_name
- email

Example:

GET

```
/api/users?username=john`
/api/users?username=john&first_name=anthony
/api/users?username=john&first_name=anthony&page=5
/api/users?username=john&first_name=anthony&last_name=greene&email=jtodd@example.org
```
