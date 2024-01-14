# Copyright
# Original author: Edino De Souza
# Repository: https://github.com/edino/PingWizard
# License: GPL-3.0 license - https://github.com/edino/TCPFlagsSender/tree/main?tab=GPL-3.0-1-ov-file

#Script Summary: The script serves as a user-friendly interface for conducting ping tests. It prompts the user to input parameters such as the destination (IP or hostname), the number of packets to send, the size of each packet, and the interval between packets. The script then constructs and executes a ping command with these parameters.

#Purpose: The purpose of the script is to simplify the process of conducting ping tests by providing a user-friendly interface. Users can easily input the desired parameters for the ping command, and the script takes care of executing the command and displaying the results. It aims to make the ping testing process accessible and customizable for users.

# BuildDate: 6:24 PM EST 2024-01-13

# A simple way to execute this script is using the following command: curl -s https://raw.githubusercontent.com/edino/TCPFlagsSender/main/ping_wizard.py | python3 -

import subprocess
import sys

def get_user_input(prompt, example):
    return input(f"{prompt} (e.g., {example}): ")

def ping(destination, count, size, interval):
    command = f"ping -c {count} -s {size} -i {interval} {destination}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("\nPing interrupted. Script execution terminated.")
        sys.exit(0)

def main():
    print("\nWelcome to the Ping Python Script!")

    destination = get_user_input("\nEnter the IP Address or hostname to ping", "example.com" "or" "8.8.8.8""")
    count = get_user_input("\nEnter the number of packets to send", "4")
    size = get_user_input("\nEnter the size of each packet in bytes", "64")
    interval = get_user_input("\nEnter the interval between packets in seconds", "1")

    ping(destination, count, size, interval)

if __name__ == "__main__":
    main()
