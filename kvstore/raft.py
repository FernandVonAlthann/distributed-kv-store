import random

class RaftNode:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.role = "follower"

    def start_election(self):
        self.current_term += 1
        self.voted_for = self.node_id
        self.role = "candidate"
        print(f"[Node {self.node_id}] Starting election for term {self.current_term}")
        # simplified: assume self-election
        self.role = "leader"
        return True

    def append_entries(self, entries):
        self.log.extend(entries)
        self.commit_index = len(self.log)
        return True
