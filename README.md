# AI Assistant Project

This is the project we made in [Kuika AI Hackathon](https://tr.kuika.com/kuika-ai-hackathon) as Finetuners team.

## Agents

The project includes the following agents to handle specific types of queries:

1. **Context Decider Agent**:
    - Decides which department (agent) should handle the user's query.
    - Utilizes `langchain.prompts` and `ChatOpenAI`.

2. **Code Analysis Agent**:
    - Analyzes Python code files and answers code-related questions.
    - Uses the OpenAI API for code analysis.

3. **Document Agent**:
    - Processes and analyzes various document types (PDF, DOCX, PPTX).
    - Extracts and summarizes content from documents.

4. **Database Agent**:
    - Executes SQL queries on a SQLite database.
    - Provides explanations for query results.
