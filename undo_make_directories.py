import os, shutil, argparse

def getDirs(key):
	listDirs = next(os.walk('.'))[1]
	dirNames = []
	for d in listDirs:
		if key in d:
			dirNames.append(d)
	return(dirNames)

def moveFilesUp(dirList):
	for d in dirList:
		for f in os.listdir(d):
			if os.path.isfile(os.path.join(d, f)):
				try:
					shutil.move(os.path.join(d, f), os.getcwd())
				except OSError:
					print("Unable to move {0} from {1}".format(f, d))
				else:
					print("Successfully moved {}".format(f))

def deleteDirs(dirList):
	for d in dirList:
	try:
		os.rmdir(d)
	except OSError:
		print("Cannot delete {} because directory is not empty".format(d))
	else:
		print("Successfully deleted {}".format(d))

parser = argparse.ArgumentParser(description = 'Move a bunch of files (identified by keyword) out of directories and optionally delete the directories')
parser.add_argument('-k', '--keyword', required=True, help = 'A keyword that identifies all the files you want to move out of directories')
parser.add_argument('-d', '--delete', required=False, help = 'Use this flag to delete directories after removing files')

args = parser.parse_args()

if __name__ == '__main__':
	dirNames = getDirs(args.keyword)
	print(*dirNames, sep = "\n")
	rmDirs = raw_input("Do these directory names look correct? Y/N") ## This won't work. Copy solution from make_directories.py
	if rmDirs == Y:
		# move all files out of the directories in that list [input: dir list, output: nothing, files get moved]
		moveFilesUp(dirNames)

	if args.delete:
		deleteDirs(dirNames)
	else:
		print("Done moving files. Directories not removed.")
