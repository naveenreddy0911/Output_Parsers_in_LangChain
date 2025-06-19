# Output Parsers in LangChain

This repository demonstrates how to work with **structured output parsers** in LangChain. It covers different ways to parse and validate model outputs, including string parsing, JSON parsing, Pydantic validation, and LangChain’s built-in `StructuredOutputParser`. These techniques ensure reliable extraction of clean, structured data from LLMs for use in downstream applications. You can use these techniques with both closed-source models (like OpenAI, Anthropic, Google) and open-source models (via Hugging Face).

## 📄 File Descriptions

- `StrOutputParser.py`  Basic string output parsing from the language model’s response.

- `JsonOutpurParser.py`  Parses raw JSON output from the model and ensures correct structure.

- `PydanticOutputParser.py`  Uses Pydantic models to validate and parse structured responses.

- `StructuredOutputParser.py`  Demonstrates LangChain’s `StructuredOutputParser` for declarative schema parsing.

## Environment Variables

To use this project, you need to set API keys in a `.env` file in the root directory.

### 📄 .env file format

```env
OPENAI_API_KEY="your_openai_key"
ANTHROPIC_API_KEY="your_anthropic_key"
GOOGLE_API_KEY="your_google_key"
HUGGINGFACEHUB_API_KEY="your_huggingfacehub_key"
```

### Dont have closed-source API key ? 
Refer to the repo [**Models_in_LangChain**](https://github.com/naveenreddy0911/Models_in_LangChain) for using open-sourced Hugging Face chat models (via API or locally).
