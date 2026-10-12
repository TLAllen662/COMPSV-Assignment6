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