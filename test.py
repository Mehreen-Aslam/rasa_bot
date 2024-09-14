# from transformers import pipeline

# # Initialize GPT-2 from Hugging Face
# generator = pipeline('text-generation', model='gpt2')

# # Provide input to GPT-2
# user_input = "i am sad"

# # Generate a response
# response = generator(user_input, max_length=50, num_return_sequences=1)

# # Print the generated response
# print(response[0]['generated_text'])
from transformers import pipeline

# Initialize GPT-2 from Hugging Face
generator = pipeline('text-generation', model='gpt2')

while True:
    # Ask user for input
    user_input = input("How are you feeling? ")

    # Generate a response from GPT-2
    response = generator(user_input, max_length=50, num_return_sequences=1)

    # Print the generated response
    print(response[0]['generated_text'])

    # Optionally, you can break the loop if the user wants to exit
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Goodbye!")
        break
