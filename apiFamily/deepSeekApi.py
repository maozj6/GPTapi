from openai import OpenAI

if __name__ == '__main__':

    client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )
