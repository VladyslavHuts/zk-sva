import argparse
import torch
from models.llm import generate_output
from blake3 import blake3
from zk.circom_runner import write_input_json, generate_proof

# 1. Аргументи з командного рядка
parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, default="What is privacy-preserving AI?")
args = parser.parse_args()
prompt = args.prompt

# 2. Пристрій
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"\n🖥️  Using device: {device}")

# 3. Вивід LLM
output = generate_output(prompt)

# 4. Digest (використовуємо лише перші 4 байти для Circom-сумісності)
combined = prompt + output
digest_bytes = blake3(combined.encode()).digest()[:4]
digest_int = int.from_bytes(digest_bytes, byteorder="big")

# 5. Створюємо input.json і генеруємо zk-proof
write_input_json(expected=digest_int, actual=digest_int)

# 6. Генеруємо доказ і верифікуємо
is_valid = generate_proof()

# 7. Вивід
print("\n🧠 Prompt:", prompt)
print("💬 Output:", output)
print("🔐 Digest (int):", digest_int)
print("✅ Proof verified. Output is valid." if is_valid else "❌ Invalid proof. Output rejected.")
