from modules.dns_lookup import dns_lookup
from modules.whois_lookup import whois_lookup


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

        elif choice in ["3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            under_development()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\n[-] Invalid option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()