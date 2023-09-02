def my_name():
    print("my name is hanan ")

def my_meal(food , drink):
    print(f"i like to eat {food} and while drinking{drink}")

my_meal('chiken',"pepsi")

def cube(number):
    return number**3
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else :
      return False
    
my_name()

print(cube(9))
print(by_three(9))