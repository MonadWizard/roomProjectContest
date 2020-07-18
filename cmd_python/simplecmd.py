import subprocess
subprocess.call('charmap .',shell=True)
subprocess.call('start chrome.exe',shell=True)






# import os
# os.system("mkdir Quora")
# Executing a shell command
# os.system() 

# Get the users environment 
# os.environ() 

# #Returns the current working directory.
# os.getcwd() 

# Return the real group id of the current process.
# os.getgid() 

# Return the current process’s user id.
# os.getuid() 

# Returns the real process ID of the current process.
# os.getpid() 

# Set the current numeric umask and return the previous umask.
# os.umask(mask) 

# Return information identifying the current operating system.
# os.uname() 

# Change the root directory of the current process to path.
# os.chroot(path) 

# Return a list of the entries in the directory given by path.
# os.listdir(path) 

# Create a directory named path with numeric mode mode.
# os.mkdir(path) 

# Recursive directory creation function.
# os.makedirs(path) 

# Remove (delete) the file path.
# os.remove(path) 

# Remove directories recursively.
# os.removedirs(path) 

# Rename the file or directory src to dst.
# os.rename(src, dst) 

# Remove (delete) the directory path.
# os.rmdir(path)

"""
# File Explorer - explorer
# Calculator - calc
# Notepad - notepad
# Character Map - charmap
# Paint - mspaint
# Command Prompt (new window) - cmd
# Windows Media Player - wmplayer
# Task Manager - taskmgr
"""




# import ctypes, sys,subprocess

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if is_admin():
#     # Code of your program here
#     subprocess.call('dir',shell=True)
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)






# import os
# import sys
# import subprocess
# import win32com.shell.shell as shell

# ASADMIN = 'CARELESS'
# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

#     subprocess.call('openfiles',shell=True)
#     sys.exit(0)