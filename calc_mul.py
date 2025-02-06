#!/usr/bin/python3

def calc(A,B):
        ai=str(A)
        bi=str(B)
        if not (ai.isdecimal() and bi.isdecimal()):
                return -1

        a = int(ai)
        b = int(bi)
        if not (1 <= a <= 999 and 1 <= b <= 999):
                return -1

        ans = a * b
        return ans


def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
