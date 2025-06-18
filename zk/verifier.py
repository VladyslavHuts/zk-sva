def verify_mock_proof(proof_data, prompt, output):
    from blake3 import blake3
    expected = blake3((prompt + output).encode()).hexdigest()
    return expected == proof_data["proof"]
