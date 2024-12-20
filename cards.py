import genanki
import random
from tts import generate_tts_for_cards
from file import read_data_from_file, copy_files_to_anki

model_id = 1981211111
deck_id = random.randrange(1 << 30, 1 << 31)


# Funkcja do tworzenia talii Anki


def create_anki_deck(cards, deck_name="Talia wygenerowana skryptem"):
    # Definiowanie modelu (układ kart)
    model = genanki.Model(
        model_id,
        "Koreańskie zdania",
        fields=[
            {"name": "Polish Word"},
            {"name": "Korean Word"},
            {"name": "Korean Sentence"},
            {"name": "Polish Sentence"},
            {"name": "Sound"},
        ],
        templates=[
            {
                "name": "kr-pl",
                "qfmt": "{{Sound}}{{Korean Sentence}} ({{Korean Word}})",
                "afmt": "{{FrontSide}}<hr>{{Polish Sentence}}<br><br><span>{{Polish Word}} - {{Korean Word}}<span>",
            },
            {
                "name": "pl-kr",
                "qfmt": "{{Polish Sentence}} ({{Polish Word}})",
                "afmt": "{{FrontSide}}<hr>{{Sound}}{{Korean Sentence}}<br><br><span>{{Korean Word}} - {{Polish Word}}</span>",
            }
        ],
        css="""
            .card {
                text-align: center;
                font-size: 32px;
            }

            .card span {
                font-size: 24px;
            }
        """
    )

    # Tworzenie talii
    deck = genanki.Deck(deck_id, deck_name)

    package = genanki.Package(deck)
    package.media_files = ['sound.mp3', 'images/image.jpg']

    # Dodawanie kart do talii
    for card in cards:
        note = genanki.Note(
            model=model,
            fields=[card[0], card[1], card[2], card[3], card[4]],
        )
        deck.add_note(note)

    return deck

# Funkcja do zapisu talii do pliku


def save_deck_to_file(deck, output_file):
    genanki.Package(deck).write_to_file(output_file)


# Wczytanie danych i generowanie kart
file_name = "semantic_primes_chunk_3"
file_path = "{name}.txt".format(name=file_name)
cards = read_data_from_file(file_path)
generate_tts_for_cards(cards)
anki_deck = create_anki_deck(cards)

# Zapisanie talii do pliku .apkg
output_file = "{name}.apkg".format(name=file_name)
save_deck_to_file(anki_deck, output_file)
print(f"Talia została zapisana jako {output_file}.")

# skopiowanie wygenerowany plikow do anki
copy_files_to_anki(cards)
print("Nagrania zostały zaimportowane do anki")
