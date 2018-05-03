# Ginstaram
- This is application to study Django.

# Environment
- python 3.6.4
- pip3
- mysql5.7
- gcc git tar zlib zlib-devel bzip2-devel openssl-devel wget make

# Setup
- setup mysql password
- cd app/gistaram 
- mysql -u root -p < sql/contruct.sql
- python3 manage.py migrate
- python3 manage.py runserver 0:8000
