# Create individual nodes
node1 = {
    "name": "Alice",
    "adm": "ADM001",
    "grades": [78, 85, 92],
    "next": None
}

node2 = {
    "name": "Brian",
    "adm": "ADM002",
    "grades": [66, 74, 80],
    "next": None
}

node3 = {
    "name": "Cynthia",
    "adm": "ADM003",
    "grades": [90, 88, 95],
    "next": None
}

# Linking the nodes to form a linked list
node1["next"] = node2
node2["next"] = node3

# The head of the linked list
head = node1


# Function to traverse the linked list
def traverse(head):
    current = head
    while current is not None:
        print("Name:", current["name"])
        print("Admission No:", current["adm"])
        print("Grades:", current["grades"])
        print("------------------------")
        current = current["next"]


# Test traverse
traverse(head)