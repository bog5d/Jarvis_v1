---
created: 2018-12-02 11:35:22
jarvis_ai_meta:
  key_people: []
  mood: 务实、探索
  summary: 王霞客为项目组技术选型，研究并总结了Python实现定时任务的多种方式，最终选定APScheduler框架。
  tagged_at: '2026-01-11 02:40:00'
  time_space:
    date: '2018-12-02'
    location: ''
source: https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/
tags:
- 技术选型
- APScheduler
- 定时任务
- 项目开发
- Python
updated: 2018-12-02 11:35:22
---

# Python 定时任务的实现方式

留着 有用 虽然自己也不会看 哈哈哈哈

* * *

# Python 定时任务的实现方式

[2016-09-27](https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/)

![unknown_filename.2.png](./_resources/Python_定时任务的实现方式.resources/unknown_filename.2.png)

# 背景

* * *

目前所在的项目组需要经常执行一些定时任务，之前都是用 Node.JS 的 [cron](https://github.com/ncb000gt/node-cron)来实现 schedule job。可是这次需要连接不同的 DB，而且实现的逻辑也有些许不同，于是选择使用 Python 的定时器。

# Python 实现定时任务

## 循环 sleep

这种方式最简单，在循环里面放入要执行的任务，然后 sleep 一段时间再执行

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | from datetime import datetime<br>import time<br>\# 每n秒执行一次<br>def timer(n):<br>    while True:<br>        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))<br>        time.sleep(n)<br>\# 5s<br>timer(5) |

这个方法的缺点是，只能执行固定间隔时间的任务，如果有定时任务就无法完成，比如早上六点半喊我起床。并且 sleep 是一个阻塞函数，也就是说 sleep 这一段时间，啥都不能做。

## threading模块中的Timer

threading 模块中的 Timer 是一个非阻塞函数，比 sleep 稍好一点，不过依然无法喊我起床。

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | from datetime import datetime<br>from threading import Timer<br>\# 打印时间函数<br>def printTime(inc):<br>    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))<br>    t = Timer(inc, printTime, (inc,))<br>    t.start()<br>\# 5s<br>printTime(5) |

Timer 函数第一个参数是时间间隔（单位是秒），第二个参数是要调用的函数名，第三个参数是调用函数的参数(tuple)

## 使用sched模块

sched 模块是 Python 内置的模块，它是一个调度（延时处理机制），每次想要定时执行某任务都必须写入一个调度。

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18 | import sched<br>import time<br>from datetime import datetime<br>\# 初始化sched模块的 scheduler 类<br>\# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。<br>schedule = sched.scheduler(time.time, time.sleep)<br>\# 被周期性调度触发的函数<br>def printTime(inc):<br>    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))<br>    schedule.enter(inc, 0, printTime, (inc,))<br>\# 默认参数60s<br>def main(inc=60):<br>    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，<br>    # 给该触发函数的参数（tuple形式）<br>    schedule.enter(0, 0, printTime, (inc,))<br>    schedule.run()<br>\# 10s 输出一次<br>main(10) |

sched 使用步骤如下：

（1）生成调度器：
s = sched.scheduler(time.time,time.sleep)
第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。

（2）加入调度事件
其实有 enter、enterabs 等等，我们以 enter 为例子。
s.enter(x1,x2,x3,x4)
四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，给触发函数的参数（注意：一定要以 tuple 给，如果只有一个参数就(xx,)）

（3）运行
s.run()
注意 sched 模块不是循环的，一次调度被执行后就 Over 了，如果想再执行，请再次 enter

# APScheduler定时框架

终于找到了可以每天定时喊我起床的方式了

[APScheduler](https://apscheduler.readthedocs.io/en/latest/userguide.html)是一个 Python 定时任务框架，使用起来十分方便。提供了基于日期、固定时间间隔以及 crontab 类型的任务，并且可以持久化任务、并以 daemon 方式运行应用。

使用 APScheduler 需要安装

|     |     |
| --- | --- |
| 1   | $ pip install apscheduler |

首先来看一个周一到周五每天早上6点半喊我起床的例子

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | from apscheduler.schedulers.blocking import BlockingScheduler<br>from datetime import datetime<br>\# 输出时间<br>def job():<br>    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))<br>\# BlockingScheduler<br>scheduler = BlockingScheduler()<br>scheduler.add\_job(job, 'cron', day\_of\_week='1-5', hour=6, minute=30)<br>scheduler.start() |

代码中的 BlockingScheduler 是什么呢？

BlockingScheduler 是 APScheduler 中的调度器，APScheduler 中有两种常用的调度器，BlockingScheduler 和 BackgroundScheduler，当调度器是应用中唯一要运行的任务时，使用 BlockingSchedule，如果希望调度器在后台执行，使用 BackgroundScheduler。

> 1. BlockingScheduler: use when the scheduler is the only thing running in your process

* BackgroundScheduler: use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
* AsyncIOScheduler: use if your application uses the asyncio module
* GeventScheduler: use if your application uses gevent
* TornadoScheduler: use if you’re building a Tornado application
* TwistedScheduler: use if you’re building a Twisted application
* QtScheduler: use if you’re building a Qt application

## APScheduler四个组件

APScheduler 四个组件分别为：触发器(trigger)，作业存储(job store)，执行器(executor)，调度器(scheduler)。

### 触发器(trigger)

包含调度逻辑，每一个作业有它自己的触发器，用于决定接下来哪一个作业会运行。除了他们自己初始配置意外，触发器完全是无状态的
APScheduler 有三种内建的 trigger:

> date: 特定的时间点触发
> interval: 固定时间间隔触发
> cron: 在特定时间周期性地触发

### 作业存储(job store)

存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存在数据库中。一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。调度器不能分享同一个作业存储。
APScheduler 默认使用 MemoryJobStore，可以修改使用 DB 存储方案

### 执行器(executor)

处理作业的运行，他们通常通过在作业中提交制定的可调用对象到一个线程或者进城池来进行。当作业完成时，执行器将会通知调度器。
最常用的 executor 有两种：

> ProcessPoolExecutor
> ThreadPoolExecutor

### 调度器(scheduler)

通常在应用中只有一个调度器，应用的开发者通常不会直接处理作业存储、调度器和触发器，相反，调度器提供了处理这些的合适的接口。配置作业存储和执行器可以在调度器中完成，例如添加、修改和移除作业。

## 配置调度器

APScheduler提供了许多不同的方式来配置调度器，你可以使用一个配置字典或者作为参数关键字的方式传入。你也可以先创建调度器，再配置和添加作业，这样你可以在不同的环境中得到更大的灵活性。

下面来看一个简单的 BlockingScheduler 例子

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | from apscheduler.schedulers.blocking import BlockingScheduler<br>from datetime import datetime<br>def job():<br>    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))<br>\# 定义BlockingScheduler<br>sched = BlockingScheduler()<br>sched.add\_job(job, 'interval', seconds=5)<br>sched.start() |

