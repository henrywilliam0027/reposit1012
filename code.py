import os
import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()

class NoteTakingApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print(f"Note added successfully - '{title}'")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            print("Your Notes:")
            for i, note in enumerate(self.notes, 1):
                print(f"{i}. {note.title} - Created at: {note.created_at}")
                print(note.content)
                print("\n")

def main():
    note_app = NoteTakingApp()

    while True:
        print("\nNote Taking App Menu:")
        print("1. Add a Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            note_app.add_note(title, content)
        elif choice == '2':
            note_app.view_notes()
        elif choice == '3':
            print("Exiting the Note Taking App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
