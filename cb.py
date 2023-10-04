from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

while True:
    user_input = input("Tú: ")
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    response = model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=model.config.pad_token_id)
    bot_response = tokenizer.decode(response[0], skip_special_tokens=True)
    print(f"Bot: {bot_response}")
