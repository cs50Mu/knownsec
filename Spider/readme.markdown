### 20140920
- 实现基本逻辑，给定一个url可以进行广度优先爬行
- 遇到编码问题，`UnicodeEncodeError: 'ascii' codec can't encode characters in position 54-60: ordinal not in range(128)`，换用Python 3后解决

### 20140921
- 增加了爬虫深度功能

### 20140922
- 添加保存含有指定关键字的页面。一直纠结该怎么来写，最终只用了很简单的写法，类似`if '美女' in r.text`，由于Python2内部编码处理不是使用utf8,所以在Python2中需要先转换一下`if '美女'.decode('utf8') in r.text`，Python3中已经默认使用utf8编码了，所以可以直接用。也不知道正确的指定关键字的实现该怎么写，目前这么写貌似还好。
- 保存到数据库，待实现

### 20140926
- 理解了多线程中join功能，意思就是阻塞主进程，等线程结束后才继续执行join以后的语句。当然，join可以有一个timeout参数，意思就是阻塞多长时间的意思，主线程只等待你那么久，过了一定时间后，不管线程结束了没有，仍然继续执行后面的语句

### 20141004
- 实现了线程池。线程池的优点是线程可以重复利用，只要还有任务，线程就不会退出。不像一般的多线程，往往只是一个任务安排一个线程去执行，每个线程只执行一次就退出了，对线程的利用率太低。（不过，我转眼一想，那如果把真正干活的函数写成当任务为空的时候才退出，那不是也一样嘛。。）
- 实现的思想是：PoolManager类负责管理线程池，比如添加任务，启动线程，加入线程阻塞等；Worker类就是线程类了。线程之间使用队列来共享信息，Python中的Queue和deque等是线程安全的，所以不用考虑锁的问题
- 遇到的问题：一开始任务队列中的任务太少，根本不够线程池里的孩子们分的，所以分不到任务的线程就直接退出了。。解决办法是先爬一点url放进任务队列里。
- 待解决的问题：sqlite似乎不支持多线程
参考：

- [http://randomk.gitcafe.com/posts/2014/01/python-threadpool/](Python的线程池实现)
- [http://cleverdeng.iteye.com/blog/938193](Python实现线程池)
- [http://www.the5fire.com/python-thread-pool.html](python线程池)
- [http://www.cnblogs.com/goodhacker/p/3359985.html](线程池原理及python实现)
