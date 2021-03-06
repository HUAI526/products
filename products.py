#載入作業系統
import os

#讀取檔案
def read_file(filename):
	products= []
	with open(filename, 'r', encoding='utf-8') as f:
	#讀取檔案也要用寫出的編碼utf8
		for line in f:
			if '商品,價格' in line:
				continue #如果遇到“商品價格”就跳到下一個回合
				#但不會跳出迴圈，break是會直接跳出迴圈結束
			name, price = line.strip().split(',')
			#name跟price要去除換行符號然後使用split切割
			#遇到逗號就切割，分成name, price
			products.append([name, price])
	return products


#讓使用者輸入購買產品和金額
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		products.append([name, price])#在清單中加入小清單有名字跟價格
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w' , encoding='utf-8') as f:#寫入檔案存成csv檔並用編碼utf8寫
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		#從os模組裡面選用isfile模組檢查檔案，不用硬背要使用再去搜尋功能就好
		print('yes')
		products = read_file(filename)
	else:
		print('no')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()
