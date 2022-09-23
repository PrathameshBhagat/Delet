
stg=input("Enter string:")
stg_list=stg.split()
uq_words=set(stg_list)
for words in uq_words:
	print('Frequency of',words,':',stg_list.count(words))
