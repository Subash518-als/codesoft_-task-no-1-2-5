def chatbot_response(user_input):
    # Normalize the input
    user_input = user_input.lower()

    # Predefined responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I am a chatbot created to assist you. What's your name?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Chatbot interaction loop
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot()
