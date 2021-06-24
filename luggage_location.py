# 팀 SIA 수하물 추적 시스템 및 수취대 위 위치 측정
# 수취대 위 수하물 정보에 대한 qr코드 스캔은 아두이노를 사용하여 스캔
# 제작자: 임호정 birds8277@gmail.com

import time
import math


# 인천공항 수하물 수취대 기준, 가로 길이가 15m 로 추정, 한바퀴 도는 데에 5분이라고 추정
# 모형 수취대의 가로 길이 = 0.5m, 너비 = 0.15m
# 모형 수취대로 한바퀴 도는 시간: 1분 = 60초

class Luggage:
    
    def __init__(self, info):
        self.info = info
        self.location = 0
        self.time = 0   #수취대에 처음 들어왔을 때에 시간은 0초
        
    def loop(self, scan_info):
        # 모형에서는 한바퀴를 돌리지 못하기 때문에 만든 부분, 실제 수취대에서는 필요없음
        if scan_info == self.info:
            self.time += 60
        elif scan_info == 0:
            return "Luggage is picked up"

    def __repr__(self):
        return '(' + self.info + ', ' + self.location + ')'
    
# end of class luggage

class StopWatch:
    
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        
    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        self.stop_time = time.time()
        return self.stop_time
    
    def get_elapsed(self):
        return self.stop_time - self.start_time
    
        
total_length = 50 #in cm
avg_speed = 5 # cm/s
sections = {'A' : 0, 'B': 10, 'C' : 20, 'D' : 30, 'E' : 40}

def calculate_distance(scan_info):  #수하물의 qr 코드 정보를 parameter로 받아야함
    
    time = StopWatch()
    l1 = Luggage(scan_info)
    
    


