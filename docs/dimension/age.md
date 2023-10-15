# 年龄

## 说明

暂无

## 示例

### 三岁

文本：`三岁`

解析实体列表：

```json
[
  {
    "dim": "Age",
    "body": "三岁",
    "value": {
      "n": 3.0
    },
    "start": 0,
    "end": 2
  }
]
```

### 三岁半以上

文本：`三岁半以上`

解析实体列表：

```json
[
  {
    "dim": "Age",
    "body": "三岁半以上",
    "value": {
      "start": 3.5,
      "direction": "After"
    },
    "start": 0,
    "end": 5
  }
]
```

`大于三岁半` 具有同上例相同的 `value` 值。

### 三岁半以下

文本：`三岁半以下`

解析实体列表：

```json
[
  {
    "dim": "Age",
    "body": "三岁半以下",
    "value": {
      "start": 3.5,
      "direction": "Before"
    },
    "start": 0,
    "end": 5
  }
]
```

### 三到五岁半

文本：`三到五岁半`

解析实体列表：

```json
[
  {
    "dim": "Age",
    "body": "三到五岁半",
    "value": {
      "left": 3.0,
      "right": 5.5,
      "leftType": "Closed",
      "rightType": "Closed"
    },
    "start": 0,
    "end": 5
  }
]
```

### 三到五岁

文本：`三到五岁`

解析实体列表：

```json
[
  {
    "dim": "Age",
    "body": "三到五岁",
    "value": {
      "left": 3.0,
      "right": 5.0,
      "leftType": "Closed",
      "rightType": "Closed"
    },
    "start": 0,
    "end": 4
  }
]
```
