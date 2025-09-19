class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

   
    def append(self, coeff, power):
        new_node = Node(coeff, power)

       
        if self.head is None or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            while current and current.power > power:
                prev = current
                current = current.next

         
            if current and current.power == power:
                current.coeff += coeff
            else:
                new_node.next = current
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node

    def display(self):
        if not self.head:
            print("0")
            return
        current = self.head
        while current:
            sign = "+" if current.coeff > 0 and current != self.head else ""
            print(f"{sign}{current.coeff}x^{current.power}", end=" ")
            current = current.next
        print()

 
    def add(p1, p2):
        result = Polynomial()
        a = p1.head
        b = p2.head

        while a and b:
            if a.power == b.power:
                result.append(a.coeff + b.coeff, a.power)
                a = a.next
                b = b.next
            elif a.power > b.power:
                result.append(a.coeff, a.power)
                a = a.next
            else:
                result.append(b.coeff, b.power)
                b = b.next

        while a:
            result.append(a.coeff, a.power)
            a = a.next

        while b:
            result.append(b.coeff, b.power)
            b = b.next

        return result

def get_polynomial():
    poly = Polynomial()
    n = int(input("Enter the number of terms in the polynomial: "))
    print("Enter the terms in format: coefficient power")
    for _ in range(n):
        coeff, power = map(int, input("Term: ").split())
        poly.append(coeff, power)
    return poly


print("Enter the first polynomial:")
poly1 = get_polynomial()

print("\nEnter the second polynomial:")
poly2 = get_polynomial()

print("\nPolynomial 1:")
poly1.display()

print("Polynomial 2:")
poly2.display()

result = Polynomial.add(poly1, poly2)

print("Resultant Polynomial after Addition:")
result.display()

