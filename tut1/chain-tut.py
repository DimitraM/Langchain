from openai import OpenAI

llm = OpenAI(api_key="sk-a8ff99453a6f4daaa20f271a87e0b91f", base_url="https://api.deepseek.com")

response = llm.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)