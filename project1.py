#Program to ask for user input and process the sentence to capitalize the first letter and add a point at the end, if it's a question it will add a question mark.
# In the end it will print all the sentences

def generate_sentence(phrase):
    questions = ("What","Why","How")
    phrase_capitalized = phrase.capitalize()
    if phrase_capitalized.startswith(questions):
        return "{}?".format(phrase_capitalized)
    else:
        return "{}.".format(phrase_capitalized)
    
m = "hello world"
q = "how are you"

finish = False
results = []
while not finish:
    message = input("Enter a message: ")
    if message == "\end":
        finish = True
    else:
        final_message = generate_sentence(message)
        results.append(final_message)


print(" ".join(results))

