#pip install -r requirements.txt

export MYSQL_HOST=apps.xmp.systems
export MYSQL_USER=root
export MYSQL_PASSWORD=09d25e094faa6ca
export MYSQL_DATABASE=plcs_db
export MYSQL_PORT=443

uvicorn main:app --reload