import openai
def explain_recommendation(user_behavior, product):
    prompt = f"Explain why product {product} is recommended to this user based on their behavior: {user_behavior}"
    response = openai.Completion.create(prompt=prompt, ...)
    return response.choices[0].text.strip()