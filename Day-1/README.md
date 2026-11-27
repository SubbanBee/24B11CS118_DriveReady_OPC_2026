# Day 1 - Sweet Crumbs AI Assistant

## 1. Objective
The objective of Day 1 was to understand the basics of Large Language Models (LLMs), API integration, prompts, temperature, hallucinations, conversation history, and token usage by building a simple AI assistant for Sweet Crumbs Home Bakery.

## 2. Tools and Technologies
- Python
- Google Colab
- Groq API
- OpenAI Python Library
- GPT-OSS-20B Model

## 3. Tasks Implemented

### Task 1: Groq API Connection
Installed the OpenAI Python library and connected to the Groq API using an API key stored securely in Google Colab Secrets.

### Task 2: Basic AI Assistant
Created a basic bakery assistant using a system prompt containing business information, pricing, and response rules.

### Task 3: Temperature Experiment
Compared AI responses at low and high temperature settings to understand how temperature affects response consistency and creativity.

### Task 4: Hallucination Experiment
Tested the AI without providing business facts and observed how it generated unsupported delivery information and contact details.

### Task 5: Conversation Memory Experiment
Compared separate API requests with requests containing conversation history to understand how an AI model uses previous messages.

### Task 6: Token Usage Experiment
Compared prompt token usage for English and Telugu questions to observe differences in tokenization.

### Task 7: Custom Business Assistant
Built a customer-support assistant for Sweet Crumbs Home Bakery using business facts and rules.

Tested the assistant with:
- Chocolate cake price enquiry.
- Eggless cake availability.
- Delivery availability in Kakinada.

### Task 8: Customer FAQs
Prepared 10 common customer questions that a bakery assistant should be able to answer.

## 4. Key Learnings
- How to connect Python applications to the Groq API.
- How system prompts control AI behaviour.
- How temperature affects AI responses.
- Why hallucinations occur when reliable information is missing.
- How conversation history provides context to an AI model.
- How token usage can differ between languages.
- How to build a basic business-focused AI assistant.

## 5. Files Included
- `task.py` - Python source code.
- `Sweet_Crumbs_AI_Day1.ipynb` - Google Colab notebook containing the implementation and experiment outputs.
- `README.md` - Task description, implementation details, and learnings.

## 6. Conclusion
Successfully completed the Day 1 practical tasks by building and testing a basic AI-powered customer-support assistant for Sweet Crumbs Home Bakery.
