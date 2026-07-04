from modules.dns_lookup import dns_lookup


def banner():
    print("=" * 50)
    print("              ReconForge v1.0")
    print(" Python Reconnaissance Framework")
    print("=" * 50)


def menu():
    print("\n[1] DNS Lookup")
    print("[2] WHOIS Lookup")
    print("[3] HTTP Header Analysis")
    print("[4] Port Scanner")
    print("[5] Banner Grabbing")
    print("[0] Exit")


def main():
    while True:
        banner()
        menu()

        choice = input("\nSelect an option: ")

        if choice == "1":
            dns_lookup()
            input("\nPress Enter to continue...")

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nThis module is under development.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()