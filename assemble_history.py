# ====================
# 나눠서 저장한 history 하나로 합치기
# ====================

# 패키지 임포트
from pathlib import Path
import shutil
from macro import SP_SEP_COUNT
from self_play import write_data
import numpy as np
import pickle

def assemble_history():
    history_path_list = sorted(Path('./data').glob('*.history'))

    with history_path_list[-1].open(mode = 'rb') as f:
        history = pickle.load(f)
        f.close()
    
    for i in range(2, SP_SEP_COUNT + 1):
        with history_path_list[-i].open(mode = 'rb') as f:
            history.extend(pickle.load(f))
            f.close()
    write_data(history)

# 동작 확인
if __name__ == '__main__':
    assemble_history()
