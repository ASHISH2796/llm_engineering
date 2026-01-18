def readSystemPrompt():
    file_path = 'travelagent_system_prompt.txt' 

    try:
        # Specify encoding='utf-8' for proper character handling
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        
        print("File content successfully read with UTF-8 encoding.")
        return file_content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
