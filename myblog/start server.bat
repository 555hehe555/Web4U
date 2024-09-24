@echo off
chcp 65001 > nul

set "server_path=D:\github\djanga"
set "project_name=myblog"
set "virtual_env_path=D:\github\djanga\venv"

cd /d "%server_path%\%project_name%"
call "%virtual_env_path%\Scripts\activate"

python manage.py runserver

