from llama_index.core import PromptTemplate
from config import SYSTEM_PROMPT, QUERY_WRAPPER_PROMPT

class PromptTemplates:
    def __init__(self):
        self.system_prompt = SYSTEM_PROMPT
        self.query_wrapper_prompt = PromptTemplate(QUERY_WRAPPER_PROMPT)

    def get_system_prompt(self):
        """
        시스템 프롬프트를 반환합니다.
        시스템 프롬프트는 LLM이 기본적으로 사용하는 지시 사항이나 맥락을 포함합니다.
        """
        print("PromptTemplates.get_system_prompt()")
        return self.system_prompt
    
    def get_query_wrapper_prompt(self):
        """
        쿼리 래퍼 프롬프트를 반환합니다.
        사용자의 쿼리를 LLM에 전달할 때 사용할 포맷을 정의합니다.
        """
        print("PromptTemplates.get_query_wrapper_prompt()")
        return self.query_wrapper_prompt
