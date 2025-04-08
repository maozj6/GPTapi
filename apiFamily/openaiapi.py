

from openai import OpenAI


if __name__ == '__main__':

    client = OpenAI(api_key="API Key") 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
        ]
    )

    print(response.choices[0].message.content)
