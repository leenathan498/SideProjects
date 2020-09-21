from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil


'''
FILESYSTEM HELPER - JOB APPS

Whenever a Resume or Cover Letter is downloaded,
my helper cleans up any old Resume or Cover Letters to prevent clutter

'''



'''
Main Handler Class 

Through the use of triggers, delete duplicate files.

Files Currently Being Checked For :
	- Resume
	- Cover Letter
	- Resume/Cover Letter

'''

class MyHandler(FileSystemEventHandler):
	def __init__(self):
		self.c_trigger = False
		self.r_trigger = False
		self.rc_trigger = False

	def on_modified(self,event):
		if event.src_path[-4:] == ".pdf":
			if event.src_path.split("\\")[-1] == "Cover Letter (Nathan Lee) (1).pdf":
				self.c_trigger = True
			else:
				self.c_trigger = False

			if event.src_path.split("\\")[-1] == "Nathan Lee - Resume (1).pdf":
				self.r_trigger = True
			else:
				self.r_trigger = 

			if event.src_path.split("\\")[-1] == "Nathan Lee - Resume_CV (1).pdf":
				self.rc_trigger = True
			else:
				self.rc_trigger = False


folder_to_track = 'C:\\Users\\abcaa\\Downloads'
event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
	while True:
		time.sleep(10)
		if event_handler.c_trigger:
			if os.path.isfile(folder_to_track + "\\Cover Letter (Nathan Lee) (1).pdf"):
				os.remove(folder_to_track + "\\Cover Letter (Nathan Lee).pdf")
				os.rename(folder_to_track + "\\Cover Letter (Nathan Lee) (1).pdf",
								 folder_to_track + "\\Cover Letter (Nathan Lee).pdf")
				event_handler.c_trigger = False

		if event_handler.r_trigger:
			if os.path.isfile(folder_to_track + "\\Nathan Lee - Resume (1).pdf"):
				os.remove(folder_to_track + "\\Nathan Lee - Resume.pdf")
				os.rename(folder_to_track + "\\Nathan Lee - Resume (1).pdf",
								 folder_to_track + "\\Nathan Lee - Resume.pdf")
				event_handler.r_trigger = False

		if event_handler.rc_trigger:
			if os.path.isfile(folder_to_track + "\\Nathan Lee - Resume_CV (1).pdf"):
				os.remove(folder_to_track + "\\Nathan Lee - Resume_CV.pdf")
				os.rename(folder_to_track + "\\Nathan Lee - Resume_CV (1).pdf",
								 folder_to_track + "\\Nathan Lee - Resume_CV.pdf")
				event_handler.rc_trigger = False

except KeyboardInterrupt:
	observer.stop()

observer.join()