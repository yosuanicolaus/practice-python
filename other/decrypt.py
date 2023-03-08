def decrypt(word):
    second_step_prev = 1
    decryption = ""

    for i in range(len(word)):
        enc_asc = ord(word[i]) - second_step_prev

        while enc_asc < ord("a"):
            enc_asc += 26

        decryption += chr(enc_asc)
        second_step_prev += enc_asc

    return decryption


def encrypt(word):
    values = []
    for ch in word:
        values.append(ord(ch))

    # add 1 to first letter
    values[0] += 1

    # add value from previous letter
    for i in range(1, len(values)):
        values[i] += values[i - 1]

    # substract 26 from every letter until in ascii range
    for i in range(len(values)):
        values[i] = (values[i] - 97) % 26 + 97

    # convert ascii value to word
    ans = ""
    for num in values:
        ans += chr(num)

    return ans


print(decrypt("dnotq"))
print(decrypt("flgxswdliefy"))
