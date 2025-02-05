from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.edge.options import Options

edge_options = Options()
edge_options.add_argument("--disable-extensions")  # 禁用扩展
edge_options.add_argument("--disable-popup-blocking")  # 允许弹窗
# edge_options.add_argument("headless")  # 可选：无头模式

driver = webdriver.Edge(options=edge_options)
driver.get(
    "https://bfda.21tb.com/els/html/courseStudyItem/courseStudyItem.learn.do?courseId=ce70c556e72546cfa6ace97f27171824&courseType=NEW_COURSE_CENTER&vb_server=http%3A%2F%2F21tb-video.21tb.com&eln_session_id=elnSessionId.43c3411d49c0474080f74f24c9b66dc1"
)

# 触发弹窗的操作（例如点击按钮）
# driver.find_element("id", "trigger-alert").click()

try:
    # 等待弹窗出现，最多等待10秒
    WebDriverWait(driver, 100000).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("弹窗内容:", alert.text)

    # 根据需求选择接受（确定）或取消（关闭）
    alert.accept()  # 点击“确定”
    # alert.dismiss()  # 点击“取消”
except TimeoutException:
    print("未检测到弹窗")
except NoAlertPresentException:
    print("弹窗意外未出现")

driver.quit()
