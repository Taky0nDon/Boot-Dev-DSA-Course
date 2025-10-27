import json
def get_average(nums: list[int|float]) -> None|int|float:
    count = len(nums)
    if count == 0:
        return None
    s = 0.0
    for n in nums:
        s += n
    return s / count

if __name__ == '__main__':
    with open('average_tests.json') as json_file:
        tests = json.load(json_file)
    print(tests[0].keys())
    for t in tests:
        if "expectedError" in t.keys():
            continue
        res = get_average(t["input"])
        if res != t["expected"]:
            print(f'Running {t["name"]}')
            print(f'Result: {res}')
            print(f'Expected: {t["expected"]}')
            print('YOU HAVE FUCKED UP!')

