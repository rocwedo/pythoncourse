


class observerable:
    
    #初始化
    def __init__(self) -> None:
        self.observers=[]
        pass
    
    #增加观察者
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print("Failed to add: {}".format(observer))

    #删除观察者
    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.notify(self)

class observer:
    def notify(self,observerable):
        print("oberver ok")


def main():
    publisher = observerable()
    obser01 = observer()
    publisher.add(observer=obser01)
    publisher.notify()


if __name__ == '__main__':
    main()