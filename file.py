import shutil
import os

anki_dir = os.path.expanduser("~/.local/share/Anki2/Michał/collection.media/")

# pobiera z pliku karty wygenrowane z chatgtp w formcie
# {{słowo po polsku}};{{słowo po koreańsku}};{{zdanie po koreańsku z wykorzystaniem tego słowa}};{{tłumaczenie zdania na polski}}
# zapisuje do tablicy


def read_data_from_file(file_path):
    cards = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if (line[0] == "#"):
                return
            parts = line.strip().split(";")
            if len(parts) == 4:
                # add empty sound field
                cards.append([*parts, ""])

    return cards


def copy_files_to_anki(cards):
    for card in cards:
        filename = "generated/{name}.mp3".format(name=card[0])

        try:
            shutil.copy(filename, anki_dir)
        except Exception:
            pass
