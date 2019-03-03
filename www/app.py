# seagal 3.3 基本web骨架
import logging
from aiohttp import web
import asyncio


logging.basicConfig(level=logging.INFO)  # 问题的严重级别


def index(request):
    # 创建一个展示页面，一般单独写一个文件
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)  # 获取请求，首页响应，相应内容
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await loop.create_server(app_runner.server, '127.0.0.1', 9000)
    # web.run_app(app, host='127.0.0.1', port=9000,
    # access_log=logging.info('server started at http://127.0.0.1:9000...'))
    logging.info('server started at http://127.0.0.1:9000...')
    # 放在前边可以显示，在后边为啥不行，执行到了run_app，直接跳过了？
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

