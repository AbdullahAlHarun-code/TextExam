import os
import sys
import django
from django.db import connection

# This script needs to be run directly from Python, not from Django shell
def reset_question_ids():
    # Setup Django environment
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taxi_project.settings")
    django.setup()
    
    # Now import models
    from taxi.models import Question, Choice
    
    # Get the correct table name
    table_name = Question._meta.db_table
    print(f"Database table name for Question model: {table_name}")
    
    # Count questions before deletion
    question_count = Question.objects.count()
    print(f"Found {question_count} questions in the database")
    
    # Delete all questions (this will cascade to choices)
    if question_count > 0:
        print("Deleting all questions and associated choices...")
        Question.objects.all().delete()
    else:
        print("No questions to delete.")
    
    # Reset the SQLite sequence
    with connection.cursor() as cursor:
        print("\nChecking sqlite_sequence table...")
        cursor.execute("SELECT name, seq FROM sqlite_sequence;")
        sequences = cursor.fetchall()
        print("Current sequences:")
        for name, seq in sequences:
            print(f"  {name}: {seq}")
        
        print(f"\nResetting primary key sequence for {table_name}...")
        cursor.execute(f"UPDATE sqlite_sequence SET seq = 0 WHERE name = '{table_name}';")
        
        # Check if any rows were affected
        if cursor.rowcount == 0:
            print(f"No sequence found for {table_name}, inserting new entry...")
            cursor.execute(f"INSERT INTO sqlite_sequence (name, seq) VALUES ('{table_name}', 0);")
        
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

if __name__ == "__main__":
    reset_question_ids()


#cd /d "g:\MyCode\App Taxi Exam" && python reset_question_ids.py
# 