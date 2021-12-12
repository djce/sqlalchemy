@echo off

cd %~dp0

set FLASK_APP=alex.py
set FLASK_ENV=development
set FLASK_DEBUG=1
set FLASK_RUN_HOST=127.0.0.1
set FLASK_RUN_PORT=80

flask run

pause