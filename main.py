import requests
import json

# API 端点和密钥
api_key = "your_api_key_here"

api_url = "https://api.openai.com/v1/chat/completions"

if __name__ == '__main__':

    # 请求数据
    data = {
        # "model": "gpt-4",
        "model": "gpt-3.5-turbo", 

        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
        ],
        "max_tokens": 50
    }

    # 请求头
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 发送 POST 请求
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # 解析并打印响应
    if response.status_code == 200:
        result = response.json()
        print("AI Response:", result['choices'][0]['message']['content'])
    else:
        print("Error:", response.status_code, response.json())
