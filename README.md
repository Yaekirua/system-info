# System Information Script

This script provides detailed information about your system, including OS details, CPU, memory, GPU (if available), and disk usage. It is useful for monitoring and troubleshooting hardware configurations.

## Requirements

The following Python packages are required to run the script:

- `psutil`: For system and process information (CPU, memory, disk usage).
- `platform`: For retrieving basic information about the operating system.
- `socket`: For fetching the system's hostname and IP address.

If you want to detect GPU information on Windows, you also need the `wmi` module. You can install it with:


### Optional (for Linux/macOS systems)
If you are running the script on Linux or macOS, `subprocess` is used to fetch GPU details using the `lspci` command. Ensure that `lspci` is available on your system.

## Features

- **System Information**:
  - OS name and version
  - OS release
  - Architecture (32/64-bit)
  - Processor name and cores
  - Total RAM and logical CPUs
  - Hostname and IP address
  - GPU (on Windows and Linux/macOS)
  
- **Disk Information**:
  - Mountpoint, file system type
  - Total size, used, free space, and percentage usage of each disk partition

## How to Run

1. Install the necessary dependencies:


On Windows, if you want GPU detection, install `wmi`:


2. Save the script in a Python file (e.g., `system_info.py`).

3. Run the script
