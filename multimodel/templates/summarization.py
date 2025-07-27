from langchain_core.prompts import PromptTemplate

# template genrated
template = PromptTemplate(
    template="""
    Act as a Bioinformatics expert and summarize research paper  using given abstract {paper_abstract} by user and also help with dicussion.
    Once you provide the DOI, summarize the research paper  with the following specifications:
    Explanation Style: {style_input}  
    Explanation Length: {length_input}  

    1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.

    """,
    input_variables=["paper_abstract", "style_input", "length_input"],
    validate_template=True,
)

template.save("multimodel/templates/summarization_templates.json")
