# Secure SSH Keygen (2024)

If you have found yourself here then you probably already know that SSH keys make your life easier and more secure than using password authentication. Whether logging into your remote servers or making commits to Github, provide significantly stronger security and the option to enter without the use of a password when configured correctly. Configuring inforrectly however could leave you more vulnerable. In this quick guide we'll cover the basics of generating and adding SSH key pairs with recommended settings as of early 2024.

## Algorithm & Security

We will be generating our SSH keys using the ED25519 algorithm. ED25519 is a 256-bit public-key signature system in based on elliptic curve cryptography with similar attack resistance as 128-bit symmetric ciphers. Essentially it is reguarded as the best way to secure an SSH connection in 2024. If you're like me and the phrase 'NSA back door' comes to your mind, you're most likely thinking of the [Dual Elliptic Curve Deterministic Random Bit Generator](https://en.wikipedia.org/wiki/Dual_EC_DRBG) algorithm which was withdrawn in 2014. Here's an [interesting YouTube video](https://youtu.be/nybVFJVXbww) on the mathmatics behind how that backdoor worked.

While ED25519 is based on elliptic curve cryptography there is no known backdoors as of the time of writing this in March 2024 and it is proven to be more secure than the default RSA algorithm. If you are still lacking trust in this algorithm, know that all asymmetric cryptography algorithms are based on complex number *theory* that will probably be broken within your lifetime by someone whose written more papers in their life than you have comments on the internet and it is simply your responsibility to stay up stay current on the most advanced techniques available to you at the time. 

## Generating Your SSH Key

From your client machine (ex. your laptop) use the command below to generate an SSH key pair using the ED25519 algorithm. Make sure to replace `KEYNAME-HERE` and `KEY-FILE-NAME` with a name that signifies the purpose of the key or the device you are using. For example, `-C "andrews-macbook"`.

```sh
ssh-keygen -t ed25519 -C "KEYNAME-HERE" -f ~/.ssh/KEY-FILE-NAME
```

**Explanation of the command:**
- `-t` *\[Optional\]* Defines the algorithm to be used; Default is rsa so its highly recommended to change it
- `-C` *\[Optional\]* Specifies the comment tag to place at the end of the public key. Defaults to *username*@*hostname* which can be vague
- `-f` *\[Optional\]* Specifies the output file name and location. Defaults to your current dircotry with its name being id_ed25519 (name of the algorithm)
- `-b` *\[Optional\]* Specifies the key size in bits; Recommended ≥4096-bits for RSA (only applicable to RSA; ED25519 with always be 256-bits)

When you run the above command it will prompt you for a password. This is optional and I recommend omitting it unless you foresee your client machine (your laptop) becoming compromised whether by malware or someone else having access to your files. Chances are in that scenario you would have much bigger problems on your hand than your SSH keys which you can easily revoke on the server side. The idea is that if someone did get your private key, they would not be able to use it without entering the password you set however that means that any time you want to use it you will need to enter the password.

After generating our SSH key pair we can add it to your SSH client by running the command below ensuring to replace the name with the name your set earlier

```sh
ssh-add ~/.ssh/KEY-FILE-NAME
```

## Using Your SSH Key

**WARNING:** Never, ever share your private key! It should essentially live where you have created it and never move from there!

You will find that the `ssh-keygen` command has created 2 files with the same name and one ending with `.pub` the file ending in `.pub` is your public key and the other is your private key. To add this key to your Github account follow [this guide provided by Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) for instructions on how to add your public key to your account.

To add this key to an SSH server that you have access to, sign into that server using your current means of doing so. Then use the following command to add your public key to the server. Make sure to paste the entire contents of your public key file within the quotes.

```sh
echo "YOUR-ENTIRE-KEY-HERE" >> ~/.ssh/authorized_keys
```

You should now be able to access your SSH server and push commits to your Github repositories from your machine without the need of entering a username and password or configuring git credentials on your machine.

## Additional Resources

This page is a good resource for generating SSH keys using a Yubikey https://rameerez.com/how-to-use-yubikey-to-log-in-via-ssh-to-server/