import json
import re
import os

def lolcat_transform(text):
    if not isinstance(text, str):
        return text
    
    # Simple LOLCAT transformations
    replacements = {
        r'\bCan\b': 'Iz',
        r'\bcan\b': 'iz',
        r'\bbe\b': 'haz',
        r'\bthe\b': 'teh',
        r'\bThe\b': 'Teh',
        r'\bme\b': 'miai',
        r'\bmy\b': 'miai',
        r'\bMy\b': 'Miai',
        r'\byou\b': 'u',
        r'\bYou\b': 'U',
        r'\byour\b': 'ur',
        r'\bYour\b': 'Ur',
        r'\bis\b': 'iz',
        r'\bare\b': 'iz',
        r'\bfor\b': '4',
        r'\bto\b': '2',
        r'\band\b': 'n',
        r'\bhello\b': 'hai',
        r'\bHello\b': 'Hai',
        r'\bgoodbye\b': 'kthxbai',
        r'\blove\b': 'lub',
        r'\bminion\b': 'minyun',
        r'\bMinion\b': 'Minyun',
        r'\bparadise\b': 'purrradise',
        r'\bParadise\b': 'Purrradise',
        r'\bwant\b': 'wants',
        r'\bhave\b': 'haz',
        r'\bHave\b': 'Haz',
        r'\bI am\b': 'Iiz',
        r'\bI\'m\b': 'Iiz',
        r'\bplease\b': 'plz',
        r'\bPlease\b': 'Plz',
        r'\boh\b': 'o',
        r'\bOh\b': 'O',
        r'\breally\b': 'rly',
        r'\bnice\b': 'naiz',
        r'\bgood\b': 'gud',
        r'\bGood\b': 'Gud',
        r'\bbad\b': 'badz',
        r'\bhappy\b': 'hapy',
        r'\bsad\b': 'sadz',
        r'\bcat\b': 'kitteh',
        r'\bCat\b': 'Kitteh',
        r'\bdog\b': 'doge',
        r'\bfood\b': 'noms',
        r'\beat\b': 'nom',
    }
    
    transformed = text
    for pattern, replacement in replacements.items():
        transformed = re.sub(pattern, replacement, transformed)
    
    # Add some randomness or common suffixes
    if '!' in transformed:
        transformed = transformed.replace('!', '!!11!!oneONE!')
    
    return transformed

def process_json(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        return
        
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            new_data[key] = lolcat_transform(value)
        elif isinstance(value, dict):
            new_value = {}
            for k, v in value.items():
                new_value[k] = lolcat_transform(v)
            new_data[key] = new_value
        else:
            new_data[key] = value
            
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully created {output_file}")

if __name__ == "__main__":
    process_json('Minionsparadise/Assets/Resources/content/dlc/loc_text/EN-US.json', 
                 'Minionsparadise/Assets/Resources/content/dlc/loc_text/LOLCAT.json')
