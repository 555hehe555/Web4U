@echo off
setlocal

rem Change to your project directory
cd C:\Users\Asus\Desktop\Web4U-dev

rem Ask if the user wants to create a new virtual environment
SET /P createVenv=Would you like to create a new virtual environment? (yes/no):
IF /I "%createVenv%"=="yes" (
    rem Check if virtual environment exists, if yes, remove it
    if exist "venv" (
        echo Removing existing virtual environment...
        rmdir /s /q "venv"
        echo Virtual environment removed.
    )

    rem Create virtual environment
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
) ELSE (
    echo Keeping the existing virtual environment.
)

rem Check if .env file exists, if yes, remove it
IF EXIST ".env" (
    SET /P removeEnv=Would you like to remove the existing .env file? (yes/no):
    IF /I "%removeEnv%"=="yes" (
        echo Removing existing .env file...
        del ".env"
        echo .env file removed.
    )
)

rem Create .env file if it doesn't exist
IF NOT EXIST ".env" (
    echo Creating .env file...
    echo DEBUG=True > .env
    echo .env file created with DEBUG=True.
)

rem Install dependencies
echo Installing dependencies from requirements.txt...
venv\Scripts\pip install -r requirements.txt
echo Dependencies installed.

REM Handle database reset
SET /P resetDB=Would you like to reset the database? (yes/no):
IF /I "%resetDB%"=="yes" (
    rem Terminate any Python processes that may be holding db.sqlite3
    echo Closing any running Python processes...
    taskkill /F /IM python.exe >nul 2>&1
    echo Python processes closed.

    IF EXIST db.sqlite3 (
        echo Deleting existing database...
        DEL db.sqlite3
        echo Database file removed.
    )

    echo Creating new database...
    venv\Scripts\python manage.py makemigrations
    venv\Scripts\python manage.py migrate
    echo New database created.
) ELSE (
    echo Keeping the existing database.
)

SET /P createSuperUser=Would you like to create super user? (yes/no):
IF /I "%createSuperUser%"=="yes" (
    venv\Scripts\python create_superuser.py
) ELSE(
    echo ok
)

SET /P start_server=Would you like to start server? (yes/no):
IF /I "%start_server%"=="yes" (
    venv\Scripts\python start_server.py
)


endlocal