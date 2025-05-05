from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(factorial, 'calculate_factorial')
print("Server is ready to accept RPC calls...")
server.serve_forever()


# import Pyro4

# @Pyro4.expose
# class StringConcatenator:
#     def concatenate(self,str1,str2):
#         return str1 + str2
    
# daemon = Pyro4.Daemon()
# uri = daemon.register(StringConcatenator)
# print(uri)
# daemon.requestLoop()