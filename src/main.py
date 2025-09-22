import json
from colorama import Fore, Style
import os

confidence = 0.9

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Charger le dataset
    with open("src/datasets/datasets.json", 'r') as file:
        data = json.load(file)
        dataset = data['word_sequences']
    
    print(f"{Fore.GREEN}Dataset: {len(dataset)} suites de mots{Style.RESET_ALL}")
    
    user_input = input(f"{Fore.YELLOW}User: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}Bot: {Style.RESET_ALL}")
    
    for entry in dataset:
        if entry['confidence'] >= confidence:
            print(f"{entry['text']}")
    print(f"{Fore.YELLOW}User: {Style.RESET_ALL}")
    user_input = input(f"{Fore.YELLOW}User: {Style.RESET_ALL}")


if __name__ == "__main__":
    main()  