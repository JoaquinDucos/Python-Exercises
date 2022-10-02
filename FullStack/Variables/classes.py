# concept of classes comes from object oritented programming which we will not touch in this course as it is
# an advanced topic
# we saw what functions did...
# they just take some data and return output,
# its a process oriented property
# with classes we can also keep data as well as process
# lets see a class
class Car:
    def __init__(self, name, gear, mileage):
        self.name = name
        self.gear = gear
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles

    def shift_gear(self, gear):
        self.gear = gear


car = Car("Toyota", 5, 0)
car.shift_gear(2)
car.drive(233)
print(car.mileage)
# deleting an object
del car
# inheritence , generalization
# we are not going to go too deep in this topic but just to explain
# An employee, can be a Manager or Assitant


class Employee:
    def __init__(self, name, age, dob, job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.job_description = job_description

    def get_salary(self):
        print("SALARY= $$$$")


class Manager(Employee):
    def __init__(self,  name, age, dob, job_description, department, employees):
        super().__init__(name, age, dob, job_description)
        self.department = department
        self.employees = employees

# super or parent class name can be used to initialize parent attributes


class Assistant(Employee):
    def __init__(self, name, age, dob, job_description, managers, working_hours):
        Employee.__init__(self, name, age, dob, job_description)
        self.managers = managers
        self.working_hours = working_hours


manager = Manager("kim", 27, "23-8-2000",
                  "manages every thing", "Engineering", 87)
manager.get_salary()