# 接口

## 对象

创建 `Duckling` 对象：

```python
from duckling_chinese import Duckling

duckling = Duckling()
```

## 方法

利用对象的 `analyze` 方法获取解析结果列表：

```python
def analyze(
    self,
    text: Text,
    context: JavaDucklingTypes.Context = None,
    options: JavaDucklingTypes.Options = None,
    remove_duplicate=True
) -> List[Dict[Text, Any]]
```

返回结果为利用 [`JsonSerde.scala`](https://github.com/XiaoMi/MiNLP/blob/main/duckling-fork-chinese/core/src/main/scala/com/xiaomi/duckling/JsonSerde.scala) 中定义的格式序列化 [`Types.scala`](https://github.com/XiaoMi/MiNLP/blob/main/duckling-fork-chinese/core/src/main/scala/com/xiaomi/duckling/Types.scala) 中的 `Answer` 列表为 JSON 后解析得到的字典列表。

利用对象的 `parse_entities` 方法获取解析实体列表：

```python
def parse_entities(
    self,
    text: Text,
    context: JavaDucklingTypes.Context = None,
    options: JavaDucklingTypes.Options = None,
    remove_duplicate=True
) -> List[Dict[Text, Any]]
```

返回结果为利用 [`JsonSerde.scala`](https://github.com/XiaoMi/MiNLP/blob/main/duckling-fork-chinese/core/src/main/scala/com/xiaomi/duckling/JsonSerde.scala) 中定义的格式序列化 [`Types.scala`](https://github.com/XiaoMi/MiNLP/blob/main/duckling-fork-chinese/core/src/main/scala/com/xiaomi/duckling/Types.scala) 中的 `Entity` 列表为 JSON 后解析得到的字典列表。

利用 `lunar_to_solar` 工具函数可以将解析结果中 `农历 一八五〇年正月初一 00:00:00 [UTC+08:00]` 样式的农历日期时间转换为 `1850-02-12 00:00:00 [UTC+08:00]` 样式的公历日期时间。

```python
from duckling_chinese import lunar_to_solar

def lunar_to_solar(lunar_datetime: Text)
```

!!! warning "注意"

    支持的转换时间区间为 `一八五〇年正月初一` 至 `二一五〇年十二月三十一`，详见 [LunarCalendar](https://github.com/heqiao2010/LunarCalendar/tree/master/java)。

## 参数

参数列表如下：

| 参数             | 类型                                | 默认值 | 说明             |
| ---------------- | ----------------------------------- | ------ | ---------------- |
| text             | `str`                               |        | 待解析文本       |
| context          | `com.xiaomi.duckling.Types.Context` | `None` | 解析上下文       |
| options          | `com.xiaomi.duckling.Types.Options` | `None` | 解析选项         |
| remove_duplicate | `bool`                              | `True` | 是否删除重复结果 |

### `context`

使用对象的 `gen_context` 方法可以构造 `context` 参数：

```python
def gen_context(
    self,
    reference_time=datetime.now(ZoneInfo('Asia/Shanghai')),
    language='zh',
    country='CN'
)
```

参数列表如下：

| 参数           | 类型     | 默认值                                  | 说明                           |
| -------------- | -------- | --------------------------------------- | ------------------------------ |
| reference_time | datetime | datetime.now(ZoneInfo('Asia/Shanghai')) | 参考时间，请设置正确的时区信息 |
| language       | str      | zh                                      | 语言                           |
| country        | str      | CN                                      | 国家                           |

针对中文解析，设置 `context` 为 `None` 会使用该方法的默认参数构建 `context`。

### `options`

使用对象的 `gen_options` 方法可以构造 `options` 参数：

```python
def gen_options(
    self,
    with_latent=False,
    full=False,
    debug=False,
    targets: Set[DucklingDimension] = None,
    varchar_expand=False,
    entity_with_node=False,
    rank_options=None,
    time_options=None,
    numeral_options=None
)
```

参数列表如下：

| 参数             | 类型                                                   | 默认值  | 说明                                                 |
| ---------------- | ------------------------------------------------------ | ------- | ---------------------------------------------------- |
| with_latent      | `bool`                                                 | `False` | 是否返回潜在结果                                     |
| full             | `bool`                                                 | `False` | 为 `true` 时，只返回完整匹配整串的结果               |
| debug            | `bool`                                                 | `False` | 是否开启调试                                         |
| targets          | `Set[DucklingDimension]`                               | `None`  | 解析目标集和，详见[维度](dimension/index.md)         |
| varchar_expand   | `bool`                                                 | `False` |                                                      |
| entity_with_node | `bool`                                                 | `False` |                                                      |
| rank_options     | `com.xiaomi.duckling.Types.RankOptions`                | `None`  | 排序配置，详见 [`rank_options`](#rank_options)       |
| time_options     | `com.xiaomi.duckling.dimension.time.TimeOptions`       | `None`  | 时间配置，详见 [`time_options`](#time_options)       |
| numeral_options  | `com.xiaomi.duckling.dimension.numeral.NumeralOptions` | `None`  | 数值配置，详见 [`numeral_options`](#numeral_options) |

#### `rank_options`

使用对象的 `gen_rank_options` 方法可以构造 `rank_options` 参数：

```python
def gen_rank_options(
    self,
    winner_only=True,
    ranker=Ranker.NAIVE_BAYES,
    combination_rank=True,
    range_rank_ahead=False,
    nodes_limit=800,
    sequence1_end_prune=True
)
```

参数列表如下：

| 参数                | 类型     | 默认值               | 说明                                                |
| ------------------- | -------- | -------------------- | --------------------------------------------------- |
| winner_only         | `bool`   | `True`               | 是否只保留分数最高的结果                            |
| ranker              | `Ranker` | `Ranker.NAIVE_BAYES` | 排序使用的分类器，详见[排序](ranker/index.md)       |
| combination_rank    | `bool`   | `True`               | 使用组合排序                                        |
| range_rank_ahead    | `bool`   | `False`              | 先进行范围排序，再做打分                            |
| nodes_limit         | `int`    | `800`                | 解析中间节点的数量限制，在超出时会返回空的解析结果  |
| sequence1_end_prune | `bool`   | `True`               | 序列优化，减少 `明天的明天...` 类解析的中间节点生成 |

#### `time_options`

使用对象的 `gen_time_options` 方法可以构造 `time_options` 参数：

```python
def gen_time_options(
    self,
    reset_time_of_day=False,
    recent_in_future=True,
    always_in_future=True,
    inherit_grain_of_duration=False,
    parse_four_seasons=False,
    sequence=True,
    duration_fuzzy_on=True,
    duration_fuzzy_value=3,
    before_end_of_interval=False
)
```

参数列表如下：

| 参数                      | 类型   | 默认值  | 说明                                                         |
| ------------------------- | ------ | ------- | ------------------------------------------------------------ |
| reset_time_of_day         | `bool` | `False` | 上午是否总是需要指今天的上午，默认是未来一个上午             |
| recent_in_future          | `bool` | `True`  | 最近是向前计算还是向后计算，默认是未来                       |
| always_in_future          | `bool` | `True`  | 对于过去的日期是否取未来一年的日期                           |
| inherit_grain_of_duration | `bool` | `False` | 继承来自持续时间的粒度，比如 `三天后`，返回天级              |
| parse_four_seasons        | `bool` | `False` | 解析春夏秋冬四季，输出结果以节气为参照                       |
| sequence                  | `bool` | `True`  | 是否支持 `明天的明天...` 类的解析                            |
| duration_fuzzy_on         | `bool` | `True`  | 持续时间是否支持几个月/几天                                  |
| duration_fuzzy_value      | `int`  | `3`     | 持续时间模糊值的数量                                         |
| before_end_of_interval    | `bool` | `False` | 参考时间点 `ref `位于 `[a, b)` 之间时，`false` 取 `a >= ref` 的值，`true` 取 `a <= ref < b` 的值 |

#### `numeral_options`

使用对象的 `gen_numeral_options` 方法可以构造 `numeral_options` 参数：

```python
def gen_numeral_options(
    self,
    allow_zero_leading_digits=False,
    cn_sequence_as_number=False,
    dialect_support=False,
    kmg_support=True
)
```

参数列表如下：

| 参数                      | 类型   | 默认值  | 说明                          |
| ------------------------- | ------ | ------- | ----------------------------- |
| allow_zero_leading_digits | `bool` | `False` | 允许 `000318` 解析为 `318`    |
| cn_sequence_as_number     | `bool` | `False` | 允许 `一二三四` 解析为 `1234` |
| dialect_support           | `bool` | `False` | 允许识别方言，例如：`俩仨`    |
| kmg_support               | `bool` | `True`  | 允许识别类似 `10k` 为 `10000` |

## 示例

```python
from duckling_chinese import Duckling, DucklingDimension

duckling = Duckling()
context = duckling.gen_context()
options = duckling.gen_options(
    targets={
        DucklingDimension.ACT
    }
)

text = '倒数第一场'
answers = duckling.analyze(text, context=context, options=options)
entities = duckling.parse_entities(text, context=context, options=options)
```
