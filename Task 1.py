import re
def get_response(user_input):
    user_input=user_input.lower()
    if re.search(r'\b(hi|hello|hey)\b',user_input):
        return "how can i assist you today?"
    elif re.search(r'\b(your name|who are you)\b',user_input):
        return "I am rule bot,your friendly chatbot!"
    elif re.search(r'\b(how are you|how do you do)\b',user_input):
        return "I am doing great!, Thanks for asking"
    elif re.search(r'\b(help|what can you do)\b',user_input):
        return "I can answer simple questions,greet you and chat with you.Try asking what is your name"
    elif re.search(r'\b(bye|exit|quit)\b',user_input):
        return "Bye!,Have a great day"
    else:
        return "I am sorry,I didn't understand.Can you rephrase?"

def chatbot():
    print("rule bot:Hi I am Rule bot. Type 'bye' to end the conversation")
    while True:
        user_input=input("you:")
        response=get_response(user_input)
        print(f"rule bot:{response}")
        if "bye" in response.lower():
            break
chatbot()
