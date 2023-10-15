# 持续时间

## 说明

`value` 值的字段如下：

| 字段   | 说明                         |
| ------ | ---------------------------- |
| value  | 时长                         |
| grain  | 时长单位                     |
| latent | 是否是潜在时间               |
| fuzzy  | 是否是模糊时间（例如：几天） |

详见：[时间](time.md#说明)

## 示例

### 1秒钟

文本：`1秒钟`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "1秒钟",
    "value": {
      "value": 1,
      "grain": "Second",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 3
  }
]
```

`1秒` 具有同上例相同的 `value` 值。

### 1分09秒

文本：`1分09秒`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "1分09秒",
    "value": {
      "value": 69,
      "grain": "Second",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 5
  }
]
```

`一分零九秒`，`一分九秒` 具有同上例相同的 `value` 值。

### 1小时09分

文本：`1小时09分`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "1小时09分",
    "value": {
      "value": 69,
      "grain": "Minute",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 6
  }
]
```

`1小时9分`，`一小时零九分`，`一小时九分` 具有同上例相同的 `value` 值。

### 30天

文本：`30天`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "30天",
    "value": {
      "value": 30,
      "grain": "Day",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 3
  }
]
```

### 七周

文本：`七周`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "七周",
    "value": {
      "value": 7,
      "grain": "Week",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 2
  }
]
```

### 示例 5

文本：`一个月`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "一个月",
    "value": {
      "value": 1,
      "grain": "Month",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 3
  }
]
```

### 3个季度

文本：`3个季度`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "3个季度",
    "value": {
      "value": 3,
      "grain": "Quarter",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 4
  }
]
```

### 两年

文本：`两年`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "两年",
    "value": {
      "value": 2,
      "grain": "Year",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 2
  }
]
```

### 两年零三个月

文本：`两年零三个月`

解析实体列表：

```json
[
  {
    "dim": "Duration",
    "body": "两年零三个月",
    "value": {
      "value": 27,
      "grain": "Month",
      "latent": false,
      "fuzzy": false
    },
    "start": 0,
    "end": 6
  }
]
```

`两年外加三个月`，`两年加上三个月`，`两年加三个月`，`两年三个月` 具有同上例相同的 `value` 值。
