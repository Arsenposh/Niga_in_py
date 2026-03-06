import json

def apply_patch(source, patch):
    result = dict(source)
    for key, value in patch.items():
        if value is None:
            result.pop(key, None)
        elif isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = apply_patch(result[key], value)
        else:
            result[key] = value
    return result

source = json.loads(input())
patch = json.loads(input())

result = apply_patch(source, patch)
print(json.dumps(result, sort_keys=True, separators=(',', ':')))

