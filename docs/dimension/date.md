# 日期

## 说明

日期作为[时间](time.md#说明)的子集在只需要提取日期时可以提高效率。

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

### 2015-3-3

文本：`2015-3-3`

解析实体列表：

```json
[
  {
    "dim": "Date",
    "body": "2015-3-3",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2015-03-03 00:00:00 [UTC+08:00]",
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

`2015-03-03`，`20150303`，`2015/3/3`，`2015.3.3`，`15.3.3`，`2015年3月3号`，`2015年3月三号`，`2015年三月3号`，`2015年三月三号` 具有同上例相同的 `value` 值。

### 2015年

文本：`2015年`

解析实体列表：

```json
[
  {
    "dim": "Date",
    "body": "2015年",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2015-01-01 00:00:00 [UTC+08:00]",
          "grain": "Year"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 5
  }
]
```

`2015版`，`2015年版`，`15年`，`15版`，`15年版`，`一五年`，`一五版`，`一五年版`，`二零一五年` 具有同上例相同的 `value` 值。

### 03/03

文本：`03/03`

`context` 参数：`reference_time=datetime(2013, 2, 10, tzinfo=ZoneInfo('Asia/Shanghai')`

解析实体列表：

```json
[
  {
    "dim": "Date",
    "body": "03/03",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-03-03 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 5
  }
]
```

### 月底

文本：`月底`

解析实体列表：

```json
[
  {
    "dim": "Date",
    "body": "月底",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "2013-02-28 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 2
  }
]
```

### 农历一月十八

文本：`农历一月十八`

`context` 参数：`reference_time=datetime(2013, 2, 10, tzinfo=ZoneInfo('Asia/Shanghai')`

解析实体列表：

```json
[
  {
    "dim": "Date",
    "body": "农历一月十八",
    "value": {
      "timeValue": {
        "instant": {
          "datetime": "农历 二〇一三年正月十八 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 6
  }
]
```

`正月十八`，`农历的一月十八`，`阴历的正月十八` 具有同上例相同的 `value` 值。

### 今明后三天

文本：`今明后三天`

`context` 参数：`reference_time=datetime(2013, 2, 10, tzinfo=ZoneInfo('Asia/Shanghai')`

解析实体列表：

```json
[
  {
    "dim": "Date",
    "body": "今明后三天",
    "value": {
      "timeValue": {
        "start": {
          "datetime": "2013-02-12 00:00:00 [UTC+08:00]",
          "grain": "Day"
        },
        "end": {
          "datetime": "2013-02-15 00:00:00 [UTC+08:00]",
          "grain": "Day"
        }
      },
      "tzSeries": []
    },
    "start": 0,
    "end": 5
  }
]
```

`今天明天后天三天` 具有同上例相同的 `value` 值。