上述代码创建了一个 BlockingScheduler，并使用默认内存存储和默认执行器。(默认选项分别是 MemoryJobStore 和 ThreadPoolExecutor，其中线程池的最大线程数为10)。配置完成后使用 start() 方法来启动。

如果想要显式设置 job store(使用mongo存储)和 executor 可以这样写：

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29 | from datetime import datetime<br>from pymongo import MongoClient<br>from apscheduler.schedulers.blocking import BlockingScheduler<br>from apscheduler.jobstores.memory import MemoryJobStore<br>from apscheduler.jobstores.mongodb import MongoDBJobStore<br>from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor<br>\# MongoDB 参数<br>host = '127.0.0.1'<br>port = 27017<br>client = MongoClient(host, port)<br>\# 输出时间<br>def job():<br>    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))<br>\# 存储方式<br>jobstores = {<br>    'mongo': MongoDBJobStore(collection='job', database='test', client=client),<br>    'default': MemoryJobStore()<br>}<br>executors = {<br>    'default': ThreadPoolExecutor(10),<br>    'processpool': ProcessPoolExecutor(3)<br>}<br>job\_defaults = {<br>    'coalesce': False,<br>    'max\_instances': 3<br>}<br>scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job\_defaults=job\_defaults)<br>scheduler.add\_job(job, 'interval', seconds=5, jobstore='mongo')<br>scheduler.start() |

在运行程序5秒后，第一次输出时间。
在 MongoDB 中可以看到 job 的状态

![unknown_filename.1.png](./_resources/Python_定时任务的实现方式.resources/unknown_filename.1.png)

## 对 job 的操作

### 添加 job

添加job有两种方式：

1. add\_job()

* scheduled\_job()

