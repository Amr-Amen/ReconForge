import socket


def dns_lookup():
    target = input("\nEnter domain: ")

    try:
        ip = socket.gethostbyname(target)

        print("\n========== DNS Lookup ==========")
        print(f"Domain : {target}")
        print(f"IP      : {ip}")

    except socket.gaierror:
        print("\n[-] Unable to resolve domain.")