
'''
 Constructing the regex:
^ indicates beginning of line
 $ indicates end of line
 ( indicates start of a group
 ) indicates end of a group
 + indicates more than 1 groups
 * indicates matching more than, including, 0.
	 -- Example: boa*t will match bot, boaat, boaaat

 ? indicates 0 or 1 match.
   -- Example: boat? will match boat, or boa but no boatt

 | pipe indicates OR operator

References:
[1] https://docs.python.org/3/library/re.html 
[2] https://docs.python.org/3/howto/regex.html#regex-howto
[3] https://unicode.org/emoji/charts/full-emoji-list.html
[4] https://en.wikipedia.org/wiki/List_of_emoticons

'''
import re

if __name__ == '__main__':

	# can be replaced with input() 
	text = "This is a list of notable and commonly used emoticons, or textual portrayals of a writer's moods or facial expressions in the :form of icons B-)  Origin:-(ally, these =) icons consisted :-| of ASCII art  , and later, Shift JIS art and Unicode art   . In :-PPP recent times, graphical icons, both static and animated, have joined the traditional text-based emoticons; these are commonly known as emoji     -Source: Wikipedia"




	#regex = r"^(:[)(])+$"
	regex = r'(?::|B|8|;|=)(?:-)?(?:\(|\)|\||O|D|P|B)'
	# (?::|B|8|;|=) group indicates 0 or 1 occurences of emoticons which start with : or = or B or 8 or ;
	# (?::|;|=)? 0 or 1 matches of a group that has 0 or 1 - in the emoticon. Will reject :--P
	# (?:\(|\)|O|D|P|B) - uses \ for escape characters. Matches 0 or 1 occurences of (
	#        or ) or | or O or D or P or B. Will reject all Ps in :-PPP other than 1

	
	emoticonsToEmoji = {
			':‑)' : "\U0001F60A",
			':)'  : "\U0001F60A",
			':-]' : "\U0001F603",
			':]'  : "\U0001F603",
			'8-)' : "\U0001F600",
			'8)'  : "\U0001F600",
			':o)' : "\U0001F62F",
			':-O' : "\U0001F632",
			':-o' : "\U0001F632",
			':-(' : "\U0001F61F",
			':('  : "\U0001F61F",
			':c)' : "\U0001F641",
			':P'  : "\U0001F61B",
			':-P' : "\U0001F61B",
			':^)' : "\U0001F604",
			'=]'  : "\U0001F604",
			'=)'  : "\U0001F604",
			'B)'  : "\U0001F60E",
			'B-)' : "\U0001F60E" 
			}

	regexInText = (re.findall(regex, text))
	
	for i in regexInText:
		if i in emoticonsToEmoji:
			if i in text:
				text = text.replace(i, emoticonsToEmoji[i])
						
	print (text)		
	
