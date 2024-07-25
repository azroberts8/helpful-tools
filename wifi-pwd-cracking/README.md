# Wi-Fi Cracking & Setup with Aircrack-ng

For this guide I will be using the [Alfa AWUS036ACS USB Wi-fi Adapter](https://www.amazon.com/gp/product/B0752CTSGD/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) as it is relatively inexpensive and discrete compared to similar devices. Unfortunately this device is not supported out-of-the-box in Linux (tested Debian 12 & Kali 2024.2) so we will first have to install drivers before we can use the device.

## Driver Installation

Alfa provides documentation for compiling and installing the appropriate drivers on Kali, Ubuntu, Debian, and Raspbian which can be found [here](https://docs.alfa.com.tw/Support/Linux/RTL8811AU/). I have also detailed some of their documentation below along with my own experiences.

*Note:* If the previously mentioned link is dead at any point in the future, the Alfa AWUS036ACS is based on the RTL8811AU chipset. Drivers are chipset-specific not necessarily device-specific.

*Important Repositories:*
aircrack-ng/rtl8812au: https://github.com/aircrack-ng/rtl8812au
morrownr/8821au-20210708: https://github.com/morrownr/8821au-20210708

### Kali Driver Installation

Install:
```bash
sudo apt update
sudo apt install realtek-rtl88xxau-dkms
```

Verify Installation:
```bash
find /lib/modules/`uname -r`/ -name "88XXau.ko"
```
*Note:* In my testing Kali **did not** find any results when running this command after installation

### Debian Driver Installation

Install:
```bash
sudo apt update
which dkms || sudo apt install dkms
which rfkill || sudo apt install rfkill
which git || sudo apt install git

git clone https://github.com/morrownr/8821au-20210708.git
cd 8821au-20210708
sudo ./install-driver.sh
```

Verify Installation:
```bash
find /lib/modules/`uname -r`/ -name "8821au.ko"
```
*Note:* In my testing Kali **did** find the binaries from the installation. If the Kali install did not succeed, possibly try the Debian or Ubuntu installation on your Kali box. Not sure why these have different installation methods.


## Using Aircrack to Crack Wi-Fi

To be continued...