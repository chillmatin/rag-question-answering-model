import sqlite3
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

class DBAgent:
    def __init__(self, api_key, model, db_path):
        self.llm = ChatOpenAI(api_key=api_key, model=model, temperature=0.5)
        self.db_path = db_path

        template = """
        You are an AI SQL expert named Bob.
        Your goal is to give correct, executable SQL queries to users and provide explanations for the results.
        You are given all tables and columns with descriptions. You MUST give queries from the tables and columns below.
        The user will give you a prompt; for each prompt, you should respond and include a SQL query and explanations for the selected employees.

        # Table and Column descriptions:
        Employees:
        EmpID   FirstName LastName  StartDate    ExitDate    Title    EmployeeStatus (it can be Active or Inactive)    PerformanceScore    SolvedNumberoftickets      TicketTimeRate


        # <rules>
        # 1. You MUST wrap the generated SQL queries within ```sql code markdown in this format e.g
        # ```sql
        # (select 1) union(select 2)
        # ```
        # 2. If I don't tell you to find a limited set of results in the sql query, you MUST limit the number of responses to 10.
        # 3. Make sure to generate a single SQL code snippet, not multiple.
        # 4. You should only use the table and columns given, you MUST NOT hallucinate about the table names.
        # 5. Provide a one sentence explanation for the query. It should be clear and concise.
        # 6. Be careful about the query asks for multiple or singular results. If user says "employee" give one, if user says "employees" give multiple.
        # </rules>

        For example:

        User: Give top rated employees who are currently employed.
        return 
        ```sql
        SELECT 
            FirstName, 
            LastName,
            PerformanceScore
        FROM 
            Employees
        WHERE 
            EmployeeStatus = 'Employed'
        ORDER BY 
            PerformanceScore DESC
        LIMIT 3;
        ```

        Explanation: These employees are selected because they are currently employed and have the highest performance scores.

        User: Can you tell me the worst performing employees?
        return
        ```sql
        SELECT 
            FirstName, 
            LastName,
            PerformanceScore
        FROM 
            Employees
        ORDER BY 
            PerformanceScore ASC
        LIMIT 3;
        ```

        Explanation: These employees are selected because they have the lowest performance scores and their ticket time rate is the lowest.

        User: Can you show me the employees who have solved more than 50 tickets?
        return
        ```sql
        SELECT 
            FirstName, 
            LastName, 
            SolvedNumberoftickets
        FROM 
            Employees
        WHERE 
            SolvedNumberoftickets > 50
        LIMIT 10;
        ```
        Explanation: These employees have been selected because they have solved more than 50 tickets.
        
        user prompt:
        {question}
        """
        
        self.prompt = PromptTemplate(template=template, input_variables=["question"])
        self.sequence = self.prompt | self.llm

    def __call__(self, question):
        response = self.sequence.invoke({"question": question})
        sql_query, explanation = self.extract_sql_query_and_explanation(response.content)
        print("Generated SQL Query:")
        print(sql_query)  # Debug: Print the generated SQL query
        print("Explanation:")
        print(explanation)  # Debug: Print the explanation
        results = self.execute_query(sql_query)
        results_with_explanation = {"results": results, "explanation": explanation}
        print(results_with_explanation)
        return results_with_explanation

    def extract_sql_query_and_explanation(self, response):
        start_sql = response.find('```sql') + 6
        end_sql = response.find('```', start_sql)
        sql_query = response[start_sql:end_sql].strip()

        start_explanation = response.find('Explanation:') + len('Explanation:')
        explanation = response[start_explanation:].strip()

        return sql_query, explanation

    def execute_query(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        print("Executing SQL Query:")  # Debug: Notify query execution
        cursor.execute(query)
        results = cursor.fetchall()
        print("Query Results:")  # Debug: Print the results
        for row in results:
            print(row)
        cursor.close()
        conn.close()
        return results

# Initialize the agent
api_key = "GPT4O KEY HERE"
model = "gpt-4o"
db_path = "../database/example.db"
agent = DBAgent(api_key, model, db_path)

# # Test the agent with a sample question
# question = "Give top rated employees who are currently employed."
# response = agent(question)
# print(response)
