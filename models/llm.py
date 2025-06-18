from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_output(prompt: str, max_tokens: int = 128) -> str:
    result = generator(prompt, max_new_tokens=max_tokens, do_sample=True)
    return result[0]["generated_text"]
