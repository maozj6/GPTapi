import requests
import json

# API 端点和密钥
api_key = "your_api_key_here"

api_url = "https://api.openai.com/v1/chat/completions"

if __name__ == '__main__':

    # 请求数据
    data = {
        "model": "gpt-4",  # 选择 GPT-4o 或 gpt-3.5-turbo
        "messages": [
            {"role": "system", "content": "You are an assistant that provides helpful responses."},
            {"role": "user", "content": "What is the capital of France?"}
        ],
        "max_tokens": 10,
        "logprobs": True,  # 启用 logprobs 来获取 token 预测概率
        "top_logprobs": 5  # 返回每个 token 的前 5 个最高概率
    }

    # 请求头
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 发送 POST 请求
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # 解析响应
    if response.status_code == 200:
        result = response.json()

        for choice in result["choices"]:
            print("Generated text:", choice["message"]["content"])
            print("\nLogprobs data for each token:")

            # 检查 logprobs 数据
            if "logprobs" in choice and "content" in choice["logprobs"]:
                token_logprobs = choice["logprobs"]["content"]

                for i, token_info in enumerate(token_logprobs):
                    print(f"Token {i + 1}: {token_info['token']}")
                    print("Top logprobs:")

                    # 检查 top_logprobs 的格式
                    if isinstance(token_info["top_logprobs"], list):
                        for prob in token_info["top_logprobs"]:
                            token_candidate = prob.get("token", "")
                            logprob = prob.get("logprob", None)
                            print(f"  {token_candidate}: {logprob}")
                    else:
                        print("  No top_logprobs available for this token.")
            else:
                print("No logprobs found in response.")
    else:
        print("Error:", response.status_code, response.json())
