import pysrt


def extract_subtitles(srt_file):
    # Lese die srt-Datei ein
    subs = pysrt.open(srt_file, encoding='utf-8')

    # Erstelle eine leere Liste, um die Untertitel zu speichern
    subtitles = []

    # Gehe durch jeden Untertitel in der Datei
    for sub in subs:
        # Füge den Text des Untertitels zur Liste hinzu
        subtitles.append(sub.text)

    # Gib die Liste der Untertitel zurück
    return subtitles


def write_to_files(subtitles_string, max_chars=20000):
    # Erstelle einen Zähler für die Dateien
    file_count = 1

    # Teile den String in Stücke von max_chars Zeichen
    for i in range(0, len(subtitles_string), max_chars):
        # Erstelle den Dateinamen für diese Datei
        filename = f'untertitel_{file_count}.txt'

        # Schreibe den Teil des Strings in die Datei
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(subtitles_string[i:i + max_chars])

        print(f"Untertitel wurden erfolgreich in die Datei '{filename}' geschrieben.")

        # Erhöhe den Zähler für die Dateien
        file_count += 1


# Verwende die Funktion, um die Untertitel aus einer srt-Datei zu extrahieren
subtitles = extract_subtitles('meine_srt_datei.srt')

# Verwandle die Liste der Untertitel in einen String mit Zeilenumbrüchen zwischen den Untertiteln
subtitles_string = '\n'.join(subtitles)

# Schreibe die Untertitel in mehrere Dateien
write_to_files(subtitles_string)