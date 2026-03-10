#2303A51543

#Task-1(Stack Implementation)
#Prompt:Generate a Stack class with push, pop, peek, and is_empty methods.
#Sample Input Code:
#class Stack:
 #pass
#Expected Output:A functional stack implementation with all required methods and docstrings.

class Stack:
    """A stack data structure implementation using a list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """Push an item onto the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
print(stack.pop())   # Output: 2
print(stack.is_empty())  # Output: False
print(stack.pop())   # Output: 1
print(stack.is_empty())  # Output: True


#Task-2(Queue Implementation)
#Prompt:Implement a Queue using Python lists.
#Sample Input Code:
#class Queue:
#pass
#Expected Output:FIFO-based queue class with enqueue, dequeue, peek, and size methods.
class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.queue = []

    def enqueue(self, item):
        # Add an item to the end of the queue (FIFO)
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item at the front of the queue (FIFO)
        if not self.is_empty():
            return self.queue.pop(0)  # Removes the first element
        else:
            return "Queue is empty"

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        # Return the number of elements in the queue
        return len(self.queue)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Peek:", q.peek())  # Peek at the front item
print("Size:", q.size())  # Get the size of the queue
print("Dequeue:", q.dequeue())  # Remove and return the front item
print("Size after dequeue:", q.size())  # Size after dequeue

