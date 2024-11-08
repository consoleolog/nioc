

from multiprocessing.dummy import Pool as ThreadPool

from main_controller import start

if __name__ == '__main__':
    pool = ThreadPool(processes=4)
    pool.map(start, [])
    pool.close()
    pool.join()