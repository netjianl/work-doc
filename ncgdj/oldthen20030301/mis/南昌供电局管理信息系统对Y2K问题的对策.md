#南昌供电局管理信息系统对Y2K问题的对策

## 一. 背景
众所周知，Y2K问题是由于某些计算机硬件或软件使用了2位数字表示年份，在公元2000年来临时，无法正确区分2000年和1900/0年，从而可能产生经济损失。

南昌供电局管理信息系统从1998年3月开始建设，已经建立起一个覆盖全局的、综合性的网络环境。在软件方面，已经开发完成并投入使用的有办公自动化系统、生产管理子系统、行政管理子系统、物资管理子系统、项目管理子系统、MAPINFO的输电线路管理子系统、配电线路的GIS子系统等。在各个子系统的使用过程中已经输入、生成了大量的数据。对于‘三分技术、七分数据’的管理信息系统而言，如何在世纪之交保护这些数据不受Y2K问题侵扰，保证管理信息系统及其数据的正确性、完整性是一项重要的任务。

## 二. 管理信息系统中可能遭受的Y2K问题   
1. 机器时钟
机器时钟包括了硬件内部所有的晶振器和COMS内部时钟。如果某台机器时钟不能正确区分出2000年，运行于这台机器的所有软件可能都会受到影响。

2. 操作系统时钟
操作系统是应用程序的基础，如果某种操作系统不能正确区分出2000年，运行于这个操作系统的所有应用程序都可能受到影响。

3. 数据库服务器日期存储
数据库纪录了管理信息系统的绝大部分数据，如果其日期存储格式不能正确区分出2000年，整个管理信息系统都会受到影响。

4. 管理信息系统软件
管理信息系统软件是人机交互的重要方式，如果某个管理信息系统软件不能争 取区分出2000年，这个子系统将会受到影响。

## 三. 南昌供电局管理信息系统对Y2K问题的对策
南昌供电局管理信息系统在开始建设的时候就非常重视Y2K问题的存在和注重防范其可能爆发带来的严重损失，并且一直密切关注Y2K问题的发展。所采取的主要对策有：

1、购置机器
在购置机器时均选择已经解决了Y2K问题的机型，并利用先进软件对绝大部分机器进行了Y2K测试。

2、选择操作系统
选择购买已经解决Y2K问题的操作系统，并对以前的操作系统进行相应的升级或者使用Y2K补丁程序解决。

3、选择数据库平台
选择购买已经解决Y2K问题的数据库平台，升级早期系统使用的平台或者开发新的系统。

4、应用软件
在和软件开发公司交涉时，南昌供电局就把Y2K问题明确的提出，并和软件开发公司商定，所有交付使用的软件均应不存在Y2K问题。

5、数据备份
数据备份是防止数据丢失的重要措施，同样，对于Y2K问题可能带来的任何数据度丢失，作为最后的补救措施，都可以通过数据备份来解决，通过把数据恢复到99/12/31日的原状，再进行相应的措施。

## 四. 南昌供电局管理信息系统数据分布概述及相应的数据备份策略
南昌供电局现有数据主要分布在3台服务器中、分别是：
### 1. WINDOWS NT主控域服务器
主要包括以下主要数据：
WINDOWS NT目录信息：主要是南昌供电局管理信息系统使用者的账号等数据。使用的是WINDOWS NT的系统目录管理。
备份策略：使用NT的目录备份实用程序进行备份。

NOTES数据库：主要包括办公自动化系统的所有数据。使用的是LOTUS的DOMINO管理数据。

备份策略：复制notes数据库文件。

WEB数据库：包含了南昌供电局主页的所有文件。使用的是IIS4.0管理数据。

备份策略：使用文件拷贝方式备份。

### 2. UNIX下的ORACLE数据库服务器
主要包括了生产、行政、物资、项目、输电线路子系统中的所有数据。使用的是ORACLE数据库。

### 3. WINDOWS NT下的配电线路GIS系统服务器
这台服务器包括了配电线路GIS系统的所有数据。使用了ORACLE数据库。

备份策略：使用ORACLE备份实用程序EXPORT/IMPORT进行数据备份。
