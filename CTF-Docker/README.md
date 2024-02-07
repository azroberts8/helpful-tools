# CTF Docker Image

This is a Docker environment that includes many of the tools needed when getting started with CTF problems. This image is an extension of [skysider/pwndocker](https://github.com/skysider/pwndocker) with some additional common CTF tools and basic tools to make the CLI environment more user/beginner-friendly.

Feel free to make pull requests to add additional tools and capabilities to this environment.

## Setting Up

### Install Docker
If you do not already have Docker installed on your system, you can get the latest version from https://www.docker.com/products/docker-desktop/.

### Create Shared Directory
Once you have docker installed, create a folder for CTF work in a memorable place on your computer. We will be mounting this folder into our Docker container so it is easy to transfer files between our host machine and our Docker container.

### Running the Docker Image
We can start our CTF Docker container by opening a terminal or command prompt and executing the command below. This command launches a new Docker container called "ctf" from my pre-made image `azroberts/pwndocker` and automatically mounts our host ctf folder at the location `/ctf/work` inside the container. It will launch bash from inside the container and provide us with an interactive shell to control the container.

**Note:** Make sure to replace `/your/directory` with the absolute path to the folder we created in the previous step. If you do not know the absolute path, you can drag the folder from your file browser to youre terminal window and it should auto-fill the path for you. If you encounter an issue where you do not have permission to execute the docker command, on Mac and Linux prefix the command with `sudo` or on Windows reopen command prompt as administrator.
```bash
docker run -it -v /your/directory:/ctf/work --name ctf azroberts/pwndocker /bin/bash
```

**Note:** If you do not know the absolute path to the folder you created, you can optionally drag the folder from your file browser to your terminal or command prompt window and it should auto-fill the absolute path for you.

If you recieve an error that you do not have permission to run docker, on Mac and Linux you can prefix the above command with `sudo` to resolve this issue or on Windows, run commmand prompt as administrator.

At this point we are good to start CTFing! Note that only files saved under our mounted directory will be retained if we stop our container.

## Included Tools

This environment is an extension of [skysider/pwndocker](https://github.com/skysider/pwndocker) and as such comes with all the tools and functionality included in that environment. Additionally the following packages have been installed:

- sudo (for when muscle memory takes control)
- nano (personal preference over vim)
- [binwalk](https://github.com/ReFirmLabs/binwalk)
- [dnsutils](https://packages.debian.org/buster/dnsutils)
- [steghide](https://github.com/StefanoDeVuono/steghide)
- [hexcurse](https://github.com/LonnyGomes/hexcurse) (basic hex editor)
- [nmap](https://github.com/nmap/nmap)