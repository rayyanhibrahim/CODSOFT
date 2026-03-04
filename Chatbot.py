#phython code
print("Welcome to Simple Chatbot!")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")
    
    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")
    
    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based Chatbot.")
    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
    
    elif user_input == "exit":
        print("Bot: Chat ended.")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")

#output
Welcome to Smart Chatbot!

You: hello
Bot: Hello! Nice to meet you.

You: what is your name?
Bot: I am your assistant chatbot.

You: bye
Bot: Goodbye!

You: exit
Bot: Conversation ended.
