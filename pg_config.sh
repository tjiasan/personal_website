sudo apt-get -qqy update
sudo apt-get -qqy install postgresql python-psycopg2



sudo apt-get -y install git
sudo apt-get -qqy install python-pip
sudo pip install pyvirtualdisplay selenium
sudo pip install bleach
sudo pip install django
sudo pip install djangorestframework 
sudo pip install unittest2
sudo pip install factory_boy
sudo pip install nose
sudo pip install django-nose
sudo apt-get update
sudo apt-get install -y libxss1 libappindicator1 libindicator7
# add key
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
#set repository
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#install package
sudo apt-get update
sudo apt-get install -y google-chrome-stable
sudo apt-get install xvfb
sudo apt-get install unzip


sudo wget "http://chromedriver.storage.googleapis.com/2.24/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin

 

su postgres -c 'createuser -dRS vagrant'


vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd

