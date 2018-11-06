import re

f = open("/Users/clara/Documents/学习/大三上/编译原理/实验二/input.txt", "r", encoding="utf-8")
temp = f.read()
f.close()
words = temp.split(" ")
it = iter(words)

pattern_identifier = r'[a-zA-Z]\w*' # 标识符正则
pattern_digit = r'\d+'
seed_code = {"begin":1, "if":2, "then":3, "while":4, "do":5, "end":6, "+":13, "-":14, "*":15, "/":16, ":":17, ":=":18, "<":20, "<>":21, "<=":22, ">":23, ">=":24, "=":25, ";":26, "(":27, ")":28, "#":0}


def scaner():
	word=next(it)
	return word


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
			exit()
	else:
		print("表达式错误!")
		exit()


def term(word):
	a=factor(word)#word=x,a=end
	while(seed_code[a]==15 or seed_code[a]==16):
		b=scaner()
		a=factor(b)#b=3,a=;
	return a


def expression(w):
	b=term(w)# w=a,b=+
	while(seed_code[b]==13 or seed_code[b]==14):
		a=scaner()
		b=term(a)# a=x,b=end
	return b


def statement(w):
	if re.match(pattern_identifier,w) is not None:
		c=scaner()
		if seed_code[c]==18:
			a=scaner()
			b=expression(a)# a=a,b=end
			return b
		else:
			print("赋值号错误!")
			exit()
	else:
		print("语句错误!")
		exit()


def sentence(word):
	w=statement(word)
	while(seed_code[w]==26):
		a=scaner()
		w=statement(a)# a=b,w=end
	return w


def main():
	word=next(it)
	if seed_code[word]==1:
		w=scaner()
		a=sentence(w)# w=a , a=end
		if seed_code[a]==6:
			b=scaner()
			if seed_code[b]==0:
				print("success!")
				exit()
			else:
				print("缺#错误!")
				exit()
		else:
			print("缺end	错误!")
			exit()
	else:
		print("begin错误")
		exit()


if __name__ == '__main__':
	main()