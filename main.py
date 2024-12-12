import os
import platform
import psutil
import socket

def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Release": platform.release(),
        "Architecture": platform.architecture()[0],
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "Total RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
    }
    if platform.system() == "Windows":
        try:
            import wmi
            c = wmi.WMI()
            gpu_info = [gpu.Name for gpu in c.Win32_VideoController()]
            info["GPU"] = ", ".join(gpu_info)
        except ImportError:
            info["GPU"] = "WMI module not installed. Install it with `pip install wmi`."
        except Exception as e:
            info["GPU"] = f"Unable to detect GPU: {e}"
    else:
        try:
            import subprocess
            gpu_info = subprocess.check_output("lspci | grep VGA", shell=True).decode('utf-8').strip()
            info["GPU"] = gpu_info
        except Exception as e:
            info["GPU"] = f"Unable to detect GPU: {e}"
    return info

def get_disk_info():
    disk_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System": partition.fstype,
            "Total Size": f"{round(usage.total / (1024**3), 2)} GB",
            "Used": f"{round(usage.used / (1024**3), 2)} GB",
            "Free": f"{round(usage.free / (1024**3), 2)} GB",
            "Percentage Used": f"{usage.percent}%",
        })
    return disk_info

def display_info():
    print("System Information:")
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"  {key}: {value}")

    print("\nDisk Information:")
    disk_info = get_disk_info()
    for disk in disk_info:
        print("  Disk:")
        for key, value in disk.items():
            print(f"    {key}: {value}")

if __name__ == "__main__":
    try:
        display_info()
    except Exception as e:
        print(f"An error occurred: {e}")
