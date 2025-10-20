import os
from openai import OpenAI

MANUS_PROXY_URL = "https://api.manus.im/api/llm-proxy/v1/"

API_KEY = os.getenv("MANUS_API_KEY")

# Модель для использования (прокси может поддерживать разные модели)
MODEL_TO_USE = "gemini-2.5-flash"
# MODEL_TO_USE = "gpt-4.1-nano"
# MODEL_TO_USE = "gpt-4.1-mini"


def chat_with_manus_proxy(prompt: str):
    if not API_KEY:
        print("❌ Ошибка: API ключ не найден.")
        print("💡 Установите переменную окружения MANUS_API_KEY или впишите ключ в скрипт.")
        return

    print(f"🚀 Отправка запроса через прокси: {MANUS_PROXY_URL}")
    print(f"🤖 Модель: {MODEL_TO_USE}")
    print(f"🔑 Используемый ключ: {API_KEY[:10]}...{API_KEY[-4:]}")

    try:
        client = OpenAI(
            base_url=MANUS_PROXY_URL,
            api_key=API_KEY
        )

        response = client.chat.completions.create(
            model=MODEL_TO_USE,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        ai_response = response.choices[0].message.content
        print("\n💬 Ответ от AI:")
        print("-" * 20)
        print(ai_response)
        print("-" * 20)
        print(f"📊 Использовано токенов: {response.usage.total_tokens}")

    except Exception as e:
        print(f"\n💥 Произошла ошибка: {e}")


if __name__ == "__main__":
    user_prompt = "Who r u?"
    chat_with_manus_proxy(user_prompt)
