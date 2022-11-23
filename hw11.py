import threading
import time


book = ""
queue1 = threading.Event()
queue2 = threading.Event()

queue2.set()


def writer1(interval):
    while True:
        queue2.wait()
        global book
        note = f"I'm Writer#{threading.get_ident()}. "
        print(f"Writer#{threading.get_ident()} приступил к записи")
        time.sleep(interval)
        book += note
        print(f"Writer#{threading.get_ident()} добавил запись '{note}'")
        queue1.set()
        queue2.clear()


def writer2(interval):
    while True:
        queue1.wait()
        global book
        note = f"I'm Writer#{threading.get_ident()}. "
        print(f"Writer#{threading.get_ident()} приступил к записи")
        time.sleep(interval)
        book += note
        print(f"Writer#{threading.get_ident()} добавил запись '{note}'")
        queue2.set()
        queue1.clear()


def reader(interval):
    while True:
        print(f"Reader#{threading.get_ident()}. Прочитано содержание книги, '{book}'")
        time.sleep(interval)


if __name__ == '__main__':
    w1 = threading.Thread(target=writer1, args=(2, ))
    w2 = threading.Thread(target=writer2, args=(3, ))
    r1 = threading.Thread(target=reader, args=(6, ))
    r2 = threading.Thread(target=reader, args=(7, ))
    r3 = threading.Thread(target=reader, args=(8, ))
    w1.start()
    w2.start()
    r1.start()
    r2.start()
    r3.start()
