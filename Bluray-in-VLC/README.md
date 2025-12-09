# Playing/Ripping Blurays in VLC

> Note: Java required for bluray menus but not required to play tracks

**1. Install Libaacs**
```bash
brew install libaacs
```

**2. Download Decryption Keys** 
Download and unzip `keydb.cfg` from FindVUK. Latest keys as of Dec 2025 [here](./keydb_eng.zip). This is source worked for me: http://fvonline-db.bplaced.net/

**3. Place Key file in Library Directory**
```bash
mkdir ~/Library/Preferences/aacs
cp ~/Downloads/keydb.cfg ~/Library/Preferences/aacs/
```

**4. Open VLC and play Bluray ☺️** 