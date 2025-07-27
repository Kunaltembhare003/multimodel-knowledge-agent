from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# embed query
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

"""
result = embedding.embed_query("90 days notice period is pain")

print(result)
"""


# similarity search
document = [
    "Protein LLMs are essentially deep learning models, often based on transformer architectures, that are trained on massive datasets of protein sequences (like those found in databases like UniProt)",
    "They learn the statistical relationships between amino acids and how they fold into 3D structures, enabling them to predict properties of unseen proteins.",
    "The 'language' aspect comes from the fact that proteins are essentially sequences of amino acids, similar to how text is a sequence of words. ",
]
query = "tell me about proteim llm"

doc_embedding = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(score)), key=lambda x: x[1])[-1]

print(query)
print(document[index])
print("similarity score is:", score)
