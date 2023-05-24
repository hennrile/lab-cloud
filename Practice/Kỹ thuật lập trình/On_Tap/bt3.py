user_input = input("Nhập giá trị: ")

try:
    float_input = float(user_input)

    if float_input.is_integer():
        int_input = int(float_input)
        if int_input > 0:
            print("Đây là một số nguyên dương.")
        elif int_input < 0:
            print("Đây là một số nguyên âm.")
        else:
            print("Đây là số 0.")
    else:
        print("Đây là một số thực.")

except ValueError:
    print("Đây không phải là một số.")