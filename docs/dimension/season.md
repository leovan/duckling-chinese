# 季数

## 说明

暂无

## 示例

### 倒数第一场

文本：`倒数第一场`

解析实体列表：

```json
[
  {
    "dim": "Season",
    "body": "倒数第一季",
    "value": {
      "v": -1.0,
      "unit": "季",
      "dim": "季"
    },
    "start": 0,
    "end": 5
  }
]
```

`最后一季` 具有同上例相同的 `value` 值。

### 第三季

文本：`第三季`

解析实体列表：

```json
[
  {
    "dim": "Season",
    "body": "第三季",
    "value": {
      "v": 3.0,
      "unit": "季",
      "dim": "季"
    },
    "start": 0,
    "end": 3
  }
]
```

`第三部`，`3季`，`三部` 具有同上例相同的 `value` 值。
