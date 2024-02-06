# Running Fooocus AI Image Generation on GCP
So you want to use AI image generation tools but the online solutions are too restricted and produce mediocre results. You want to try tools like stable diffusion and Foocus on your own machine but your wallet said no to a fancy graphics card. The solution... run it on the cloud for pennies an hour! For typical use cases this will be orders of magnitude cheaper than purchasing your own GPU. At the time of writing this, the setup documented in this guide should cost roughly $0.22/hour of runtime. Lets get started!

## Google Cloud Basics
Running Fooocus requires access to cloud VMs with GPUs. If you have any free Google Cloud credit, it cannot be applied towards instances with GPUs so we will need to add a payment method to our account. If you have not already set up a payment method you can proceed with the following steps until you are prompted to do so.

Lets start by navigating to `cloud.google.com` and proceeding to the cloud console. Then select the navigation panel in the top left corner and navigate to the Compute Engine tab. Under VM Instances select Create Instance.

## VM Settings
We'll create a VM with the following specifications:
* GPU type: NVIDIA T4
* Number of GPUs 1
* Machine Type: n1-standard-8 (or any machine with ≥4 cores and ≥30GB memory)
* Use spot pricing to cut your cost nearly in half
* A minimum of 50GB of harddisk space (if planning to use more than 1 model add 10GB per model; note: storage space cannot be increased later)
* Use the Deep Learning VM with CUDA 11.8 machine image (comes with Debian 11, Python 3.10, and CUDA 11.8)

Create and start the Virtual Machine

## Setting Up the VM
Once we create and launch our VM we can connect to it using Google's provided SSH feature in the browser. If you selected the Deep Learning image in the previous step, our machine will automatically prompt us to install the CUDA drivers. Select yes when prompted, it will then take a few minutes to install the drivers.

If you did not select the Deep Learning image in the previous step you will have to manually install the GPU drivers and build Python 3.10 from source. This can take some time but I have included the details below for how to do this.

### Installing GPU Drivers
Debian may not come with the necessary drivers to use the GPU. If that is the case you will need to install them with the following commands.
```bash
curl https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-installation/main/linux/install_gpu_driver.py --output install_gpu_driver.py
sudo python3 install_gpu_driver.py
```

### Building Python 3.10 From Source
Fooocus, like other AI and ML programs that run on python, is picky about what Python versions they work with. At the time of writing this, the [Fooocus documentation](https://github.com/lllyasviel/Fooocus) states that it has been tested to work on Python 3.10 so for the purposes of this guide we will be using Python 3.10 to run Fooocus. However, since python 3.10 has been depricated, we will need to build it from source manually.

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
We can use the command below to clone the Fooocus repository, create a python virtual environment using python3.10 and install the required packages. (This may take a while)
```bash
cd ~/
git clone https://github.com/lllyasviel/Fooocus.git
cd Fooocus
python3.10 -m venv fooocus_env
source fooocus_env/bin/activate
pip install -r requirements_versions.txt
```

## Running Fooocus
If you have just completed the previous step you should already be using the Python 3.10 virtual environment that you created. However, if you have restarted your virtual machine or shell session you will need to run the following commands before running Fooocus to reactivate your python virtual environment.
```bash
cd ~/Fooocus
source fooocus_env/bin/activate
```

We can now launch the Fooocus server using the command below. Note that we have included the `--share` flag which allows us to connect to the webUI externally. Fooocud will connect to a proxy server and provide you with a link that allows you to access the Fooocus UI from any machine via the web browser.
```bash
python entry_with_update.py --share
```

Optionally, if you would like a more private connection to your instance, you can install a private VPN software such as [Tailscale](https://tailscale.com) then use the `--listen` flag when launching Fooocus to allow LAN connections. VPN software such as Tailscale enables devices on your virtual network communicate more similarly to if they were on the same physical network allowing you to to connect to your machine in the browser without a publicly exposed proxy link.
```bash
python entry_with_update.py --listen
```
Assuming that Tailscale is configured correctly on both the GCP VM and your personal machine, you should be able to access the Fooocus web UI from your personal machine by navigating to `http://<vm-hostname>:7865`