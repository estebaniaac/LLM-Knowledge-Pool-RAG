# This script runs locally (w/LM Studio server) and an embedding model loaded.
import json
import os
from config import *

document_to_embed = "knowledge_pool/MasterThesisSummary_Stella_Gonzlez_ColivingExperiences.txt"

def get_embedding(text, model=embedding_model):
   text = text.replace("\n", " ")
   return local_client.embeddings.create(input = [text], model=model).data[0].embedding

# Read the text document
with open(document_to_embed, 'r', encoding='utf-8', errors='ignore') as infile:
    text_file = infile.read()

# Split the text into lines (each line = 1 vector). Pick this or the following chunking strategy.
chunks = text_file.split("\n")
chunks = [line for line in chunks if line.strip() and line.strip() != '---']

# Alternetively, split the text into paragraphs by using the empty lines in between them
# Figure out your own strategy according to the structure of the txt you have.
# chunks = text_file.split("\n\n")
        
# Create the embeddings
embeddings = []
for i, line in enumerate(chunks):
    print(f'{i} / {len(chunks)}')
    vector = get_embedding(line.encode(encoding='utf-8').decode())
    database = {'content': line, 'vector': vector}
    embeddings.append(database)

# Save the embeddings to a json file
output_filename = os.path.splitext(document_to_embed)[0]
output_path = f"{output_filename}.json"

with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(embeddings, outfile, indent=2, ensure_ascii=False)

print(f"Finished vectorizing. Created {document_to_embed}")
