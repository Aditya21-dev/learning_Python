# Q2. (File Handling + Binary Mode + seek/tell)
# Problem:
    # Binary file me data likho, cursor move karo, position print karo.

with open("data.bin", "wb+") as f:
    f.write(b"PythonFRIDAY")
    print(f.tell())     # cursor position
    f.seek(0)
    print(f.read())
