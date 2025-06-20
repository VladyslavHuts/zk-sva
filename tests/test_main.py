from main import main_function

def test_main_function_output():
    result = main_function("What is Zero-Knowledge Proof?")
    assert isinstance(result, dict)
    assert "output" in result and isinstance(result["output"], str)
    assert result["is_valid"] is True
