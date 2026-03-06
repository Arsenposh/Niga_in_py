x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

px = x1 + y1 * (x2 - x1) / (y1 + y2)
py = 0.0
print(f"{px:.10f} {py:.10f}")