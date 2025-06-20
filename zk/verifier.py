import subprocess
import os

ZK_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(ZK_DIR, "build")

def verify_proof():
    os.chdir(BUILD_DIR)

    result = subprocess.run(
        ["snarkjs", "groth16", "verify", "verification_key.json", "public.json", "proof.json"],
        capture_output=True,
        text=True
    )

    if "OK!" in result.stdout:
        print("✅ ZK Proof: OK")
        return True
    else:
        print("❌ ZK Proof: INVALID")
        print(result.stdout)
        return False
