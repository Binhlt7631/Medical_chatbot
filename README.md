# End-to-end Medical Chatbot Generative AI

## How to run?

### STEPS:

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-repo-url.git
    cd your-repo-url
    ```

2. **Create a conda environment**

    ```bash
    conda create -n medicalbot python=3.10 -y
    conda activate medicalbot
    ```

3. **Install the requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your Pinecone & OpenAI credentials**

    ```ini
    PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

5. **Store embeddings to Pinecone**

    ```bash
    python src/store_index.py
    ```

6. **Run the application**

    ```bash
    python app.py
    ```

7. **Open up localhost**

    ```bash
    open http://localhost:8080
    ```

## Techstack Used:

- Python
- LangChain
- Flask
- Hugging face
- Pinecone



## Project Structure

.
├── .env
├── .gitignore
├── app.py
├── Data/
├── Generative_AI_Project.egg-info/
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── top_level.txt
├── README.md
├── requirements.txt
├── research/
│   └── trials.ipynb
├── setup.py
├── src/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── helper.py
│   └── store_index.py
├── static/
│   └── style.css
├── template.py
└── templates/
    └── index.html




