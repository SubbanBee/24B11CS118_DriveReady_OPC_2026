
# Day 1 - Sweet Crumbs AI Assistant
# Drive Ready AI Agents - One Person Company Initiative

# Install the required library before running:
# pip install openai

from google.colab import userdata
from openai import OpenAI


# Connect to Groq API using the securely stored API key
client = OpenAI(
    api_key=userdata.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"


# Basic bakery assistant instructions
SYSTEM = """ROLE: You are the assistant for Sweet Crumbs Home Bakery.
FACTS: We bake to order. Orders need 24 hours' notice.
All cakes have eggless versions.
Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80.
RULES: Never promise a delivery time.
If the answer isn't in FACTS, say "I'll check with the owner."
FORMAT: Under 50 words, friendly, English or Telugu matching the customer."""


# Function to send a message to the AI model
def ask_ai(question, system_prompt=None, temperature=0.2):
    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature
    )

    return response


# Task 1: Basic AI Assistant
print("\n--- Basic AI Assistant ---")

response = ask_ai(
    "Can I get an eggless cake today evening?",
    SYSTEM
)
print(response.choices[0].message.content)


# Task 2: Temperature Experiment
print("\n--- Temperature Experiment ---")

for temperature in [0.2, 1.2]:
    print(f"\nTemperature: {temperature}")

    for i in range(3):
        response = ask_ai(
            "Suggest a creative tagline for Sweet Crumbs Home Bakery.",
            temperature=temperature
        )
        print(response.choices[0].message.content)


# Task 3: Hallucination Experiment
print("\n--- Hallucination Experiment ---")

response = ask_ai(
    "Do you deliver to Kakinada?",
    system_prompt="You are a helpful assistant for Sweet Crumbs Home Bakery."
)
print(response.choices[0].message.content)


# Task 4: Conversation Memory Experiment
print("\n--- Conversation Memory Experiment ---")

# Separate API requests do not automatically share conversation history
first = ask_ai("My name is Ravi.")
print("First response:", first.choices[0].message.content)

second = ask_ai("What is my name?")
print("Second response:", second.choices[0].message.content)

# Include previous messages to provide conversation context
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "My name is Ravi."},
        {"role": "assistant", "content": "Nice to meet you, Ravi!"},
        {"role": "user", "content": "What is my name?"}
    ]
)
print("With conversation history:", response.choices[0].message.content)


# Task 5: Token Usage Experiment
print("\n--- Token Usage Experiment ---")

questions = [
    "What cakes are available at Sweet Crumbs?",
    "Sweet Crumbs lo ye cakes available ga unnayi?"
]

for question in questions:
    response = ask_ai(question)

    print("\nQuestion:", question)
    print("Answer:", response.choices[0].message.content)
    print("Prompt Tokens:", response.usage.prompt_tokens)


# Task 6: Custom Business Assistant
print("\n--- Custom Business Assistant ---")

BUSINESS_SYSTEM = """ROLE: You are a friendly assistant for Sweet Crumbs Home Bakery.

FACTS:
- We bake cakes to order.
- Orders require 24 hours' notice.
- All cakes have eggless versions.
- Plum cake costs Rs 500.
- Chocolate cake costs Rs 650.

RULES:
- Never promise a delivery time.
- Do not invent prices or menu items.
- If information is unavailable, say "I'll check with the owner."

FORMAT: Keep answers friendly and under 50 words."""

customer_questions = [
    "What is the price of a chocolate cake?",
    "Can I order an eggless cake?",
    "Do you deliver to Kakinada?"
]

for question in customer_questions:
    response = ask_ai(question, BUSINESS_SYSTEM)

    print("\nCustomer:", question)
    print("Assistant:", response.choices[0].message.content)


# Task 7: Ten Common Customer FAQs
print("\n--- Customer FAQs ---")

faqs = [
    "What cakes are available?",
    "Do you make eggless cakes?",
    "What is the price of a plum cake?",
    "What is the price of a chocolate cake?",
    "Do you accept custom cake orders?",
    "How much advance notice is required?",
    "Do you provide home delivery?",
    "Do you deliver to Kakinada?",
    "How can I place an order?",
    "What payment methods do you accept?"
]

for number, question in enumerate(faqs, start=1):
    print(f"{number}. {question}")
