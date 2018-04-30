## Quotes
## Date: 17 Apr 2018
## Hridin. During Python Class

class QUOTES(object):
	## we should be passing in the quote for the parameter quote and the correct response.
	def __init__(self,quote,correct_answer):
		self.quote = quote
		self.correct_answer = correct_answer
		print self.quote
	
	def check_answer(self,user_response):
		if user_response.lower() == self.correct_answer.lower():
			print 'Good Job! You got it!'
		else:
			print 'Womp, Womp. Go Away!'

lincoln = QUOTES('Quote said by Lincoln', 'Lincoln')
washington = QUOTES('Quote said by washington', 'washington')
henry = QUOTES('Quote said by henry', 'henry')


lincoln.check_answer(raw_input('Who said the first quote ?:'))
washington.check_answer(raw_input('Who said the Second quote ?:'))
henry.check_answer(raw_input('Who said the third quote ?:'))



