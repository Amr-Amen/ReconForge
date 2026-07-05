import subprocess
import shutil
import time

from yaspin import yaspin
from tabulate import tabulate

from utils.ui import title, section, success, error, info


def port_scanner(target):

    title("Port Scanner")

    if shutil.which("nmap") is None:
        error("Nmap is not installed.")
        return []

    section("Scan Options")

    print("[1] Quick Scan (Top 100 Ports)")
    print("[2] Standard Scan (1-1024)")
    print("[3] Full Scan (1-65535)")

    choice = input("\nSelect Scan Type: ")

    if choice == "1":
        command = [
            "nmap",
            "-Pn",
            "-T4",
            "-sV",
            "--top-ports",
            "100",
            target
        ]
        scan_name = "Quick Scan"

    elif choice == "3":
        command = [
            "nmap",
            "-Pn",
            "-T4",
            "-sV",
            "-p-",
            target
        ]
        scan_name = "Full Scan"

    else:
        command = [
            "nmap",
            "-Pn",
            "-T4",
            "-sV",
            "-p",
            "1-1024",
            target
        ]
        scan_name = "Standard Scan"

    info("Preparing scanner...")

    start_time = time.time()

    with yaspin(text="Scanning target...", color="cyan") as spinner:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        spinner.ok("✔")

    end_time = time.time()

    scan_time = round(end_time - start_time, 2)

    output = result.stdout.splitlines()

    open_ports = []

    services = set()

    for line in output:

        if "/tcp" in line and "open" in line:

            parts = line.split()

            if len(parts) < 3:
                continue

            port = parts[0]
            state = parts[1]
            service = parts[2]

            if len(parts) > 3:
                version = " ".join(parts[3:])
            else:
                version = "Unknown"

            open_ports.append([
                port,
                state.upper(),
                service.upper(),
                version
            ])

            services.add(service.upper())

    section("Open Ports")

    if open_ports:

        print(
            tabulate(
                open_ports,
                headers=[
                    "Port",
                    "State",
                    "Service",
                    "Version"
                ],
                tablefmt="grid"
            )
        )

    else:

        error("No open ports found.")

    section("Scan Summary")

    success(f"Open Ports : {len(open_ports)}")

    success(f"Scan Time  : {scan_time} Seconds")

    info(f"Scan Type   : {scan_name}")

    print()

    if services:

        info("Detected Services")

        for service in sorted(services):
            print(f"  • {service}")

    return open_ports