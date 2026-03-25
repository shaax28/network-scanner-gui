import nmap

scanner = nmap.PortScanner()

target = input("Enter IP address to scan: ")

print(f"\n🔍 Scanning {target}...\n")

scanner.scan(target, '1-1000')

for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        print(f"\nProtocol: {proto}")

        ports = scanner[host][proto].keys()
        for port in sorted(ports):
            print(f"Port: {port} - State: {scanner[host][proto][port]['state']}")

print("\n✅ Scan Completed!")