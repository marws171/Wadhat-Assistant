def chat_with_wadhat(llm, user_input, system_prompt):
    prompt = f"{system_prompt}\nUser: {user_input}"
    response = llm(prompt, max_new_tokens=200, temperature=0.7)
    clean_response = response.split(f"User: {user_input}")[-1].strip()
    return clean_response