#Task-3(Linked List)
#Prompt:Generate a Singly Linked List with insert and display methods.
#Sample Input Code:
#class Node:
#pass
#class LinkedList:
#pass
#Expected Output:A working linked list implementation with clear method documentation.
class Node:
    """A node in a singly linked list."""
    
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None
class LinkedList:
    """A singly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def insert(self, data):
        """Insert a new node with the given data at the end of the list.
        
        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        """Display the contents of the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()  # for a new line after displaying the list
# Example usage:
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.display()  # Output: 1 2 3

#Task Description #4 – Hash Table
#Prompt:Implement a hash table with basic insert, search, and delete methods.
#Sample Input Code:
#class HashTable:
#pass
#Expected Output:Collision handling using chaining, with well-commented methods.
class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a specified size and create empty buckets
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        # Generate a hash value for the given key
        return hash(key) % self.size
    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash(key)
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        self.table[index].append((key, value))  # Add new key-value pair
    def search(self, key):
        # Search for a value by its key in the hash table
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if key is found
        return None  # Return None if key is not found
    def delete(self, key):
        # Delete a key-value pair from the hash table
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True  # Return True if deletion is successful
        return False  # Return False if key is not found
# Example usage:
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print(hash_table.search("name"))  # Output: Alice
print(hash_table.search("age"))   # Output: 30
hash_table.delete("name")
print(hash_table.search("name"))  # Output: None

#Task-5(Graph Representation)
#Prompt:Implement a graph using an adjacency list.
#Sample Input Code:
#class Graph:
#pass
#Expected Output:Graph with methods to add vertices, add edges, and display connections.
class Graph:
    """A graph data structure implemented using an adjacency list."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph.
        
        Args:
            vertex: The vertex to be added.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices in the graph.
        
        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def display(self):
        """Display the adjacency list of the graph."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(edges)}")
# Example usage:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.display()

#Task-6: Smart Hospital Management System – Data Structure Selection
#Prompt:A hospital wants to develop a Smart Hospital Management System that handles:
#Patient Check-In System – Patients are registered and treated in order of arrival.
#Emergency Case Handling – Critical patients must be treated first.
#Medical Records Storage – Fast retrieval of patient details using ID.
#Doctor Appointment Scheduling – Appointments sorted by time.
#Hospital Room Navigation – Represent connections between wards and rooms.

print("\n" + "="*80)
print("TASK-6: SMART HOSPITAL MANAGEMENT SYSTEM - DATA STRUCTURE SELECTION")
print("="*80)

# ============================================================================
# TABLE 1: FEATURE → DATA STRUCTURE → JUSTIFICATION
# ============================================================================

print("\n" + "-"*80)
print("TABLE 1: Data Structure Selection for Hospital Features")
print("-"*80)

table_data = [
    ("Patient Check-In System", "Queue", "FIFO principle ensures patients are treated in order of arrival, maintaining fairness and preventing queue jumping."),
    ("Emergency Case Handling", "Priority Queue", "Allows critical patients to move to the front based on severity level, ensuring urgent cases are prioritized over routine ones."),
    ("Medical Records Storage", "Hash Table", "Provides O(1) average-case retrieval using patient ID as key, enabling instant access to records without sequential searching."),
    ("Doctor Appointment Scheduling", "Binary Search Tree (BST)", "Maintains appointments sorted by time automatically; enables efficient insertion, deletion, and time-range queries."),
    ("Hospital Room Navigation", "Graph", "Represents connections between wards and rooms as nodes and edges; enables pathfinding and connection queries between departments.")
]

print(f"\n{'Feature':<35} | {'Data Structure':<20} | {'Justification':<80}")
print("-" * 145)
for feature, structure, justification in table_data:
    print(f"{feature:<35} | {structure:<20} | {justification:<80}")

# ============================================================================
# TABLE 2: FUNCTIONAL IMPLEMENTATIONS
# ============================================================================

print("\n" + "-"*80)
print("TABLE 2: Implementation - Emergency Case Handling (Priority Queue)")
print("-"*80)

import heapq
from datetime import datetime

class EmergencyCaseManager:
    """
    Manages emergency cases using a priority queue.
    Patients with higher severity are treated first.
    """
    
    def __init__(self):
        """Initialize an empty priority queue for emergency cases."""
        self.emergency_queue = []
        self.patient_counter = 0
    
    def add_patient(self, patient_name, severity):
        """
        Add a patient to the emergency queue.
        
        Args:
            patient_name: Name of the patient.
            severity: Severity level (1=critical, 2=urgent, 3=moderate).
        """
        # Lower priority value = higher priority (treated first)
        self.patient_counter += 1
        heapq.heappush(self.emergency_queue, (severity, self.patient_counter, patient_name))
        print(f"✓ Added: {patient_name} (Severity: {severity}) - ID: {self.patient_counter}")
    
    def treat_next_patient(self):
        """
        Remove and treat the next patient (highest priority).
        
        Returns:
            The patient being treated or a message if queue is empty.
        """
        if self.emergency_queue:
            severity, patient_id, patient_name = heapq.heappop(self.emergency_queue)
            severity_label = {1: "CRITICAL", 2: "URGENT", 3: "MODERATE"}
            print(f"→ Now treating: {patient_name} (Priority: {severity_label[severity]})")
            return patient_name
        else:
            print("→ No patients in queue")
            return None
    
    def peek_next_patient(self):
        """
        View the next patient without removing them.
        
        Returns:
            The next patient to be treated or a message if queue is empty.
        """
        if self.emergency_queue:
            severity, patient_id, patient_name = self.emergency_queue[0]
            severity_label = {1: "CRITICAL", 2: "URGENT", 3: "MODERATE"}
            print(f"→ Next patient: {patient_name} (Priority: {severity_label[severity]})")
            return patient_name
        else:
            print("→ Queue is empty")
            return None
    
    def queue_size(self):
        """
        Get the number of patients waiting.
        
        Returns:
            The size of the emergency queue.
        """
        return len(self.emergency_queue)
    
    def display_queue(self):
        """Display all patients in the emergency queue."""
        if self.emergency_queue:
            print("\nCurrent Emergency Queue:")
            severity_map = {1: "CRITICAL", 2: "URGENT", 3: "MODERATE"}
            sorted_queue = sorted(self.emergency_queue)
            for severity, patient_id, patient_name in sorted_queue:
                print(f"  - {patient_name} (ID: {patient_id}, Priority: {severity_map[severity]})")
        else:
            print("Queue is empty")

# Example usage:
print("\n" + "-"*80)
print("DEMONSTRATION: Emergency Case Management System")
print("-"*80)

emergency_manager = EmergencyCaseManager()

# Add patients with different severity levels
emergency_manager.add_patient("John Doe", 3)      # Moderate
emergency_manager.add_patient("Jane Smith", 1)    # Critical
emergency_manager.add_patient("Mike Johnson", 2)  # Urgent
emergency_manager.add_patient("Sarah Williams", 1) # Critical
emergency_manager.add_patient("Tom Brown", 2)     # Urgent

# Display the queue
emergency_manager.display_queue()

# Treat patients
print("\n--- Treating Patients (by priority) ---")
while emergency_manager.queue_size() > 0:
    emergency_manager.treat_next_patient()

print("\n" + "="*80)

#Task-7: Smart City Traffic Control System
#Prompt:A city plans a Smart Traffic Management System that includes:
#Traffic Signal Queue – Vehicles waiting at signals.
#Emergency Vehicle Priority Handling – Ambulances and fire trucks prioritized.
#Vehicle Registration Lookup – Instant access to vehicle details.
#Road Network Mapping – Roads and intersections connected logically.
#Parking Slot Availability – Track available and occupied slots.
#Student Task
#For each feature, select the most appropriate data structure fromthe list below:
#Stack,Queue,Priority Queue,Linked List,Binary Search Tree (BST),Graph,Hash Table,Deque
#Justify your choice in 2–3 sentences per feature.
#Implement one selected feature as a working Python program with code generation.
#Expected Output:1.A table mapping feature → chosen data structure → justification.
#2.A functional Python program implementing the chosen feature with comments and docstrings.

class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        This queue will be used to manage vehicles waiting at the traffic signal.
        """
        self.queue = []

    def enqueue(self, vehicle):
        """
        Add a vehicle to the queue.
        
        :param vehicle: The vehicle to be added to the queue.
        """
        self.queue.append(vehicle)
        print(f"Vehicle {vehicle} added to the queue.")

    def dequeue(self):
        """
        Remove and return the first vehicle from the queue (the vehicle that has waited the longest).
        
        :return: The first vehicle in the queue or a message if the queue is empty.
        """
        if self.is_empty():
            return "No vehicles waiting at the signal."
        return self.queue.pop(0)

    def peek(self):
        """
        Return the first vehicle in the queue without removing it.
        
        :return: The first vehicle in the queue or a message if the queue is empty.
        """
        if self.is_empty():
            return "No vehicles waiting at the signal."
        return self.queue[0]

    def size(self):
        """
        Return the current number of vehicles in the queue.
        
        :return: The size of the queue.
        """
        return len(self.queue)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0


