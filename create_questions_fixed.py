from taxi.models import Question, Category, Choice

print("Starting question creation process...")

# First, let's make sure we have some basic categories
categories_to_check = ["Main Roads", "Housing Estates", "Towns/Villages Passed Through on Routes", "Routes from This Area to Another"]
for cat_name in categories_to_check:
    try:
        Category.objects.get(name=cat_name)
        print(f"Category '{cat_name}' already exists")
    except Category.DoesNotExist:
        Category.objects.create(name=cat_name)
        print(f"Created missing category: '{cat_name}'")

# === Question 1 ===
try:
    question1 = Question.objects.create(
        question_text="What towns do you pass from Celbridge to Allenwood?",
        question_type=Question.SINGLE
    )
    print("Created Question 1")

    category_names1 = ["Celbridge", "Allenwood", "Clane", "Prosperous", "Towns/Villages Passed Through on Routes", "Routes from This Area to Another"]
    for name in category_names1:
        try:
            cat = Category.objects.get(name=name)
            question1.categories.add(cat)
        except Category.DoesNotExist:
            print(f"[Q1] Category '{name}' not found in DB")

    choices1 = [
        {"text": "Clane and Prosperous", "label": "A", "is_correct": True},
        {"text": "Maynooth and Kilcock", "label": "B", "is_correct": False},
        {"text": "Maynooth and Rathcoffee", "label": "C", "is_correct": False},
        {"text": "Lexlip and Maynooth", "label": "D", "is_correct": False},
    ]
    for choice in choices1:
        try:
            Choice.objects.create(
                question=question1,
                choice_text=choice["text"],
                option_label=choice["label"],
                is_correct=choice["is_correct"]
            )
        except Exception as e:
            print(f"[Q1] Failed to create choice {choice['label']}: {e}")
except Exception as e:
    print(f"Error creating Question 1: {e}")

# === Question 2 ===
try:
    question2 = Question.objects.create(
        question_text="What road is Beechmount housing estate on in Newbridge?",
        question_type=Question.SINGLE
    )
    print("Created Question 2")

    category_names2 = ["Newbridge", "Housing Estates", "Main Roads"]
    for name in category_names2:
        try:
            cat = Category.objects.get(name=name)
            question2.categories.add(cat)
        except Category.DoesNotExist:
            print(f"[Q2] Category '{name}' not found in DB")

    choices2 = [
        {"text": "Green Rd", "label": "A", "is_correct": True},
        {"text": "Langton Park", "label": "B", "is_correct": False},
        {"text": "Dublin Rd", "label": "C", "is_correct": False},
        {"text": "Ballymany", "label": "D", "is_correct": False},
    ]
    for choice in choices2:
        try:
            Choice.objects.create(
                question=question2,
                choice_text=choice["text"],
                option_label=choice["label"],
                is_correct=choice["is_correct"]
            )
        except Exception as e:
            print(f"[Q2] Failed to create choice {choice['label']}: {e}")
except Exception as e:
    print(f"Error creating Question 2: {e}")

# === Question 3 ===
try:
    question3 = Question.objects.create(
        question_text="What Junction number is Straffan on the M4?",
        question_type=Question.SINGLE
    )
    print("Created Question 3")

    category_names3 = ["Straffan", "Main Roads"]
    for name in category_names3:
        try:
            cat = Category.objects.get(name=name)
            question3.categories.add(cat)
        except Category.DoesNotExist:
            print(f"[Q3] Category '{name}' not found in DB")

    choices3 = [
        {"text": "Junction 6", "label": "A", "is_correct": False},
        {"text": "Junction 7", "label": "B", "is_correct": True},
        {"text": "Junction 8", "label": "C", "is_correct": False},
        {"text": "Junction 9", "label": "D", "is_correct": False},
    ]
    for choice in choices3:
        try:
            Choice.objects.create(
                question=question3,
                choice_text=choice["text"],
                option_label=choice["label"],
                is_correct=choice["is_correct"]
            )
        except Exception as e:
            print(f"[Q3] Failed to create choice {choice['label']}: {e}")
except Exception as e:
    print(f"Error creating Question 3: {e}")

print("✅ All questions created successfully.")
