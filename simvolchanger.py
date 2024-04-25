def replace_characters(text):
    replacements = {
        'у': 'y', 'У': 'Y',
        'к': 'k', 'К': 'K',
        'е': 'e', 'Е': 'E',
        'б': '6', 'Б': '6',
        'н': 'H', 'Н': 'H',
        'з': '3', 'З': '3',
        'х': 'x', 'Х': 'X',
        'в': 'B', 'В': 'B',
        'а': 'a', 'А': 'A',
        'р': 'p', 'Р': 'P',
        'о': 'o', 'О': 'O',
        'ч': '4', 'Ч': '4',
        'с': 'c', 'С': 'C',
        'м': 'M', 'М': 'M',
        'и': 'u', 'И': 'U',
        'т': 'T', 'Т': 'T'
    }
    replaced_text = ''
    for char in text:
        if char in replacements:
            replaced_text += replacements[char]
        else:
            replaced_text += char
    return replaced_text

def save_to_file(text):
    file_name = input("Введите имя файла для сохранения: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    try:
        with open(file_name, 'w') as file:
            file.write(text)
        print(f"Результат успешно сохранён в файле {file_name}")
    except:
        print("Ошибка при сохранении файла.")

def process_text_input(choice):
    if choice == '1':
        user_text = input("Введите текст для замены символов: ")
        replaced_text = replace_characters(user_text)
        print("Изменённый текст:", replaced_text)
        save_choice = input("Хотите сохранить результат в файл? (да/нет): ")
        if save_choice.lower() == 'да':
            save_to_file(replaced_text)
    elif choice == '2':
        file_name = input("Введите имя файла для чтения: ")
        try:
            with open(file_name, 'r') as file:
                text = file.read()
                replaced_text = replace_characters(text)
                print("Изменённый текст:", replaced_text)
                save_choice = input("Хотите сохранить результат в файл? (да/нет): ")
                if save_choice.lower() == 'да':
                    save_to_file(replaced_text)
        except FileNotFoundError:
            print("Файл не найден.")
    else:
        print("Некорректный выбор.")

def main():
    print("Меню:")
    print("1. Ввести текст в консоли")
    print("2. Прочитать текст из файла")
    choice = input("Выберите способ ввода текста (1 или 2): ")
    process_text_input(choice)

if __name__ == "__main__":
    main()
