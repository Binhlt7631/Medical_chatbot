from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import HuggingFaceHub
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


embeddings = download_hugging_face_embeddings()


index_name = "medicalbot"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})


llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    task="text-generation",
    model_kwargs={"temperature": 0.3, "max_length": 200},
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)


qa_chain = load_qa_chain(llm=llm, chain_type="stuff" )

# Create Retrieval-QA pipeline
qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=retriever)



def extract_answer(result):
    answer_start = result.find("Answer:")
    if answer_start != -1:
        answer_end = result.find("Answer:", answer_start + len("Answer:"))
        if answer_end != -1:
            return result[answer_start + len("Answer:"):answer_end].strip()
        else:
            return result[answer_start + len("Answer:"):].strip()
    return result.strip()



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = extract_answer(qa.run(input))
    print("Response : ", response)
    return str(response)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
