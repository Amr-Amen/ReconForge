from modules.dns_lookup import dns_lookup
from modules.whois_lookup import whois_lookup
from modules.http_headers import http_headers
from modules.banner_grab import banner_grab
from modules.port_scanner import port_scanner
from modules.ssl_info import ssl_information
from modules.security_headers import security_headers
from modules.technology_detection import technology_detection
from modules.subdomain_enum import subdomain_enum

def banner():
    print("=" * 60)
    print("                 ReconForge")
    print("     Python Reconnaissance Framework")
    print("=" * 60)


def menu():
    print("\n[1] DNS Lookup")
    print("[2] WHOIS Lookup")
    print("[3] HTTP Header Analysis")
    print("[4] Port Scanner")
    print("[5] Banner Grabbing")
    print("[6] SSL Information")
    print("[7] Security Headers")
    print("[8] Technology Detection")
    print("[9] Subdomain Enumeration")
    print("[10] Directory Enumeration")
    print("[11] Run Full Recon")
    print("[0] Exit")


def under_development():
    print("\n[!] This module is under development.")
    input("\nPress Enter to continue...")


def main():
    target = input("Enter target domain: ").strip()

    while True:
        banner()
        print(f"\nCurrent Target: {target}")
        menu()

        choice = input("\nSelect an option: ")

        if choice == "1":
            dns_lookup(target)
            input("\nPress Enter to continue...")

        elif choice == "2":
            whois_lookup(target)
            input("\nPress Enter to continue...")
        elif choice == "3":
            http_headers(target)
            input("\nPress Enter to continue...")   
        elif choice == "4":
            port_scanner(target)
            input("\nPress Enter to continue...")
        elif choice == "5":
            banner_grab(target)
            input("\nPress Enter to continue...") 
        elif choice == "6":
            ssl_information(target)
            input("\nPress Enter to continue...")    
        elif choice == "7":
            security_headers(target)
            input("\nPress Enter to continue...")
        elif choice == "8":
            technology_detection(target)
            input("\nPress Enter to continue...")   
        elif choice == "9":
            subdomain_enum(target)
            input("\nPress Enter to continue...")     

        elif choice in ["10", "11"]:
            under_development()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\n[-] Invalid option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()