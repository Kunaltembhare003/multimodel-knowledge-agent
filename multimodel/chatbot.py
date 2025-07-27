import pathlib

from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

from fetch_abstract import fetch_abstract

load_dotenv()

# load prompt input
paper_abstract = fetch_abstract(str(input("Please provide DOI:")))
style_input = "Basic"
length_input = int(100)

# use  openAI model
model = ChatOpenAI(model="gpt-4", max_completion_tokens=50)

curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent

# load prompt template
template_path = home_dir.as_posix() + "/templates/summarization_templates.json"
template = load_prompt(template_path)

# Create chain to use templat and use modle to genrate summary
chain = template | model
result = chain.invoke(
    {"paper_abstract": paper_abstract, "style_input": style_input, "length_input": length_input}
)

print(result.content)
