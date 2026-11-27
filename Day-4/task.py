
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.tools import tool

# Sweet Crumbs menu
MENU = {
    "chocolate cake": 650,
    "plum cake": 500
}

# Tool 1: Get cake price
@tool
def get_price(cake_name: str) -> str:
    """Get the price of a cake from the Sweet Crumbs menu."""
    price = MENU.get(cake_name.lower())

    if price is None:
        return "Cake not found. Please check with the owner."

    return f"{cake_name}: Rs. {price}"


# Tool 2: Check business hours
@tool
def is_open() -> str:
    """Check whether Sweet Crumbs bakery is currently open."""
    return "Business hours are not available. Please check with the owner."


# Pydantic Order Model
class Order(BaseModel):
    name: str
    item: Literal["Chocolate Cake", "Plum Cake"]
    qty: int = Field(gt=0)
    date: str
    eggless: bool


# Tool 3: Record a practice order
@tool
def log_order(order: Order) -> str:
    """Validate and record a practice order in Google Sheets."""
    validated_order = Order.model_validate(order)

    price = MENU[validated_order.item.lower()]
    total = price * validated_order.qty

    ws.append_row([
        validated_order.name,
        validated_order.item,
        validated_order.qty,
        validated_order.date,
        validated_order.eggless,
        total
    ])

    return f"Practice order recorded successfully! Total: Rs. {total}"


# AI Agent configuration
tools = [get_price, is_open, log_order]

system_prompt = """
You are the AI assistant for Sweet Crumbs Home Bakery.

Available cakes:
- Chocolate Cake: Rs. 650
- Plum Cake: Rs. 500

Both cakes have eggless versions available.

Use tools to check prices and business hours.
Collect all required order details before recording a practice order.
Never accept unknown cakes or quantities below 1.
Never invent delivery, business hours or advance-booking details.
Practice orders are not real bakery bookings.
"""

print("Day 4 task.py created successfully!")
print("Tools:", [t.name for t in tools])
