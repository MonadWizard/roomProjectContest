import language_check
tool = language_check.LanguageTool('en-US')
text = input("enter text : ")
matches = tool.check(text)

len(matches)

language_check.correct(text, matches)