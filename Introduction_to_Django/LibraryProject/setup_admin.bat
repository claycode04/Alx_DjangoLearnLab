@echo off
echo ========================================
echo Django Admin Interface Setup
echo ========================================
echo.

echo Checking if virtual environment exists...
if exist "venv" (
    echo Virtual environment found. Activating...
    call venv\Scripts\activate
) else (
    echo Virtual environment not found. Creating...
    python -m venv venv
    call venv\Scripts\activate
    echo Installing requirements...
    pip install -r requirements.txt
)

echo.
echo ========================================
echo Setting up Django Admin Interface
echo ========================================
echo.

echo 1. Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo 2. Creating sample data for testing...
python admin_demo.py

echo.
echo 3. Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ========================================
echo Admin Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a superuser account:
echo    python manage.py createsuperuser
echo.
echo 2. Run the development server:
echo    python manage.py runserver
echo.
echo 3. Access the admin interface:
echo    http://127.0.0.1:8000/admin/
echo.
echo Features available in admin:
echo - Book management with custom list display
echo - Search by title, author, or ISBN
echo - Filter by publication year, cover type, language
echo - Bulk actions for cover type changes
echo - Library management with book assignments
echo.
echo For detailed documentation, see:
echo bookshelf/admin_documentation.md
echo.
echo Press any key to create a superuser account...
pause

echo Creating superuser...
python manage.py createsuperuser

echo.
echo ========================================
echo Setup Complete! Starting server...
echo ========================================
echo.
echo Access the admin at: http://127.0.0.1:8000/admin/
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
