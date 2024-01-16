# Running Mixtral 8x7B AI LLM on GCP
Mixtral is an LLM similar to ChatGPT but differs in the fact that it is completely free and open source meaning that we have the ability to run it on our own hardware and integrate custom uncensored models. Although it is becoming more common to find consumer devices with the necessary hardware, the minimum system requirements are still quite high so for the sake of this guide we will be running Mixtral on Google Cloud.

In this guide we will be running Mixtral on GCP with an easy-to-use CLI tool, [Ollama](https://github.com/jmorganca/ollama), with the [Dolphin Mixtral 8x7B](https://huggingface.co/cognitivecomputations/dolphin-2.6-mixtral-8x7b) model which aims to be an unaligned, unbiased, and as a result uncensored model. This means by the end of this guide we can reclaim our freedom 🇺🇸 by creating a chatbot that is nearly on par with ChatGPT without restrictions on topics that are legally or morally questionable. Read [this article](https://erichartford.com/uncensored-models) by the creator of the Dolphin model for why unbiased and uncensored models are a good thing. Alternatively, we could also use the [Oobabooga WebUI](https://github.com/oobabooga/text-generation-webui) in place of Ollama, however I have yet to have any luck getting it to work with the resources available to mortals on GCP.

If you would like to take your freedom a step further 🤠 and have the hardware to do so, this guide should also work natively on most standard Linux distributions.

*Side note:* Uncensored freedom aside, many corporations have expressed concerns of services like ChatGPT potentially leaking company IP if used by their employees. Open source models such as Mixtral provide a solution to this issue providing them with the ability to run a local instance of an LLM ensuring that their company IP is not leaked to other users outside their organization.

## VM Setup
Ollama features suport for running models both directly on the CPU and accelerated by the GPU. Considering that we want our text generation to run at a decent rate, we will choose the latter option and create a VM with an NVIDIA T4. If you have not done this before, Google may ask for you to request an increase in your GPU quota. 1 GPU will be plenty sufficient for our purposes. For my setup I'll be using an n1-standard-16 instance and adding a 70GB SSD. An n1-standard-8 should also be sufficient with 30GB of memory however the extra cores provided with the 16 can provide slightly better performance. To save time we can also use the "Deep Learning VM with CUDA 11.8 M114" image provided by Google rather than the standard Debian 11 image as this image comes with the NVIDIA drivers preloaded on the system. If you do not see this option or enjoy making your life more difficult, it is also possible to stick with the base Debian 11 image and manually install Google's NVIDIA drivers later. I also recommend using spot pricing to significantly reduce your machine cost. My machine looks like this:

- NVIDIA T4 GPU
- 8 CPU Cores (16 threads)
- 60GB RAM
- 70GB SSD
- Deep Learning with CUDA Image
- Spot Pricing (for reduced cost)

*For me, this configuration has come to a total of $0.31/hour to run*

## First Boot-up
If you chose the Deep Learning image insead of the base Debian image in the previous step the upon first boot you should be prompted to install the GPU drivers. Select "Y" and press enter. This may take a few minutes for it to complete installing the drivers.

## Installing & Using Ollama
After the GPU driver is installed, we'll perform a package update and install Ollama.
```bash
sudo apt update
sudo apt upgrade
curl https://ollama.ai/install.sh | sh
```

I personally like to install tmux as well which allows us to run multiple BASH sessions from the same SSH connection and easily reconnect to our session if our SSH connection dies.

```bash
sudo apt install tmux
```

Now is the moment we've all been waiting for, the time has come for us to put our cowboy hats on 🤠 and wave our freedom flags 🇺🇸 as we launch our unchained chatbot

```bash
ollama run dolphin-mixtral:latest
```

This will launch Ollama and begin downloading the latest version of dolphin-mixtral. This may take a few minutes to download the complete model. Once it is complete you can type prompts the same way you would to any other LLM such as ChatGPT.

