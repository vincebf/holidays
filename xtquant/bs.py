import tdxtrader
from config import config



tdxtrader.start(
    account_id=account_id,
    mini_qmt_path=mini_qmt_path,
    file_path=file_path,
    interval=interval,
    buy_sign=buy_sign,
    sell_sign=sell_sign,
    buy_event=buy_event,
    sell_event=sell_event,
    cancel_after=10 # 10秒未成交则撤单
)


```

### 按金额买卖

```python
def buy_event(params):
    '''买入事件'''

    stock = params.get('stock')

    return { 
        'amount': 100000, 
        'price': stock.get('price'), # 如果是市价，则设置-1
        'type': '限价', # 市价，限价
    }

def sell_event(params):
    '''卖出事件'''

    stock = params.get('stock')

    return { 
        'amount': 100000, # 卖全仓
        'price': stock.get('price'),  # 如果是市价，则设置-1
        'type': '限价' # 市价，限价
    }
```

### 使用当前持仓判断是否买入

```python
def buy_event(params):
    '''买入数量'''

    stock = params.get('stock')
    position = params.get('position')

    if position is None:
        return { 
            'amount': 100000, 
            'price': stock.get('price'), # 如果是市价，则设置-1
            'type': '限价', # 市价，限价
        }
    else:
        return None

def sell_event(params):
    '''卖出数量'''

    stock = params.get('stock')

    return { 
        'amount': 100000, # 卖全仓
        'price': stock.get('price'),  # 如果是限价，则设置价格
        'type': '限价' # 市价，限价
    }


### 多个买入信号/多个卖出信号
import tdxtrader
# 参数
account_id = 'xxxx' # 账号ID
mini_qmt_path = r'D:\国金证券QMT交易端\userdata_mini' # mini_qmt 路径
file_path = r'D:\new_tdx\sign.txt' # 预警文件路径
interval = 1 # 轮询时间(秒)
buy_sign = ['KDJ买入条件选股', 'MACD买入条件选股'] # 多个买入信号
sell_sign = ['KDJ卖出条件选股', 'MACD卖出条件选股'] # 多个卖出信号

def buy_event(params):
    '''买入事件'''
    stock = params.get('stock')
    return { 
        'size': 200, 
        'price': -1, # 如果是限价，则设置价格
        'type': '市价', # 市价，限价
    }

def sell_event(params):
    '''卖出事件'''
    stock = params.get('stock')
    position = params.get('position')
    return { 
        'size': position.can_use_volume, # 卖全仓
        'price': -1,  # 如果是限价，则设置价格
        'type': '市价' # 市价，限价
    }



tdxtrader.start(
    account_id=account_id,
    mini_qmt_path=mini_qmt_path,
    file_path=file_path,
    interval=interval,
    buy_sign=buy_sign,
    sell_sign=sell_sign,
    buy_event=buy_event,
    sell_event=sell_event,
    cancel_after=10, # 10秒未成交则撤单,
    wechat_webhook_url='你的webhook_url' # 企业微信机器人webhook url
)
