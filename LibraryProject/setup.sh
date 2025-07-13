#!/bin/bash

# Django Library Project - Quick Setup Script
# This script sets up the development environment quickly

echo "🚀 Starting Django Library Project Setup..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
if ! command -v python &> /dev/null; then
    print_error "Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

print_status "Python found: $(python --version)"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    print_error "pip is not installed. Please install pip first."
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    print_status "Creating virtual environment..."
    python -m venv venv
else
    print_warning "Virtual environment already exists."
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    print_status "Installing Python packages..."
    pip install -r requirements.txt
else
    print_warning "requirements.txt not found. Installing Django manually..."
    pip install Django==5.2.4
fi

# Create environment file if it doesn't exist
if [ ! -f ".env" ]; then
    print_status "Creating environment file..."
    cp .env.example .env
    print_warning "Please update .env file with your configuration."
fi

# Create necessary directories
print_status "Creating project directories..."
mkdir -p logs
mkdir -p static
mkdir -p media
mkdir -p templates

# Run migrations
print_status "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
print_status "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser (optional)
read -p "Do you want to create a superuser account? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Creating superuser..."
    python manage.py createsuperuser
fi

# Final instructions
echo
print_status "✅ Setup completed successfully!"
echo
echo "📋 Next steps:"
echo "  1. Activate virtual environment: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"
echo "  2. Update .env file with your configuration"
echo "  3. Start development server: python manage.py runserver"
echo "  4. Visit http://127.0.0.1:8000 to see your application"
echo
echo "📚 Additional commands:"
echo "  • Run tests: python manage.py test"
echo "  • Create app: python manage.py startapp app_name"
echo "  • Make migrations: python manage.py makemigrations"
echo "  • Apply migrations: python manage.py migrate"
echo
print_status "Happy coding! 🎉"
