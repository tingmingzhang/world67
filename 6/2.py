import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
alpha = ['i']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
suffix = ""
flag=0
for alpha3 in alphabets:
	for alpha4 in alphabets:
		for alpha5 in alphabets:
			for alpha6 in alphabets:
				for number7 in numbers:
					for number8 in numbers:
						name = "62"
						suffix = name+alpha3+alpha4+alpha5+alpha6+number7+number8
						compare = name + "aaaa00"
						if(suffix==compare):
							flag=1;
						if flag==1:
							url="https://m.llspace.com/v/"+suffix;
							r=requests.get(url)
							demo=r.text
							h = etree.HTML(demo)
							
							name_coming = name + "coming.txt"
							f_coming=open(name_coming,'a',encoding='utf-8')
							f_coming.write(suffix+'\n')
							f_coming.close()
							
							post_name = h.xpath('//span[contains(@class,"l-user-name")]//text()')
							if post_name:
								post_title = h.xpath('//h1[contains(@class,"l-title")]//text()')
								post_text = h.xpath('//div[contains(@class,"l-text")]//text()')
								post_date = h.xpath('//span[contains(@class,"l-date")]//text()')
								
								name_success = name + "success.txt"
								f_success=open(name_success,'a',encoding='utf-8')
								f_success.write(suffix+'\n')
								f_success.close()
								
								name_file = name + ".txt"
								f=open(name_file,'a',encoding='utf-8')
								f.write(suffix+'\n')
								f.write(json.dumps(post_title,ensure_ascii=False) + '\n') #必须格式化数据
								f.write(json.dumps(post_text,ensure_ascii=False) + '\n')
								f.write(json.dumps(post_name,ensure_ascii=False) + '\n')
								f.write(json.dumps(post_date,ensure_ascii=False) + '\n')
								f.write('\n')
								f.write('\n')
								f.close();
							
	

#print(post_title)
#print(post_text)
#print(post_name)
#print(post_date)
#print("\n")
