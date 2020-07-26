# asuswebstorage-tray-linux

 ASUS WebStorage Tray/App-Indicator for Linux
 
 Brandon Bourret (phatwares@cpan.org)

 ASUS provides a very primitive way to sync your files to their cloud on Linux - it's a "main" app and a "sync" app
 that runs from the terminal. There is no GUI or other interface. Certainly nothing fancy like they did for Windows
 users. I got tired of it, and I was screwing around with making tray app indicators in Python ... so I thought I'd
 share with the community :-)

 You will need to have a lot of prerequisites installed on your Linux box for this to work. Primarily Python 3 and Gtk
 along with the bindings that make them work together.

 sudo apt install python3.6
 sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
 sudo apt install pycairo PyGObject

 You may also need to tweak this Python script to point to different paths if you want to have your ASUS WebStorage apps
 and/or the tray icons reside elsewhere on your system.

 Side Note: The "main.ini" file is where you'll enter your username, password, and sync folder path for ASUS WebStorage.
 After your first time running the "webstorage_main_process" app, it will overwrite the "main.ini" file with an ENCRYPTED
 version of your password for security.
