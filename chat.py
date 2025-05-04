
def chatbot():
    print("ChatBot: Hi! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'hello':
            print("ChatBot: Hello! How can I help you?")
        elif user_input == 'how are you':
            print("ChatBot: I'm just a bunch of code, but thanks for asking!")
        elif user_input == 'what is your name':
            print("ChatBot: I'm ChatBot 101.")
        elif user_input == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("ChatBot: Sorry, I don't understand that.")

chatbot()
