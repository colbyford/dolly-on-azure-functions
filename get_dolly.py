from transformers import AutoModelForCausalLM, AutoTokenizer

## 3B Model (~5GB)
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b", device_map="auto")

## 7B Model (~14GB)
# tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-7b", padding_side="left")
# model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-7b", device_map="auto")

## 12B Model (~24GB)
# tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b", padding_side="left")
# model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b", device_map="auto")

## Save Tokenizer and Model
tokenizer.save_pretrained('/home/site/wwwroot/dolly/tokenizer')
model.save_pretrained('/home/site/wwwroot/dolly/model')

