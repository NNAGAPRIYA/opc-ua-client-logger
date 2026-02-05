from opcua import ua, Server
from datetime import datetime
import time

# Server Creation
server = Server()

# Setting the endpoint
server.set_endpoint("opc.tcp://localhost:4840")

# Setting the server name
server.set_server_name("Python OPC UA Demo Server")

# To get objects node
objects = server.get_objects_node()

# Creation of a custom namespace
uri = "http://example.opcua.demo"
idx = server.register_namespace(uri)

# Creation of an object
demo_object = objects.add_object(idx, "DemoObject")

# Creation of 10 dummy variables
tags = []
for i in range(1, 11):
    tag = demo_object.add_variable(idx, f"Tag{i}", i * 10)
    tag.set_writable()
    tags.append(tag)

# Starting of server
server.start()
print("OPC UA Demo Server started at opc.tcp://localhost:4840")

try:
    while True:
        # Updation of tag values every second
        for i, tag in enumerate(tags):
            tag.set_value(i * 10 + time.time() % 10)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping server...")

finally:
    server.stop()
