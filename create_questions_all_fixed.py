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
        print(f"Category '{name}' not found in DB")
choices1 = [
    {"text": "Clane and Prosperous", "label": "A", "is_correct": True},
    {"text": "Maynooth and Kilcock", "label": "B", "is_correct": False},
    {"text": "Maynooth and Rathcoffee", "label": "C", "is_correct": False},
    {"text": "Lexlip and Maynooth", "label": "D", "is_correct": False},
]
for choice_data in choices1:
    Choice.objects.create(question=question1, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question1.save()

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
        print(f"Category '{name}' not found in DB")
choices2 = [
    {"text": "Green Rd", "label": "A", "is_correct": True},
    {"text": "Langton Park", "label": "B", "is_correct": False},
    {"text": "Dublin Rd", "label": "C", "is_correct": False},
    {"text": "Ballymany", "label": "D", "is_correct": False},
]
for choice_data in choices2:
    Choice.objects.create(question=question2, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question2.save()

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
        print(f"Category '{name}' not found in DB")
choices3 = [
    {"text": "Sallins Rd", "label": "A", "is_correct": True},
    {"text": "Dublin Rd", "label": "B", "is_correct": False},
    {"text": "Maudlins Ave", "label": "C", "is_correct": False},
    {"text": "Monread Road", "label": "D", "is_correct": False},
]
for choice_data in choices3:
    Choice.objects.create(question=question3, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question3.save()

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
for choice_data in choices4:
    Choice.objects.create(question=question4, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question4.save()

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
for choice_data in choices5:
    Choice.objects.create(question=question5, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question5.save()

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
for choice_data in choices6:
    Choice.objects.create(question=question6, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question6.save()

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
for choice_data in choices7:
    Choice.objects.create(question=question7, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question7.save()

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
for choice_data in choices8:
    Choice.objects.create(question=question8, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question8.save()

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
for choice_data in choices9:
    Choice.objects.create(question=question9, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question9.save()

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
for choice_data in choices10:
    Choice.objects.create(question=question10, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question10.save()

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
for choice_data in choices11:
    Choice.objects.create(question=question11, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question11.save()

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
for choice_data in choices12:
    Choice.objects.create(question=question12, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question12.save()

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
for choice_data in choices13:
    Choice.objects.create(question=question13, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question13.save()

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
for choice_data in choices14:
    Choice.objects.create(question=question14, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question14.save()

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
for choice_data in choices15:
    Choice.objects.create(question=question15, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question15.save()

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
for choice_data in choices16:
    Choice.objects.create(question=question16, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question16.save()

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
for choice_data in choices17:
    Choice.objects.create(question=question17, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question17.save()

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
for choice_data in choices18:
    Choice.objects.create(question=question18, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question18.save()

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
for choice_data in choices19:
    Choice.objects.create(question=question19, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question19.save()

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
for choice_data in choices20:
    Choice.objects.create(question=question20, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question20.save()

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
for choice_data in choices21:
    Choice.objects.create(question=question21, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question21.save()

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
for choice_data in choices22:
    Choice.objects.create(question=question22, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question22.save()

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
for choice_data in choices23:
    Choice.objects.create(question=question23, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question23.save()

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
for choice_data in choices24:
    Choice.objects.create(question=question24, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question24.save()

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
for choice_data in choices25:
    Choice.objects.create(question=question25, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question25.save()

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
for choice_data in choices26:
    Choice.objects.create(question=question26, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question26.save()

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
for choice_data in choices27:
    Choice.objects.create(question=question27, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question27.save()

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
for choice_data in choices28:
    Choice.objects.create(question=question28, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question28.save()

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
for choice_data in choices29:
    Choice.objects.create(question=question29, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question29.save()

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
for choice_data in choices30:
    Choice.objects.create(question=question30, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question30.save()

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
for choice_data in choices31:
    Choice.objects.create(question=question31, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question31.save()

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
for choice_data in choices32:
    Choice.objects.create(question=question32, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question32.save()

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
for choice_data in choices33:
    Choice.objects.create(question=question33, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question33.save()

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
for choice_data in choices34:
    Choice.objects.create(question=question34, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question34.save()

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
for choice_data in choices35:
    Choice.objects.create(question=question35, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question35.save()

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
for choice_data in choices36:
    Choice.objects.create(question=question36, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question36.save()

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
for choice_data in choices37:
    Choice.objects.create(question=question37, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question37.save()

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
for choice_data in choices38:
    Choice.objects.create(question=question38, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question38.save()

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
for choice_data in choices39:
    Choice.objects.create(question=question39, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question39.save()

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
for choice_data in choices40:
    Choice.objects.create(question=question40, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question40.save()

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
for choice_data in choices41:
    Choice.objects.create(question=question41, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question41.save()

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
for choice_data in choices42:
    Choice.objects.create(question=question42, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question42.save()

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
for choice_data in choices43:
    Choice.objects.create(question=question43, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question43.save()

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
for choice_data in choices44:
    Choice.objects.create(question=question44, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question44.save()

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
for choice_data in choices45:
    Choice.objects.create(question=question45, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question45.save()

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
for choice_data in choices46:
    Choice.objects.create(question=question46, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question46.save()

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
for choice_data in choices47:
    Choice.objects.create(question=question47, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question47.save()

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
for choice_data in choices48:
    Choice.objects.create(question=question48, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question48.save()

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
for choice_data in choices49:
    Choice.objects.create(question=question49, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question49.save()

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
for choice_data in choices50:
    Choice.objects.create(question=question50, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question50.save()

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
for choice_data in choices51:
    Choice.objects.create(question=question51, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question51.save()

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
for choice_data in choices52:
    Choice.objects.create(question=question52, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question52.save()

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
for choice_data in choices53:
    Choice.objects.create(question=question53, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question53.save()

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
for choice_data in choices54:
    Choice.objects.create(question=question54, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question54.save()

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
for choice_data in choices55:
    Choice.objects.create(question=question55, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question55.save()

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
for choice_data in choices56:
    Choice.objects.create(question=question56, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question56.save()

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
for choice_data in choices57:
    Choice.objects.create(question=question57, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question57.save()

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
for choice_data in choices58:
    Choice.objects.create(question=question58, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question58.save()

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
for choice_data in choices59:
    Choice.objects.create(question=question59, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question59.save()

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
for choice_data in choices60:
    Choice.objects.create(question=question60, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question60.save()

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
for choice_data in choices61:
    Choice.objects.create(question=question61, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question61.save()

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
for choice_data in choices62:
    Choice.objects.create(question=question62, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question62.save()

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
for choice_data in choices63:
    Choice.objects.create(question=question63, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question63.save()

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
for choice_data in choices64:
    Choice.objects.create(question=question64, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question64.save()

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
for choice_data in choices65:
    Choice.objects.create(question=question65, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question65.save()

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
for choice_data in choices66:
    Choice.objects.create(question=question66, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question66.save()

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
for choice_data in choices67:
    Choice.objects.create(question=question67, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question67.save()

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
for choice_data in choices68:
    Choice.objects.create(question=question68, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question68.save()

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
for choice_data in choices69:
    Choice.objects.create(question=question69, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question69.save()

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
for choice_data in choices70:
    Choice.objects.create(question=question70, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question70.save()

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
for choice_data in choices71:
    Choice.objects.create(question=question71, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question71.save()

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
for choice_data in choices72:
    Choice.objects.create(question=question72, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question72.save()

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
for choice_data in choices73:
    Choice.objects.create(question=question73, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question73.save()

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
for choice_data in choices74:
    Choice.objects.create(question=question74, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question74.save()

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
for choice_data in choices75:
    Choice.objects.create(question=question75, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question75.save()

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
for choice_data in choices76:
    Choice.objects.create(question=question76, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question76.save()

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
for choice_data in choices77:
    Choice.objects.create(question=question77, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question77.save()

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
for choice_data in choices78:
    Choice.objects.create(question=question78, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question78.save()

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
for choice_data in choices79:
    Choice.objects.create(question=question79, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question79.save()

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
for choice_data in choices80:
    Choice.objects.create(question=question80, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question80.save()

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
for choice_data in choices81:
    Choice.objects.create(question=question81, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question81.save()

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
for choice_data in choices82:
    Choice.objects.create(question=question82, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question82.save()

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
for choice_data in choices83:
    Choice.objects.create(question=question83, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question83.save()

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
for choice_data in choices84:
    Choice.objects.create(question=question84, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question84.save()

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
for choice_data in choices85:
    Choice.objects.create(question=question85, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question85.save()

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
for choice_data in choices86:
    Choice.objects.create(question=question86, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question86.save()

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
for choice_data in choices87:
    Choice.objects.create(question=question87, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question87.save()

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
for choice_data in choices88:
    Choice.objects.create(question=question88, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question88.save()

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
for choice_data in choices89:
    Choice.objects.create(question=question89, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question89.save()

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
for choice_data in choices90:
    Choice.objects.create(question=question90, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question90.save()

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
for choice_data in choices91:
    Choice.objects.create(question=question91, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question91.save()

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
for choice_data in choices92:
    Choice.objects.create(question=question92, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question92.save()

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
for choice_data in choices93:
    Choice.objects.create(question=question93, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question93.save()

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
for choice_data in choices94:
    Choice.objects.create(question=question94, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question94.save()

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
for choice_data in choices95:
    Choice.objects.create(question=question95, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question95.save()

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
for choice_data in choices96:
    Choice.objects.create(question=question96, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question96.save()

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
for choice_data in choices97:
    Choice.objects.create(question=question97, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question97.save()

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
for choice_data in choices98:
    Choice.objects.create(question=question98, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question98.save()

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
for choice_data in choices99:
    Choice.objects.create(question=question99, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question99.save()

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
for choice_data in choices100:
    Choice.objects.create(question=question100, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question100.save()

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
for choice_data in choices101:
    Choice.objects.create(question=question101, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question101.save()

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
for choice_data in choices102:
    Choice.objects.create(question=question102, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question102.save()

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
for choice_data in choices103:
    Choice.objects.create(question=question103, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question103.save()

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
for choice_data in choices104:
    Choice.objects.create(question=question104, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question104.save()

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
for choice_data in choices105:
    Choice.objects.create(question=question105, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question105.save()

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
for choice_data in choices106:
    Choice.objects.create(question=question106, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question106.save()

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
for choice_data in choices107:
    Choice.objects.create(question=question107, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question107.save()

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
for choice_data in choices108:
    Choice.objects.create(question=question108, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question108.save()

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
for choice_data in choices109:
    Choice.objects.create(question=question109, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question109.save()

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
for choice_data in choices110:
    Choice.objects.create(question=question110, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question110.save()

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
for choice_data in choices111:
    Choice.objects.create(question=question111, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question111.save()

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
for choice_data in choices112:
    Choice.objects.create(question=question112, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question112.save()

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
for choice_data in choices113:
    Choice.objects.create(question=question113, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question113.save()

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
for choice_data in choices114:
    Choice.objects.create(question=question114, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question114.save()

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
for choice_data in choices115:
    Choice.objects.create(question=question115, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question115.save()

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
for choice_data in choices116:
    Choice.objects.create(question=question116, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question116.save()

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
for choice_data in choices117:
    Choice.objects.create(question=question117, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question117.save()

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
for choice_data in choices118:
    Choice.objects.create(question=question118, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question118.save()

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
for choice_data in choices119:
    Choice.objects.create(question=question119, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question119.save()

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
for choice_data in choices120:
    Choice.objects.create(question=question120, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question120.save()

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
for choice_data in choices121:
    Choice.objects.create(question=question121, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question121.save()

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
for choice_data in choices122:
    Choice.objects.create(question=question122, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question122.save()

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
for choice_data in choices123:
    Choice.objects.create(question=question123, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question123.save()

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
for choice_data in choices124:
    Choice.objects.create(question=question124, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question124.save()

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
for choice_data in choices125:
    Choice.objects.create(question=question125, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question125.save()

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
for choice_data in choices126:
    Choice.objects.create(question=question126, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question126.save()

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
for choice_data in choices127:
    Choice.objects.create(question=question127, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question127.save()

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
for choice_data in choices128:
    Choice.objects.create(question=question128, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question128.save()

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
for choice_data in choices129:
    Choice.objects.create(question=question129, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question129.save()

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
for choice_data in choices130:
    Choice.objects.create(question=question130, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question130.save()

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
for choice_data in choices131:
    Choice.objects.create(question=question131, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question131.save()

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
for choice_data in choices132:
    Choice.objects.create(question=question132, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question132.save()

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
for choice_data in choices133:
    Choice.objects.create(question=question133, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question133.save()

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
for choice_data in choices134:
    Choice.objects.create(question=question134, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question134.save()

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
for choice_data in choices135:
    Choice.objects.create(question=question135, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question135.save()

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
for choice_data in choices136:
    Choice.objects.create(question=question136, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question136.save()

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
for choice_data in choices137:
    Choice.objects.create(question=question137, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question137.save()

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
for choice_data in choices138:
    Choice.objects.create(question=question138, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question138.save()

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
for choice_data in choices139:
    Choice.objects.create(question=question139, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question139.save()

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
for choice_data in choices140:
    Choice.objects.create(question=question140, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question140.save()

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
for choice_data in choices141:
    Choice.objects.create(question=question141, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question141.save()

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
for choice_data in choices142:
    Choice.objects.create(question=question142, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question142.save()

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
for choice_data in choices143:
    Choice.objects.create(question=question143, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question143.save()

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
for choice_data in choices144:
    Choice.objects.create(question=question144, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question144.save()

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
for choice_data in choices145:
    Choice.objects.create(question=question145, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question145.save()

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
for choice_data in choices146:
    Choice.objects.create(question=question146, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question146.save()

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
for choice_data in choices147:
    Choice.objects.create(question=question147, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question147.save()

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
for choice_data in choices148:
    Choice.objects.create(question=question148, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question148.save()

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
for choice_data in choices149:
    Choice.objects.create(question=question149, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question149.save()

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
for choice_data in choices150:
    Choice.objects.create(question=question150, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question150.save()

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
for choice_data in choices151:
    Choice.objects.create(question=question151, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question151.save()

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
for choice_data in choices152:
    Choice.objects.create(question=question152, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question152.save()

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
for choice_data in choices153:
    Choice.objects.create(question=question153, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question153.save()

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
for choice_data in choices154:
    Choice.objects.create(question=question154, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question154.save()

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
for choice_data in choices155:
    Choice.objects.create(question=question155, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question155.save()

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
for choice_data in choices156:
    Choice.objects.create(question=question156, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question156.save()

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
for choice_data in choices157:
    Choice.objects.create(question=question157, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question157.save()

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
for choice_data in choices158:
    Choice.objects.create(question=question158, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question158.save()

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
for choice_data in choices159:
    Choice.objects.create(question=question159, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question159.save()

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
for choice_data in choices160:
    Choice.objects.create(question=question160, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question160.save()

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
for choice_data in choices161:
    Choice.objects.create(question=question161, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question161.save()

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
for choice_data in choices162:
    Choice.objects.create(question=question162, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question162.save()

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
for choice_data in choices163:
    Choice.objects.create(question=question163, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question163.save()

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
for choice_data in choices164:
    Choice.objects.create(question=question164, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question164.save()

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
for choice_data in choices165:
    Choice.objects.create(question=question165, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question165.save()

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
for choice_data in choices166:
    Choice.objects.create(question=question166, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question166.save()

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
for choice_data in choices167:
    Choice.objects.create(question=question167, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question167.save()

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
for choice_data in choices168:
    Choice.objects.create(question=question168, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question168.save()

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
for choice_data in choices169:
    Choice.objects.create(question=question169, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question169.save()

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
for choice_data in choices170:
    Choice.objects.create(question=question170, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question170.save()

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
for choice_data in choices171:
    Choice.objects.create(question=question171, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question171.save()

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
for choice_data in choices172:
    Choice.objects.create(question=question172, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question172.save()

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
for choice_data in choices173:
    Choice.objects.create(question=question173, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question173.save()

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
for choice_data in choices174:
    Choice.objects.create(question=question174, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question174.save()

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
for choice_data in choices175:
    Choice.objects.create(question=question175, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question175.save()

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
for choice_data in choices176:
    Choice.objects.create(question=question176, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question176.save()

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
for choice_data in choices177:
    Choice.objects.create(question=question177, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question177.save()

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
for choice_data in choices178:
    Choice.objects.create(question=question178, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question178.save()

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
for choice_data in choices179:
    Choice.objects.create(question=question179, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question179.save()

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
for choice_data in choices180:
    Choice.objects.create(question=question180, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question180.save()

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
for choice_data in choices181:
    Choice.objects.create(question=question181, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question181.save()

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
for choice_data in choices182:
    Choice.objects.create(question=question182, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question182.save()

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
for choice_data in choices183:
    Choice.objects.create(question=question183, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question183.save()

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
for choice_data in choices184:
    Choice.objects.create(question=question184, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question184.save()

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
for choice_data in choices185:
    Choice.objects.create(question=question185, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question185.save()

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
for choice_data in choices186:
    Choice.objects.create(question=question186, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question186.save()

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
for choice_data in choices187:
    Choice.objects.create(question=question187, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question187.save()

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
for choice_data in choices188:
    Choice.objects.create(question=question188, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question188.save()

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
for choice_data in choices189:
    Choice.objects.create(question=question189, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question189.save()

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
for choice_data in choices190:
    Choice.objects.create(question=question190, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question190.save()

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
for choice_data in choices191:
    Choice.objects.create(question=question191, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question191.save()

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
for choice_data in choices192:
    Choice.objects.create(question=question192, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question192.save()

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
for choice_data in choices193:
    Choice.objects.create(question=question193, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question193.save()

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
for choice_data in choices194:
    Choice.objects.create(question=question194, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question194.save()

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
for choice_data in choices195:
    Choice.objects.create(question=question195, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question195.save()

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
for choice_data in choices196:
    Choice.objects.create(question=question196, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question196.save()

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
for choice_data in choices197:
    Choice.objects.create(question=question197, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question197.save()

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
for choice_data in choices198:
    Choice.objects.create(question=question198, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question198.save()

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
for choice_data in choices199:
    Choice.objects.create(question=question199, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question199.save()

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
for choice_data in choices200:
    Choice.objects.create(question=question200, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question200.save()

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
for choice_data in choices201:
    Choice.objects.create(question=question201, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question201.save()

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
for choice_data in choices202:
    Choice.objects.create(question=question202, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question202.save()

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
for choice_data in choices203:
    Choice.objects.create(question=question203, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question203.save()

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
for choice_data in choices204:
    Choice.objects.create(question=question204, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question204.save()

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
for choice_data in choices205:
    Choice.objects.create(question=question205, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question205.save()

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
for choice_data in choices206:
    Choice.objects.create(question=question206, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question206.save()

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
for choice_data in choices207:
    Choice.objects.create(question=question207, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question207.save()

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
for choice_data in choices208:
    Choice.objects.create(question=question208, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question208.save()

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
for choice_data in choices209:
    Choice.objects.create(question=question209, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question209.save()

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
for choice_data in choices210:
    Choice.objects.create(question=question210, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question210.save()

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
for choice_data in choices211:
    Choice.objects.create(question=question211, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question211.save()

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
for choice_data in choices212:
    Choice.objects.create(question=question212, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question212.save()

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
for choice_data in choices213:
    Choice.objects.create(question=question213, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question213.save()

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
for choice_data in choices214:
    Choice.objects.create(question=question214, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question214.save()

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
for choice_data in choices215:
    Choice.objects.create(question=question215, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question215.save()

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
for choice_data in choices216:
    Choice.objects.create(question=question216, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question216.save()

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
for choice_data in choices217:
    Choice.objects.create(question=question217, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question217.save()

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
for choice_data in choices218:
    Choice.objects.create(question=question218, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question218.save()

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
for choice_data in choices219:
    Choice.objects.create(question=question219, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question219.save()

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
for choice_data in choices220:
    Choice.objects.create(question=question220, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question220.save()

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
for choice_data in choices221:
    Choice.objects.create(question=question221, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question221.save()

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
for choice_data in choices222:
    Choice.objects.create(question=question222, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question222.save()

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
for choice_data in choices223:
    Choice.objects.create(question=question223, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question223.save()

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
for choice_data in choices224:
    Choice.objects.create(question=question224, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question224.save()

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
for choice_data in choices225:
    Choice.objects.create(question=question225, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question225.save()

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
for choice_data in choices226:
    Choice.objects.create(question=question226, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question226.save()

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
for choice_data in choices227:
    Choice.objects.create(question=question227, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question227.save()

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
for choice_data in choices228:
    Choice.objects.create(question=question228, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question228.save()

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
for choice_data in choices229:
    Choice.objects.create(question=question229, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question229.save()

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
for choice_data in choices230:
    Choice.objects.create(question=question230, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question230.save()

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
for choice_data in choices231:
    Choice.objects.create(question=question231, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question231.save()

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
for choice_data in choices232:
    Choice.objects.create(question=question232, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question232.save()

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
for choice_data in choices233:
    Choice.objects.create(question=question233, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question233.save()

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
for choice_data in choices234:
    Choice.objects.create(question=question234, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question234.save()

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
for choice_data in choices235:
    Choice.objects.create(question=question235, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question235.save()

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
for choice_data in choices236:
    Choice.objects.create(question=question236, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question236.save()

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
for choice_data in choices237:
    Choice.objects.create(question=question237, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question237.save()

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
for choice_data in choices238:
    Choice.objects.create(question=question238, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question238.save()

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
for choice_data in choices239:
    Choice.objects.create(question=question239, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question239.save()

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
for choice_data in choices240:
    Choice.objects.create(question=question240, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question240.save()

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
for choice_data in choices241:
    Choice.objects.create(question=question241, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question241.save()

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
for choice_data in choices242:
    Choice.objects.create(question=question242, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question242.save()

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
for choice_data in choices243:
    Choice.objects.create(question=question243, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question243.save()

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
for choice_data in choices244:
    Choice.objects.create(question=question244, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question244.save()

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
for choice_data in choices245:
    Choice.objects.create(question=question245, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question245.save()

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
for choice_data in choices246:
    Choice.objects.create(question=question246, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question246.save()

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
for choice_data in choices247:
    Choice.objects.create(question=question247, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question247.save()

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
for choice_data in choices248:
    Choice.objects.create(question=question248, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question248.save()

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
for choice_data in choices249:
    Choice.objects.create(question=question249, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question249.save()

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
for choice_data in choices250:
    Choice.objects.create(question=question250, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question250.save()

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
for choice_data in choices251:
    Choice.objects.create(question=question251, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question251.save()

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
for choice_data in choices252:
    Choice.objects.create(question=question252, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question252.save()

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
for choice_data in choices253:
    Choice.objects.create(question=question253, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question253.save()

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
for choice_data in choices254:
    Choice.objects.create(question=question254, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question254.save()

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
for choice_data in choices255:
    Choice.objects.create(question=question255, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question255.save()

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
for choice_data in choices256:
    Choice.objects.create(question=question256, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question256.save()

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
for choice_data in choices257:
    Choice.objects.create(question=question257, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question257.save()

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
for choice_data in choices258:
    Choice.objects.create(question=question258, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question258.save()

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
for choice_data in choices259:
    Choice.objects.create(question=question259, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question259.save()

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
for choice_data in choices260:
    Choice.objects.create(question=question260, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question260.save()

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
for choice_data in choices261:
    Choice.objects.create(question=question261, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question261.save()

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
for choice_data in choices262:
    Choice.objects.create(question=question262, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question262.save()

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
for choice_data in choices263:
    Choice.objects.create(question=question263, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question263.save()

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
for choice_data in choices264:
    Choice.objects.create(question=question264, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question264.save()

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
for choice_data in choices265:
    Choice.objects.create(question=question265, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question265.save()

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
for choice_data in choices266:
    Choice.objects.create(question=question266, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question266.save()

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
for choice_data in choices267:
    Choice.objects.create(question=question267, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question267.save()

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
for choice_data in choices268:
    Choice.objects.create(question=question268, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question268.save()

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
for choice_data in choices269:
    Choice.objects.create(question=question269, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question269.save()

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
for choice_data in choices270:
    Choice.objects.create(question=question270, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question270.save()

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
for choice_data in choices271:
    Choice.objects.create(question=question271, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question271.save()

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
for choice_data in choices272:
    Choice.objects.create(question=question272, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question272.save()

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
for choice_data in choices273:
    Choice.objects.create(question=question273, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question273.save()

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
for choice_data in choices274:
    Choice.objects.create(question=question274, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question274.save()

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
for choice_data in choices275:
    Choice.objects.create(question=question275, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question275.save()

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
for choice_data in choices276:
    Choice.objects.create(question=question276, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question276.save()

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
for choice_data in choices277:
    Choice.objects.create(question=question277, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question277.save()

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
for choice_data in choices278:
    Choice.objects.create(question=question278, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question278.save()

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
for choice_data in choices279:
    Choice.objects.create(question=question279, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question279.save()

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
for choice_data in choices280:
    Choice.objects.create(question=question280, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question280.save()

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
for choice_data in choices281:
    Choice.objects.create(question=question281, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question281.save()

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
for choice_data in choices282:
    Choice.objects.create(question=question282, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question282.save()

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
for choice_data in choices283:
    Choice.objects.create(question=question283, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question283.save()

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
for choice_data in choices284:
    Choice.objects.create(question=question284, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question284.save()

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
for choice_data in choices285:
    Choice.objects.create(question=question285, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question285.save()

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
for choice_data in choices286:
    Choice.objects.create(question=question286, choice_text=choice_data["text"], option_label=choice_data["label"], is_correct=choice_data["is_correct"])
question286.save()

print("✅ All questions created successfully.")
## cd /d "g:\MyCode\App Taxi Exam" && python manage.py shell < create_questions_all.py
## cd /d "g:\MyCode\App Taxi Exam" && python manage.py shell < create_question.py