import os
from groq import Groq

# Initialize the Groq client
# You can pass the API key directly, or set the GROQ_API_KEY environment variable
client = Groq(
    api_key="<Your API Key>"  # Replace with your actual key
)

# Send a prompt using Llama 3.3 (70B)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"
        },
        {
            "role": "user",
            "content": "What is coding"
        }
    ],
    # Fast, capable open-source model hosted on Groq
    model="llama-3.3-70b-versatile"
)

# Print the response text
print(chat_completion.choices[0].message.content)
