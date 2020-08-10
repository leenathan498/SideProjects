from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import time
import os.path
import os
import shutil
import eyed3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def metaData():
	print("Meta.........")
	global song,artist,album,added_file

	downloadsPath = "C:\\Users\\abcaa\\Downloads\\" + added_file
	file = eyed3.load(downloadsPath).tag
	
	if song != "":
		file.title = song

	if artist != "":
		file.artist = artist

	if album != "":
		file.album = album

	file.save()


def grab():
	global Master, UrlEntry , ArtistEntry, AlbumEntry, SongEntry, UrlEntryLabel, ArtistLabel, AlbumLabel, SongEntryLabel, SubmissionButton, progress
	
	url = UrlEntry.get()
	if url == "":
		print("Try Again")
		return
	global artist, album, song
	artist = ArtistEntry.get()	
	album = AlbumEntry.get()
	song = SongEntry.get()

	progress = Progressbar(Master, orient = HORIZONTAL,
		length = 100, mode = 'determinate')
	progress.grid()

	print("Grabbing..")

	progress['value'] = 20
	getmp3(url)
	progress['value'] = 70
	metaData()
	progress['value'] = 80
	move()


def move():
	global added_file,Master
	print("moving")
	downloadsPath = "C:\\Users\\abcaa\\Downloads\\" + added_file
	itunesPath = "C:\\Users\\abcaa\\Music\\iTunes\\iTunes Media\\Automatically Add to iTunes"
	shutil.move(downloadsPath, itunesPath)
	progress['value'] = 100
	progress.destroy()


def getmp3(url):

	global added_file, progress

	options = webdriver.chrome.options.Options()
	#options.add_argument("--headless")
	browser = webdriver.Chrome(options = options)
	browser.implicitly_wait(100)
	browser.get("https://ytmp3.cc/en13/")
	progress['value'] = 40
	elem = browser.find_element_by_id("input")
	elem.send_keys(url)
	elem.submit()
	browser.find_element_by_link_text("Download").click()
	print("downloading")
	progress['value'] = 50
	time.sleep(10)
	added_file = None
	for _, _, files in os.walk("C:\\Users\\abcaa\\Downloads"):
		for file in files:
			if file.endswith(".mp3"):
				added_file = file
				break

def close():
	global Master
	Master.destroy()
	quit()

def main():
	global Master
	Master = Tk()
	Master.protocol("WM_DELETE_WINDOW", close)
	while(True):
		setup()
		Master.mainloop()

def setup():
	global Master, UrlEntry , ArtistEntry, AlbumEntry, SongEntry, UrlEntryLabel, ArtistLabel, AlbumLabel, SongEntryLabel, SubmissionButton

	#URL ENTRY
	UrlEntryLabel = Label(Master,text="Enter Youtube URL :")
	UrlEntryLabel.grid(row = 0, column = 0)
	UrlEntry = Entry(Master)
	UrlEntry.grid(row = 0, column = 1)


	#SONG ENTRY
	SongEntryLabel = Label(Master,text="Enter Song :")
	SongEntryLabel.grid(row = 1, column = 0)
	SongEntry = Entry(Master)
	SongEntry.grid(row = 1, column = 1)	

	#ARTIST ENTRY
	ArtistLabel = Label(Master,text="Enter Artist :")
	ArtistLabel.grid(row = 2, column = 0)
	ArtistEntry = Entry(Master)
	ArtistEntry.grid(row = 2, column = 1)

	#ALBUM ENTRY
	AlbumLabel = Label(Master,text="Enter Album :")
	AlbumLabel.grid(row = 3, column = 0)
	AlbumEntry = Entry(Master)
	AlbumEntry.grid(row = 3, column = 1)

	#SUBMISSION
	SubmissionButton = Button(Master, text = "Submit", command = grab)
	SubmissionButton.grid(row  = 10, column = 10)




if __name__ == '__main__':
	main()
