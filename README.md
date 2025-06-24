# Distributed Key-Value Store

This is a simplified Raft-based distributed key-value store using gRPC.

## Features
- GET/PUT/DELETE operations
- Raft-style leader simulation
- Multi-node replication
- CLI client

## Run

0. Create and activate the virtual environment (if not already)
```bash
python3 -m venv venv
source venv/bin/activate
```
1. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Compile gRPC:
```bash
python -m grpc_tools.protoc \
  -I kvstore \
  --python_out=. \
  --grpc_python_out=. \
  kvstore/rpc.proto
```

4. Start nodes:
```bash
python -m kvstore.node 1 5000
```
On two other terminal windows:
```bash
source venv/bin/activate
python -m kvstore.node 2 5001
```
```bash
source venv/bin/activate
python -m kvstore.node 3 5002
```
5. Use CLI:
```bash
python -m cli.client PUT name fernando --port 5000
python -m cli.client GET name --port 5000
```
6.
```bash
deactivate
```
