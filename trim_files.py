# Remove comments from data files
import os

def trim_file(file, directory):
	with open(directory+'/'+file, "r") as infile, open(directory+'/'+file[:-4]+'_new.txt','w') as outfile:
		f_content = infile.read()
		f_content = f_content[f_content.find(' 0>  Page ='):]
		f_content = f_content[:f_content.find('Done')]
		outfile.write(f_content)
		os.remove(directory+'/'+file)


trim_file('Chip1_Block25_RandomData_WithShift_ReadRetry_SetFeature_0.txt','chip1')
def trim_all_files():
	for i in range(0,5):
		directory = 'chip'+str(i)
		for file in os.listdir(directory):
			print(directory, file)
			trim_file(file, directory)

#trim_all_files()
