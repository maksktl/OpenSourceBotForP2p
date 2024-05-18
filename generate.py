import os
import random
import subprocess
from datetime import datetime, timedelta

import git

# Авторизованный пользователь Git
author_name = 'maksktl'
author_email = 'matantsev0@gmail.com'

# Текущая директория с репозиторием
repo_path = os.getcwd()

# Список случайного кода
random_code_samples = [
    "print('Hello, World!')\n",
    "def foo():\n    return 'bar'\n",
    "for i in range(10):\n    print(i)\n",
    "class MyClass:\n    def __init__(self):\n        self.value = 42\n",
    "if __name__ == '__main__':\n    print('This is a test script')\n"
]

# Открытие репозитория
os.chdir(repo_path)
repo = git.Repo(repo_path)

# Начало 3-месячного периода
start_date = datetime.now() - timedelta(days=90)

# Генерация коммитов за каждый день
for i in range(91):
    commit_date = start_date + timedelta(days=i)
    commit_message = f'Commit on {commit_date.strftime("%Y-%m-%d")}'

    # 30% шанс на создание нового файла, 70% шанс на дополнение существующего
    if random.random() < 0.3:
        file_name = f'new_script_{i}.py'
        with open(file_name, 'w') as file:
            file.write(random.choice(random_code_samples))
    else:
        # Поиск всех файлов с расширением .py в текущей директории
        py_files = [f for f in os.listdir(repo_path) if f.endswith('.py')]
        if py_files:
            file_name = random.choice(py_files)
            with open(file_name, 'a') as file:
                file.write(random.choice(random_code_samples))
        else:
            # Если .py файлы не найдены, создаём новый файл
            file_name = f'new_script_{i}.py'
            with open(file_name, 'w') as file:
                file.write(random.choice(random_code_samples))

    subprocess.run(['git', 'add', file_name])

    # Форматирование даты коммита
    commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')

    # Создание коммита с использованием команды git
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = commit_date_str
    env['GIT_COMMITTER_DATE'] = commit_date_str

    subprocess.run(['git', 'commit', '-m', commit_message, '--author', f'{author_name} <{author_email}>'], env=env)

print('Commits generated successfully.')
class MyClass:
    def __init__(self):
        self.value = 42
for i in range(10):
    print(i)
for i in range(10):
    print(i)
print('Hello, World!')
for i in range(10):
    print(i)
print('Hello, World!')
print('Hello, World!')
if __name__ == '__main__':
    print('This is a test script')
for i in range(10):
    print(i)
class MyClass:
    def __init__(self):
        self.value = 42
if __name__ == '__main__':
    print('This is a test script')
if __name__ == '__main__':
    print('This is a test script')
for i in range(10):
    print(i)
def foo():
    return 'bar'
for i in range(10):
    print(i)
if __name__ == '__main__':
    print('This is a test script')
