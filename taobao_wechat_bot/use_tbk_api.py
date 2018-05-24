# -*- coding: utf-8 -*-
import top.api

appkey = '24901549'
secret = 'eb873fc3f35c86f25925052220e8c4fe'
adzone_id = '624564913'


# 获取淘宝客商品优惠券
def get_tbk_coupon(keyword):
    req = top.api.TbkDgItemCouponGetRequest()
    req.set_app_info(top.appinfo(appkey, secret))

    req.adzone_id = adzone_id
    # 商品的平台：1为PC端，2为无线端，默认为1
    req.platform = 2
    # 商品的类目ID
    req.cat = "16,18"
    # 每页返回的商品数量
    req.page_size = 5
    # 商品的搜索词
    req.q = keyword
    # 返回商品的页数
    req.page_no = 1
    try:
        resp = req.getResponse()
        for r in resp['tbk_dg_item_coupon_get_response']['results']['tbk_coupon']:
            coupon_url = r['coupon_click_url']
            coupon_text = r['title']
            print(">>>商品标题：", coupon_text)
            print(">>>优惠券链接：", coupon_url)
            generate_ttoken(coupon_url, coupon_text)
            print()
    except Exception as e:
        print(e)


# 生成淘口令
def generate_ttoken(url, text):
    req = top.api.TbkTpwdCreateRequest()
    req.set_app_info(top.appinfo(appkey, secret))

    req.text = text
    req.url = url
    req.logo = "http://ozuz7s0lj.bkt.clouddn.com/avas.webp"
    try:
        resp = req.getResponse()
        print(resp['tbk_tpwd_create_response']['data']['model'])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_tbk_coupon('python')
