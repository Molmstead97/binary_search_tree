class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearch:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self.insert_recursive(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert_recursive(node.right, value)
            else:
                node.right = Node(value)

    def search(self, value):
        return self.search_recursive(self.root, value) if self.root else False

    def search_recursive(self, node, value):
        if not node:
            return False
        elif node.value == value:
            return True
        return self.search_recursive(node.left if value < node.value else node.right, value)

    def traverse_in_order(self, node):
        if node:
            yield from self.traverse_in_order(node.left)
            yield node.value
            yield from self.traverse_in_order(node.right)

    def in_order_traversal(self):
        return list(self.traverse_in_order(self.root))
    
    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.value if current else None
    
    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.value if current else None

    def traverse_height(self, node):
        if not node:
            return -1
        return 1 + max(self.traverse_height(node.left), self.traverse_height(node.right))

    def height(self):
        return self.traverse_height(self.root)

    def traverse_count_leaves(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.traverse_count_leaves(node.left) + self.traverse_count_leaves(node.right)

    def count_leaves(self):
        return self.traverse_count_leaves(self.root)

    def serialize_recursive(self, node):
        if not node:
            return '#'
        return str(node.value) + ',' + self.serialize_recursive(node.left) + ',' + self.serialize_recursive(node.right)

    def serialize(self):
        return self.serialize_recursive(self.root)

    def deserialize_recursive(self, nodes):
        if not nodes:
            return None
        value = nodes.pop(0)
        if value == '#':
            return None
        node = Node(int(value))
        node.left = self.deserialize_recursive(nodes)
        node.right = self.deserialize_recursive(nodes)
        return node

    def deserialize(self, tree):
        nodes = tree.split(',')
        self.root = self.deserialize_recursive(nodes)

bst = BinarySearch()
bst.insert(10)
bst.insert(12)
bst.insert(8)
bst.insert(22)
bst.insert(4)

print(bst.search(6))  
print(bst.search(9))  

print(bst.in_order_traversal())  
print(bst.find_min()) 
print(bst.find_max())  
print(bst.height()) 
print(bst.count_leaves()) 

serialized_tree = bst.serialize()
print(serialized_tree) 

new_bst = BinarySearch()
new_bst.deserialize(serialized_tree)
print(new_bst.in_order_traversal())


        
        
        
        
        