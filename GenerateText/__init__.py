import logging, json
import azure.functions as func
from GenerateText.instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python GenerateText HTTP trigger function processed a request.')
    func.HttpResponse.mimetype = 'application/json'
    func.HttpResponse.charset = 'utf-8'

    torch.device("cuda" if torch.cuda.is_available() else "cpu")

    req_body = req.get_json()
    prompt = req_body.get('prompt')

    if prompt:

        tokenizer = AutoTokenizer.from_pretrained('/home/site/wwwroot/dolly/tokenizer', local_files_only=True, padding_side="left")
        model = AutoModelForCausalLM.from_pretrained('/home/site/wwwroot/dolly/model', local_files_only=True, device_map="auto")

        generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)

        response = generate_text(prompt)

        return func.HttpResponse(
            json.dumps({'response': response}),
             status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({'response': "Error: Missing prompt."}),
            status_code=400
        )
