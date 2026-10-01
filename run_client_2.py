# run_client_2.py
from authexample.client_app import client_fn
from flwr.simulation.ray_transport.supernode import run_supernode
from flwr.client import ClientApp
from flwr.client.authentication import AuthConfig

if __name__ == "__main__":
    app = ClientApp(client_fn=client_fn)

    run_supernode(
        app=app,
        grpc_max_message_length=100 * 1024 * 1024,  # Allow up to 100MB
        node_config={"dataset-path": "datasets/cifar10_part_2"},
        root_certificates="certificates/ca.crt",
        auth_config=AuthConfig(
            supernode_private_key="keys/client_credentials_2",
            supernode_public_key="keys/client_credentials_2.pub",
        ),
        clientappio_api_address="0.0.0.0:9095",
    )

