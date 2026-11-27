
import json

# Day 2 - Sweet Crumbs AI Chatbot

business_catalogue = {
    "business_name": "Sweet Crumbs Home Bakery",
    "products": {
        "Chocolate Cake": {
            "price": 650,
            "eggless_available": True
        },
        "Plum Cake": {
            "price": 500,
            "eggless_available": True
        }
    }
}

chat_history = []

def calculate_total(price: int, quantity: int) -> int:
    return price * quantity


def process_order(customer_name, cake_type, quantity, eggless):
    try:
        quantity = int(quantity)

        if quantity <= 0:
            print("Please enter a valid quantity.")
            return

        if cake_type not in business_catalogue["products"]:
            print("Sorry, this cake is not available.")
            return

        price = business_catalogue["products"][cake_type]["price"]
        total = calculate_total(price, quantity)

        order = {
            "customer_name": customer_name,
            "cake_type": cake_type,
            "quantity": quantity,
            "price": price,
            "total_amount": total,
            "eggless": eggless
        }

        print("\nProcessing customer order...")
        print(json.dumps(order, indent=4))
        print("Order placed successfully!")

    except ValueError:
        print("Invalid quantity! Please enter a number.")
    except Exception as error:
        print("Something went wrong:", error)


def bakery_chatbot(customer_message):
    chat_history.append({
        "role": "user",
        "content": customer_message
    })

    messages = [
        {
            "role": "system",
            "content": """
            You are a friendly assistant for Sweet Crumbs Home Bakery.

            Business Facts:
            - Chocolate Cake costs Rs. 650.
            - Plum Cake costs Rs. 500.
            - All cakes are available in eggless versions.

            Rules:
            - Remember the conversation history.
            - Never invent prices or business information.
            - If information is unavailable, say so politely.
            - Give short and helpful answers.
            """
        }
    ] + chat_history

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.2
    )

    answer = response.choices[0].message.content

    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    return answer


# Sample chatbot interaction
print("Customer:", "What is the price of chocolate cake?")
print("Assistant:", bakery_chatbot("What is the price of chocolate cake?"))

print("\nCustomer:", "My name is Ravi.")
print("Assistant:", bakery_chatbot("My name is Ravi."))

print("\nCustomer:", "What is my name?")
print("Assistant:", bakery_chatbot("What is my name?"))

# Sample customer order
print("\nCustomer Order:")
process_order("Ravi", "Chocolate Cake", 2, True)
