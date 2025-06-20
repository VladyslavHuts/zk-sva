import subprocess
import json
import os

ZK_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(ZK_DIR, "build")

def write_input_json(expected: int, actual: int):
    data = {
        "expected": str(expected),
        "actual": str(actual)
    }
    with open(os.path.join(BUILD_DIR, "input.json"), "w") as f:
        json.dump(data, f)
    print("📝 input.json створено")

def generate_proof():
    os.chdir(BUILD_DIR)

    print("⚙️  Генерація witness...")
    subprocess.run(["node", "proof_js/generate_witness.js", "proof_js/proof.wasm", "input.json", "witness.wtns"], check=True)

    print("⚙️  Генерація proof...")
    subprocess.run(["snarkjs", "groth16", "prove", "proof_0000.zkey", "witness.wtns", "proof.json", "public.json"], check=True)

    print("⚙️  Верифікація proof...")
    result = subprocess.run(["snarkjs", "groth16", "verify", "verification_key.json", "public.json", "proof.json"], capture_output=True, text=True)

    if "OK!" in result.stdout:
        print("✅ Proof успішно верифіковано")
        return True
    else:
        print("❌ Помилка при перевірці")
        print(result.stdout)
        return False
