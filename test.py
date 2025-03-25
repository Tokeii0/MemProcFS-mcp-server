from process.process import *
from registry.registry import *

if __name__ == "__main__":
    mempath = "D:/test.raw"
    processname = "notepad.exe"
    #print(handle_get_reghive_attribute(mempath, "\\SystemRoot\\System32\\Config\\SAM", "rootkey"))
    print(handle_get_regkey_attribute(mempath, "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", "values"))
    print(handle_get_regvalue_attribute(mempath, "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\VMware User Process", "value"))