def reverse_while_loob(s):
    sl = " "
    length = len(s)-1
    while length >= 0:
        sl = sl+s[length]
        length = length-1
    return sl
input_str = "INE-KMUTNB"
if __name__ == "__main__":
    print('Reverse String using for loob =',reverse_while_loob(input_str))
