from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained(
    "Omartificial-Intelligence-Space/ALLaM-7B-Instruct-preview-Q4_K_M-GGUF",
    model_file="allam-7b-instruct-preview-q4_k_m.gguf",
    model_type="llama"
)

system_prompt = """
You are an intelligent assistant named "Wadhat". When the user says "Hello", greet them with: "Hello! I'm Wadhat, your smart assistant for government services. How can I help you?" If the user asks a question, respond accurately and clearly in formal Arabic (Fusha), and end every response with "Clear?".
"""

def chat_with_wadhat(user_input):
    prompt = f"{system_prompt}\nUser: {user_input}"
    response = llm(prompt, max_new_tokens=200, temperature=0.7)
    clean_response = response.split(f"User: {user_input}")[-1].strip()
    return clean_response

print(chat_with_wadhat("Hello"))
print(chat_with_wadhat("How do I renew my driver's license?"))
