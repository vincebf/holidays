# 参数
account_id = "xxxx"  # 账号ID
mini_qmt_path = r"D:\国金证券QMT交易端\userdata_mini"  # mini_qmt 路径
file_path = r"D:\new_tdx\sign.txt"  # 预警文件路径
interval = 1  # 轮询时间(秒)
buy_sign = "KDJ买入条件选股"  # 买入信号
sell_sign = "KDJ卖出条件选股"  # 卖出信号


### 按金额买卖
def buy_event(params):
    """买入事件"""
    stock = params.get("stock")
    return {
        "amount": 100000,
        "price": stock.get("price"),  # 如果是市价，则设置-1
        "type": "限价",  # 市价，限价
    }


### 卖全仓
def sell_event(params):
    """卖出事件"""
    stock = params.get("stock")
    position = params.get("position")
    return {
        "size": position.can_use_volume,  # 卖全仓
        "price": stock.get("price"),  # 如果是市价，则设置-1
        "type": "限价",  # 市价，限价
    }
