
# Предварительно


Сама установка модуля **требовательна к версиям програмного обеспечивания**

> Предритальная установка

-  Версия Python ([скачать](https://www.python.org/ftp/python/3.11.1/))

```
Python 3.11.1
```

-  Версия TouchDesigner ([скачать](https://derivative.ca/download/archive))

```
64-bit Build 2023.12120
```

# LLMHandler

Содержит .tox файл.
Модуль позволяет вводить фразы/слова и преобразовать их в эмоцию

## Input

#### Single Word

## LLM
Взаимодействие с LLM и её компоненнами

### Options
Настройки LLM

#### Auto LLM Parsed
- Тип: On/Off

On: Автоматически обрабатывает [Input](#input) при его изменении
Off: Автоматически НЕ обрабатывает [Input](#input) при его изменении

### Actions
Отрабатывает функционал LMM

#### Parse Single Word
- Тип: Pulse

Обрабатывает [Single Word](#single-word)

#### Update Table
- Тип: Pulse

Обновляет [Emote_Table](#emote_table)

### Singnals
Технические сигналы модуля. Являются техническими и доступны только для чтения

#### Input Parsed
- Тип: Pulse

Отправляет сигнал при завершении обработки [Input](#input)

## Setup
Предварительная установка утилит для полноценной работы модуля

### Download

#### Python libs
- Тип: Pulse

Устанавривает библиотеки python в директорию с проектом


## About
Общая информация

#### README

Открывает этот readme.md файл

#### Version

Версия модуля

## IN

...

## OUT

### Emote
- Тип: Text DAT

Выводит эмоцию ввиде Text DAT

### Emote_Table
- Тип: Table DAT

Список всех возможных эмоций

- Структура Table

Единственный Column - Индекс 0
Множество Raw - Индекс от 0 до N
