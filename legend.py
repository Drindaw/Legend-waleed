import requests
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def approval():
    """Clear the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def raj_logo():
    """Display the logo and clear the screen after displaying it."""
    logo = r"""
            
      
       
    
     
          
                                                       

    """.format(Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.BLUE, Fore.WHITE)

    print(Fore.MAGENTA + Style.BRIGHT + logo)

def show_termux_message():
    """Display the custom message after the logo."""
    termux_message = r"""
╔═══════════════════════════════════════════════════════════════════════════╗
║  {0}WONER      : WALEED                                                   ║
║  {1}RULL3X     : THE BR3ND WALEED                                          ║
║  {1}FACEBOK    : ❮❮  𓆩DRINDAW𓆪  ❯❯                                            ║
║  {2}RULS       : MULTI TOKEN CONVO                                           ║
║  {3}GITHUB     : L3G3ND XD                                                   ║ 
║  {1}WH9TS9P    : 0000000000000                                              ║
╚═══════════════════════════════════════════════════════════════════════════╝
""".format(Fore.RED, Fore.GREEN, Fore.BLUE, Fore.WHITE)
    print(Fore.GREEN + Style.BRIGHT + termux_message)

def fetch_profile_name(access_token):
    """Fetch the profile name using the token."""
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    """Fetch the target profile name using the target ID and token."""
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except requests.exceptions.RequestException:
        return "Unknown Target"

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    """Send messages to the target profile."""
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    # Fetch the profile name for each token
    token_profiles = {token: fetch_profile_name(token) for token in tokens}

    # Fetch the target profile name
    target_profile_name = fetch_target_name(target_id, tokens[0])  # Using the first token for the target fetch

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                print(Fore.GREEN + f"\n┌────────────────────────────────────────────────────────────────────┐")
                print(Fore.CYAN + f"[✔] {Fore.YELLOW}Message {message_index + 1} Successfully Sent!")
                print(Fore.CYAN + f"[👤] Sender: {Fore.MAGENTA}{sender_name}")
                print(Fore.CYAN + f"[📩] Target: {Fore.MAGENTA}{target_profile_name} ({target_id})")
                print(Fore.CYAN + f"[📨] Message: {Fore.LIGHTGREEN_EX}{full_message}")
                print(Fore.CYAN + f"[⏰] Time: {Fore.LIGHTBLUE_EX}{current_time}")
                print(Fore.GREEN + f"└────────────────────────────────────────────────────────────────────┘\n")
                print(Fore.YELLOW + "\033[1;37m<<======== MADE BY THE BR3ND WALEED😈🩷 ======>>")
                print("\n" + ("─" * 80) + "\n")
            except requests.exceptions.RequestException:
                continue  # Ignore error and continue sending next message
            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()  # Clear screen before displaying the logo
    raj_logo()  # Display logo
    show_termux_message()  # Show the custom message

    approval()  # Clear screen before starting inputs
    tokens_file = input(Fore.GREEN + "[+] ENTER-THE-TOKENS-FILE=>> ").strip()

    approval()  # Clear screen before further inputs
    target_id = input(Fore.YELLOW + "[+] ENTER-THE-TARGET-ID=>> ").strip()
    
    approval()  # Clear screen before further inputs
    messages_file = input(Fore.YELLOW + "[+] ENTER-----GALI-FILE=>> ").strip()

    approval()  # Clear screen before further inputs
    haters_name = input(Fore.YELLOW + "[+] ENTER-HATER-NAME=>> ").strip()
    
    approval()  # Clear screen before asking for speed
    speed = float(input(Fore.GREEN + "[+] ENTER THE SPEED (IN SECONDS) BETWEEN MESSAGES=>> ").strip())

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
