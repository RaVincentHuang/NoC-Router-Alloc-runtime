pre_dalays = [0.5241, 0.3325, 0.4552, 0.6621, 0.7422, 0.3423]
now_dalays = [0.3515, 0.4525, 0.4522, 0.5661, 0.7241, 0.2521]

def get_delays(num, opt):
    if opt:
        return now_dalays[num]
    else:
        return pre_dalays[num]