# Table mapping feature to chosen data structure with justification
feature_table = [
    ("Traffic Signal Queue", "Queue", "A queue follows the FIFO principle, ideal for vehicles waiting at signals, where the first vehicle should be processed first."),
    ("Emergency Vehicle Priority", "Priority Queue", "Emergency vehicles must be prioritized over regular vehicles, and a priority queue allows for fast access to high-priority elements."),
    ("Vehicle Registration Lookup", "Hash Table", "A hash table provides constant-time lookup of vehicle details using a unique identifier as the key, enabling quick and efficient access to vehicle information."),
    ("Road Network Mapping", "Graph", "A graph is ideal for modeling road networks where intersections are vertices, and roads are edges, enabling efficient pathfinding and analysis."),
    ("Parking Slot Availability", "Linked List", "A linked list allows for easy tracking and updating of parking slots, with nodes representing each slot and its status (available or occupied).")
]

# Display the feature table
print("Feature → Chosen Data Structure → Justification")
for feature in feature_table:
    print(f"{feature[0]} → {feature[1]} → {feature[2]}")

# Example usage of the Traffic Signal Queue
if __name__ == "__main__":
    signal_queue = Queue()
    
    # Enqueue vehicles
    signal_queue.enqueue("Car1")
    signal_queue.enqueue("Car2")
    signal_queue.enqueue("Car3")

    # Display the size of the queue
    print(f"Number of vehicles waiting: {signal_queue.size()}")

    # Peek at the vehicle that will leave the queue first
    print(f"Next vehicle to pass: {signal_queue.peek()}")

    # Dequeue a vehicle (signal turns green for the vehicle)
    print(f"Vehicle passed the signal: {signal_queue.dequeue()}")
    
    # Display the remaining queue
    print(f"Remaining vehicles in the queue: {signal_queue.queue}")

