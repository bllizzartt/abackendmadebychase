from typing import List

def generate_prompt(ingredients: List[str]):
    return '''In the following format: 
Recipe 1:
Step 1.
Step 2.
...
Step n.
Please provide a list of 1-3 recipes that can be made with the following ingredients:''' + "".join(ingredients)