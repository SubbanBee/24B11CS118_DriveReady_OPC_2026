# Day 3 - Sweet Crumbs AI Agent
# LangChain and Groq Integration

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent

# Configure Groq
# Set GROQ_API_KEY as an environment variable before running.

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)

# Business assistant instructions
SYSTEM = """
ROLE:
You are a friendly assistant for Sweet Crumbs Home Bakery.

FACTS:
Chocolate Cake costs Rs. 650.
Plum Cake costs Rs. 500.
Both cakes have eggless options.

RULES:
Never invent business information.
For unavailable information, say:
I'll check with the owner.
Calculate totals carefully.

FORMAT:
Keep answers under 50 words.
"""

# Create prompt and chain
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

# Conversation memory
history = []

def ask(question: str) -> str:
    answer = chain.invoke({
        "history": history,
        "question": question
    })

    history.extend([
        ("human", question),
        ("ai", answer)
    ])

    return answer


# Python functions for Day 4 tools
def get_cake_price(cake_name: str) -> int:
    """Return the price of a cake."""
    prices = {
        "chocolate cake": 650,
        "plum cake": 500
    }
    return prices.get(cake_name.lower(), -1)


def check_eggless_availability(cake_name: str) -> str:
    """Check eggless cake availability."""
    available_cakes = ["chocolate cake", "plum cake"]

    if cake_name.lower() in available_cakes:
        return "Eggless version available"

    return "Please check with the owner"


if __name__ == "__main__":
    print(ask("Do you have eggless cakes?"))
    print("Chocolate Cake Price:", get_cake_price("Chocolate Cake"))
    print(check_eggless_availability("Plum Cake"))
