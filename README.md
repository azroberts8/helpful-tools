# Helpful Tools
A collection of simple tools, commands & solutions that I'll likely need again. Small solutions are featured directly on this page while more involved solutions are linked to additional pages.

## Deeper Guides

 - **[Program Arduino Uno with AVR](./AVR-PWM-on-Arduino-Uno)**
 - **[Change MAC Address](./Change-MAC-Address)**
 - **[CTF Docker Image](./CTF-Docker)**
 - **[Fooocus AI Image Generation on GCP](./Fooocus-on-GCP)**
 - **[Docker LAMP Stack](./LAMP-Image)**
 - **[Running Mixtral LLM on GCP](./Mixtral-on-GCP)**
 - **[Secure SSH Keygen (2024)](./SSH-Keygen)**
 - **[Creating & Using GPG Keys](./gpg-usage)**
 - **[WiFi Cracking with Aircrack](./wifi-pwd-cracking)**

## Installing Docker on Linux

*Official Documentation: https://docs.docker.com/engine/install/debian*

### Add Docker's GPG Key
```bash
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### Add Docker's Repository to Apt Sources
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker
Full docker desktop installation
```bash
sudo apt update
sudo apt install docker.io
```

Headless Docker installation
```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Adding User to Docker Group
*This is so that you do not need to prefix every Docker command with `sudo`*
```bash
sudo usermod -aG docker $(whoami)
```
*In my testing a session restart is not sufficent, you will need to reboot before you can run Docker without `sudo`*

### Docker Hello World
```bash
docker run hello-world
```

## Installing VirtualBox from `apt` on Debian

*Official Documentation: https://virtualbox.org/wiki/Linux_Downloads*

### Add Official Virtualbox Source
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/oracle-virtualbox-2016.gpg] https://download.virtualbox.org/virtualbox/debian $(. /etc/os-release && echo "$VERSION_CODENAME") contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list > /dev/null
```

### Add Oracle GPG Key
```bash
wget -O- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --yes --output
```

### Install Virtualbox
```bash
sudo apt update
sudo apt install virtualbox-7.0
```
