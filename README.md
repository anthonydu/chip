# Chip 片語

**Ch**inese **I**nterpreted **P**ython

## Example 範例

### Source Code 原始碼

```chip
寫出：「你好，世界」

將甲定義為「你好，片語」
寫出：甲

將乙定義為三
寫出：以八加九加以八十減七十之差之和乘十三除以乙

寫出：「今天天氣晴，零上三十六攝氏度」
寫出：「明天天氣陰，零下三百六十八度」

九十九起小於一百零三的甲：
  若甲除以二之餘數不等於零：
    寫出：甲
  否則：
    寫出：甲除以二取整
```

### Interpreted 解讀

```python
print("你好，世界")

甲 = "你好，片語"
print(甲)

乙 = 3
print((8 + 9 + (80 - 70)) * 13 / 乙)

print("今天天氣晴，零上三十六攝氏度")
print("明天天氣陰，零下三百六十八度")

for 甲 in range(99, 103):
  if 甲 % 2 != 0:
    print(甲)
  else:
    print(甲 // 2)
```

### Output 輸出

```text
你好，世界
你好，片語
一百一十七点零
今天天氣晴，零上三十六攝氏度
明天天氣陰，零下三百六十八度
九十九
五十
一百零一
```
