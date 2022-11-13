param_values = []
coefficients = []
time = 1000
delta = 1
populations_count = 0


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def default_values(n):
    global populations_count, param_values, coefficients, time, delta
    populations_count = n
    param_values = [[0.0] * 3 for i in range(populations_count)]
    for i in range(populations_count):
        param_values[i][0] = 100 * (i + 1)
        param_values[i][1] = -0.01
        param_values[i][2] = i
    param_values[0][1] = 0.01
    print(param_values)
    coefficients = [[0.0] * populations_count for i in range(populations_count)]
    for i in range(populations_count):
        for j in range(i + 1, populations_count):
            coefficients[i][j] = -0.0001
            coefficients[j][i] = 0.0001
    time = 1000
    delta = 1


def set_params(buf, buf1, t, d):
    global param_values, coefficients, time, delta
    param_values = buf
    coefficients = buf1
    time = t
    delta = d
