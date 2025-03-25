import memprocfs
# mempath = "D:\test.raw"
# 获取指定进程PID
def loadmem(mempath):
    vmm = memprocfs.Vmm(['-device', mempath])
    return vmm
