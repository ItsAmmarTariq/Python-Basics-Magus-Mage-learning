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

"""
NESTED TRY CATCH
"""
try:
    1/0
    try:
        # Inner try block
        x = int(input("Enter a number: "))
        result = 10 / 0
        print("Result:", result)
    
    except ValueError:
        print("Inner: Please enter a valid number.")
    
    except ZeroDivisionError:
        print("Inner: Cannot divide by zero.")
    
    else:
        print("Inner: No exceptions in the inner try block.")
    
    finally:
        print("Inner: This is always executed in the inner try block.")

except Exception as e:
    print("Outer: An error occurred in the outer try block:", e)

else:
    print("Outer: No exceptions in the outer try block.")

finally:
    print("Outer: This is always executed in the outer try block.")


# try:
#     result = 10 / 2  # No exception here
# except ZeroDivisionError as e:
#     print(f"Error: {e}")
# finally:
#     print("This will always be executed")


# class Father:
#     def __init__(self):
#         print("Father's constructor")

# class Mother:
#     def __init__(self):
#         print("Mother's constructor")

# class Child(Mother, Father):
#     def __init__(self):
#         Father.__init__(self)  # Call Father's constructor
#         super().__init__()  # Call Mother's constructor

# # Create an instance of Child
# child = Child()


