def reverse_for_loop(s):
    sl = " "
    for c in s:
        sl = c + sl
    return sl

input_str = "INE-KMUTNB"
if __name__ == "__main__":
    print('Reverse String using for loob =',reverse_for_loop(input_str))