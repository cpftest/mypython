from urllib.request import urlopen
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
	"""docstring for MyHTMLParser"""
	vurl=''

	def handle_starttag(self, tag,attrs):
		#print('start:',tag)
		pass

	def handle_endtag(self,tag):
		pass
		#print('end tag',tag)

	def handle_data(self,data):
		if 'datas' in data:
			#print('handle_data:',data)
			mydata=data.split(';')

			# for sp in mydata:
			# 	print('-'*50)
			# 	print(sp)
			udata=mydata[0].split('\'')
			# print(mydata[0])
			# print('-'*100)
			#print(udata[1])
			tstr=udata[1].split('*')
			turl=''
			for st in tstr:#解密数据
				if len(st)>0:
					turl=turl+chr(int(st))

			self.vurl=turl.split('&')[0]

	def getVurl(self):
		
		return self.vurl


		

def myDown():
	#生成下载页面连接
	for i in range(202,399):
		tmpUrl='http://www.xxxx.com/video/12204-0-'+str(i)+'.html'
		print(tmpUrl)
		dfile=str(i)+'.m4a'

		# if i>189:
		# 	break

		with urlopen(tmpUrl) as response:
			fdata=''
			for line in response:
				line=line.decode('gb2312')
				fdata=fdata+line

			parser=MyHTMLParser()
			parser.feed(fdata)
			print('parser==',parser.getVurl())

			voteurl=parser.getVurl()
			with urlopen(voteurl) as response:
				# print(response.read())
				with open(dfile,'wb+') as f:
					f.write(response.read())
				print('down finish!!',dfile)



#函数入口
def main():
	myDown()

if __name__ == '__main__':
	main()
