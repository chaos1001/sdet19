import logging
import time
from pathlib import Path


def pytest_collection_modifyitems(items):
    # items 代表所有测试用例列表
    for item in items:
        # 用例名称
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # 用例路径
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def set_logger():
    fpath = Path(f"log/log-{int(time.time())}.txt")
    if not fpath.parent.exists():
        fpath.parent.mkdir(exist_ok=True, parents=True)

    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    file_haddler = logging.FileHandler(str(fpath), encoding="utf-8", mode='w')
    file_haddler.setLevel(logging.DEBUG)
    file_haddler.setFormatter(formatter)
    _logger.addHandler(file_haddler)
    return _logger


logger = set_logger()
