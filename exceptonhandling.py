# try:
#     print(2/0)
# except ZeroDivisionError:
#     print('you cant divide anything to zero')

# try:
#     # Open a file in write-mode
#     f = open("myfile.txt", 'w')
#     f.write("Hello World!")
# except IOError as e:
#     print("An error occurred:", e)
# finally:
#     print("Closing the file now")
#     f.close()

# try:
#     print(2/3)
# except ZeroDivisionError as e:
#     print('error',e)

# else:
#     print('no exception occurs')
# finally:
#     print('hi from final')



# try:
#     result = 10 / 2  # No exception here
# except ZeroDivisionError as e:
#     print(f"Error: {e}")
# finally:
#     print("This will always be executed")


class Father:
    def __init__(self):
        print("Father's constructor")

class Mother:
    def __init__(self):
        print("Mother's constructor")

class Child(Mother, Father):
    def __init__(self):
        Father.__init__(self)  # Call Father's constructor
        super().__init__()  # Call Mother's constructor

# Create an instance of Child
child = Child()


