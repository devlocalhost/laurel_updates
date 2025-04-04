import os
import hmac
import hashlib
import subprocess

from flask import request


def verify_signature(secret_token, signature_header, payload_body):
    if not signature_header:
        return False

    expected = (
        "sha256="
        + hmac.new(secret_token.encode(), payload_body, hashlib.sha256).hexdigest()
    )

    return hmac.compare_digest(expected, signature_header)


def deploy(secret_token):
    signature = request.headers.get("X-Hub-Signature-256")
    payload = request.get_data()

    if verify_signature(secret_token, signature, payload):
        subprocess.run([os.path.abspath("auto-deploy.sh")])

        return "", 200

    else:
        return "", 403
