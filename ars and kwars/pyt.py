hard_skills = ['machine_learning','computer_vision','NLP','Data_Analysis'] #creating a list
print(hard_skills[0:2])#returning the first 2 elements

hard_skills.append('statistical_Analysis')#appending

print(hard_skills)

print(hard_skills[-1])#returning last element

hard_skills.insert(0,'Python')#inserting

print(hard_skills)

soft_skills =['resourceful','commitment','attention_to_detail','teamwork']

skills = hard_skills + soft_skills #concatenation

print(skills)

print(len(skills)) #the number of elements in skills variable

'deep_learning' in skills #look up function in

skills.insert(-1,'deep_learning')

print(skills)

my_address = '''1200 Nairobi Kenya '''

print("my_address is",my_address)

def sum_prod(num1,num2): #functions;positional arguments
    num_sum = num1 + num2
    num_prod = num1 * num2
    return num_sum,num_prod
x = int(input('Enter the first number :'))
y = int(input('Enter the second number :'))
print(sum_prod(x,y))
def sum_prod(num1,num2 =0): #default arguments
    num_sum = num1 + num2
    num_prod = num1 * num2
    return num_sum,num_prod
print(sum_prod(2,5))
print(sum_prod(2))
def sum_func(a, *args): #args
    s = a + sum(args)
    print(s)
sum_func(10)
sum_func(10,20)
sum_func(10,20,30)
sum_func(10, 20, 30, 40)
def shopping(**kwargs): #kwargs
    print(kwargs)
    if kwargs:
        print('you bought', kwargs['dress'])
        print('you bought', kwargs['food'])
        print('you bought', kwargs['Shampoo'])
shopping(dress = 'Frock',Shampoo ='Dove',food = 'Pedigree Puppy')

def adding_numbers(num1, num2, num3):
    print('Have to add three numbers')
    print('First Number = {}'.format(num1))
    print('Second Number = {}'.format(num2))
    print('Third Number = {}'.format(num3))
    return num1 + num2 + num3
x = adding_numbers(10, 20, 30)
print('The function returned a value of {}'.format(x))
yr_of_birth = int(input("Please enter your year of birth: "))
your_age = lambda yr_of_birth: 2023 - yr_of_birth #Lambda Function
print('Your age is', your_age(yr_of_birth))



class ClientCredential: #class function
    def __init__(self):
        self.first_name = input("Please enter your first name: ")
        self.second_name = input("Please enter your second name (optional): ")
        self.last_name = input("Please enter your last name: ")
        self.email = input("Please enter your email: ")
        self.username = input("Please enter your username: ")

    def print_credentials(self):
        print("First Name:", self.first_name)
        if self.second_name:
            print("Second Name:", self.second_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Username:", self.username)

client = ClientCredential()
client.print_credentials()






             

