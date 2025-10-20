import os
from openai import OpenAI

# Manus Proxy endpoint (OpenAI-compatible)
MANUS_PROXY_URL = "https://api.manus.im/api/llm-proxy/v1/"

# Get API key from environment variable
API_KEY = os.getenv("MANUS_API_KEY")

# Model to use (the proxy may support multiple models)
MODEL_TO_USE = "gemini-2.5-flash"
# MODEL_TO_USE = "gpt-4.1-nano"
# MODEL_TO_USE = "gpt-4.1-mini"


def chat_with_manus_proxy(prompt: str):
    """Send a prompt to the Manus proxy API and display the AI response."""

    if not API_KEY:
        print("❌ Error: API key not found.")
        print("💡 Please set the MANUS_API_KEY environment variable or paste your key directly in the script.")
        return

    print(f"🚀 Sending request via proxy: {MANUS_PROXY_URL}")
    print(f"🤖 Model: {MODEL_TO_USE}")
    print(f"🔑 Using key: {API_KEY[:10]}...{API_KEY[-4:]}")

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

        print("\n💬 AI Response:")
        print("-" * 20)
        print(ai_response)
        print("-" * 20)
        print(f"📊 Tokens used: {response.usage.total_tokens}")

    except Exception as e:
        print(f"\n💥 An error occurred: {e}")


if __name__ == "__main__":
    user_prompt = "Who are you?"
    chat_with_manus_proxy(user_prompt)
