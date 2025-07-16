from django.core.management.base import BaseCommand
from taxi.models import Category
import os

class Command(BaseCommand):
    help = 'Imports categories from a text file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the category text file.')

    def handle(self, *args, **options):
        file_path = options['file_path']
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found at: {file_path}'))
            return

        self.stdout.write(self.style.SUCCESS(f'Starting category import from: {file_path}'))
        
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing categories.'))

        with open(file_path, 'r') as f:
            lines = f.readlines()

        parent_stack = [None] * 10  # Support up to 10 levels of nesting

        for line in lines:
            if not line.strip():
                continue

            # Improved indentation detection
            stripped_line = line.lstrip()
            indent_str = line[:len(line) - len(stripped_line)]
            
            level = 0
            if '\t' in indent_str:
                # Count tabs for level
                level = indent_str.count('\t')
            else:
                # Count spaces for level (assuming 4 spaces per level)
                level = indent_str.count(' ') // 4

            category_name = stripped_line.strip()

            # This handles cases where a line might be indented but have no text.
            if not category_name:
                continue

            parent = parent_stack[level - 1] if level > 0 else None

            category, created = Category.objects.get_or_create(
                name=category_name,
                parent=parent
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {"    " * level}{category.name}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Exists: {"    " * level}{category.name}'))

            if level < len(parent_stack) -1:
                parent_stack[level] = category

        self.stdout.write(self.style.SUCCESS('Category import finished.'))
