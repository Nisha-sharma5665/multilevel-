class basecls:
    x=5
    def feature1(self):
        print("hello feature1")
        class subcls(basecls):
            def feature2(self):
                print("hello feature2")
                class subcls1(subcls):
                    def feature3(self):
                        print("hello feature3")
                        obj=basecls()
                        obj1=subcls()
                        obj2=subcls1()
                        obj1.feature1()
                        obj1.feature2()
                        print(obj1.x)
                        print(obj2.x)
                        obj2.feature2()