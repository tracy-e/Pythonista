import os
import zipfile


def main(files):
	if len(files) == 1:
		file = files[0]
		if zipfile.is_zipfile(file):
			return unzip(file)
	zip(files)


def zip(files):
	print('zip files: ', files)
	if len(files) == 1:
		zip_name = os.path.basename(files[0]) + '.zip'
	else:
		dirname = os.path.dirname(files[0])
		if dirname:
			zip_name = dirname + '/archive.zip'
		else:
			zip_name = 'archive.zip'
		
	zipped = zipfile.ZipFile(zip_name, 'w')
	for file in files:
		file_name = os.path.basename(file)
		zipped.write(file, file_name)
	zipped.close()
	print('Done')


def unzip(file):
	print('unzip file: ', file)
	path = get_unzip_path(file)
	zipped = zipfile.ZipFile(file, 'r')
	zipped.printdir()
	zipped.extractall(path)
	zipped.close()
	print('Done')


def get_unzip_path(zip_path):
	dirname = os.path.dirname(zip_path)
	zip_name = os.path.basename(zip_path)
	file_name = os.path.splitext(zip_name)[0]
	path = os.path.join(dirname, file_name)
	return path


if __name__ == '__main__':
	import sys
	files = sys.argv[1::]
	main(files)
