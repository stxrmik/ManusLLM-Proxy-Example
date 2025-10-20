# 🧠 Chat with Manus Proxy (OpenAI-compatible API)

[🇷🇺 Русская версия](#-Русская-версия) | [🇬🇧 English version](#-english-version)

---

## 🇷🇺 Русская версия

### 📘 Описание

Этот репозиторий содержит два Python-скрипта для взаимодействия с прокси Manus API, совместимым с OpenAI API.  
Оба файла выполняют одну и ту же задачу — отправляют текстовый запрос к LLM-модели и выводят ответ.  
Различие только в языке комментариев и интерфейса:

- `main_ru.py` — русская версия  
- `main_en.py` — английская версия  

### ⚙️ Требования

- Python 3.9+
- Установленная библиотека [`openai`](https://pypi.org/project/openai/)
- Переменная окружения `MANUS_API_KEY` с вашим API ключом Manus

### 🚀 Установка и запуск

1. Установите зависимости:
   ```bash
   pip install openai

2. Установите переменную окружения с API ключом:
    ```bash
    export MANUS_API_KEY="ваш_ключ"
   ```
   *(в Windows PowerShell:)*
    ```bash
    setx MANUS_API_KEY "ваш_ключ"
3. Запустите скрипт:
    ```bash
   python main_ru.py
4. Пример вывода:
    ```
    🚀 Отправка запроса через прокси: https://api.manus.im/api/llm-proxy/v1/
    🤖 Модель: gemini-2.5-flash
    💬 Ответ от AI:
    --------------------
    Hello! I am an AI assistant.
    --------------------
    📊 Использовано токенов: 42
    ```

### 🔧 Настройки
Вы можете изменить модель, раскомментировав нужную строку в коде:
```
MODEL_TO_USE = "gemini-2.5-flash"
# MODEL_TO_USE = "gpt-4.1-mini"
# MODEL_TO_USE = "gpt-4.1-nano"
```

## 🇬🇧 English Version

### 📘 Description

This repository contains two Python scripts for interacting with the Manus proxy API, which is compatible with the OpenAI API.
Both scripts perform the same logic — sending a text prompt to an LLM model and displaying the AI response.
The only difference is the language of comments and printed messages:

- `main_en.py` — English version  
- `main_ru.py` — Russian version  

### ⚙️ Requirements

- Python 3.9+
- Installed [`openai`](https://pypi.org/project/openai/) library
  - Environment variable `MANUS_API_KEY` containing your Manus API key

### 🚀 Setup and Run

1. Install dependencies:
   ```bash
   pip install openai

2. Set your API key:
    ```bash
    export MANUS_API_KEY="your_key"
   ```
   *(on Windows PowerShell:)*
    ```bash
    setx MANUS_API_KEY "your_key"
3. Run the script:
    ```bash
   python main_en.py
4. Example output:
    ```
    🚀 Sending request via proxy: https://api.manus.im/api/llm-proxy/v1/
    🤖 Model: gemini-2.5-flash
    💬 AI response:
    --------------------
    Hello! I am an AI assistant.
    --------------------
    📊 Tokens used: 42
    ```

### 🔧 Configuration
You can change the model by modifying this line:
```
MODEL_TO_USE = "gemini-2.5-flash"
# MODEL_TO_USE = "gpt-4.1-mini"
# MODEL_TO_USE = "gpt-4.1-nano"
```