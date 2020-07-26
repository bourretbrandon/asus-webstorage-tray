#!/usr/bin/python3

#############################################################################################################################
#																															#
# ASUS WebStorage Tray by Brandon Bourret (phatwares@cpan.org)																#
#																															#
# ASUS provides a very primitive way to sync your files to their cloud on Linux - it's a "main" app and a "sync" app		#
# that runs from the terminal. There is no GUI or other interface. Certainly nothing fancy like they did for Windows		#
# users. I got tired of it, and I was screwing around with making tray app indicators in Python ... so I thought I'd		#
# share with the community :-)																								#
#																															#
# You will need to have a lot of prerequisites installed on your Linux box for this to work. Primarily Python 3 and Gtk		#
# along with the bindings that make them work together.																		#
#																															#
# sudo apt install python3.6																								#
# sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0							#
# sudo apt install pycairo PyGObject																						#
#																															#
# You may also need to tweak this Python script to point to different paths if you want to have your ASUS WebStorage apps	#
# and/or the tray icons reside elsewhere on your system.																	#
#																															#
# Side Note: The "main.ini" file is where you'll enter your username, password, and sync folder path for ASUS WebStorage.	#
# After your first time running the "webstorage_main_process" app, it will overwrite the "main.ini" file with an ENCRYPTED	#
# version of your password for security.																					#
#																															#
#############################################################################################################################

import gi
import os
import re

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GObject, AppIndicator3

def main():
	global indicator
	indicator = AppIndicator3.Indicator.new("asus_ws_tray", icon_status(), AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
	indicator.set_title('ASUS Webstorage')
	indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
	indicator.set_menu(menu())
	GObject.timeout_add(2500, icon_change)
	Gtk.main()
  
def menu():
	menu = Gtk.Menu()
	
	title_str = Gtk.MenuItem('ASUS WebStorage')
	menu.append(title_str)
	
	start_command = Gtk.MenuItem('Start Sync')
	start_command.connect('activate', start_shell)
	menu.append(start_command)
	
	stop_command = Gtk.MenuItem('Stop Sync')
	stop_command.connect('activate', stop_shell)
	menu.append(stop_command)
	
	stop_tray = Gtk.MenuItem('Exit Tray')
	stop_tray.connect('activate', exit_tray)
	menu.append(stop_tray)
	
	menu.show_all()
	return menu

def icon_change():
	icon_path = icon_status()
	indicator.set_icon_full(icon_path, 'icon')
	return True

def icon_status():
	get_stat = app_status()
	if(get_stat):
		return("./asusws_on.png")
	else:
		return("./asusws_off.png")

def app_status():
	stat_str = os.popen("./webstorage_main_process status").read()
	matched = re.search("running", stat_str)
	return matched
  
def start_shell(_):
	os.system("./webstorage_main_process start")
  
def stop_shell(_):
	os.system("./webstorage_main_process stop")
  
def exit_tray(_):
	Gtk.main_quit()
  
if __name__ == "__main__":
	main()