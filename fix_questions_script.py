import os
import re

def fix_create_questions_file():
    # Path to the original file
    file_path = r"g:\MyCode\App Taxi Exam\create_questions_all.py"
    
    # Path to the fixed file
    fixed_file_path = r"g:\MyCode\App Taxi Exam\create_questions_all_fixed.py"
    
    # Read the original file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Process the file line by line
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)
        
        # Check if this is a category loop
        if re.match(r'for name in category_names\d+:', line.strip()):
            next_line = lines[i+1] if i+1 < len(lines) else ""
            
            # If the next line doesn't have 'try:' in it, add the missing code
            if 'try:' not in next_line:
                question_num = re.search(r'category_names(\d+)', line).group(1)
                fixed_lines.append("    try:\n")
                fixed_lines.append(f"        cat = Category.objects.get(name=name)\n")
                fixed_lines.append(f"        question{question_num}.categories.add(cat)\n")
                fixed_lines.append("    except Category.DoesNotExist:\n")
                fixed_lines.append("        print(f\"Category '{name}' not found in DB\")\n")
        
        # Check if this is a choice loop
        elif re.match(r'for choice_data in choices\d+:', line.strip()):
            next_line = lines[i+1] if i+1 < len(lines) else ""
            
            # If the next line doesn't have 'Choice.objects.create' in it, add the missing code
            if 'Choice.objects.create' not in next_line:
                question_num = re.search(r'choices(\d+)', line).group(1)
                fixed_lines.append(f"    Choice.objects.create(question=question{question_num}, choice_text=choice_data[\"text\"], option_label=choice_data[\"label\"], is_correct=choice_data[\"is_correct\"])\n")
        
        i += 1
    
    # Write the fixed content to a new file
    with open(fixed_file_path, 'w', encoding='utf-8') as file:
        file.writelines(fixed_lines)
    
    print(f"Fixed file saved to: {fixed_file_path}")

if __name__ == "__main__":
    fix_create_questions_file()
