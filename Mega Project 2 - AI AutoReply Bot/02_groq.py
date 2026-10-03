import os
from groq import Groq

# Initialize the Groq client
# You can pass the API key directly, or set the GROQ_API_KEY environment variable
client = Groq(
    api_key="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"  # Replace with your actual key
)

command = '''
[1:42 am, 4/8/2026] Light Yagami: Thx for the ingame assist btw 😎
[1:42 am, 4/8/2026] Garvit Rawat: Np np
[3:11 pm, 4/8/2026] Garvit Rawat: When u free from driving school?
[3:13 pm, 4/8/2026] Light Yagami: Just sat down atm
[3:13 pm, 4/8/2026] Light Yagami: Will take atleast an hour
[3:13 pm, 4/8/2026] Light Yagami: 20 mins each, so yea
[4:03 pm, 4/8/2026] Garvit Rawat: Now u free?
[4:17 pm, 4/8/2026] Light Yagami: Well just reached society
[4:17 pm, 4/8/2026] Light Yagami: Gonna go up
[4:17 pm, 4/8/2026] Garvit Rawat: Which society?
[4:17 pm, 4/8/2026] Garvit Rawat: Soul society?
[4:17 pm, 4/8/2026] Light Yagami: Lmao
[4:22 pm, 4/8/2026] Light Yagami: Alr m home now
[4:26 pm, 4/8/2026] Garvit Rawat: V good
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