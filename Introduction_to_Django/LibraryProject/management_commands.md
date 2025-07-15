# Django Management Commands Documentation

This directory contains custom Django management commands for the Library Project.

## Available Commands

### Setup Commands
- `setup_dev_data` - Creates sample data for development
- `clear_cache` - Clears all cache data
- `backup_db` - Creates a database backup

### Maintenance Commands
- `cleanup_old_sessions` - Removes expired sessions
- `optimize_db` - Optimizes database performance
- `check_system` - Runs system health checks

## Usage

Run any command using:
```bash
python manage.py <command_name>
```

For help with a specific command:
```bash
python manage.py <command_name> --help
```

## Creating Custom Commands

1. Create a new Python file in this directory
2. Define a class that inherits from `BaseCommand`
3. Implement the `handle` method
4. Add appropriate help text and arguments

Example:
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of your command'
    
    def add_arguments(self, parser):
        parser.add_argument('--option', type=str, help='Optional argument')
    
    def handle(self, *args, **options):
        self.stdout.write('Command executed successfully!')
```
