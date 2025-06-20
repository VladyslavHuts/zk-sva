import subprocess
import json
import os

ZK_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(ZK_DIR, "build")

SNARKJS_PATH = "C:/Users/vladg/AppData/Roaming/npm/snarkjs.cmd"  # абсолютний шлях

def write_input_json(expected: int, actual: int):
    data = {
        "expected": str(expected),
        "actual": str(actual)
    }
    input_path = os.path.join(BUILD_DIR, "input.json")
    with open(input_path, "w") as f:
        json.dump(data, f)
    print(f"📝 input.json створено в {input_path}")


def generate_proof():
    os.chdir(BUILD_DIR)

    print("⚙️ Генерація witness...")
    subprocess.run([
        "node",
        "proof_js/generate_witness.js",
        "proof_js/proof.wasm",
        "input.json",
        "witness.wtns"
    ], check=True)

    print("🔐 Генерація proof...")
    subprocess.run([
        SNARKJS_PATH,
        "groth16",
        "prove",
        "proof_0000.zkey",
        "witness.wtns",
        "proof.json",
        "public.json"
    ], check=True)

    print("🔎 Перевірка proof...")
    result = subprocess.run([
        SNARKJS_PATH,
        "groth16",
        "verify",
        "verification_key.json",
        "public.json",
        "proof.json"
    ], capture_output=True, text=True)

    if "OK!" in result.stdout:
        print("✅ Proof підтверджено!")
        return True
    else:
        print("❌ Proof НЕ підтверджено!")
        print(result.stdout)
        return False
