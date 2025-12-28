# Personal Notes Manager (Python)

Ein konsolenbasiertes Notizverwaltungssystem in Python zur Organisation persönlicher Notizen.  
Das Projekt dient als Lernprojekt zur Vertiefung von Python-Kenntnissen im Umgang mit Datenstrukturen, Funktionen und persistenter Datenspeicherung.

---

## Features

- Erstellung, Anzeige, Bearbeitung und Löschung von Notizen  
- Persistente Speicherung von Notizen in einer JSON-Datei  
- Suche nach Stichworten oder Tags  
- Verwaltung von Tags für bessere Organisation  
- Einfaches, benutzerfreundliches Konsolenmenü  

---

## Datenstruktur

Jede Notiz enthält folgende Felder:

- **ID** (String, eindeutig für jede Notiz)  
- **Titel**  
- **Inhalt**  
- **Erstellungsdatum**  
- **Tags** (Liste von Strings)

Beispiel:

```python
notes = {
    "0": {
        "notes_title": "Beispiel-Notiz",
        "notes_content": "Dies ist ein Beispiel.",
        "notes_date": "24.12.2025",
        "notes_tags": ["test", "beispiel"]
    }
}
