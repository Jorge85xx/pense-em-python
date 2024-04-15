""". Suponha que o preço de capa de um livro seja
R$ 24,95, mas as livrarias recebem um desconto de
40%. O transporte custa R$  3,00 para o primeiro
exemplar e 75 centavos para cada exemplar
adicional. Qual é o custo total de atacado para 60
cópias?"""

number_of_copies : int = 60
price_book_cover : float =  24.95 - (24.95*0.40) #without transporter and quantity
print(price_book_cover)
price_book_cover : float = (price_book_cover*number_of_copies) + (3 + (0.75 * (number_of_copies - 1)))#with transporter and quantity
print(f'{price_book_cover:.2f}')
