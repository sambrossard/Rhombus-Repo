from transformers import pipeline, AutoTokenizer, TFAutoModelForQuestionAnswering

model = TFAutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

input_data = {
    'what is the capital of France?': 'Paris',
    'what is the capital of Germany?': 'Berlin',
    'what is the capital of Spain?': 'Madrid',
    'what is the capital of Italy?': 'Rome',
    'what is the capital of Portugal?': 'Lisbon',
    'what is the capital of Poland?': 'Warsaw'
}


knowledge_base = {}
for question, answer in input_data.items():
    knowledge_base[question] = answer

def answer_question(question):
    if question in knowledge_base:
        return knowledge_base[question]
    else:
        result = qa_pipeline(question=question, context=' '.join(input_data.keys()))
        if 'answer' in result:
            return result['answer']
        else:
            print("Answer not found in the knowledge base.")
    


question = 'what is the capital of France?'
answer = answer_question(question)
print(f"Answer to '{question}': {answer}")




