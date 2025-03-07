import os
import platform
import socket
print("Current machinw type")
print(platform.machine())
print("====================================")

print("Current processor")
print(platform.architecture())
print("====================================")

print("Set socket timeout to 50 seconds and then retrieve it")
print(socket.setdefaulttimeout(50))
print(socket.getdefaulttimeout())
print("====================================")

print("Get the current operating system type")
print(os.name)
print("Get the current operating system name")
print(platform.system())
print("====================================")

print("Get the current process id")
print(os.getpid())