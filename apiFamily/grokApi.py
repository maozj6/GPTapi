import os
from openai import OpenAI


if __name__ == '__main__':

    client = OpenAI(
        api_key="<YOUR_XAI_API_KEY_HERE>",
        base_url="https://api.x.ai/v1",
    )

    completion = client.chat.completions.create(
        model="grok-2-latest",
        messages=[
            {"role": "system", "content": "You are a PhD-level mathematician."},
            {"role": "user", "content": "What is 2 + 2?"},
        ],
    )

    print(completion.choices[0].message)
