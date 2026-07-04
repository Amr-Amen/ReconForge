import whois


def whois_lookup(target):
    try:
        data = whois.whois(target)

        print("\n========== WHOIS Lookup ==========")
        print(f"Domain          : {data.domain_name}")
        print(f"Registrar       : {data.registrar}")
        print(f"Creation Date   : {data.creation_date}")
        print(f"Expiration Date : {data.expiration_date}")
        print(f"Name Servers    : {data.name_servers}")

    except Exception as e:
        print(f"\n[-] Error: {e}")