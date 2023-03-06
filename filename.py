import random

# Define possible responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing great, thanks!", "I'm fine, thank you for asking."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I don't understand.", "Can you please rephrase that?", "I'm not sure what you mean."],
}

# Define a function to generate a response
def get_response(message):
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    else:
        return random.choice(responses["default"])

# Define the main function to run the chatbot
def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        message = input("You: ")
        if message.lower() == "bye":
            print(get_response("bye"))
            break
        else:
            print("Chatbot:", get_response(message))

# Call the main function to run the chatbot
if __name__ == "__main__":
    main()
