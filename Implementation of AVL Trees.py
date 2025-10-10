class Node:
    def __init__(self, enrollment_id, student_name):
        self.enrollment_id = enrollment_id
        self.student_name = student_name
        self.left = None
        self.right = None
        self.height = 1 

class AVLTree:

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x  

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  

    def insert(self, root, enrollment_id, student_name):
        if not root:
            return Node(enrollment_id, student_name)
        elif enrollment_id < root.enrollment_id:
            root.left = self.insert(root.left, enrollment_id, student_name)
        elif enrollment_id > root.enrollment_id:
            root.right = self.insert(root.right, enrollment_id, student_name)
        else:
            return root  

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and enrollment_id < root.left.enrollment_id:
            return self.right_rotate(root)

        if balance < -1 and enrollment_id > root.right.enrollment_id:
            return self.left_rotate(root)

        if balance > 1 and enrollment_id > root.left.enrollment_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and enrollment_id < root.right.enrollment_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, enrollment_id):
        if not root:
            return root
        elif enrollment_id < root.enrollment_id:
            root.left = self.delete(root.left, enrollment_id)
        elif enrollment_id > root.enrollment_id:
            root.right = self.delete(root.right, enrollment_id)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.enrollment_id = temp.enrollment_id
            root.student_name = temp.student_name
            root.right = self.delete(root.right, temp.enrollment_id)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def search(self, root, enrollment_id):
        if not root:
            return None
        if enrollment_id == root.enrollment_id:
            return root
        elif enrollment_id < root.enrollment_id:
            return self.search(root.left, enrollment_id)
        else:
            return self.search(root.right, enrollment_id)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(f"Enrollment ID: {root.enrollment_id}, Name: {root.student_name}")
        self.inorder(root.right)

    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)


avl = AVLTree()
root = None

while True:
    print("\n--- STUDENT ENROLLMENT SYSTEM USING AVL TREE ---")
    print("1. Insert Enrollment Record")
    print("2. Delete Record by Enrollment ID")
    print("3. Search Student Enrollment")
    print("4. Display All Enrollments (Inorder)")
    print("5. Count Total Enrollments")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        eid = int(input("Enter Enrollment ID: "))
        name = input("Enter Student Name: ")
        root = avl.insert(root, eid, name)
        print("Record inserted successfully!")

    elif ch == 2:
        eid = int(input("Enter Enrollment ID to delete: "))
        root = avl.delete(root, eid)
        print("Record deleted successfully!")

    elif ch == 3:
        eid = int(input("Enter Enrollment ID to search: "))
        res = avl.search(root, eid)
        if res:
            print(f"Record Found → ID: {res.enrollment_id}, Name: {res.student_name}")
        else:
            print("Record Not Found!")

    elif ch == 4:
        print("\nAll Enrollments (Inorder):")
        avl.inorder(root)

    elif ch == 5:
        print("Total Enrollments:", avl.count(root))

    elif ch == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
