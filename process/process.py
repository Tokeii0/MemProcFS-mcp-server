import memprocfs
from load import loadmem

def handle_get_process_attribute(mempath, process_name, attributes):
    '''
    Get the attribute of a specified process
    :param mempath: Memory image file location
    :param process_name: name of the process
    :param attributes: attributes of the process
    :return: attribute of the process
    process.pid         # int: process id. ex: process.pid -> 4280
    process.ppid        # int: parent process id. ex: process.ppid -> 4248
    process.eprocess    # int: _EPROCESS address. ex: process.eprocess -> 18446644053912244352
    process.dtb         # int: directory table base, dtb, cr3. ex: process.dtb -> 5930565632
    process.dtb_user    # int: user-mode directory table base, dtb, cr3. ex: process.dtb_user -> 5930561536
    process.state       # int: process state. ex: process.state -> 0
    process.peb         # int: process environment block, peb. ex: process.peb -> 14229504
    process.peb32       # int: 64-bit OS, 32-bit process environment block, peb. ex: process.peb32 -> 0
    process.is_wow64    # bool: 64-bit OS, 32-bit process. ex: process.is_wow64 -> False
    process.is_usermode # bool: is process user-mode. ex: process.is_usermode -> True
    process.name        # str: process short name (max 15 chars). ex: process.name -> 'explorer.exe'
    process.fullname    # str: process full name. ex: process.fullname -> 'explorer.exe'
    process.pathuser    # str: process path as seen by user-mode. ex: process.pathuser -> 'C:\\Windows\\Explorer.EXE'
    process.pathkernel  # str: process path as seen by kernel-mode. ex: process.pathkernel -> '\\Device\\HarddiskVolume4\\Windows\\explorer.exe'
    process.tp_memorymodel # int: memory model type. ex: process.tp_memorymodel -> 3
    process.tp_system   # int: system type. ex: process.tp_system -> 2
    process.luid        # int: process token LUID. ex: process.luid -> 225102
    process.session     # int: process token session id. ex: process.session -> 1
    process.sid         # str: process token SID. ex: process.sid -> 'S-1-5-21-3317879871-105768242-2947499445-1001'
    process.cmdline     # str: process command line. ex: process.cmdline -> 'cmd.exe /c calc.exe'
    process.integrity   # int: process integrity level as specified by VMMDLL_PROCESS_INTEGRITY_LEVEL. ex: process.integrity -> 3
    process.maps        # VmmProcessMaps: see methods below. ex: process.maps -> ProcessMaps:4280
    process.memory      # VmmVirtualMemory: see methods below. ex: process.memory -> VirtualMemory:4280
    '''
    vmm = loadmem(mempath)
    tagret_process = vmm.process(process_name)
    
    if not attributes.startswith("tagret_process.") and not attributes.startswith("process."):
        return eval(f"tagret_process.{attributes}")
    elif attributes.startswith("process."):
        return eval(f"tagret_process.{attributes[8:]}")
    else:
        return eval(attributes)
