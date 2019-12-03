def reverse_str_join(s):
    sl = "".join(reversed(s))
    return sl
input_str = "INE-KMUTNB"
if __name__ == "__main__":
    print('Reverse String using for loob =',reverse_str_join(input_str))