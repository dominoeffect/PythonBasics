import re
def multiply_divide(s):
    if '*' in s:
        ret = float(s.split('*')[0])*float(s.split('*')[1])
    elif '/' in s:
        ret = float(s.split('/')[0])/float(s.split('/')[1])
    return ret

def cal_mul_div(s):
    if '*' not in s and '/' not in s:
        return s
    else:
        k = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', s).group()
        s = s.replace(k, '+' + str(multiply_divide(k))) if len(re.findall(r'-', k)) == 2 else s.replace(k, str(
            multiply_divide(k)))
        return cal_mul_div(s)

def cal_plu_min(s):
    l = re.findall('([\d\.]+|-|\+)',s)
    if l[0] == '-':
        l[0] = l[0] + l[1]
        del l[1]
    sum = float(l[0])
    for i in range(1, len(l), 2):
        if l[i] == '+' and l[i + 1] != '-':
            sum += float(l[i + 1])
        elif l[i] == '+' and l[i + 1] == '-':
            sum -= float(l[i + 2])
        elif l[i] == '-' and l[i + 1] == '-':
            sum += float(l[i + 2])
        elif l[i] == '-' and l[i + 1] != '-':
            sum -= float(l[i + 1])
    return sum

def basic_operation(s):
    s = s.replace('%', '/100')
    return cal_plu_min(cal_mul_div(s))

print(basic_operation('6/3+3*2+10%'))

