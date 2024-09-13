# Download and install the libu2f-udev package
wget http://archive.ubuntu.com/ubuntu/pool/main/libu/libu2f-host/libu2f-udev_1.1.4-1_all.deb
sudo dpkg -i libu2f-udev_1.1.4-1_all.deb

# Download and install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt -f install -y

# Get the version of ChromeDriver installed
CHROME_DRIVER_VERSION=$(dpkg -s google-chrome-stable | grep '^Version:' | grep -oP '\d+\.\d+\.\d+\.\d+')
wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P /tmp/

# Unzip and set permissions for ChromeDriver
unzip -o /tmp/chromedriver_linux64.zip -d /tmp/
chmod +x /tmp/chromedriver
sudo mv /tmp/chromedriver /usr/local/bin/chromedriver

# Install Selenium
pip install selenium
pip install chromedriver-autoinstaller
