# read from input.txt and generate output.txt

def read_file(filename):
	lines = []
	# utf-8-sig: turn the beginning of the output from '\ufeffAllen\n'
	# to 'Allen\n', remove the default '\ufeff' in the .txt file
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())	# get rid of all '\n' in the output
	return lines

def convert(lines):
	new = []
	person = None			# 防止程序因爲第一次執行時沒有讀取到人名，person未能declared而down掉
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:			# if person is not None(has been declared)
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input_Eng.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
