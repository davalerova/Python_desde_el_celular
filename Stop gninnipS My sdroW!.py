def spin_words(sentence):
	res = ""
	ceros = sentence.count(" ")
	for pal in sentence.split(" "):
		if len(pal) >4:
			if ceros >= 0:
				res += " "
				ceros -=1
			res += pal[::-1]
		else:
			if ceros >= 0:
				res += " "
				ceros -=1
			res += pal
	return res
print(spin_words("Stop Spinning My Words!"))