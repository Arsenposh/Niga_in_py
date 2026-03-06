import json

def find_diff(obj1, obj2, path=''):
    diffs = []
    keys = sorted(set(obj1) | set(obj2))
    
    for key in keys:
        curr_path = f"{path}.{key}" if path else key
        val1 = obj1.get(key, '<missing>')
        val2 = obj2.get(key, '<missing>')
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            diffs.extend(find_diff(val1, val2, curr_path))
        elif val1 != val2:
            v1_str = json.dumps(val1, separators=(',', ':')) if val1 != '<missing>' else val1
            v2_str = json.dumps(val2, separators=(',', ':')) if val2 != '<missing>' else val2
            diffs.append(f"{curr_path} : {v1_str} -> {v2_str}")
            
    return diffs

o1 = json.loads(input())
o2 = json.loads(input())
result = find_diff(o1, o2)
print('\n'.join(result) if result else 'No differences')
