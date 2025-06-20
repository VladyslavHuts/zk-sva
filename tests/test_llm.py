from models.llm import generate_output

def test_llm_response():
    prompt = "What is ZK?"
    output = generate_output(prompt)
    assert isinstance(output, str)
    assert len(output.strip()) > 0
