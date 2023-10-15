# 演出

## 说明

暂无

## 示例

### 倒数第一场

文本：`倒数第一场`

解析实体列表：

```json
[
  {
    "dim": "Act",
    "body": "倒数第一场",
    "value": {
      "v": -1.0,
      "unit": "场",
      "dim": "场"
    },
    "start": 0,
    "end": 5
  }
]
```

`最后一番`，`最新一场` 具有同上例相同的 `value` 值。

### 第三场

文本：`第三场`

解析实体列表：

```json
[
  {
    "dim": "Act",
    "body": "第三场",
    "value": {
      "v": 3.0,
      "unit": "场",
      "dim": "场"
    },
    "start": 0,
    "end": 3
  }
]
```

`第三番`，`3场`，`三弹` 具有同上例相同的 `value` 值。