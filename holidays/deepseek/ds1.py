

def analyze_sector_performance(n=10):
    """
    分析各板块涨跌幅
    """
    concept_quotes = ak.stock_board_concept_name_em()  # 获取概念板块行情数据
    performance = concept_quotes.sort_values(by='涨跌幅', ascending=False)  # 按涨跌幅排序
    print("今日表现最好的概念板块：")
    print(performance.head(n))  # 打印前n个表现最好的板块
    return performance.head(n)  # 返回前n个表现最好的板块


def sh(str):
    if str.startswith('6'):
        return str + '.SH'
    elif str.startswith('3') or str.startswith('0'):
        return str + '.SZ'
    elif str.startswith('8'):
        return str + '.BJ'
    return str

def filter_df(df):
    """
    过滤掉科创板、创业板、北交所的股票，排除ST、名称中含Z,R的股票
    """
    df = df[df['最新价'] > 1]
    df = df[~df['名称'].str.startswith('ST')]
    df = df[~df['名称'].str.startswith('Z')]
    df = df[~df['名称'].str.startswith('*')]
    df = df[~df['名称'].str.startswith('R')]
    return df

def get_em_head_concept_stock():
    """
    获取概念板块关联的股票列表
    """
    sectors = analyze_sector_performance()  # 获取表现最好的板块
    stock_list = []  # 初始化股票列表
    for sector in sectors['板块名称']:  # 遍历每个板块
        concept_stocks = ak.stock_board_concept_cons_em(symbol=sector)  # 获取板块关联的股票列表
        stock_list.extend(concept_stocks)  # 添加到股票列表中
    all_stocks = sh_all(stock_list)  # 转换所有股票代码为标准格式
    filtered_stocks = filter_df(pd.DataFrame(all_stocks))  # 过滤掉不需要的股票
    return filtered_stocks  # 返回过滤后的股票列表

def select_stocks_before():
    print(f'开始盘前选股')

    trade_date = datetime.now().strftime('%Y%m%d')
    A.stock_list=get_em_head_stocks()
    all_stocks = list(filter(lambda symbol : not (symbol.startswith('30') or symbol.startswith('688') or symbol.startswith('8')), A.stock_list))
    all_stocks = sh_all(all_stocks)
    start_time = (datetime.strptime(trade_date,'%Y%m%d')-timedelta(120)).strftime('%Y%m%d')

    xtdata.download_history_data2(stock_list=all_stocks, period='1d', start_time=start_time, end_time=end_time)
    A.his_dict = xtdata.get_market_data_ex(stock_list=all_stocks, period='1d', start_time=start_time, end_time=trade_date)


    selected = []
    A.info_dict = dict()

    for stock in all_stocks:
        try:
            # ===== 基本筛选 =====
            # 排除ST、新股（上市<60天）
            info = xtdata.get_instrument_detail(stock)
            if'ST'in info['InstrumentName']: continue
            ipo_date = datetime.strptime(str(info['OpenDate']), '%Y%m%d')
            if (datetime.strptime(trade_date,'%Y%m%d') - ipo_date).days < 60: continue
            
            # 获取流通市值
            float_shares = info['FloatVolume']  # 流通股本(股)
            close = info['PreClose']
            float_mv = float_shares * close  / 10000/10000# 转换为亿元
            if float_mv >= 80: continue
            
            # 60日价格位置            
            his_df = A.his_dict[stock]
            ma60 = his_df['close'].rolling(60).mean().iloc[-1]
            if close > ma60 * 1.2: continue

            # 首板验证
            hist_20 = his_df.iloc[-20:]
            up_limit_days = hist_20['close'] >= hist_20['preClose'] * 1.095
            if up_limit_days.sum() > 0: continue# 20日内有涨停

            A.info_dict[stock]=info
            selected.append(stock)
        except Exception as e:
            print(f"处理{stock}时出错：{str(e)}")
            continue


