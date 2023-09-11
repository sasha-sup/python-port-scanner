import socket

# List of ports to scan.
ports = [22, 80, 443, 1194]

with open("./ip_list", "r") as read_from:
    lines = read_from.readlines() 
    for line in lines:
        host = line.rstrip()
        if not host:
            continue  
        print(f"\nWait, port scanning is in progress for {host}!")
        for port in ports:
            s = socket.socket()
            s.settimeout(1)
            try:
                s.connect((host, port))
            except socket.error:
                pass
            else:
                with open("./result", "a") as write_to:
                    write_to.write(f"{host}: {port} port is active\n")
                    print(f"{host}: {port} port is active")

            s.close()

print("Scan complete!")

