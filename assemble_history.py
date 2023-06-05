# ====================
# 나눠서 저장한 history 하나로 합치기
# ====================

# 패키지 임포트
from pathlib import Path
import shutil
from macro import SP_SEP_COUNT

def assemble_history():
    history_path = sorted(Path('./data').glob('*.history'))
    
    for i in range(2, SP_SEP_COUNT + 1)
    
    with history_path.open(mode='rb') as f:
        return pickle.load(f)