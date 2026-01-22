import data_fetcher


def generate_card_html(animal):
    """Erstellt HTML für ein Tier."""
    name = animal.get('name', 'Unknown')
    char = animal.get('characteristics', {})

    card_content = f"Name: {name}\n"
    if char.get('diet'): card_content += f"Diet: {char.get('diet')}\n"
    if animal.get('locations'): card_content += f"Location: {animal.get('locations')[0]}\n"

    return f'<li class="cards__item"><div class="card__text">{card_content}</div></li>'


def main():
    # 1. Template laden
    with open("animals_templates.html", "r", encoding='utf-8') as f:
        template = f.read()

    # 2. Daten über den Fetcher holen
    animal_name = input("Please enter an animal: ")
    animal_data = data_fetcher.fetch_data(animal_name)

    # 3. HTML bauen (Meilenstein 3: Fehlerbehandlung)
    if animal_data:
        cards = "".join([generate_card_html(a) for a in animal_data])
    else:
        cards = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    # 4. Speichern
    final_html = template.replace("__REPLACE_CARDS__", cards)
    with open("animals.html", "w", encoding='utf-8') as f:
        f.write(final_html)
    print("Website was successfully generated.")


if __name__ == "__main__":
    main()