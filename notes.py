import json
import datetime

# Функция для загрузки заметок из файла
def load_notes(file_name):
    try:
        with open(file_name, 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для сохранения заметок в файл
def save_notes(notes, file_name):
    with open(file_name, 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для добавления заметки
def add_note(notes):
    id = len(notes) + 1
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": id, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    return notes

# Функция для редактирования заметки
def edit_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            title = input("Enter new note title: ")
            body = input("Enter new note body: ")
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return notes
    print("Note not found")
    return notes

# Функция для удаления заметки
def delete_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return notes
    print("Note not found")
    return notes

# Функция для печати списка заметок
def print_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}; Title: {note['title']}; Body: {note['body']}; Timestamp: {note['timestamp']}")

def main():
    file_name = "notes.json"
    notes = load_notes(file_name)

    while True:
        print("\nMenu:")
        print("1. Add a new note")
        print("2. Edit a note")
        print("3. Delete a note")
        print("4. Show all notes")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            notes = add_note(notes)
        elif choice == "2":
            note_id = int(input("Enter the ID of the note to edit: "))
            notes = edit_note(notes, note_id)
        elif choice == "3":
            note_id = int(input("Enter the ID of the note to delete: "))
            notes = delete_note(notes, note_id)
        elif choice == "4":
            print_notes(notes)
        elif choice == "5":
            save_notes(notes, file_name)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()