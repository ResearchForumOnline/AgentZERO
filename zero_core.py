import requests
import time
import sys
import paramiko
import getpass
from colorama import Fore, Style, init

init()

# CONFIG
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma2:9b"

# --- SSH MODULE (The Remote Hand) ---
def ssh_execute(host, user, password, command):
    """
    Connects to a remote server and executes a command.
    Includes Safety Interlock for destructive commands.
    """
    # SAFETY INTERLOCK: P(G) Check
    risky_keywords = ["rm -rf", "mkfs", "dd", ":(){ :|:& };:"]
    if any(keyword in command for keyword in risky_keywords):
        print(f"{Fore.RED}[CRITICAL WARNING] Destructive command detected: {command}{Style.RESET_ALL}")
        confirm = input(f"{Fore.RED}Type 'EXECUTE' to confirm this action > {Style.RESET_ALL}")
        if confirm != "EXECUTE":
            return "Action Aborted by Safety Protocol."

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password, timeout=10)
        
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        
        client.close()
        return output if output else error
    except Exception as e:
        return f"SSH Error: {str(e)}"

# --- BRAIN MODULE ---
def ask_ollama(prompt):
    try:
        # We inject the capability into the system prompt
        system_instruction = (
            "You are Agent Zero. You can SSH into servers. "
            "To SSH, output JSON: {\"action\": \"ssh\", \"target\": \"IP\", \"cmd\": \"command\"}. "
            "Otherwise, just answer normally."
        )
        
        res = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": f"{system_instruction} User: {prompt}",
            "stream": False
        })
        return res.json()['response']
    except:
        return "Brain Offline (Ollama Error)"

# --- MAIN LOOP ---
def main():
    print(f"{Fore.CYAN}=== OPENZERO: SSH ENABLED ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Commands: 'ssh <ip> <user> <cmd>' or chat normally.{Style.RESET_ALL}")
    
    # Credentials cache (Temporary for session)
    current_ssh_pass = None
    
    while True:
        user_input = input(f"{Fore.GREEN}ZERO > {Style.RESET_ALL}").strip()
        if user_input.lower() in ["exit", "quit"]: break

        # Direct SSH Command Parser
        if user_input.startswith("ssh "):
            try:
                # Format: ssh 192.168.1.5 root ls -la
                parts = user_input.split(" ")
                target_ip = parts[1]
                target_user = parts[2]
                cmd = " ".join(parts[3:])
                
                if not current_ssh_pass:
                    current_ssh_pass = getpass.getpass(f"Password for {target_user}@{target_ip}: ")
                
                print(f"{Fore.MAGENTA}Connecting to {target_ip}...{Style.RESET_ALL}")
                result = ssh_execute(target_ip, target_user, current_ssh_pass, cmd)
                print(f"\n{Fore.WHITE}{result}{Style.RESET_ALL}\n")
            except IndexError:
                print("Usage: ssh <ip> <user> <command>")
        
        else:
            # Normal Chat
            print(ask_ollama(user_input))

if __name__ == "__main__":
    main()
