class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first #Instance Variable #1
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@rtl.de"
        
        Employee.num_of_emps += 1 # Anzahl der Mitarbeiter, immer wenn eine Instance Variable geschaffen wird +1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
        
emp_1 = Employee("Niklas", "Büllesbach", "55000") # Eine Instance der Klasse
emp_2 = Employee("John", "Müller", "100000") # Zweite Instance der Klasse