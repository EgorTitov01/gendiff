# gendiff

`gendiff` — это консольное приложение на Python, предназначенное для сравнения двух файлов конфигурации в форматах **JSON** или **YAML**. Результат сравнения может быть представлен в одном из трёх удобных для чтения и обработки форматов вывода:

* **stylish** (формат по умолчанию) — древовидное представление различий с уровнями вложенности и отступами.
* **plain** — плоский, построчный список изменений, удобно читаемый человеком.
* **json** — стандартизированный формат JSON, подходящий для машинной обработки.

📽 **Пример работы:**

Посмотрите краткую демонстрацию работы утилиты `gendiff`:

[![asciicast](https://asciinema.org/a/fqD0qNnxOVwaBMUyKoyjlful9.svg)](https://asciinema.org/a/fqD0qNnxOVwaBMUyKoyjlful9)

---

## 📦 Установка

Для успешной установки и запуска проекта убедитесь, что у вас установлен **Python 3.10+** и менеджер зависимостей **Poetry**. Если Poetry не установлен, следуйте [официальным инструкциям по установке](https://python-poetry.org/docs/#installation).

Выполните следующие команды в терминале:

1.  Клонируйте репозиторий проекта:
    ```bash
    git clone git@github.com:EgorTitov01/gendiff.git
    ```
    Перейдите в директорию проекта:
    ```bash
    cd gendiff
    ```
2.  Установите все необходимые зависимости с помощью Poetry:
    ```bash
    poetry install
    ```
3.  (Опционально) Активируйте виртуальное окружение, созданное Poetry:
    ```bash
    poetry shell
    ```

## 🚀 Использование

Основной синтаксис команды для сравнения файлов:

```bash
gendiff <путь_к_файлу1> <путь_к_файлу2>
```
По умолчанию используется формат вывода stylish.
Примеры:
Сравнение с использованием формата plain:
```bash
gendiff file1.json file2.json --format plain
```
Сравнение с выводом результата в формате json:
```bash
gendiff file1.yaml file2.yaml --format json
```
Вы также можете сравнивать файлы с разными расширениями (.json и .yaml):
```bash
gendiff file1.json file2.yaml
```

### 📁 Поддерживаемые форматы входных файлов  
Утилита gendiff может обрабатывать файлы следующих форматов:
 * .json
 * .yaml / .yml
### 📤 Поддерживаемые форматы вывода  
Результат сравнения может быть отображен в одном из следующих форматов:
 * stylish: Формат по умолчанию. Представляет собой структурированное, древовидное отображение изменений с индентацией. Показывает добавленные (+), удаленные (-) и измененные (+/-) ключи.
 * plain: Человеко-читаемый, плоский формат. Описывает изменения построчно, указывая путь к измененным значениям.
 * json: Формат JSON. Подходит для интеграции с другими программами или скриптами.  
### 🧪 Тестирование
Для запуска набора тестов проекта выполните команду:
```bash
make test
```

### 🧹 Проверка кода (Линтинг)
Для проверки стиля кода и выявления потенциальных ошибок с помощью линтеров:
```bash
make lint
```

Для одновременного запуска линтера и тестов используйте:
```bash
make check
```

### 👤 Автор
 * Egor Titov
   * [GitHub](https://github.com/EgorTitov01)
   
## Статусы и метрики проекта  
### Hexlet tests and linter status:
[![Actions Status](https://github.com/EgorTitov01/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EgorTitov01/python-project-50/actions)

### CodeClimate mantainability:
[![Maintainability](https://api.codeclimate.com/v1/badges/1cc6d1a3e23453377b93/maintainability)](https://codeclimate.com/github/EgorTitov01/python-project-50/maintainability)

### CodeClimate test coverage:
[![Test Coverage](https://api.codeclimate.com/v1/badges/1cc6d1a3e23453377b93/test_coverage)](https://codeclimate.com/github/EgorTitov01/python-project-50/test_coverage)



