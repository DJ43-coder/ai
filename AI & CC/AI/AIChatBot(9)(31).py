import re

# Function for chatbot response based on user input
def chatbot_response(user_input, user_name):
    user_input = user_input.lower()

    # List of possible responses with regex matching
    responses = {
        r"\b(hello|hi|hey)\b": f"Hello, {user_name}! Welcome to our grocery store. How can I help you today?",
        r"\b(how are you)\b": "I'm just a bot, but I'm here to assist you with groceries!",
        r"\b(order status|track order)\b": "Please provide your order ID to check the status.",
        r"\b(shipping time|delivery time)\b": "We offer same-day delivery and standard shipping (3-5 business days).",
        r"\b(return policy)\b": "You can return items within 7 days if unopened. Would you like help with a return?",
        r"\b(thank you|thanks)\b": f"You're welcome, {user_name}! Let me know if you need anything else.",
        r"\b(milk)\b": "Milk is 30rs per liter.",
        r"\b(eggs)\b": "A dozen eggs cost 80rs.",
        r"\b(rice)\b": "Rice is 50rs per kg.",
        r"\b(price|cost)\b": "Please specify the product name to check its price.",
        r"\b(vegetables|veggies)\b": "We have fresh vegetables available. What are you looking for?",
        r"\b(fruits)\b": "We have apples, bananas, and oranges in stock. Which one do you need?",
        r"\b(snacks)\b": "We have chips, biscuits, and chocolates available.",
        r"\b(beverages|drinks)\b": "We have soft drinks, juices, and bottled water. What would you like?",
        r"\b(buy|order)\b": "You can place an order on our website or visit our store.",
        r"\b(payment methods)\b": "We accept cash, credit/debit cards, and UPI payments.",
        r"\b(store hours|timing)\b": "Our store is open from 8 AM to 10 PM every day.",
        r"\b(location|address)\b": "We are located at XYZ Market, Main Street, City.",
        r"\b(bye|exit)\b": "Are you sure you want to exit? (yes/no)"
    }

    # Loop through the responses dictionary
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # Default response if no match found
    return "I am sorry, I didn't understand that. Here are some things I can help with: 1. Product prices, 2. Order status, 3. Store hours."

# Main interaction loop
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")
user_name = input("What's your name? ")

while True:
    user_message = input(f"{user_name}: ")
    if user_message.lower() in ["bye", "exit"]:
        confirmation = input("Chatbot: Are you sure you want to exit? (yes/no): ")
        if confirmation.lower() == 'yes':
            print(f"Chatbot: Goodbye, {user_name}! Happy shopping!")
            break
    response = chatbot_response(user_message, user_name)
    print(f"Chatbot: {response}")


# Hi
# How are you?
# What is the price of milk?
# How long does delivery take?
# I want to order some eggs.
# Can I return items if I don't need them?
# Thank you! I think I’m done.
# Bye
# Yes
