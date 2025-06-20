import os
import json
from zk.circom_runner import write_input_json, BUILD_DIR

def test_input_json_creation():
    expected = 123
    actual = 123
    write_input_json(expected, actual)
    with open(os.path.join(BUILD_DIR, "input.json")) as f:
        data = json.load(f)
    assert data["expected"] == str(expected)
    assert data["actual"] == str(actual)
