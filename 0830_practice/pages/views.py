
from django.shortcuts import render
import requests
import random

# Create your views here.
def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1' 
    # 당첨 정보 받아오기
    lotto = requests.get(url).json()

    # 당첨 번호 6개 가져오기
    lotto_nums = []
    lotto_bonus = lotto['bnusNo']
    for i in range(1, 7):
        lotto_nums.append(lotto[f'drwtNo{i}'])
    
    # 당첨 횟수 기록하기 위한 dicionary
    record = {'1등':0, '2등':0, '3등':0, '4등':0,'5등':0, '꽝':0}

    # 랜덤 로또 1000장 만들고 당첨번호와 비교하기
    for i in range(1000):
        my_nums = random.sample(range(1,46),6)

        match = 0
        for num in my_nums:
            if num in lotto_nums:
                match += 1
        
        if match == 6:
            record['1등'] += 1
        elif match == 5 and lotto_bonus in my_nums:
            record['2등'] += 1
        elif match == 5:
            record['3등'] += 1
        elif match == 4:
            record['4등'] += 1
        elif match == 3:
            record['5등'] += 1
        else:
            record['꽝'] += 1
        
    context = {
        'lotto_nums' : lotto_nums,
        'lotto_bonus' : lotto_bonus,
        'match' : match, 
    }

    return render(request, 'lotto.html', context)