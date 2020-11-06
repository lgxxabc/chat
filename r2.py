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
	# Count how many words
	allen_word_count = 0
	viki_word_count = 0
	# Count how many pictures 
	allen_image_count = 0
	viki_image_count = 0
	# Count how many '圖片'
	allen_sticker_count = 0
	viki_sticker_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:		# from s[2] to s[end]
					allen_word_count += len(m)	# count the number of words
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:		# from s[2] to s[end]
					viki_word_count += len(m)
		# print(s)
	print('Allen said', allen_word_count, 'words, and sent', allen_sticker_count, 'pictures')
	print('Allen sent', allen_image_count, 'images')
	print('Viki said', viki_word_count, 'words, and sent', viki_sticker_count, 'pictures')
	print('Viki sent', viki_image_count, 'images')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()
