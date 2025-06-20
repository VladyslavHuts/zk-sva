import argparse
import torch
from models.llm import generate_output
from blake3 import blake3
from zk.circom_runner import write_input_json, generate_proof

def main_function(prompt: str) -> dict:
    # 1. Set up device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 2. Generate LLM output
    output = generate_output(prompt)

    # 3. Calculate digest
    combined = prompt + output
    digest_bytes = blake3(combined.encode()).digest()[:4]
    digest_int = int.from_bytes(digest_bytes, byteorder="big")

    # 4. Write JSON and generate proof
    write_input_json(expected=digest_int, actual=digest_int)
    is_valid = generate_proof()

    # 5. Return structured result
    return {
        "device": str(device),
        "prompt": prompt,
        "output": output,
        "digest": digest_int,
        "is_valid": is_valid
    }

# CLI interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, default="What is privacy-preserving AI?")
    args = parser.parse_args()

    result = main_function(args.prompt)

    # Print formatted output
    print(f"\n🖥️  Using device: {result['device']}")
    print(f"🧠 Prompt: {result['prompt']}")
    print(f"💬 Output: {result['output']}")
    print(f"🔐 Digest (int): {result['digest']}")
    print("✅ Proof verified. Output is valid." if result["is_valid"] else "❌ Invalid proof. Output rejected.")
