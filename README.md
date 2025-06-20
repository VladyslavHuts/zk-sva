# Zero-Knowledge Self-Verification Architecture (ZK-SVA)

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![ZK-SNARK](https://img.shields.io/badge/ZKProof-Groth16-informational?logo=lock&color=blue)
![Python Tests](https://github.com/VladyslavHuts/zk-sva/actions/workflows/python-tests.yml/badge.svg?cacheBust=1)





A **proof-of-concept system** that enables Large Language Models (LLMs) to **self-verify their outputs** using real zero-knowledge proofs (ZKPs) and cryptographic hashing.  
Built for **verifiable**, **privacy-preserving**, and **decentralized AI**.

---

## ⚙️ How It Works

1. Accept a user prompt  
2. Generate an output using GPT-2 (or any LLM)  
3. Compute a BLAKE3 hash of `prompt + output`  
4. Create a zk-SNARK proof of correct hashing using Circom + snarkjs  
5. Verify the proof — and only then accept the output

---

## 🔐 Why It Matters

> In an era of AI hallucinations and unverifiable claims, **ZK-SVA** introduces a cryptographic mechanism to **verify model outputs without revealing internal logic**.

This enables:
- Verifiable AI results  
- Tamper-resistant response chains  
- Trust without transparency compromises

---

## ✅ Real ZK-SNARK Integration

This version integrates real cryptographic zero-knowledge proofs using:

- [`circom`](https://docs.circom.io/) — circuit design  
- [`snarkjs`](https://github.com/iden3/snarkjs) — proof generation and verification  
- [`blake3`](https://github.com/BLAKE3-team/BLAKE3) — hashing mechanism  

---

## 🔄 ZK Proof Workflow

```bash
# 1. Compile the circuit (one-time)
circom proof.circom --r1cs --wasm --sym -o zk/build

# 2. Generate the witness
node proof_js/generate_witness.js proof_js/proof.wasm input.json witness.wtns

# 3. Generate the zk-SNARK proof
snarkjs groth16 prove proof_0000.zkey witness.wtns proof.json public.json

# 4. Verify the proof
snarkjs groth16 verify verification_key.json public.json proof.json

```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/zk_sva_project.git
cd zk_sva_project
```

### Create virtual environment and install Python dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### Install Circom and snarkjs

```bash
# Install Rust & Circom
cargo install --locked --git https://github.com/iden3/circom

# Install snarkjs via npm
npm install -g snarkjs
```

### Run the Project

```bash
python main.py --prompt "What is ZK and why does it matter?"
```

### Example Output

```bash
Prompt: What is ZK and why does it matter?
Output: ZK allows you to prove a statement is true without revealing why it's true...
Digest (mod 2^251): 12345678901234567890
Proof verified. Output is cryptographically valid.
```

## Project Structure

```bash
zk-sva/
├── main.py               # Entry point
├── models/               # GPT-2 inference logic
│   └── llm.py
├── zk/                   # ZK proof generation logic
│   ├── build/            # Input/output/proof artifacts
│   ├── proof.circom      # ZK circuit
│   └── circom_runner.py
├── requirements.txt      # Python deps
├── .gitignore
└── README.md

```
## License
This project is licensed under the MIT License.
See LICENSE for details.
MIT License: https://opensource.org/licenses/MIT





