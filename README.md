# Details App

Applications that can store your personal details and list all the written users on html

### What I added:
- worked on Windows 11
- added to pyproject.toml: " psycopg2-binary = "^2.9.5" "
- added the postgres service in docker-compose, added postgres environment variables for the app
- installed pgadmin locally on Windows to be able to see the tables and saved data
- modified "app.py" so that I can connect to postgres and add entires to the table
- Had to replace the index.html (used copilot) since the form was saving "none"
- added the pgadmin service in docker compose

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
- go to: http://localhost:8000/ and type in name and email

To see the data you entered:
- go to: http://localhost:5050/  and enter user: admin@admin.com, password: postgres
- click on "add new server":
  1. in tab general -> "name" -> enter whatever you want
  2. in tab connect -> "host name" is "postgres-database", maintance database is "postgres", 
     username and password are both "postgres", click "save".
  3. on the left sidebar click on "servers"->the name you entered->databases->user-details->scehmas->tables.
     right click on details->query tool-> to see all data you entered do: "SELECT * FROM details"

