'''
 参考： https://docs.python.org/3/reference/import.html
'''
import sys


print("package加载顺序演示:")
import package1.package2
#print(sys.modules)
print("package重复导入 加载顺序演示:")
import package1.package2
#print(sys.modules)
print()

print("module加载顺序演示:")
import package1.package2.module2_1
print("module 重复导入  加载顺序演示:")
import package1.package2.module2_1
print()

#特殊用法

print("遍历某个目录下的类")
import pkgutil
for importer, modname, ispkg in pkgutil.iter_modules(package1.package2.__path__):
  plugin = importer.find_module(modname).load_module(modname)
  print(plugin)

#TODO
# 1. 重新加载一个类:importlib.reload()



print("类演示:")

print("类加载演示:")
# pyton的代码在编译时，无论是函数，还是类，都生成了相应的对象，无论这个类是否实例化，都生成了类对象
# pytyon类对象是一个静态对象, 一旦生成，就不再变化

from package1.package3.module3_1 import Module3_1_class_1
print(Module3_1_class_1.__name__)
print("类实例a:")
a=Module3_1_class_1()
print("a类变量:",a.class_variable)
print("a类实例变量:",a.class_instance_variable)


print("类实例b:")
b=Module3_1_class_1()
print("b类变量:",b.class_variable)
print("b类实例变量:",b.class_instance_variable)

a.class_variable=2 # 这里其实操作是创建了一个相同名的类实例变量
a.class_instance_variable=2  
print("修改a后:") 
print("b类变量:",b.class_variable)
print("b类实例变量:",b.class_instance_variable)

print("修改类变量后:")
Module3_1_class_1.class_variable=3
print("a类变量:",a.class_variable)
print("a类实例变量:",a.class_instance_variable)
print("b类变量:",b.class_variable)
print("b类实例变量:",b.class_instance_variable)



# TODO
# 需要类后，再次导入


# 删除一个类实例变量
# 删除一个类变量
# 删除一个类实例
# 删除一个类
print()