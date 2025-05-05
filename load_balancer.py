import random

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers

    def round_robin(self):
        server_index = 0
        while True:
            yield self.servers[server_index]
            server_index = (server_index + 1) % len(self.servers)

    def random_selection(self):
        while True:
            yield random.choice(self.servers)

    def least_connection(self):
        while True:
            min_connections = min(self.servers, key=lambda x: x.connections)
            min_connections.connections += 1
            yield min_connections

class Server:
    def __init__(self, name):
        self.name = name
        self.connections = 0

def simulate_requests(load_balancer, num_requests):
    print("Simulating {} requests...\n".format(num_requests))
    for i in range(num_requests):
        server = next(load_balancer)
        print("Request {} handled by Server {}".format(i + 1, server.name))
    print("\nSimulation complete.")

if __name__ == "__main__":
    server1 = Server("Server1")
    server2 = Server("Server2")
    server3 = Server("Server3")
    servers = [server1, server2, server3]

    lb = LoadBalancer(servers)

    # Choose the load balancing algorithm:
    # load_balancer = lb.round_robin()
    load_balancer = lb.random_selection()
    # load_balancer = lb.least_connection()

    simulate_requests(load_balancer, 10)
