# -*- coding: utf-8 -*-
import os

from iutil.pdf_helper import (
    url2pdf,
)

from iutil.tests.configs import FAST_MODE


FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def test_url2pdf_ok():
    if FAST_MODE:
        return

    # 公众号开通了流量主，两周赚了 47.63 元广告费
    url = 'https://mp.weixin.qq.com/s/LUavw-4dc1UgB1xiM8UT5Q'
    expect = '94be36e5d5615ac1f6af5e3dc396a44b.pdf'  # filename

    res, filename = url2pdf(url, out_dir=FILE_PATH)

    assert res == 0
    assert filename == os.path.join(FILE_PATH, expect)


def test_url2pdf_image():
    if FAST_MODE:
        return

    # my blog, no referrer check in images
    url = 'http://jackonyang.github.io/blog/2013/05/25/javascript-primer/'
    expect = '577a8b0d2cb6ec2c54683db44fa29db7.pdf'  # filename

    res, filename = url2pdf(url, out_dir=FILE_PATH)

    assert res == 0
    assert filename == os.path.join(FILE_PATH, expect)
