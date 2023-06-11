# university_AI_alphazero   
python, tensorflow 기반   
알파제로를 분석하며 배우는 인공지능   
[책](https://jpub.tistory.com/996)과 [깃허브](https://github.com/Jpub/AlphaZero)를 보고 내가 원하는 간단한 보드게임 인공지능 만들어보기   
여기서 사용해본 게임의 룰은 이전에 [학교에서 유니티로 만들어본 게임](https://github.com/flalini/university_gameprogramming)을 이용했다.   
   
## 학습을 위한 구조   
### macro   
> 다른 여러 함수에 사용될 매크로 정의   
   
### dual_network   
> 알파제로의 핵심 모델 구성   
> 이 모델을 학습시키고 게임의 현 상황을 집어넣어 정책(수)과 가치(승률)를 출력   
> <img src="./image/스크린샷%202023-06-11%20오후%206.19.29.png" width="20%" height="20%">   
> <img src="./image/스크린샷%202023-06-11%20오후%206.19.03.png" width="33%" height="33%">   
   
### pv_mcts   
> 몬테카를로트리를 이용한 정책 선택 알고리즘   
> 주어진 모델을 이용해 가치를 판단하여 몬테카를로트리를 구성    
   
### self_play   
> best 모델을 이용하여 스스로 대전하여 히스토리(학습시킬 데이터) 생성   
   
### assemble_history   
> 코랩이나 로컬의 메모리 한계, 혹은 병렬 컴퓨팅으로 인해 history를 여럿 나눠서 생성할 때 사용   
> 정해진 수 만큼의 최신 history를 하나로 합쳐준다   
   
### train_network   
> 최신의 히스토리를 이용해서 model 학습   
> latest 모델을 저장한다   
   
### evaluate_network   
> best와 latest를 비교하여 best의 교체를 결정한다   
   
### train_cycle   
> best가 존재하지 않을 경우 dual_network를 통해 best를 만들어 두고 시작한다   
> 아래 사이클을 원하는 만큼 반복   
> > 특정 사이클마다 best를 따로 저장(이후 비교를 위해)   
> > self_play   
> > 필요하다면 assemvle_history   
> > train_network   
> > evaluate_network   
   
## 확인용 코드   
### evaluate_model   
> 만들어진 best 모델들의 평가   
> 여기서는 10사이클마다의 best를 비교해봄   
   
### human_play_*   
> 로컬에서 best 모델을 불러와 text mode로 실제 플레이   
> 게임 방식은 1에서 부터 6까지의 가치를 가진 말을 이용한 틱택토   
> 높은 가치의 말은 낮은 가치의 말을 잡고 그 자리에 둘 수 있음   
> 1 2 3   
> 4 5 6   
> 7 8 9   
> 위 포지션에 맞게 포지션을 입력하고 한칸을 띄고 가치를 적으면 해당 위치에 해당 가치의 말이 놓인다   
> ex)8 4   
> 이렇게 두면 아래 중앙에 4짜리 말이 놓임   
> 후수의 말은 구분을 위해 F 부터 A까지의 말을 둠   
> f 파일은 플레이어가 선수 s 파일은 플레이어가 후수   
