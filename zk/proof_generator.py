def generate_mock_proof(prompt, output):
    from blake3 import blake3
    digest = blake3((prompt + output).encode()).hexdigest()
    return {"proof": digest, "model": "gpt2"}
