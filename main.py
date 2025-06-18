import torch
from models.llm import generate_output
from blake3 import blake3
from zk.proof_generator import generate_mock_proof
from zk.verifier import verify_mock_proof

# 1. Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"✅ Using device: {device}")

# 2. Prompt
prompt = "What is privacy-preserving AI?"
output = generate_output(prompt)

# 3. Digest + ZKP
digest = blake3((prompt + output).encode()).hexdigest()
proof = generate_mock_proof(prompt, output)
is_valid = verify_mock_proof(proof, prompt, output)

# 4. Display
print("\nPrompt:", prompt)
print("\nOutput:", output)
print("\nDigest:", digest)

if is_valid:
    print("✔️ Proof verified. Output is valid.")
else:
    print("❌ Invalid proof. Output rejected.")
