# Creating & Using GPG Keys (Cheat Sheet)

### MacOS Installation

#### GPG
```bash
brew install gnupg
```

#### Pinentry (store GPG key password in Keychain)
```bash
brew install pinentry-mac
```

### Generating GPG Keys

```bash
gpg --full-generate-key
```

### Listing Available Keys

```bash
gpg --list-keys
```

### Deleting Keys

1. Run `gpg --list-keys` and node the identifier of the key you want to remove
2. Delete the secret key (if available) `gpg --delete-secret-key <identifier>`
3. Delete the public key `gpg --delete-key <identifier>`

### Exporting Keys

```bash
gpg --export --armor --output <filename>.pub <email>
```

This command exports your identify (public key) to the file that you define

### Importing Keys

```bash
gpg --import <filename>.pub
```

### Signing Someone's Public Key

Signing person A's public key with your private key demonstrates to person B that you trust person A. If person B trusts you (has your identity added) they can verify that you trust person A and can choose to trust person A by association.

```bash
gpg --sign-key <email>
```
Note: the email address is the address associated with they key you are signing

Typically, after you have signed a key you would then export that key and send it to a friend so they have the identity of and can trust the identity you have signed

### Making Your Identity Highly Available

https://pgp.mit.edu/ is a popular key server for exchanging and looking up identities. This site can be visited in your browser allowing you to manually paste your key & look up other's keys or you can interface with it directly through the GPG command line tool.

##### Publishing Your Public Key

```bash
gpg --send-keys --keyserver pgp.mit.edu <key-id>
```

##### Looking Up Others' Identities

```bash
gpg --keyserver pgp.mit.edu --search-keys <search-parameters>
```

Note: Search parameters can be the name, email, or other details associated with an identity


### Signing & Verifying Messages Using Key

##### Signing a Message

Signing a message allows a recipient to verify the author of the message assuming that they have the public key identity of the author added to their identity list.

1. Create a file containing the data you would like to sign `echo "Hello World!" > message.txt`
2. Sign the file `gpg --output message.sig --sign message.txt`

This will create a new file containing the original message and the signature to validate it which can be verified with your public key

##### Verifying a Message

```bash
gpg --output decrypted.txt --decrypt message.sig
```

This command will output the identity and validity of the signed message to the console and write the contents/message to the file `decrypted.txt`

### Encrypting a Message

```bash
gpg --encrypt --sign --armor -r <recipient@example.com> <message.txt>
```
Note: This command will sign the message with your private key as well as encrypt the message with the recipient's public key so that only the the recipient can decrypt it using their private key and they can verify you as the author using your public key identity.

### Decrypting a Message

```bash
gpg --decrypt --output <decrypted-message> <encrypted-file>.asc
```

### Using GPG To Sign Commits

1. Install `pinentry-mac` (for storing GPG password in keychain on Mac)
```bash
brew install pinentry-mac
```
2. Set pinentry-mac as GPG pinentry program
```bash
mkdir ~/.gnupg
echo "use-agent" >> ~/.gnupg/gpg.conf
echo "pinentry-program /usr/local/bin/pinentry-mac" >> ~/.gnupg/gpg-agent.conf
echo "export GPG_TTY=$(tty)" >> ~/.zshrc
source ~/.zshrc
```
*Use `/opt/homebrew` for Apple Silicon; use `/usr/local` for x86*

3. Generate GPG Key
```bash
gpg --full-generate-key
```
4. List the key ID
```bash
gpg --list-keys --keyid-format LONG
```
*The ID is listed on the first line after the algorithm*

5. Configure Git
```bash
git config --global user.signingkey KEY-ID
git config --global commit.gpgsign true
```
6. Add public key to GitHub
```bash
gpg --armor --export KEY-ID
```
*Add the output of this to GitHub*