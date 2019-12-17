from threading import Thread

def fibonacci(limit):
    if limit >= 1:
        n2 = 1
        yield n2
    n1 = 0
    for i in range(1, limit):
        n = n1 + n2
        yield n
        n1, n2 = n2, n


def simplescript(thefile, num):
    with open(thefile, 'w') as f:
        for i in range(num):
            if num > 500:
                f.write('МногоБукв\n')
                for j in fibonacci(200):
                    f.write(str(j))
            else:
                f.write('МалоБукв\n')

                for j in fibonacci(200):
                    f.write(str(j))


thread1 = Thread(target=simplescript, args=('f1.txt', 200,))
thread2 = Thread(target=simplescript, args=('f2.txt', 1000,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()