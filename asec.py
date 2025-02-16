import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        sys.exit(1)

def update_system():
    run_command("sudo apt-get update -y")
    run_command("sudo apt-get upgrade -y")
    run_command("sudo apt-get dist-upgrade -y")
    run_command("sudo apt-get autoremove -y")
    run_command("sudo apt-get autoclean -y")

def install_security_tools():
    tools = [
        "nmap", "wireshark", "tcpdump", "nikto", "john", "hydra", "metasploit-framework",
        "aircrack-ng", "kismet", "gobuster", "sqlmap", "dirb", "ophcrack", "lynis",
        "chkrootkit", "rkhunter", "fail2ban", "clamav", "ufw", "gufw", "openssh-server",
        "openssl", "sslscan", "sslyze", "testssl.sh", "nikto", "wapiti", "openvas",
        "snort", "suricata", "bro", "zeek", "osquery", "tripwire", "aide", "auditd",
        "selinux-basics", "apparmor", "tiger", "bastille", "lynis", "lynis", "lynis"
    ]
    for tool in tools:
        run_command(f"sudo apt-get install -y {tool}")

def configure_firewall():
    run_command("sudo ufw enable")
    run_command("sudo ufw default deny incoming")
    run_command("sudo ufw default allow outgoing")
    run_command("sudo ufw allow ssh")
    run_command("sudo ufw allow http")
    run_command("sudo ufw allow https")

def harden_ssh():
    ssh_config = "/etc/ssh/sshd_config"
    with open(ssh_config, "r") as file:
        lines = file.readlines()
    with open(ssh_config, "w") as file:
        for line in lines:
            if line.startswith("#PermitRootLogin"):
                file.write("PermitRootLogin no\n")
            elif line.startswith("#PasswordAuthentication"):
                file.write("PasswordAuthentication no\n")
            elif line.startswith("#PubkeyAuthentication"):
                file.write("PubkeyAuthentication yes\n")
            elif line.startswith("#AllowTcpForwarding"):
                file.write("AllowTcpForwarding no\n")
            elif line.startswith("#X11Forwarding"):
                file.write("X11Forwarding no\n")
            else:
                file.write(line)
    run_command("sudo systemctl restart sshd")

def install_antivirus():
    run_command("sudo apt-get install -y clamav clamav-daemon")
    run_command("sudo freshclam")
    run_command("sudo systemctl start clamav-daemon")
    run_command("sudo systemctl enable clamav-daemon")

def install_malware_tools():
    run_command("sudo apt-get install -y rkhunter chkrootkit")
    run_command("sudo rkhunter --check")
    run_command("sudo chkrootkit")

def configure_auditd():
    run_command("sudo apt-get install -y auditd")
    run_command("sudo auditctl -e 1")
    run_command("sudo systemctl start auditd")
    run_command("sudo systemctl enable auditd")

def install_network_security_tools():
    run_command("sudo apt-get install -y ettercap-graphical dsniff driftnet")
    run_command("sudo apt-get install -y netsniff-ng tshark")
    run_command("sudo apt-get install -y netcat socat")

def install_web_security_tools():
    run_command("sudo apt-get install -y burpsuite zaproxy")
    run_command("sudo apt-get install -y wpscan joomscan")
    run_command("sudo apt-get install -y skipfish wapiti")

def install_password_tools():
    run_command("sudo apt-get install -y hashcat crunch")
    run_command("sudo apt-get install -y cewl wordlists")

def install_forensic_tools():
    run_command("sudo apt-get install -y sleuthkit autopsy")
    run_command("sudo apt-get install -y foremost scalpel")
    run_command("sudo apt-get install -y binwalk")

def install_vpn_tools():
    run_command("sudo apt-get install -y openvpn wireguard")
    run_command("sudo apt-get install -y tor torsocks")

def install_misc_tools():
    run_command("sudo apt-get install -y git curl wget")
    run_command("sudo apt-get install -y vim tmux htop")
    run_command("sudo apt-get install -y python3-pip python3-venv")

def main():
    update_system()
    install_security_tools()
    configure_firewall()
    harden_ssh()
    install_antivirus()
    install_malware_tools()
    configure_auditd()
    install_network_security_tools()
    install_web_security_tools()
    install_password_tools()
    install_forensic_tools()
    install_vpn_tools()
    install_misc_tools()

if __name__ == "__main__":
    main()
