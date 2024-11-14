def hanoi(n, source, target, auxiliary):
    if n == 1:
        return [f"Move disk 1 from rod {source} to rod {target}"]
    else:
        moves = hanoi(n - 1, source, auxiliary, target)
        moves.append(f"Move disk {n} from rod {source} to rod {target}")
        moves.extend(hanoi(n - 1, auxiliary, target, source))
        return moves

def solve_towers_of_hanoi(n):
    print("Output:", " ".join(hanoi(n, 'A', 'C', 'B')))


# Example
n = int(input("Input: "))
if n < 1 or n > 10:
    print("Number of disks must be between 1 and 10.")
else:
    solve_towers_of_hanoi(n)
