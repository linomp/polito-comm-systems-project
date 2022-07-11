.\env\Scripts\activate
pip install -r requirements.txt

SET MYSQL_HOST=apps.xmp.systems
SET MYSQL_USER=root
SET MYSQL_PASSWORD=09d25e094faa6ca
SET MYSQL_DATABASE=plcs_db
SET MYSQL_PORT=443

uvicorn main:app --reload