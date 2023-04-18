from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b", padding_side="left")
tokenizer.save_pretrained('/home/site/wwwroot/dolly/tokenizer')

# model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b", device_map="auto")
# model.save_pretrained('/home/site/wwwroot/dolly/model')