# Using map and lambda function, compute the Fahrenheit with Celsius input:

# Hints: the Fahrenheit function
def fahrenheit(T):
	return ((float(9)/5)*T + 32)

Cs = (36.5, 37, 37.5, 38, 39)
Fs = map(lambda T: float(9)/5*T + 32, Cs)
print(list(Fs))

# Change the for-loop to be 1-line list comprehension code

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
#word_lengths = []
#for word in words:
#	if word != "the":
#        word_lengths.append(len(word))
word_lengths = [len(word) for word in words if word != 'the']
print(words)
print(word_lengths)