第二种方法只适用于应用运行期间不会改变的 job，而第一种方法返回一个[apscheduler.job.Job](https://apscheduler.readthedocs.io/en/latest/modules/job.html#apscheduler.job.Job) 的实例，可以用来改变或者移除 job。

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | from apscheduler.schedulers.blocking import BlockingScheduler<br>sched = BlockingScheduler()<br>\# 装饰器<br>@sched.scheduled\_job('interval', id='my\_job\_id', seconds=5)<br>def job\_function():<br>    print("Hello World")<br>\# 开始<br>sched.start() |

@sched.scheduled\_job() 是 Python 的装饰器。

### 移除 job

移除 job 也有两种方法：

1. remove\_job()

* job.remove()

remove\_job 使用 jobID 移除
job.remove() 使用 add\_job() 返回的实例

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | job = scheduler.add\_job(myfunc, 'interval', minutes=2)<br>job.remove()<br>\# id<br>scheduler.add\_job(myfunc, 'interval', minutes=2, id='my\_job\_id')<br>scheduler.remove\_job('my\_job\_id') |

### 暂停和恢复 job

暂停一个 job：

|     |     |
| --- | --- |
| 1<br>2 | apscheduler.job.Job.pause()<br>apscheduler.schedulers.base.BaseScheduler.pause\_job() |

恢复一个 job：

|     |     |
| --- | --- |
| 1<br>2 | apscheduler.job.Job.resume()<br>apscheduler.schedulers.base.BaseScheduler.resume\_job() |

希望你还记得 apscheduler.job.Job 是 add\_job() 返回的实例

### 获取 job 列表

获得可调度 job 列表，可以使用[get_jobs()](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.get_jobs) 来完成，它会返回所有的 job 实例。

也可以使用[print_jobs()](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.print_jobs) 来输出所有格式化的 job 列表。

### 修改 job

除了 jobID 之外 job 的所有属性都可以修改，使用 apscheduler.job.Job.modify() 或者 modify\_job() 修改一个 job 的属性

|     |     |
| --- | --- |
| 1<br>2 | job.modify(max\_instances=6, name='Alternate name')<br>modify\_job('my\_job\_id', trigger='cron', minute='\*/5') |

### 关闭 job

默认情况下调度器会等待所有的 job 完成后，关闭所有的调度器和作业存储。将 wait 选项设置为 False 可以立即关闭。

|     |     |
| --- | --- |
| 1<br>2 | scheduler.shutdown()<br>scheduler.shutdown(wait=False) |

### scheduler 事件

scheduler 可以添加事件监听器，并在特殊的时间触发。

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | def my\_listener(event):<br>    if event.exception:<br>        print('The job crashed :(')<br>    else:<br>        print('The job worked :)')<br>\# 添加监听器<br>scheduler.add\_listener(my\_listener, EVENT\_JOB\_EXECUTED \| EVENT\_JOB\_ERROR) |

## trigger 规则

### [date](https://apscheduler.readthedocs.io/en/latest/modules/triggers/date.html)

最基本的一种调度，作业只会执行一次。它的参数如下：

* run\_date (datetime|str) – the date/time to run the job at
* timezone (datetime.tzinfo|str) – time zone for run\_date if it doesn’t have one already

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12 | from datetime import date<br>from apscheduler.schedulers.blocking import BlockingScheduler<br>sched = BlockingScheduler()<br>def my\_job(text):<br>    print(text)<br>\# The job will be executed on November 6th, 2009<br>sched.add\_job(my\_job, 'date', run\_date=date(2009, 11, 6), args=\['text'\])<br>sched.add\_job(my\_job, 'date', run\_date=datetime(2009, 11, 6, 16, 30, 5), args=\['text'\])<br>sched.add\_job(my\_job, 'date', run\_date='2009-11-06 16:30:05', args=\['text'\])<br>\# The 'date' trigger and datetime.now() as run\_date are implicit<br>sched.add\_job(my\_job, args=\['text'\])<br>sched.start() |

### [cron](https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html)

* year (int|str) – 4-digit year
* month (int|str) – month (1-12)
* day (int|str) – day of the (1-31)
* week (int|str) – ISO week (1-53)
* day\_of\_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
* hour (int|str) – hour (0-23)
* minute (int|str) – minute (0-59)
* second (int|str) – second (0-59)
* start\_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
* end\_date (datetime|str) – latest possible date/time to trigger on (inclusive)
* timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

表达式:

![unknown_filename.png](./_resources/Python_定时任务的实现方式.resources/unknown_filename.png)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12 | from apscheduler.schedulers.blocking import BlockingScheduler<br>def job\_function():<br>    print("Hello World")<br>\# BlockingScheduler<br>sched = BlockingScheduler()<br>\# Schedules job\_function to be run on the third Friday<br>\# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00<br>sched.add\_job(job\_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')<br>\# Runs from Monday to Friday at 5:30 (am) until 2014-05-30 00:00:00<br>sched.add\_job(job\_function, 'cron', day\_of\_week='mon-fri', hour=5, minute=30, end\_date='2014-05-30')<br>sched.start() |

### [interval](https://apscheduler.readthedocs.io/en/latest/modules/triggers/interval.html)

参数：

* weeks (int) – number of weeks to wait
* days (int) – number of days to wait
* hours (int) – number of hours to wait
* minutes (int) – number of minutes to wait
* seconds (int) – number of seconds to wait
* start\_date (datetime|str) – starting point for the interval calculation
* end\_date (datetime|str) – latest possible date/time to trigger on
* timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12 | from datetime import datetime<br>from apscheduler.schedulers.blocking import BlockingScheduler<br>def job\_function():<br>    print("Hello World")<br>\# BlockingScheduler<br>sched = BlockingScheduler()<br>\# Schedule job\_function to be called every two hours<br>sched.add\_job(job\_function, 'interval', hours=2)<br>\# The same as before, but starts on 2010-10-10 at 9:30 and stops on 2014-06-15 at 11:00<br>sched.add\_job(job\_function, 'interval', hours=2, start\_date='2010-10-10 09:30:00', end\_date='2014-06-15 11:00:00')<br>sched.start() |

Measure
Measure