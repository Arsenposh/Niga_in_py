import sys

def solve():
    g = 0  
    n = 0  
    try:
        line = sys.stdin.readline()
        if not line:
            return
        count = int(line.strip())
    except ValueError:
        return

    for _ in range(count):
        command = sys.stdin.readline().split()
        if not command:
            continue
        
        scope = command[0]
        value = int(command[1])

        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value
        elif scope == "local":
            pass

    print(f"{g} {n}")

if __name__ == "__main__":
    solve()
