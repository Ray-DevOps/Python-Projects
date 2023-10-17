Illustration #1
------------------------

class User:
  def __init__(self, user_id, username):
    self.user_id = user_id
    self.username = username
    self.followers = 0             # We set default values for followers and following to zero
    self.following = 0             # When setting default values, we don't need to include them inside the init function

  def follow(self, user):
      user.followers += 1
      self.following += 1     

user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)  ---> 0
print(user_1.following)  ---> 1
print(user_2.followers)  ---> 1
print(user_2.following)  ---> 0


Illustration #2
------------------------

class Employee:                                                 # We create a class called "Employee"
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@companyltd.com"

    def full_name(self):                                        # Within that class we create a method called full_name
        return f"{self.first_name} {self.last_name}"            # to return the employee's full name


employee1 = Employee("Jenny", "Corey", 50000)

print(employee1.full_name())         ------->   Jenny Corey     # Notice that when printing methods we include the empty parenthesis
