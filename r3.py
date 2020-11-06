# Read 3.txt
# split a part of the string
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')	# 按空格將list分割后，發現第一個String是time/name連在一起的
	time = s[0][:5]
	name = s[0][5:]
	print(name)
