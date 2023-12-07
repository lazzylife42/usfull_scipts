import os
import re

def find_internal_function_calls(directory):
    functions_calls = {}

    c_files = [file for file in os.listdir(directory) if file.endswith('.c')]

    for file in c_files:
        functions_calls[file] = {}
        with open(os.path.join(directory, file), 'r') as f:
            content = f.read()
            function_pattern = re.compile(r'\b(\w+)\s*\([^)]*\);')
            function_matches = function_pattern.findall(content)
            functions_calls[file] = function_matches

    return functions_calls

directory_path = '.'  # Chemin vers le répertoire contenant vos fichiers .c
internal_function_calls = find_internal_function_calls(directory_path)

for file, calls in internal_function_calls.items():
    print(f"Appels de fonctions dans le fichier '{file}':")
    for call in calls:
        print(call)
    print()

