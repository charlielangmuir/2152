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
print("====================================")

file_name = "fdpractice.txt"
print(f"\n[Before fork] Process {os.getpid()}")
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT) # Open the file in read/write mode, or create if it doenst exist
print(f"[Process {os.getpid()} Opened file_handle: {file_handle}]")

file_object_TextIO = os.fdopen(file_handle, "w+") # Open the file handle in write mode

file_object_TextIO.write("Hello World\n")
file_object_TextIO.flush()