from src.utils.bird_parser import load_bird_data

def main():
    # Load bird data from the JSON file
    birds = load_bird_data('data/bird_cards.json', 'data/bonus_cards.json')
    
    # Print each bird object to verify the output
    for bird in birds:
        print(bird, end="\n")

if __name__ == "__main__":
    main()
