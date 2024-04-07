import json
from datetime import datetime

NOTES_FILE = 'notes.json'

def load_notes():
    try:
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    notes = load_notes()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    filter_date = input("Введите дату для фильтрации (yyyy-mm-dd), или нажмите Enter для просмотра всех заметок: ")
    notes = load_notes()
    if filter_date:
        filtered_notes = [note for note in notes if note['timestamp'].startswith(filter_date)]
        if not filtered_notes:
            print("Нет заметок за указанную дату")
            return
        notes = filtered_notes
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['message']}, Дата/время: {note['timestamp']}")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = load_notes()
    filtered_notes = [note for note in notes if note['id'] != note_id]
    if len(filtered_notes) == len(notes):
        print("Заметка с указанным ID не найдена")
        return
    save_notes(filtered_notes)
    print("Заметка успешно удалена")

if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Удалить заметку")
        print("4. Выйти")

        choice = input("Выберите действие (1/2/3/4): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите один из вариантов (1/2/3/4).")