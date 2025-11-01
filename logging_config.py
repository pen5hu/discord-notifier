import logging
import sys


def setup_logging(log_level=logging.INFO):
    root_logger = logging.getLogger()

    if root_logger.handlers:
        return root_logger

    # ログレベル設定
    root_logger.setLevel(log_level)

    # 出力フォーマット設定
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d | %(message)s"
    )

    # コンソール出力（標準出力）
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    return root_logger
