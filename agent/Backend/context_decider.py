from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

class Agent:
    def __init__(self, api_key, model):
        self.llm = ChatOpenAI(api_key=api_key, model=model)
        template = (
            "You are a helpful assistant. Based on the question, decide which department should handle it. "
            "Here are the departments and their responsibilities:\n"
            "1. AI Code Agent: for code-related questions or explaining a code file. If prompt contain code file then return it\n"
            "2. AI Document Agent: for document-related questions\n"
            "3. AI Database Agent: for database-related questions. If prompt requires database search (usually judgements due to employee's stats) u should use this. \n"
            "Question: {question}"
            "\nReturn the department name only."
        )
        self.prompt = PromptTemplate(template=template, input_variables=["question"])
        self.sequence = self.prompt | self.llm

    def __call__(self, question):
        response = self.sequence.invoke({"question": question})
        return response.content.strip()

# Initialize the agent with API key and model
api_key = "[GPT4O KEY HERE]"
model = "gpt-4o"
agent = Agent(api_key=api_key, model=model)

# Test the agent with sample questions
questions = [
    
]

for question in questions:
    department = agent(question)
    print(f"Question: {question}\nDepartment: {department}\n")