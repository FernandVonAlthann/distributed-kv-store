import grpc
from concurrent import futures
import time
import sys
import random
from kvstore import kv, raft, rpc_pb2, rpc_pb2_grpc

class KVService(rpc_pb2_grpc.KeyValueServiceServicer):
    def __init__(self, node_id, peers):
        self.kvstore = kv.KeyValueStore()
        self.raftnode = raft.RaftNode(node_id, peers)

    def Put(self, request, context):
        print(f"Put: {request.key} -> {request.value}")
        self.kvstore.put(request.key, request.value)
        return rpc_pb2.KVResponse(status="OK", value="")

    def Get(self, request, context):
        val = self.kvstore.get(request.key)
        print(f"Get: {request.key} -> {val}")
        return rpc_pb2.KVResponse(status="OK", value=val)

    def Delete(self, request, context):
        result = self.kvstore.delete(request.key)
        return rpc_pb2.KVResponse(status=result, value="")

    def AppendEntries(self, request, context):
        print(f"AppendEntries from leader {request.leaderId}")
        entries = [(e.key, e.value) for e in request.entries]
        self.raftnode.append_entries(entries)
        return rpc_pb2.AppendEntriesResponse(term=self.raftnode.current_term, success=True)

    def RequestVote(self, request, context):
        granted = random.choice([True, False])
        return rpc_pb2.VoteResponse(term=self.raftnode.current_term, voteGranted=granted)

def serve(node_id, port, peers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc_pb2_grpc.add_KeyValueServiceServicer_to_server(KVService(node_id, peers), server)
    server.add_insecure_port(f"[::]:{port}")
    print(f"Node {node_id} running on port {port}")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python -m kvstore.node <node_id> <port>")
        sys.exit(1)

    node_id = int(sys.argv[1])
    port = int(sys.argv[2])
    peers = []  # Add peers as needed later

    serve(node_id, port, peers)
