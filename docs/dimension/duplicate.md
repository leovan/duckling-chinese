# 重复

## 说明

暂无

## 示例

### 张三张三张三

文本：`张三张三张三`

解析实体列表：

```json
[
  {
    "dim": "Duplicate",
    "body": "张三张三张三",
    "value": {
      "w": "张三",
      "times": 3
    },
    "start": 0,
    "end": 6
  }
]
```

### 123123123

文本：`123123123`

解析实体列表：

```json
[
  {
    "dim": "Duplicate",
    "body": "123123123",
    "value": {
      "w": "123",
      "times": 3
    },
    "start": 0,
    "end": 9
  }
]
```