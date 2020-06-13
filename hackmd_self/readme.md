# Python中self參數與＠裝飾器的作用

> 109/06/05. 
 

## :memo: Python中self參數的用法

### 在介紹Python的self用法之前，先說下Python中的類別和實例

```python
class test():
    def __init__(self, name):
        self.name = name
    def who(self):
        return self.name

a = test("nick")

print(a.name)
print(a.who)
```
 - **class**是常用的類別宣告，為使用者提供可自訂名稱、匯入參數的模板。

- a = test("nick")此行是將已經宣告的test類別套入a變數，使a變數成為test類別的實例，並帶入"nick"作為name參數。

- **init**是特殊的名稱，用來定義類別的實例建立之後，要進行的初始化動作。

- __init__之後則可指定初始化時所必須給定的資料－－self參數。

- **self**參數代表建立的類別實例即**a**本身，在Python中，第一個參數必須明確作為接受實例之用，慣例上取名為self名稱。

### 執行結果

```python
print(a.name) -- nick
print(a.who) --
<bound method test.who of <__main__.test object at 0x7f22f71e9048>>
```

- 可以看到a.name直接指向"nick"字串，而a.who則指向self本身。

## :memo: Python中＠裝飾器的用法

### 一個簡單的裝飾器範例

```python
def wrapper(func):
    def access():
        print('...驗證許可權...')
        func()
    return access
    
@wrapper
def func1():
    print('func1 called')
@wrapper
def func2():
    print('func2 called')
    
func1()
func2()
```

### 執行結果

```python
...驗證許可權...
func1 called
...驗證許可權...
func2 called
```

- 可以看到，當我們執行func1函式時，不會直接印出called，而是會跳到前面呼叫＠裝飾器連接的wrapper，並將裝飾器下方的func1丟入wrapper。
- 運行步驟為：先進行wrapper底下access內的print('...驗證許可權...')，並在驗證完許可權後呼叫傳進來的引數func，接上print('func1 called')，隨後回到原點接著執行下一個裝飾器。
