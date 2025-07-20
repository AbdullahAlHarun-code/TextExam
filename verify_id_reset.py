from taxi.models import Question, Category, Choice

# Create a test question
test_question = Question.objects.create(
    question_text="Test question after ID reset",
    question_type=Question.SINGLE
)

# Add a test choice
Choice.objects.create(
    question=test_question,
    choice_text="Test choice",
    option_label="A",
    is_correct=True
)

# Print the ID to verify
print(f"Created test question with ID: {test_question.id}")
print(f"If ID is 1, the reset worked correctly!")
