# Running Mixtral 8x7B AI LLM on GCP
Mixtral is an LLM similar to ChatGPT but differs in the fact that it is completely free and open source meaning that we have the ability to run it on our own hardware and integrate custom uncensored models. Currently, the minimum system requirements are still quite high and most of us do not have the sufficient RAM of 64GB installed in our laptops yet.

In this guide we will be running Mixtral on GCP with an easy-to-use CLI tool, [Ollama](https://github.com/jmorganca/ollama), with the [Dolphin Mixtral 8x7B](https://huggingface.co/cognitivecomputations/dolphin-2.6-mixtral-8x7b) model which aims to be an unaligned, unbiased, and as a result uncensored model. This means by the end of this guide we can reclaim our freedom 🇺🇸 by creating a chatbot that is nearly on par with ChatGPT without restrictions on topics that are legally or morally questionable. Read [this article](https://erichartford.com/uncensored-models) by the creator of the Dolphine model for why unbiased and uncensored models are a good thing. Alternatively, we could also use the [Oobabooga WebUI](https://github.com/oobabooga/text-generation-webui) in place of Ollama, however I have yet to have any luck getting it to work with the resources available to mortals on GCP.

If you would like to take your freedom a step further 🤠 and have the hardware to do so, this guide should also work if you have a linux distribution running on a machine with ≥64GB RAM and a decent GPU.

*Side note:* Uncensored freedom aside, many corporations have expressed concerns of services like ChatGPT potentially leaking company IP if used by their employees. Open source models such as Mixtral provide a solution to this issue providing them with the ability to run a local instance of an LLM ensuring that their company IP is not leaked to other users outside their organization.

*Side Note:* At the time of writing this (January 2024) the latest version of Dolphin Mixtral 8x7B is version 2.6. It is noted on [Dolphin's Huggingface page](https://huggingface.co/cognitivecomputations/dolphin-2.6-mixtral-8x7b) that version 3.0 is currently in the works and may be coming soon.

## VM Setup
Since Ollama currently does not feature GPU support on Linux installations, we can save some 💰 on GCP by renting a general purpose machine. For my setup I'll be using an e2-highmem-8 instance and adding a 100GB SSD. As usual, I recommend using spot pricing to significantly reduce your machine cost. Our machine should have specs like this:

- 4 CPU Cores
- 64GB RAM
- 100GB SSD
- Spot Pricing (for reduced cost)

*For me, this configuration has come to a total of $0.13/hour to run*

## Installing & Using Ollama
After our machine is started and we have SSHed into it, we'll perform a package update and install Ollama.
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

This will launch Ollama and begin downloading the latest version of dolphin-mixtral. This may take a few minutes to download the complete model. Once it is complete you can type prompts the same way you would to any other LLM. Note that because we are running our model entirely on the CPU that we will have a severe performance hit to our output and you should expect generation to take a few minutes for each prompt.

I will continue to experiment with GPU solutions to increase our performance however for now, our freedom from surveilance and censorship comes at the cost of time.

