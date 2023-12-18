# Running Fooocus AI Image Generation on GCP
So you want to use AI image generation tools but the online solutions are too restricted and produce mediocre results. You want to try tools like stable diffusion and Foocus on your own machine but your wallet said no to a fancy graphics card. The solution... run it on the cloud for pennies an hour! For typical use cases this will be orders of magnitude cheaper than purchasing your own GPU. At the time of writing this, the setup documented in this guide should cost roughly $0.22/hour of runtime. Lets get started!

## Google Cloud Basics
If you already have experience using Google Cloud you can proceed to setting up the VM.

Running Fooocus requires access to cloud VMs with GPUs. If you are using the free trial of Google Cloud, keep in mind that **your free credit cannot be applied towards VMs with GPUs** therefore you must setup a payment method. You can proceed with the following steps as directed but Google will prompt you to setup billing and request access to use GPUs at some point. Follow the prompts to make them happy and you will be able to resume these steps. 

Start by navigating to `cloud.google.com` and proceed to the cloud console. Open the navigation panel from the top left corner and go to Compute Engine. Under VM Instances select Create Instance.

## VM Settings
Create a VM with the following specifications:
* GPU type: NVIDIA T4
* Number of GPUs 1
* Machine Type: n1-standard-8 (or any machine with ≥4 cores and ≥30GB memory)
* Use spot pricing to cut your cost nearly in half
* A minimum of 50GB of harddisk space (if planning to use more than 1 model add 10GB per model; note: storage space cannot be increased later)
* Debian works well

Create and start the Virtual Machine

## Connecting To The VM
The easiest way to connect to the VM is through SSH provided in the cloud console. You may continue to use this method however I find installing tailscale on the machine and adding it to my tailnet allows for easier access in some of the later steps. However, Tailscale is **NOT required**.

### Setting Up Tailscale
**IF YOU PLAN TO USE TAILSCALE:** First setup an account at `tailscale.com`, install the tailscale client on your personal machine and authenticate your machine with your account. Then install and authenticate tailscale on the GCP VM by running the following on the VM:
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```
After following the tailscale setup you should be able to connect to your VM from your personal machine by running `ssh <vm-hostname>`.

### Installing GPU Drivers
Debian may not come with the necessary drivers to use the GPU. If that is the case you will need to install them with the following commands.
```bash
curl https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-installation/main/linux/install_gpu_driver.py --output install_gpu_driver.py
sudo python3 install_gpu_driver.py
```

## Building Python 3.10 From Source
Fooocus, like other AI and ML programs that run on python, is picky about what Python versions they work with. At the time of writing this, the [Fooocus documentation](https://github.com/lllyasviel/Fooocus) states that it has been tested to work on Python 3.10 so for the purposes of this guide we will be using Python 3.10 to run Fooocus. However, since python 3.10 has been depricated to security updates only we will need to build it from source manually. 

To start, install the tools and libraries to compile python
```bash
sudo apt update
sudo apt install git gcc make zlib1g zlib1g-dev libssl1.1 libssl-dev libffi-dev libbz2-dev lzma liblzma-dev
```

Clone, build and install Python 3.10 (this may take a while)
```bash
cd ~/
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz
tar -xvzf Python-3.10.12.tgz
cd Python-3.10.12/
./configure --enable-optimizations
make
sudo make install
```

## Setting up Fooocus
Clone the Fooocus repository, create a python virtual environment using python3.10 and install the requirments. (This may take a while)
```bash
cd ~/
git clone https://github.com/lllyasviel/Fooocus.git
cd Fooocus
python3.10 -m venv fooocus_env
source fooocus_env/bin/activate
pip install -r requirements_versions.txt
```

## Running Fooocus
If you have just completed the previous step you should already be using the Python 3.10 virtual environment that you created. However, if you have restarted your virtual machine or even just your shell session you will need to run the following commands before running Fooocus to reactivate your python virtual environment.
```bash
cd ~/Fooocus
source fooocus_env/bin/activate
```

If you did not go the route of installing Tailscale, launch the Fooocus server with the `--share` flag. This will connect to a proxy server and provide you with a link that allows you to access the Fooocus UI from any machine via the web browser.
```bash
python entry_with_update.py --share
```

If you decided to install Tailscale and would like to take a slightly more private route. Launch the Fooocus server with the `--listen` flag to allow devices on the local network to directly connect via a web browser without the use of a proxy. 
```bash
python entry_with_update.py --listen
```
Assuming that Tailscale is configured correctly on both the GCP VM and your personal machine, you should be able to access the Fooocus web UI from your personal machine by navigating to `http://<vm-hostname>:7865`