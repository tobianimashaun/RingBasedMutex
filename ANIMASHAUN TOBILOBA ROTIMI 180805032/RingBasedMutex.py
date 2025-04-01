import threading
import time
import random

class RingNode:
    def __init__(self, node_id, next_node=None):
        self.node_id = node_id  # Unique identifier for the node
        self.next_node = next_node  # Reference to the next node in the ring
        self.has_token = False  # Token availability flag
        self.lock = threading.Lock()  # Synchronization lock

    def receive_token(self):
        """Method to receive and process the token"""
        self.has_token = True
        print(f"Node {self.node_id} received the token.")
        self.enter_critical_section()

    def enter_critical_section(self):
        """Simulates entering the critical section"""
        with self.lock:
            print(f"Node {self.node_id} is in the critical section.")
            time.sleep(random.uniform(1, 3))  # Simulate processing time
            print(f"Node {self.node_id} is exiting the critical section.")
            self.pass_token()

    def pass_token(self):
        """Passes the token to the next node in the ring"""
        self.has_token = False
        print(f"Node {self.node_id} passing the token to Node {self.next_node.node_id}.")
        time.sleep(1)  # Simulate token transmission delay
        self.next_node.receive_token()

# Create ring topology with 4 nodes
node1 = RingNode(1)
node2 = RingNode(2)
node3 = RingNode(3)
node4 = RingNode(4)

# Form the ring
node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node1  # Last node links back to the first node

# Initialize the ring with the token at node 1
node1.has_token = True
print("Starting Ring-Based Mutual Exclusion")

# Start execution by passing the token
node1.receive_token()
