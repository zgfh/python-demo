
print("package3.module3_1 加载开始")

class Module3_1_class_1:
  class_variable=1
  
  def __init__(self) -> None:
    self.class_instance_variable=1
    '''
    __init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后
    '''
    print("package3.module3_1 module3_1_class_1 __init__  加载开始")
    print("package3.module3_1 module3_1_class_1 __init__ 加载完成")
  
  def __new__(cls):
    '''
    __new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。
    '''
    print("package3.module3_1 module3_1_class_1 __new__ 加载开始")
    print("package3.module3_1 module3_1_class_1 __new__ 加载完成")
    return super(Module3_1_class_1, cls).__new__(cls)
    
print("package3.module3_1 加载完成")

