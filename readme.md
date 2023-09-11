# Port Scanner Script

This Python script scans a list of IP addresses for open ports and records the results in a file.

## Description

The script reads a list of IP addresses from a file named `ip_list` and scans them for open ports specified in the `ports` list. It records the results in a file named `result`. Each result line contains the IP address, the port, and a message indicating whether the port is active.

## Usage

1. Create a file named `ip_list` and add the list of IP addresses you want to scan, with each IP address on a new line.

2. Open the script in a Python environment and run it. Make sure you have the required Python libraries installed.

3. The script will scan each IP address for open ports and write the results to the `result` file.

## Configuration

You can configure the list of ports to scan by modifying the `ports` list in the script.

```python
ports = [22, 80, 443, 1194]

