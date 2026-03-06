import math

def length(A, B, R):
    x1, y1 = A
    x2, y2 = B
    
    dx, dy = x2 - x1, y2 - y1
    AB_len = math.hypot(dx, dy)
    
    num = abs(x2 * y1 - y2 * x1)
    dist = num / AB_len if AB_len > 0 else math.hypot(x1, y1)
    dot1 = (x2 - x1) * (-x1) + (y2 - y1) * (-y1)
    dot2 = (x1 - x2) * (-x2) + (y1 - y2) * (-y2)
    
    if dist >= R or dot1 <= 0 or dot2 <= 0:
        return AB_len 
    OA = math.hypot(x1, y1)
    OB = math.hypot(x2, y2)
    alphaA = math.acos(R / OA)
    alphaB = math.acos(R / OB)
    phi = abs(math.atan2(y2, x2) - math.atan2(y1, x1))
    if phi > math.pi:
        phi = 2 * math.pi - phi       
    gamma = phi - alphaA - alphaB  
    if gamma <= 0:
        return AB_len
        
    L = math.sqrt(OA**2 - R**2) + (R * gamma) + math.sqrt(OB**2 - R**2)  
    return L

try:
    R = float(input())
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    print(f"{length((x1, y1), (x2, y2), R):.10f}")
except EOFError:
    pass
