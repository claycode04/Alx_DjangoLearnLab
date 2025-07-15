@echo off
REM Django Library Project - Quick Setup Script for Windows
REM This script sets up the development environment quickly

echo 🚀 Starting Django Library Project Setup...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo [INFO] Python found
python --version

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pip is not installed. Please install pip first.
    pause
    exit /b 1
)

REM Create virtual environment
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
) else (
    echo [WARNING] Virtual environment already exists.
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
if exist "requirements.txt" (
    echo [INFO] Installing Python packages...
    pip install -r requirements.txt
) else (
    echo [WARNING] requirements.txt not found. Installing Django manually...
    pip install Django==5.2.4
)

REM Create environment file if it doesn't exist
if not exist ".env" (
    echo [INFO] Creating environment file...
    copy .env.example .env
    echo [WARNING] Please update .env file with your configuration.
)

REM Create necessary directories
echo [INFO] Creating project directories...
if not exist "logs" mkdir logs
if not exist "static" mkdir static
if not exist "media" mkdir media
if not exist "templates" mkdir templates

REM Run migrations
echo [INFO] Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Collect static files
echo [INFO] Collecting static files...
python manage.py collectstatic --noinput

REM Create superuser (optional)
set /p create_superuser="Do you want to create a superuser account? (y/n): "
if /i "%create_superuser%"=="y" (
    echo [INFO] Creating superuser...
    python manage.py createsuperuser
)

REM Final instructions
echo.
echo [INFO] ✅ Setup completed successfully!
echo.
echo 📋 Next steps:
echo   1. Activate virtual environment: venv\Scripts\activate
echo   2. Update .env file with your configuration
echo   3. Start development server: python manage.py runserver
echo   4. Visit http://127.0.0.1:8000 to see your application
echo.
echo 📚 Additional commands:
echo   • Run tests: python manage.py test
echo   • Create app: python manage.py startapp app_name
echo   • Make migrations: python manage.py makemigrations
echo   • Apply migrations: python manage.py migrate
echo.
echo [INFO] Happy coding! 🎉
pause
