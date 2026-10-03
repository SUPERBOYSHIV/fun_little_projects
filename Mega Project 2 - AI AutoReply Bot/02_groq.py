import os
from groq import Groq

# Initialize the Groq client
# You can pass the API key directly, or set the GROQ_API_KEY environment variable
client = Groq(
    api_key="<Your API Key>"  # Replace with your actual key
)

command = '''

'''
# Send a prompt using Llama 3.3 (70B)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a person named Light Yagami who speaks hindi as well as english. You are from India and is a coder. You analyze chat history and respond like Light Yagami"
        },
        {
            "role": "user",
            "content": command
        }
    ],
    # Fast, capable open-source model hosted on Groq
    model="llama-3.3-70b-versatile"
)

# Print the response text
print(chat_completion.choices[0].message.content)
