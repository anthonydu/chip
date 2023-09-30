# Chip 片語

**Ch**inese **I**nterpreted **P**ython

## Example 範例

### Source Code 原始碼

```chip
寫出「你好，世界」
將甲定義為三
寫出【【【八加九】乘十三】除以三】

對於在九十九至一百零三之區間的甲：
  如果甲除以二之餘數不等於零：
    寫出甲
  否則：
    寫出甲除以二
```

### Interpreted 解釋

```python
print("你好，世界")
甲 = 3
print((((8 + 9) * 13) / 3))

for 甲 in range(99, 103):
  if 甲 % 2 != 0:
    print(甲)
  else:
    print(甲 / 2)
```

### Output 輸出

```
你好，世界
73.66666666666667
99
50.0
101
51.0
```
