import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from llama_index.llms.huggingface import HuggingFaceLLM
from config import BASE_MODEL

class LLMLoader:
    def __init__(self, system_prompt, query_wrapper_prompt):
        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
        self.stopping_ids = [self.tokenizer.eos_token_id, self.tokenizer.convert_tokens_to_ids("<|eot_id|>")]
        self.system_prompt = system_prompt
        self.query_wrapper_prompt = query_wrapper_prompt
        self.base_model = BASE_MODEL

    def load_llm(self):
        print("Loading LLM...")
        return HuggingFaceLLM(
            context_window=8192,
            max_new_tokens=256,
            generate_kwargs={"temperature": 0.7, "do_sample": False},
            system_prompt=self.system_prompt,
            query_wrapper_prompt=self.query_wrapper_prompt,
            tokenizer_name=self.base_model,
            model_name=self.base_model,
            device_map="auto",  # GPU 사용
            stopping_ids=self.stopping_ids,
            tokenizer_kwargs={"max_length": 4096},
            model_kwargs={"torch_dtype": torch.float16}  # GPU에서 float16 사용
        )
