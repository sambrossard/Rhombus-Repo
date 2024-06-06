from langchain_community.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.llms import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from PyPDF2 import PdfReader
from datasets import load_dataset
import cassio
from typing_extensions import Concatenate
from langchain.text_splitter import CharacterTextSplitter

ASTRA_DB_APPLICATION_TOKEN = ''
ASTRA_DB_ID = ''
OPENAI_API_KEY = ''
pdf_reader = PdfReader(open('/Users/samuelbrossard/python/projectvenv/HM test RFP.pdf', 'rb'))
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, db_id=ASTRA_DB_ID)
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

class PreProcess:
    def process_pdf(pdf_reader):
        raw_text = ''
        for i, page in enumerate(pdf_reader.pages):
            content = page.extract_text()
            if content:
                raw_text += content
            else:
                print(f"Warning: Unable to extract text from page {i + 1}")
        print(raw_text)
        return raw_text

    result = process_pdf(pdf_reader)
    print(result)

    def vector_store(result):
        astra_vector_store = Cassandra(
            embedding=embedding,
            table_name =" wa_mini_demo",
            session=None,
            keyspace=None,
        )

        text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 800,
            chunk_overlap = 200,
            length_function = len,
        )
        text = text_splitter.split_text(result)
        text[:50]
        astra_vector_store.add_texts(text[:50])
        print ("inserted %i texts" % len(text[:50]))
        astra_vector_index = VectorStoreIndexWrapper(astra_vector_store)

class QA: ## update class
    def questions():
        first_question = True
        while True:
            if first_question:
                pass
            else:
                pass
     
if __name__ == "__main__":
    caller = PreProcess()
    PreProcess.vector_store()
    