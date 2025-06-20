from blake3 import blake3

def test_digest_consistency():
    prompt = "ZK"
    output = "Proof"
    digest1 = blake3((prompt + output).encode()).hexdigest()
    digest2 = blake3((prompt + output).encode()).hexdigest()
    assert digest1 == digest2
