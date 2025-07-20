import os
import sys
import django
from django.db import connection
import shutil
import time

# This script can be run directly or through Django shell
def reset_question_ids():
    # Only setup Django if not already setup (for direct Python execution)
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taxi_exam.settings")
        django.setup()
    
    # Now import models
    from taxi.models import Question, Choice, Category  # Added Category
    from django.conf import settings
    
    # Get the correct table name
    table_name = Question._meta.db_table
    choice_table_name = Choice._meta.db_table
    print(f"Database table name for Question model: {table_name}")
    print(f"Database table name for Choice model: {choice_table_name}")
    
    # Count questions before deletion
    question_count = Question.objects.count()
    choice_count = Choice.objects.count()
    print(f"Found {question_count} questions and {choice_count} choices in the database")
    
    # Delete all questions (this will cascade to choices)
    if question_count > 0:
        print("Deleting all questions and associated choices...")
        Question.objects.all().delete()
    else:
        print("No questions to delete.")
    
    # Close all database connections to allow DB file operations
    connection.close()
    
    # Get database path - assuming SQLite
    db_path = settings.DATABASES['default']['NAME']
    print(f"Database path: {db_path}")
    
    # Create backup
    backup_path = f"{db_path}.bak"
    print(f"Creating backup at {backup_path}...")
    shutil.copy2(db_path, backup_path)
    
    # Extreme approach: recreate tables with proper constraints
    print("Recreating tables with reset IDs...")
    
    # Reconnect to database
    connection.connect()
    
    with connection.cursor() as cursor:
        # Drop and recreate tables - SQLite way
        # First, get table creation SQL
        print("Getting table schema...")
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        question_create_sql = cursor.fetchone()[0]
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{choice_table_name}';")
        choice_create_sql = cursor.fetchone()[0]
        
        print("Dropping tables...")
        cursor.execute(f"DROP TABLE IF EXISTS {choice_table_name};")
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        
        print("Recreating tables...")
        cursor.execute(question_create_sql)
        cursor.execute(choice_create_sql)
        
        # Clear all sequence information - more aggressive approach
        print("Clearing sequences...")
        cursor.execute("DELETE FROM sqlite_sequence;")  # Delete ALL sequences
        
        # Explicitly reset sequences for our tables
        cursor.execute(f"INSERT OR REPLACE INTO sqlite_sequence (name, seq) VALUES ('{table_name}', 0);")
        cursor.execute(f"INSERT OR REPLACE INTO sqlite_sequence (name, seq) VALUES ('{choice_table_name}', 0);")
        
        # VACUUM the database to ensure all changes are applied
        print("Vacuuming database to apply changes...")
        cursor.execute("VACUUM;")
        
        print("\nVerifying reset...")
        cursor.execute("SELECT name, seq FROM sqlite_sequence;")
        sequences = cursor.fetchall()
        print("Updated sequences:")
        for name, seq in sequences:
            print(f"  {name}: {seq}")
    
    # Verification
    print("\nVerification:")
    print(f"Questions in database: {Question.objects.count()}")
    print(f"Choices in database: {Choice.objects.count()}")
    
    print("\nDone! New questions should start from ID 1.")
    print("NOTE: You may need to run migrations again to recreate other tables that might have been dropped.")
    print("If you have issues, restore from backup at:", backup_path)

# Always run the function, whether imported or run directly
# This ensures it works both with python reset_question_ids.py
# and with python manage.py shell < reset_question_ids.py
reset_question_ids()