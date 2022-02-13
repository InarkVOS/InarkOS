list = ['h', 'i']

def process(lst):
    for i in range(len(lst)):
        yield lst[i]

for ele in process(list):
    print(ele)