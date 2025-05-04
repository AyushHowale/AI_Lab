def chatbot():
    print("🤖 Welcome to ElectroStore Assistant!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I assist you today?")
        
        elif "laptop" in user_input:
            print("Bot: We have laptops from Dell, HP, and Lenovo. Would you like to know the price?")
        
        elif "price" in user_input:
            print("Bot: Our laptops start from ₹35,000. Would you like to place an order?")
        
        elif "phone" in user_input or "mobile" in user_input:
            print("Bot: We offer Realme, Samsung, and iPhones. Prices start from ₹8,000.")

        elif "order" in user_input:
            print("Bot: To place an order, visit our website or call customer support at 1800-123-456.")

        elif "return" in user_input:
            print("Bot: You can return any product within 7 days of delivery.")

        elif "support" in user_input:
            print("Bot: For support, email us at support@electrostore.com or call 1800-123-456.")

        elif user_input in ['exit', 'bye', 'quit']:
            print("Bot: Thank you for visiting ElectroStore. Have a great day! 👋")
            break

        else:
            print("Bot: I'm sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()