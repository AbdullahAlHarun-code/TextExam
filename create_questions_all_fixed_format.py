from taxi.models import Question, Category, Choice

# === Question 1 ===
question1 = Question.objects.create(
    question_text="What towns do you pass from Celbridge to Allenwood?",
    question_type=Question.SINGLE
)
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

# === Question 2 ===
question2 = Question.objects.create(
    question_text="What road is Beechmount housing estate on in Newbridge?",
    question_type=Question.SINGLE
)
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

# === Question 3 ===
question3 = Question.objects.create(
    question_text="What road is Globe Retail Park on in Naas?",
    question_type=Question.SINGLE
)
category_names3 = ["Naas", "Shopping Centres and Retail Parks", "Main Roads"]
for name in category_names3:
    try:
        cat = Category.objects.get(name=name)
        question3.categories.add(cat)
    except Category.DoesNotExist:
        print(f"[Q3] Category '{name}' not found in DB")

choices3 = [
    {"text": "Sallins Rd", "label": "A", "is_correct": True},
    {"text": "Dublin Rd", "label": "B", "is_correct": False},
    {"text": "Maudlins Ave", "label": "C", "is_correct": False},
    {"text": "Monread Road", "label": "D", "is_correct": False},
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

# === Question 4 ===
question4 = Question.objects.create(
    question_text="What road is Maynooth Post Primary School on?",
    question_type=Question.SINGLE
)
category_names4 = ["Maynooth", "Schools and Educational Institutions", "Main Roads"]
for name in category_names4:
    try:
        cat = Category.objects.get(name=name)
        question4.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices4 = [
    {"text": "Dunboyne Rd", "label": "A", "is_correct": True},
    {"text": "Moyglare Rd", "label": "B", "is_correct": False},
    {"text": "Parson St", "label": "C", "is_correct": False},
    {"text": "Kilcock Rd", "label": "D", "is_correct": False},
]
for choice in choices4:
    try:
        Choice.objects.create(
            question=question4,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q4] Failed to create choice {choice['label']}: {e}")


# === Question 5 ===
question5 = Question.objects.create(
    question_text="What road is St Conleths Gaa on in Newbridge?",
    question_type=Question.SINGLE
)
category_names5 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names5:
    try:
        cat = Category.objects.get(name=name)
        question5.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices5 = [
    {"text": "Henry Road", "label": "A", "is_correct": True},
    {"text": "Main St", "label": "B", "is_correct": False},
    {"text": "Station Road", "label": "C", "is_correct": False},
    {"text": "Standhouse Road", "label": "D", "is_correct": False},
]
for choice in choices5:
    try:
        Choice.objects.create(
            question=question5,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q5] Failed to create choice {choice['label']}: {e}")


# === Question 6 ===
question6 = Question.objects.create(
    question_text="What road is Newbridge Golf Club on?",
    question_type=Question.SINGLE
)
category_names6 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names6:
    try:
        cat = Category.objects.get(name=name)
        question6.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices6 = [
    {"text": "Ring of Roseberry", "label": "A", "is_correct": True},
    {"text": "Blackberry Road", "label": "B", "is_correct": False},
    {"text": "Barrettstown Road", "label": "C", "is_correct": False},
    {"text": "Station Road", "label": "D", "is_correct": False},
]
for choice in choices6:
    try:
        Choice.objects.create(
            question=question6,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q6] Failed to create choice {choice['label']}: {e}")


# === Question 7 ===
question7 = Question.objects.create(
    question_text="What road do you take from Naas to the Curragh?",
    question_type=Question.SINGLE
)
category_names7 = ["Naas", "Curragh", "Routes from This Area to Another", "Main Roads"]
for name in category_names7:
    try:
        cat = Category.objects.get(name=name)
        question7.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices7 = [
    {"text": "Ballyclane Road", "label": "A", "is_correct": True},
    {"text": "Blessington Road", "label": "B", "is_correct": False},
    {"text": "Dublin Road", "label": "C", "is_correct": False},
    {"text": "Abbey Street", "label": "D", "is_correct": False},
]
for choice in choices7:
    try:
        Choice.objects.create(
            question=question7,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q7] Failed to create choice {choice['label']}: {e}")


# === Question 8 ===
question8 = Question.objects.create(
    question_text="What street is Neighbourhood restaurant on in Naas?",
    question_type=Question.SINGLE
)
category_names8 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names8:
    try:
        cat = Category.objects.get(name=name)
        question8.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices8 = [
    {"text": "Maudlins Ave", "label": "A", "is_correct": True},
    {"text": "North Main St", "label": "B", "is_correct": False},
    {"text": "Tipper Road", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": False},
]
for choice in choices8:
    try:
        Choice.objects.create(
            question=question8,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q8] Failed to create choice {choice['label']}: {e}")


# === Question 9 ===
question9 = Question.objects.create(
    question_text="What roads do you take from Athy to Kilcullen?",
    question_type=Question.SINGLE
)
category_names9 = ["Athy", "Kilcullen", "Routes from This Area to Another", "Road Numbers"]
for name in category_names9:
    try:
        cat = Category.objects.get(name=name)
        question9.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices9 = [
    {"text": "R413 and N78", "label": "A", "is_correct": True},
    {"text": "N78", "label": "B", "is_correct": False},
    {"text": "R413 and R415", "label": "C", "is_correct": False},
    {"text": "N80 and R413", "label": "D", "is_correct": False},
]
for choice in choices9:
    try:
        Choice.objects.create(
            question=question9,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q9] Failed to create choice {choice['label']}: {e}")


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
        print(f"Category '{name}' not found in DB")
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


# === Question 11 ===
question11 = Question.objects.create(
    question_text="Where is Playbarn Kids centre?",
    question_type=Question.SINGLE
)
category_names11 = ["Johnstown", "Sports Clubs and Leisure Facilities"]
for name in category_names11:
    try:
        cat = Category.objects.get(name=name)
        question11.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices11 = [
    {"text": "Johnstown", "label": "A", "is_correct": True},
    {"text": "Naas", "label": "B", "is_correct": False},
    {"text": "Sallins", "label": "C", "is_correct": False},
    {"text": "Kill", "label": "D", "is_correct": False},
]
for choice in choices11:
    try:
        Choice.objects.create(
            question=question11,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q11] Failed to create choice {choice['label']}: {e}")


# === Question 12 ===
question12 = Question.objects.create(
    question_text="What road is Tesco Extra in Maynooth on?",
    question_type=Question.SINGLE
)
category_names12 = ["Maynooth", "Shopping Centres and Retail Parks", "Main Roads"]
for name in category_names12:
    try:
        cat = Category.objects.get(name=name)
        question12.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices12 = [
    {"text": "Dublin Rd and Leinster Park", "label": "A", "is_correct": True},
    {"text": "Maynooth and Kilcock", "label": "B", "is_correct": False},
    {"text": "Maynooth and Rathcoffee", "label": "C", "is_correct": False},
    {"text": "Lexlip and Maynooth", "label": "D", "is_correct": False},
]
for choice in choices12:
    try:
        Choice.objects.create(
            question=question12,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q12] Failed to create choice {choice['label']}: {e}")


# === Question 13 ===
question13 = Question.objects.create(
    question_text="What road is Celbridge Abbey Gardens on?",
    question_type=Question.SINGLE
)
category_names13 = ["Celbridge", "Parks and Gardens", "Main Roads"]
for name in category_names13:
    try:
        cat = Category.objects.get(name=name)
        question13.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices13 = [
    {"text": "Priory Lodge", "label": "A", "is_correct": True},
    {"text": "Newtown Rd", "label": "B", "is_correct": False},
    {"text": "Tea Ln", "label": "C", "is_correct": False},
    {"text": "Clane Rd", "label": "D", "is_correct": False},
]
for choice in choices13:
    try:
        Choice.objects.create(
            question=question13,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q13] Failed to create choice {choice['label']}: {e}")


# === Question 14 ===
question14 = Question.objects.create(
    question_text="Where is the K Club?",
    question_type=Question.SINGLE
)
category_names14 = ["Straffan", "Hotels and Guesthouses", "Sports Clubs and Leisure Facilities"]
for name in category_names14:
    try:
        cat = Category.objects.get(name=name)
        question14.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices14 = [
    {"text": "Naas", "label": "A", "is_correct": False},
    {"text": "Kilmeage", "label": "B", "is_correct": False},
    {"text": "Kill", "label": "C", "is_correct": False},
    {"text": "Straffan", "label": "D", "is_correct": True},
]
for choice in choices14:
    try:
        Choice.objects.create(
            question=question14,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q14] Failed to create choice {choice['label']}: {e}")


# === Question 15 ===
question15 = Question.objects.create(
    question_text="What towns do you pass going from Kildare to Dublin?",
    question_type=Question.SINGLE
)
category_names15 = ["Kildare (Town)", "Dublin", "Newbridge", "Naas", "Kill", "Towns/Villages Passed Through on Routes", "Routes from This Area to Another"]
for name in category_names15:
    try:
        cat = Category.objects.get(name=name)
        question15.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices15 = [
    {"text": "Naas, Clane; & Kilmeage", "label": "A", "is_correct": False},
    {"text": "Newbridge, Naas; & Kill", "label": "B", "is_correct": True},
    {"text": "Kilmeage; Clane; & Kill", "label": "C", "is_correct": False},
    {"text": "Clane, Newbridge; & Kill", "label": "D", "is_correct": False},
]
for choice in choices15:
    try:
        Choice.objects.create(
            question=question15,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q15] Failed to create choice {choice['label']}: {e}")


# === Question 16 ===
question16 = Question.objects.create(
    question_text="Where can you find the Newbridge Industrial Estate?",
    question_type=Question.SINGLE
)
category_names16 = ["Newbridge", "Business and Industrial Parks"]
for name in category_names16:
    try:
        cat = Category.objects.get(name=name)
        question16.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices16 = [
    {"text": "Currabeg", "label": "A", "is_correct": True},
    {"text": "Borahard", "label": "B", "is_correct": False},
    {"text": "Loughtown", "label": "C", "is_correct": False},
    {"text": "Kilbelin", "label": "D", "is_correct": False},
]
for choice in choices16:
    try:
        Choice.objects.create(
            question=question16,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q16] Failed to create choice {choice['label']}: {e}")


# === Question 17 ===
question17 = Question.objects.create(
    question_text="Where can you find the Newbridge Silverware Visitor Centre?",
    question_type=Question.SINGLE
)
category_names17 = ["Newbridge", "Museums and Galleries", "Main Roads"]
for name in category_names17:
    try:
        cat = Category.objects.get(name=name)
        question17.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices17 = [
    {"text": "Eyre Street", "label": "A", "is_correct": True},
    {"text": "Limerick Lane", "label": "B", "is_correct": False},
    {"text": "Station Road", "label": "C", "is_correct": False},
    {"text": "Athgarvan Road", "label": "D", "is_correct": False},
]
for choice in choices17:
    try:
        Choice.objects.create(
            question=question17,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q17] Failed to create choice {choice['label']}: {e}")


# === Question 18 ===
question18 = Question.objects.create(
    question_text="Where can you find the Coney housing estate?",
    question_type=Question.SINGLE
)
category_names18 = ["Athy", "Housing Estates"]
for name in category_names18:
    try:
        cat = Category.objects.get(name=name)
        question18.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices18 = [
    {"text": "Athy", "label": "A", "is_correct": True},
    {"text": "Naas", "label": "B", "is_correct": False},
    {"text": "Kildare Town", "label": "C", "is_correct": False},
    {"text": "Newbridge", "label": "D", "is_correct": False},
]
for choice in choices18:
    try:
        Choice.objects.create(
            question=question18,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q18] Failed to create choice {choice['label']}: {e}")


# === Question 19 ===
question19 = Question.objects.create(
    question_text="Where are the Japanese Gardens located?",
    question_type=Question.SINGLE
)
category_names19 = ["Kildare (Town)", "Parks and Gardens"]
for name in category_names19:
    try:
        cat = Category.objects.get(name=name)
        question19.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices19 = [
    {"text": "Kyle", "label": "A", "is_correct": False},
    {"text": "Beechpark", "label": "B", "is_correct": False},
    {"text": "Ballyvoneen", "label": "C", "is_correct": False},
    {"text": "Brallistown Little (Tully)", "label": "D", "is_correct": True},
]
for choice in choices19:
    try:
        Choice.objects.create(
            question=question19,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q19] Failed to create choice {choice['label']}: {e}")


# === Question 20 ===
question20 = Question.objects.create(
    question_text="Which of these roads is not directly connected with Edward Street?",
    question_type=Question.SINGLE
)
category_names20 = ["Newbridge", "Connecting Road Junctions and Roundabouts", "Main Roads"]
for name in category_names20:
    try:
        cat = Category.objects.get(name=name)
        question20.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices20 = [
    {"text": "Limerick Lane", "label": "A", "is_correct": True},
    {"text": "Cutlery Road", "label": "B", "is_correct": False},
    {"text": "Athgarvan Road", "label": "C", "is_correct": False},
    {"text": "Charlotte Street", "label": "D", "is_correct": False},
]
for choice in choices20:
    try:
        Choice.objects.create(
            question=question20,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q20] Failed to create choice {choice['label']}: {e}")


# === Question 21 ===
question21 = Question.objects.create(
    question_text="Which of these towns has no train station?",
    question_type=Question.SINGLE
)
category_names21 = ["Naas", "Sallins", "Clane", "Train Stations and Transport Hubs"]
for name in category_names21:
    try:
        cat = Category.objects.get(name=name)
        question21.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices21 = [
    {"text": "Kilcock", "label": "A", "is_correct": False},
    {"text": "Naas", "label": "B", "is_correct": False},
    {"text": "Sallins", "label": "C", "is_correct": False},
    {"text": "Clane", "label": "D", "is_correct": True},
]
for choice in choices21:
    try:
        Choice.objects.create(
            question=question21,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q21] Failed to create choice {choice['label']}: {e}")


# === Question 22 ===
question22 = Question.objects.create(
    question_text="What road is the Maynooth library situated on?",
    question_type=Question.SINGLE
)
category_names22 = ["Maynooth", "Libraries", "Main Roads"]
for name in category_names22:
    try:
        cat = Category.objects.get(name=name)
        question22.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices22 = [
    {"text": "Pound Lane", "label": "A", "is_correct": False},
    {"text": "Straffan Road", "label": "B", "is_correct": False},
    {"text": "Dunboyne Road", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": True},
]
for choice in choices22:
    try:
        Choice.objects.create(
            question=question22,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q22] Failed to create choice {choice['label']}: {e}")


# === Question 23 ===
question23 = Question.objects.create(
    question_text="What is the main road leading into the Shamrock Lodge in Athy?",
    question_type=Question.SINGLE
)
category_names23 = ["Athy", "Hotels and Guesthouses", "Main Roads"]
for name in category_names23:
    try:
        cat = Category.objects.get(name=name)
        question23.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices23 = [
    {"text": "Gallowshill", "label": "A", "is_correct": True},
    {"text": "Church Road", "label": "B", "is_correct": False},
    {"text": "Geraldine Road", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": False},
]
for choice in choices23:
    try:
        Choice.objects.create(
            question=question23,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q23] Failed to create choice {choice['label']}: {e}")


# === Question 24 ===
question24 = Question.objects.create(
    question_text="What roads adjoin with Edward Street in Newbridge?",
    question_type=Question.SINGLE
)
category_names24 = ["Newbridge", "Connecting Road Junctions and Roundabouts", "Main Roads"]
for name in category_names24:
    try:
        cat = Category.objects.get(name=name)
        question24.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices24 = [
    {"text": "Henry Street & Main Street", "label": "A", "is_correct": True},
    {"text": "Eyre Street & James' Lane", "label": "B", "is_correct": False},
    {"text": "Rowan Terrace & The Grange", "label": "C", "is_correct": False},
    {"text": "College Park Road & Station Road", "label": "D", "is_correct": False},
]
for choice in choices24:
    try:
        Choice.objects.create(
            question=question24,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q24] Failed to create choice {choice['label']}: {e}")


# === Question 25 ===
question25 = Question.objects.create(
    question_text="What road runs between Anne Street and John Street?",
    question_type=Question.SINGLE
)
category_names25 = ["Newbridge", "Connecting Road Junctions and Roundabouts", "Main Roads"]
for name in category_names25:
    try:
        cat = Category.objects.get(name=name)
        question25.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices25 = [
    {"text": "James Street", "label": "A", "is_correct": True},
    {"text": "Thomas Street", "label": "B", "is_correct": False},
    {"text": "Patrick Street", "label": "C", "is_correct": False},
    {"text": "Francis Street", "label": "D", "is_correct": False},
]
for choice in choices25:
    try:
        Choice.objects.create(
            question=question25,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q25] Failed to create choice {choice['label']}: {e}")


# === Question 26 ===
question26 = Question.objects.create(
    question_text="Travelling from Naas, what road do you take to Punchestown Racecourse?",
    question_type=Question.SINGLE
)
category_names26 = ["Naas", "Punchestown", "Routes from This Area to Another", "Road Numbers", "Racecourses"]
for name in category_names26:
    try:
        cat = Category.objects.get(name=name)
        question26.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices26 = [
    {"text": "R448", "label": "A", "is_correct": False},
    {"text": "R410", "label": "B", "is_correct": True},
    {"text": "R445", "label": "C", "is_correct": False},
    {"text": "R409", "label": "D", "is_correct": False},
]
for choice in choices26:
    try:
        Choice.objects.create(
            question=question26,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q26] Failed to create choice {choice['label']}: {e}")


# === Question 27 ===
question27 = Question.objects.create(
    question_text="Where is the Athy Health Centre located?",
    question_type=Question.SINGLE
)
category_names27 = ["Athy", "Hospitals and Medical Centres"]
for name in category_names27:
    try:
        cat = Category.objects.get(name=name)
        question27.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices27 = [
    {"text": "Kings Grove", "label": "A", "is_correct": False},
    {"text": "Rockfield Road", "label": "B", "is_correct": False},
    {"text": "Bleach Road", "label": "C", "is_correct": False},
    {"text": "Carlow Road", "label": "D", "is_correct": True},
]
for choice in choices27:
    try:
        Choice.objects.create(
            question=question27,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q27] Failed to create choice {choice['label']}: {e}")


# === Question 28 ===
question28 = Question.objects.create(
    question_text="Name the road that houses Athy Library:",
    question_type=Question.SINGLE
)
category_names28 = ["Athy", "Libraries", "Main Roads"]
for name in category_names28:
    try:
        cat = Category.objects.get(name=name)
        question28.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices28 = [
    {"text": "Emily Square", "label": "A", "is_correct": True},
    {"text": "Church Road", "label": "B", "is_correct": False},
    {"text": "Stanhope Street", "label": "C", "is_correct": False},
    {"text": "Convent Lane", "label": "D", "is_correct": False},
]
for choice in choices28:
    try:
        Choice.objects.create(
            question=question28,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q28] Failed to create choice {choice['label']}: {e}")


# === Question 29 ===
question29 = Question.objects.create(
    question_text="Where can Celbridge Library be found?",
    question_type=Question.SINGLE
)
category_names29 = ["Celbridge", "Libraries", "Main Roads"]
for name in category_names29:
    try:
        cat = Category.objects.get(name=name)
        question29.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices29 = [
    {"text": "Maynooth Road", "label": "A", "is_correct": False},
    {"text": "St. Patrick's Park", "label": "B", "is_correct": True},
    {"text": "Castletown Drive", "label": "C", "is_correct": False},
    {"text": "Shackleton Road", "label": "D", "is_correct": False},
]
for choice in choices29:
    try:
        Choice.objects.create(
            question=question29,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q29] Failed to create choice {choice['label']}: {e}")


# === Question 30 ===
question30 = Question.objects.create(
    question_text="San Carlo Junior School is located where in Leixlip?",
    question_type=Question.SINGLE
)
category_names30 = ["Leixlip", "Schools and Educational Institutions", "Main Roads"]
for name in category_names30:
    try:
        cat = Category.objects.get(name=name)
        question30.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices30 = [
    {"text": "Captains Hill", "label": "A", "is_correct": True},
    {"text": "Newtown", "label": "B", "is_correct": False},
    {"text": "Glendale", "label": "C", "is_correct": False},
    {"text": "Avondale", "label": "D", "is_correct": False},
]
for choice in choices30:
    try:
        Choice.objects.create(
            question=question30,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q30] Failed to create choice {choice['label']}: {e}")


# === Question 31 ===
question31 = Question.objects.create(
    question_text="Which of these roads houses St Patrick's College in Maynooth?",
    question_type=Question.SINGLE
)
category_names31 = ["Maynooth", "Schools and Educational Institutions", "Main Roads"]
for name in category_names31:
    try:
        cat = Category.objects.get(name=name)
        question31.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices31 = [
    {"text": "Leinster Street", "label": "A", "is_correct": False},
    {"text": "Pound Lane", "label": "B", "is_correct": False},
    {"text": "Straffan Road", "label": "C", "is_correct": False},
    {"text": "Parson Street", "label": "D", "is_correct": True},
]
for choice in choices31:
    try:
        Choice.objects.create(
            question=question31,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q31] Failed to create choice {choice['label']}: {e}")


# === Question 32 ===
question32 = Question.objects.create(
    question_text="What road leads to the main entrance of the Maynooth University?",
    question_type=Question.SINGLE
)
category_names32 = ["Maynooth", "Schools and Educational Institutions", "Main Roads"]
for name in category_names32:
    try:
        cat = Category.objects.get(name=name)
        question32.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices32 = [
    {"text": "Kilcock Road", "label": "A", "is_correct": False},
    {"text": "Maynooth Park", "label": "B", "is_correct": False},
    {"text": "Straffan Road", "label": "C", "is_correct": True},
    {"text": "Newtown Road", "label": "D", "is_correct": False},
]
for choice in choices32:
    try:
        Choice.objects.create(
            question=question32,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q32] Failed to create choice {choice['label']}: {e}")


# === Question 33 ===
question33 = Question.objects.create(
    question_text="Where is the Maynooth Boys National School located?",
    question_type=Question.SINGLE
)
category_names33 = ["Maynooth", "Schools and Educational Institutions", "Main Roads"]
for name in category_names33:
    try:
        cat = Category.objects.get(name=name)
        question33.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices33 = [
    {"text": "Meadowbrook Road", "label": "A", "is_correct": False},
    {"text": "Newtown Road", "label": "B", "is_correct": False},
    {"text": "Kilcock Road", "label": "C", "is_correct": False},
    {"text": "Moyglare Road", "label": "D", "is_correct": True},
]
for choice in choices33:
    try:
        Choice.objects.create(
            question=question33,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q33] Failed to create choice {choice['label']}: {e}")


# === Question 34 ===
question34 = Question.objects.create(
    question_text="Presentation Girls School can be found where in Maynooth?",
    question_type=Question.SINGLE
)
category_names34 = ["Maynooth", "Schools and Educational Institutions", "Main Roads"]
for name in category_names34:
    try:
        cat = Category.objects.get(name=name)
        question34.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices34 = [
    {"text": "Parson Street", "label": "A", "is_correct": True},
    {"text": "Kilcock Road", "label": "B", "is_correct": False},
    {"text": "Moyglare Road", "label": "C", "is_correct": False},
    {"text": "Dunboyne Road", "label": "D", "is_correct": False},
]
for choice in choices34:
    try:
        Choice.objects.create(
            question=question34,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q34] Failed to create choice {choice['label']}: {e}")


# === Question 35 ===
question35 = Question.objects.create(
    question_text="Pick the street that houses St Brigid's Girls National School situated in Celbridge?",
    question_type=Question.SINGLE
)
category_names35 = ["Celbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names35:
    try:
        cat = Category.objects.get(name=name)
        question35.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices35 = [
    {"text": "Maynooth Road", "label": "A", "is_correct": False},
    {"text": "Shackleton Road", "label": "B", "is_correct": False},
    {"text": "Oldtown Road", "label": "C", "is_correct": True},
    {"text": "Main Street", "label": "D", "is_correct": False},
]
for choice in choices35:
    try:
        Choice.objects.create(
            question=question35,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q35] Failed to create choice {choice['label']}: {e}")


# === Question 36 ===
question36 = Question.objects.create(
    question_text="The Primrose Hill National School is located where in Celbridge?",
    question_type=Question.SINGLE
)
category_names36 = ["Celbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names36:
    try:
        cat = Category.objects.get(name=name)
        question36.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices36 = [
    {"text": "Clane Road", "label": "A", "is_correct": True},
    {"text": "Newtown Road", "label": "B", "is_correct": False},
    {"text": "Loughlinstown Road", "label": "C", "is_correct": False},
    {"text": "Hazelhatch Road", "label": "D", "is_correct": False},
]
for choice in choices36:
    try:
        Choice.objects.create(
            question=question36,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q36] Failed to create choice {choice['label']}: {e}")


# === Question 37 ===
question37 = Question.objects.create(
    question_text="Select the road that houses North Kildare Educate Together School in Celbridge?",
    question_type=Question.SINGLE
)
category_names37 = ["Celbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names37:
    try:
        cat = Category.objects.get(name=name)
        question37.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices37 = [
    {"text": "Clane Road", "label": "A", "is_correct": False},
    {"text": "Oldtown Road", "label": "B", "is_correct": False},
    {"text": "Maynooth Road", "label": "C", "is_correct": False},
    {"text": "The Walk", "label": "D", "is_correct": True},
]
for choice in choices37:
    try:
        Choice.objects.create(
            question=question37,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q37] Failed to create choice {choice['label']}: {e}")


# === Question 38 ===
question38 = Question.objects.create(
    question_text="Where is the St Conleth's & Mary's National School located in Newbridge?",
    question_type=Question.SINGLE
)
category_names38 = ["Newbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names38:
    try:
        cat = Category.objects.get(name=name)
        question38.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices38 = [
    {"text": "The Priory", "label": "A", "is_correct": False},
    {"text": "Naas Road", "label": "B", "is_correct": False},
    {"text": "St Dominics Park", "label": "C", "is_correct": False},
    {"text": "Chapel Lane", "label": "D", "is_correct": True},
]
for choice in choices38:
    try:
        Choice.objects.create(
            question=question38,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q38] Failed to create choice {choice['label']}: {e}")


# === Question 39 ===
question39 = Question.objects.create(
    question_text="Name the road that St Patrick's National School is located on in Newbridge?",
    question_type=Question.SINGLE
)
category_names39 = ["Newbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names39:
    try:
        cat = Category.objects.get(name=name)
        question39.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices39 = [
    {"text": "Morristown Road", "label": "A", "is_correct": True},
    {"text": "Blackberry Lane", "label": "B", "is_correct": False},
    {"text": "Dara Park", "label": "C", "is_correct": False},
    {"text": "The Elms", "label": "D", "is_correct": False},
]
for choice in choices39:
    try:
        Choice.objects.create(
            question=question39,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q39] Failed to create choice {choice['label']}: {e}")


# === Question 40 ===
question40 = Question.objects.create(
    question_text="What road houses Scoil Mhuire in Newbridge?",
    question_type=Question.SINGLE
)
category_names40 = ["Newbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names40:
    try:
        cat = Category.objects.get(name=name)
        question40.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices40 = [
    {"text": "Langton Road", "label": "A", "is_correct": False},
    {"text": "Morristown Road", "label": "B", "is_correct": False},
    {"text": "Standhouse Road", "label": "C", "is_correct": True},
    {"text": "The Oaks", "label": "D", "is_correct": False},
]
for choice in choices40:
    try:
        Choice.objects.create(
            question=question40,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q40] Failed to create choice {choice['label']}: {e}")


# === Question 41 ===
question41 = Question.objects.create(
    question_text="Newbridge Educate Together National School is situated where?",
    question_type=Question.SINGLE
)
category_names41 = ["Newbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names41:
    try:
        cat = Category.objects.get(name=name)
        question41.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices41 = [
    {"text": "Curragh Chase", "label": "A", "is_correct": True},
    {"text": "Rosemount Court", "label": "B", "is_correct": False},
    {"text": "Green Road", "label": "C", "is_correct": False},
    {"text": "Ballymany", "label": "D", "is_correct": False},
]
for choice in choices41:
    try:
        Choice.objects.create(
            question=question41,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q41] Failed to create choice {choice['label']}: {e}")


# === Question 42 ===
question42 = Question.objects.create(
    question_text="Where is the Newbridge College located?",
    question_type=Question.SINGLE
)
category_names42 = ["Newbridge", "Schools and Educational Institutions", "Main Roads"]
for name in category_names42:
    try:
        cat = Category.objects.get(name=name)
        question42.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices42 = [
    {"text": "Common", "label": "A", "is_correct": False},
    {"text": "The Glen", "label": "B", "is_correct": False},
    {"text": "College Park Road", "label": "C", "is_correct": True},
    {"text": "Rosconnell Avenue", "label": "D", "is_correct": False},
]
for choice in choices42:
    try:
        Choice.objects.create(
            question=question42,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q42] Failed to create choice {choice['label']}: {e}")


# === Question 43 ===
question43 = Question.objects.create(
    question_text="What road houses Scoil Bhride in Naas?",
    question_type=Question.SINGLE
)
category_names43 = ["Naas", "Schools and Educational Institutions", "Main Roads"]
for name in category_names43:
    try:
        cat = Category.objects.get(name=name)
        question43.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices43 = [
    {"text": "Church Road", "label": "A", "is_correct": False},
    {"text": "Clane Road", "label": "B", "is_correct": False},
    {"text": "Monread Road", "label": "C", "is_correct": False},
    {"text": "Sallins Road", "label": "D", "is_correct": True},
]
for choice in choices43:
    try:
        Choice.objects.create(
            question=question43,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q43] Failed to create choice {choice['label']}: {e}")


# === Question 44 ===
question44 = Question.objects.create(
    question_text="Mercy Convent Primary School can be found where in Naas?",
    question_type=Question.SINGLE
)
category_names44 = ["Naas", "Schools and Educational Institutions", "Main Roads"]
for name in category_names44:
    try:
        cat = Category.objects.get(name=name)
        question44.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices44 = [
    {"text": "Woodlands", "label": "A", "is_correct": False},
    {"text": "Sallins Road", "label": "B", "is_correct": True},
    {"text": "Dublin Road", "label": "C", "is_correct": False},
    {"text": "Tipper Road", "label": "D", "is_correct": False},
]
for choice in choices44:
    try:
        Choice.objects.create(
            question=question44,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q44] Failed to create choice {choice['label']}: {e}")


# === Question 45 ===
question45 = Question.objects.create(
    question_text="St Corbans boys national school is located on what road in Naas?",
    question_type=Question.SINGLE
)
category_names45 = ["Naas", "Schools and Educational Institutions", "Main Roads"]
for name in category_names45:
    try:
        cat = Category.objects.get(name=name)
        question45.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices45 = [
    {"text": "Cillcorban", "label": "A", "is_correct": False},
    {"text": "Sarto Road", "label": "B", "is_correct": False},
    {"text": "Pacelli Road", "label": "C", "is_correct": False},
    {"text": "Corban's Lane", "label": "D", "is_correct": True},
]
for choice in choices45:
    try:
        Choice.objects.create(
            question=question45,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q45] Failed to create choice {choice['label']}: {e}")


# === Question 46 ===
question46 = Question.objects.create(
    question_text="Where can you find Kildare Town Community School?",
    question_type=Question.SINGLE
)
category_names46 = ["Kildare (Town)", "Schools and Educational Institutions", "Main Roads"]
for name in category_names46:
    try:
        cat = Category.objects.get(name=name)
        question46.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices46 = [
    {"text": "Dunmurray Road", "label": "A", "is_correct": True},
    {"text": "Grey Abbey", "label": "B", "is_correct": False},
    {"text": "Rathbride Road", "label": "C", "is_correct": False},
    {"text": "Green Road", "label": "D", "is_correct": False},
]
for choice in choices46:
    try:
        Choice.objects.create(
            question=question46,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q46] Failed to create choice {choice['label']}: {e}")


# === Question 47 ===
question47 = Question.objects.create(
    question_text="Where is Kildare Town Educate Together National School?",
    question_type=Question.SINGLE
)
category_names47 = ["Kildare (Town)", "Schools and Educational Institutions", "Main Roads"]
for name in category_names47:
    try:
        cat = Category.objects.get(name=name)
        question47.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices47 = [
    {"text": "Bishopsland", "label": "A", "is_correct": True},
    {"text": "Willow Grove", "label": "B", "is_correct": False},
    {"text": "Chapel Road", "label": "C", "is_correct": False},
    {"text": "Melitta Road", "label": "D", "is_correct": False},
]
for choice in choices47:
    try:
        Choice.objects.create(
            question=question47,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q47] Failed to create choice {choice['label']}: {e}")


# === Question 48 ===
question48 = Question.objects.create(
    question_text="St Brigid's Primary School is located where in Kildare?",
    question_type=Question.SINGLE
)
category_names48 = ["Kildare (Town)", "Schools and Educational Institutions", "Main Roads"]
for name in category_names48:
    try:
        cat = Category.objects.get(name=name)
        question48.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices48 = [
    {"text": "Grey Abbey Road", "label": "A", "is_correct": False},
    {"text": "Bride Street", "label": "B", "is_correct": True},
    {"text": "Pigeon Lane", "label": "C", "is_correct": False},
    {"text": "Priests Lane", "label": "D", "is_correct": False},
]
for choice in choices48:
    try:
        Choice.objects.create(
            question=question48,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q48] Failed to create choice {choice['label']}: {e}")


# === Question 49 ===
question49 = Question.objects.create(
    question_text="Where can you find Gaelscoil Mhic Aodha in Kildare?",
    question_type=Question.SINGLE
)
category_names49 = ["Kildare (Town)", "Schools and Educational Institutions", "Main Roads"]
for name in category_names49:
    try:
        cat = Category.objects.get(name=name)
        question49.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices49 = [
    {"text": "Monasterevin Road", "label": "A", "is_correct": True},
    {"text": "Dunmurray Road", "label": "B", "is_correct": False},
    {"text": "Melitta Road", "label": "C", "is_correct": False},
    {"text": "Rathbride Road", "label": "D", "is_correct": False},
]
for choice in choices49:
    try:
        Choice.objects.create(
            question=question49,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q49] Failed to create choice {choice['label']}: {e}")


# === Question 50 ===
question50 = Question.objects.create(
    question_text="The Further Education and Training Centre in Kildare town can be found where?",
    question_type=Question.SINGLE
)
category_names50 = ["Kildare (Town)", "Schools and Educational Institutions", "Main Roads"]
for name in category_names50:
    try:
        cat = Category.objects.get(name=name)
        question50.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices50 = [
    {"text": "Lourdesville", "label": "A", "is_correct": False},
    {"text": "Melitta Road", "label": "B", "is_correct": False},
    {"text": "Fair Green Road", "label": "C", "is_correct": True},
    {"text": "Priest's Lane", "label": "D", "is_correct": False},
]
for choice in choices50:
    try:
        Choice.objects.create(
            question=question50,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q50] Failed to create choice {choice['label']}: {e}")


# === Question 51 ===
question51 = Question.objects.create(
    question_text="What road leads into Scoil Phadraig Naofa in Athy?",
    question_type=Question.SINGLE
)
category_names51 = ["Athy", "Schools and Educational Institutions", "Main Roads"]
for name in category_names51:
    try:
        cat = Category.objects.get(name=name)
        question51.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices51 = [
    {"text": "Kingsgrove", "label": "A", "is_correct": True},
    {"text": "Rathstewart Crescent", "label": "B", "is_correct": False},
    {"text": "Conneyboro", "label": "C", "is_correct": False},
    {"text": "Old Lawm", "label": "D", "is_correct": False},
]
for choice in choices51:
    try:
        Choice.objects.create(
            question=question51,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q51] Failed to create choice {choice['label']}: {e}")


# === Question 52 ===
question52 = Question.objects.create(
    question_text="Where is Athy College located?",
    question_type=Question.SINGLE
)
category_names52 = ["Athy", "Schools and Educational Institutions", "Main Roads"]
for name in category_names52:
    try:
        cat = Category.objects.get(name=name)
        question52.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices52 = [
    {"text": "Monasterevin Road", "label": "A", "is_correct": True},
    {"text": "Rockfield Road", "label": "B", "is_correct": False},
    {"text": "Earls Court", "label": "C", "is_correct": False},
    {"text": "Salisbury", "label": "D", "is_correct": False},
]
for choice in choices52:
    try:
        Choice.objects.create(
            question=question52,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q52] Failed to create choice {choice['label']}: {e}")


# === Question 53 ===
question53 = Question.objects.create(
    question_text="Which of these streets is Ardscoil na Trinoide situated on in Athy?",
    question_type=Question.SINGLE
)
category_names53 = ["Athy", "Schools and Educational Institutions", "Main Roads"]
for name in category_names53:
    try:
        cat = Category.objects.get(name=name)
        question53.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices53 = [
    {"text": "Rathstewart", "label": "A", "is_correct": True},
    {"text": "Geraldine Road", "label": "B", "is_correct": False},
    {"text": "Woodstock Street", "label": "C", "is_correct": False},
    {"text": "Holland's Close", "label": "D", "is_correct": False},
]
for choice in choices53:
    try:
        Choice.objects.create(
            question=question53,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q53] Failed to create choice {choice['label']}: {e}")


# === Question 54 ===
question54 = Question.objects.create(
    question_text="Scoil Mhichil Naofa can be found where in Athy?",
    question_type=Question.SINGLE
)
category_names54 = ["Athy", "Schools and Educational Institutions", "Main Roads"]
for name in category_names54:
    try:
        cat = Category.objects.get(name=name)
        question54.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices54 = [
    {"text": "Shamrock Drive", "label": "A", "is_correct": True},
    {"text": "Mount Hawkins", "label": "B", "is_correct": False},
    {"text": "The Hollands", "label": "C", "is_correct": False},
    {"text": "Castle Park", "label": "D", "is_correct": False},
]
for choice in choices54:
    try:
        Choice.objects.create(
            question=question54,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q54] Failed to create choice {choice['label']}: {e}")


# === Question 55 ===
question55 = Question.objects.create(
    question_text="Where is the Athy Adult Learning centre Located?",
    question_type=Question.SINGLE
)
category_names55 = ["Athy", "Schools and Educational Institutions", "Main Roads"]
for name in category_names55:
    try:
        cat = Category.objects.get(name=name)
        question55.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices55 = [
    {"text": "Carlow Road", "label": "A", "is_correct": True},
    {"text": "Woodstock Street", "label": "B", "is_correct": False},
    {"text": "Convent View", "label": "C", "is_correct": False},
    {"text": "Stanhope Place", "label": "D", "is_correct": False},
]
for choice in choices55:
    try:
        Choice.objects.create(
            question=question55,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q55] Failed to create choice {choice['label']}: {e}")


# === Question 56 ===
question56 = Question.objects.create(
    question_text="Off which road is IDA Business Park located in Newbridge?",
    question_type=Question.SINGLE
)
category_names56 = ["Newbridge", "Business and Industrial Parks", "Main Roads"]
for name in category_names56:
    try:
        cat = Category.objects.get(name=name)
        question56.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices56 = [
    {"text": "Green Road", "label": "A", "is_correct": True},
    {"text": "The Hall", "label": "B", "is_correct": False},
    {"text": "Edward Street", "label": "C", "is_correct": False},
    {"text": "Langton Road", "label": "D", "is_correct": False},
]
for choice in choices56:
    try:
        Choice.objects.create(
            question=question56,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q56] Failed to create choice {choice['label']}: {e}")


# === Question 57 ===
question57 = Question.objects.create(
    question_text="Where can Kildare Business Park be located?",
    question_type=Question.SINGLE
)
category_names57 = ["Kildare (Town)", "Business and Industrial Parks", "Main Roads"]
for name in category_names57:
    try:
        cat = Category.objects.get(name=name)
        question57.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices57 = [
    {"text": "Rathbride Road", "label": "A", "is_correct": True},
    {"text": "Curragh Road", "label": "B", "is_correct": False},
    {"text": "Melitta Road", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": False},
]
for choice in choices57:
    try:
        Choice.objects.create(
            question=question57,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q57] Failed to create choice {choice['label']}: {e}")


# === Question 58 ===
question58 = Question.objects.create(
    question_text="Which street leads into Monatrea industrial estate located in Celbridge?",
    question_type=Question.SINGLE
)
category_names58 = ["Celbridge", "Business and Industrial Parks", "Main Roads"]
for name in category_names58:
    try:
        cat = Category.objects.get(name=name)
        question58.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices58 = [
    {"text": "Maynooth Road", "label": "A", "is_correct": True},
    {"text": "Tea Lane", "label": "B", "is_correct": False},
    {"text": "Dublin Road", "label": "C", "is_correct": False},
    {"text": "Elm Park", "label": "D", "is_correct": False},
]
for choice in choices58:
    try:
        Choice.objects.create(
            question=question58,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q58] Failed to create choice {choice['label']}: {e}")


# === Question 59 ===
question59 = Question.objects.create(
    question_text="Maynooth Business Campus is accessed from what road?",
    question_type=Question.SINGLE
)
category_names59 = ["Maynooth", "Business and Industrial Parks", "Main Roads"]
for name in category_names59:
    try:
        cat = Category.objects.get(name=name)
        question59.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices59 = [
    {"text": "Newtown Road", "label": "A", "is_correct": False},
    {"text": "Moyglare Road", "label": "B", "is_correct": False},
    {"text": "Dunboyne Road", "label": "C", "is_correct": False},
    {"text": "Straffan Road", "label": "D", "is_correct": True},
]
for choice in choices59:
    try:
        Choice.objects.create(
            question=question59,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q59] Failed to create choice {choice['label']}: {e}")


# === Question 60 ===
question60 = Question.objects.create(
    question_text="Newbridge Industrial Estate is found on what road?",
    question_type=Question.SINGLE
)
category_names60 = ["Newbridge", "Business and Industrial Parks", "Main Roads"]
for name in category_names60:
    try:
        cat = Category.objects.get(name=name)
        question60.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices60 = [
    {"text": "Standhouse Road", "label": "A", "is_correct": True},
    {"text": "Athgarvan Road", "label": "B", "is_correct": False},
    {"text": "Morristown Road", "label": "C", "is_correct": False},
    {"text": "Green Road", "label": "D", "is_correct": False},
]
for choice in choices60:
    try:
        Choice.objects.create(
            question=question60,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q60] Failed to create choice {choice['label']}: {e}")


# === Question 61 ===
question61 = Question.objects.create(
    question_text="Celbridge Industrial Estate can be accessed from what road?",
    question_type=Question.SINGLE
)
category_names61 = ["Celbridge", "Business and Industrial Parks", "Main Roads"]
for name in category_names61:
    try:
        cat = Category.objects.get(name=name)
        question61.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices61 = [
    {"text": "Dublin Road", "label": "A", "is_correct": True},
    {"text": "Maynooth Road", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": False},
    {"text": "Shackleton Road", "label": "D", "is_correct": False},
]
for choice in choices61:
    try:
        Choice.objects.create(
            question=question61,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q61] Failed to create choice {choice['label']}: {e}")


# === Question 62 ===
question62 = Question.objects.create(
    question_text="Off which road is Naas Industrial Estate located?",
    question_type=Question.SINGLE
)
category_names62 = ["Naas", "Business and Industrial Parks", "Main Roads"]
for name in category_names62:
    try:
        cat = Category.objects.get(name=name)
        question62.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices62 = [
    {"text": "Dublin Road", "label": "A", "is_correct": False},
    {"text": "Monread Road", "label": "B", "is_correct": False},
    {"text": "Ballyclane Road", "label": "C", "is_correct": False},
    {"text": "Sallins Road", "label": "D", "is_correct": True},
]
for choice in choices62:
    try:
        Choice.objects.create(
            question=question62,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q62] Failed to create choice {choice['label']}: {e}")


# === Question 63 ===
question63 = Question.objects.create(
    question_text="Travelling from Monasterevin to Portlaoise on the R445, what areas do you pass?",
    question_type=Question.SINGLE
)
category_names63 = ["Monasterevin", "Portlaoise", "Routes from This Area to Another", "Road Numbers", "Towns/Villages Passed Through on Routes"]
for name in category_names63:
    try:
        cat = Category.objects.get(name=name)
        question63.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices63 = [
    {"text": "Fairgreen & Ballyfin", "label": "A", "is_correct": False},
    {"text": "Ballybrittas & Morett", "label": "B", "is_correct": True},
    {"text": "Loughteague & Knockbawn", "label": "C", "is_correct": False},
    {"text": "Scrub & Foxburrow", "label": "D", "is_correct": False},
]
for choice in choices63:
    try:
        Choice.objects.create(
            question=question63,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q63] Failed to create choice {choice['label']}: {e}")


# === Question 64 ===
question64 = Question.objects.create(
    question_text="What areas would you pass through on the way from Monasterevin to Athy on the R417?",
    question_type=Question.SINGLE
)
category_names64 = ["Monasterevin", "Athy", "Routes from This Area to Another", "Road Numbers", "Towns/Villages Passed Through on Routes"]
for name in category_names64:
    try:
        cat = Category.objects.get(name=name)
        question64.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices64 = [
    {"text": "Nurney & Whitelands", "label": "A", "is_correct": False},
    {"text": "Moatefield & Downings", "label": "B", "is_correct": False},
    {"text": "Lackagh & Quinnsboro", "label": "C", "is_correct": False},
    {"text": "Kildangan & Kilberry", "label": "D", "is_correct": True},
]
for choice in choices64:
    try:
        Choice.objects.create(
            question=question64,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q64] Failed to create choice {choice['label']}: {e}")


# === Question 65 ===
question65 = Question.objects.create(
    question_text="Which of these roads do you take travelling from Athy to Kilkenny?",
    question_type=Question.SINGLE
)
category_names65 = ["Athy", "Kilkenny", "Routes from This Area to Another", "Road Numbers"]
for name in category_names65:
    try:
        cat = Category.objects.get(name=name)
        question65.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices65 = [
    {"text": "N81 & N80", "label": "A", "is_correct": False},
    {"text": "N78 & N77", "label": "B", "is_correct": True},
    {"text": "N80 & N79", "label": "C", "is_correct": False},
    {"text": "N77 & N10", "label": "D", "is_correct": False},
]
for choice in choices65:
    try:
        Choice.objects.create(
            question=question65,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q65] Failed to create choice {choice['label']}: {e}")


# === Question 66 ===
question66 = Question.objects.create(
    question_text="If travelling from Athy to Waterford, which roads would you take?",
    question_type=Question.SINGLE
)
category_names66 = ["Athy", "Waterford", "Routes from This Area to Another", "Road Numbers"]
for name in category_names66:
    try:
        cat = Category.objects.get(name=name)
        question66.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices66 = [
    {"text": "N78 & M9", "label": "A", "is_correct": True},
    {"text": "N78 & N76", "label": "B", "is_correct": False},
    {"text": "N78 & N80", "label": "C", "is_correct": False},
    {"text": "N81 & N80", "label": "D", "is_correct": False},
]
for choice in choices66:
    try:
        Choice.objects.create(
            question=question66,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q66] Failed to create choice {choice['label']}: {e}")


# === Question 67 ===
question67 = Question.objects.create(
    question_text="Choose the road you would take from Celbridge to Maynooth?",
    question_type=Question.SINGLE
)
category_names67 = ["Celbridge", "Maynooth", "Routes from This Area to Another", "Road Numbers"]
for name in category_names67:
    try:
        cat = Category.objects.get(name=name)
        question67.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices67 = [
    {"text": "R148", "label": "A", "is_correct": True},
    {"text": "R449", "label": "B", "is_correct": False},
    {"text": "R15z", "label": "C", "is_correct": False},
    {"text": "R405", "label": "D", "is_correct": False},
]
for choice in choices67:
    try:
        Choice.objects.create(
            question=question67,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q67] Failed to create choice {choice['label']}: {e}")


# === Question 68 ===
question68 = Question.objects.create(
    question_text="Which roads must you take driving from Celbridge to Lucan?",
    question_type=Question.SINGLE
)
category_names68 = ["Celbridge", "Lucan", "Routes from This Area to Another", "Road Numbers"]
for name in category_names68:
    try:
        cat = Category.objects.get(name=name)
        question68.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices68 = [
    {"text": "R405 & R120", "label": "A", "is_correct": False},
    {"text": "R403 & R835", "label": "B", "is_correct": False},
    {"text": "R10? & R149", "label": "C", "is_correct": False},
    {"text": "R449 & R148", "label": "D", "is_correct": True},
]
for choice in choices68:
    try:
        Choice.objects.create(
            question=question68,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q68] Failed to create choice {choice['label']}: {e}")


# === Question 69 ===
question69 = Question.objects.create(
    question_text="What road would you take going from Celbridge to Newcastle?",
    question_type=Question.SINGLE
)
category_names69 = ["Celbridge", "Newcastle", "Routes from This Area to Another", "Road Numbers"]
for name in category_names69:
    try:
        cat = Category.objects.get(name=name)
        question69.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices69 = [
    {"text": "R403", "label": "A", "is_correct": True},
    {"text": "R405", "label": "B", "is_correct": False},
    {"text": "R449", "label": "C", "is_correct": False},
    {"text": "R120", "label": "D", "is_correct": False},
]
for choice in choices69:
    try:
        Choice.objects.create(
            question=question69,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q69] Failed to create choice {choice['label']}: {e}")


# === Question 70 ===
question70 = Question.objects.create(
    question_text="Which of these roads connects Kildare to Portlaoise?",
    question_type=Question.SINGLE
)
category_names70 = ["Kildare (Town)", "Portlaoise", "Routes from This Area to Another", "Road Numbers"]
for name in category_names70:
    try:
        cat = Category.objects.get(name=name)
        question70.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices70 = [
    {"text": "M7", "label": "A", "is_correct": True},
    {"text": "M4", "label": "B", "is_correct": False},
    {"text": "M9", "label": "C", "is_correct": False},
    {"text": "N81", "label": "D", "is_correct": False},
]
for choice in choices70:
    try:
        Choice.objects.create(
            question=question70,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q70] Failed to create choice {choice['label']}: {e}")


# === Question 71 ===
question71 = Question.objects.create(
    question_text="What Road would you take from Naas to Dublin?",
    question_type=Question.SINGLE
)
category_names71 = ["Naas", "Dublin", "Routes from This Area to Another", "Road Numbers"]
for name in category_names71:
    try:
        cat = Category.objects.get(name=name)
        question71.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices71 = [
    {"text": "N7", "label": "A", "is_correct": True},
    {"text": "N81", "label": "B", "is_correct": False},
    {"text": "M9", "label": "C", "is_correct": False},
    {"text": "M4", "label": "D", "is_correct": False},
]
for choice in choices71:
    try:
        Choice.objects.create(
            question=question71,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q71] Failed to create choice {choice['label']}: {e}")


# === Question 72 ===
question72 = Question.objects.create(
    question_text="Simmonstown Manor housing estate is located on which road in Celbridge?",
    question_type=Question.SINGLE
)
category_names72 = ["Celbridge", "Housing Estates", "Main Roads"]
for name in category_names72:
    try:
        cat = Category.objects.get(name=name)
        question72.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices72 = [
    {"text": "Shackleton Road", "label": "A", "is_correct": False},
    {"text": "Oldtown Road", "label": "B", "is_correct": False},
    {"text": "Newtown Road", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": True},
]
for choice in choices72:
    try:
        Choice.objects.create(
            question=question72,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q72] Failed to create choice {choice['label']}: {e}")


# === Question 73 ===
question73 = Question.objects.create(
    question_text="Name the road Beatty Park housing estate is situated on in Celbridge?",
    question_type=Question.SINGLE
)
category_names73 = ["Celbridge", "Housing Estates", "Main Roads"]
for name in category_names73:
    try:
        cat = Category.objects.get(name=name)
        question73.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices73 = [
    {"text": "Maynooth Road", "label": "A", "is_correct": True},
    {"text": "Oldtown Rod", "label": "B", "is_correct": False},
    {"text": "Dublin Road", "label": "C", "is_correct": False},
    {"text": "Loughlinstown Road", "label": "D", "is_correct": False},
]
for choice in choices73:
    try:
        Choice.objects.create(
            question=question73,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q73] Failed to create choice {choice['label']}: {e}")


# === Question 74 ===
question74 = Question.objects.create(
    question_text="Wolstan Heaven housing estate can be located where in Celbridge?",
    question_type=Question.SINGLE
)
category_names74 = ["Celbridge", "Housing Estates", "Main Roads"]
for name in category_names74:
    try:
        cat = Category.objects.get(name=name)
        question74.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices74 = [
    {"text": "Shakleton Road", "label": "A", "is_correct": False},
    {"text": "Oldtown Road", "label": "B", "is_correct": False},
    {"text": "Newtown Road", "label": "C", "is_correct": False},
    {"text": "Maynooth Road", "label": "D", "is_correct": True},
]
for choice in choices74:
    try:
        Choice.objects.create(
            question=question74,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q74] Failed to create choice {choice['label']}: {e}")


# === Question 75 ===
question75 = Question.objects.create(
    question_text="Which of these streets leads into Newtown Court housing estate in Maynooth?",
    question_type=Question.SINGLE
)
category_names75 = ["Maynooth", "Housing Estates", "Main Roads"]
for name in category_names75:
    try:
        cat = Category.objects.get(name=name)
        question75.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices75 = [
    {"text": "Meadowbrook", "label": "A", "is_correct": False},
    {"text": "Ballygoran Road", "label": "B", "is_correct": False},
    {"text": "Kilcock Road", "label": "C", "is_correct": False},
    {"text": "Newtown Road", "label": "D", "is_correct": True},
]
for choice in choices75:
    try:
        Choice.objects.create(
            question=question75,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q75] Failed to create choice {choice['label']}: {e}")


# === Question 76 ===
question76 = Question.objects.create(
    question_text="Where can you find Maynooth Park housing estate in Maynooth?",
    question_type=Question.SINGLE
)
category_names76 = ["Maynooth", "Housing Estates", "Main Roads"]
for name in category_names76:
    try:
        cat = Category.objects.get(name=name)
        question76.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices76 = [
    {"text": "Kilcock Road", "label": "A", "is_correct": True},
    {"text": "Straffan Road", "label": "B", "is_correct": False},
    {"text": "Newtown Road", "label": "C", "is_correct": False},
    {"text": "Moyglare Road", "label": "D", "is_correct": False},
]
for choice in choices76:
    try:
        Choice.objects.create(
            question=question76,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q76] Failed to create choice {choice['label']}: {e}")


# === Question 77 ===
question77 = Question.objects.create(
    question_text="What road leads into Sundays Well housing estate located in Naas?",
    question_type=Question.SINGLE
)
category_names77 = ["Naas", "Housing Estates", "Main Roads"]
for name in category_names77:
    try:
        cat = Category.objects.get(name=name)
        question77.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices77 = [
    {"text": "Kilcullen Road", "label": "A", "is_correct": False},
    {"text": "Tipper Road", "label": "B", "is_correct": False},
    {"text": "Ballycane Road", "label": "C", "is_correct": False},
    {"text": "Blessington Road", "label": "D", "is_correct": True},
]
for choice in choices77:
    try:
        Choice.objects.create(
            question=question77,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q77] Failed to create choice {choice['label']}: {e}")


# === Question 78 ===
question78 = Question.objects.create(
    question_text="Off which road is Lakelands housing estate located in Naas?",
    question_type=Question.SINGLE
)
category_names78 = ["Naas", "Housing Estates", "Main Roads"]
for name in category_names78:
    try:
        cat = Category.objects.get(name=name)
        question78.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices78 = [
    {"text": "Craddockstown Road", "label": "A", "is_correct": False},
    {"text": "New Caragh Road", "label": "B", "is_correct": False},
    {"text": "Monread Road", "label": "C", "is_correct": False},
    {"text": "Newbridge Road", "label": "D", "is_correct": True},
]
for choice in choices78:
    try:
        Choice.objects.create(
            question=question78,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q78] Failed to create choice {choice['label']}: {e}")


# === Question 79 ===
question79 = Question.objects.create(
    question_text="What street is Lakeside Park housing estate situated on in Naas?",
    question_type=Question.SINGLE
)
category_names79 = ["Naas", "Housing Estates", "Main Roads"]
for name in category_names79:
    try:
        cat = Category.objects.get(name=name)
        question79.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices79 = [
    {"text": "Barberstown Road", "label": "A", "is_correct": False},
    {"text": "Straffan Road", "label": "B", "is_correct": False},
    {"text": "Ballycane Road", "label": "C", "is_correct": False},
    {"text": "Ballymore Road", "label": "D", "is_correct": True},
]
for choice in choices79:
    try:
        Choice.objects.create(
            question=question79,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q79] Failed to create choice {choice['label']}: {e}")


# === Question 80 ===
question80 = Question.objects.create(
    question_text="The Rathasker Heights housing estate can be found on which road in Naas?",
    question_type=Question.SINGLE
)
category_names80 = ["Naas", "Housing Estates", "Main Roads"]
for name in category_names80:
    try:
        cat = Category.objects.get(name=name)
        question80.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices80 = [
    {"text": "Kilcullen Road", "label": "A", "is_correct": False},
    {"text": "Monread Road", "label": "B", "is_correct": False},
    {"text": "Sallins Road", "label": "C", "is_correct": False},
    {"text": "New Caragh Road", "label": "D", "is_correct": True},
]
for choice in choices80:
    try:
        Choice.objects.create(
            question=question80,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q80] Failed to create choice {choice['label']}: {e}")


# === Question 81 ===
question81 = Question.objects.create(
    question_text="The Ardconagh housing estate is located where in Naas?",
    question_type=Question.SINGLE
)
category_names81 = ["Naas", "Housing Estates", "Main Roads"]
for name in category_names81:
    try:
        cat = Category.objects.get(name=name)
        question81.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices81 = [
    {"text": "John Devoy Road", "label": "A", "is_correct": True},
    {"text": "Rathasker Rd", "label": "B", "is_correct": False},
    {"text": "New Caragh Rd", "label": "C", "is_correct": False},
    {"text": "Newbridge Road", "label": "D", "is_correct": False},
]
for choice in choices81:
    try:
        Choice.objects.create(
            question=question81,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q81] Failed to create choice {choice['label']}: {e}")


# === Question 82 ===
question82 = Question.objects.create(
    question_text="Name the street where Langton Park housing estate is found in Newbridge?",
    question_type=Question.SINGLE
)
category_names82 = ["Newbridge", "Housing Estates", "Main Roads"]
for name in category_names82:
    try:
        cat = Category.objects.get(name=name)
        question82.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices82 = [
    {"text": "Green Road", "label": "A", "is_correct": True},
    {"text": "Ballymany", "label": "B", "is_correct": False},
    {"text": "Curragh Grange", "label": "C", "is_correct": False},
    {"text": "Athgarvan Rd", "label": "D", "is_correct": False},
]
for choice in choices82:
    try:
        Choice.objects.create(
            question=question82,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q82] Failed to create choice {choice['label']}: {e}")


# === Question 83 ===
question83 = Question.objects.create(
    question_text="Which road houses the Oaks housing estate in Newbridge?",
    question_type=Question.SINGLE
)
category_names83 = ["Newbridge", "Housing Estates", "Main Roads"]
for name in category_names83:
    try:
        cat = Category.objects.get(name=name)
        question83.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices83 = [
    {"text": "Langton Road", "label": "A", "is_correct": False},
    {"text": "Liffey Terrace", "label": "B", "is_correct": False},
    {"text": "Standhouse Rd", "label": "C", "is_correct": True},
    {"text": "Artillery PI", "label": "D", "is_correct": False},
]
for choice in choices83:
    try:
        Choice.objects.create(
            question=question83,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q83] Failed to create choice {choice['label']}: {e}")


# === Question 84 ===
question84 = Question.objects.create(
    question_text="Where is The Seven Springs housing estate situated in Newbridge?",
    question_type=Question.SINGLE
)
category_names84 = ["Newbridge", "Housing Estates", "Main Roads"]
for name in category_names84:
    try:
        cat = Category.objects.get(name=name)
        question84.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices84 = [
    {"text": "Morristown Rd", "label": "A", "is_correct": False},
    {"text": "Green Rd", "label": "B", "is_correct": False},
    {"text": "Standhouse Road", "label": "C", "is_correct": True},
    {"text": "Langton Rd", "label": "D", "is_correct": False},
]
for choice in choices84:
    try:
        Choice.objects.create(
            question=question84,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q84] Failed to create choice {choice['label']}: {e}")


# === Question 85 ===
question85 = Question.objects.create(
    question_text="Lakeside Park housing estate is found where in Newbridge?",
    question_type=Question.SINGLE
)
category_names85 = ["Newbridge", "Housing Estates", "Main Roads"]
for name in category_names85:
    try:
        cat = Category.objects.get(name=name)
        question85.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices85 = [
    {"text": "Station Rd", "label": "A", "is_correct": True},
    {"text": "Blackberry Lane", "label": "B", "is_correct": False},
    {"text": "Moorefield Dr", "label": "C", "is_correct": False},
    {"text": "Morristown Road", "label": "D", "is_correct": False},
]
for choice in choices85:
    try:
        Choice.objects.create(
            question=question85,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q85] Failed to create choice {choice['label']}: {e}")


# === Question 86 ===
question86 = Question.objects.create(
    question_text="Where is Foodshala Indian Restaurant found in Naas?",
    question_type=Question.SINGLE
)
category_names86 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names86:
    try:
        cat = Category.objects.get(name=name)
        question86.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices86 = [
    {"text": "North Main Street", "label": "A", "is_correct": True},
    {"text": "Abbey Street", "label": "B", "is_correct": False},
    {"text": "South Main Street", "label": "C", "is_correct": False},
    {"text": "Sallins Road", "label": "D", "is_correct": False},
]
for choice in choices86:
    try:
        Choice.objects.create(
            question=question86,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q86] Failed to create choice {choice['label']}: {e}")


# === Question 87 ===
question87 = Question.objects.create(
    question_text="Name the road that houses Plur Wood Fire Pizza Restaurant in Naas?",
    question_type=Question.SINGLE
)
category_names87 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names87:
    try:
        cat = Category.objects.get(name=name)
        question87.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices87 = [
    {"text": "Sallins Road", "label": "A", "is_correct": True},
    {"text": "Friary Road", "label": "B", "is_correct": False},
    {"text": "Church Road", "label": "C", "is_correct": False},
    {"text": "Tipper Road", "label": "D", "is_correct": False},
]
for choice in choices87:
    try:
        Choice.objects.create(
            question=question87,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q87] Failed to create choice {choice['label']}: {e}")


# === Question 88 ===
question88 = Question.objects.create(
    question_text="Where can one find the BANG Restaurant in Naas?",
    question_type=Question.SINGLE
)
category_names88 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names88:
    try:
        cat = Category.objects.get(name=name)
        question88.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices88 = [
    {"text": "Merrion Row", "label": "A", "is_correct": True},
    {"text": "Fairgreen Street", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": False},
    {"text": "Church Lane", "label": "D", "is_correct": False},
]
for choice in choices88:
    try:
        Choice.objects.create(
            question=question88,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q88] Failed to create choice {choice['label']}: {e}")


# === Question 89 ===
question89 = Question.objects.create(
    question_text="The Monread is found on what road?",
    question_type=Question.SINGLE
)
category_names89 = ["Naas", "Pubs and Bars", "Main Roads"]
for name in category_names89:
    try:
        cat = Category.objects.get(name=name)
        question89.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices89 = [
    {"text": "Main Street", "label": "A", "is_correct": False},
    {"text": "Monread Avenue", "label": "B", "is_correct": True},
    {"text": "Monread Crescent", "label": "C", "is_correct": False},
    {"text": "Monread Heights", "label": "D", "is_correct": False},
]
for choice in choices89:
    try:
        Choice.objects.create(
            question=question89,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q89] Failed to create choice {choice['label']}: {e}")


# === Question 90 ===
question90 = Question.objects.create(
    question_text="The Tiger can be found on which of these roads in Clane?",
    question_type=Question.SINGLE
)
category_names90 = ["Clane", "Pubs and Bars", "Main Roads"]
for name in category_names90:
    try:
        cat = Category.objects.get(name=name)
        question90.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices90 = [
    {"text": "Millicent Road", "label": "A", "is_correct": False},
    {"text": "Central Park", "label": "B", "is_correct": False},
    {"text": "Ballinagappa Road", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": True},
]
for choice in choices90:
    try:
        Choice.objects.create(
            question=question90,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q90] Failed to create choice {choice['label']}: {e}")


# === Question 91 ===
question91 = Question.objects.create(
    question_text="what road is the Fate Restaurant housed on in Naas?",
    question_type=Question.SINGLE
)
category_names91 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names91:
    try:
        cat = Category.objects.get(name=name)
        question91.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices91 = [
    {"text": "Railway Terrace", "label": "A", "is_correct": False},
    {"text": "Friary Road", "label": "B", "is_correct": False},
    {"text": "Sallins Road", "label": "C", "is_correct": True},
    {"text": "John's Lane", "label": "D", "is_correct": False},
]
for choice in choices91:
    try:
        Choice.objects.create(
            question=question91,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q91] Failed to create choice {choice['label']}: {e}")


# === Question 92 ===
question92 = Question.objects.create(
    question_text="Eddie Rocket's is located where in Naas?",
    question_type=Question.SINGLE
)
category_names92 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names92:
    try:
        cat = Category.objects.get(name=name)
        question92.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices92 = [
    {"text": "Basin Street", "label": "A", "is_correct": False},
    {"text": "Abbey Road", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Blessington Road", "label": "D", "is_correct": False},
]
for choice in choices92:
    try:
        Choice.objects.create(
            question=question92,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q92] Failed to create choice {choice['label']}: {e}")


# === Question 93 ===
question93 = Question.objects.create(
    question_text="Where can you find The Harvest Kitchen in Naas?",
    question_type=Question.SINGLE
)
category_names93 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names93:
    try:
        cat = Category.objects.get(name=name)
        question93.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices93 = [
    {"text": "Patrician Avenue", "label": "A", "is_correct": False},
    {"text": "Sallins Road", "label": "B", "is_correct": False},
    {"text": "Craddockstown Road", "label": "C", "is_correct": False},
    {"text": "Millbridge Way", "label": "D", "is_correct": True},
]
for choice in choices93:
    try:
        Choice.objects.create(
            question=question93,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q93] Failed to create choice {choice['label']}: {e}")


# === Question 94 ===
question94 = Question.objects.create(
    question_text="Which street is Butt Mullins found on in Naas?",
    question_type=Question.SINGLE
)
category_names94 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names94:
    try:
        cat = Category.objects.get(name=name)
        question94.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices94 = [
    {"text": "Blessington Road", "label": "A", "is_correct": True},
    {"text": "Sallins Road", "label": "B", "is_correct": False},
    {"text": "Tipper Road", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": False},
]
for choice in choices94:
    try:
        Choice.objects.create(
            question=question94,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q94] Failed to create choice {choice['label']}: {e}")


# === Question 95 ===
question95 = Question.objects.create(
    question_text="Which of these roads can you find Vie De Chateaux on in Naas?",
    question_type=Question.SINGLE
)
category_names95 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names95:
    try:
        cat = Category.objects.get(name=name)
        question95.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices95 = [
    {"text": "Caragh Road", "label": "A", "is_correct": True},
    {"text": "Canal Bank", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": False},
    {"text": "Harbour View", "label": "D", "is_correct": False},
]
for choice in choices95:
    try:
        Choice.objects.create(
            question=question95,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q95] Failed to create choice {choice['label']}: {e}")


# === Question 96 ===
question96 = Question.objects.create(
    question_text="Name the street that houses Lemongrass Fusion in Naas.",
    question_type=Question.SINGLE
)
category_names96 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names96:
    try:
        cat = Category.objects.get(name=name)
        question96.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices96 = [
    {"text": "Blessington Road", "label": "A", "is_correct": False},
    {"text": "Abbey Street", "label": "B", "is_correct": True},
    {"text": "Ballycane Road", "label": "C", "is_correct": False},
    {"text": "Sallins Road", "label": "D", "is_correct": False},
]
for choice in choices96:
    try:
        Choice.objects.create(
            question=question96,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q96] Failed to create choice {choice['label']}: {e}")


# === Question 97 ===
question97 = Question.objects.create(
    question_text="Where is the Bouchon located in Naas?",
    question_type=Question.SINGLE
)
category_names97 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names97:
    try:
        cat = Category.objects.get(name=name)
        question97.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices97 = [
    {"text": "St.Martin's Avenue", "label": "A", "is_correct": False},
    {"text": "Corban's Lane", "label": "B", "is_correct": False},
    {"text": "South Main Street", "label": "C", "is_correct": True},
    {"text": "Tipper Road", "label": "D", "is_correct": False},
]
for choice in choices97:
    try:
        Choice.objects.create(
            question=question97,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q97] Failed to create choice {choice['label']}: {e}")


# === Question 98 ===
question98 = Question.objects.create(
    question_text="Les Olives Farm and Food is housed where in Naas?",
    question_type=Question.SINGLE
)
category_names98 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names98:
    try:
        cat = Category.objects.get(name=name)
        question98.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices98 = [
    {"text": "Abbey Street", "label": "A", "is_correct": False},
    {"text": "Millbrook Court", "label": "B", "is_correct": False},
    {"text": "Friary Road", "label": "C", "is_correct": True},
    {"text": "Sarto Road", "label": "D", "is_correct": False},
]
for choice in choices98:
    try:
        Choice.objects.create(
            question=question98,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q98] Failed to create choice {choice['label']}: {e}")


# === Question 99 ===
question99 = Question.objects.create(
    question_text="Name the street that Herald and Devoy Restaurant can be found on in Naas?",
    question_type=Question.SINGLE
)
category_names99 = ["Naas", "Restaurants", "Main Roads"]
for name in category_names99:
    try:
        cat = Category.objects.get(name=name)
        question99.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices99 = [
    {"text": "Caragh Road", "label": "A", "is_correct": False},
    {"text": "Devoy Quarter", "label": "B", "is_correct": True},
    {"text": "Ballymore Road", "label": "C", "is_correct": False},
    {"text": "John Devoy Road", "label": "D", "is_correct": False},
]
for choice in choices99:
    try:
        Choice.objects.create(
            question=question99,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q99] Failed to create choice {choice['label']}: {e}")


# === Question 100 ===
question100 = Question.objects.create(
    question_text="What road is the Town Restaurant housed on in Leixlip?",
    question_type=Question.SINGLE
)
category_names100 = ["Leixlip", "Restaurants", "Main Roads"]
for name in category_names100:
    try:
        cat = Category.objects.get(name=name)
        question100.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices100 = [
    {"text": "Green Lane", "label": "A", "is_correct": False},
    {"text": "Riverdale", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Station Road", "label": "D", "is_correct": False},
]
for choice in choices100:
    try:
        Choice.objects.create(
            question=question100,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q100] Failed to create choice {choice['label']}: {e}")


# === Question 101 ===
question101 = Question.objects.create(
    question_text="Where can one find Da Vinci's Restaurant in Leixlip?",
    question_type=Question.SINGLE
)
category_names101 = ["Leixlip", "Restaurants", "Main Roads"]
for name in category_names101:
    try:
        cat = Category.objects.get(name=name)
        question101.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices101 = [
    {"text": "Main Street", "label": "A", "is_correct": True},
    {"text": "Green Lane", "label": "B", "is_correct": False},
    {"text": "Captain's Hill", "label": "C", "is_correct": False},
    {"text": "Station Road", "label": "D", "is_correct": False},
]
for choice in choices101:
    try:
        Choice.objects.create(
            question=question101,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q101] Failed to create choice {choice['label']}: {e}")


# === Question 102 ===
question102 = Question.objects.create(
    question_text="Edward Harrigan & Sons is located where in Newbridge?",
    question_type=Question.SINGLE
)
category_names102 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names102:
    try:
        cat = Category.objects.get(name=name)
        question102.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices102 = [
    {"text": "The Priory", "label": "A", "is_correct": False},
    {"text": "Canning Place", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "The Grange", "label": "D", "is_correct": False},
]
for choice in choices102:
    try:
        Choice.objects.create(
            question=question102,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q102] Failed to create choice {choice['label']}: {e}")


# === Question 103 ===
question103 = Question.objects.create(
    question_text="Where can you find the Panda Inn in Newbridge?",
    question_type=Question.SINGLE
)
category_names103 = ["Newbridge", "Restaurants", "Main Roads"]
for name in category_names103:
    try:
        cat = Category.objects.get(name=name)
        question103.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices103 = [
    {"text": "Old Connell", "label": "A", "is_correct": False},
    {"text": "Eyre Street", "label": "B", "is_correct": True},
    {"text": "Rowan Terrace", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": False},
]
for choice in choices103:
    try:
        Choice.objects.create(
            question=question103,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q103] Failed to create choice {choice['label']}: {e}")


# === Question 104 ===
question104 = Question.objects.create(
    question_text="Where is the Charcoal Grill found in Newbridge?",
    question_type=Question.SINGLE
)
category_names104 = ["Newbridge", "Restaurants", "Main Roads"]
for name in category_names104:
    try:
        cat = Category.objects.get(name=name)
        question104.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices104 = [
    {"text": "Station Road", "label": "A", "is_correct": False},
    {"text": "James Lane", "label": "B", "is_correct": False},
    {"text": "Limerick Lane", "label": "C", "is_correct": True},
    {"text": "College Park Road", "label": "D", "is_correct": False},
]
for choice in choices104:
    try:
        Choice.objects.create(
            question=question104,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q104] Failed to create choice {choice['label']}: {e}")


# === Question 105 ===
question105 = Question.objects.create(
    question_text="Choose the road that Market Kitchen is located on in Newbridge?",
    question_type=Question.SINGLE
)
category_names105 = ["Newbridge", "Restaurants", "Main Roads"]
for name in category_names105:
    try:
        cat = Category.objects.get(name=name)
        question105.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices105 = [
    {"text": "Cutlery Road", "label": "A", "is_correct": False},
    {"text": "Limerick Lane", "label": "B", "is_correct": False},
    {"text": "Dawson Street", "label": "C", "is_correct": False},
    {"text": "Edward Street", "label": "D", "is_correct": True},
]
for choice in choices105:
    try:
        Choice.objects.create(
            question=question105,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q105] Failed to create choice {choice['label']}: {e}")


# === Question 106 ===
question106 = Question.objects.create(
    question_text="Where is The Palace Restaurant located in Newbridge?",
    question_type=Question.SINGLE
)
category_names106 = ["Newbridge", "Restaurants", "Main Roads"]
for name in category_names106:
    try:
        cat = Category.objects.get(name=name)
        question106.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices106 = [
    {"text": "Henry Road", "label": "A", "is_correct": False},
    {"text": "Ryston Avenue", "label": "B", "is_correct": False},
    {"text": "Moorefield Road", "label": "C", "is_correct": False},
    {"text": "Edward Street", "label": "D", "is_correct": True},
]
for choice in choices106:
    try:
        Choice.objects.create(
            question=question106,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q106] Failed to create choice {choice['label']}: {e}")


# === Question 107 ===
question107 = Question.objects.create(
    question_text="What street houses Picaderos in Maynooth?",
    question_type=Question.SINGLE
)
category_names107 = ["Maynooth", "Restaurants", "Main Roads"]
for name in category_names107:
    try:
        cat = Category.objects.get(name=name)
        question107.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices107 = [
    {"text": "Moyglare Road", "label": "A", "is_correct": False},
    {"text": "Straffan Road", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Parson Street", "label": "D", "is_correct": False},
]
for choice in choices107:
    try:
        Choice.objects.create(
            question=question107,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q107] Failed to create choice {choice['label']}: {e}")


# === Question 108 ===
question108 = Question.objects.create(
    question_text="Select the road that the Donatello's restaurant is situated on in Maynooth?",
    question_type=Question.SINGLE
)
category_names108 = ["Maynooth", "Restaurants", "Main Roads"]
for name in category_names108:
    try:
        cat = Category.objects.get(name=name)
        question108.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices108 = [
    {"text": "Doctor's Lane", "label": "A", "is_correct": False},
    {"text": "Main Street", "label": "B", "is_correct": True},
    {"text": "Leinster Park", "label": "C", "is_correct": False},
    {"text": "Straffan Road", "label": "D", "is_correct": False},
]
for choice in choices108:
    try:
        Choice.objects.create(
            question=question108,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q108] Failed to create choice {choice['label']}: {e}")


# === Question 109 ===
question109 = Question.objects.create(
    question_text="Bistro 53 is housed on what road in Maynooth?",
    question_type=Question.SINGLE
)
category_names109 = ["Maynooth", "Restaurants", "Main Roads"]
for name in category_names109:
    try:
        cat = Category.objects.get(name=name)
        question109.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices109 = [
    {"text": "Dunboyne Road", "label": "A", "is_correct": False},
    {"text": "Moyglare Road", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Lyreen Lodge", "label": "D", "is_correct": False},
]
for choice in choices109:
    try:
        Choice.objects.create(
            question=question109,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q109] Failed to create choice {choice['label']}: {e}")


# === Question 110 ===
question110 = Question.objects.create(
    question_text="Royal City Restaurant can be found where in Maynooth?",
    question_type=Question.SINGLE
)
category_names110 = ["Maynooth", "Restaurants", "Main Roads"]
for name in category_names110:
    try:
        cat = Category.objects.get(name=name)
        question110.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices110 = [
    {"text": "Mill Street", "label": "A", "is_correct": True},
    {"text": "Straffan Road", "label": "B", "is_correct": False},
    {"text": "Kilcock Road", "label": "C", "is_correct": False},
    {"text": "Pound Lane", "label": "D", "is_correct": False},
]
for choice in choices110:
    try:
        Choice.objects.create(
            question=question110,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q110] Failed to create choice {choice['label']}: {e}")


# === Question 111 ===
question111 = Question.objects.create(
    question_text="Which of these streets is Stone Heaven Restaurant located on in Maynooth?",
    question_type=Question.SINGLE
)
category_names111 = ["Maynooth", "Restaurants", "Main Roads"]
for name in category_names111:
    try:
        cat = Category.objects.get(name=name)
        question111.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices111 = [
    {"text": "Parson Street", "label": "A", "is_correct": True},
    {"text": "Limetree Hall", "label": "B", "is_correct": False},
    {"text": "Dunboyne Road", "label": "C", "is_correct": False},
    {"text": "Mill Street", "label": "D", "is_correct": False},
]
for choice in choices111:
    try:
        Choice.objects.create(
            question=question111,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q111] Failed to create choice {choice['label']}: {e}")


# === Question 112 ===
question112 = Question.objects.create(
    question_text="What road houses the Hartes of Kildare?",
    question_type=Question.SINGLE
)
category_names112 = ["Kildare (Town)", "Pubs and Bars", "Main Roads"]
for name in category_names112:
    try:
        cat = Category.objects.get(name=name)
        question112.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices112 = [
    {"text": "Cleamore Road", "label": "A", "is_correct": False},
    {"text": "Market Square", "label": "B", "is_correct": True},
    {"text": "Green Road", "label": "C", "is_correct": False},
    {"text": "Old Road", "label": "D", "is_correct": False},
]
for choice in choices112:
    try:
        Choice.objects.create(
            question=question112,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q112] Failed to create choice {choice['label']}: {e}")


# === Question 113 ===
question113 = Question.objects.create(
    question_text="Where can one find Chapter 16 in Kildare?",
    question_type=Question.SINGLE
)
category_names113 = ["Kildare (Town)", "Restaurants", "Main Roads"]
for name in category_names113:
    try:
        cat = Category.objects.get(name=name)
        question113.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices113 = [
    {"text": "Pigeon Lane", "label": "A", "is_correct": False},
    {"text": "Melitta Road", "label": "B", "is_correct": False},
    {"text": "Market Square", "label": "C", "is_correct": True},
    {"text": "White Abbey Road", "label": "D", "is_correct": False},
]
for choice in choices113:
    try:
        Choice.objects.create(
            question=question113,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q113] Failed to create choice {choice['label']}: {e}")


# === Question 114 ===
question114 = Question.objects.create(
    question_text="Ngai's Restaurant can be located where in Athy?",
    question_type=Question.SINGLE
)
category_names114 = ["Athy", "Restaurants", "Main Roads"]
for name in category_names114:
    try:
        cat = Category.objects.get(name=name)
        question114.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices114 = [
    {"text": "Woodstock Street", "label": "A", "is_correct": True},
    {"text": "Stanhope Place", "label": "B", "is_correct": False},
    {"text": "Rockfield Road", "label": "C", "is_correct": False},
    {"text": "Leinster Street", "label": "D", "is_correct": False},
]
for choice in choices114:
    try:
        Choice.objects.create(
            question=question114,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q114] Failed to create choice {choice['label']}: {e}")


# === Question 115 ===
question115 = Question.objects.create(
    question_text="Where can one find Mama Mia restaurant in Athy?",
    question_type=Question.SINGLE
)
category_names115 = ["Athy", "Restaurants", "Main Roads"]
for name in category_names115:
    try:
        cat = Category.objects.get(name=name)
        question115.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices115 = [
    {"text": "Church road", "label": "A", "is_correct": False},
    {"text": "Chapel Lane", "label": "B", "is_correct": False},
    {"text": "Leinster Street", "label": "C", "is_correct": True},
    {"text": "Mount Hawkins", "label": "D", "is_correct": False},
]
for choice in choices115:
    try:
        Choice.objects.create(
            question=question115,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q115] Failed to create choice {choice['label']}: {e}")


# === Question 116 ===
question116 = Question.objects.create(
    question_text="One New Row is found where in Naas?",
    question_type=Question.SINGLE
)
category_names116 = ["Naas", "Pubs and Bars", "Main Roads"]
for name in category_names116:
    try:
        cat = Category.objects.get(name=name)
        question116.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices116 = [
    {"text": "Main Street", "label": "A", "is_correct": False},
    {"text": "New Row", "label": "B", "is_correct": True},
    {"text": "Ballymore Road", "label": "C", "is_correct": False},
    {"text": "Corban's Lane", "label": "D", "is_correct": False},
]
for choice in choices116:
    try:
        Choice.objects.create(
            question=question116,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q116] Failed to create choice {choice['label']}: {e}")


# === Question 117 ===
question117 = Question.objects.create(
    question_text="Where is The Town Leixlip located?",
    question_type=Question.SINGLE
)
category_names117 = ["Leixlip", "Pubs and Bars", "Main Roads"]
for name in category_names117:
    try:
        cat = Category.objects.get(name=name)
        question117.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices117 = [
    {"text": "Captain's Hill", "label": "A", "is_correct": False},
    {"text": "Main Street", "label": "B", "is_correct": True},
    {"text": "Mill Lane", "label": "C", "is_correct": False},
    {"text": "Castle Park", "label": "D", "is_correct": False},
]
for choice in choices117:
    try:
        Choice.objects.create(
            question=question117,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q117] Failed to create choice {choice['label']}: {e}")


# === Question 118 ===
question118 = Question.objects.create(
    question_text="The Middle Shop can be found where in Leixlip?",
    question_type=Question.SINGLE
)
category_names118 = ["Leixlip", "Pubs and Bars", "Main Roads"]
for name in category_names118:
    try:
        cat = Category.objects.get(name=name)
        question118.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices118 = [
    {"text": "Station Road", "label": "A", "is_correct": False},
    {"text": "Main Street", "label": "B", "is_correct": True},
    {"text": "Rye River Mall", "label": "C", "is_correct": False},
    {"text": "Old Hill", "label": "D", "is_correct": False},
]
for choice in choices118:
    try:
        Choice.objects.create(
            question=question118,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q118] Failed to create choice {choice['label']}: {e}")


# === Question 119 ===
question119 = Question.objects.create(
    question_text="Where is McGowans & Apollo Nighclub found in Newbridge?",
    question_type=Question.SINGLE
)
category_names119 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names119:
    try:
        cat = Category.objects.get(name=name)
        question119.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices119 = [
    {"text": "Main Street", "label": "A", "is_correct": True},
    {"text": "Liffey Terrace", "label": "B", "is_correct": False},
    {"text": "Ryston Avenue", "label": "C", "is_correct": False},
    {"text": "Athgarvan Road", "label": "D", "is_correct": False},
]
for choice in choices119:
    try:
        Choice.objects.create(
            question=question119,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q119] Failed to create choice {choice['label']}: {e}")


# === Question 120 ===
question120 = Question.objects.create(
    question_text="Where is The Railway Bar located in Newbridge?",
    question_type=Question.SINGLE
)
category_names120 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names120:
    try:
        cat = Category.objects.get(name=name)
        question120.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices120 = [
    {"text": "Eyre Street", "label": "A", "is_correct": False},
    {"text": "Station Road", "label": "B", "is_correct": True},
    {"text": "Main Street", "label": "C", "is_correct": False},
    {"text": "Edward Street", "label": "D", "is_correct": False},
]
for choice in choices120:
    try:
        Choice.objects.create(
            question=question120,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q120] Failed to create choice {choice['label']}: {e}")


# === Question 121 ===
question121 = Question.objects.create(
    question_text="Where is the Edward Harrigan and Sons found in Newbridge?",
    question_type=Question.SINGLE
)
category_names121 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names121:
    try:
        cat = Category.objects.get(name=name)
        question121.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices121 = [
    {"text": "Athgarvan Road", "label": "A", "is_correct": False},
    {"text": "Station Road", "label": "B", "is_correct": False},
    {"text": "Green Road", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": True},
]
for choice in choices121:
    try:
        Choice.objects.create(
            question=question121,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q121] Failed to create choice {choice['label']}: {e}")


# === Question 122 ===
question122 = Question.objects.create(
    question_text="Where is the Coffeys located in Newbridge?",
    question_type=Question.SINGLE
)
category_names122 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names122:
    try:
        cat = Category.objects.get(name=name)
        question122.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices122 = [
    {"text": "Chapel Lane", "label": "A", "is_correct": False},
    {"text": "College Park Road", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Eyre Street", "label": "D", "is_correct": False},
]
for choice in choices122:
    try:
        Choice.objects.create(
            question=question122,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q122] Failed to create choice {choice['label']}: {e}")


# === Question 123 ===
question123 = Question.objects.create(
    question_text="The Curragh Inn is located where in Newbridge?",
    question_type=Question.SINGLE
)
category_names123 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names123:
    try:
        cat = Category.objects.get(name=name)
        question123.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices123 = [
    {"text": "Liffey View", "label": "A", "is_correct": False},
    {"text": "The Lane", "label": "B", "is_correct": False},
    {"text": "Edward Street", "label": "C", "is_correct": True},
    {"text": "Pairc Mhuire", "label": "D", "is_correct": False},
]
for choice in choices123:
    try:
        Choice.objects.create(
            question=question123,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q123] Failed to create choice {choice['label']}: {e}")


# === Question 124 ===
question124 = Question.objects.create(
    question_text="The Judge Beans is located where in Newbridge?",
    question_type=Question.SINGLE
)
category_names124 = ["Newbridge", "Pubs and Bars", "Main Roads"]
for name in category_names124:
    try:
        cat = Category.objects.get(name=name)
        question124.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices124 = [
    {"text": "Edward Street", "label": "A", "is_correct": True},
    {"text": "Athgarvan Road", "label": "B", "is_correct": False},
    {"text": "Station Road", "label": "C", "is_correct": False},
    {"text": "Piercetown", "label": "D", "is_correct": False},
]
for choice in choices124:
    try:
        Choice.objects.create(
            question=question124,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q124] Failed to create choice {choice['label']}: {e}")


# === Question 125 ===
question125 = Question.objects.create(
    question_text="Pick the road that houses Oak Alley Cocktail Bar in Maynooth?",
    question_type=Question.SINGLE
)
category_names125 = ["Maynooth", "Pubs and Bars", "Main Roads"]
for name in category_names125:
    try:
        cat = Category.objects.get(name=name)
        question125.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices125 = [
    {"text": "Parson Street", "label": "A", "is_correct": False},
    {"text": "Lyreen Avenue", "label": "B", "is_correct": False},
    {"text": "Carton Square", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": True},
]
for choice in choices125:
    try:
        Choice.objects.create(
            question=question125,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q125] Failed to create choice {choice['label']}: {e}")


# === Question 126 ===
question126 = Question.objects.create(
    question_text="Brady's Clockhouse is housed on what road in Maynooth?",
    question_type=Question.SINGLE
)
category_names126 = ["Maynooth", "Pubs and Bars", "Main Roads"]
for name in category_names126:
    try:
        cat = Category.objects.get(name=name)
        question126.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices126 = [
    {"text": "Main Street", "label": "A", "is_correct": True},
    {"text": "Kilcock Road", "label": "B", "is_correct": False},
    {"text": "Newtown Road", "label": "C", "is_correct": False},
    {"text": "Leinster Road", "label": "D", "is_correct": False},
]
for choice in choices126:
    try:
        Choice.objects.create(
            question=question126,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q126] Failed to create choice {choice['label']}: {e}")


# === Question 127 ===
question127 = Question.objects.create(
    question_text="McMahon's Bar & Lounge is found on what road in Maynooth?",
    question_type=Question.SINGLE
)
category_names127 = ["Maynooth", "Pubs and Bars", "Main Roads"]
for name in category_names127:
    try:
        cat = Category.objects.get(name=name)
        question127.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices127 = [
    {"text": "Dunboyne Road", "label": "A", "is_correct": False},
    {"text": "Parson Street", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Moyglare Road", "label": "D", "is_correct": False},
]
for choice in choices127:
    try:
        Choice.objects.create(
            question=question127,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q127] Failed to create choice {choice['label']}: {e}")


# === Question 128 ===
question128 = Question.objects.create(
    question_text="Where is Newtown Inn and Sports Bar found in Maynooth?",
    question_type=Question.SINGLE
)
category_names128 = ["Maynooth", "Pubs and Bars", "Main Roads"]
for name in category_names128:
    try:
        cat = Category.objects.get(name=name)
        question128.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices128 = [
    {"text": "Newtown Road", "label": "A", "is_correct": True},
    {"text": "Meadowbrook Road", "label": "B", "is_correct": False},
    {"text": "Kingsbry", "label": "C", "is_correct": False},
    {"text": "Straffan Road", "label": "D", "is_correct": False},
]
for choice in choices128:
    try:
        Choice.objects.create(
            question=question128,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q128] Failed to create choice {choice['label']}: {e}")


# === Question 129 ===
question129 = Question.objects.create(
    question_text="What road houses The Roost in Maynooth?",
    question_type=Question.SINGLE
)
category_names129 = ["Maynooth", "Pubs and Bars", "Main Roads"]
for name in category_names129:
    try:
        cat = Category.objects.get(name=name)
        question129.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices129 = [
    {"text": "Moyglare Street", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": False},
    {"text": "Carton Grove", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": True},
]
for choice in choices129:
    try:
        Choice.objects.create(
            question=question129,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q129] Failed to create choice {choice['label']}: {e}")


# === Question 130 ===
question130 = Question.objects.create(
    question_text="Yolo Gastro Bar & Grill can be found where?",
    question_type=Question.SINGLE
)
category_names130 = ["Kildare (Town)", "Pubs and Bars", "Main Roads"]
for name in category_names130:
    try:
        cat = Category.objects.get(name=name)
        question130.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices130 = [
    {"text": "Lourdesville", "label": "A", "is_correct": False},
    {"text": "Station Road", "label": "B", "is_correct": True},
    {"text": "Monasterevin Road", "label": "C", "is_correct": False},
    {"text": "Dara Park", "label": "D", "is_correct": False},
]
for choice in choices130:
    try:
        Choice.objects.create(
            question=question130,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q130] Failed to create choice {choice['label']}: {e}")


# === Question 131 ===
question131 = Question.objects.create(
    question_text="MJ McEnerney is located on what road in Kildare?",
    question_type=Question.SINGLE
)
category_names131 = ["Kildare (Town)", "Pubs and Bars", "Main Roads"]
for name in category_names131:
    try:
        cat = Category.objects.get(name=name)
        question131.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices131 = [
    {"text": "White Abbey road", "label": "A", "is_correct": False},
    {"text": "Southgreen Road", "label": "B", "is_correct": False},
    {"text": "Cleamore Road", "label": "C", "is_correct": False},
    {"text": "Pigeon Lane", "label": "D", "is_correct": True},
]
for choice in choices131:
    try:
        Choice.objects.create(
            question=question131,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q131] Failed to create choice {choice['label']}: {e}")


# === Question 132 ===
question132 = Question.objects.create(
    question_text="The Five Jockeys is situated on what road in Kildare?",
    question_type=Question.SINGLE
)
category_names132 = ["Kildare (Town)", "Pubs and Bars", "Main Roads"]
for name in category_names132:
    try:
        cat = Category.objects.get(name=name)
        question132.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices132 = [
    {"text": "Dara Park", "label": "A", "is_correct": False},
    {"text": "Old Road", "label": "B", "is_correct": False},
    {"text": "Green Road", "label": "C", "is_correct": False},
    {"text": "Claregate Street", "label": "D", "is_correct": True},
]
for choice in choices132:
    try:
        Choice.objects.create(
            question=question132,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q132] Failed to create choice {choice['label']}: {e}")


# === Question 133 ===
question133 = Question.objects.create(
    question_text="Where can one find Top Nolan's in Kildare?",
    question_type=Question.SINGLE
)
category_names133 = ["Kildare (Town)", "Pubs and Bars", "Main Roads"]
for name in category_names133:
    try:
        cat = Category.objects.get(name=name)
        question133.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices133 = [
    {"text": "Melitta Road", "label": "A", "is_correct": False},
    {"text": "Priest's Lane", "label": "B", "is_correct": False},
    {"text": "Cleamore Road", "label": "C", "is_correct": False},
    {"text": "Market Square", "label": "D", "is_correct": True},
]
for choice in choices133:
    try:
        Choice.objects.create(
            question=question133,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q133] Failed to create choice {choice['label']}: {e}")


# === Question 134 ===
question134 = Question.objects.create(
    question_text="James Nolan's is located where in Kildare?",
    question_type=Question.SINGLE
)
category_names134 = ["Kildare (Town)", "Pubs and Bars", "Main Roads"]
for name in category_names134:
    try:
        cat = Category.objects.get(name=name)
        question134.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices134 = [
    {"text": "Meadow Road", "label": "A", "is_correct": False},
    {"text": "Dublin Street", "label": "B", "is_correct": True},
    {"text": "Bride Street", "label": "C", "is_correct": False},
    {"text": "Heffernan's Lane", "label": "D", "is_correct": False},
]
for choice in choices134:
    try:
        Choice.objects.create(
            question=question134,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q134] Failed to create choice {choice['label']}: {e}")


# === Question 135 ===
question135 = Question.objects.create(
    question_text="Clancy's is located on what road in Athy?",
    question_type=Question.SINGLE
)
category_names135 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names135:
    try:
        cat = Category.objects.get(name=name)
        question135.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices135 = [
    {"text": "Gallow Hill Court", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": True},
    {"text": "Leinster Street", "label": "C", "is_correct": False},
    {"text": "Woodstock Street", "label": "D", "is_correct": False},
]
for choice in choices135:
    try:
        Choice.objects.create(
            question=question135,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q135] Failed to create choice {choice['label']}: {e}")


# === Question 136 ===
question136 = Question.objects.create(
    question_text="The Auld Shebeen Bar is found where in Athy?",
    question_type=Question.SINGLE
)
category_names136 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names136:
    try:
        cat = Category.objects.get(name=name)
        question136.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices136 = [
    {"text": "Upper William Street", "label": "A", "is_correct": True},
    {"text": "Rockfield Road", "label": "B", "is_correct": False},
    {"text": "Ardrew Heights", "label": "C", "is_correct": False},
    {"text": "Bleach Road", "label": "D", "is_correct": False},
]
for choice in choices136:
    try:
        Choice.objects.create(
            question=question136,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q136] Failed to create choice {choice['label']}: {e}")


# === Question 137 ===
question137 = Question.objects.create(
    question_text="Anderson's Pub is located on what road in Athy?",
    question_type=Question.SINGLE
)
category_names137 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names137:
    try:
        cat = Category.objects.get(name=name)
        question137.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices137 = [
    {"text": "Emily Square", "label": "A", "is_correct": True},
    {"text": "Moneen Driive", "label": "B", "is_correct": False},
    {"text": "Church Road", "label": "C", "is_correct": False},
    {"text": "Green Alley", "label": "D", "is_correct": False},
]
for choice in choices137:
    try:
        Choice.objects.create(
            question=question137,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q137] Failed to create choice {choice['label']}: {e}")


# === Question 138 ===
question138 = Question.objects.create(
    question_text="Anns Place is situated on what road in Athy?",
    question_type=Question.SINGLE
)
category_names138 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names138:
    try:
        cat = Category.objects.get(name=name)
        question138.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices138 = [
    {"text": "Leinster Street", "label": "A", "is_correct": True},
    {"text": "Woodstock Street", "label": "B", "is_correct": False},
    {"text": "Kingsgrove", "label": "C", "is_correct": False},
    {"text": "Stanhope Place", "label": "D", "is_correct": False},
]
for choice in choices138:
    try:
        Choice.objects.create(
            question=question138,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q138] Failed to create choice {choice['label']}: {e}")


# === Question 139 ===
question139 = Question.objects.create(
    question_text="McEvoys can be found on what road in Athy?",
    question_type=Question.SINGLE
)
category_names139 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names139:
    try:
        cat = Category.objects.get(name=name)
        question139.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices139 = [
    {"text": "Emily Square", "label": "A", "is_correct": True},
    {"text": "Kirwan's Lane", "label": "B", "is_correct": False},
    {"text": "Leinster Street", "label": "C", "is_correct": False},
    {"text": "Geraldine Road", "label": "D", "is_correct": False},
]
for choice in choices139:
    try:
        Choice.objects.create(
            question=question139,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q139] Failed to create choice {choice['label']}: {e}")


# === Question 140 ===
question140 = Question.objects.create(
    question_text="The Duke in Athy can be found on what road?",
    question_type=Question.SINGLE
)
category_names140 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names140:
    try:
        cat = Category.objects.get(name=name)
        question140.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices140 = [
    {"text": "Duke Street", "label": "A", "is_correct": True},
    {"text": "Woodstock Street", "label": "B", "is_correct": False},
    {"text": "Rockfield Road", "label": "C", "is_correct": False},
    {"text": "Canal Side", "label": "D", "is_correct": False},
]
for choice in choices140:
    try:
        Choice.objects.create(
            question=question140,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q140] Failed to create choice {choice['label']}: {e}")


# === Question 141 ===
question141 = Question.objects.create(
    question_text="Paddy Dunne's Bar & Lounge is found where in Athy?",
    question_type=Question.SINGLE
)
category_names141 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names141:
    try:
        cat = Category.objects.get(name=name)
        question141.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices141 = [
    {"text": "Convent View", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": True},
    {"text": "Woodstock Street", "label": "C", "is_correct": False},
    {"text": "Bothai bui", "label": "D", "is_correct": False},
]
for choice in choices141:
    try:
        Choice.objects.create(
            question=question141,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q141] Failed to create choice {choice['label']}: {e}")


# === Question 142 ===
question142 = Question.objects.create(
    question_text="Where is W Doyle situated in Athy?",
    question_type=Question.SINGLE
)
category_names142 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names142:
    try:
        cat = Category.objects.get(name=name)
        question142.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices142 = [
    {"text": "Green Hills", "label": "A", "is_correct": False},
    {"text": "Stanhope Place", "label": "B", "is_correct": False},
    {"text": "Woodstock Street", "label": "C", "is_correct": True},
    {"text": "Mount Hawkins", "label": "D", "is_correct": False},
]
for choice in choices142:
    try:
        Choice.objects.create(
            question=question142,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q142] Failed to create choice {choice['label']}: {e}")


# === Question 143 ===
question143 = Question.objects.create(
    question_text="Where can the CI:Bar be found in Athy?",
    question_type=Question.SINGLE
)
category_names143 = ["Athy", "Pubs and Bars", "Main Roads"]
for name in category_names143:
    try:
        cat = Category.objects.get(name=name)
        question143.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices143 = [
    {"text": "Woodstock Street", "label": "A", "is_correct": False},
    {"text": "Leinster Street", "label": "B", "is_correct": True},
    {"text": "Main Street", "label": "C", "is_correct": False},
    {"text": "Meeting Lane", "label": "D", "is_correct": False},
]
for choice in choices143:
    try:
        Choice.objects.create(
            question=question143,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q143] Failed to create choice {choice['label']}: {e}")


# === Question 144 ===
question144 = Question.objects.create(
    question_text="Select the road that Leixlip Garda Station is situated on.",
    question_type=Question.SINGLE
)
category_names144 = ["Leixlip", "Garda Stations", "Main Roads"]
for name in category_names144:
    try:
        cat = Category.objects.get(name=name)
        question144.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices144 = [
    {"text": "Station Rd", "label": "A", "is_correct": False},
    {"text": "Celbridge Rd", "label": "B", "is_correct": False},
    {"text": "Green Ln", "label": "C", "is_correct": False},
    {"text": "Main St", "label": "D", "is_correct": True},
]
for choice in choices144:
    try:
        Choice.objects.create(
            question=question144,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q144] Failed to create choice {choice['label']}: {e}")


# === Question 145 ===
question145 = Question.objects.create(
    question_text="Name the road that Maynooth Garda Station can be found on:",
    question_type=Question.SINGLE
)
category_names145 = ["Maynooth", "Garda Stations", "Main Roads"]
for name in category_names145:
    try:
        cat = Category.objects.get(name=name)
        question145.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices145 = [
    {"text": "Leinster St", "label": "A", "is_correct": True},
    {"text": "Lyreen Ave", "label": "B", "is_correct": False},
    {"text": "Straffan Rd", "label": "C", "is_correct": False},
    {"text": "Dunboyne Rd", "label": "D", "is_correct": False},
]
for choice in choices145:
    try:
        Choice.objects.create(
            question=question145,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q145] Failed to create choice {choice['label']}: {e}")


# === Question 146 ===
question146 = Question.objects.create(
    question_text="Which of these roads houses Monasterevin Garda Station?",
    question_type=Question.SINGLE
)
category_names146 = ["Monasterevin", "Garda Stations", "Main Roads"]
for name in category_names146:
    try:
        cat = Category.objects.get(name=name)
        question146.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices146 = [
    {"text": "Abbeygate", "label": "A", "is_correct": False},
    {"text": "Drogheda Row", "label": "B", "is_correct": False},
    {"text": "L7055", "label": "C", "is_correct": False},
    {"text": "Dublin Rd", "label": "D", "is_correct": True},
]
for choice in choices146:
    try:
        Choice.objects.create(
            question=question146,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q146] Failed to create choice {choice['label']}: {e}")


# === Question 147 ===
question147 = Question.objects.create(
    question_text="What road is the Naas Garda Station found?",
    question_type=Question.SINGLE
)
category_names147 = ["Naas", "Garda Stations", "Main Roads"]
for name in category_names147:
    try:
        cat = Category.objects.get(name=name)
        question147.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices147 = [
    {"text": "Craddockstown Rd", "label": "A", "is_correct": False},
    {"text": "Ballymore Rd", "label": "B", "is_correct": False},
    {"text": "Rathasker Rd", "label": "C", "is_correct": False},
    {"text": "Kilcullen Rd", "label": "D", "is_correct": True},
]
for choice in choices147:
    try:
        Choice.objects.create(
            question=question147,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q147] Failed to create choice {choice['label']}: {e}")


# === Question 148 ===
question148 = Question.objects.create(
    question_text="Newbridge Garda Station can be found on which road?",
    question_type=Question.SINGLE
)
category_names148 = ["Newbridge", "Garda Stations", "Main Roads"]
for name in category_names148:
    try:
        cat = Category.objects.get(name=name)
        question148.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices148 = [
    {"text": "Liffey View", "label": "A", "is_correct": False},
    {"text": "Eyre St", "label": "B", "is_correct": False},
    {"text": "Main St", "label": "C", "is_correct": True},
    {"text": "Collge Park Rd", "label": "D", "is_correct": False},
]
for choice in choices148:
    try:
        Choice.objects.create(
            question=question148,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q148] Failed to create choice {choice['label']}: {e}")


# === Question 149 ===
question149 = Question.objects.create(
    question_text="Where is the Rathangan Garda Station situated?",
    question_type=Question.SINGLE
)
category_names149 = ["Rathangan", "Garda Stations", "Main Roads"]
for name in category_names149:
    try:
        cat = Category.objects.get(name=name)
        question149.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices149 = [
    {"text": "Bracknagh Rd", "label": "A", "is_correct": False},
    {"text": "L3100", "label": "B", "is_correct": False},
    {"text": "Rathangan Main St", "label": "C", "is_correct": True},
    {"text": "New St", "label": "D", "is_correct": False},
]
for choice in choices149:
    try:
        Choice.objects.create(
            question=question149,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q149] Failed to create choice {choice['label']}: {e}")


# === Question 150 ===
question150 = Question.objects.create(
    question_text="On what road is the Robertstown Garda Station located?",
    question_type=Question.SINGLE
)
category_names150 = ["Robertstown", "Garda Stations", "Main Roads"]
for name in category_names150:
    try:
        cat = Category.objects.get(name=name)
        question150.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices150 = [
    {"text": "Grand Canal Way", "label": "A", "is_correct": False},
    {"text": "Main St", "label": "B", "is_correct": True},
    {"text": "Grove Ln", "label": "C", "is_correct": False},
    {"text": "Father Murphy Park", "label": "D", "is_correct": False},
]
for choice in choices150:
    try:
        Choice.objects.create(
            question=question150,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q150] Failed to create choice {choice['label']}: {e}")


# === Question 151 ===
question151 = Question.objects.create(
    question_text="The Hazelhatch and Celbridge Railway station is situated on which of these roads?",
    question_type=Question.SINGLE
)
category_names151 = ["Celbridge", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names151:
    try:
        cat = Category.objects.get(name=name)
        question151.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices151 = [
    {"text": "Simmonstown Manor", "label": "A", "is_correct": False},
    {"text": "Loughlinstown Road", "label": "B", "is_correct": False},
    {"text": "The Lord Rd", "label": "C", "is_correct": False},
    {"text": "Newtown Rd", "label": "D", "is_correct": True},
]
for choice in choices151:
    try:
        Choice.objects.create(
            question=question151,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q151] Failed to create choice {choice['label']}: {e}")


# === Question 152 ===
question152 = Question.objects.create(
    question_text="The Post office situated in Celbridge can be found where?",
    question_type=Question.SINGLE
)
category_names152 = ["Celbridge", "Post Offices and Civic Services", "Main Roads"]
for name in category_names152:
    try:
        cat = Category.objects.get(name=name)
        question152.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices152 = [
    {"text": "St Patrick's Park", "label": "A", "is_correct": False},
    {"text": "Main St", "label": "B", "is_correct": True},
    {"text": "Newtown Rd", "label": "C", "is_correct": False},
    {"text": "Tea Ln", "label": "D", "is_correct": False},
]
for choice in choices152:
    try:
        Choice.objects.create(
            question=question152,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q152] Failed to create choice {choice['label']}: {e}")


# === Question 153 ===
question153 = Question.objects.create(
    question_text="Where can one find the Post office located in Leixlip?",
    question_type=Question.SINGLE
)
category_names153 = ["Leixlip", "Post Offices and Civic Services", "Main Roads"]
for name in category_names153:
    try:
        cat = Category.objects.get(name=name)
        question153.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices153 = [
    {"text": "Main St", "label": "A", "is_correct": True},
    {"text": "Mill Ln", "label": "B", "is_correct": False},
    {"text": "Buckley's Lane", "label": "C", "is_correct": False},
    {"text": "Old Hill", "label": "D", "is_correct": False},
]
for choice in choices153:
    try:
        Choice.objects.create(
            question=question153,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q153] Failed to create choice {choice['label']}: {e}")


# === Question 154 ===
question154 = Question.objects.create(
    question_text="What road can the Leixlip Confey Bridge Railway station be found on?",
    question_type=Question.SINGLE
)
category_names154 = ["Leixlip", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names154:
    try:
        cat = Category.objects.get(name=name)
        question154.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices154 = [
    {"text": "Glendale", "label": "A", "is_correct": False},
    {"text": "Main St", "label": "B", "is_correct": False},
    {"text": "Station Rd", "label": "C", "is_correct": True},
    {"text": "Captains Hill", "label": "D", "is_correct": False},
]
for choice in choices154:
    try:
        Choice.objects.create(
            question=question154,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q154] Failed to create choice {choice['label']}: {e}")


# === Question 155 ===
question155 = Question.objects.create(
    question_text="Where is Leixlip Louisa Bridge Railway station located?",
    question_type=Question.SINGLE
)
category_names155 = ["Leixlip", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names155:
    try:
        cat = Category.objects.get(name=name)
        question155.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices155 = [
    {"text": "Main St", "label": "A", "is_correct": False},
    {"text": "Green Ln", "label": "B", "is_correct": False},
    {"text": "Celbridge Rd", "label": "C", "is_correct": False},
    {"text": "Station Road", "label": "D", "is_correct": True},
]
for choice in choices155:
    try:
        Choice.objects.create(
            question=question155,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q155] Failed to create choice {choice['label']}: {e}")


# === Question 156 ===
question156 = Question.objects.create(
    question_text="What road leads to Leixlip town council?",
    question_type=Question.SINGLE
)
category_names156 = ["Leixlip", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names156:
    try:
        cat = Category.objects.get(name=name)
        question156.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices156 = [
    {"text": "Captains Hill", "label": "A", "is_correct": True},
    {"text": "Avondale", "label": "B", "is_correct": False},
    {"text": "Main St", "label": "C", "is_correct": False},
    {"text": "Green Lane", "label": "D", "is_correct": False},
]
for choice in choices156:
    try:
        Choice.objects.create(
            question=question156,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q156] Failed to create choice {choice['label']}: {e}")


# === Question 157 ===
question157 = Question.objects.create(
    question_text="Where can one find the Post office located in Maynooth?",
    question_type=Question.SINGLE
)
category_names157 = ["Maynooth", "Post Offices and Civic Services", "Main Roads"]
for name in category_names157:
    try:
        cat = Category.objects.get(name=name)
        question157.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices157 = [
    {"text": "Straffan Rd", "label": "A", "is_correct": False},
    {"text": "Dublin Rd", "label": "B", "is_correct": True},
    {"text": "Molyglare Rd", "label": "C", "is_correct": False},
    {"text": "Doctors Ln", "label": "D", "is_correct": False},
]
for choice in choices157:
    try:
        Choice.objects.create(
            question=question157,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q157] Failed to create choice {choice['label']}: {e}")


# === Question 158 ===
question158 = Question.objects.create(
    question_text="What road houses the Maynooth Railway station?",
    question_type=Question.SINGLE
)
category_names158 = ["Maynooth", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names158:
    try:
        cat = Category.objects.get(name=name)
        question158.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices158 = [
    {"text": "Straffan Rd", "label": "A", "is_correct": True},
    {"text": "Dunboyne Rd", "label": "B", "is_correct": False},
    {"text": "Lienster Cottage", "label": "C", "is_correct": False},
    {"text": "Laurence Ave", "label": "D", "is_correct": False},
]
for choice in choices158:
    try:
        Choice.objects.create(
            question=question158,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q158] Failed to create choice {choice['label']}: {e}")


# === Question 159 ===
question159 = Question.objects.create(
    question_text="The Kildare County Council can be found?",
    question_type=Question.SINGLE
)
category_names159 = ["Naas", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names159:
    try:
        cat = Category.objects.get(name=name)
        question159.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices159 = [
    {"text": "Ballymore Rd", "label": "A", "is_correct": False},
    {"text": "John Devoy Rd", "label": "B", "is_correct": False},
    {"text": "Rathasker Rd", "label": "C", "is_correct": False},
    {"text": "Devoy Park", "label": "D", "is_correct": True},
]
for choice in choices159:
    try:
        Choice.objects.create(
            question=question159,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q159] Failed to create choice {choice['label']}: {e}")


# === Question 160 ===
question160 = Question.objects.create(
    question_text="Where can the Post office located in Naas be found?",
    question_type=Question.SINGLE
)
category_names160 = ["Naas", "Post Offices and Civic Services", "Main Roads"]
for name in category_names160:
    try:
        cat = Category.objects.get(name=name)
        question160.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices160 = [
    {"text": "Friary Rd", "label": "A", "is_correct": False},
    {"text": "Moat Lane", "label": "B", "is_correct": False},
    {"text": "Main St Naas", "label": "C", "is_correct": True},
    {"text": "Corban's Ln", "label": "D", "is_correct": False},
]
for choice in choices160:
    try:
        Choice.objects.create(
            question=question160,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q160] Failed to create choice {choice['label']}: {e}")


# === Question 161 ===
question161 = Question.objects.create(
    question_text="Name the street that Naas town hall is situated on:",
    question_type=Question.SINGLE
)
category_names161 = ["Naas", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names161:
    try:
        cat = Category.objects.get(name=name)
        question161.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices161 = [
    {"text": "Main St Naas", "label": "A", "is_correct": True},
    {"text": "Rathasker Rd", "label": "B", "is_correct": False},
    {"text": "Corban's Ln", "label": "C", "is_correct": False},
    {"text": "Friary Rd", "label": "D", "is_correct": False},
]
for choice in choices161:
    try:
        Choice.objects.create(
            question=question161,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q161] Failed to create choice {choice['label']}: {e}")


# === Question 162 ===
question162 = Question.objects.create(
    question_text="Where is Naas District court located?",
    question_type=Question.SINGLE
)
category_names162 = ["Naas", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names162:
    try:
        cat = Category.objects.get(name=name)
        question162.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices162 = [
    {"text": "Corban's Lane", "label": "A", "is_correct": True},
    {"text": "Church Ln", "label": "B", "is_correct": False},
    {"text": "Main St Naas", "label": "C", "is_correct": False},
    {"text": "Rathasker Rd", "label": "D", "is_correct": False},
]
for choice in choices162:
    try:
        Choice.objects.create(
            question=question162,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q162] Failed to create choice {choice['label']}: {e}")


# === Question 163 ===
question163 = Question.objects.create(
    question_text="The Post office located in Newbridge is housed on what road?",
    question_type=Question.SINGLE
)
category_names163 = ["Newbridge", "Post Offices and Civic Services", "Main Roads"]
for name in category_names163:
    try:
        cat = Category.objects.get(name=name)
        question163.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices163 = [
    {"text": "Athgarvan Rd", "label": "A", "is_correct": False},
    {"text": "Eyre St", "label": "B", "is_correct": False},
    {"text": "Main St Newbridge", "label": "C", "is_correct": True},
    {"text": "Liffey View", "label": "D", "is_correct": False},
]
for choice in choices163:
    try:
        Choice.objects.create(
            question=question163,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q163] Failed to create choice {choice['label']}: {e}")


# === Question 164 ===
question164 = Question.objects.create(
    question_text="Name the road that houses the Newbridge Railway Station?",
    question_type=Question.SINGLE
)
category_names164 = ["Newbridge", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names164:
    try:
        cat = Category.objects.get(name=name)
        question164.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices164 = [
    {"text": "Bride St", "label": "A", "is_correct": False},
    {"text": "Rickardstown", "label": "B", "is_correct": False},
    {"text": "Eyre St", "label": "C", "is_correct": False},
    {"text": "Station Rd", "label": "D", "is_correct": True},
]
for choice in choices164:
    try:
        Choice.objects.create(
            question=question164,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q164] Failed to create choice {choice['label']}: {e}")


# === Question 165 ===
question165 = Question.objects.create(
    question_text="Newbridge Town Hall can be found on which of these roads?",
    question_type=Question.SINGLE
)
category_names165 = ["Newbridge", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names165:
    try:
        cat = Category.objects.get(name=name)
        question165.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices165 = [
    {"text": "Henry Rd", "label": "A", "is_correct": False},
    {"text": "Main St Newbridge", "label": "B", "is_correct": True},
    {"text": "James St", "label": "C", "is_correct": False},
    {"text": "College Park Rd", "label": "D", "is_correct": False},
]
for choice in choices165:
    try:
        Choice.objects.create(
            question=question165,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q165] Failed to create choice {choice['label']}: {e}")


# === Question 166 ===
question166 = Question.objects.create(
    question_text="Where can one find the Post Office located in Kildare?",
    question_type=Question.SINGLE
)
category_names166 = ["Kildare (Town)", "Post Offices and Civic Services", "Main Roads"]
for name in category_names166:
    try:
        cat = Category.objects.get(name=name)
        question166.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices166 = [
    {"text": "Bride St", "label": "A", "is_correct": True},
    {"text": "Meadow Rd", "label": "B", "is_correct": False},
    {"text": "Claregate St", "label": "C", "is_correct": False},
    {"text": "Pigeon Ln", "label": "D", "is_correct": False},
]
for choice in choices166:
    try:
        Choice.objects.create(
            question=question166,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q166] Failed to create choice {choice['label']}: {e}")


# === Question 167 ===
question167 = Question.objects.create(
    question_text="What road is Kildare Railway Station situated on?",
    question_type=Question.SINGLE
)
category_names167 = ["Kildare (Town)", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names167:
    try:
        cat = Category.objects.get(name=name)
        question167.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices167 = [
    {"text": "Station Road", "label": "A", "is_correct": True},
    {"text": "Assumpta Villas", "label": "B", "is_correct": False},
    {"text": "Fair Green Rd", "label": "C", "is_correct": False},
    {"text": "Curragh Finn", "label": "D", "is_correct": False},
]
for choice in choices167:
    try:
        Choice.objects.create(
            question=question167,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q167] Failed to create choice {choice['label']}: {e}")


# === Question 168 ===
question168 = Question.objects.create(
    question_text="The Post Office located in Athy can be found on what road?",
    question_type=Question.SINGLE
)
category_names168 = ["Athy", "Post Offices and Civic Services", "Main Roads"]
for name in category_names168:
    try:
        cat = Category.objects.get(name=name)
        question168.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices168 = [
    {"text": "Duke St", "label": "A", "is_correct": True},
    {"text": "Green Alley", "label": "B", "is_correct": False},
    {"text": "Convent Ln", "label": "C", "is_correct": False},
    {"text": "Stanhope PI", "label": "D", "is_correct": False},
]
for choice in choices168:
    try:
        Choice.objects.create(
            question=question168,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q168] Failed to create choice {choice['label']}: {e}")


# === Question 169 ===
question169 = Question.objects.create(
    question_text="On what road is Athy Railway Station located on?",
    question_type=Question.SINGLE
)
category_names169 = ["Athy", "Train Stations and Transport Hubs", "Main Roads"]
for name in category_names169:
    try:
        cat = Category.objects.get(name=name)
        question169.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices169 = [
    {"text": "Church Road", "label": "A", "is_correct": True},
    {"text": "Rheban Manor", "label": "B", "is_correct": False},
    {"text": "Convent View", "label": "C", "is_correct": False},
    {"text": "Mansfield Grove", "label": "D", "is_correct": False},
]
for choice in choices169:
    try:
        Choice.objects.create(
            question=question169,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q169] Failed to create choice {choice['label']}: {e}")


# === Question 170 ===
question170 = Question.objects.create(
    question_text="Which of these roads houses Athy Municipal District Council?",
    question_type=Question.SINGLE
)
category_names170 = ["Athy", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names170:
    try:
        cat = Category.objects.get(name=name)
        question170.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices170 = [
    {"text": "Rathstewart", "label": "A", "is_correct": True},
    {"text": "Convent View", "label": "B", "is_correct": False},
    {"text": "Stanhope St", "label": "C", "is_correct": False},
    {"text": "Stanhope PI", "label": "D", "is_correct": False},
]
for choice in choices170:
    try:
        Choice.objects.create(
            question=question170,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q170] Failed to create choice {choice['label']}: {e}")


# === Question 171 ===
question171 = Question.objects.create(
    question_text="Athy Courthouse is housed on what road?",
    question_type=Question.SINGLE
)
category_names171 = ["Athy", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names171:
    try:
        cat = Category.objects.get(name=name)
        question171.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices171 = [
    {"text": "Emily Square", "label": "A", "is_correct": True},
    {"text": "Convent View", "label": "B", "is_correct": False},
    {"text": "Meeting Ln", "label": "C", "is_correct": False},
    {"text": "Barrow Quay", "label": "D", "is_correct": False},
]
for choice in choices171:
    try:
        Choice.objects.create(
            question=question171,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q171] Failed to create choice {choice['label']}: {e}")


# === Question 172 ===
question172 = Question.objects.create(
    question_text="The Kilcullen Town Hall can be found where?",
    question_type=Question.SINGLE
)
category_names172 = ["Kilcullen", "Town Halls and Municipal Buildings", "Main Roads"]
for name in category_names172:
    try:
        cat = Category.objects.get(name=name)
        question172.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices172 = [
    {"text": "Riverside Cresent", "label": "A", "is_correct": False},
    {"text": "Main St, Kilcullen", "label": "B", "is_correct": True},
    {"text": "Kilcullen Slope", "label": "C", "is_correct": False},
    {"text": "New Abbey Rd", "label": "D", "is_correct": False},
]
for choice in choices172:
    try:
        Choice.objects.create(
            question=question172,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q172] Failed to create choice {choice['label']}: {e}")


# === Question 173 ===
question173 = Question.objects.create(
    question_text="The John Devoy Memorial Statue stands where in Naas?",
    question_type=Question.SINGLE
)
category_names173 = ["Naas", "Heritage Sites and Monuments", "Main Roads"]
for name in category_names173:
    try:
        cat = Category.objects.get(name=name)
        question173.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices173 = [
    {"text": "Abbey Bridge", "label": "A", "is_correct": False},
    {"text": "Friary Gate", "label": "B", "is_correct": False},
    {"text": "Poplar Sq", "label": "C", "is_correct": True},
    {"text": "Kildare Square", "label": "D", "is_correct": False},
]
for choice in choices173:
    try:
        Choice.objects.create(
            question=question173,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q173] Failed to create choice {choice['label']}: {e}")


# === Question 174 ===
question174 = Question.objects.create(
    question_text="Which Street connects Leinster Cottages and Dunboyne RD?",
    question_type=Question.SINGLE
)
category_names174 = ["Maynooth", "Connecting Road Junctions and Roundabouts", "Main Roads"]
for name in category_names174:
    try:
        cat = Category.objects.get(name=name)
        question174.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices174 = [
    {"text": "Pebble Hill", "label": "A", "is_correct": False},
    {"text": "Back Lane", "label": "B", "is_correct": True},
    {"text": "Leinster Park", "label": "C", "is_correct": False},
    {"text": "lyreen Lodge", "label": "D", "is_correct": False},
]
for choice in choices174:
    try:
        Choice.objects.create(
            question=question174,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q174] Failed to create choice {choice['label']}: {e}")


# === Question 175 ===
question175 = Question.objects.create(
    question_text="Which Lane runs one way between Dublin Rd and Straffan Rd?",
    question_type=Question.SINGLE
)
category_names175 = ["Maynooth", "One-Way Streets", "Main Roads"]
for name in category_names175:
    try:
        cat = Category.objects.get(name=name)
        question175.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices175 = [
    {"text": "Buckley's Ln", "label": "A", "is_correct": False},
    {"text": "Doctors Lane", "label": "B", "is_correct": True},
    {"text": "Leinster St", "label": "C", "is_correct": False},
    {"text": "Pound Ln", "label": "D", "is_correct": False},
]
for choice in choices175:
    try:
        Choice.objects.create(
            question=question175,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q175] Failed to create choice {choice['label']}: {e}")


# === Question 176 ===
question176 = Question.objects.create(
    question_text="what road runs between Dawson St and Henry St?",
    question_type=Question.SINGLE
)
category_names176 = ["Newbridge", "Connecting Road Junctions and Roundabouts", "Main Roads"]
for name in category_names176:
    try:
        cat = Category.objects.get(name=name)
        question176.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices176 = [
    {"text": "College Park Rd", "label": "A", "is_correct": False},
    {"text": "Henry Street", "label": "B", "is_correct": False},
    {"text": "Rowan Tce", "label": "C", "is_correct": False},
    {"text": "Limerick Lane", "label": "D", "is_correct": True},
]
for choice in choices176:
    try:
        Choice.objects.create(
            question=question176,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q176] Failed to create choice {choice['label']}: {e}")


# === Question 177 ===
question177 = Question.objects.create(
    question_text="Name the road that connects Athgarvan Rd and Edward St?",
    question_type=Question.SINGLE
)
category_names177 = ["Newbridge", "Main Roads", "Connecting Road Junctions and Roundabouts"]
for name in category_names177:
    try:
        cat = Category.objects.get(name=name)
        question177.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices177 = [
    {"text": "Henry Street", "label": "A", "is_correct": False},
    {"text": "Cutlery Rd", "label": "B", "is_correct": True},
    {"text": "Liffey View", "label": "C", "is_correct": False},
    {"text": "Limerick Ln", "label": "D", "is_correct": False},
]
for choice in choices177:
    try:
        Choice.objects.create(
            question=question177,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q177] Failed to create choice {choice['label']}: {e}")


# === Question 178 ===
question178 = Question.objects.create(
    question_text="What road runs between Main St and Eyre St?",
    question_type=Question.SINGLE
)
category_names178 = ["Newbridge", "Main Roads", "Connecting Road Junctions and Roundabouts"]
for name in category_names178:
    try:
        cat = Category.objects.get(name=name)
        question178.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices178 = [
    {"text": "Henry Street", "label": "A", "is_correct": True},
    {"text": "College Park Rd", "label": "B", "is_correct": False},
    {"text": "Rowan Tce", "label": "C", "is_correct": False},
    {"text": "Robert St", "label": "D", "is_correct": False},
]
for choice in choices178:
    try:
        Choice.objects.create(
            question=question178,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q178] Failed to create choice {choice['label']}: {e}")


# === Question 179 ===
question179 = Question.objects.create(
    question_text="North Main St and Abbey Rd are connected by which road?",
    question_type=Question.SINGLE
)
category_names179 = ["Naas", "Main Roads", "Connecting Road Junctions and Roundabouts"]
for name in category_names179:
    try:
        cat = Category.objects.get(name=name)
        question179.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices179 = [
    {"text": "Friary Rd", "label": "A", "is_correct": True},
    {"text": "Town Hall Lane", "label": "B", "is_correct": False},
    {"text": "Corban's Ln", "label": "C", "is_correct": False},
    {"text": "St Martins Ave", "label": "D", "is_correct": False},
]
for choice in choices179:
    try:
        Choice.objects.create(
            question=question179,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q179] Failed to create choice {choice['label']}: {e}")


# === Question 180 ===
question180 = Question.objects.create(
    question_text="Select the road that connects Abbey Rd and North Main St?",
    question_type=Question.SINGLE
)
category_names180 = ["Naas", "Main Roads", "Connecting Road Junctions and Roundabouts"]
for name in category_names180:
    try:
        cat = Category.objects.get(name=name)
        question180.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices180 = [
    {"text": "Corban's Ln", "label": "A", "is_correct": True},
    {"text": "Moat Lane", "label": "B", "is_correct": False},
    {"text": "Blessignton Rd", "label": "C", "is_correct": False},
    {"text": "Friary Rd", "label": "D", "is_correct": False},
]
for choice in choices180:
    try:
        Choice.objects.create(
            question=question180,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q180] Failed to create choice {choice['label']}: {e}")


# === Question 181 ===
question181 = Question.objects.create(
    question_text="Which of these roads is the connector between Rathasker Rd and North Main St?",
    question_type=Question.SINGLE
)
category_names181 = ["Naas", "Main Roads", "Connecting Road Junctions and Roundabouts"]
for name in category_names181:
    try:
        cat = Category.objects.get(name=name)
        question181.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices181 = [
    {"text": "St Michaels", "label": "A", "is_correct": False},
    {"text": "St Martins Ave", "label": "B", "is_correct": False},
    {"text": "Caragh Rd", "label": "C", "is_correct": False},
    {"text": "John Devoy Rd", "label": "D", "is_correct": True},
]
for choice in choices181:
    try:
        Choice.objects.create(
            question=question181,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q181] Failed to create choice {choice['label']}: {e}")


# === Question 182 ===
question182 = Question.objects.create(
    question_text="Which of these roads runs between Station Road and Dunmurray Rd?",
    question_type=Question.SINGLE
)
category_names182 = ["Kildare (Town)", "Main Roads", "Connecting Road Junctions and Roundabouts"]
for name in category_names182:
    try:
        cat = Category.objects.get(name=name)
        question182.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices182 = [
    {"text": "Fair Green Rd", "label": "A", "is_correct": False},
    {"text": "Dara Park", "label": "B", "is_correct": True},
    {"text": "White Abbey Rd", "label": "C", "is_correct": False},
    {"text": "Elm Park", "label": "D", "is_correct": False},
]
for choice in choices182:
    try:
        Choice.objects.create(
            question=question182,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q182] Failed to create choice {choice['label']}: {e}")


# === Question 183 ===
question183 = Question.objects.create(
    question_text="Which Street runs one way between Stanhope place and Leinster Street in Athy?",
    question_type=Question.SINGLE
)
category_names183 = ["Athy", "Main Roads", "One-Way Streets"]
for name in category_names183:
    try:
        cat = Category.objects.get(name=name)
        question183.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices183 = [
    {"text": "Green Alley", "label": "A", "is_correct": False},
    {"text": "Clonmullion Estate", "label": "B", "is_correct": False},
    {"text": "Kirwans Ln", "label": "C", "is_correct": False},
    {"text": "Chapel Lane", "label": "D", "is_correct": True},
]
for choice in choices183:
    try:
        Choice.objects.create(
            question=question183,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q183] Failed to create choice {choice['label']}: {e}")


# === Question 184 ===
question184 = Question.objects.create(
    question_text="What road houses Wonderful Barn in Leixlip?",
    question_type=Question.SINGLE
)
category_names184 = ["Leixlip", "Heritage Sites and Monuments", "Main Roads"]
for name in category_names184:
    try:
        cat = Category.objects.get(name=name)
        question184.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices184 = [
    {"text": "Forrest park", "label": "A", "is_correct": False},
    {"text": "Green Ln", "label": "B", "is_correct": False},
    {"text": "Celbridge Rd", "label": "C", "is_correct": False},
    {"text": "Barnhall Drive", "label": "D", "is_correct": True},
]
for choice in choices184:
    try:
        Choice.objects.create(
            question=question184,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q184] Failed to create choice {choice['label']}: {e}")


# === Question 185 ===
question185 = Question.objects.create(
    question_text="Where can one find the Castletown House?",
    question_type=Question.SINGLE
)
category_names185 = ["Celbridge", "Heritage Sites and Monuments"]
for name in category_names185:
    try:
        cat = Category.objects.get(name=name)
        question185.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices185 = [
    {"text": "Kildare", "label": "A", "is_correct": False},
    {"text": "Rathangan", "label": "B", "is_correct": False},
    {"text": "Naas", "label": "C", "is_correct": False},
    {"text": "Celbridge", "label": "D", "is_correct": True},
]
for choice in choices185:
    try:
        Choice.objects.create(
            question=question185,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q185] Failed to create choice {choice['label']}: {e}")


# === Question 186 ===
question186 = Question.objects.create(
    question_text="Select the road that Kildrought House can be found on in Celbridge:",
    question_type=Question.SINGLE
)
category_names186 = ["Celbridge", "Heritage Sites and Monuments", "Main Roads"]
for name in category_names186:
    try:
        cat = Category.objects.get(name=name)
        question186.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices186 = [
    {"text": "Dara Ct", "label": "A", "is_correct": False},
    {"text": "Elm Park", "label": "B", "is_correct": False},
    {"text": "Main St", "label": "C", "is_correct": True},
    {"text": "Castletown Dr", "label": "D", "is_correct": False},
]
for choice in choices186:
    try:
        Choice.objects.create(
            question=question186,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q186] Failed to create choice {choice['label']}: {e}")


# === Question 187 ===
question187 = Question.objects.create(
    question_text="Maynooth Castle is situated on what road?",
    question_type=Question.SINGLE
)
category_names187 = ["Maynooth", "Heritage Sites and Monuments", "Main Roads"]
for name in category_names187:
    try:
        cat = Category.objects.get(name=name)
        question187.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices187 = [
    {"text": "Meadowbrook Rd", "label": "A", "is_correct": False},
    {"text": "Molglare Rd", "label": "B", "is_correct": False},
    {"text": "Parson St", "label": "C", "is_correct": True},
    {"text": "Parson Lodge", "label": "D", "is_correct": False},
]
for choice in choices187:
    try:
        Choice.objects.create(
            question=question187,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q187] Failed to create choice {choice['label']}: {e}")


# === Question 188 ===
question188 = Question.objects.create(
    question_text="Where can one find the Steam Museum?",
    question_type=Question.SINGLE
)
category_names188 = ["Straffan", "Museums and Galleries"]
for name in category_names188:
    try:
        cat = Category.objects.get(name=name)
        question188.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices188 = [
    {"text": "Newbridge", "label": "A", "is_correct": False},
    {"text": "Kildare", "label": "B", "is_correct": False},
    {"text": "Naas", "label": "C", "is_correct": False},
    {"text": "Straffan", "label": "D", "is_correct": True},
]
for choice in choices188:
    try:
        Choice.objects.create(
            question=question188,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q188] Failed to create choice {choice['label']}: {e}")


# === Question 189 ===
question189 = Question.objects.create(
    question_text="Which of these streets is Jigginstown Castle situated on in Naas?",
    question_type=Question.SINGLE
)
category_names189 = ["Naas", "Heritage Sites and Monuments", "Main Roads"]
for name in category_names189:
    try:
        cat = Category.objects.get(name=name)
        question189.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices189 = [
    {"text": "Jigginstown Green", "label": "A", "is_correct": False},
    {"text": "Elsmore Walk", "label": "B", "is_correct": False},
    {"text": "Caragh Rd", "label": "C", "is_correct": False},
    {"text": "Newbridge Rd", "label": "D", "is_correct": True},
]
for choice in choices189:
    try:
        Choice.objects.create(
            question=question189,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q189] Failed to create choice {choice['label']}: {e}")


# === Question 190 ===
question190 = Question.objects.create(
    question_text="Which of these roads is Liffey Linear Park located on in Newbridge?",
    question_type=Question.SINGLE
)
category_names190 = ["Newbridge", "Parks and Gardens", "Main Roads"]
for name in category_names190:
    try:
        cat = Category.objects.get(name=name)
        question190.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices190 = [
    {"text": "Liffey View", "label": "A", "is_correct": True},
    {"text": "Henry St", "label": "B", "is_correct": False},
    {"text": "Athgarvan Rd", "label": "C", "is_correct": False},
    {"text": "Connell Drive", "label": "D", "is_correct": False},
]
for choice in choices190:
    try:
        Choice.objects.create(
            question=question190,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q190] Failed to create choice {choice['label']}: {e}")


# === Question 191 ===
question191 = Question.objects.create(
    question_text="Which road is Kildare town Heritage centre located on?",
    question_type=Question.SINGLE
)
category_names191 = ["Kildare (Town)", "Heritage Sites and Monuments", "Main Roads"]
for name in category_names191:
    try:
        cat = Category.objects.get(name=name)
        question191.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices191 = [
    {"text": "Pigeon Ln", "label": "A", "is_correct": False},
    {"text": "Fire Castle Ln", "label": "B", "is_correct": False},
    {"text": "Market Sq", "label": "C", "is_correct": True},
    {"text": "Bride St", "label": "D", "is_correct": False},
]
for choice in choices191:
    try:
        Choice.objects.create(
            question=question191,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q191] Failed to create choice {choice['label']}: {e}")


# === Question 192 ===
question192 = Question.objects.create(
    question_text="The Irish National Stud & Gardens is situated where in Kildare?",
    question_type=Question.SINGLE
)
category_names192 = ["Kildare (Town)", "Heritage Sites and Monuments", "Parks and Gardens"]
for name in category_names192:
    try:
        cat = Category.objects.get(name=name)
        question192.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices192 = [
    {"text": "Rathangan", "label": "A", "is_correct": False},
    {"text": "Newbridge", "label": "B", "is_correct": False},
    {"text": "Tully", "label": "C", "is_correct": True},
    {"text": "Miltown", "label": "D", "is_correct": False},
]
for choice in choices192:
    try:
        Choice.objects.create(
            question=question192,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q192] Failed to create choice {choice['label']}: {e}")


# === Question 193 ===
question193 = Question.objects.create(
    question_text="Where can you find the Athy Heritage Centre and Museum?",
    question_type=Question.SINGLE
)
category_names193 = ["Athy", "Heritage Sites and Monuments", "Museums and Galleries"]
for name in category_names193:
    try:
        cat = Category.objects.get(name=name)
        question193.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices193 = [
    {"text": "Butlers Ln", "label": "A", "is_correct": False},
    {"text": "Mount Hawkins", "label": "B", "is_correct": False},
    {"text": "Convent View", "label": "C", "is_correct": False},
    {"text": "Emily Sq", "label": "D", "is_correct": True},
]
for choice in choices193:
    try:
        Choice.objects.create(
            question=question193,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q193] Failed to create choice {choice['label']}: {e}")


# === Question 194 ===
question194 = Question.objects.create(
    question_text="Off which road is The peoples park located in Athy?",
    question_type=Question.SINGLE
)
category_names194 = ["Athy", "Parks and Gardens", "Main Roads"]
for name in category_names194:
    try:
        cat = Category.objects.get(name=name)
        question194.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices194 = [
    {"text": "Meeting Ln", "label": "A", "is_correct": False},
    {"text": "Church Rd", "label": "B", "is_correct": True},
    {"text": "Convent View", "label": "C", "is_correct": False},
    {"text": "Mount Hawkins", "label": "D", "is_correct": False},
]
for choice in choices194:
    try:
        Choice.objects.create(
            question=question194,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q194] Failed to create choice {choice['label']}: {e}")


# === Question 195 ===
question195 = Question.objects.create(
    question_text="Where can Burtown House & Gardens be found?",
    question_type=Question.SINGLE
)
category_names195 = ["Athy", "Heritage Sites and Monuments", "Parks and Gardens"]
for name in category_names195:
    try:
        cat = Category.objects.get(name=name)
        question195.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices195 = [
    {"text": "Kilkea", "label": "A", "is_correct": False},
    {"text": "Calverstown", "label": "B", "is_correct": False},
    {"text": "Athy", "label": "C", "is_correct": True},
    {"text": "Baltinglass", "label": "D", "is_correct": False},
]
for choice in choices195:
    try:
        Choice.objects.create(
            question=question195,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q195] Failed to create choice {choice['label']}: {e}")


# === Question 196 ===
question196 = Question.objects.create(
    question_text="Riverbank Arts Centre can be located where in Newbridge?",
    question_type=Question.SINGLE
)
category_names196 = ["Newbridge", "Cinemas and Theatres", "Main Roads"]
for name in category_names196:
    try:
        cat = Category.objects.get(name=name)
        question196.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices196 = [
    {"text": "Main St", "label": "A", "is_correct": True},
    {"text": "Liffey View", "label": "B", "is_correct": False},
    {"text": "Patrick St", "label": "C", "is_correct": False},
    {"text": "Station Rd", "label": "D", "is_correct": False},
]
for choice in choices196:
    try:
        Choice.objects.create(
            question=question196,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q196] Failed to create choice {choice['label']}: {e}")


# === Question 197 ===
question197 = Question.objects.create(
    question_text="Gables Guest House is on what road?",
    question_type=Question.SINGLE
)
category_names197 = ["Newbridge", "Hotels and Guesthouses", "Road Numbers"]
for name in category_names197:
    try:
        cat = Category.objects.get(name=name)
        question197.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices197 = [
    {"text": "R416", "label": "A", "is_correct": False},
    {"text": "R403", "label": "B", "is_correct": False},
    {"text": "R415", "label": "C", "is_correct": False},
    {"text": "R445", "label": "D", "is_correct": True},
]
for choice in choices197:
    try:
        Choice.objects.create(
            question=question197,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q197] Failed to create choice {choice['label']}: {e}")


# === Question 198 ===
question198 = Question.objects.create(
    question_text="The Keadeen Hotel in Newbridge is situated on what road?",
    question_type=Question.SINGLE
)
category_names198 = ["Newbridge", "Hotels and Guesthouses", "Main Roads"]
for name in category_names198:
    try:
        cat = Category.objects.get(name=name)
        question198.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices198 = [
    {"text": "Standhouse Road", "label": "A", "is_correct": False},
    {"text": "Ballymany", "label": "B", "is_correct": False},
    {"text": "Morristown Road", "label": "C", "is_correct": False},
    {"text": "Green Road", "label": "D", "is_correct": True},
]
for choice in choices198:
    try:
        Choice.objects.create(
            question=question198,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q198] Failed to create choice {choice['label']}: {e}")


# === Question 199 ===
question199 = Question.objects.create(
    question_text="Springfield B&B in Celbridge is to be found on which of these roads?",
    question_type=Question.SINGLE
)
category_names199 = ["Celbridge", "Hotels and Guesthouses", "Road Numbers"]
for name in category_names199:
    try:
        cat = Category.objects.get(name=name)
        question199.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices199 = [
    {"text": "R403", "label": "A", "is_correct": True},
    {"text": "R445", "label": "B", "is_correct": False},
    {"text": "R415", "label": "C", "is_correct": False},
    {"text": "R416", "label": "D", "is_correct": False},
]
for choice in choices199:
    try:
        Choice.objects.create(
            question=question199,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q199] Failed to create choice {choice['label']}: {e}")


# === Question 200 ===
question200 = Question.objects.create(
    question_text="Name the area that houses The Westgrove Hotel Clane",
    question_type=Question.SINGLE
)
category_names200 = ["Clane", "Hotels and Guesthouses", "Minor Roads"]
for name in category_names200:
    try:
        cat = Category.objects.get(name=name)
        question200.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices200 = [
    {"text": "The Coot", "label": "A", "is_correct": False},
    {"text": "Hillview", "label": "B", "is_correct": False},
    {"text": "Abbeylands", "label": "C", "is_correct": True},
    {"text": "Brooklands", "label": "D", "is_correct": False},
]
for choice in choices200:
    try:
        Choice.objects.create(
            question=question200,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q200] Failed to create choice {choice['label']}: {e}")


# === Question 201 ===
question201 = Question.objects.create(
    question_text="The Springfield Hotel in Leixlip is situated on which of these roads?",
    question_type=Question.SINGLE
)
category_names201 = ["Leixlip", "Hotels and Guesthouses", "Main Roads"]
for name in category_names201:
    try:
        cat = Category.objects.get(name=name)
        question201.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices201 = [
    {"text": "Old Hill", "label": "A", "is_correct": False},
    {"text": "Leixlip Road", "label": "B", "is_correct": True},
    {"text": "The Black Avenue", "label": "C", "is_correct": False},
    {"text": "", "label": "D", "is_correct": False},
]
for choice in choices201:
    try:
        Choice.objects.create(
            question=question201,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q201] Failed to create choice {choice['label']}: {e}")


# === Question 202 ===
question202 = Question.objects.create(
    question_text="Where can one find The Court Yard Hotel in Leixlip?",
    question_type=Question.SINGLE
)
category_names202 = ["Leixlip", "Hotels and Guesthouses", "Main Roads"]
for name in category_names202:
    try:
        cat = Category.objects.get(name=name)
        question202.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices202 = [
    {"text": "Elton Court", "label": "A", "is_correct": False},
    {"text": "Captain's Hill", "label": "B", "is_correct": False},
    {"text": "Green Lane", "label": "C", "is_correct": False},
    {"text": "Main Street", "label": "D", "is_correct": True},
]
for choice in choices202:
    try:
        Choice.objects.create(
            question=question202,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q202] Failed to create choice {choice['label']}: {e}")


# === Question 203 ===
question203 = Question.objects.create(
    question_text="Where can Leixlip Manor Hotel be found?",
    question_type=Question.SINGLE
)
category_names203 = ["Leixlip", "Hotels and Guesthouses", "Main Roads"]
for name in category_names203:
    try:
        cat = Category.objects.get(name=name)
        question203.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices203 = [
    {"text": "Backweston", "label": "A", "is_correct": False},
    {"text": "Kilmacredock", "label": "B", "is_correct": False},
    {"text": "Stacumny Lane", "label": "C", "is_correct": True},
    {"text": "Saint Catherines Park", "label": "D", "is_correct": False},
]
for choice in choices203:
    try:
        Choice.objects.create(
            question=question203,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q203] Failed to create choice {choice['label']}: {e}")


# === Question 204 ===
question204 = Question.objects.create(
    question_text="The Glenroyal Hotel can be found where in Maynooth?",
    question_type=Question.SINGLE
)
category_names204 = ["Maynooth", "Hotels and Guesthouses", "Main Roads"]
for name in category_names204:
    try:
        cat = Category.objects.get(name=name)
        question204.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices204 = [
    {"text": "Moyglare Road", "label": "A", "is_correct": False},
    {"text": "Back Lane", "label": "B", "is_correct": False},
    {"text": "Straffan Road", "label": "C", "is_correct": True},
    {"text": "Kilcock Road", "label": "D", "is_correct": False},
]
for choice in choices204:
    try:
        Choice.objects.create(
            question=question204,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q204] Failed to create choice {choice['label']}: {e}")


# === Question 205 ===
question205 = Question.objects.create(
    question_text="Where is Lawlor's of Naas found?",
    question_type=Question.SINGLE
)
category_names205 = ["Naas", "Hotels and Guesthouses", "Main Roads"]
for name in category_names205:
    try:
        cat = Category.objects.get(name=name)
        question205.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices205 = [
    {"text": "Tipper Road", "label": "A", "is_correct": False},
    {"text": "Roselawn", "label": "B", "is_correct": False},
    {"text": "Poplar Square", "label": "C", "is_correct": True},
    {"text": "Moat Lane", "label": "D", "is_correct": False},
]
for choice in choices205:
    try:
        Choice.objects.create(
            question=question205,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q205] Failed to create choice {choice['label']}: {e}")


# === Question 206 ===
question206 = Question.objects.create(
    question_text="The Osprey Hotel in Naas is housed on which road?",
    question_type=Question.SINGLE
)
category_names206 = ["Naas", "Hotels and Guesthouses", "Main Roads"]
for name in category_names206:
    try:
        cat = Category.objects.get(name=name)
        question206.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices206 = [
    {"text": "Millbrook Court", "label": "A", "is_correct": False},
    {"text": "Devoy Quarter", "label": "B", "is_correct": True},
    {"text": "Newbridge Road", "label": "C", "is_correct": False},
    {"text": "Kilcullen Road", "label": "D", "is_correct": False},
]
for choice in choices206:
    try:
        Choice.objects.create(
            question=question206,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q206] Failed to create choice {choice['label']}: {e}")


# === Question 207 ===
question207 = Question.objects.create(
    question_text="The Town House Hotel can be found on what road in Naas?",
    question_type=Question.SINGLE
)
category_names207 = ["Naas", "Hotels and Guesthouses", "Main Roads"]
for name in category_names207:
    try:
        cat = Category.objects.get(name=name)
        question207.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices207 = [
    {"text": "Corbally Court", "label": "A", "is_correct": False},
    {"text": "Sarto Road", "label": "B", "is_correct": False},
    {"text": "Church Lane", "label": "C", "is_correct": False},
    {"text": "Newbridge Road", "label": "D", "is_correct": True},
]
for choice in choices207:
    try:
        Choice.objects.create(
            question=question207,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q207] Failed to create choice {choice['label']}: {e}")


# === Question 208 ===
question208 = Question.objects.create(
    question_text="Where is the Naas Court Hotel situated?",
    question_type=Question.SINGLE
)
category_names208 = ["Naas", "Hotels and Guesthouses", "Main Roads"]
for name in category_names208:
    try:
        cat = Category.objects.get(name=name)
        question208.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices208 = [
    {"text": "Blessignton Road", "label": "A", "is_correct": False},
    {"text": "South Main Street", "label": "B", "is_correct": True},
    {"text": "Corban's Lane", "label": "C", "is_correct": False},
    {"text": "Sallins Road", "label": "D", "is_correct": False},
]
for choice in choices208:
    try:
        Choice.objects.create(
            question=question208,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q208] Failed to create choice {choice['label']}: {e}")


# === Question 209 ===
question209 = Question.objects.create(
    question_text="The Killashee Hotel is located off which main road?",
    question_type=Question.SINGLE
)
category_names209 = ["Naas", "Hotels and Guesthouses", "Main Roads"]
for name in category_names209:
    try:
        cat = Category.objects.get(name=name)
        question209.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices209 = [
    {"text": "Rathasker Road", "label": "A", "is_correct": False},
    {"text": "Green Avenue", "label": "B", "is_correct": False},
    {"text": "The Park", "label": "C", "is_correct": False},
    {"text": "Kilcullen Road", "label": "D", "is_correct": True},
]
for choice in choices209:
    try:
        Choice.objects.create(
            question=question209,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q209] Failed to create choice {choice['label']}: {e}")


# === Question 210 ===
question210 = Question.objects.create(
    question_text="The Kildare House Hotel can be found on which of these roads?",
    question_type=Question.SINGLE
)
category_names210 = ["Kildare (Town)", "Hotels and Guesthouses", "Main Roads"]
for name in category_names210:
    try:
        cat = Category.objects.get(name=name)
        question210.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices210 = [
    {"text": "Grey Abbey", "label": "A", "is_correct": False},
    {"text": "Tully Road", "label": "B", "is_correct": False},
    {"text": "Monasterevin Road", "label": "C", "is_correct": False},
    {"text": "Dublin Street", "label": "D", "is_correct": True},
]
for choice in choices210:
    try:
        Choice.objects.create(
            question=question210,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q210] Failed to create choice {choice['label']}: {e}")


# === Question 211 ===
question211 = Question.objects.create(
    question_text="Where can you find the Silken Thomas Hotel in Kildare?",
    question_type=Question.SINGLE
)
category_names211 = ["Kildare (Town)", "Hotels and Guesthouses", "Main Roads"]
for name in category_names211:
    try:
        cat = Category.objects.get(name=name)
        question211.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices211 = [
    {"text": "Priory Court", "label": "A", "is_correct": False},
    {"text": "Market Square", "label": "B", "is_correct": True},
    {"text": "Beechgrove", "label": "C", "is_correct": False},
    {"text": "Meadow Road", "label": "D", "is_correct": False},
]
for choice in choices211:
    try:
        Choice.objects.create(
            question=question211,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q211] Failed to create choice {choice['label']}: {e}")


# === Question 212 ===
question212 = Question.objects.create(
    question_text="Where is the Clanard Court Hotel located in Athy?",
    question_type=Question.SINGLE
)
category_names212 = ["Athy", "Hotels and Guesthouses", "Main Roads"]
for name in category_names212:
    try:
        cat = Category.objects.get(name=name)
        question212.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices212 = [
    {"text": "Woodstock Street", "label": "A", "is_correct": False},
    {"text": "Gallowshill", "label": "B", "is_correct": False},
    {"text": "Geraldine Road", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": True},
]
for choice in choices212:
    try:
        Choice.objects.create(
            question=question212,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q212] Failed to create choice {choice['label']}: {e}")


# === Question 213 ===
question213 = Question.objects.create(
    question_text="UPMC Kildare is situated on which of these roads?",
    question_type=Question.SINGLE
)
category_names213 = ["Clane", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names213:
    try:
        cat = Category.objects.get(name=name)
        question213.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices213 = [
    {"text": "Prosperous Road", "label": "A", "is_correct": False},
    {"text": "Hemingway Park", "label": "B", "is_correct": False},
    {"text": "Millicent Road", "label": "C", "is_correct": True},
    {"text": "Main Street", "label": "D", "is_correct": False},
]
for choice in choices213:
    try:
        Choice.objects.create(
            question=question213,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q213] Failed to create choice {choice['label']}: {e}")


# === Question 214 ===
question214 = Question.objects.create(
    question_text="Where is the Institut Marques located in Clane?",
    question_type=Question.SINGLE
)
category_names214 = ["Clane", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names214:
    try:
        cat = Category.objects.get(name=name)
        question214.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices214 = [
    {"text": "Prosperous Road", "label": "A", "is_correct": False},
    {"text": "Main Street", "label": "B", "is_correct": False},
    {"text": "The Avenue", "label": "C", "is_correct": False},
    {"text": "Millicent Road", "label": "D", "is_correct": True},
]
for choice in choices214:
    try:
        Choice.objects.create(
            question=question214,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q214] Failed to create choice {choice['label']}: {e}")


# === Question 215 ===
question215 = Question.objects.create(
    question_text="Naas General Hospital can be found on which road?",
    question_type=Question.SINGLE
)
category_names215 = ["Naas", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names215:
    try:
        cat = Category.objects.get(name=name)
        question215.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices215 = [
    {"text": "Mountain View", "label": "A", "is_correct": False},
    {"text": "Craddockstown Road", "label": "B", "is_correct": True},
    {"text": "Corban's Lane", "label": "C", "is_correct": False},
    {"text": "Ballycane Road", "label": "D", "is_correct": False},
]
for choice in choices215:
    try:
        Choice.objects.create(
            question=question215,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q215] Failed to create choice {choice['label']}: {e}")


# === Question 216 ===
question216 = Question.objects.create(
    question_text="What road leads into Newbridge Women's Health & Family Planning Clinic?",
    question_type=Question.SINGLE
)
category_names216 = ["Newbridge", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names216:
    try:
        cat = Category.objects.get(name=name)
        question216.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices216 = [
    {"text": "The View", "label": "A", "is_correct": False},
    {"text": "The Square", "label": "B", "is_correct": True},
    {"text": "Curragh Grange", "label": "C", "is_correct": False},
    {"text": "Kilbelin Alley", "label": "D", "is_correct": False},
]
for choice in choices216:
    try:
        Choice.objects.create(
            question=question216,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q216] Failed to create choice {choice['label']}: {e}")


# === Question 217 ===
question217 = Question.objects.create(
    question_text="Saint Brigid's Hospice The Curragh can be found where?",
    question_type=Question.SINGLE
)
category_names217 = ["Curragh", "Hospitals and Medical Centres", "Road Numbers"]
for name in category_names217:
    try:
        cat = Category.objects.get(name=name)
        question217.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices217 = [
    {"text": "R413", "label": "A", "is_correct": False},
    {"text": "R415", "label": "B", "is_correct": False},
    {"text": "R416", "label": "C", "is_correct": True},
    {"text": "R445", "label": "D", "is_correct": False},
]
for choice in choices217:
    try:
        Choice.objects.create(
            question=question217,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q217] Failed to create choice {choice['label']}: {e}")


# === Question 218 ===
question218 = Question.objects.create(
    question_text="Where is Kildare Medical Centre located?",
    question_type=Question.SINGLE
)
category_names218 = ["Kildare (Town)", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names218:
    try:
        cat = Category.objects.get(name=name)
        question218.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices218 = [
    {"text": "Bride Street", "label": "A", "is_correct": True},
    {"text": "Cleamore Road", "label": "B", "is_correct": False},
    {"text": "Grey Abbey Road", "label": "C", "is_correct": False},
    {"text": "Curragh Road", "label": "D", "is_correct": False},
]
for choice in choices218:
    try:
        Choice.objects.create(
            question=question218,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q218] Failed to create choice {choice['label']}: {e}")


# === Question 219 ===
question219 = Question.objects.create(
    question_text="Where can one find Saint Vincent's Hospital located in Athy?",
    question_type=Question.SINGLE
)
category_names219 = ["Athy", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names219:
    try:
        cat = Category.objects.get(name=name)
        question219.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices219 = [
    {"text": "Green Alley", "label": "A", "is_correct": False},
    {"text": "Church Road", "label": "B", "is_correct": False},
    {"text": "Woodstock Street", "label": "C", "is_correct": False},
    {"text": "Rockfield Road", "label": "D", "is_correct": True},
]
for choice in choices219:
    try:
        Choice.objects.create(
            question=question219,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q219] Failed to create choice {choice['label']}: {e}")


# === Question 220 ===
question220 = Question.objects.create(
    question_text="Where is Kelly Medical Centre in Leixlip located?",
    question_type=Question.SINGLE
)
category_names220 = ["Leixlip", "Hospitals and Medical Centres", "Main Roads"]
for name in category_names220:
    try:
        cat = Category.objects.get(name=name)
        question220.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices220 = [
    {"text": "Clane Road", "label": "A", "is_correct": False},
    {"text": "Station Road", "label": "B", "is_correct": False},
    {"text": "Celbridge Road", "label": "C", "is_correct": True},
    {"text": "Green Lane", "label": "D", "is_correct": False},
]
for choice in choices220:
    try:
        Choice.objects.create(
            question=question220,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q220] Failed to create choice {choice['label']}: {e}")


# === Question 221 ===
question221 = Question.objects.create(
    question_text="Which of these areas is Ryevale Nursing home located in?",
    question_type=Question.SINGLE
)
category_names221 = ["Leixlip", "Nursing Homes"]
for name in category_names221:
    try:
        cat = Category.objects.get(name=name)
        question221.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices221 = [
    {"text": "Leixlip", "label": "A", "is_correct": True},
    {"text": "Maynooth", "label": "B", "is_correct": False},
    {"text": "Kilcock", "label": "C", "is_correct": False},
    {"text": "Celbridge", "label": "D", "is_correct": False},
]
for choice in choices221:
    try:
        Choice.objects.create(
            question=question221,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q221] Failed to create choice {choice['label']}: {e}")


# === Question 222 ===
question222 = Question.objects.create(
    question_text="Where can one find the TLC Centre Nursing home?",
    question_type=Question.SINGLE
)
category_names222 = ["Maynooth", "Nursing Homes", "Road Numbers"]
for name in category_names222:
    try:
        cat = Category.objects.get(name=name)
        question222.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices222 = [
    {"text": "R148", "label": "A", "is_correct": True},
    {"text": "R408", "label": "B", "is_correct": False},
    {"text": "R406", "label": "C", "is_correct": False},
    {"text": "R405", "label": "D", "is_correct": False},
]
for choice in choices222:
    try:
        Choice.objects.create(
            question=question222,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q222] Failed to create choice {choice['label']}: {e}")


# === Question 223 ===
question223 = Question.objects.create(
    question_text="Where is the Maynooth Lodge Nursing home situated?",
    question_type=Question.SINGLE
)
category_names223 = ["Maynooth", "Nursing Homes", "Main Roads"]
for name in category_names223:
    try:
        cat = Category.objects.get(name=name)
        question223.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices223 = [
    {"text": "Ballygoran Road", "label": "A", "is_correct": True},
    {"text": "Old Greenfield", "label": "B", "is_correct": False},
    {"text": "Laurence Avenue", "label": "C", "is_correct": False},
    {"text": "Rathcoffey Road", "label": "D", "is_correct": False},
]
for choice in choices223:
    try:
        Choice.objects.create(
            question=question223,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q223] Failed to create choice {choice['label']}: {e}")


# === Question 224 ===
question224 = Question.objects.create(
    question_text="What road houses the Moyglare Nursing home?",
    question_type=Question.SINGLE
)
category_names224 = ["Maynooth", "Nursing Homes", "Main Roads"]
for name in category_names224:
    try:
        cat = Category.objects.get(name=name)
        question224.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices224 = [
    {"text": "Moyglare Rise", "label": "A", "is_correct": False},
    {"text": "The Paddock", "label": "B", "is_correct": False},
    {"text": "Silken Vale", "label": "C", "is_correct": False},
    {"text": "Moyglare Road", "label": "D", "is_correct": True},
]
for choice in choices224:
    try:
        Choice.objects.create(
            question=question224,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q224] Failed to create choice {choice['label']}: {e}")


# === Question 225 ===
question225 = Question.objects.create(
    question_text="Where is FirstCare Nursing home located?",
    question_type=Question.SINGLE
)
category_names225 = ["Kilcock", "Nursing Homes", "Minor Roads"]
for name in category_names225:
    try:
        cat = Category.objects.get(name=name)
        question225.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices225 = [
    {"text": "Courtown Park", "label": "A", "is_correct": True},
    {"text": "Clane Road", "label": "B", "is_correct": False},
    {"text": "The Way", "label": "C", "is_correct": False},
    {"text": "Duncreevan", "label": "D", "is_correct": False},
]
for choice in choices225:
    try:
        Choice.objects.create(
            question=question225,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q225] Failed to create choice {choice['label']}: {e}")


# === Question 226 ===
question226 = Question.objects.create(
    question_text="Select the street that houses Shalom Nursing home:",
    question_type=Question.SINGLE
)
category_names226 = ["Kilcock", "Nursing Homes", "Minor Roads"]
for name in category_names226:
    try:
        cat = Category.objects.get(name=name)
        question226.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices226 = [
    {"text": "Courtown Park", "label": "A", "is_correct": False},
    {"text": "The View", "label": "B", "is_correct": False},
    {"text": "Kilcock Road", "label": "C", "is_correct": False},
    {"text": "Church Street", "label": "D", "is_correct": True},
]
for choice in choices226:
    try:
        Choice.objects.create(
            question=question226,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q226] Failed to create choice {choice['label']}: {e}")


# === Question 227 ===
question227 = Question.objects.create(
    question_text="Name the area that Parke House Nursing home can be found in:",
    question_type=Question.SINGLE
)
category_names227 = ["Kilcock", "Nursing Homes"]
for name in category_names227:
    try:
        cat = Category.objects.get(name=name)
        question227.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices227 = [
    {"text": "Kilcock", "label": "A", "is_correct": True},
    {"text": "Clane", "label": "B", "is_correct": False},
    {"text": "Celbridge", "label": "C", "is_correct": False},
    {"text": "Maynooth", "label": "D", "is_correct": False},
]
for choice in choices227:
    try:
        Choice.objects.create(
            question=question227,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q227] Failed to create choice {choice['label']}: {e}")


# === Question 228 ===
question228 = Question.objects.create(
    question_text="What road houses the Hazel Hall Nursing home?",
    question_type=Question.SINGLE
)
category_names228 = ["Clane", "Nursing Homes", "Main Roads"]
for name in category_names228:
    try:
        cat = Category.objects.get(name=name)
        question228.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices228 = [
    {"text": "Main Street", "label": "A", "is_correct": False},
    {"text": "Prosperous Road", "label": "B", "is_correct": False},
    {"text": "Clane Relief Road", "label": "C", "is_correct": False},
    {"text": "College Road", "label": "D", "is_correct": True},
]
for choice in choices228:
    try:
        Choice.objects.create(
            question=question228,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q228] Failed to create choice {choice['label']}: {e}")


# === Question 229 ===
question229 = Question.objects.create(
    question_text="Where can one find the Naas care of the aged Nursing home?",
    question_type=Question.SINGLE
)
category_names229 = ["Naas", "Nursing Homes", "Main Roads"]
for name in category_names229:
    try:
        cat = Category.objects.get(name=name)
        question229.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices229 = [
    {"text": "The Harbour", "label": "A", "is_correct": False},
    {"text": "Caragh Road", "label": "B", "is_correct": True},
    {"text": "Pacelli Road", "label": "C", "is_correct": False},
    {"text": "Limerick Road", "label": "D", "is_correct": False},
]
for choice in choices229:
    try:
        Choice.objects.create(
            question=question229,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q229] Failed to create choice {choice['label']}: {e}")


# === Question 230 ===
question230 = Question.objects.create(
    question_text="Larchfield Nursing home is located where?",
    question_type=Question.SINGLE
)
category_names230 = ["Naas", "Nursing Homes", "Minor Roads"]
for name in category_names230:
    try:
        cat = Category.objects.get(name=name)
        question230.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices230 = [
    {"text": "Roseville", "label": "A", "is_correct": False},
    {"text": "Johnstown", "label": "B", "is_correct": False},
    {"text": "Kerdiff Close", "label": "C", "is_correct": True},
    {"text": "Monread Road", "label": "D", "is_correct": False},
]
for choice in choices230:
    try:
        Choice.objects.create(
            question=question230,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q230] Failed to create choice {choice['label']}: {e}")


# === Question 231 ===
question231 = Question.objects.create(
    question_text="Which of these roads leads into Mill Lane Manor Nursing home?",
    question_type=Question.SINGLE
)
category_names231 = ["Naas", "Nursing Homes", "Main Roads"]
for name in category_names231:
    try:
        cat = Category.objects.get(name=name)
        question231.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices231 = [
    {"text": "Poker Drive", "label": "A", "is_correct": False},
    {"text": "Millbridge", "label": "B", "is_correct": False},
    {"text": "The Sycamores", "label": "C", "is_correct": False},
    {"text": "Ashgrove Drive", "label": "D", "is_correct": True},
]
for choice in choices231:
    try:
        Choice.objects.create(
            question=question231,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q231] Failed to create choice {choice['label']}: {e}")


# === Question 232 ===
question232 = Question.objects.create(
    question_text="What road houses Craddock Nursing home?",
    question_type=Question.SINGLE
)
category_names232 = ["Naas", "Nursing Homes", "Main Roads"]
for name in category_names232:
    try:
        cat = Category.objects.get(name=name)
        question232.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices232 = [
    {"text": "Longstone", "label": "A", "is_correct": False},
    {"text": "Blessington Road", "label": "B", "is_correct": False},
    {"text": "Oak Glade Close", "label": "C", "is_correct": False},
    {"text": "Craddockstown road", "label": "D", "is_correct": True},
]
for choice in choices232:
    try:
        Choice.objects.create(
            question=question232,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q232] Failed to create choice {choice['label']}: {e}")


# === Question 233 ===
question233 = Question.objects.create(
    question_text="Name the road that Beechpark Nursing home is situated on",
    question_type=Question.SINGLE
)
category_names233 = ["Kildare (Town)", "Nursing Homes", "Main Roads"]
for name in category_names233:
    try:
        cat = Category.objects.get(name=name)
        question233.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices233 = [
    {"text": "Green Road", "label": "A", "is_correct": False},
    {"text": "Dunmurray Road", "label": "B", "is_correct": True},
    {"text": "Southgreen Road", "label": "C", "is_correct": False},
    {"text": "Rathbride Road", "label": "D", "is_correct": False},
]
for choice in choices233:
    try:
        Choice.objects.create(
            question=question233,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q233] Failed to create choice {choice['label']}: {e}")


# === Question 234 ===
question234 = Question.objects.create(
    question_text="Lourdesville Nursing home can be found where?",
    question_type=Question.SINGLE
)
category_names234 = ["Kildare (Town)", "Nursing Homes", "Main Roads"]
for name in category_names234:
    try:
        cat = Category.objects.get(name=name)
        question234.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices234 = [
    {"text": "Meadowncourt", "label": "A", "is_correct": False},
    {"text": "Tully Road", "label": "B", "is_correct": True},
    {"text": "Dunmurray", "label": "C", "is_correct": False},
    {"text": "Athy Road", "label": "D", "is_correct": False},
]
for choice in choices234:
    try:
        Choice.objects.create(
            question=question234,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q234] Failed to create choice {choice['label']}: {e}")


# === Question 235 ===
question235 = Question.objects.create(
    question_text="Name the street that Ashley Lodge Nursing home can be located",
    question_type=Question.SINGLE
)
category_names235 = ["Kildare (Town)", "Nursing Homes", "Main Roads"]
for name in category_names235:
    try:
        cat = Category.objects.get(name=name)
        question235.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices235 = [
    {"text": "Rathbride Road", "label": "A", "is_correct": False},
    {"text": "Grey Abbey Road", "label": "B", "is_correct": False},
    {"text": "Melitta Road", "label": "C", "is_correct": False},
    {"text": "Tully Road", "label": "D", "is_correct": True},
]
for choice in choices235:
    try:
        Choice.objects.create(
            question=question235,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q235] Failed to create choice {choice['label']}: {e}")


# === Question 236 ===
question236 = Question.objects.create(
    question_text="Where can Oghill Nursing home be found?",
    question_type=Question.SINGLE
)
category_names236 = ["Monasterevin", "Nursing Homes"]
for name in category_names236:
    try:
        cat = Category.objects.get(name=name)
        question236.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices236 = [
    {"text": "Monasterevin", "label": "A", "is_correct": True},
    {"text": "Naas", "label": "B", "is_correct": False},
    {"text": "Newbridge", "label": "C", "is_correct": False},
    {"text": "Athy", "label": "D", "is_correct": False},
]
for choice in choices236:
    try:
        Choice.objects.create(
            question=question236,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q236] Failed to create choice {choice['label']}: {e}")


# === Question 237 ===
question237 = Question.objects.create(
    question_text="The Elm Hall Nursing home is situated where?",
    question_type=Question.SINGLE
)
category_names237 = ["Celbridge", "Nursing Homes", "Main Roads"]
for name in category_names237:
    try:
        cat = Category.objects.get(name=name)
        question237.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices237 = [
    {"text": "The Grove", "label": "A", "is_correct": False},
    {"text": "Loughlinstown Road", "label": "B", "is_correct": False},
    {"text": "Dublin Road", "label": "C", "is_correct": True},
    {"text": "Tubber Lane Road", "label": "D", "is_correct": False},
]
for choice in choices237:
    try:
        Choice.objects.create(
            question=question237,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q237] Failed to create choice {choice['label']}: {e}")


# === Question 238 ===
question238 = Question.objects.create(
    question_text="Where can one find the Glenashling Nursing home?",
    question_type=Question.SINGLE
)
category_names238 = ["Celbridge", "Nursing Homes", "Minor Roads"]
for name in category_names238:
    try:
        cat = Category.objects.get(name=name)
        question238.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices238 = [
    {"text": "Dara Court", "label": "A", "is_correct": False},
    {"text": "Newtown Road", "label": "B", "is_correct": False},
    {"text": "St. Raphael's Avenue", "label": "C", "is_correct": True},
    {"text": "Oldtown Mill Road", "label": "D", "is_correct": False},
]
for choice in choices238:
    try:
        Choice.objects.create(
            question=question238,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q238] Failed to create choice {choice['label']}: {e}")


# === Question 239 ===
question239 = Question.objects.create(
    question_text="Where is the Clover lodge Nursing home located?",
    question_type=Question.SINGLE
)
category_names239 = ["Athy", "Nursing Homes", "Main Roads"]
for name in category_names239:
    try:
        cat = Category.objects.get(name=name)
        question239.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices239 = [
    {"text": "Moneen Lane", "label": "A", "is_correct": False},
    {"text": "Rockfield Road", "label": "B", "is_correct": False},
    {"text": "Mount Hawkins", "label": "C", "is_correct": False},
    {"text": "Woodstock Street", "label": "D", "is_correct": True},
]
for choice in choices239:
    try:
        Choice.objects.create(
            question=question239,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q239] Failed to create choice {choice['label']}: {e}")


# === Question 240 ===
question240 = Question.objects.create(
    question_text="Where in Naas can the Odeon Cinema be Located in?",
    question_type=Question.SINGLE
)
category_names240 = ["Naas", "Cinemas and Theatres", "Main Roads"]
for name in category_names240:
    try:
        cat = Category.objects.get(name=name)
        question240.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices240 = [
    {"text": "Woodlands", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": False},
    {"text": "Canal Bank", "label": "C", "is_correct": False},
    {"text": "Monread Road", "label": "D", "is_correct": True},
]
for choice in choices240:
    try:
        Choice.objects.create(
            question=question240,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q240] Failed to create choice {choice['label']}: {e}")


# === Question 241 ===
question241 = Question.objects.create(
    question_text="Where can you find the Moat Theatre situated in Naas?",
    question_type=Question.SINGLE
)
category_names241 = ["Naas", "Cinemas and Theatres", "Main Roads"]
for name in category_names241:
    try:
        cat = Category.objects.get(name=name)
        question241.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices241 = [
    {"text": "Canal Bank", "label": "A", "is_correct": False},
    {"text": "Rathasker Road", "label": "B", "is_correct": False},
    {"text": "Abbey Road", "label": "C", "is_correct": True},
    {"text": "Limerick Road", "label": "D", "is_correct": False},
]
for choice in choices241:
    try:
        Choice.objects.create(
            question=question241,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q241] Failed to create choice {choice['label']}: {e}")


# === Question 242 ===
question242 = Question.objects.create(
    question_text="The Odeon Cinema is located where in Newbridge?",
    question_type=Question.SINGLE
)
category_names242 = ["Newbridge", "Cinemas and Theatres", "Shopping Centres and Retail Parks"]
for name in category_names242:
    try:
        cat = Category.objects.get(name=name)
        question242.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices242 = [
    {"text": "Henry Road", "label": "A", "is_correct": False},
    {"text": "Whitewater shopping centre", "label": "B", "is_correct": True},
    {"text": "Liffey View", "label": "C", "is_correct": False},
    {"text": "Moorefield Road", "label": "D", "is_correct": False},
]
for choice in choices242:
    try:
        Choice.objects.create(
            question=question242,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q242] Failed to create choice {choice['label']}: {e}")


# === Question 243 ===
question243 = Question.objects.create(
    question_text="Where can you find the Manor Mills shopping centre in Maynooth?",
    question_type=Question.SINGLE
)
category_names243 = ["Maynooth", "Shopping Centres and Retail Parks", "Main Roads"]
for name in category_names243:
    try:
        cat = Category.objects.get(name=name)
        question243.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices243 = [
    {"text": "Rockfield Avenue", "label": "A", "is_correct": False},
    {"text": "Dunboyne Road", "label": "B", "is_correct": False},
    {"text": "Carton Road", "label": "C", "is_correct": False},
    {"text": "Mill Street", "label": "D", "is_correct": True},
]
for choice in choices243:
    try:
        Choice.objects.create(
            question=question243,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q243] Failed to create choice {choice['label']}: {e}")


# === Question 244 ===
question244 = Question.objects.create(
    question_text="Which of these roads leads into Monread shopping centre located in Naas?",
    question_type=Question.SINGLE
)
category_names244 = ["Naas", "Shopping Centres and Retail Parks", "Main Roads"]
for name in category_names244:
    try:
        cat = Category.objects.get(name=name)
        question244.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices244 = [
    {"text": "Sallins Road", "label": "A", "is_correct": False},
    {"text": "Monread Road", "label": "B", "is_correct": True},
    {"text": "Millenium Park", "label": "C", "is_correct": False},
    {"text": "Osberstown Road", "label": "D", "is_correct": False},
]
for choice in choices244:
    try:
        Choice.objects.create(
            question=question244,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q244] Failed to create choice {choice['label']}: {e}")


# === Question 245 ===
question245 = Question.objects.create(
    question_text="Where can you find the Naas town centre?",
    question_type=Question.SINGLE
)
category_names245 = ["Naas", "Shopping Centres and Retail Parks", "Main Roads"]
for name in category_names245:
    try:
        cat = Category.objects.get(name=name)
        question245.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices245 = [
    {"text": "Woodlands", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": False},
    {"text": "Tipper Road", "label": "C", "is_correct": False},
    {"text": "Sallins Road", "label": "D", "is_correct": True},
]
for choice in choices245:
    try:
        Choice.objects.create(
            question=question245,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q245] Failed to create choice {choice['label']}: {e}")


# === Question 246 ===
question246 = Question.objects.create(
    question_text="Where is the Whitewater Shopping centre located in Newbridge?",
    question_type=Question.SINGLE
)
category_names246 = ["Newbridge", "Shopping Centres and Retail Parks", "Minor Roads"]
for name in category_names246:
    try:
        cat = Category.objects.get(name=name)
        question246.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices246 = [
    {"text": "Cutlery Road", "label": "A", "is_correct": False},
    {"text": "The Grange", "label": "B", "is_correct": False},
    {"text": "College Grove", "label": "C", "is_correct": False},
    {"text": "Hawthorn Close", "label": "D", "is_correct": True},
]
for choice in choices246:
    try:
        Choice.objects.create(
            question=question246,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q246] Failed to create choice {choice['label']}: {e}")


# === Question 247 ===
question247 = Question.objects.create(
    question_text="Where is Kildare village located in Kildare?",
    question_type=Question.SINGLE
)
category_names247 = ["Kildare (Town)", "Shopping Centres and Retail Parks", "Main Roads"]
for name in category_names247:
    try:
        cat = Category.objects.get(name=name)
        question247.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices247 = [
    {"text": "Green Road", "label": "A", "is_correct": False},
    {"text": "Nurney Road", "label": "B", "is_correct": True},
    {"text": "Market Square", "label": "C", "is_correct": False},
    {"text": "Monasterevin Road", "label": "D", "is_correct": False},
]
for choice in choices247:
    try:
        Choice.objects.create(
            question=question247,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q247] Failed to create choice {choice['label']}: {e}")


# === Question 248 ===
question248 = Question.objects.create(
    question_text="What road is Clane Rugby FC found?",
    question_type=Question.SINGLE
)
category_names248 = ["Clane", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names248:
    try:
        cat = Category.objects.get(name=name)
        question248.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices248 = [
    {"text": "College Wood Manor", "label": "A", "is_correct": False},
    {"text": "Central Park", "label": "B", "is_correct": False},
    {"text": "Park View", "label": "C", "is_correct": False},
    {"text": "Ballinagappa Road", "label": "D", "is_correct": True},
]
for choice in choices248:
    try:
        Choice.objects.create(
            question=question248,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q248] Failed to create choice {choice['label']}: {e}")


# === Question 249 ===
question249 = Question.objects.create(
    question_text="Where can Clane GAA club be found?",
    question_type=Question.SINGLE
)
category_names249 = ["Clane", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names249:
    try:
        cat = Category.objects.get(name=name)
        question249.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices249 = [
    {"text": "College Road", "label": "A", "is_correct": False},
    {"text": "Clane Relief Road", "label": "B", "is_correct": False},
    {"text": "Prosperous Road", "label": "C", "is_correct": True},
    {"text": "Millicent Road", "label": "D", "is_correct": False},
]
for choice in choices249:
    try:
        Choice.objects.create(
            question=question249,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q249] Failed to create choice {choice['label']}: {e}")


# === Question 250 ===
question250 = Question.objects.create(
    question_text="Millicent Golf Club is located on what road?",
    question_type=Question.SINGLE
)
category_names250 = ["Clane", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names250:
    try:
        cat = Category.objects.get(name=name)
        question250.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices250 = [
    {"text": "Millicent Road", "label": "A", "is_correct": True},
    {"text": "Ballinagappa Road", "label": "B", "is_correct": False},
    {"text": "Sallins Link Road", "label": "C", "is_correct": False},
    {"text": "Prosperous Road", "label": "D", "is_correct": False},
]
for choice in choices250:
    try:
        Choice.objects.create(
            question=question250,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q250] Failed to create choice {choice['label']}: {e}")


# === Question 251 ===
question251 = Question.objects.create(
    question_text="Clongowes Golf Club is accessed by what main road?",
    question_type=Question.SINGLE
)
category_names251 = ["Clane", "Sports Clubs and Leisure Facilities", "Road Numbers"]
for name in category_names251:
    try:
        cat = Category.objects.get(name=name)
        question251.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices251 = [
    {"text": "R406", "label": "A", "is_correct": False},
    {"text": "R403", "label": "B", "is_correct": False},
    {"text": "R407", "label": "C", "is_correct": True},
    {"text": "R408", "label": "D", "is_correct": False},
]
for choice in choices251:
    try:
        Choice.objects.create(
            question=question251,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q251] Failed to create choice {choice['label']}: {e}")


# === Question 252 ===
question252 = Question.objects.create(
    question_text="Which of these roads connects Naas to Kilcullen?",
    question_type=Question.SINGLE
)
category_names252 = ["Naas", "Kilcullen", "Routes from This Area to Another", "Road Numbers"]
for name in category_names252:
    try:
        cat = Category.objects.get(name=name)
        question252.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices252 = [
    {"text": "R409", "label": "A", "is_correct": False},
    {"text": "R445", "label": "B", "is_correct": False},
    {"text": "R448", "label": "C", "is_correct": True},
    {"text": "R148", "label": "D", "is_correct": False},
]
for choice in choices252:
    try:
        Choice.objects.create(
            question=question252,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q252] Failed to create choice {choice['label']}: {e}")


# === Question 253 ===
question253 = Question.objects.create(
    question_text="Punchestown Racecourse is found off which main road?",
    question_type=Question.SINGLE
)
category_names253 = ["Naas", "Racecourses", "Road Numbers"]
for name in category_names253:
    try:
        cat = Category.objects.get(name=name)
        question253.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices253 = [
    {"text": "R448", "label": "A", "is_correct": False},
    {"text": "R413", "label": "B", "is_correct": False},
    {"text": "R412", "label": "C", "is_correct": False},
    {"text": "R411", "label": "D", "is_correct": True},
]
for choice in choices253:
    try:
        Choice.objects.create(
            question=question253,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q253] Failed to create choice {choice['label']}: {e}")


# === Question 254 ===
question254 = Question.objects.create(
    question_text="Off what road can Naas Racecourse be found?",
    question_type=Question.SINGLE
)
category_names254 = ["Naas", "Racecourses", "Main Roads"]
for name in category_names254:
    try:
        cat = Category.objects.get(name=name)
        question254.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices254 = [
    {"text": "Friary Road", "label": "A", "is_correct": False},
    {"text": "Blessington Road", "label": "B", "is_correct": False},
    {"text": "Tipper Road", "label": "C", "is_correct": True},
    {"text": "Ballymore Road", "label": "D", "is_correct": False},
]
for choice in choices254:
    try:
        Choice.objects.create(
            question=question254,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q254] Failed to create choice {choice['label']}: {e}")


# === Question 255 ===
question255 = Question.objects.create(
    question_text="Where can Osprey Leisure Club be found?",
    question_type=Question.SINGLE
)
category_names255 = ["Naas", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names255:
    try:
        cat = Category.objects.get(name=name)
        question255.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices255 = [
    {"text": "Rathasker Road", "label": "A", "is_correct": False},
    {"text": "Corban's Lane", "label": "B", "is_correct": False},
    {"text": "St Michaels's Terrace", "label": "C", "is_correct": False},
    {"text": "Devoy Quarter", "label": "D", "is_correct": True},
]
for choice in choices255:
    try:
        Choice.objects.create(
            question=question255,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q255] Failed to create choice {choice['label']}: {e}")


# === Question 256 ===
question256 = Question.objects.create(
    question_text="Leixlip Amenities Sports Centre is found on what road?",
    question_type=Question.SINGLE
)
category_names256 = ["Leixlip", "Sports Clubs and Leisure Facilities", "Road Numbers"]
for name in category_names256:
    try:
        cat = Category.objects.get(name=name)
        question256.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices256 = [
    {"text": "R148", "label": "A", "is_correct": False},
    {"text": "M4", "label": "B", "is_correct": False},
    {"text": "R405", "label": "C", "is_correct": False},
    {"text": "R449", "label": "D", "is_correct": True},
]
for choice in choices256:
    try:
        Choice.objects.create(
            question=question256,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q256] Failed to create choice {choice['label']}: {e}")


# === Question 257 ===
question257 = Question.objects.create(
    question_text="Where can Leixlip GAA club be found?",
    question_type=Question.SINGLE
)
category_names257 = ["Leixlip", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names257:
    try:
        cat = Category.objects.get(name=name)
        question257.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices257 = [
    {"text": "Green Lane", "label": "A", "is_correct": False},
    {"text": "Celbridge Road", "label": "B", "is_correct": False},
    {"text": "Station Road", "label": "C", "is_correct": False},
    {"text": "Accommodation Road", "label": "D", "is_correct": True},
]
for choice in choices257:
    try:
        Choice.objects.create(
            question=question257,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q257] Failed to create choice {choice['label']}: {e}")


# === Question 258 ===
question258 = Question.objects.create(
    question_text="The Newbridge Greyhound Stadium can be found off which main road?",
    question_type=Question.SINGLE
)
category_names258 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Road Numbers"]
for name in category_names258:
    try:
        cat = Category.objects.get(name=name)
        question258.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices258 = [
    {"text": "R401", "label": "A", "is_correct": False},
    {"text": "R445", "label": "B", "is_correct": False},
    {"text": "R415", "label": "C", "is_correct": True},
    {"text": "R416", "label": "D", "is_correct": False},
]
for choice in choices258:
    try:
        Choice.objects.create(
            question=question258,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q258] Failed to create choice {choice['label']}: {e}")


# === Question 259 ===
question259 = Question.objects.create(
    question_text="Where is the entrance to Sarsfield GAA club located?",
    question_type=Question.SINGLE
)
category_names259 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names259:
    try:
        cat = Category.objects.get(name=name)
        question259.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices259 = [
    {"text": "Dawson Street", "label": "A", "is_correct": False},
    {"text": "Roseberry Hill", "label": "B", "is_correct": False},
    {"text": "Morristown Road", "label": "C", "is_correct": False},
    {"text": "Henry Street", "label": "D", "is_correct": True},
]
for choice in choices259:
    try:
        Choice.objects.create(
            question=question259,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q259] Failed to create choice {choice['label']}: {e}")


# === Question 260 ===
question260 = Question.objects.create(
    question_text="Where is the entrance to St. Conleth's GAA Park located?",
    question_type=Question.SINGLE
)
category_names260 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names260:
    try:
        cat = Category.objects.get(name=name)
        question260.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices260 = [
    {"text": "Eyre Street", "label": "A", "is_correct": False},
    {"text": "Liffey View", "label": "B", "is_correct": False},
    {"text": "Cutlery Road", "label": "C", "is_correct": False},
    {"text": "Athgarvan Road", "label": "D", "is_correct": True},
]
for choice in choices260:
    try:
        Choice.objects.create(
            question=question260,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q260] Failed to create choice {choice['label']}: {e}")


# === Question 261 ===
question261 = Question.objects.create(
    question_text="The Ryston Sports & Social Club is located on what road?",
    question_type=Question.SINGLE
)
category_names261 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names261:
    try:
        cat = Category.objects.get(name=name)
        question261.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices261 = [
    {"text": "Main Street", "label": "A", "is_correct": False},
    {"text": "Athgarvan Road", "label": "B", "is_correct": True},
    {"text": "Langton Road", "label": "C", "is_correct": False},
    {"text": "Curragh Grange", "label": "D", "is_correct": False},
]
for choice in choices261:
    try:
        Choice.objects.create(
            question=question261,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q261] Failed to create choice {choice['label']}: {e}")


# === Question 262 ===
question262 = Question.objects.create(
    question_text="The Curragh Racecourse can be found off which main road?",
    question_type=Question.SINGLE
)
category_names262 = ["Curragh", "Racecourses", "Road Numbers"]
for name in category_names262:
    try:
        cat = Category.objects.get(name=name)
        question262.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices262 = [
    {"text": "R445", "label": "A", "is_correct": True},
    {"text": "R415", "label": "B", "is_correct": False},
    {"text": "R401", "label": "C", "is_correct": False},
    {"text": "R413", "label": "D", "is_correct": False},
]
for choice in choices262:
    try:
        Choice.objects.create(
            question=question262,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q262] Failed to create choice {choice['label']}: {e}")


# === Question 263 ===
question263 = Question.objects.create(
    question_text="KLeisure in Newbridge can be found on what road?",
    question_type=Question.SINGLE
)
category_names263 = ["Newbridge", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names263:
    try:
        cat = Category.objects.get(name=name)
        question263.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices263 = [
    {"text": "College Park Road", "label": "A", "is_correct": False},
    {"text": "Henry Road", "label": "B", "is_correct": False},
    {"text": "Station Road", "label": "C", "is_correct": True},
    {"text": "Athgarvan Road", "label": "D", "is_correct": False},
]
for choice in choices263:
    try:
        Choice.objects.create(
            question=question263,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q263] Failed to create choice {choice['label']}: {e}")


# === Question 264 ===
question264 = Question.objects.create(
    question_text="Round Towers GAA Club can be found off what road?",
    question_type=Question.SINGLE
)
category_names264 = ["Kildare (Town)", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names264:
    try:
        cat = Category.objects.get(name=name)
        question264.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices264 = [
    {"text": "Rathbride Road", "label": "A", "is_correct": True},
    {"text": "Fire Castle Lane", "label": "B", "is_correct": False},
    {"text": "Old Road", "label": "C", "is_correct": False},
    {"text": "Melitta Road", "label": "D", "is_correct": False},
]
for choice in choices264:
    try:
        Choice.objects.create(
            question=question264,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q264] Failed to create choice {choice['label']}: {e}")


# === Question 265 ===
question265 = Question.objects.create(
    question_text="Off what road is St. Brigid's Boxing club located?",
    question_type=Question.SINGLE
)
category_names265 = ["Kildare (Town)", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names265:
    try:
        cat = Category.objects.get(name=name)
        question265.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices265 = [
    {"text": "Connagh Road", "label": "A", "is_correct": False},
    {"text": "Melitta Road", "label": "B", "is_correct": False},
    {"text": "Bride Street", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": True},
]
for choice in choices265:
    try:
        Choice.objects.create(
            question=question265,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q265] Failed to create choice {choice['label']}: {e}")


# === Question 266 ===
question266 = Question.objects.create(
    question_text="What road can Maynooth GAA Club be found?",
    question_type=Question.SINGLE
)
category_names266 = ["Maynooth", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names266:
    try:
        cat = Category.objects.get(name=name)
        question266.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices266 = [
    {"text": "Dunboyne Road", "label": "A", "is_correct": False},
    {"text": "Moyglare Road", "label": "B", "is_correct": True},
    {"text": "Moyglare Abbey", "label": "C", "is_correct": False},
    {"text": "Straffan Road", "label": "D", "is_correct": False},
]
for choice in choices266:
    try:
        Choice.objects.create(
            question=question266,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q266] Failed to create choice {choice['label']}: {e}")


# === Question 267 ===
question267 = Question.objects.create(
    question_text="Where can Saint Michael's Boxing Club Athy be found?",
    question_type=Question.SINGLE
)
category_names267 = ["Athy", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names267:
    try:
        cat = Category.objects.get(name=name)
        question267.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices267 = [
    {"text": "Canal Walk", "label": "A", "is_correct": False},
    {"text": "Church Road", "label": "B", "is_correct": False},
    {"text": "Stanhope Street", "label": "C", "is_correct": True},
    {"text": "Rockfield Road", "label": "D", "is_correct": False},
]
for choice in choices267:
    try:
        Choice.objects.create(
            question=question267,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q267] Failed to create choice {choice['label']}: {e}")


# === Question 268 ===
question268 = Question.objects.create(
    question_text="Where can K Leisure Athy be found?",
    question_type=Question.SINGLE
)
category_names268 = ["Athy", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names268:
    try:
        cat = Category.objects.get(name=name)
        question268.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices268 = [
    {"text": "Barrack Lane", "label": "A", "is_correct": False},
    {"text": "Canal Side", "label": "B", "is_correct": False},
    {"text": "William Street", "label": "C", "is_correct": False},
    {"text": "Duke Street", "label": "D", "is_correct": True},
]
for choice in choices268:
    try:
        Choice.objects.create(
            question=question268,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q268] Failed to create choice {choice['label']}: {e}")


# === Question 269 ===
question269 = Question.objects.create(
    question_text="What road is Athy Tennis Club found?",
    question_type=Question.SINGLE
)
category_names269 = ["Athy", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names269:
    try:
        cat = Category.objects.get(name=name)
        question269.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices269 = [
    {"text": "Moyglare Road", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": False},
    {"text": "Mansfield Grove", "label": "C", "is_correct": False},
    {"text": "Marina Court", "label": "D", "is_correct": True},
]
for choice in choices269:
    try:
        Choice.objects.create(
            question=question269,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q269] Failed to create choice {choice['label']}: {e}")


# === Question 270 ===
question270 = Question.objects.create(
    question_text="Off what road can Athy RFC be found?",
    question_type=Question.SINGLE
)
category_names270 = ["Athy", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names270:
    try:
        cat = Category.objects.get(name=name)
        question270.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices270 = [
    {"text": "Geraldine Road", "label": "A", "is_correct": False},
    {"text": "Church Road", "label": "B", "is_correct": False},
    {"text": "Mansfield Grove", "label": "C", "is_correct": False},
    {"text": "Dublin Road", "label": "D", "is_correct": True},
]
for choice in choices270:
    try:
        Choice.objects.create(
            question=question270,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q270] Failed to create choice {choice['label']}: {e}")


# === Question 271 ===
question271 = Question.objects.create(
    question_text="What road is Athy Golf Club found?",
    question_type=Question.SINGLE
)
category_names271 = ["Athy", "Sports Clubs and Leisure Facilities", "Main Roads"]
for name in category_names271:
    try:
        cat = Category.objects.get(name=name)
        question271.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices271 = [
    {"text": "Rockfield Road", "label": "A", "is_correct": False},
    {"text": "Dublin Road", "label": "B", "is_correct": True},
    {"text": "Woodstock Street", "label": "C", "is_correct": False},
    {"text": "Geraldine Road", "label": "D", "is_correct": False},
]
for choice in choices271:
    try:
        Choice.objects.create(
            question=question271,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q271] Failed to create choice {choice['label']}: {e}")


# === Question 272 ===
question272 = Question.objects.create(
    question_text="Our Ladys Nativity church is where in Leixlip?",
    question_type=Question.SINGLE
)
category_names272 = ["Leixlip", "Churches and Cathedrals", "Minor Roads"]
for name in category_names272:
    try:
        cat = Category.objects.get(name=name)
        question272.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices272 = [
    {"text": "Station Road", "label": "A", "is_correct": False},
    {"text": "Forest Park", "label": "B", "is_correct": False},
    {"text": "Green Lane", "label": "C", "is_correct": False},
    {"text": "Celbridge Road", "label": "D", "is_correct": True},
]
for choice in choices272:
    try:
        Choice.objects.create(
            question=question272,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q272] Failed to create choice {choice['label']}: {e}")


# === Question 273 ===
question273 = Question.objects.create(
    question_text="What street is St Charles Borromeo Church housed on in Leixlip",
    question_type=Question.SINGLE
)
category_names273 = ["Leixlip", "Churches and Cathedrals", "Minor Roads"]
for name in category_names273:
    try:
        cat = Category.objects.get(name=name)
        question273.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices273 = [
    {"text": "River Forest", "label": "A", "is_correct": False},
    {"text": "The Walk", "label": "B", "is_correct": False},
    {"text": "Captains Hill", "label": "C", "is_correct": True},
    {"text": "The Grove", "label": "D", "is_correct": False},
]
for choice in choices273:
    try:
        Choice.objects.create(
            question=question273,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q273] Failed to create choice {choice['label']}: {e}")


# === Question 274 ===
question274 = Question.objects.create(
    question_text="St Marys church of Ireland is located where in Leixlip?",
    question_type=Question.SINGLE
)
category_names274 = ["Leixlip", "Churches and Cathedrals", "Main Roads"]
for name in category_names274:
    try:
        cat = Category.objects.get(name=name)
        question274.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices274 = [
    {"text": "Captain's Hill", "label": "A", "is_correct": False},
    {"text": "Main Street", "label": "B", "is_correct": True},
    {"text": "The Black Avenue", "label": "C", "is_correct": False},
    {"text": "Mill Lane", "label": "D", "is_correct": False},
]
for choice in choices274:
    try:
        Choice.objects.create(
            question=question274,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q274] Failed to create choice {choice['label']}: {e}")


# === Question 275 ===
question275 = Question.objects.create(
    question_text="What street is St Marys church of Ireland located on in Maynooth?",
    question_type=Question.SINGLE
)
category_names275 = ["Maynooth", "Churches and Cathedrals", "Main Roads"]
for name in category_names275:
    try:
        cat = Category.objects.get(name=name)
        question275.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices275 = [
    {"text": "Parson Street", "label": "A", "is_correct": True},
    {"text": "Kilcock Road", "label": "B", "is_correct": False},
    {"text": "Moyglare Road", "label": "C", "is_correct": False},
    {"text": "Straffan Road", "label": "D", "is_correct": False},
]
for choice in choices275:
    try:
        Choice.objects.create(
            question=question275,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q275] Failed to create choice {choice['label']}: {e}")


# === Question 276 ===
question276 = Question.objects.create(
    question_text="The Naas Presbyterian church can be found where?",
    question_type=Question.SINGLE
)
category_names276 = ["Naas", "Churches and Cathedrals", "Main Roads"]
for name in category_names276:
    try:
        cat = Category.objects.get(name=name)
        question276.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices276 = [
    {"text": "Wolfe Tone Street", "label": "A", "is_correct": True},
    {"text": "The Paddocks", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": False},
    {"text": "Abbey Bridge", "label": "D", "is_correct": False},
]
for choice in choices276:
    try:
        Choice.objects.create(
            question=question276,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q276] Failed to create choice {choice['label']}: {e}")


# === Question 277 ===
question277 = Question.objects.create(
    question_text="Name the road that St. Davids church can be found on in Naas",
    question_type=Question.SINGLE
)
category_names277 = ["Naas", "Churches and Cathedrals", "Main Roads"]
for name in category_names277:
    try:
        cat = Category.objects.get(name=name)
        question277.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices277 = [
    {"text": "Sarto Road", "label": "A", "is_correct": False},
    {"text": "St Martin's Avenue", "label": "B", "is_correct": False},
    {"text": "Main Street", "label": "C", "is_correct": True},
    {"text": "Abbey Road", "label": "D", "is_correct": False},
]
for choice in choices277:
    try:
        Choice.objects.create(
            question=question277,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q277] Failed to create choice {choice['label']}: {e}")


# === Question 278 ===
question278 = Question.objects.create(
    question_text="Where is the church of Our Lady and St David found in Naas?",
    question_type=Question.SINGLE
)
category_names278 = ["Naas", "Churches and Cathedrals", "Main Roads"]
for name in category_names278:
    try:
        cat = Category.objects.get(name=name)
        question278.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices278 = [
    {"text": "Lakelands", "label": "A", "is_correct": False},
    {"text": "Ballymore Road", "label": "B", "is_correct": False},
    {"text": "Sallins Road", "label": "C", "is_correct": True},
    {"text": "Friary Road", "label": "D", "is_correct": False},
]
for choice in choices278:
    try:
        Choice.objects.create(
            question=question278,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q278] Failed to create choice {choice['label']}: {e}")


# === Question 279 ===
question279 = Question.objects.create(
    question_text="Where can you find the Church of the Irish Martyrs located in Naas?",
    question_type=Question.SINGLE
)
category_names279 = ["Naas", "Churches and Cathedrals", "Main Roads"]
for name in category_names279:
    try:
        cat = Category.objects.get(name=name)
        question279.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices279 = [
    {"text": "Ballycane Road", "label": "A", "is_correct": True},
    {"text": "Stoneleigh", "label": "B", "is_correct": False},
    {"text": "Blessington Road", "label": "C", "is_correct": False},
    {"text": "Glynn", "label": "D", "is_correct": False},
]
for choice in choices279:
    try:
        Choice.objects.create(
            question=question279,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q279] Failed to create choice {choice['label']}: {e}")


# === Question 280 ===
question280 = Question.objects.create(
    question_text="St Conleths Church is located where in Newbridge?",
    question_type=Question.SINGLE
)
category_names280 = ["Newbridge", "Churches and Cathedrals", "Minor Roads"]
for name in category_names280:
    try:
        cat = Category.objects.get(name=name)
        question280.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices280 = [
    {"text": "Old Connell", "label": "A", "is_correct": False},
    {"text": "Naas Road", "label": "B", "is_correct": False},
    {"text": "The Priory", "label": "C", "is_correct": False},
    {"text": "Mount Carmel", "label": "D", "is_correct": True},
]
for choice in choices280:
    try:
        Choice.objects.create(
            question=question280,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q280] Failed to create choice {choice['label']}: {e}")


# === Question 281 ===
question281 = Question.objects.create(
    question_text="Where is the St: Brigids Parish church located in Kildare?",
    question_type=Question.SINGLE
)
category_names281 = ["Kildare (Town)", "Churches and Cathedrals", "Main Roads"]
for name in category_names281:
    try:
        cat = Category.objects.get(name=name)
        question281.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices281 = [
    {"text": "Oaktree Avenue", "label": "A", "is_correct": False},
    {"text": "Pigeon Lane", "label": "B", "is_correct": False},
    {"text": "Curragh Road", "label": "C", "is_correct": False},
    {"text": "Bride Street", "label": "D", "is_correct": True},
]
for choice in choices281:
    try:
        Choice.objects.create(
            question=question281,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q281] Failed to create choice {choice['label']}: {e}")


# === Question 282 ===
question282 = Question.objects.create(
    question_text="Pick the road on which St. Brigids Cathedral is housed on in Kildare",
    question_type=Question.SINGLE
)
category_names282 = ["Kildare (Town)", "Churches and Cathedrals", "Main Roads"]
for name in category_names282:
    try:
        cat = Category.objects.get(name=name)
        question282.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices282 = [
    {"text": "Market Square", "label": "A", "is_correct": True},
    {"text": "Maryville", "label": "B", "is_correct": False},
    {"text": "Drumcree Court", "label": "C", "is_correct": False},
    {"text": "Priests Lane", "label": "D", "is_correct": False},
]
for choice in choices282:
    try:
        Choice.objects.create(
            question=question282,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q282] Failed to create choice {choice['label']}: {e}")


# === Question 283 ===
question283 = Question.objects.create(
    question_text="Pick the road that houses Carmelite friary church in Kildare.",
    question_type=Question.SINGLE
)
category_names283 = ["Kildare (Town)", "Churches and Cathedrals", "Main Roads"]
for name in category_names283:
    try:
        cat = Category.objects.get(name=name)
        question283.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices283 = [
    {"text": "Station View", "label": "A", "is_correct": False},
    {"text": "Green Road", "label": "B", "is_correct": False},
    {"text": "Chapel Lane", "label": "C", "is_correct": False},
    {"text": "Melitta Road", "label": "D", "is_correct": True},
]
for choice in choices283:
    try:
        Choice.objects.create(
            question=question283,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q283] Failed to create choice {choice['label']}: {e}")


# === Question 284 ===
question284 = Question.objects.create(
    question_text="Athy Presbyterian Church is housed on which of these roads?",
    question_type=Question.SINGLE
)
category_names284 = ["Athy", "Churches and Cathedrals", "Main Roads"]
for name in category_names284:
    try:
        cat = Category.objects.get(name=name)
        question284.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices284 = [
    {"text": "Dublin Road", "label": "A", "is_correct": True},
    {"text": "Cyprian Road", "label": "B", "is_correct": False},
    {"text": "Barrow Way", "label": "C", "is_correct": False},
    {"text": "Kiingsgrove", "label": "D", "is_correct": False},
]
for choice in choices284:
    try:
        Choice.objects.create(
            question=question284,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q284] Failed to create choice {choice['label']}: {e}")


# === Question 285 ===
question285 = Question.objects.create(
    question_text="The Athy Methodist Church is situated on what road?",
    question_type=Question.SINGLE
)
category_names285 = ["Athy", "Churches and Cathedrals", "Main Roads"]
for name in category_names285:
    try:
        cat = Category.objects.get(name=name)
        question285.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices285 = [
    {"text": "Rockfield", "label": "A", "is_correct": False},
    {"text": "Castle Park", "label": "B", "is_correct": False},
    {"text": "St Dominic's Park", "label": "C", "is_correct": False},
    {"text": "Woodstock Street", "label": "D", "is_correct": True},
]
for choice in choices285:
    try:
        Choice.objects.create(
            question=question285,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q285] Failed to create choice {choice['label']}: {e}")


# === Question 286 ===
question286 = Question.objects.create(
    question_text="Where is the St Michaels church located in Athy?",
    question_type=Question.SINGLE
)
category_names286 = ["Athy", "Churches and Cathedrals", "Main Roads"]
for name in category_names286:
    try:
        cat = Category.objects.get(name=name)
        question286.categories.add(cat)
    except Category.DoesNotExist:
        print(f"Category '{name}' not found in DB")
choices286 = [
    {"text": "White Castle Lawn", "label": "A", "is_correct": False},
    {"text": "Stanhope Street", "label": "B", "is_correct": True},
    {"text": "Convent View", "label": "C", "is_correct": False},
    {"text": "Church Road", "label": "D", "is_correct": False},
]
for choice in choices286:
    try:
        Choice.objects.create(
            question=question286,
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q286] Failed to create choice {choice['label']}: {e}")


print("✅ All questions created successfully.")
## cd /d "g:\MyCode\App Taxi Exam" && python manage.py shell < create_questions_all.py
## cd /d "g:\MyCode\App Taxi Exam" && python manage.py shell < create_question.py
## cd /d "g:\MyCode\App Taxi Exam" && python manage.py shell < create_questions_all_fix.py
## cd /d "g:\MyCode\App Taxi Exam" && python manage.py shell < reset_question_ids.py

## # First, reset the IDs
# python manage.py shell < reset_question_ids.py

# Then create a test question to verify IDs start from 1
# python manage.py shell < verify_id_reset.py