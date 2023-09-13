import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me some ideas for fintech apps I could build for my start up "}])
print(completion.choices[0].message.content)