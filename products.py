products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])#在清單中加入小清單有名字跟價格
print(products)