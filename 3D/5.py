def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return "".join(temp_list)
input_str = "INE-KMUTNB"
if __name__ == "__main__":
    print('Reverse String using for loob =',reverse_list(input_str))