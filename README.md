# Chatbot App

This is a Streamlit-based chatbot application that utilizes the LangChain library and the Google Gemma 7B language model from Hugging Face Hub. The chatbot can answer questions by providing detailed responses without repetition.

## Features

- User-friendly Streamlit interface
- Integration with the Google Gemma 7B language model from Hugging Face Hub
- Prompt template for generating detailed answers
- Spinner indication while processing user input
- Success message display for the chatbot's response

## Prerequisites

Before running the chatbot app, make sure you have the following prerequisites installed:

- Python (version 3.6 or higher)
- Streamlit (`pip install streamlit`)
- LangChain (`pip install langchain`)
- Hugging Face Hub API token (sign up at [https://huggingface.co/](https://huggingface.co/))

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/chatbot-app.git
```

2. Navigate to the project directory:

```
cd chatbot-app
```

## Usage

1. Set your Hugging Face Hub API token in the code:

```python
huggingfacehub_api_token = 'your_hugging_face_hub_api_token'
```

2. Run the Streamlit app:

```
streamlit run test.py
```

3. The app will open in your default web browser. You can now interact with the chatbot by typing your questions in the text input field and clicking the "Ask" button.

4. The chatbot will process your question and provide a detailed response without repetition.

## Use Case

![Screenshot (159)](https://github.com/Bhudil/ML-ChatBot/assets/99169324/567c6bc4-e059-4bf0-9218-4576e561bd7f)


## Code Structure

- `test.py`: The main script that runs the Streamlit application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the interactive app framework
- [LangChain](https://python.langchain.com/en/latest/index.html) for the language model integration
- [Hugging Face Hub](https://huggingface.co/) for providing the Google Gemma 7B language model
