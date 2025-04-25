from langchain_ollama import ChatOllama
import json

def get_task_breakdown(task_description, model_name="llama3.2"):
    try:
        # Initialize the language model with the specified model
        llm = ChatOllama(model=model_name)
        
        # Create a direct prompt instead of using templates
        prompt = f"""You are a helpful AI assistant that breaks down tasks into detailed, step-by-step instructions.
        
        Please break down this task into clear, numbered steps:
        
        Task: "{task_description}"
        
        Format your response as a JSON object with the following structure:
        {{
            "task": "The original task description",
            "steps": [
                {{"step_number": 1, "description": "First step description"}},
                {{"step_number": 2, "description": "Second step description"}},
                ...
            ]
        }}
        
        Return only the JSON object, with no other text.
        """
        
        # Get response from the model
        response = llm.invoke(prompt)
        
        # Try to parse the response as JSON
        try:
            # Extract JSON if it's wrapped in text
            import re
            json_match = re.search(r'({.*})', response.content, re.DOTALL)
            if json_match:
                text = json_match.group(1)
            else:
                text = response.content
                
            # Parse the JSON
            result = json.loads(text)
            return result
        except Exception as json_error:
            print(f"Error parsing JSON: {json_error}")
            print("Raw response:", response.content)
            return None
            
    except Exception as e:
        print(f"Error calling language model: {e}")
        return None

def main():
    print("Task Breakdown Assistant")
    print("------------------------")
    print("Enter the tasks you want broken down into steps.")
    print("Type 'exit' to quit.")
    print()
    
    while True:
        # Get user input
        task = input("\nEnter a task to break down: ")
        
        # Check if user wants to exit
        if task.lower() in ['exit', 'quit', 'q']:
            print("Goodbye!")
            break
        
        # Skip empty inputs
        if not task.strip():
            continue
        
        print("\nBreaking down your task...")
        result = get_task_breakdown(task)
        
        if result and "steps" in result:
            print(f"\nTask: {result['task']}")
            for step in result['steps']:
                print(f"{step['step_number']}. {step['description']}")
        else:
            print("\nCouldn't generate task breakdown. Please try again with a different task.")

if __name__ == "__main__":
    main()
