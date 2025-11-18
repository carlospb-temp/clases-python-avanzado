from time import sleep
from threading import Thread


stop = False


def listen_stop():
    global stop
    input("Press ENTER to stop...")
    stop = True


def count_secs():
    count = 0
    global stop

    while not stop:
        sleep(1)
        print(count)
        count += 1


if __name__ == "__main__":
    Thread(target=count_secs).start()
    Thread(target=listen_stop).start()
