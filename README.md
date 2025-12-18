# AI Coding Agent

An AI-powered coding assistant that interacts with your codebase using Google's Gemini API. It can list files, read content, write code, and execute Python scripts, all within a secure working directory.

## Features

- 📁 **File Operations**: List directories and read file contents.
- ✍️ **Code Writing**: Create and modify files.
- 🏃 **Code Execution**: Run Python scripts with arguments.
- 🤖 **AI-Powered**: Uses Google's Gemini 2.5 Flash model.
- 🔒 **Security**: Operations are sandboxed to a working directory.

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Google Gemini API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yoshiioko/aiagent.git
   cd aiagent
   ```
2. **Install uv**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    ```
3. **Create an .env file in the project root with your API key**:
   ```bash
   export GEMINI_API_KEY="your_google_gemini_api_key"
   ```

## Usage
Run AI Agent with prompt:
```bash
uv run main.py "Your prompt here"
```
   
### Example
List files:
```bash
uv run main.py "What files are in this project?"
```

Run tests:
```bash
uv run main.py "Run the tests and tell me if they pass"
```

Use the calculator app:
```bash
uv run main.py "What is 3 + 7 * 2?"
```

## Security
- File operations are sandboxed to the working directory.
- Path traversal attempts are blocked.
- Only Python scripts can be executed.


## License
MIT License - feel free to use this project for learning and development.