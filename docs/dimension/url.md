# URL

## 说明

暂无

## 示例

### http://www.bla.com

文本：`http://www.bla.com`

解析实体列表：

```json
[
  {
    "dim": "URL",
    "body": "http://www.bla.com",
    "value": {
      "url": "http://www.bla.com",
      "domain": "bla.com",
      "protocol": "http"
    },
    "start": 0,
    "end": 18
  }
]
```

### www.bla.com:8080/path

文本：`www.bla.com:8080/path`

解析实体列表：

```json
[
  {
    "dim": "URL",
    "body": "www.bla.com:8080/path",
    "value": {
      "url": "www.bla.com:8080/path",
      "domain": "bla.com"
    },
    "start": 0,
    "end": 21
  }
]
```

### https://myserver?foo=bar

文本：`https://myserver?foo=bar`

解析实体列表：

```json
[
  {
    "dim": "URL",
    "body": "https://myserver?foo=bar",
    "value": {
      "url": "https://myserver?foo=bar",
      "domain": "myserver",
      "protocol": "https"
    },
    "start": 0,
    "end": 24
  }
]
```
