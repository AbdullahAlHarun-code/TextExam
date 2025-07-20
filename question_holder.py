from taxi.models import Question, Category, Choice

# === Question 10 ===
question10 = Question.objects.create(
    question_text="What road do you take from Naas town to Punchestown?",
    question_type=Question.SINGLE
)

category_names10 = ["Naas", "Punchestown", "Routes from This Area to Another", "Main Roads"]
for name in category_names10:
    try:
        cat = Category.objects.get(name=name)
        question10.categories.add(cat)
    except Category.DoesNotExist:
        print(f"[Q10] Category '{name}' not found in DB")

choices10 = [
    {"text": "Sallins Road", "label": "A", "is_correct": False},
    {"text": "Blessington Road", "label": "B", "is_correct": True},
    {"text": "Monread Road", "label": "C", "is_correct": False},
    {"text": "Tipper Road", "label": "D", "is_correct": False},
]

for choice in choices10:
    try:
        Choice.objects.create(
            question=question10,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q10] Failed to create choice {choice['label']}: {e}")