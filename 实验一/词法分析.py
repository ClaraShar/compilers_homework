import re

seed_code = {"begin":1, "if":2, "then":3, "while":4, "do":5, "end":6, "+":13, "-":14, "*":15, "/":16, ":":17, ":=":18, "<":20, "<>":21, "<=":22, ">":23, ">=":24, "=":25, ";":26, "(":27, ")":28, "#":0}


def main():
	f = open("/Users/clara/Documents/学习/大三上/编译原理/input.txt", "r", encoding="utf-8")
	temp = f.read()
	f.close()
	input = temp.split(" ")
	pattern_identifier = r'[a-zA-Z]\w*'
	pattern_digit = r'\d+'
	for each_word in input:
		if each_word in seed_code:
			print("("+str(seed_code[each_word])+","+each_word+")")
		elif re.match(pattern_identifier,each_word) is not None:
			print("("+str(10)+","+each_word+")")
		elif re.match(pattern_digit,each_word) is not None:
			print("("+str(11)+","+each_word+")")
		else:
			print("error!")


if __name__ == '__main__':
	main()