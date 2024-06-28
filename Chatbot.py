import re

def simple_chatbot():
    print("Hello! I'm a versatile chatbot. You can start chatting with me.")
    
    while True:
        user_input = input("You: ").lower()
        
        # Regular expressions to match specific types of queries
        if re.search(r'\b(hello|hi)\b', user_input):
            print("Bot: Hi there!")
        elif re.search(r'\b(how are you)\b', user_input):
            print("Bot: I'm doing well, thank you!")
        elif re.search(r'\b(what is your name)\b', user_input):
            print("Bot: I'm just a simple chatbot.")
        elif re.search(r'\b(who created you)\b', user_input):
            print("Bot: I was created by OpenAI.")
        elif re.search(r'\b(tell me a joke)\b', user_input):
            print("Bot: Why don't scientists trust atoms? Because they make up everything!")
        elif re.search(r'\b(favorite music|music genre)\b', user_input):
            print("Bot: I enjoy electronic and classical music.")
        elif re.search(r'\b(pizza|favorite food)\b', user_input):
            print("Bot: Pizza is delicious, especially with extra cheese!")
        elif re.search(r'\b(invent the light bulb|who created the light bulb)\b', user_input):
            print("Bot: Thomas Edison is credited with inventing the light bulb.")
        elif re.search(r'\b(capital of france)\b', user_input):
            print("Bot: The capital of France is Paris.")
        elif re.search(r'\b(solve a rubik\'s cube|how to solve rubik\'s cube)\b', user_input):
            print("Bot: Solving a Rubik's Cube involves several algorithms and strategies.")
        elif re.search(r'\b(best way to learn programming|how to learn programming)\b', user_input):
            print("Bot: Learning programming involves practice, reading documentation, and building projects.")
        elif re.search(r'\b(help with my math homework|math problem)\b', user_input):
            print("Bot: I'm sorry, I can't assist with specific homework problems.")
        elif re.search(r'\b(improve writing skills|how to write better)\b', user_input):
            print("Bot: Writing skills improve with practice, feedback, and reading widely.")
        elif re.search(r'\b(good book recommendation|recommend a book)\b', user_input):
            print("Bot: I don't have recommendations for specific books.")
        elif re.search(r'\b(news updates|current events)\b', user_input):
            print("Bot: I'm sorry, I don't have access to real-time news updates.")
        elif re.search(r'\b(favorite sport|sports)\b', user_input):
            print("Bot: I don't play sports, but I think soccer is quite popular.")
        elif re.search(r'\b(bye|see you later)\b', user_input):
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't have information on that topic.")

# Run the chatbot function
if _name_ == "_main_":
    simple_chatbot()
