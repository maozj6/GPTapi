
# https://github.com/NirDiamant/Prompt_Engineering/blob/main/all_prompt_engineering_techniques/cot-prompting.ipynb
from openai import OpenAI

def standard(question):
    client = OpenAI(api_key="API Key")  

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Answer the question: "+question}
        ]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content

def concise(question):
    client = OpenAI(api_key="API Key")  

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Answer the following question concisely: "+question}
        ]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content

def CoTsimple(question):
    client = OpenAI(api_key="API Key")  

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Answer the following question concisely: "+question+""}
        ]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content

def CoTComplex(question):
    client = OpenAI(api_key="API Key")  

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": """Solve the following problem step by step. For each step:
1. State what you're going to calculate
2. Write the formula you'll use (if applicable)
3. Perform the calculation
4. Explain the result

Question: {question}"""+question
             }
        ]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == '__main__':


    question =  "2. (5 \u5206) \u5df2\u77e5\u590d\u6570 $z=\\frac{\\sqrt{3}+i}{(1-\\sqrt{3} i)^{2}}, \\bar{z}$ \u662f $z$ \u7684\u5171\u8f6d\u590d\u6570, \u5219 $z\\cdot\bar{z}=(\\quad)$\nA. $\\frac{1}{4}$\nB. $\\frac{1}{2}$\nC. 1\nD. 2\n"
    print(question)
    print("standard------")

    standard(question)
    print("concise------")
    concise(question)
    print("simple------")

    CoTsimple(question)
    print("complex------")

    CoTComplex(question)
