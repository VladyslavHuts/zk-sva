import subprocess
import json
import os
import shutil

ZK_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(ZK_DIR, "build")

# Платформонезалежний шлях до snarkjs
def get_snarkjs_cmd():
    if shutil.which("snarkjs"):
        return ["snarkjs"]
    elif shutil.which("npx"):
        return ["npx", "snarkjs"]
    else:
        raise FileNotFoundError("snarkjs not found. Make sure it's installed globally or accessible via npx.")

def write_input_json(expected: int, actual: int):
    data = {
        "expected": str(expected),
        "actual": str(actual)
    }
    input_path = os.path.join(BUILD_DIR, "input.json")
    with open(input_path, "w") as f:
        json.dump(data, f)
    print(f"📝 input.json created at {input_path}")

def generate_proof():
    os.chdir(BUILD_DIR)

    print("⚙️ Generating witness...")
    subprocess.run([
        "node",
        "proof_js/generate_witness.js",
        "proof_js/proof.wasm",
        "input.json",
        "witness.wtns"
    ], check=True)

    snarkjs = get_snarkjs_cmd()

    print("🔐 Generating proof...")
    subprocess.run(snarkjs + [
        "groth16",
        "prove",
        "proof_0000.zkey",
        "witness.wtns",
        "proof.json",
        "public.json"
    ], check=True)

    print("🔎 Verifying proof...")
    result = subprocess.run(snarkjs + [
        "groth16",
        "verify",
        "verification_key.json",
        "public.json",
        "proof.json"
    ], capture_output=True, text=True)

    if "OK!" in result.stdout:
        print("✅ Proof verified!")
        return True
    else:
        print("❌ Proof NOT verified!")
        print(result.stdout)
        return False
