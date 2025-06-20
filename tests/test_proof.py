from zk.circom_runner import write_input_json, generate_proof

def test_proof_verification():
    digest = 123456789
    write_input_json(digest, digest)
    assert generate_proof() is True
