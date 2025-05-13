from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load environment variables (like GOOGLE_API_KEY)
load_dotenv()

# Create a Gemini Chat model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  # 'gemini-pro' is the chat-capable model

chat_history = []  # Store conversation history

# Initial system message (optional, sets behavior)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))  # User input

    # Send entire history to Gemini
    result = model.invoke(chat_history)
    response = result.content

    chat_history.append(AIMessage(content=response))  # AI response
    print(f"AI: {response}")

# Print full history
print("---- Message History ----")
for msg in chat_history:
    print(f"{msg.type}: {msg.content}")
