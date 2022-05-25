pip install -r requirements.txt

export MYSQL_HOST=165.227.107.127
export MYSQL_USER=root
export MYSQL_PASSWORD=09d25e094faa6ca
export MYSQL_DATABASE=plcs_db
export MYSQL_PORT=3306

uvicorn main:app --reload