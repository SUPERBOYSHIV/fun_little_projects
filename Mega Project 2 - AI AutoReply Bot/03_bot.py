import pyautogui
import time
import pyperclip
from groq import Groq
import os




client = Groq(
    api_key="<Your API Key>"  # Replace with your actual key
)

def is_last_message_from_sender(chat_log, sender_name="<Exact Name of the person>"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1180, 1050)
pyautogui.click(1180, 1050)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (700, 175) to (1900, 990) to select the text
    pyautogui.moveTo(1850, 960)
    pyautogui.dragTo(736, 367, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1891, 228)
    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        # Send a prompt using Llama 3.3 (70B)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a person named Light Yagami who speaks english. You are from India and are a well known kind person. You need to talk about something random related to the on-going conversation and stall some time. You analyze chat history and respond like a normal person. Output should be the next chat response (text message only). Also keep them short and concise. Only respond with the next message a normal person would send in the chat."
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ],
            # Fast, capable open-source model hosted on Groq
            model="openai/gpt-oss-20b"
        )

        # Print the response text
        response = chat_completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (940, 1036)
        pyautogui.click(940, 1036)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')
