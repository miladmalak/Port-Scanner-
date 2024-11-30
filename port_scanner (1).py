import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # وقت الانتظار
            s.connect((ip, port))
            return f"[+] Port {port} is open"
    except:
        return f"[-] Port {port} is closed"

def main():
    print("Simple Port Scanner")
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(scan_port, target_ip, port)
            for port in range(start_port, end_port + 1)
        ]
        for future in futures:
            print(future.result())

if __name__ == "__main__":
    main()
