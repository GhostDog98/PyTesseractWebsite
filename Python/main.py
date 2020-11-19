import os.path
from os import path
import time
from time import sleep
""" Depricated Section, to be done in the future, keeping it here as a reminder
for pid in psutil.pids():
    a = psutil.Process(pid) # This is a safety measure, simply to detect if a specific proccess is running to avoid accidental read/write to memory
    if a.name() == "notepad.exe":
        print("notepad found, starting")
        import psutil 
"""
while True: # While true, meaning constantly run.
        while not path.exists("E:\wamp64\www\www\done.txt"): # While this file doesn't exist
            print("File not found")
            time.sleep(0.5) # Wait 0.5s as not to lag out the computer
        print("File Found, continuing!")
        
        import sys
        import ctypes
        import os # Import the "os" package
        import glob as g # Importing glob with the alias g
        from datetime import datetime # Using datetime to create logs
        try:
            from PIL import Image # Try to import PIL 
                                  # This is the main bit where i try to import my main
                                  # OCR engine, pytesseract.
        except ImportError: # In the case i get an import error i.e. the lib isn't found
            import Image # In this case import a dependency if it hasn't been opened for any
                         # reason
        import pytesseract # Import my OCR

        class FileCheck(Exception): #In the case i get this exception, simply pass
            pass

        WriteDir = 'E:\\wamp64\\www\\www\\proc' # This is where i will upload the finished pdf
        GetDir = 'E:\\wamp64\\www\\www\\uploads' # this is where the images are located, the double '\\' is to escape the escape char of a single '\'
        # the below little code snippet checks how many files are in a dir, credit to Bruno Bronosky
        Files = os.listdir(GetDir) # Array of files in the dir
        if len(Files) != 1 and len(Files) != 0: # If the amount isnt 1 or 0 (This would cause so many errors...)
            i = 0
            for file in Files: # For every file we have
                os.remove(GetDir + "\\" + Files[i]) # Remove the items specified in the list, appended to the dir
                i = i+1 # Iterate i
            #with open("E:\wamp64\www\www\log.txt", a) as Logs: # Open the log file to add this has happened
              #  Logs.write("Files: " + str(Files)  + "have been removed on " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n") # Print files that were removed and print the date as well
            print("An internal error has occered with ID 0x01, please contact the admin at ghostoverflow256@gmail.com if this issue persists") # This is so php can pick up the error and communicate it 
            raise FileCheck("An internal error has occered with ID 0x01, please contact the admin at ghostoverflow256@gmail.com if this issue persists") # Communicate that an error has happened to the user
        else: # if this directory has exactly 1 file in it
                PictureInput = "Null"
                if g.glob(GetDir + "\\" + "*.jpg"): # If the file exists
                # You'll notice here that i don't use sys.exists, this is due to the fact
                # That it takes the input as a raw string, meaning wildcards don't work.
                        PictureInput = g.glob(GetDir + "\\" + "*.jpg")[0] # Change the var
                        # Here i point to object [0], this is due to the fact that glob 
                        # for some godforsaken reason stores the result in an array
                        # even if i've only got 1 result!
                        print("Found .jpg")
                elif g.glob(GetDir + "\\" + "*.png"):
                        PictureInput = g.glob(GetDir + "\\" + "*.png")[0]
                        print("Found .png")
                elif g.glob(GetDir + "\\" + "*.jpeg"):
                        PictureInput = g.glob(GetDir + "\\" + "*.jpeg")[0]
                        print("Found .jpeg")
                else:
                    print("AAAAAAAAAAAAAAAAAAAAAAA")
            
            

                pdf = pytesseract.image_to_pdf_or_hocr(PictureInput, extension='pdf') # This is taken directly from the docs lol
                with open(WriteDir + '\\' + 'out.pdf', 'w+b') as f:
                        f.write(pdf) # pdf type is bytes by default 
                print("DONE")
                os.remove("E:\wamp64\www\www\done.txt") # Remove the done indicator file
                os.remove(PictureInput) # Remove the processed image
            #with open("E:\wamp64\www\www\log.txt", 'a') as Logs: # Open the log file to add this has happened
            #    Logs.write("PDF has been written on: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
                time.sleep(3) # If we have reached here, then we must have finished, wait
                # ~3 seconds to make sure the memory is clear i dont have any random memory
                # leaks
