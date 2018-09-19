
from os import listdir, rename
from os.path import abspath, split, join,splitext
import sys
import glob

def main():
	tdir = abspath(sys.argv[1])
	paths = listdir(tdir)
	for path in paths:
		filepath, ext = splitext(path)
		head, filename = split(filepath)
		if (filename[-3:]=="(1)"):
			newpath = join(tdir,filename[:-4]+ext)
			print join(tdir,path)
			print newpath
			rename(join(tdir,path),newpath)

if __name__ == "__main__":
	main()