#Task-8: Smart E-Commerce Platform – Data Structure Challenge
#Prompt:An e-commerce company wants to build a Smart Online Shopping System with:
#Shopping Cart Management – Add and remove products dynamically.
#Order Processing System – Orders processed in the order they areplaced.
#Top-Selling Products Tracker – Products ranked by sales count.
#Product Search Engine – Fast lookup of products using product ID.
#Delivery Route Planning – Connect warehouses and delivery locations.
#Student Task
#For each feature, select the most appropriate data structure from the list below:
#Stack,Queue,Priority Queue, Linked List,Binary Search Tree (BST),Graph,Hash Table,Deque
#Justify your choice in 2–3 sentences per feature.
#Implement one selected feature as a working Python program with code generation.
#Expected Output:1.A table mapping feature → chosen data structure → justification.
#2.A functional Python program implementing the chosen feature with comments and docstrings.

# Data structure selection and justification
feature_table = [
    ("Shopping Cart Management", "Deque", "A deque allows efficient adding/removing of products from both ends of the shopping cart, making it dynamic and quick for user interaction."),
    ("Order Processing System", "Queue", "A queue follows the FIFO principle, making it ideal for processing orders in the order they are placed."),
    ("Top-Selling Products Tracker", "Priority Queue", "A priority queue allows us to easily track products ranked by sales count, giving priority to those with the highest sales."),
    ("Product Search Engine", "Hash Table", "A hash table offers fast and efficient lookups of products using their product ID, making it optimal for a search engine."),
    ("Delivery Route Planning", "Graph", "A graph is ideal for representing and planning delivery routes between warehouses and destinations using vertices and edges.")
]

# Display the feature table
print("Feature → Chosen Data Structure → Justification")
for feature in feature_table:
    print(f"{feature[0]} → {feature[1]} → {feature[2]}")

# Order Processing System - Queue implementation
class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        This queue will manage orders in the order they are placed (FIFO).
        """
        self.queue = []

    def enqueue(self, order_id):
        """
        Add an order to the queue.
        
        :param order_id: The order ID to be added to the queue.
        """
        self.queue.append(order_id)
        print(f"Order {order_id} added to the queue.")

    def dequeue(self):
        """
        Remove and return the first order from the queue (the order that was placed first).
        
        :return: The first order ID in the queue or a message if the queue is empty.
        """
        if self.is_empty():
            return "No orders to process."
        return self.queue.pop(0)

    def peek(self):
        """
        Return the first order in the queue without removing it.
        
        :return: The first order in the queue or a message if the queue is empty.
        """
        if self.is_empty():
            return "No orders to process."
        return self.queue[0]

    def size(self):
        """
        Return the current number of orders in the queue.
        
        :return: The size of the queue.
        """
        return len(self.queue)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0


# Example usage of the Order Processing System (Queue)
if __name__ == "__main__":
    order_queue = Queue()

    # Enqueue orders
    order_queue.enqueue("Order_001")
    order_queue.enqueue("Order_002")
    order_queue.enqueue("Order_003")

    # Display the size of the queue
    print(f"Number of orders in queue: {order_queue.size()}")

    # Peek at the next order to be processed
    print(f"Next order to process: {order_queue.peek()}")

    # Dequeue an order (process the order)
    print(f"Processing order: {order_queue.dequeue()}")

    # Display remaining orders in the queue
    print(f"Remaining orders in the queue: {order_queue.queue}")
