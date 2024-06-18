from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(f"data com máscara pt-br{data_hora_atual.strftime(mascara_ptbr)}")

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(f'data convertida: {data_convertida}')
print(f'Tipo da data convertida: {type(data_convertida)}')