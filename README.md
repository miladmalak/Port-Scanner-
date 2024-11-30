# Port-Scanner-
The project is a simple tool that scans for open ports on any device or server by entering the IP address. These ports are important because they are used to run various services on the device, such as HTTP (websites) or SSH (secure connection).
Port Scanner Tool
Overview:

This is a simple Python-based tool that scans a range of ports on a specified target IP to identify open and closed ports. The tool is designed for educational purposes and beginner-level penetration testing practice.
Features:

    Scans multiple ports in a range defined by the user.
    Uses multithreading to perform faster scans.
    Displays whether each port is open or closed.

Requirements:

    Python 3.x
    No external libraries required (uses built-in Python libraries).

How to Use:

    Clone or download this repository.
    Run the script using Python:

    python port_scanner.py

    Follow the prompts:
        Enter the target IP address.
        Enter the range of ports to scan (start port and end port).
    The tool will display the results directly in the terminal.

Example:

    Input:

Enter target IP: 192.168.1.1
Enter start port: 1
Enter end port: 100

Output:

    [+] Port 22 is open
    [-] Port 23 is closed
    [+] Port 80 is open
    ...

Disclaimer:

    This tool is for educational purposes only.
    Do not use it to scan any device or server without explicit permission. Unauthorized scanning can lead to legal consequences.

Future Improvements:

    Add a feature to save scan results in a file.
    Support for UDP port scanning.
    Include a graphical interface for ease of use
