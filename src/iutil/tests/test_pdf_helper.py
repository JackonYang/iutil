# -*- coding: utf-8 -*-
import os

from iutil.pdf_helper import (
    url2pdf,
)


FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def test_url2pdf_ok():
    # 公众号开通了流量主，两周赚了 47.63 元广告费
    url = 'https://mp.weixin.qq.com/s/LUavw-4dc1UgB1xiM8UT5Q'
    expect = '94be36e5d5615ac1f6af5e3dc396a44b.pdf'  # filename

    res, filename = url2pdf(url, out_dir=FILE_PATH)

    assert res == 0
    assert filename == os.path.join(FILE_PATH, expect)
