import re

def fix_questions_file():
    source_file = "g:\\MyCode\\App Taxi Exam\\create_questions_all.py"
    output_file = "g:\\MyCode\\App Taxi Exam\\create_questions_all_fixed_format.py"
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Step 1: Fix the category error message format
    # Extract the question number from the context
    def fix_category_message(match):
        # Try to find the question number from the context
        context_before = content[:match.start()]
        question_match = re.search(r'question(\d+) =', context_before[::-1])
        if question_match:
            question_num = question_match.group(1)[::-1]  # Reverse back
            return f'print(f"[Q{question_num}] Category \'{match.group(1)}\' not found in DB")'
        return match.group(0)  # Return original if no number found
    
    content = re.sub(r'print\(f"Category \'(.*?)\' not found in DB"\)',
                     fix_category_message,
                     content)
    
    # Step 2: Fix the for loop for choices to match question_holder.py
    pattern = r'for choice_data in choices(\d+):\s+Choice\.objects\.create\(\s*question=question\1,\s*choice_text=choice_data\["text"\],\s*option_label=choice_data\["label"\],\s*is_correct=choice_data\["is_correct"\]\s*\)'
    
    def replace_choice_loop(match):
        num = match.group(1)
        return f'''for choice in choices{num}:
    try:
        Choice.objects.create(
            question=question{num},
            choice_text=choice["text"],
            option_label=choice["label"],
            is_correct=choice["is_correct"]
        )
    except Exception as e:
        print(f"[Q{num}] Failed to create choice {{choice['label']}}: {{e}}")'''
    
    content = re.sub(pattern, replace_choice_loop, content)
    
    # Step 3: Fix for loops for choice with different variable name
    pattern = r'for choice in choices(\d+):\s+Choice\.objects\.create\(\s*question=question\1,\s*choice_text=choice\["text"\],\s*option_label=choice\["label"\],\s*is_correct=choice\["is_correct"\]\s*\)'
    content = re.sub(pattern, replace_choice_loop, content)
    
    # Step 4: Fix variable names that might be inconsistent
    content = content.replace("choice_data", "choice")
    
    # Step 5: Replace the category names storage format
    pattern = r'category_names(\d+) = (.*?)\nfor name in category_names\1:'
    
    def replace_category_declaration(match):
        num = match.group(1)
        categories = match.group(2)
        return f'category_names{num} = {categories}\nfor name in category_names{num}:'
    
    content = re.sub(pattern, replace_category_declaration, content)
    
    # Step 6: Remove unnecessary question.save() calls
    content = re.sub(r'question\d+\.save\(\)', '', content)
    
    # Write the updated content to the new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed file saved to: {output_file}")

if __name__ == "__main__":
    fix_questions_file()
