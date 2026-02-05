from opcua import Client

client = Client("opc.tcp://localhost:4840")
client.connect()

print("Connected. Browsing nodes...\n")

objects = client.get_objects_node()
children = objects.get_children()

for child in children:
    print("Object:", child, child.get_browse_name())

    for sub in child.get_children():
        print("  Node:", sub, sub.get_browse_name(), "NodeId:", sub.nodeid)

client.disconnect()
print("\nDisconnected")
