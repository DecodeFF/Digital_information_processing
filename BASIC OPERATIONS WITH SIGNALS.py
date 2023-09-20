def scale_signal(signal, scale_factor):
    scaled_signal = [value * scale_factor for value in signal]
    return scaled_signal


def reverse_signal(signal):
    return list(reversed(signal))


def shift_signal(signal, shift_amount):
    shifted_signal = [0] * len(signal)
    for i in range(len(signal)):
        new_index = i + shift_amount
        if 0 <= new_index < len(signal):
            shifted_signal[new_index] = signal[i]
    return shifted_signal


def add_signals(signal1, signal2):
    result_signal = []
    min_length = min(len(signal1), len(signal2))
    for i in range(min_length):
        result_signal.append(signal1[i] + signal2[i])
    result_signal.extend(signal1[min_length:])
    result_signal.extend(signal2[min_length:])
    return result_signal


def multiply_signals(signal1, signal2):
    result_signal = []
    min_length = min(len(signal1), len(signal2))
    for i in range(min_length):
        result_signal.append(signal1[i] * signal2[i])
    result_signal.extend([0] * (len(signal1) - min_length))
    result_signal.extend([0] * (len(signal2) - min_length))
    return result_signal


def expand_signal(signal, expansion_factor):
    expanded_signal = []
    for i in range(len(signal)):
        new_index = i * expansion_factor
        expanded_signal.append(signal[i])
        if i < len(signal) - 1:
            for j in range(1, expansion_factor):
                expanded_signal.append(0)
    return expanded_signal



signalX = [4, 0, 8, 7, 0, 3, 7]
signalY = [4, 3, 9, 0, 8, 7]


scale_factor = 4
scaledX = scale_signal(signalX, scale_factor)


reversedX = reverse_signal(signalX)


shift_amount = 4
shiftedX = shift_signal(signalX, shift_amount)


expansion_factor = 4
expanded_signal = expand_signal(signalX, expansion_factor)


added_signals = add_signals(signalX, signalY)


multiplied_signals = multiply_signals(signalX, signalY)


print("Масштабування X:", scaledX)
print("Реверс X:", reversedX)
print("Зсув X:", shiftedX)
print("Розширення X:",expanded_signal)
print("Додавання:", added_signals)
print("Множення:", multiplied_signals)


