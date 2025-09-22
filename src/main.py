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

        last_word_current = entry['text'].split()[-1]
        last_word_last = dataset[-1]['text'].split()[-1]
        if entry['confidence'] >= confidence and int.from_bytes(last_word_current.encode(), 'big') != int.from_bytes(last_word_last.encode(), 'big'):
            print(f"{entry['text']}")
    print(f"{Fore.YELLOW}User: {Style.RESET_ALL}")
    user_input = input(f"{Fore.YELLOW}User: {Style.RESET_ALL}")


if __name__ == "__main__":
    main()  