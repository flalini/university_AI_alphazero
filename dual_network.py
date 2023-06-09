# ====================
# 듀얼 네트워크 생성
# ====================

# 패키지 임포트
from tensorflow.keras.layers import Activation, Add, BatchNormalization, Conv2D, Dense, GlobalAveragePooling2D, Input
from tensorflow.keras.models import Model
from tensorflow.keras.regularizers import l2
from tensorflow.keras import backend as K
from macro import DN_FILTERS, DN_RESIDUAL_NUM, DN_INPUT_SHAPE, DN_OUTPUT_SIZE
import os


# 컨볼루션 레이어 생성
def conv(filters):
    return Conv2D(filters, 3, padding='same', use_bias=False,
                  kernel_initializer='he_normal', kernel_regularizer=l2(0.0005))


# 레지듀얼 블록 생성
def residual_block():
    def f(x):
        sc = x
        x = conv(DN_FILTERS)(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = conv(DN_FILTERS)(x)
        x = BatchNormalization()(x)
        x = Add()([x, sc])
        x = Activation('relu')(x)
        return x

    return f


# 듀얼 네트워크 생성
def dual_network():
    # 모델 생성이 완료된 경우 처리하지 않음
    if os.path.exists('./model/best.h5'):
        return

    # 입력 레이어
    input = Input(shape=DN_INPUT_SHAPE)

    # 컨볼루션 레이어
    x = conv(DN_FILTERS)(input)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    # 레지듀얼 블록 x 16
    for i in range(DN_RESIDUAL_NUM):
        x = residual_block()(x)

    # 풀링 레이어
    x = GlobalAveragePooling2D()(x)

    # policy 출력
    p = Dense(DN_OUTPUT_SIZE, kernel_regularizer=l2(0.0005),
              activation='softmax', name='pi')(x)

    # value 출력
    v = Dense(1, kernel_regularizer=l2(0.0005))(x)
    v = Activation('tanh', name='v')(v)

    # 모델 생성
    model = Model(inputs=input, outputs=[p, v])

    # 모델 저장
    os.makedirs('./model/', exist_ok=True)  # 폴더가 없는 경우 생성
    model.save('./model/best.h5')  # 베스트 플레이어 모델

    # 모델 피기
    K.clear_session()
    del model


# 동작 확인
if __name__ == '__main__':
    dual_network()
