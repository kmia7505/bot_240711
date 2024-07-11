# 밀키트!를 떠올려 봅시다
#1.주가정보를 크롤링하는 기능 -> s10
#2.텔레그램 메시지 전송 기능 -> s11
import s10_getStockPrice as getStockPrice
import s11_telegram_first as telegram

stocks = getStockPrice.setPrice(getStockPrice.stocks)
print(stocks)

text_lst = []
for _key, _value in stocks.items():
    _price = _value['price']
    text_lst.append(f'{_key} 현재가: {_price}')
# print(text_lst)
_text4tele = '\n'.join(text_lst)

telegram.tele(telegram.MY_TOKEN, telegram.myChatId, _text4tele)