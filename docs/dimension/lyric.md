# 歌词

## 说明

暂无

## 示例

### 作曲:刘德华

文本：`作曲:刘德华`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "作曲:刘德华",
    "value": {
      "roles": {
        "作曲": [
          "刘德华"
        ]
      }
    },
    "start": 0,
    "end": 6
  }
]
```

### 作曲-编曲:刘德华

文本：`作曲-编曲:刘德华`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "作曲-编曲:刘德华",
    "value": {
      "roles": {
        "作曲": [
          "刘德华"
        ],
        "编曲": [
          "刘德华"
        ]
      }
    },
    "start": 0,
    "end": 9
  }
]
```

### 作曲:张三 作词:李四

文本：`作曲:张三 作词:李四`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "作曲:张三 作词:李四",
    "value": {
      "roles": {
        "作曲": [
          "张三"
        ],
        "作词": [
          "李四"
        ]
      }
    },
    "start": 0,
    "end": 11
  }
]
```

### 编曲:墨辞  词: 刀郎

文本：`编曲:墨辞  词: 刀郎`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "编曲:墨辞  词: 刀郎",
    "value": {
      "roles": {
        "作词": [
          "刀郎"
        ],
        "编曲": [
          "墨辞"
        ]
      }
    },
    "start": 0,
    "end": 12
  }
]
```

### 编曲:墨辞  词: 刀郎 曲 周杰伦

文本：`编曲:墨辞  词: 刀郎 曲 周杰伦`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "编曲:墨辞  词: 刀郎 曲 周杰伦",
    "value": {
      "roles": {
        "作曲": [
          "周杰伦"
        ],
        "作词": [
          "刀郎"
        ],
        "编曲": [
          "墨辞"
        ]
      }
    },
    "start": 0,
    "end": 18
  },
  {
    "dim": "Lyric",
    "body": "编曲:墨辞  词: 刀郎 曲 周杰伦",
    "value": {
      "roles": {
        "作曲": [
          "周杰伦"
        ],
        "作词": [
          "刀郎"
        ],
        "编曲": [
          "墨辞"
        ]
      }
    },
    "start": 0,
    "end": 18
  }
]
```

### 作词:爱内里菜/作曲/编曲:corin

文本：`作词:爱内里菜/作曲/编曲:corin`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "作词:爱内里菜/作曲/编曲:corin",
    "value": {
      "roles": {
        "作曲": [
          "corin"
        ],
        "作词": [
          "爱内里菜"
        ],
        "编曲": [
          "corin"
        ]
      }
    },
    "start": 0,
    "end": 19
  }
]
```

### 作曲:黄耀光|填词:林夕

文本：`作曲:黄耀光|填词:林夕`

解析实体列表：

```json
[
  {
    "dim": "Lyric",
    "body": "作曲:黄耀光|填词:林夕",
    "value": {
      "roles": {
        "作曲": [
          "黄耀光"
        ],
        "作词": [
          "林夕"
        ]
      }
    },
    "start": 0,
    "end": 12
  }
]
```