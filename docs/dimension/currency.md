# 货币

## 说明

暂无

## 示例

### 九十九元九角九分

文本：`九十九元九角九分`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九十九元九角九分",
    "value": {
      "v": 99.99,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 8
  }
]
```

`九十九块九毛九` 具有同上例相同的 `value` 值。

### 九十九块九

文本：`九十九块九`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九十九块九",
    "value": {
      "v": 99.9,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 5
  }
]
```

### 九块九

文本：`九块九`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九块九",
    "value": {
      "v": 9.9,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 3
  }
]
```

`九元九角` 具有同上例相同的 `value` 值。

### 九元零九分

文本：`九元零九分`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九元零九分",
    "value": {
      "v": 9.09,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 5
  }
]
```

### 九角九分

文本：`九角九分`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九角九分",
    "value": {
      "v": 0.99,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 4
  }
]
```

`九毛九` 具有同上例相同的 `value` 值。

### 九毛钱

文本：`九毛钱`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九毛钱",
    "value": {
      "v": 0.9,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 3
  }
]
```

### 九分钱

文本：`九分钱`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "九分钱",
    "value": {
      "v": 0.09,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 3
  }
]
```

### 两块九毛九

文本：`两块九毛九`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "两块九毛九",
    "value": {
      "v": 2.99,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 5
  }
]
```

### RMB两块九毛九

文本：`RMB两块九毛九`

解析实体列表：

```json
[
  {
    "dim": "Currency",
    "body": "RMB两块九毛九",
    "value": {
      "v": 2.99,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 8
  },
  {
    "dim": "Currency",
    "body": "RMB两块九毛九",
    "value": {
      "v": 2.99,
      "unit": "元",
      "dim": "货币:CNY"
    },
    "start": 0,
    "end": 8
  }
]
```

`两块九毛九RMB` 具有同上例相同的 `value` 值。
