import os 
import openai


openai.api_key = "YOUR-API-KEY-HERE"


completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {
            "role":"user",
            "content": "Greet me in the style of a pirate"
        }
    ]
)


# prinnt the response
print("\n"+completion.choices[0].message.content)

print("hello world")