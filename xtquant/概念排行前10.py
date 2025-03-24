import akshare as ak
import pandas as pd

def analyze_sector_performance(n=10):
    """
    分析各板块涨跌幅
    """
    concept_quotes = ak.stock_board_concept_name_em()  # 获取概念板块行情数据
    performance = concept_quotes.sort_values(
        by="涨跌幅", ascending=False
    )  # 按涨跌幅排序
    print("今日表现最好的概念板块：")
    print(performance.head(n))  # 打印前n个表现最好的板块
    return performance.head(n)  # 返回前n个表现最好的板块


def analyze_stock_list(n=10):
    stock_board_concept_hist_min_em_df = ak.stock_board_concept_hist_min_em(
        symbol="长寿药", period="1"
    )
    print(stock_board_concept_hist_min_em_df)


def filter_df(df):
    """
    过滤掉科创板、创业板、北交所的股票，排除ST、名称中含Z,R的股票
    """
    df = df[df["最新价"] > 1]
    df = df[~df["名称"].str.startswith("ST")]
    df = df[~df["名称"].str.startswith("Z")]
    df = df[~df["名称"].str.startswith("*")]
    df = df[~df["名称"].str.startswith("R")]
    return df


def get_em_head_concept_stock():
    """
    获取概念板块关联的股票列表
    """
    sectors = analyze_sector_performance()  # 获取表现最好的板块
    stock_list = []  # 初始化股票列表
    for sector in sectors["板块名称"]:  # 遍历每个板块
        concept_stocks = ak.stock_board_concept_cons_em(
            symbol=sector
        )  # 获取板块关联的股票列表
        stock_list.extend(concept_stocks)  # 添加到股票列表中
    performance = stock_list

    # print(performance)
    # all_stocks = sh_all(stock_list)  # 转换所有股票代码为标准格式
    # filtered_stocks = filter_df(pd.DataFrame(all_stocks))  # 过滤掉不需要的股票
    # return filtered_stocks  # 返回过滤后的股票列表

if __name__ == "__main__":
    get_em_head_concept_stock()