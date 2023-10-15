# 时间

## 说明

时间作为最复杂最基础的维度，需要注意如下事项：

1. 所有时间区间都是左闭右开的。
2. 在没有指定范围时，总是取下一个即将发生的。
3. 时间点/时间区间与[持续时间](duration.md)的概念是不同的。
4. 由上下文无关文法（CFG）保证规则复用。
5. 由概率上下文无关文法（PCFC）保证组合结果择优。
6. Scala 内部采用纯函数式实现，无线程安全问题。
7. 具有更高的测试覆盖和可接受的性能。

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

### 现在

文本：`现在`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "现在",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2023-10-14 20:30:10 [UTC+08:00]",
          "grain": "Second"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 2
  }
]
```

`此时`，`此刻`，`当前`，`04:30:00` 具有同上例相同的 `value` 值。

### 下午三点十五

文本：`下午三点十五`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "下午三点十五",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-12 15:15:00 [UTC+08:00]",
          "grain": "Minute"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 6
  }
]
```

`下午3:15`，`15:15`，`3:15pm`，`3:15p.m`，`下午三点一刻`，`下午的三点一刻` 具有同上例相同的 `value` 值。

### 明天晚上12点

文本：`明天晚上12点`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "明天晚上12点",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-14 00:00:00 [UTC+08:00]",
          "grain": "Hour"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 7
  }
]
```

`13号晚上12点`，`13号晚12点` 具有同上例相同的 `value` 值。

### 今早6点

文本：`今早6点`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "今早6点",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-12 06:00:00 [UTC+08:00]",
          "grain": "Hour"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 4
  }
]
```

`今天早上6点`，`12号早上6点`，`12号早6点` 具有同上例相同的 `value` 值。

### 明天10点

文本：`明天10点`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "明天10点",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-13 10:00:00 [UTC+08:00]",
          "grain": "Hour"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 5
  }
]
```

`明天上午十点`，`明天中午10点` 具有同上例相同的 `value` 值。

### 上两秒

文本：`上两秒`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "上两秒",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "2013-02-12 04:29:58 [UTC+08:00]",
          "grain": "Second"
        },
        "end": {
          "datetime": "2013-02-12 04:30:00 [UTC+08:00]",
          "grain": "Second"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 3
  }
]
```

`上二秒`，`前两秒`，`前二秒` 具有同上例相同的 `value` 值。

### 未来一刻钟

文本：`未来一刻钟`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "未来一刻钟",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "2013-02-12 04:30:00 [UTC+08:00]",
          "grain": "Minute"
        },
        "end": {
          "datetime": "2013-02-12 04:45:00 [UTC+08:00]",
          "grain": "Minute"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 5
  }
]
```

`之后一刻钟`，`向后一刻钟`，`往后一刻钟`，`下一刻钟`，`后一刻钟` 具有同上例相同的 `value` 值。

### 星期日

文本：`星期日`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "星期日",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-17 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 3
  }
]
```

`星期天`，`礼拜日`，`礼拜天`，`周日`，`周天` 具有同上例相同的 `value` 值。

### 这周三

文本：`这周三`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "这周三",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-13 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 3
  }
]
```

`这礼拜三`，`今个星期三`，`今个礼拜三` 具有同上例相同的 `value` 值。

### 下周

文本：`下周`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "下周",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-18 00:00:00 [UTC+08:00]",
          "grain": "Week"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 2
  }
]
```

`下星期`，`下礼拜` 具有同上例相同的 `value` 值。

### 三星期后

文本：`三星期后`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "三星期后",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-03-05 04:30:00 [UTC+08:00]",
          "grain": "Second"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 4
  }
]
```

`三星期之后`，`三个礼拜后`，`三个礼拜之后`，`三星期以后`，`三星期过后` 具有同上例相同的 `value` 值。

### 国庆节

文本：`国庆节`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "国庆节",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-10-01 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": [],
      "holiday": "国庆节"
    },
    "start": 0,
    "end": 3
  }
]
```

`十一`，`国庆` 具有同上例相同的 `value` 值。

### 周一早上

文本：`周一早上`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "周一早上",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "2013-02-18 04:00:00 [UTC+08:00]",
          "grain": "Hour"
        },
        "end": {
          "datetime": "2013-02-18 12:00:00 [UTC+08:00]",
          "grain": "Hour"
        }
      },
      "tzSeries": [],
      "partOfDay": "早上"
    },
    "start": 0,
    "end": 4
  }
]
```

`周一早晨`，`周一清晨`，`礼拜一早上`，`礼拜一早晨`，`下周一早上` 具有同上例相同的 `value` 值。

### 十月第一个星期一

文本：`十月第一个星期一`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "十月第一个星期一",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-10-07 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 8
  }
]
```

`十月的第一个星期一` 具有同上例相同的 `value` 值。

### 女生节下午三点十五

文本：`女生节下午三点十五`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "女生节下午三点十五",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-03-07 15:15:00 [UTC+08:00]",
          "grain": "Minute"
        }
      },
      "tzSeries": [],
      "holiday": "女生节"
    },
    "start": 0,
    "end": 9
  }
]
```

### 11点05分到15点08分

文本：`11点05分到15点08分`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "11点05分到15点08分",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "2013-02-12 11:05:00 [UTC+08:00]",
          "grain": "Minute"
        },
        "end": {
          "datetime": "2013-02-12 15:08:00 [UTC+08:00]",
          "grain": "Minute"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 13
  }
]
```

`11点05到15点08`，`十一点零五分到十五点零八分`，`十一点零五到十五点零八`，`11:05~15:08` 具有同上例相同的 `value` 值。

### 凌晨

文本：`凌晨`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "凌晨",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "2013-02-12 00:00:00 [UTC+08:00]",
          "grain": "Hour"
        },
        "end": {
          "datetime": "2013-02-12 06:00:00 [UTC+08:00]",
          "grain": "Hour"
        }
      },
      "tzSeries": [],
      "partOfDay": "凌晨"
    },
    "start": 0,
    "end": 2
  }
]
```

### 明年的11月份第二个周日

文本：`明年的11月份第二个周日`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "明年的11月份第二个周日",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2014-11-09 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 12
  },
  {
    "dim": "Time",
    "body": "明年的11月份第二个周日",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2014-11-09 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 12
  }
]
```

### 2019年腊月初一上午

文本：`2019年腊月初一上午`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "2019年腊月初一上午",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "农历 二〇一九年腊月初一 08:00:00 [UTC+08:00]",
          "grain": "Hour"
        },
        "end": {
          "datetime": "农历 二〇一九年腊月初一 12:00:00 [UTC+08:00]",
          "grain": "Hour"
        }
      },
      "tzSeries": [],
      "partOfDay": "上午"
    },
    "start": 0,
    "end": 11
  }
]
```

### 下一个中秋节

文本：`下一个中秋节`

解析实体列表：

```json
[
  {
    "dim": "Time",
    "body": "下一个中秋节",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "农历 二〇一三年八月十五 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": [],
      "holiday": "中秋节"
    },
    "start": 0,
    "end": 6
  }
]
```
