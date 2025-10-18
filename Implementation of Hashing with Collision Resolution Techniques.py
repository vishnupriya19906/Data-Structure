class Student:
 def __init__(self, roll_no, name):
 self.roll_no = roll_no
 self.name = name
 def __str__(self):
 return f"({self.roll_no}, {self.name})"

class HashTableLinear:
 def __init__(self, size):
 self.size = size
 self.table = [None] * size
 def hash_function(self, key):
 return key % self.size
 def insert(self, roll_no, name):
 index = self.hash_function(roll_no)
 start_index = index
 while self.table[index] is not None and self.table[index].roll_no != roll_no:
 index = (index + 1) % self.size
 if index == start_index:
 print("Hash Table is full!")
 return
 self.table[index] = Student(roll_no, name)
 print(f"Student {name} inserted at index {index}.")
 def search(self, roll_no):
 index = self.hash_function(roll_no)
 start_index = index
 while self.table[index] is not None:
 if self.table[index].roll_no == roll_no:
 print(f"Record Found: {self.table[index]}")
 return
 index = (index + 1) % self.size
 if index == start_index:
 break
 print("Record not found.")
 def delete(self, roll_no):
 index = self.hash_function(roll_no)
 start_index = index
 while self.table[index] is not None:
 if self.table[index].roll_no == roll_no:
 print(f"Record deleted: {self.table[index]}")
 self.table[index] = None
 return
 index = (index + 1) % self.size
 if index == start_index:
 break
 print("Record not found.")
 def display(self):
 print("\nHash Table (Linear Probing):")
 for i, student in enumerate(self.table):
 if student is not None:
 print(f"Index {i}: {student}")
 else:
 print(f"Index {i}: Empty")

class HashTableChaining:
 def __init__(self, size):
 self.size = size
 self.table = [[] for _ in range(size)]
 def hash_function(self, key):
 return key % self.size
 def insert(self, roll_no, name):
 index = self.hash_function(roll_no)
 for student in self.table[index]:
 if student.roll_no == roll_no:
 print("Duplicate roll number.")
 return
 self.table[index].append(Student(roll_no, name))
 print(f"Student {name} inserted at index {index}.")
 def search(self, roll_no):
 index = self.hash_function(roll_no)
 for student in self.table[index]:
 if student.roll_no == roll_no:
 print(f"Record Found: {student}")
 return
 print("Record not found.")
 def delete(self, roll_no):
 index = self.hash_function(roll_no)
 for student in self.table[index]:
 if student.roll_no == roll_no:
 self.table[index].remove(student)
 print(f"Record deleted: {student}")
 return
 print("Record not found.")
 def display(self):
 print("\nHash Table (Chaining):")
 for i, chain in enumerate(self.table):
 if chain:
 print(f"Index {i}: {' -> '.join(str(s) for s in chain)}")
 else:
 print(f"Index {i}: Empty")

def main():
 size = int(input("Enter the size of hash table: "))
 print("Choose collision resolution technique:")
 print("1. Linear Probing")
 print("2. Chaining")
 choice = int(input("Enter choice: "))
 if choice == 1:
 ht = HashTableLinear(size)
 else:
 ht = HashTableChaining(size)
 while True:
 print("\n--- Student Registration System ---")
 print("1. Insert Student")
 print("2. Search Student")
 print("3. Delete Student")
 print("4. Display Hash Table")
 print("5. Exit")
 op = int(input("Enter your choice: "))
 if op == 1:
 roll_no = int(input("Enter Roll Number: "))
 name = input("Enter Name: ")
 ht.insert(roll_no, name)
 elif op == 2:
 roll_no = int(input("Enter Roll Number to Search: "))
 ht.search(roll_no)
 elif op == 3:
 roll_no = int(input("Enter Roll Number to Delete: "))
 ht.delete(roll_no)
 elif op == 4:
 ht.display()
 elif op == 5:
 print("Exiting program...")
 break
 else:
 print("Invalid choice.")
if __name__ == "__main__":
 main()
