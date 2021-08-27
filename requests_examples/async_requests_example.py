from requests_html import AsyncHTMLSession
import time


asession = AsyncHTMLSession()


async def get_delay_1():
    r = await asession.get('https://httpbin.org/delay/1')
    return r


async def get_delay_2():
    r = await asession.get('https://httpbin.org/delay/2')
    return r


async def get_delay_5():
    r = await asession.get('https://httpbin.org/delay/5')
    return r


t1 = time.perf_counter()

results = asession.run(get_delay_1, get_delay_2, get_delay_5)

for result in results:
    response = result.html.url
    print(response)

t2 = time.perf_counter()

print(f'Asynchronous execution took {t2 - t1} seconds')
