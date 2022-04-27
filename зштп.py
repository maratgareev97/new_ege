import os


def cons_read(mstr):
    a = os.popen(mstr)
    res = a.read()
    a.close()
    print(res)


if __name__ == '__main__':
    cons_read(mstr='ping ya.ru')