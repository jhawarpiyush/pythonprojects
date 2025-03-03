import sys
from datetime import datetime


def get_response(text: str) -> str:
    lowered: str = text.lower()


    if lowered in ["hello", "hi", "hey"]:
        return "Hi there!"
    elif "how are you" in lowered:
        return "I am good thanks!"
    elif "your name" in lowered:
        return "My name is: Bot"
    elif "time" in lowered:
        current_time: datetime = datetime.now()
        return f"The current time is: {current_time:%H:%M %p}"
    elif lowered in ["bye", "see you", "goodbye"]:
        return "It was nice talking to you! Bye!"
    else:
        return f"Sorry, I do not understand: {text}"
    

while True:
    user_input: str = input("You: ")

    if user_input == "exit" or user_input == "quit":
        print("Bot: It was pleasure talking to you!")
        sys.exit()

    bot_response: str = get_response(user_input)
    print(f"Bot: {bot_response}")
    