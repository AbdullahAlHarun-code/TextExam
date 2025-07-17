from taxi.models import Question, Category, Choice

# Check a sample of questions (first, middle, and last)
question_ids = [1, 140, 286]  # Adjust these IDs if needed

for qid in question_ids:
    try:
        q = Question.objects.get(id=qid)
        cats = q.categories.all()
        choices = Choice.objects.filter(question=q)
        
        print(f"Question {qid}: {q.question_text}")
        print(f"  Categories: {cats.count()} - {', '.join([c.name for c in cats])}")
        print(f"  Choices: {choices.count()}")
        for c in choices:
            correct = "✓" if c.is_correct else " "
            print(f"    [{correct}] {c.option_label}. {c.choice_text}")
        print()
    except Question.DoesNotExist:
        print(f"Question {qid} not found")
        print()

# Get overall stats
total_questions = Question.objects.count()
questions_with_cats = sum(1 for q in Question.objects.all() if q.categories.exists())
questions_with_choices = sum(1 for q in Question.objects.all() if Choice.objects.filter(question=q).exists())

print(f"Total questions: {total_questions}")
print(f"Questions with categories: {questions_with_cats}")
print(f"Questions with choices: {questions_with_choices}")
