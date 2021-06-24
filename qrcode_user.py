import pyzbar.pyzbar as pyzbar
import cv2
import sqlite3 as sq
import pandas as pd
import numpy as np
import datetime

'''사용자가 스마트폰이나 키오스크를 통해 qr코드를 찍었을때 사용되는 프로그램'''

# Database part
# DB 연결
conn = sq.connect('C:\sql_output\example.db')
cur = conn.cursor()

cap = cv2.VideoCapture(0)

i = 0
while(cap.isOpened()):
  ret, img = cap.read()

  if not ret:
    continue

  # 카메라로 찍은 이미지
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # gray로 변환한 이미지 decode
  decoded = pyzbar.decode(gray)

  for d in decoded:
    # 이미지에서의 좌표 계산
    x, y, w, h = d.rect

    # 좌표의 데이터 utf-8 형식으로 변환
    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    # qr코드에 바운딩박스 치기
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # qr코드의 데이터 텍스트화 
    text = '%s (%s)' % (barcode_data, barcode_type)
    
    # DB에서 수하물 정보 찾아내기
    cur.execute('SELECT * from Luggage_Database where fligt_id=? and luggage_num=?', (text[:6], text[6:]))
    row = cur.fetchall()
    if row == []:
      print("Your Luggage is already picked up")
    else:
      print(row[0])
      
  cv2.imshow('cam', img)

  key = cv2.waitKey(1)
  # ESC 누르면 종료
  if key == 27:
    cv2.destroyWindow('cam')
    break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
