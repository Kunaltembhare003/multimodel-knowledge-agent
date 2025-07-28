import pathlib

from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from fetch_abstract import fetch_abstract

load_dotenv()

# Initialize chat history as empty list
chat_history = []

# use  openAI model
model = ChatOpenAI(model="gpt-4", max_completion_tokens=256)
curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent

# load prompt template
template_path = home_dir.as_posix() + "/templates/summarization_templates.json"
template = load_prompt(template_path)

# load prompt input
paper_abstract = fetch_abstract(str(input("Please provide DOI:")))
style_input = input("Explanation style (e.g., Basic, Detailed): ").strip() or "Basic"
length_input = input("Explanation length (e.g., 100 words, short): ").strip() or "100 words"



    

formatted_prompt = template.format(paper_abstract= paper_abstract,
                                    style_input= style_input,
                                    length_input= length_input)
while True:
    # Add user message (the summarization request) to chat history
    chat_history.append(HumanMessage(content=formatted_prompt))

    # Get bot response using entire chat history (ordered list of messages)
    bot_response = model.invoke(chat_history)

    # Print and store assistant response
    print("Bot:", bot_response.content)
    chat_history.append(AIMessage(content=bot_response.content))

    # Optionally allow user to continue conversation or quit
    cont = input("Query:").strip().lower()
    if cont == "exit":
        break

print(chat_history)
   