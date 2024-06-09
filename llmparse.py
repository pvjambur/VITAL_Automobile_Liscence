from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex , SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from code_reader1 import code_reader
from pydantic import BaseModel
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import Settings
import ast
import csv
import json

llm = Ollama(model = "llama3" , request_timeout = 30.0)
class CodeOutput(BaseModel):
    CarNumber : str
    CarColor : str
    CarType : str
parser = PydanticOutputParser(CodeOutput)
code_parser_template = """Parse this response from the user into carNumber ,CarColor , CarType in oneword here is the response {response} also remove the double quotes and dont give any other text  also map the colors to the closest color from [
    'beige', 
    'black', 
    'blue', 
    'brown', 
    'gold', 
    'green', 
    'grey', 
    'orange', 
    'pink', 
    'purple', 
    'red', 
    'silver', 
    'tan', 
    'white', 
    'yellow'
] dont say any details about the color parsing be silent also parse the CarType to the closest in the list [
    'Hatchback',
    'SUV',
    'Sedan',
    'Pickup',
    'Others'
] also be silent about the mapping"""
json_prompt_str = parser.format(code_parser_template)
json_prompt_tmpl = PromptTemplate(json_prompt_str)
output_pipeline = QueryPipeline(chain=[json_prompt_tmpl, llm])
def retry(response):
    ans = output_pipeline.run(response = response)
    print(ans)
    cleaned_json = ast.literal_eval(str(ans).replace("assistant: Here is the parsed response in JSON format:", ""))
    car_data_str = cleaned_json
    car_data = car_data_str
    csv_file = 'car_data.csv'
    
    with open(csv_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(car_data.values())
    print(f"Data successfully written to {csv_file} without headers")

while( prompt := input("Enter a prompt (q to quit) :")) != "q":
    number_retry =0
    while(number_retry<4):
        try:
            retry(prompt)
            break
        except Exception as e:
            print("Failed")





