import math

def rgb_to_temperature(rgb):
    # RGB 값을 0과 1 사이로 정규화합니다.
    r = rgb[0] / 255.0
    g = rgb[1] / 255.0
    b = rgb[2] / 255.0

    # sRGB를 선형 RGB로 변환합니다.
    r = inverse_gamma_correction(r)
    g = inverse_gamma_correction(g)
    b = inverse_gamma_correction(b)

    # 선형 RGB를 CIE XYZ로 변환합니다.
    X, Y, Z = linear_rgb_to_XYZ(r, g, b)

    # CIE XYZ를 색온도로 변환합니다.
    temperature = XYZ_to_temperature(X, Y, Z)
    return temperature

def inverse_gamma_correction(channel):
    if channel <= 0.04045:
        return channel / 12.92
    else:
        return math.pow((channel + 0.055) / 1.055, 2.4)

def linear_rgb_to_XYZ(r, g, b):
    # sRGB to XYZ 변환 행렬
    M = [[0.4124564, 0.3575761, 0.1804375],
         [0.2126729, 0.7151522, 0.0721750],
         [0.0193339, 0.1191920, 0.9503041]]

    X = M[0][0] * r + M[0][1] * g + M[0][2] * b
    Y = M[1][0] * r + M[1][1] * g + M[1][2] * b
    Z = M[2][0] * r + M[2][1] * g + M[2][2] * b

    return X, Y, Z

def XYZ_to_temperature(X, Y, Z):
    # CIE XYZ to 색온도 변환
    x = X / (X+Y+Z)
    y = Y / (X+Y+Z)
    n = (x - 0.3320) / (y - 0.1858)
    temperature = -449 * math.pow(n, 3) + 3525 * math.pow(n, 2) - 6823.3 * n + 5520.33
    print("x,y : ",x,y) 
    return temperature

# RGB 값 입력
rgb = [2000, 2000, 2500]

# 색온도로 변환
temperature = rgb_to_temperature(rgb)
print("Temperature: ", temperature)
