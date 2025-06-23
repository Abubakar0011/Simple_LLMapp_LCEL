# LLM Translator with LangChain + FastAPI + Streamlit

This is a simple demo project that shows how to create a Local LLM Translator app using **LangChain**, **Groq API**, **FastAPI**, and **Streamlit**.

## Features

* Translates English text into **French** using a locally hosted chain.
* Built with:

  * **LangChain** for chaining the prompt, model, and output parser
  * **FastAPI** to serve the translation chain as an API
  * **Streamlit** frontend to take user input and display the translated output

## How It Works

1. **FastAPI Server** runs a LangChain pipeline:

   * Takes `text` and `language` as input
   * Sends it to the Groq LLM (`Gemma2-9b-It`)
   * Returns the translated text

2. **Streamlit App**:

   * Takes user input (English)
   * Calls the FastAPI `/chain/invoke` endpoint
   * Displays the translated (French) output

## How to Run

### 1. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

### 2. Run the Streamlit app

```bash
streamlit run app.py
```

## Environment Variables

Create a `.env` file and set your Groq API key:

```
GROQ_API_KEY=your-groq-api-key
```

---

Simple and clean — perfect for beginners testing LangChain + FastAPI pipelines!
