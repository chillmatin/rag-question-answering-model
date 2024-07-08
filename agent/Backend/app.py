import re
from flask import Flask, request, jsonify
import os
import base64
from flask_cors import CORS
from context_decider import Agent  # Import the Agent class
from document_agent import DataAgent  # Import the DataAgent class
from openai import OpenAI
from codeagent import CodeAnalysisAgent
from databaseagent import DBAgent

app = Flask(__name__)

# Ensure the 'files' directory exists
if not os.path.exists('files'):
    os.makedirs('files')

CORS(app, resources={r"/*": {"origins": "*"}})
   

# Initialize the agent with API key and model
api_key = "[ENTER GPT4O API KEY HERE]"
model = "gpt-4o"
agent = Agent(api_key=api_key, model=model)

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()

    if 'formData' in data:
        fields = data['formData'].get('fields', [])
        messages = []
        for field in fields:
            if field['name'] == 'file':
                filename = field['filename']
                content = field['content']
                file_path = os.path.join('files', filename)

                # Decode the base64 content and save the file
                with open(file_path, 'wb') as f:
                    f.write(base64.b64decode(content))

                messages.append(f"File {filename} received successfully.")

        return jsonify({"message": " ".join(messages)})

    elif 'prompt' in data:
        prompt = data['prompt']
        # Use the agent to get the department
        department = agent(prompt)
        
        if department == "AI Document Agent":
            # Initialize and run DataAgent with the prompt
            data_agent = DataAgent(api_key=api_key, folder_path='.')
            response = data_agent.get_answer(prompt)
            return jsonify({"response": response})
        elif department == "AI Code Agent":
            # Initialize and run CodeAgent with the prompt
            code_agent = CodeAnalysisAgent(api_key=api_key)

            # extract filename from prompt using regex pattern i.e animation.py
            file_name = re.findall(r'\w+\.py', prompt)[0]
            print(f"The name of the Python file is: {file_name}")
            response = code_agent.__call__(prompt, file_name, '../codebase/')
            return jsonify({"response": response})
        else:
            # Initialize and run DBAgent with the prompt
            db_agent = DBAgent(api_key=api_key, model=model, db_path='../database/example.db')
            response = db_agent(prompt)
    
            explanation = response["explanation"]
            results = response["results"]

            size = len(results)
            if(size == 1):
                # Add results to the explanation
                for result in results:
                    explanation += f": {result[0]}.\n"
            elif(size == 2):
                # Add results to the explanation
                for result in results:
                    explanation += f": {result[0]} and {result[1]}.\n"
            elif(size == 3):
                # Add results to the explanation
                for result in results:
                    explanation += f": {result[0]}, {result[1]}, and {result[2]}.\n"
            else:
                for result in results:
                    explanation += f": {result[0]}, {result[1]}, {result[2]}, and {result[3]}.\n"
    
            return jsonify({"response": explanation})

    
    return jsonify({"error": "Invalid request."}), 400

if __name__ == '__main__':
    app.run(debug=True)