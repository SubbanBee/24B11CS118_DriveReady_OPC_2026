
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from google.colab import userdata

# Groq configuration
groq_api_key = userdata.get("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=groq_api_key,
    temperature=0
)

# Conversation memory
memory = InMemorySaver()

# Confirmed bakery information
SYSTEM = """
You are the AI assistant for Sweet Crumbs Home Bakery.

Confirmed menu:
- Chocolate Cake: Rs. 650
- Plum Cake: Rs. 500
- Both cakes have eggless versions.

Never invent delivery, payment, booking or business-hour details.
Do not claim that an order is confirmed.
If information is unknown, say:
"I'll check with the owner."
"""

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Bakery FAQ documents
faq_documents = [
    "Chocolate Cake costs Rs. 650.",
    "Plum Cake costs Rs. 500.",
    "Both Chocolate Cake and Plum Cake are available in eggless versions.",
    "Delivery information is not available. Please check with the owner.",
    "Business hours are not available. Please check with the owner.",
    "Cupcake availability is not confirmed. Please check with the owner."
]

# ChromaDB
vector_store = Chroma.from_texts(
    texts=faq_documents,
    embedding=embeddings,
    collection_name="sweet_crumbs_faq"
)

# FAQ search tool
@tool
def search_faq(question: str) -> str:
    """Search Sweet Crumbs bakery FAQs and policies."""
    results = vector_store.similarity_search(question, k=3)

    if not results:
        return "Information not available. Please check with the owner."

    return "\n".join(doc.page_content for doc in results)

# RAG-enabled agent
agent = create_agent(
    model=llm,
    tools=[search_faq],
    system_prompt=SYSTEM,
    checkpointer=memory
)

# Customer chat function
def chat(thread_id, message):
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    response = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config
    )

    return response["messages"][-1].content

print("Sweet Crumbs Day 5 AI Agent is ready!")
