import os
import shutil

# Створюємо потрібні папки
os.makedirs("files", exist_ok=True)
os.makedirs("backup", exist_ok=True)

# Створюємо потрібні файли для роботи
open("files/data.txt", "w").close()
open("files/old_data.txt", "w").close()
open("important_data.txt", "w").close()


# 1. Виводимо всі файли та папки
print("1. Вміст поточної папки:")
for item in os.listdir("."):
    print(item)


# 2. Створюємо NewFolder
if not os.path.exists("NewFolder"):
    os.mkdir("NewFolder")

print("2. NewFolder створено")


# 3. Копіюємо data.txt
shutil.copy(
    "files/data.txt",
    "backup/data_copy.txt"
)

print("3. data.txt скопійовано в backup як data_copy.txt")


# 4. Перейменовуємо old_data.txt
if os.path.exists("files/old_data.txt"):
    os.rename(
        "files/old_data.txt",
        "files/new_data.txt"
    )

print("4. old_data.txt перейменовано на new_data.txt")


# 5. Переміщуємо important_data.txt
if os.path.exists("important_data.txt"):
    shutil.move(
        "important_data.txt",
        "backup/important_data.txt"
    )

print("5. important_data.txt переміщено в backup")


# ПЕРЕВІРКА
print("========== ПЕРЕВІРКА ==========")

print("Поточна папка:")
print(os.listdir("."))

print("Папка files:")
print(os.listdir("files"))

print("Папка backup:")
print(os.listdir("backup"))

print("Папка NewFolder:")
print(os.listdir("NewFolder"))