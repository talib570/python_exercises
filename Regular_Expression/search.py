import re

def main():
	fh = open('dummy.txt')
	for line in fh:
		match = re.search('(ing)', line)
		if match:
			print(match.group())


if __name__ == "__main__": main()
