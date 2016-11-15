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
sudo apt-get -y install apache2 
sudo apt-get -y install python-pip libapache2-mod-wsgi





 

su postgres -c 'createuser -dRS vagrant'


vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd

