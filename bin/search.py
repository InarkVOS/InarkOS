try:
    import os
    import sys
except ImportError as e:
    print("Error: Some modules could not be imported from stdlib('sys' and 'os')")

print(sys.argv[1])
keyword = sys.argv[1]
path = " ".join(sys.argv[2:])

filesMatched = 0
def search_files(keyword, path):
    filesFound = filesMatched
    for root, dirs, files in os.walk(path): #
        for file in files:
            if keyword in file:
                filesFound += 1
                print(" "+root+'\\'+str(file)+"\n")
                if filesFound == 0:
                    print("No matching files in the given directory! Try another directory!")
    print(f"No. of files matched: {filesFound}")

try:
    search_files(keyword, path)
except FileNotFoundError as e:
    print("Error: FileNotFoundError occured! Make sure you entered the correct path and entered it correctly.")
except Exception as e:
    print(f"Error: Some Error occured! \nDetails: {e}")