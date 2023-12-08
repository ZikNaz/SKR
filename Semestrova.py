print("\tАналіз текстових файлів")
introduction = input("Якщо хочете дізнатися, як працює програма, то напишіть (так/ні): ")
if introduction == "так":
    print("Програма виведе кількість слів і символів для кожного рядку тексту з текстового файлу.\nВам треба ввести шлях до текстового файлу.")
else:
    print("Тоді почнемо!")

def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            for i, line in enumerate(lines, start=1):
                words = line.split()
                num_words = len(words)
                num_chars = sum(len(word) for word in words)
                
                print(f"Рядок {i}:")
                print(f"  Кількість слів: {num_words}")
                print(f"  Кількість символів: {num_chars}")
                print()
                
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

# Користувач вводить шлях до файлу
file_path = input("Введіть шлях до текстового файлу: ")

# Викликаємо функцію з введеним користувачем шляхом
analyze_text(file_path)
