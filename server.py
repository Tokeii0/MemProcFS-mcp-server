from mcp.server.fastmcp import FastMCP
from typing import Optional
from process.process import *
from registry.registry import *
from load import loadmem


mcp = FastMCP("MemProcFS-mcp-server")

@mcp.tool()
def get_process_attribute(mempath, process_name, attributes):
    '''
    Get the attribute of a specified process
    :param mempath: Memory image file location
    :param process_name: name of the process
    :param attributes: attributes of the process
    :return: attribute of the process
    Examples of valid attributes:
    pid         # int: process id. ex: pid -> 4280
    ppid        # int: parent process id. ex: ppid -> 4248
    eprocess    # int: _EPROCESS address. ex: eprocess -> 18446644053912244352
    dtb         # int: directory table base, dtb, cr3. ex: dtb -> 5930565632
    dtb_user    # int: user-mode directory table base, dtb, cr3. ex: dtb_user -> 5930561536
    state       # int: process state. ex: state -> 0
    peb         # int: process environment block, peb. ex: peb -> 14229504
    peb32       # int: 64-bit OS, 32-bit process environment block, peb. ex: peb32 -> 0
    is_wow64    # bool: 64-bit OS, 32-bit  ex: is_wow64 -> False
    is_usermode # bool: is process user-mode. ex: is_usermode -> True
    name        # str: process short name (max 15 chars). ex: name -> 'explorer.exe'
    fullname    # str: process full name. ex: fullname -> 'explorer.exe'
    pathuser    # str: process path as seen by user-mode. ex: pathuser -> 'C:\\Windows\\Explorer.EXE'
    pathkernel  # str: process path as seen by kernel-mode. ex: pathkernel -> '\\Device\\HarddiskVolume4\\Windows\\explorer.exe'
    tp_memorymodel # int: memory model type. ex: tp_memorymodel -> 3
    tp_system   # int: system type. ex: tp_system -> 2
    luid        # int: process token LUID. ex: luid -> 225102
    session     # int: process token session id. ex: session -> 1
    sid         # str: process token SID. ex: sid -> 'S-1-5-21-3317879871-105768242-2947499445-1001'
    cmdline     # str: process command line. ex: cmdline -> 'cmd.exe /c calc.exe'
    integrity   # int: process integrity level as specified by VMMDLL_PROCESS_INTEGRITY_LEVEL. ex: integrity -> 3
    maps        # VmmProcessMaps: see methods below. ex: maps -> ProcessMaps:4280
    memory      # VmmVirtualMemory: see methods below. ex: memory -> VirtualMemory:4280
    '''
    return handle_get_process_attribute(mempath, process_name, attributes)

@mcp.tool()
def get_reghive_attribute(mempath, hive_identifier, attributes):
    '''
    Get the attribute of a specified registry hive
    :param mempath: Memory image file location
    :param hive_identifier: name or index of the registry hive
    :param attributes: attributes of the registry hive
    :return: attribute of the registry hive
    Examples of valid attributes:
    name           # str: hive name. ex: name -> '0xffffbc079b45f000-SAM-MACHINE_SAM'
    name_short     # str: short hive name. ex: name_short -> '\\SystemRoot\\System32\\Config\\SAM'
    path           # str: hive kernel object path. ex: path -> '\\REGISTRY\\MACHINE\\SAM'
    size           # int: hive size of on-disk hive. ex: size -> 12288
    addr           # int: address of CMHIVE object. ex: addr -> 18446669339588685824
    addr_baseblock # int: address of HIVE BASE BLOCK (.regf). ex: addr_baseblock -> 18446669339638857728
    rootkey        # VmmRegKey: root key of the hive. ex: rootkey -> RegKey:ROOT
    orphankey      # VmmRegKey: orphan 'virtual' root key of the hive. ex: orphankey -> RegKey:ORPHAN
    memory         # VmmRegMemory: registry memory functions. Please see methods below for more info.
    '''
    return handle_get_reghive_attribute(mempath, hive_identifier, attributes)

@mcp.tool()
def get_regkey_attribute(mempath, key_path, attributes):
    '''
    Get the attribute of a specified registry key
    :param mempath: Memory image file location
    :param key_path: path of the registry key
    :param attributes: attributes of the registry key
    :return: attribute of the registry key
    Examples of valid attributes:
    name     # str: key name. ex: name -> 'Run'
    path     # str: key path. ex: path -> 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'
    parent   # VmmRegKey: parent registry key. ex: parent -> RegKey:CurrentVersion
    time_int # int: key last write time. ex: time_int -> 131983260431204405
    time_str # str: key last write time. ex: time_str -> '2019-03-29 09:40:43 UTC'
    values   # list: values of the registry key. ex: values -> [RegValue:SecurityHealth]
    values_dict # dict: values of the registry key. ex: values_dict -> {'SecurityHealth': RegValue:SecurityHealth}
    '''
    return handle_get_regkey_attribute(mempath, key_path, attributes)

@mcp.tool()
def get_regvalue_attribute(mempath, value_path, attributes):
    '''
    Get the attribute of a specified registry value
    :param mempath: Memory image file location
    :param value_path: full path of the registry value
    :param attributes: attributes of the registry value
    :return: attribute of the registry value
    Examples of valid attributes:
    name     # str: value name. ex: name -> 'SecurityHealth'
    path     # str: value path. ex: path -> 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\SecurityHealth'
    parent   # VmmRegKey: parent registry key. ex: parent -> RegKey:Run
    size     # int: value byte size. ex: size -> 90
    type     # int: value type as memprocfs.WINREG_*. ex: type -> 2
    value    # bytes: the raw registry value as a bytes object. ex: value -> b'%\x00P\x00r\x00o\x00g\x00r\x00a\x00m\x00F ...'
    '''
    return handle_get_regvalue_attribute(mempath, value_path, attributes)

@mcp.tool()
def get_reghive_list(mempath):
    '''
    Get the list of registry hives
    :param mempath: Memory image file location
    :return: list of registry hives
    '''
    return handle_get_reghive_list(mempath)

if __name__ == "__main__":
    mcp.run()
