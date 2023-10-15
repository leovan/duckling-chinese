# 评分

## 说明

暂无

## 示例

### 评分8点5分

文本：`评分8点5分`

解析实体列表：

```json
[
  {
    "dim": "Rating",
    "body": "评分8点5分",
    "value": {
      "n": 8.5
    },
    "start": 0,
    "end": 6
  }
]
```

`8.5分`，`评分8.5` 具有同上例相同的 `value` 值。

### 评分在8.5分以上

文本：`评分在8.5分以上`

解析实体列表：

```json
[
  {
    "dim": "Rating",
    "body": "评分在8.5分以上",
    "value": {
      "start": 8.5,
      "direction": "After"
    },
    "start": 0,
    "end": 9
  }
]
```

`8.5分以上`，`评分大于八点五` 具有同上例相同的 `value` 值。

### 评分九点零以下

文本：`评分九点零以下`

解析实体列表：

```json
[
  {
    "dim": "Rating",
    "body": "评分九点零以下",
    "value": {
      "start": 9.0,
      "direction": "Before"
    },
    "start": 0,
    "end": 7
  }
]
```

`9分以下`，`评分小于九` 具有同上例相同的 `value` 值。

### 评分在7到8.5分

文本：`评分在7到8.5分`

解析实体列表：

```json
[
  {
    "dim": "Rating",
    "body": "评分在7到8.5分",
    "value": {
      "left": 7.0,
      "right": 8.5,
      "leftType": "Closed",
      "rightType": "Closed"
    },
    "start": 0,
    "end": 9
  }
]
```

`评分在7到8.5`，`评分在7到8.5分之间` 具有同上例相同的 `value` 值。
