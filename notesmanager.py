# ============================================
# PROJEKT: Personal Notes Manager
#
# ZIEL:
# Ein Konsolenprogramm zur Verwaltung pers�nlicher Notizen.
#
# ANFORDERUNGEN:
# 1. Zeige beim Start ein Men� mit folgenden Optionen:
#    - Neue Notiz erstellen
#    - Alle Notizen anzeigen
#    - Notiz bearbeiten
#    - Notiz l�schen
#    - Notizen durchsuchen (Stichwort)
#    - Programm beenden
#
# 2. Jede Notiz soll mindestens enthalten:
#    - Eindeutige ID
#    - Titel
#    - Inhalt (mehrzeiliger Text erlaubt)
#    - Erstellungsdatum
#
# 3. Der Benutzer soll Notizen �ber ihre ID ausw�hlen k�nnen.
#
# 4. Alle Notizen m�ssen dauerhaft gespeichert werden
#    (z. B. in einer JSON-Datei).
#
# 5. Verwende Funktionen f�r jede Hauptaktion
#    (create_note, show_notes, edit_note, delete_note, search_notes).
#
# OPTIONAL / ERWEITERUNGEN:
# - Tags pro Notiz
# - Sortierung nach Datum oder Titel
# - Automatisches Speichern nach jeder �nderung
# - Export einzelner Notizen als Textdatei
#
# RESULTAT:
# Ein �bersichtliches, robustes Konsolenprogramm,
# das strukturierte Daten liest, verarbeitet und speichert.
# ============================================

import json

print("Welcome to your Personal Notes Manager! Choose one of the following options to proceed!\n\n")
#menu = int(input("1. Create new Note\n2. Show all Notes\n3. Edit a Note\n4. Delete a Note\n5. Search Notes for keywords\n6. Exit Notes Manager\n"))

notes = {
    "0": {
        "notes_title": "Test Note",
        "notes_content": "This is a test note to test the note system if it works or nah",
        "notes_date": "24.12.2025",
        "notes_tags": ["test", "system", "sex"]
    },
    "3": {
        "notes_title": "Fuck Note",
        "notes_content": "SOmething something something",
        "notes_date": "26.12.2025",
        "notes_tags": ["tag1", "tag2", "tag3"]
    },
    "5": {
        "notes_title": "Fuck Note",
        "notes_content": "SOmething something something",
        "notes_date": "26.12.2025",
        "notes_tags": ["tag1", "tag2", "tag3"]
    }
}


notes_json = json.dumps(notes)
#print(type(notes))
#print(notes_json)

def getLastKey(notes: dict):
  last_key = int(list(notes)[-1])
  return last_key

print(notes["0"])

# print(getLastKey(notes))

with open('notes.json', 'w') as json_file:
  json.dump(notes, json_file, indent=4)