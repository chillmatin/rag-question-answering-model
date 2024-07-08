from langchain.agents import Agent
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import QAGenerationChain

class PDFPromptAgent(Agent):
    def __init__(self):
        super().__init__()

    def load_pdf(self, document_path):
        pdf_loader = PyMuPDFLoader(document_path)
        documents = pdf_loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(documents)
        return chunks

    def generate_answer(self, chunks, prompt):
        qa_chain = QAGenerationChain(prompt=prompt, model_name="your-model-name")
        answers = []
        for chunk in chunks:
            answer = qa_chain.run({"text": chunk['text']})
            answers.append(answer)
        return answers

    def run_agent(self, document_path, prompt):
        chunks = self.load_pdf(document_path)
        answers = self.generate_answer(chunks, prompt)
        return answers
    
    # Create an instance of the agent
agent = PDFPromptAgent()

# Define PDF document path and prompt
document_path = "path/to/your/document.pdf"
prompt = "Your prompt goes here."

# Run the agent
answers = agent.run_agent(document_path, prompt)

# Process the answers
for answer in answers:
    print(answer)

