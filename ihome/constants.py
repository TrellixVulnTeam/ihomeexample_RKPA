# coding:utf-8 


# 图片验证码的redis有效期, 单位：秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的redis有效期，单位：秒
SMS_CODE_REDIS_EXPIRES = 300

#发送短信验证码的间隔，单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 最大登录错误请求次数
LOGIN_ERROR_MAX_TIMES = 10

# 登录错误限制的时间
LOGIN_ERROR_FORBID_TIME = 600


# 七牛的域名
QINIU_URL_DOMAIN = "http://pztnjwcqu.bkt.clouddn.com/"

# 城区信息的缓存时间, 单位：秒
AREA_INFO_REDIS_CACHE_EXPIRES = 7200

#首页展示最多的房屋数量
HOME_PAGE_MAX_HOSUE = 5

# 首页房屋数据的Redis缓存时间，单位：秒
HOME_PAGE_DATA_REDIS_EXPIRES = 7200
