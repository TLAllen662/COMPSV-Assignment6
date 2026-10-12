class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        is_top_call = current_node is None
        if current_node is None:
            current_node = self.root
            if current_node is None:
                print("❌ Error: The team tree is empty. Add a team lead first.")
                return False

        if current_node.name == manager_name:
            side = side.lower()
            if side not in ("left", "right"):
                print(f"❌ Error: '{side}' is not a valid side. Choose 'left' or 'right'.")
                return True

            if getattr(current_node, side) is not None:
                print(f"⚠️ Error: {manager_name} already has someone on the {side}.")
                return True

            setattr(current_node, side, EmployeeNode(employee_name))
            print(f"✅ {employee_name} added under {manager_name} on the {side}.")
            return True

        found = False
        if current_node.left is not None:
            found = self.insert(manager_name, employee_name, side, current_node.left)
        if not found and current_node.right is not None:
            found = self.insert(manager_name, employee_name, side, current_node.right)

        if is_top_call and not found:
            print(f"❌ Error: Manager '{manager_name}' not found in the team tree.")

        return found

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            return

        print("  " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

'''
Design Memo: Building the Team Management Tree

Recursive insertion in this project works by walking the tree one node at a
time, starting at the root. The `insert()` method checks whether the current
node's name matches the target manager. If it does, the new employee is
attached as a left or right child, provided that side is open. If it doesn't
match, the method calls itself on the current node's left child and then,
if the employee still hasn't been placed, on the right child. Each recursive
call narrows the search until the manager is found or the tree is exhausted,
at which point only the outermost call reports a "manager not found" error,
since the deeper calls can't tell whether a sibling branch already succeeded.

The trickiest part was making sure the search didn't print duplicate error
messages every time a recursive call didn't find the manager in its own
subtree, since a failed search in the left branch is not necessarily a
failure overall if the right branch succeeds. I solved this by having every
recursive call return a boolean indicating whether the manager was located
anywhere in its subtree, and only letting the top-level call decide whether
to print the final "not found" message. I also had to be careful to check
whether a side was already occupied before overwriting it, and to validate
that the side argument was actually "left" or "right" so bad input didn't
silently corrupt the tree.

Trees are preferable to flat lists or tables whenever data has a natural
hierarchy and you need fast, structured traversal, like org charts, file
systems, decision trees, or routing tables. Unlike a flat list, a tree lets
you model parent-child relationships directly, so operations like "find all
of this manager's reports" or "print the whole structure" are simple
recursive traversals instead of manual filtering. Balanced trees also offer
faster lookup than a list once the data set grows large, and the recursive
structure naturally mirrors how real organizations and file systems are
already structured, making the code easier to reason about and extend.
'''