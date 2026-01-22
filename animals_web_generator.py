import data_fetcher
import pytz

import data_fetcher


def generate_card_html(animal):
    """Erstellt den HTML-Inhalt für eine einzelne Tier-Karte."""
    name = animal.get('name')
    if not name:
        return ""

    card_content = f"Name: {name}\n"
    characteristics = animal.get('characteristics', {})

    diet = characteristics.get('diet')
    if diet:
        card_content += f"Diet: {diet}\n"

    locations = animal.get('locations')
    if locations and isinstance(locations, list):
        card_content += f"Location: {locations[0]}\n"

    return f"""
            <li class="cards__item">
                <div class="card__text">
{card_content}
                </div>
            </li>
    """


def main():
    # Benutzereingabe
    animal_name = input("Please enter an animal: ")

    # Aufruf des Daten-Fetchers (neue Architektur)
    animal_data = data_fetcher.fetch_data(animal_name)

    # Template laden
    try:
        with open("animals_templates.html", "r", encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print("Fehler: Template-Datei nicht gefunden.")
        return

    # Inhalt basierend auf Daten generieren
    if animal_data:
        all_cards_html = ""
        for animal in animal_data:
            all_cards_html += generate_card_html(animal)
    else:
        all_cards_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    # Finale Webseite erstellen
    final_html = template_content.replace("__REPLACE_CARDS__", all_cards_html)

    with open("animals.html", "w", encoding='utf-8') as f:
        f.write(final_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()