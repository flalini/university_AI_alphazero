# ====================
# 학습 사이클 실행
# ====================

# 패키지 임포트
from dual_network import dual_network
from self_play import self_play
from train_network import train_network
from evaluate_network import evaluate_network
import gc

SP_SEP_COUNT = 10

# 듀얼 네트워크 생성
dual_network()

for i in range(1):
    print('Train', i, '====================')
    # 셀프 플레이 파트
    # 코랩에서 self_play 실행시 ram 용량이 꽉 차는 문제가 생겨
    # SP_SEP_COUNT 만큼 나눠서 (실행 -> history 저장) 을 반복
    for j in range(SP_SEP_COUNT):
        self_play()
        gc.collect()

    # 파라미터 변경 파트
    train_network()

    # 신규 파라미터 평가 파트
    evaluate_network()
