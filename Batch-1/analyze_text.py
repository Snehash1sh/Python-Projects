def analyze_text(text):
    cnt = 0
    dig_cnt = 0
    sp_cnt = 0
    spe_cnt = 0
    print("Text Analysis Report")
    if text == text [::-1]:
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")
    print("Total Characters: ",len(text))
    print("Words",len(text.split()))
    for i in text:
        if i in "aeiou":
            cnt = cnt + 1
        if i.isdigit():
            dig_cnt = dig_cnt + 1
        if i == " ":
            sp_cnt = sp_cnt + 1
        if i.isalnum():
            pass
        else:
            spe_cnt = spe_cnt + 1
    print("Vowels: ",cnt)
    print("Consonents: ",len(text) - cnt)
    print("Digits: ",dig_cnt)
    print("Spaces: ",sp_cnt)
    print("Special Characters: ",spe_cnt - sp_cnt)

    return []
analyze_text()
