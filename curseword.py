import urllib
def read():
	text=open("C:\Users\Rahul\ITP\pyth\curse\curse.txt")
	content=text.read()
	#print(content)
	text.close()
	check(content)

def check(content):
	connect=urllib.urlopen("http://www.wdylike.appspot.com/?q="+content)
	output=connect.read()
	connect.close()
	if "true" in output:
		print "Curse Word in your file"
	elif "false" in output:
		print "Your document is free of curse words ! :)"
	else:
		print "your file is not supported :("


read()