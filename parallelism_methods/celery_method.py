from tasks import mk
if __name__ == '__main__':
    [mk.delay(i) for i in range(10)]
