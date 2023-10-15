# 重复

## 说明

详见：[时间](time.md#说明)

## 示例

!!! warning "注意"

    如下示例 `context` 参数的 `reference_time` 参数为：

    ```python
    datetime(
        year=2013,
        month=2,
        day=12,
        hour=4,
        minute=30,
        second=0,
        tzinfo=ZoneInfo('Asia/Shanghai')
    )
    ```

### 每天

文本：`每天`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每天",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Day",
        "latent": false,
        "fuzzy": false
      }
    },
    "start": 0,
    "end": 2
  }
]
```

### 每周

文本：`每周`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每周",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Week",
        "latent": false,
        "fuzzy": false
      }
    },
    "start": 0,
    "end": 2
  }
]
```

### 每隔15分钟

文本：`每隔15分钟`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每隔15分钟",
    "value": {
      "interval": {
        "value": 15,
        "grain": "Minute",
        "latent": false,
        "fuzzy": false
      }
    },
    "start": 0,
    "end": 6
  }
]
```

`隔15分钟` 具有同上例相同的 `value` 值。

### 每个月五号的早上

文本：`每个月五号的早上`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每个月五号的早上",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Month",
        "latent": false,
        "fuzzy": false
      },
      "start": {
        "_1": {
          "timeValue": {
            "start": {
              "datetime": "2013-03-05 04:00:00 [UTC+08:00]",
              "grain": "Hour"
            },
            "end": {
              "datetime": "2013-03-05 12:00:00 [UTC+08:00]",
              "grain": "Hour"
            }
          },
          "tzSeries": []
        }
      }
    },
    "start": 0,
    "end": 8
  }
]
```

### 每个月的五号

文本：`每个月的五号`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每个月的五号",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Month",
        "latent": false,
        "fuzzy": false
      },
      "start": {
        "_1": {
          "timeValue": {
            "instant": {
              "datetime": "2013-03-05 00:00:00 [UTC+08:00]",
              "grain": "Day"
            }
          },
          "tzSeries": []
        }
      }
    },
    "start": 0,
    "end": 6
  }
]
```

### 每月2号下午2点

文本：`每月2号下午2点`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每月2号下午2点",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Month",
        "latent": false,
        "fuzzy": false
      },
      "start": {
        "_1": {
          "timeValue": {
            "instant": {
              "datetime": "2013-03-02 14:00:00 [UTC+08:00]",
              "grain": "Hour"
            }
          },
          "tzSeries": []
        }
      }
    },
    "start": 0,
    "end": 8
  }
]
```

### 每周三

文本：`每周三`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每周三",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Week",
        "latent": false,
        "fuzzy": false
      },
      "start": {
        "_1": {
          "timeValue": {
            "instant": {
              "datetime": "2013-02-13 00:00:00 [UTC+08:00]",
              "grain": "Day"
            }
          },
          "tzSeries": []
        },
        "_2": {}
      }
    },
    "start": 0,
    "end": 3
  }
]
```

`每个星期三` 具有同上例相同的 `value` 值。

### 每天上午八点

文本：`每天上午八点`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每天上午八点",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Day",
        "latent": false,
        "fuzzy": false
      },
      "start": {
        "_1": {
          "timeValue": {
            "instant": {
              "datetime": "2013-02-12 08:00:00 [UTC+08:00]",
              "grain": "Hour"
            }
          },
          "tzSeries": []
        },
        "_2": {
          "hours": 8,
          "is12H": false
        }
      }
    },
    "start": 0,
    "end": 6
  }
]
```

`每个上午八点` 具有同上例相同的 `value` 值。

### 非工作日

文本：`非工作日`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "非工作日",
    "value": {
      "workdayType": "NonWorkday"
    },
    "start": 0,
    "end": 4
  }
]
```

`节假日` 具有同上例相同的 `value` 值。

### 工作日三点

文本：`工作日三点`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "工作日三点",
    "value": {
      "start": {
        "_1": {
          "timeValue": {
            "instant": {
              "datetime": "2013-02-13 03:00:00 [UTC+08:00]",
              "grain": "Hour"
            }
          },
          "tzSeries": []
        },
        "_2": {
          "hours": 3,
          "is12H": false
        }
      },
      "workdayType": "Workday"
    },
    "start": 0,
    "end": 5
  }
]
```

`每个工作日三点` 具有同上例相同的 `value` 值。

### 每个工作日上午

文本：`每个工作日上午`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每个工作日上午",
    "value": {
      "start": {
        "_1": {
          "timeValue": {
            "start": {
              "datetime": "2013-02-12 08:00:00 [UTC+08:00]",
              "grain": "Hour"
            },
            "end": {
              "datetime": "2013-02-12 12:00:00 [UTC+08:00]",
              "grain": "Hour"
            }
          },
          "tzSeries": [],
          "partOfDay": "上午"
        },
        "_2": {
          "part": "上午"
        }
      },
      "workdayType": "Workday"
    },
    "start": 0,
    "end": 7
  }
]
```

### 每周三下午

文本：`每周三下午`

解析实体列表：

```json
[
  {
    "dim": "Repeat",
    "body": "每周三下午",
    "value": {
      "interval": {
        "value": 1,
        "grain": "Week",
        "latent": false,
        "fuzzy": false
      },
      "start": {
        "_1": {
          "timeValue": {
            "start": {
              "datetime": "2013-02-13 12:00:00 [UTC+08:00]",
              "grain": "Hour"
            },
            "end": {
              "datetime": "2013-02-13 18:00:00 [UTC+08:00]",
              "grain": "Hour"
            }
          },
          "tzSeries": [],
          "partOfDay": "下午"
        },
        "_2": {
          "part": "下午"
        }
      }
    },
    "start": 0,
    "end": 5
  }
]
```
