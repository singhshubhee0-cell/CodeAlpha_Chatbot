# Simple Rule-Based Chatbot in Python

def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot.")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()  # take input from user

        # Rule-based responses
        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm fine, thanks for asking!")
        elif "what is your name" in user_input:
            print("🤖 Chatbot: I'm a simple rule-based bot created in Python.")
        elif "bye" in user_input or "exit" in user_input:
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Try something else!")

# Run the chatbot
chatbot()
