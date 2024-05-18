'''
WWW型栅栏密码
'''
def num(s, n):
    f = len(s) // (n - 1)
    g = len(s) % (n - 1)
    return f, g
def _list(s, n):
    x, y = num(s, n)
    if y == 0:
        c = [[] for i in range(x + 1)]
        lie = x
    else:
        c = [[] for i in range(x + 2)]
        lie = x + 1
    jk = 0
    if lie % 2 == 0:
        hk = n - y + 1
    else:
        hk = y
    for i in range(1, n + 1):
        for j in range(1, lie + 1):
            if i == 1:
                if j % 2 != 0:
                    c[j].append(s[jk])
                    jk += 1

            else:

                if lie % 2 == 0:
                    if y == 0:
                        if i != n:
                            c[j].append(s[jk])
                            jk += 1
                        if i == n:
                            if j % 2 == 0:
                                c[j].append(s[jk])
                                jk += 1
                    else:
                        if i != n:
                            if i >= hk:
                                c[j].append(s[jk])
                                jk += 1
                        else:
                            if j % 2 == 0:
                                c[j].append(s[jk])
                                jk += 1
                else:
                    if y == 0:
                        if i != n:
                            c[j].append(s[jk])
                            jk += 1
                        if i == n:
                            if j % 2 == 0:
                                c[j].append(s[jk])
                                jk += 1
                    else:
                        if i <= hk:
                            c[j].append(s[jk])
                            jk += 1
                        else:
                            if j != lie:
                                if i < n:
                                    c[j].append(s[jk])
                                    jk += 1
                                else:
                                    if j % 2 == 0:
                                        c[j].append(s[jk])
                                        jk += 1
    cs = ''
    for i in range(1, len(c)):
        if i % 2 != 0:
            for j in range(0,len(c[i])):
                cs += c[i][j]
        else:
            for j in range(len(c[i]) - 1, -1, -1):
                cs += c[i][j]
    print('明文为:{}'.format(cs))
s = input('请输入密文：')
n = int(input('栅栏深度：'))
_list(s, n)