import re


pattern_identifier = r'[a-zA-Z]\w*' # 标识符正则
pattern_digit = r'\d+'
seed_code = {"begin":1, "if":2, "then":3, "while":4, "do":5, "end":6, "+":13, "-":14, "*":15, "/":16, ":":17, ":=":18, "<":20, "<>":21, "<=":22, ">":23, ">=":24, "=":25, ";":26, "(":27, ")":28, "#":0}



def factor(word):
	if re.match(pattern_identifier,word) is not None or re.match(pattern_digit,word) is not None: # 匹配成功
		a=scaner()
		return a
	elif seed_code[word]==27:
		b=scaner()
		expression(b)
		if seed_code[b]==28:
			next(li)
		else:
			print("')'错误!")
			kk=1
			exit()
	else:
		print("表达式错误!")
		kk=1
		exit()


def term(word):
	a=factor(word)
	while seed_code[a]==15 or 16:
		b=scaner()
		c=factor(b)	


def expression(w):
	term(w)
	while(seed_code[it]==13 or seed_code[it]==14):
		a=scaner()
		term(a)


def statement(w):
	if re.match(pattern_identifier,w) is not None:
		word=scaner()
		if seed_code[word]==18:
			a=scaner()
			expression(a)
		else:
			print("赋值号错误!")
			kk=1
			exit()
	else:
		print("语句错误!")
		kk=1
		exit()


def sentence(word):# ok
	statement(word)
	while(seed_code[it]==26):
		a=scaner()
		statement(a)


def main():
	f = open("/Users/clara/Documents/学习/大三上/编译原理/实验二/input.txt", "r", encoding="utf-8")
	temp = f.read()
	f.close()
	words = temp.split(" ")
	for each_word in word:
		



	if seed_code[word]==1:
		w=scaner()
		sentence(w)
		if seed_code[it]==6:
			w=scaner()
			if seed_code[w]==0 and kk==0:
				print("success!")
				exit()
			else:
				print("缺#错误!")
				exit()
		else:
			if kk!=1:
				print("缺end	错误!")
				kk=1
				exit()
	else:
		print("begin错误")
		kk=1
		exit()


if __name__ == '__main__':
	main()