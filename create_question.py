from taxi.models import Question, Category, Choice

# === First Question ===
question1 = Question.objects.create(
    question_text="What towns do you pass from Celbridge to Allenwood?",
    question_type=Question.SINGLE
)

category_names1 = [
    "Clane", "Prosperous", "Allenwood", "Celbridge",
    "Towns/Villages Passed Through on Routes",
    "Routes from This Area to Another"
]

for name in category_names1:
    try:
        cat = Category.objects.get(name=name)
        question1.categories.add(cat)
        print(f"Added category: {name}")
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")

choices1 = [
    {"text": "Clane and Prosperous", "label": "A", "is_correct": True},
    {"text": "Maynooth and Kilcock", "label": "B", "is_correct": False},
    {"text": "Maynooth and Rathcoffee", "label": "C", "is_correct": False},
    {"text": "Lexlip and Maynooth", "label": "D", "is_correct": False},
]

for choice_data in choices1:
    Choice.objects.create(
        question=question1,
        choice_text=choice_data["text"],
        option_label=choice_data["label"],
        is_correct=choice_data["is_correct"]
    )

question1.save()

# === Second Question ===
question2 = Question.objects.create(
    question_text="What road is Beechmount housing estate on in Newbridge?",
    question_type=Question.SINGLE
)

category_names2 = [
    "Newbridge", "Housing Estates", "Main Roads"
]

for name in category_names2:
    try:
        cat = Category.objects.get(name=name)
        question2.categories.add(cat)
        print(f"Added category: {name}")
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")

choices2 = [
    {"text": "Green Rd", "label": "A", "is_correct": True},
    {"text": "Langton Park", "label": "B", "is_correct": False},
    {"text": "Dublin Rd", "label": "C", "is_correct": False},
    {"text": "Ballymany", "label": "D", "is_correct": False},
]

for choice_data in choices2:
    Choice.objects.create(
        question=question2,
        choice_text=choice_data["text"],
        option_label=choice_data["label"],
        is_correct=choice_data["is_correct"]
    )

question2.save()

print("✅ Both questions created successfully.")
