import memprocfs
from load import loadmem

def handle_get_reghive_attribute(mempath, hive_identifier, attributes):
    '''
    Get the attribute of a specified registry hive
    :param mempath: Memory image file location
    :param hive_identifier: name or index of the registry hive
    :param attributes: attributes of the registry hive
    :return: attribute of the registry hive
    reghive.name           # str: hive name. ex: reghive.name -> '0xffffbc079e436000-settingsdat-A_{c4fac4f4-b28f-17e2-b8a7-4d3640adf5aa}'
    reghive.name_short     # str: short hive name. ex: reghive.name_short -> '1h2txyewy\\Settings\\settings.dat'
    reghive.path           # str: hive kernel object path. ex: reghive.path -> '\\REGISTRY\\A\\{c4fac4f4-b28f-17e2-b8a7-4d3640adf5aa}'
    reghive.size           # int: hive size of on-disk hive. ex: reghive.size -> 12288
    reghive.addr           # int: address of CMHIVE object. ex: reghive.addr -> 18446669339638849536
    reghive.addr_baseblock # int: address of HIVE BASE BLOCK (.regf). ex: reghive.addr_baseblock -> 18446669339638857728
    reghive.rootkey        # VmmRegKey: root key of the hive. ex: reghive.rootkey -> RegKey:ROOT
    reghive.orphankey      # VmmRegKey: orphan 'virtual' root key of the hive. ex: reghive.orphankey -> RegKey:ORPHAN
    reghive.memory         # VmmRegMemory: registry memory functions. Please see methods below for more info.
    '''
    vmm = loadmem(mempath)
    
    # 如果 hive_identifier 是整数或可以转换为整数，则按索引获取
    try:
        reghive_list = vmm.reg_hive_list()
        len_reghive_list = len(reghive_list)
        target_reghive = reghive_list[len_reghive_list-1]
    except Exception as e:
        return f"Error: {str(e)}"
    
    # 处理属性
    try:
        if not attributes.startswith("target_reghive.") and not attributes.startswith("reghive."):
            return eval(f"target_reghive.{attributes}")
        elif attributes.startswith("reghive."):
            return eval(f"target_reghive.{attributes[8:]}")
        else:
            return eval(attributes)
    except Exception as e:
        return f"Error accessing attribute '{attributes}': {str(e)}"

def handle_get_regkey_attribute(mempath, key_path, attributes):
    '''
    Get the attribute of a specified registry key
    :param mempath: Memory image file location
    :param key_path: path of the registry key
    :param attributes: attributes of the registry key
    :return: attribute of the registry key
    regkey.name     # str: key name. ex: regkey.name -> 'Run'
    regkey.path     # str: key path. ex: regkey.path -> 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'
    regkey.parent   # VmmRegKey: parent registry key. ex: regkey.parent -> RegKey:CurrentVersion
    regkey.time_int # int: key last write time. ex: regkey.time_int -> 131983260431204405
    regkey.time_str # str: key last write time. ex: regkey.time_str -> '2019-03-29 09:40:43 UTC'
    '''
    vmm = loadmem(mempath)
    
    try:
        target_regkey = vmm.reg_key(key_path)
    except Exception as e:
        return f"Error: {str(e)}"
    
    # 处理属性
    try:
        if not attributes.startswith("target_regkey.") and not attributes.startswith("regkey."):
            # 处理特殊情况：values() 和 values_dict() 是方法调用
            if attributes == "values" or attributes == "values_dict":
                return eval(f"target_regkey.{attributes}()")
            return eval(f"target_regkey.{attributes}")
        elif attributes.startswith("regkey."):
            attr = attributes[7:]
            # 处理特殊情况：values() 和 values_dict() 是方法调用
            if attr == "values" or attr == "values_dict":
                return eval(f"target_regkey.{attr}()")
            return eval(f"target_regkey.{attr}")
        else:
            return eval(attributes)
    except Exception as e:
        return f"Error accessing attribute '{attributes}': {str(e)}"

def handle_get_regvalue_attribute(mempath, value_path, attributes):
    '''
    Get the attribute of a specified registry value
    :param mempath: Memory image file location
    :param value_path: full path of the registry value
    :param attributes: attributes of the registry value
    :return: attribute of the registry value
    regvalue.name   # str: value name. ex: regvalue.name -> 'SecurityHealth'
    regvalue.path   # str: value path. ex: regvalue.path -> 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\SecurityHealth'
    regvalue.parent # VmmRegKey: parent registry key. ex: regvalue.parent -> RegKey:Run
    regvalue.size   # int: value byte size. ex: regvalue.size -> 90
    regvalue.type   # int: value type as memprocfs.WINREG_*. ex: regvalue.type -> 2
    regvalue.value  # bytes: the raw registry value as a bytes object. ex: regvalue.value -> b'%\x00P\x00r\x00o\x00g\x00r\x00a\x00m\x00F ...'
    '''
    vmm = loadmem(mempath)
    
    try:
        target_regvalue = vmm.reg_value(value_path)
    except Exception as e:
        return f"Error: {str(e)}"
    
    # 处理属性
    try:
        if not attributes.startswith("target_regvalue.") and not attributes.startswith("regvalue."):
            return eval(f"target_regvalue.{attributes}")
        elif attributes.startswith("regvalue."):
            return eval(f"target_regvalue.{attributes[9:]}")
        else:
            return eval(attributes)
    except Exception as e:
        return f"Error accessing attribute '{attributes}': {str(e)}"

def handle_get_reghive_list(mempath):
    '''
    Get the list of registry hives
    :param mempath: Memory image file location
    :return: list of registry hives
    '''
    vmm = loadmem(mempath)
    return vmm.reg_hive_list()