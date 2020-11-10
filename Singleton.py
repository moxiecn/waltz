class SINGLETON:
    """
    单例装饰器。
    """
    __cls = dict()

    def __init__(self, cls):
        self.__key = cls

    # 類的專有方法:在裝飾器內執行被裝飾的函數.
    # 調用的邏輯是,當待執行的函數self.__key,不在本類記錄的已執行函數字典中時執行一次self.__key函數.
    # 否則,不執行入參中的self.__key函數,直接返回本類實例字典中已經記錄在案的與入參同名的函數對象.
    def __call__(self, *args, **kwargs):
        if self.__key not in self.cls:
            self[self.__key] = self.__key(*args, **kwargs)
        return self[self.__key]

    # 類的專有方法:__setitem__按照索引對cls屬性做set操作
    def __setitem__(self, key, value):
        self.cls[key] = value

    # 類的專有方法:__getitem__按照索引對cls屬性作getter
    def __getitem__(self, item):
        return self.cls[item]

    # 聲明cls(self)類方法是一個屬性,屬性名就是方法名cls,相當於聲明了一個cls屬性,本方法是cls屬性的getter.
    # 比如當在類外部執行a=本類實例名.cls時,本類實際調用本類方法,返回self.__cls的值賦給變量a
    @property
    def cls(self):
        return self.__cls

    # 聲明cls(self,cls)類方法是一個setter,屬性名就是方法名cls,相當於聲明了一個cls屬性,本方法是cls屬性的setter.
    @cls.setter
    def cls(self, cls):
        self.__cls = cls
