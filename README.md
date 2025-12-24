# Browser Use Examples

This folder contains examples of using the `browser-use` library for automated browser interactions powered by LLMs.

## What is Browser-Use?

Browser-Use is a Python library that enables AI agents to interact with web browsers through natural language instructions. It allows you to automate complex web interactions by simply describing what you want to accomplish.

## Requirements

### Prerequisites
- Python 3.8+
- A Browser-Use API key (for cloud mode) or local browser setup
- API keys for LLM providers (OpenAI, Anthropic, Ollama, etc.)

### Python Dependencies
```bash
pip install browser-use
pip install python-dotenv
pip install pandas
```

Or install from requirements.txt if available in the parent directory.

## Setup

### 1. Environment Variables

Create a `.env` file in the project root with the following:

```env
# For Browser-Use Cloud (optional)
BROWSER_USE_API_KEY=your-browser-use-api-key

# For OpenAI models
OPENAI_API_KEY=your-openai-api-key

# For custom search (find_influencer.py)
BEARER_TOKEN=your-heytessa-api-key
```

### 2. Get API Keys

- **Browser-Use Cloud API**: Get from [https://cloud.browser-use.com/new-api-key](https://cloud.browser-use.com/new-api-key)
- **OpenAI API Key**: Get from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Hey Tessa API** (for influencer search): Get from [https://www.heytessa.ai/](https://www.heytessa.ai/)

### 3. For Local Browser Control

Some examples use Chrome DevTools Protocol (CDP). To enable:

**Option A: Chrome with Remote Debugging**
```bash
# Windows
chrome.exe --remote-debugging-port=9222

# Mac
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

## Files Overview

### 1. `simple_use.py` - Basic Example
**Purpose**: Simple demonstration of browser automation

**What it does**: Searches for the browser-use GitHub repository and counts its stars

**Usage**:
```bash
python simple_use.py
```

**Test**: Should successfully find and display the number of stars on the browser-use GitHub repo

---

### 2. `browser_use_llm.py` - Cloud Setup Example
**Purpose**: Demonstrates using Browser-Use with cloud API

**What it does**: Same as simple_use.py but configured for cloud usage

**Requirements**: 
- `BROWSER_USE_API_KEY` environment variable

**Usage**:
```bash
python browser_use_llm.py
```

**Test**: Verify it connects to Browser-Use cloud and retrieves GitHub stars

---

### 3. `ollama_model.py` - Local LLM Example
**Purpose**: Use Browser-Use with Ollama (local LLM)

**Setup**:
1. Install Ollama: [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
2. Start Ollama server: `ollama serve`
3. Download model: `ollama pull llama3.1:8b` (4.9GB)

**What it does**: Finds founders of browser-use using a local Llama model

**Usage**:
```bash
python ollama_model.py
```

**Test**: Should complete the search using local Llama model without requiring OpenAI API

---

### 4. `follow_up_tasks.py` - Sequential Tasks
**Purpose**: Demonstrates how to chain multiple tasks in a single browser session

**What it does**: 
1. Searches for "browser-use"
2. Returns the title of the first result

**Usage**:
```bash
python follow_up_tasks.py
```

**Test**: Should keep browser alive and successfully complete both tasks sequentially

---

### 5. `price_compare_agent.py` - Structured Output Example
**Purpose**: Price comparison across multiple marketplaces with structured data extraction

**What it does**: 
- Searches for an item on eBay, Amazon, and Swappa
- Extracts product listings with title, price, condition, URL
- Returns structured data using Pydantic models

**Requirements**:
- Local Chrome with remote debugging on port 9222

**Usage**:
```bash
python price_compare_agent.py
```
Then enter the item to search (default: "Used iPhone 12")

**Test**: Should return 6-9 listings across three platforms with structured data

---

### 6. `grocery_agent.py` - E-commerce Automation
**Purpose**: Automated grocery shopping with login

**What it does**:
- Logs into Instacart
- Searches for specified items
- Adds items to cart
- Returns structured cart data

**Credentials** (for testing):
- Email: test@example.com
- Password: 12345678

**Usage**:
```bash
python grocery_agent.py
```
Enter comma-separated items (default: "milk, eggs, bread")

**Test**: Should successfully add items to Instacart cart and return structured results

---

### 7. `find_influencer.py` - Custom Tools & Web Search
**Purpose**: Find social media profiles using custom search tools

**What it does**:
1. Extracts username from TikTok video
2. Searches web for social media profiles
3. Returns structured list of profile URLs

**Requirements**:
- `BEARER_TOKEN` for Hey Tessa API
- `OPENAI_API_KEY`

**Usage**:
```bash
python find_influencer.py
```

**Test**: Should extract TikTok username and find associated social media profiles

---

### 8. `signup_agent.py` - Complete Workflow Example
**Purpose**: Multi-step workflow for account creation and onboarding

**What it does**:
1. Creates temporary email on tmailor.com
2. Signs up for a service (example.com)
3. Completes onboarding forms

**Additional Files Needed**:
- `first_names.csv` - List of first names
- `last_names.csv` - List of last names

**Usage**:
```bash
python signup_agent.py
```

**Test**: Should create temp email, save credentials to `email-password.csv`, and complete signup

---

## Testing Tips

### Verify Setup
```bash
# Check if browser-use is installed
python -c "import browser_use; print('✓ browser-use installed')"

# Check environment variables
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('BROWSER_USE_API_KEY:', 'Set' if os.getenv('BROWSER_USE_API_KEY') else 'Not Set')"
```



