from openai import OpenAI
class CodeAnalysisAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    def __call__(self, question, file_name, codebase_dir):
        code = self.get_code_file_content(file_name, codebase_dir)
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant specialized in analyzing Python code. "
                        "Based on the content of the code file, please answer the following question: "
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"{question}\n\n"
                        f"Based on the content of the code file: {code}\n\n"
                        "If the answer is not directly available in the code, provide the most relevant "
                        "information you can infer from the code structure and content."
                    )
                }
            ],
            max_tokens=100,
            n=1,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    
    def get_code_file_content(self, file_name, codebase_dir):
        code = self.read_python_file(f"{codebase_dir}/{file_name}")

        # turn code into a string
        code = code.__str__()
        return code
    
    def read_python_file(self, file_path):
        with open(file_path, 'r') as f:
            code = f.read()
        return code





# # Example usage
# file_name = "animation.py"
# codebase_dir = "/home/cuneyd/agent/codebase"
# question = "What is the size of edges array in animation.py?"

# # Get the answer from the agent
# answer = agent(question, file_name, codebase_dir)
# print(f"Question: {question}\nAnswer: {answer}")