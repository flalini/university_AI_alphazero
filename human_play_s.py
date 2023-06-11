# ====================
# 사람과 AI의 대전
# ====================

# 패키지 임포트
from game import State
from pv_mcts import pv_mcts_action
from tensorflow.keras.models import load_model
from pathlib import Path

# 베스트 플레이어 모델 로드
model = load_model('./model/best.h5')


# 동작 확인
if __name__ == '__main__':
    # 상태 생성
    state = State()
    next_action = pv_mcts_action(model, 0.0)

    # 게임 종료 시까지 반복
    while True:
        print(state)
        print()
        # 게임 종료 시
        if state.is_done():
            if state.is_first_player() and state.is_lose():
                print("win")
            else:
                print("lose")
            break

        if state.is_first_player():
            action = next_action(state)
        else :
            actions = state.legal_actions()
            while True:
                p, v = input("위치와 사용할 피스:").split()
                action = (int(p) - 1) * 6 + int(v) - 1
                if action in actions :
                    break

        # 다음 상태 얻기
        state = state.next(action)

        # 문자열 표시

