# GitSaw

This project provides a self-contained virtual environment running GitSaw.

Installation
Requirements: this is meant to run on almost any system. However, you will need a substantial amount of RAM (4 GB) and disk space (5 GB).
Install Vagrant.
Install VirtualBox.
Download this repository as a zip archive and unzip it. Note the folder you unzip it into.
Open a terminal (of your choice) and change to the folder from the last step. (Use the cd command.) You're in the right place if, when you enter ls and press Return, you see Vagrantfile among those listed.
Enter the command: vagrant box add generic/ubuntu2010 and press Return.
Enter the command: vagrant up and press Return. Now begins a long process of downloading and installing software. This will require a large amount of disk space and time to complete (on my machine, it took about 5GB and about an hour of downloading and installing). You will know it is finished when you get a new command prompt (and hopefully no error messages).

Testing
Open your web browser and visit http://localhost:3010 (nology.training/api). You will be prompted to GitSaw login screen. Enter your username and password for vagrant and log in.
Enter vagrant destroy and press Return.

Starting and stopping the virtual machine
Before you can use GiitSaw in your web browser, you have to start the virtual machine. That is what vagrant up does. (It's much faster after the first time, because there's no new software to install.) Once you are done working, you will want to reclaim the (large) amount of RAM required to run all this software locally. That is the purpose of the command vagrant destroy.
