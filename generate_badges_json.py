import os
import json

BADGES_DIR = 'badges'
OUTPUT_FILE = 'badges.json'

def generate_index():
    badges = []
    if not os.path.exists(BADGES_DIR):
        print(f"Directory '{BADGES_DIR}' not found.")
        return

    for filename in os.listdir(BADGES_DIR):
        if filename.lower().endswith(('.svg', '.png')):
            badges.append(filename)
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(badges, f, indent=2)
    
    print(f"Generated {OUTPUT_FILE} with {len(badges)} entries.")

if __name__ == "__main__":
    generate_index()
