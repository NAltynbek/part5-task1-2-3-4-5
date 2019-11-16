def isFunny(s):
    for i in range(1, len(s)):
        if abs(s[i] - s[i-1]) != abs(s[-i-1] - s[-i]): return False
    return True
    

if __name__ == "__main__":
    num_cases = int(input());
    for case in range(num_cases):
        s = [ord(c) for c in input()];
        if isFunny(s): print("Funny")
        else: print("Not Funny");
