# Details App

Applications that can store your personal details and list all the written users on html

### What I added:
- worked on Windows 11
- added to pyproject.toml: " psycopg2-binary = "^2.9.5" "
- added the postgres service in docker-compose, added environment variables for the app and postgres
- installed pgadmin locally on Windows to be able to see the tables and saved data
- modified "app.py" so that I can connect to postgres add entires to the table
- Had to replace the index.html (used copilot) since the form was saving "none"

### Requirements:

- Python: 3.11
- Bash Shell
- "psycopg2-binary = "^2.9.5"
- Docker
    - Postgresql container needed
- Docker compose for multi container environment
- pgadmin for checking the data

### Install
- pgadmin

### Setup
- run "docker compose up --build -d"

