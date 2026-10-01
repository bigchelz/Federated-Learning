# run_server.py
# run_server.py
# run_server.py
# run_server.py
# run_server.py

from authexample.server_app import app
from flwr.server.superlink.app import run_superlink
from flwr.server.authentication import AuthConfig

if __name__ == "__main__":
    run_superlink(
        app=app,
        grpc_max_message_length=100 * 1024 * 1024,
        ssl_certificates=(
            "certificates/ca.crt",
            "certificates/server.pem",
            "certificates/server.key",
        ),
        auth_config=AuthConfig(
            superlink_private_key="keys/server_credentials",
            superlink_public_key="keys/server_credentials.pub",
            list_public_keys="keys/client_public_keys.csv",
        ),
    )

