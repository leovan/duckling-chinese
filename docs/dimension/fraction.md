# 分数

## 说明

暂无

## 示例

### 百分之六十

文本：`百分之六十`

解析实体列表：

```json
[
  {
    "dim": "Fraction",
    "body": "百分之六十",
    "value": {
      "n": 0.6,
      "numerator": 60.0,
      "denominator": 100.0
    },
    "start": 0,
    "end": 5
  }
]
```

`60%` 具有同上例相同的 `value` 值。

### 4分之3

文本：`4分之3`

解析实体列表：

```json
[
  {
    "dim": "Fraction",
    "body": "4分之3",
    "value": {
      "n": 0.75,
      "numerator": 3.0,
      "denominator": 4.0
    },
    "start": 0,
    "end": 4
  }
]
```

`四分之3`，`3/4` 具有同上例相同的 `value` 值。

### 负百分之百

文本：`负百分之百`

解析实体列表：

```json
[
  {
    "dim": "Fraction",
    "body": "负百分之百",
    "value": {
      "n": -1.0,
      "numerator": 100.0,
      "denominator": -100.0
    },
    "start": 0,
    "end": 5
  }
]
```

`负的百分之百`，`负的百分之一百` 具有同上例相同的 `value` 值。
