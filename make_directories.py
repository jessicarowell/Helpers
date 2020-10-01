import os, shutil, argparse

# Take user inputs (filename keyword) and make directories for those files

def getDirNames(key):
    dirNames = []
    for f in os.listdir():
    	if key in f: 
        	fname = os.path.splitext(f)[0]
        	dirNames.append(fname)
    return(dirNames)

def moveFiles(key, dirList):
    for d in dirList:
    	if not os.path.isdir(os.path.join(os.getcwd(), d)):
    		try:
    			os.mkdir(os.path.join(os.getcwd(), d))
    		except OSError:
    			print("Creation of directory {} failed".format(d))
    		else:
    			print("Creation of directory {} successful".format(d))
    for f in os.listdir():
    	if key in f:
    		fname = os.path.splitext(f)[0]
    		dirname = os.path.join(os.getcwd(), fname)
    		if os.path.isdir(dirname):
	    		try:
	    			shutil.move(f, dirname)
	    		except OSError:
	    			print("Could not move {0} to {1}".format(f,dirname))
	    		else:
	    			print("Successfully moved {0} to {1}".format(f, dirname))
	    	else:
	    		print("{0} does not exist. Cannot move {1}".format(dirname,f))


def copyFiles(key, dirList):
    for d in dirList:
    	if not os.path.isdir(os.path.join(os.getcwd(), d)):
    		try:
    			os.mkdir(os.path.join(os.getcwd(), d))
    		except OSError:
    			print("Creation of directory {} failed".format(d))
    		else:
    			print("Creation of directory {} successful".format(d))
    for f in os.listdir():
    	if key in f:
    		fname = os.path.splitext(f)[0]
    		dirname = os.path.join(os.getcwd(), fname)
    		if os.path.isdir(dirname):
	    		try:
	    			shutil.copy(f, dirname)
	    		except OSError:
	    			print("Could not copy {0} to {1}".format(f,dirname))
	    		else:
	    			print("Successfully copied {0} to {1}".format(f, dirname))
	    	else:
	    		print("{0} does not exist. Cannot copy {1}".format(dirname,f))


parser = argparse.ArgumentParser(description = 'Organize a list of files, identified by a common keyword, into directories')
parser.add_argument('-k', '--keyword', required=True, help = 'A keyword that identifies all the files you want to organize into directories')
parser.add_argument('-m', '--move', required=False, action = "store_true", help = 'Use this flag to move the files into the new directories instead of copying them')

args = parser.parse_args()

if __name__ == '__main__':
	dirNames = getDirNames(args.keyword)
	print(*dirNames, sep = "\n")
	useDirs = raw_input("Do these directory names look correct? Y/N")  ## This doesn't work!
	if useDirs == Y:
		if args.move:
			print("Making directories and moving files to them")
			moveFiles(args.keyword, dirNames)
		else:
			print("Making directories and copying files to them")
			copyFiles(args.keyword, dirNames)
	else:
		print("Exiting without making directories or moving/copying files")
		sys.exit(1) 