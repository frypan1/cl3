import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy('http://localhost:8000')
    n = int(input("Enter the number to calculate factorial: "))
    result = server.calculate_factorial(n)
    print(f"The factorial of {n} is: {result}")

if __name__ == "__main__":
    main()



# import Pyro4

# uri = input("Enter uri: ")
# concatenate = Pyro4.Proxy(uri)
# str1 = input("1: ")
# str2 = input("2: ")
# print(concatenate.concatenate(str1,str2))
