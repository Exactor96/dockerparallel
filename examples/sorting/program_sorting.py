def srt(lst):
    return sorted(lst)



if __name__ == '__main__':
    import random
    count=random.randint(100,10**5)
    list_for_sort=[random.randint(-10**6,10**6) for i in range(count)]
    with open('res','w') as f:
        for each in srt(list_for_sort):
            f.write(str(each)+' ')
    f.close()
