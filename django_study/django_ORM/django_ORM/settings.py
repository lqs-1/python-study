"""
Django settings for django_ORM project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目路径，manager所在的目录
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f5l32ids$d7bprgq!y6eedltc8$8-(!ny%w!$%&)4iidfxpo)a'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试打开
DEBUG = True

# 允许访问的主机
ALLOWED_HOSTS = ["*"]

# Application definition

# 功能注册
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册应用
    'user',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 一级url配置文件的位置
ROOT_URLCONF = 'django_ORM.urls'

# 模板文件存放位置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_ORM.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# 数据库配置
# 使用mysql需要安装pymysql库
'''
django添加事务：
    方式一(全局开启功能)：settings.py中的DATABASES添加一项：ATOMIC_REQUEST = True,
    
    方式二(装饰器局部开启功能):from django.db import transaction
                     在方法上：@transaction.atomic，表示这个方法具有事务功能
                     如果使用的是全局开启方式，那么可以使用@transaction.non_atomic_requests, 这个装饰器可以局部上某个方法不开启事务功能
    
    方式一和方式二使用方法(在try...exception中使用)：
        创建保存点
        save_id = transaction.savepoint()
        回滚到保存点()
		transaction.savepoint_rollback(save_id)
		主动提交（相当于 对象.save()）
		transaction.savepoint_commit(save_id) 
		清除保存点
		transaction.clean_savepoints()  清除保存点
		
	方式三：
	    不需要装饰器，也不需要配置文件配置
	    在需要回滚的try...exception中使用,不用没有异常就自动提交，有异常自动回滚：
	        with transaction.atomic():
	            这个地方写语句

    
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test1',
        'USER': 'lqs',
        'PASSWORD': 'lqs',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # "ATOMIC_REQUESTS": True  # 全局开启事务

    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# 文字语言设置
LANGUAGE_CODE = 'zh-hans'
# 时间区域配置
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# 静态资源的前缀，或者别名
STATIC_URL = 'static/'
# 静态资源所在的位置，可以有多个
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 访问前缀或者别名
MEDIA_URL = 'media'
# 媒体文件的存放位置，用户上传的
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



'''
日志配置，多数抄别人的
    在python的文件中使用日志：
        import logging
        logger = logging.getLogger('lqs')  : 名字和配置的名字一样就可以
        
        logger.warning("你好")
        logger.error("你好")
        logger.info("你好")
        logger.debug("你好")
        logger.critical("你好")
'''

log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

import time

LOGGING = {
    # 版本
    'version': 1,
    # 是否禁用默认的日志管理
    'disable_existing_loggers': True,

    # 输出格式
    'formatters': {
        # 日志标准格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        # 日志简单格式
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    # 过滤，一般不设置
    'filters': {
    },

    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 lqs 处理所有类型的日志， 默认调用
        'lqs': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
        },
    }
}














'''
    分词器使用：
        安装全文检索框架：pip install haystack
        安装搜索引擎：pip install whoosh
        安装jieba分词器: pip install jieba
        
        whoosh路径：....../site-packages/whoosh
        haystack路径：....../site-packages/haystack
        haystack默认引擎路径：....../site-packages/haystack/backends
        
        
        第一步：
        在settings文件中配置：
            注册应用haystack
            HAYSTACK_CONNECTIONS = {
                'default': {
                    # 配置使用whoosh引擎，cn版本是我们加了jieba分词器之后的whoosh引擎，原始版本不能删除
                    'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
                    # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
                    # 检索文件路径, 自动生成
                    'PATH': os.path.join(BASE_DIR, 'whoosh.index')
                },
            }
            # 当增删查改数据时候自动生成索引
            HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
            
        第二步：
        编写索引类：
            索引类定义在需要进行所搜的应用模块下面
            索引类名：模型类名+Index, 如（GoodsSKUIndex）
            
            # 定义索引类
            from haystack import indexes
            from .models import GoodsSKU
            
            # 指定对于某个类的某些数据建立索引
            # 索引类名格式： 模型类名+Index
            class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):
                # 索引类里面的索引字段
                # use_template：指定根据表中的哪些字段建立索引文件， 把说明放在一个文件中
                text = indexes.CharField(document=True, use_template=True)
                # 返回模型类
                def get_model(self):
                    # 返回你的模型类
                    return GoodsSKU
                # 建立索引的数据
                def index_queryset(self, using=None):
                    return self.get_model().objects.all()
                    
        第三步：
        建立索引文件
            在templates文件夹下创建search/indexes/数据模型类所属的应用名/数据模型类类名小写_text.txt
            在这个txt文件中书写指定根据表中的哪些字段建立索引
            {{object.name}}  # 根据商品名称建立索引
            {{object.desc}}  # 根据商品描述建立索引
            {{object.goods.detail}}  # 根据商品详情建立索引
            
        第四步：
        python manager.py rebuild_index  生成检索文件
        
        第五步：
        配置haystack路由: 
            path('search', include('haystack.urls')),  # 配置全文检索框架路由
            
        第六步：
        在search/indexes/下创建一个search.html文件，来展示结果
            query对象：搜索的关键字
            搜索的关键字{{ query }}<br>
            
            page对象：搜索结果，便利出来通过object.xxx使用，有以下作用
            遍历对象
            {% for item in page %}
                {{ item.object.name }}
            {% endfor %}
            判断上一页下一页：
            {% if page.has_previous %}<a href="/search?q={{ query }}&page={{ page.previous_page_number }}">下一页></a>{% endif %}
            {% if page.has_next %}<a href="/search?q={{ query }}&page={{ page.next_page_number }}">下一页></a>{% endif %}
            判断是否是当前页：
            {% if pindex == page.number %}
            
            {#Page对象可以便历出来，便历的都是SearchResult实例对象，里面的object供我们使用#}
            
            分页的Paginator对象{{ paginator }}<br>
           {% for pindex in paginator.page_range %}
                {% if pindex == page.number %}
                    <a href="/search?q={{ query }}&page={{ pindex }}" class="active">{{ pindex }}</a>
                {% else%}
                    <a href="/search?q={{ query }}&page={{ pindex }}">{{ pindex }}</a>
                {% endif %}
            {% endfor %}
            
            
        第七步：
        更换分词器（jieba）：
        在/site-packages/haystack/backends下创建ChineseAnalyzer.py，内容网上搜索
        在/site-packages/haystack/backends下复制一份whoosh_backend.py并且改名为whoosh_cn_backend.py,然后修改里面analyzer=ChineseTokenizer(),先引入，再使用
        在配置文件中修改使用的whoosh引擎为whoosh_cn_backend
        
        重新生成检索文件：python manager.py rebuild_index

'''

