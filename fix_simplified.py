import re
import os

def fix_question_file():
    # Input and output file paths
    input_file = 'g:\\MyCode\\App Taxi Exam\\create_questions_all.py'
    output_file = 'g:\\MyCode\\App Taxi Exam\\create_questions_all_simplified.py'
    
    # Read the entire content of the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content into questions
    questions = re.split(r'# === Question \d+ ===', content)
    
    # Skip the first part (imports and any preamble)
    preamble = questions[0]
    questions = questions[1:]
    
    # Write the fixed file
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write imports and any initial setup
        f.write("from taxi.models import Question, Category, Choice\n\n")
        f.write("print('Starting question creation process...')\n\n")
        
        # Create some common categories first
        f.write("# Create common categories if they don't exist\n")
        f.write("categories_to_check = ['Main Roads', 'Housing Estates', 'Towns/Villages']\n")
        f.write("for cat_name in categories_to_check:\n")
        f.write("    try:\n")
        f.write("        Category.objects.get(name=cat_name)\n")
        f.write("        print(f\"Category '{cat_name}' already exists\")\n")
        f.write("    except Category.DoesNotExist:\n")
        f.write("        Category.objects.create(name=cat_name)\n")
        f.write("        print(f\"Created missing category: '{cat_name}'\")\n\n")
        
        # Process the first 5 questions
        for i, question in enumerate(questions[:286], 1):
            f.write(f"# === Question {i} ===\n")
            f.write("try:\n")
            
            # Extract question text
            question_match = re.search(r'question\d+\s*=\s*Question\.objects\.create\(\s*question_text\s*=\s*"([^"]+)"', question)
            if question_match:
                question_text = question_match.group(1)
                f.write(f"    question{i} = Question.objects.create(\n")
                f.write(f"        question_text=\"{question_text}\",\n")
                f.write(f"        question_type=Question.SINGLE\n")
                f.write(f"    )\n")
                f.write(f"    print(f\"Created Question {i}\")\n\n")
            
            # Extract categories
            categories_match = re.search(r'category_names\d+\s*=\s*\[(.*?)\]', question, re.DOTALL)
            if categories_match:
                categories_str = categories_match.group(1)
                f.write(f"    category_names{i} = [{categories_str}]\n")
                f.write(f"    for name in category_names{i}:\n")
                f.write(f"        try:\n")
                f.write(f"            cat = Category.objects.get(name=name)\n")
                f.write(f"            question{i}.categories.add(cat)\n")
                f.write(f"        except Category.DoesNotExist:\n")
                f.write(f"            print(f\"[Q{i}] Category '{{name}}' not found in DB\")\n\n")
            
            # Extract choices
            choices_text = re.search(r'choices\d+\s*=\s*\[(.*?)\]', question, re.DOTALL)
            if choices_text:
                choices_str = choices_text.group(1)
                f.write(f"    choices{i} = [\n")
                for choice_line in choices_str.strip().split('\n'):
                    choice_line = choice_line.strip()
                    if choice_line and not choice_line.startswith(']'):
                        f.write(f"        {choice_line}\n")
                f.write(f"    ]\n")
                f.write(f"    for choice in choices{i}:\n")
                f.write(f"        try:\n")
                f.write(f"            Choice.objects.create(\n")
                f.write(f"                question=question{i},\n")
                f.write(f"                choice_text=choice[\"text\"],\n")
                f.write(f"                option_label=choice[\"label\"],\n")
                f.write(f"                is_correct=choice[\"is_correct\"]\n")
                f.write(f"            )\n")
                f.write(f"        except Exception as e:\n")
                f.write(f"            print(f\"[Q{i}] Failed to create choice {{choice['label']}}: {{e}}\")\n")
            
            f.write("except Exception as e:\n")
            f.write(f"    print(f\"Error creating Question {i}: {{e}}\")\n\n")
        
        # Add footer
        f.write("\nprint(\"✅ All questions created successfully.\")\n")
    
    print(f"Fixed file saved to: {output_file}")

# Run the function
if __name__ == "__main__":
    fix_question_file()
