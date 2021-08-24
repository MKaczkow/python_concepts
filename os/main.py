import os
from datetime import datetime


def main():
	# print(dir(os))
	# print(os.getcwd())

	# change directory and see if it works...
	os.chdir('..')
	# print(os.getcwd())
	os.chdir('os')
	# print(os.getcwd())

	# make dirs recursively
	os.makedirs('test')
	# print(os.listdir())

	# rename test directory
	os.rename('test', 'renamed_test')
	# print(os.listdir())

	# remove dirs NON-recursively (safer)
	os.rmdir('renamed_test')
	# print(os.listdir())

	# get file info
	print(os.stat('threading_example.py'))
	last_mod_time = os.stat('threading_example.py').st_mtime
	print(datetime.fromtimestamp(last_mod_time))

	# traverse directory tree - walk - generator
	for dirpath, dirnames, filenames in os.walk(os.getcwd()):
		print(f"Current path: {dirpath}")
		print(f"Directories: {dirnames}")
		print(f"Files: {filenames}")
		print()

	# accessing enviroment variables
	print(os.environ.get("HOME"))
	

if __name__ == "__main__":
	main()
