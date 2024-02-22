import streamlit as st
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

# Set up HuggingFace Hub configuration
r_id = 'google/gemma-7b-it'
huggingfacehub_api_token = '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'
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token, repo_id=r_id, model_kwargs={'temperature': 0.7, 'max_new_tokens': 500})

# Define prompt template
template = """
Question: {question}
Answer: Let us give a detailed answer to the question without any repetition
"""
prompt = PromptTemplate(template=template, input_variables=['question'])
chain = LLMChain(prompt=prompt, llm=llm)

# Set page title and favicon
st.set_page_config(page_title="Chatbot App", page_icon=":robot_face:")

# Streamlit app
st.title("Chatbot")
st.markdown("---")

# User input
user_input = st.text_input("Ask a question")

# Get chatbot response
if st.button("Ask"):
    with st.spinner("Thinking..."):  # Show a spinner while processing
        response = chain.run(user_input)
        st.success(f"**Response:** {response}")  # Display response with success message

