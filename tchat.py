from transformers import pipeline
model_name = "gpt2"
generator = pipeline('text-generation', model=model_name, max_length=1000)
def chatbot():
    user_input = input("You: ")
    response = generator(user_input, max_length=1000, do_sample=True, temperature=0.7)
    print("Bot: " + response[0]['generated_text'].split(".")[0] + ".")
while True:
    chatbot()
