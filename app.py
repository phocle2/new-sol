import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.get("/")
def root():
    return jsonify({"ok": True, "service": "solana-reward-api"})

@app.get("/health")
def health():
    return jsonify({"ok": True})

@app.post("/reward/send")
def reward_send():
    data = request.get_json(silent=True) or {}
    receiver = data.get("receiver_wallet_address")

    if not receiver:
        return jsonify({"ok": False, "error": "missing receiver_wallet_address"}), 400

    return jsonify({
        "ok": True,
        "receiver_wallet_address": receiver,
        "note": "Reward endpoint reached (Solana logic next)"
    })
