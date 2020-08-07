# asus-webstorage-tray

 ASUS WebStorage Tray/App-Indicator for Linux
 
 Brandon Bourret (phatwares@cpan.org)

 ASUS provides a very primitive way to sync your files to their cloud on Linux - it's a "main" app and a "sync" app
 that runs from the terminal. There is no GUI or other interface. Certainly nothing fancy like they did for Windows
 users. I got tired of it, and I was screwing around with making tray app indicators in Perl ... so I thought I'd
 share with the community :-)

 Some basic rules for this to work:
 
 - You must have "libappindicator" installed on your Linux distro
 
 - Your desktop environment must support tray app indicators (some don't)
 
 - This app (asus-webstorage-tray) must be located in the same directory as the ASUS executables (webstorage_main_process & webstorage_sync_process)
 
This app (and all others I publish so far) are PORTABLE APPS. That means there is no need for installation because all the program assets (images, fonts, .dll, and .so files) are packaged into the executable. Simply double-click and GO! Having said this, let me explain that some users may get a false positive warning about this app being a "Trojan". Why? Because when you execute the app, it unpacks all the aforementioned program assets into a temporary folder on your computer. Therefore, some anti-virus apps falsely identify this as malicious "Trojan Horse" activity. Please rest assured that this app is completely harmless - I would not put my real name on a malicious app.

I develop using ActivePerl (don't laugh, it's rapid development!) and "compile" with ActiveState's Perl Dev Kit (PDK).

Linux 64-bit: https://www.dropbox.com/s/5tgiuk5xetj48hr/asus-webstorage-tray?dl=0
