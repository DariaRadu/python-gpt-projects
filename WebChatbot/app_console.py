from openai import OpenAI
import os
from dotenv import load_dotenv

# pass the api key
client = OpenAI(
    api_key = os.getenv('OPEN_AI_API_KEY')
)

messages = []

messages.append({
    'role': 'system',
    'content':  '''You are an interviewer at a tech company.
            You want to know if the user has good technical knowledge in game programming at a senior level.
            Present the user with questions.
            Give 4 different answers to each question (a, b, c, d).
            Reply to the user whether their answer is correct or not, and continue with a new question.'''
})

while True:
    # send the api call
    response = client.chat.completions.create(
        messages=messages, 
        model="gpt-4o-mini"
    )

    # print the reply
    print(response.choices[0].message.content)

    # expand the conversation
    messages.append(response.choices[0].message)

    # capture user input
    user_input = input('Enter your answer: ')
    if user_input == 'q':
        exit()

    # prompt preparation
    messages.append({'role' : 'user', 'content': user_input })