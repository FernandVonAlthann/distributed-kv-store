import grpc
import click
from kvstore import rpc_pb2, rpc_pb2_grpc

@click.command()
@click.argument("cmd")
@click.argument("key")
@click.argument("value", required=False)
@click.option("--port", default=5000)
def cli(cmd, key, value, port):
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = rpc_pb2_grpc.KeyValueServiceStub(channel)

    if cmd.upper() == "PUT":
        response = stub.Put(rpc_pb2.KVRequest(key=key, value=value))
    elif cmd.upper() == "GET":
        response = stub.Get(rpc_pb2.KVRequest(key=key))
    elif cmd.upper() == "DELETE":
        response = stub.Delete(rpc_pb2.KVRequest(key=key))
    else:
        print("Invalid command")
        return

    print(f"Status: {response.status}, Value: {response.value}")

if __name__ == "__main__":
    cli()
