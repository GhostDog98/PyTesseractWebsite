import os.path
from os import path
import time
from time import sleep
"""
for pid in psutil.pids():
    a = psutil.Process(pid) # This is a safety measure, simply to detect if a specific proccess is running to avoid accidental read/write to memory
    if a.name() == "notepad.exe":
        print("notepad found, starting")
        import psutil 
"""
while True:
        while not path.exists("E:\wamp64\www\www\done.txt"): # While this file doesn't exist
            print("File not found")
            time.sleep(1.5) # Wait 0.5s as not to lag out the computer
        print("File Found, continuing!")


        import sys
        import ctypes
        import os # Import the "os" package
        import glob as g
        from datetime import datetime
        try:
            from PIL import Image
        except ImportError:
            import Image
        import pytesseract

        class FileCheck(Exception):
            pass

        WriteDir = 'E:\\wamp64\\www\\www\\proc'
        GetDir = 'E:\\wamp64\\www\\www\\uploads' # this is where the images are located, the double '\\' is to escape the escape char of a single '\'
        # the below little code snippet checks how many files are in a dir, credit to Bruno Bronosky
        Files = os.listdir(GetDir) # Array of files in the dir
        if len(Files) != 1 and len(Files) != 0: # If the amount isnt 1 or 0 (This would cause so many errors...)
            i = 0
            for file in Files: # For every file we have
                os.remove(GetDir + "\\" + Files[i]) # Remove the items specified in the list, appended to the dir
                i = i+1 # Iterate i
            with open("E:\wamp64\www\www\log.txt", a) as Logs: # Open the log file to add this has happened
                Logs.write("Files: " + str(Files) + "have been removed on " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n") # Print files that were removed and print the date as well
            print("An internal error has occered with ID 0x01, please contact the admin at ghostoverflow256@gmail.com if this issue persists") # This is so php can pick up the error and communicate it 
            raise FileCheck("An internal error has occered with ID 0x01, please contact the admin at ghostoverflow256@gmail.com if this issue persists") # Communicate that an error has happened to the user
        else: # if this directory has exactly 1 file in it
                #print("1 file found, processing")
                PictureInput = "Null"
                if g.glob(GetDir + "\\" + "*.jpg"):
                        PictureInput = g.glob(GetDir + "\\" + "*.jpg")[0]
                        print("Found .jpg")
                elif g.glob(GetDir + "\\" + "*.png"):
                        PictureInput = g.glob(GetDir + "\\" + "*.png")[0]
                        print("Found .png")
                elif g.glob(GetDir + "\\" + "*.jpeg"):
                        PictureInput = g.glob(GetDir + "\\" + "*.jpeg")[0]
                        print("Found .jpeg")
                else:
                    print("AAAAAAAAAAAAAAAAAAAAAAA")
            
            # Get name of image file in dir, IT IS VERY IMPORTANT THAT THIS IS ONLY 1 IMAGE
            # This is why i run the check above
            

                pdf = pytesseract.image_to_pdf_or_hocr(PictureInput, extension='pdf') # This is taken directly from the docs lol
                with open(WriteDir + '\\' + 'out.pdf', 'w+b') as f:
                        f.write(pdf) # pdf type is bytes by default 
                print("DONE")
                os.remove("E:\wamp64\www\www\done.txt") # Remove the done indicator file
                os.remove(PictureInput) # Remove the processed image
                with open("E:\wamp64\www\www\log.txt", 'a') as Logs: # Open the log file to add this has happened
                        Logs.write("PDF has been written on: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
                with open("E:\wamp64\www\www\PyDone.txt", "x") as file: # Make indicator file
                        file.close() 
                time.sleep(3)


            
