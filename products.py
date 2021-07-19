## 記帳程式 ##

#i.讓使用者"重複"輸入商品(買過的東西); 講到重複就要想到迴圈,講到執行"不知幾次"就想到while; for適合用在"特定"次數
#ii.我要讓使用者也輸入"價格"該如何處理?清單怎麼又裝名字又裝價格?!
#方法一:一格商品一格價格,想法可以但實做不好;因為清單裡裝了2個"不同類"的東西,還要知道奇數格偶數格是什麼
#方法二:那一個清單全名稱,另個清單全價格,名稱價格分開存;也不好,同個商品分開存,要找兩次
#方法三:第一次見識"兩個維度"的清單,簡單來說就是:清單中還有清單.大清單中,還有很多小小的清單(火車廂中還有橫向小車廂)
#iii.二維清單創好了,我們來看怎麼存取

products = []  #i2.我們要用一個清單裝input的商品,創products清單
#[延伸3]  檔案"讀取" (為了讀要先,才寫在開頭)
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:  #跳過欄位名稱: 如果資料是"商品,價格(欄位名稱)"就跳到下一循環
			continue
		s = line.strip().split(',')  #去除換行記號+以逗點為分隔
		name = s[0]
		price = s[1]
		products.append([name, price])
print(products)

#[開始]
while True:
	name = input('請輸入商品名稱:')  #i1.使用者輸入商品名
	if name == 'q':  #i1-1.quit輸入迴圈
		break
	price = input('請輸入價格:')  #ii1.使用者輸入價格,會遇到問題,要用二維清單
	p = []  #ii1-2.建立小清單
	p.append(name)
	p.append(price)
	#上三行亦可寫成 p = [name, price]
	products.append(p)  #i2-1.input裝進"清單products"	#ii1-1.清單我不裝商品名name了,改裝小清單(二維)
print(products)
#products[0][0]  #練習存取二維清單: [第1個商品],[品名]

#[延伸1]為熟悉二維清單, 寫一for循環印出商品/價格
for p in products:
	print(p)   #印出車廂中的小清單[ramen, 220]
	print(p[0]) #印出車廂中的小清單,第1個(就是品名)
	print(p[0], '的價格是', p[1])

#[延伸2]檔案"寫入"+ 註解欄位
with open("products.csv", "w", encoding = 'utf-8') as f:	#as f(as file):當作f,易忘!有了這個我就可以用f來稱呼我打開的整個檔案了
										#沒products.txt沒關係,會自建;有該檔也沒關係,會覆寫(改存csv較方便)
	f.write('商品,價格\n')	##加寫欄位,但發現是亂碼(編碼問題),在上行加註以utf-8寫入
	for p in products:	#用for循環,一個個存取我們清單的商品
		f.write(p[0] + ',' + p[1] + '\n')	#"品名"併"價格"併"換行"
