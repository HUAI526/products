#讀取檔案
products= []
with open('products.csv', 'r', encoding='utf-8') as f:
	#讀取檔案也要用寫出的編碼utf8
	for line in f:
		if '商品,價格' in line:
			continue #如果遇到“商品價格”就跳到下一個回合
			#但不會跳出迴圈，break是會直接跳出迴圈結束
		name, price = line.strip().split(',')
		#name跟price要去除換行符號然後使用split切割
		#遇到逗號就切割，分成name, price
		products.append([name, price])


while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price)
	products.append([name, price])#在清單中加入小清單有名字跟價格
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w' , encoding='utf-8') as f:#寫入檔案存成csv檔並用編碼utf8寫
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
