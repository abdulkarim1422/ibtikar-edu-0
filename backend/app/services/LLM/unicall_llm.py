from app.services.LLM import gpt_service
from backend.app.services.LLM import gemini_service

def unicall(llm_type="gemini", system_prompt="", user_prompt=""):
    if llm_type == "gpt":
        return gpt_service.call_gpt_basic(system_prompt, user_prompt)
    elif llm_type == "gemini":
        user_prompt = f"{system_prompt} \n {user_prompt}"
        return gemini_service.call_gemini_basic(user_prompt)
    else:
        return "LLM type not found"