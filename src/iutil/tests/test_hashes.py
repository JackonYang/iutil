# -*- coding: utf-8 -*-
from iutil.hashes import (
    md5_for_file,
    md5_for_text,
)


def test_md5_for_file():
    assert isinstance(md5_for_file(__file__), str)


def test_md5_for_text():
    text = 'hello 中文'
    expect = '59304285079e2d7a3f2c30c8eead6179'

    assert md5_for_text(text) == expect
