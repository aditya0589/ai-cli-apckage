from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


class GeminiChatBot:
    def __init__(self, system_prompt="You are a helpful AI assistant."):
        # Load environment variables (like GOOGLE_API_KEY)
        load_dotenv()
        
        # Initialize the Gemini model
        self.model = ChatGoogleGenerativeAI(model="gemini-pro")
        
        # Initialize chat history with a system message
        self.chat_history = [SystemMessage(content=system_prompt)]

    def take_input(self):
        """Takes user input from the console."""
        return input("You: ")

    def get_response(self, user_input):
        """Sends user input to the model and gets AI response."""
        self.chat_history.append(HumanMessage(content=user_input))  # Add user message
        result = self.model.invoke(self.chat_history)               # Get AI response
        response = result.content
        self.chat_history.append(AIMessage(content=response))       # Add AI response
        return response

    def start_chat(self):
        """Runs a loop for continuous chatting."""
        print("Type 'exit' to end the chat.")
        while True:
            query = self.take_input()
            if query.lower() == "exit":
                break
            response = self.get_response(query)
            print(f"AI: {response}")
        print("---- Chat Ended ----")
        self.show_history()

    def show_history(self):
        """Prints the chat history."""
        for msg in self.chat_history:
            print(f"{msg.type}: {msg.content}")


# Usage
if __name__ == "__main__":
    chatbot = GeminiChatBot()
    chatbot.start_chat()
