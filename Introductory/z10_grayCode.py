def grayCode(n: int):
    prev = ["0","1"]
    for i in range(1,n):
        fir_half=["0"+i for i in prev]
        sec_half=["1"+i for i in prev[::-1]]
        prev=fir_half+sec_half
    for i in prev:
        print(i)

n=int(input())
grayCode(n)