# Task Breakdown Assistant

## What is Task Breakdown Assistant?

Task Breakdown Assistant is a special helper that breaks big tasks into smaller, easier tasks. It's like when you have a big pile of toys to clean up, and instead of trying to do it all at once, you pick up one toy at a time! The assistant uses a smart computer brain (called llama3.2) to help figure out all the little steps.

## What You Need Before Starting

- A computer with Python installed (ask a grown-up to help with this part)
- The task_breakdown_assistant.py file saved on your computer
- Ollama installed (for AI capabilities)

## How to Install

1. Make sure Python is on your computer
   - Ask a grown-up to download Python from [python.org](https://www.python.org/downloads/)
   - When they install it, tell them to check the box that says "Add Python to PATH"

2. Install Ollama for AI capabilities
   - Ask a grown-up to download Ollama from [ollama.ai](https://ollama.ai/download)
   - Follow the installation instructions on the website
   - Once installed, Ollama will run in the background
   - Make sure to download the llama3 model by typing this command:
     ```
     ollama run llama3
     ```

3. You might need some special helpers for Python
   - Ask a grown-up to open the "Command Prompt" or "Terminal"
   - They should type this and press Enter:
     ```
     pip install -r requirements.txt
     ```
   - If there's no requirements.txt file, they might need to type:
     ```
     pip install langchain-ollama colorama tqdm
     ```

## How to Use Task Breakdown Assistant

### Starting Task Breakdown Assistant

1. Ask a grown-up to open the "Command Prompt" or "Terminal"
2. They should go to the folder where task_breakdown_assistant.py is saved by typing:
   ```
   cd path/to/folder
   ```
3. Then they can start the program by typing:
   ```
   python task_breakdown_assistant.py
   ```

### Using Task Breakdown Assistant

When Task Breakdown Assistant is running:

1. Type in your big task (like "Clean my room")
2. The assistant will show you smaller steps (like "Pick up toys", "Make the bed", "Put away clothes")
3. You can do one small task at a time!
4. The assistant will also show you the steps in a special computer language called JSON, which looks like a list with numbers

## Examples

If you type: "Make a cup of coffee"

Task Breakdown Assistant might show:
1. Boil water.
2. Add coffee grounds to a cup.
3. Pour hot water into the cup.
4. Stir the coffee.
5. Add sugar or milk if desired.

And it will also show this in a special format called JSON that looks like this:
```
{
  "task": "Make a cup of coffee",
  "steps": [
    {"step_number": 1, "description": "Boil water."},
    {"step_number": 2, "description": "Add coffee grounds to a cup."},
    {"step_number": 3, "description": "Pour hot water into the cup."},
    {"step_number": 4, "description": "Stir the coffee."},
    {"step_number": 5, "description": "Add sugar or milk if desired."}
  ]
}
```

## Need Help?

If Task Breakdown Assistant isn't working:

1. Make sure Python is installed correctly
2. Check that you're in the right folder
3. Make sure Ollama is installed and running
4. Check that the llama3 model is downloaded
5. Ask a grown-up to help you

## Fun Tip

You can use Task Breakdown Assistant for anything that seems too big or hard! Like cleaning your room, doing homework, or learning something new!

Remember: Taking small steps makes big jobs easier!

## Technical Details (For Grown-ups)

This application uses:
- Python 3.6 or later
- Langchain Ollama API to communicate with local LLMs
- JSON formatting for structured output
- Regular expressions to extract JSON content from responses

The application breaks down tasks into numbered steps and provides both a human-readable format and a structured JSON output that can be used programmatically.
