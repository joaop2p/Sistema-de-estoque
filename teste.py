# import base64
# from calendar import c
# import re
# # import mimetypes
from pathlib import Path
# # import flet as ft
import pymysql

photo = Path(r'C:\Users\joaop\Downloads\x.jpg')

with open(photo, 'rb') as f:
    blob: bytes = f.read()  # já é o BLOB em Python

# # print(f'Bytes lidos: {len(blob)}')

# # # Opcional: Base64 (para JSON/HTML/Flet)
# # b64 = base64.b64encode(blob).decode('ascii')
# # mime, _ = mimetypes.guess_type(photo.name)
# # mime = mime or 'application/octet-stream'
# # data_url = f'data:{mime};base64,{b64}'

# # # Armazene o BLOB com parâmetros (sem f-string)
query = "UPDATE clients SET photo=%s WHERE id=%s"
con = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='sys_inventory_db'
)
cur = con.cursor()
# res = cur.execute("SELECT photo FROM clients WHERE id=%s", (1,))
# result = cur.fetchone()
# a = result[0]
# print(a[:30])
cur.execute(query, (pymysql.Binary(blob), 5))  # ou apenas (blob, 1)
con.commit()
# # # Ex.: no Flet, usar em uma imagem:r em uma imagem:
# # # import flet as ft

# # # img = ft.Image(src_base64=b64)# img = ft.Image(src_base64=b64)

# import io
# from PIL import Image


# # with open(r"C:\Users\joaop\Downloads\clients-photo.bin", 'rb') as f:
# #     image_bytes: bytes = f.read()
# #     print(f'Bytes lidos do BIN: {len(image_bytes)}')

# image=Image.open(io.BytesIO(a))
# image.show()

