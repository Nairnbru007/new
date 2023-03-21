import threading

def Count_smth(int_c):
    print('start f-'+str(int_c))
    i=0
    while i<=10**int_c:
      i+=1
    print('end f-'+str(int_c))
    


if __name__ == '__main__':
    t1 = threading.Thread(target=Count_smth, args=(7,), daemon=True)
    t2 = threading.Thread(target=Count_smth, args=(3,), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
