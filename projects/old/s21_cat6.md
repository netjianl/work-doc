

#### 2019.09.06
**郑达**    这是s21 版本：1.23
**郑达**    这是s21 版本：1.24
- tr069 修复升级没有后台运行导致回包阻塞（封远钊）
- 将Home页面的顶部提示信息改成默认为隐藏（董锡文）
- 将系统设置和系统升级两个文件夹下所有页面上的js代码分离成独立文件（巢丽媛）
- 将VPN文件夹下所有页面的js代码分离成独立的js文件方便后期压缩（巢丽媛）
#### 2019.09.05
**郑达**    这是s21 版本：1.22 
#### 2019.09.03
**eddy**  product_tool_onlyForMT7621 
**封远钊**  附件是 V1.19   合了 宽翼  0823 版本的升级包
#### 2019.09.02
**喻潇** 针对1.19版本；最近几天发现的问题
#### 2019.08.31
**陈良**  今天测试发现0813的版本有重大问题，有个进程的CPU占用率过高，导致模块的温度会一直增加，最终模块会死机。
#### 2019.08.29
**陈良**  VOIP的短号码设置菜单需要做一些调整，具体调整请参考以下截图和附件的客户需求表。为空的部分看能不能先隐藏掉，因为目前这些功能是不支持的。
#### 2019.08.28
**封远钊** V1.19版本，主要修改如下：      1、root 密码使用随机生成方案      2、tr069 补全 VOIP 节点 
**封远钊**  测试程序修改：
1. VOIP 三方通话功能修改
2. 合入VOIP 授权程序
3. PCI  SCAN 功能
4. ECGI 锁修改为PCI 锁小区
5. tr069 增加 PCI SCAN 节点，以及修复部分节点
#### 2019.08.27
**封远钊**  S21  VOIP 的授权程序会将 授权码　写入校准区　的 e100~ e165 位置（授权码最大长度１０１字节　即　0x65 ）所以　校准区的　e100~ e200　目前保留出给ＶＯＩＰ的授权使用
#### 2019.08.26
**陈良**  今天和客户确认了以下需求需要更改:
- 一、三方通话：
  - 1.當Callee： A Call B(待測對象:3406)之後，B按Flash之後再撥打給C，C再接起來。
  - 2.當Caller： A(待測對象:3406) Call B之後，A按Flash之後再撥打給C，C再接起來。
        此時即表示滿足測試三方通話的前置條件，之後再進行切換測試。
         Flash + 1 (掛掉當前Active的通話，轉換到等待插播的電話)           ///此功能客户不做要求，可以做可以不做；
        Flash + 2 (保留當前Active的通話，切換至另一通等待插播的電話)   ///此功能客户不做要求，可以做可以不做；
        Flash  (開啟三方通話，此時三方都能互相聽到對方的聲音)
- 二、 Call Waiting:
        A call B,接通电话以后，C呼B；
      此时：B长按 flash按键，会挂断B和A的通话，接通C的电话；
                 B 短按 flash按键，会接通B和C的通话，保持住A，再短按flash按键进行切换A和C通话。
- 三、    将锁ECGI换成锁PCI, 并增加 PCI SCAN
        在WEBUI上做个SCAN按钮，点击后，CPE会做邻区PCI扫描，然后在WEBUI上显示出邻区的PCI列表，因为只有在connect状态下才会有邻区信息，因此：
        1 ，如果CPE没有入网，SCAN按钮是灰色的，不能做扫描；
        2，当CPE入网后，点击SCAN按钮后，确保CPE工作在connect态，再开始查询当前的邻区信息，并在WEBUI页面上显示出服务小区和邻区PCI和RSRP列表。 
        3，列表最大支持显示6个PCI,以RSRP的值降序排列，信号最好的小区排前面.
        4，支持TR069上报，最大上报6个邻区信息，在TR069获取该参数时重新扫描一次再上报。
**封远钊**  调试验证  与ACS 服务器双向认证  ok， 升级ok  的临时版本
#### 2019.08.25
**陈良** TR069的问题需要优先进行修复，我们需要尽快完成TR069的测试，
#### 2019.08.23
**喻潇**  s21-bug总结-20190823；其中新增TR069和网页菜单配置控制的一些需求；请修改 另外，VOIP尝试在深圳使用阿里云测试，基本属于无法测试，打通的概率极低；  
**封远钊**  把模块升级bin注：升级这个bin 大概需要5 -6 分钟 ，才能升级完， 所以请耐心等待设备自动重启
#### 2019.08.21
**喻潇** 附件是烧片文件、网页升级文件、生产测试配置、校验参数；网页升级文件、生产测试配置；经过简单验证有线无线功能；可以先用于烧片生产，后期还需要升级才能发货。  
#### 2019.08.19
**封远钊**  发出 S21的指令及调试检验说明
新的软件版本1.18更新记录如下：
1. 修改test/root用户密码         test:tz83583000s21          root:tzs21+LAN MAC 后六位
2. 修复logo 不显示问题
3. 修复锁运营失败问题
#### 2019.08.18
**陈良**  电话接通后，前面几句会有回音，发现出现的几率还是比较大
**封远钊**  V1.18  添加迪拜单独的xml等。
#### 2019.08.15
**封远钊**  修改了 tr069 WANIPConnection.{i}.ExternalIPAddress 节点的为tr069 的那一路 IP  的临时版本
#### 2019.08.14
**邹春来** BM916R-T1 cat6模块固件正式版本发布，修改点：
1. 初次出正式版本，用于生产做货，请测试承认版本
2. 模块两路发at命令导致模块异常问题，该问题目前合入了高通的patch，虽未完全解决，但概率已经大大降低；
3. 模块通过AT命令恢复出厂设置功能;
4. 模块注册到3g情况下，cfun=0，模块会重启；
5. 模块升级包太大问题，目前升级包大小为86.5M
6. reset脚拉低100ms重启
7. BMTCELLINFO 概率性ENODEBID和CELL_ID都为-1，测试无复现
#### 2019.08.12
**封远钊** 附件是 S21 V1.17 
#### 2019.08.11
**陈良**  V08版本，目前只有防打扰模式无法生效，感觉好像是服务器不支持.  
网口重启的问题已经修复，这几天需要验证一下。
#### 2019.08.10
**封远钊**  发出当前针对Dialog 的tr069 节点进度表
#### 2019.08.08
**郑达**  V1.16，请查收。
#### 2019.08.07
**任银善**  CAT6 IPTV基本搞定，防火墙功能统一加在了config中  
与盒子配合上的问题，目前打算将网卡驱动编成KO，动态挂载，这样可以解决网卡不断重启的问题  
MTK的PATCH测试无效  
修改了高端内存问题，关闭高端内存功能时，部分内存没有释放  
#### 2019.08.06
**任银善**  使用吕强发来的固件，网络也是不通的。  
**郑达**  当前iptv功能已不需要与辅桥3绑定在一起，因此配置上需要做些修改，请用该xml出配置  
**陈良**  华为VOIP的验收测试已经完成,
#### 2019.08.05
**任银善** open 的SDK编译出来的MT7621的固件，网络不通。动态IP获取不到地址，静态IP也不通，但是插拔网线，物理连接是OK的。
**封远钊**   V1.15， 修复的bug见附件表格
**陈良**  目前现场测试发现的一些问题和需求 <hide>  
VOIP功能:
1.短号码功能.
2.增加语音邮箱的功能.
3.设备上电话的指示灯没有工作,正常摘机后指示灯会亮
4.连续按免提键,VOIP会出现状态异常的情况

IPTV问题:
1.开启锁小区功能会影响到igmpproxy进程的启动.
2.自动配置IPTV DNS.
3.网口重启的问题.

基本功能问题修复
1.WIFI无法切换信道
2.长时间运行后,WIFI有出现严重丢包的情况,检查之后发现有内存泄露的问题,正在定位问题.
3.模块获取基站和小区ID出现异常,基站ID显示为-1,华为设备正常,正在定位问题.

TR069:
1.TR069 单独APN的功能
</hide>

#### 2019.08.03
**陈良**  voip连续按免提的情况下,会出现状态错误的情况.  
设备锁住的情况下,依然可以播放IPTV的问题已经修复了.  
#### 2019.08.02
**封远钊**  S21 factory 校准区（/dev/mtd2），各个号段信息的位置
#### 2019.08.01
**喻潇**  s21-bug总结-20190801
#### 2019.07.31
**陈良**  今天测试呼叫等待保持,三方通话,呼叫前转这几个功能,这几个功能可以正常工作
#### 2019.07.30
**吕强**  port link up & link down的问题 patch 见附件
**陈良**  viop 下午把帐号配置成功了,已经可以正常拨打外线电话.  
#### 2019.07.29
**郑达**  把模块设置为4g优先，b41 only, 通过at^sysinfo查询到注册到3g情况下，cfun=0，模块会重启。
**陈良**  不开放实验室给我们测试了,只能先从华为那边借了一套设备出来,在实网下进行测试.  
**封远钊** S21  V1.14 ，请测试
#### 2019.07.28
**陈良**   VOIP在合版本的过程中发现通话没有声音,已反馈给星禾那边处理,预计明天可以出新的版本.  
iptv 按照华为的测试用例过了一遍,没有发现什么问题。
#### 2019.07.27
**李柱栋**  即使解决了读取到假的switch网口状态，如何初始化复位网卡重新协商出真正的状态，还要研究下。  
**任银善**  swconfig  dev switch0 port n get link 读出来的是假装态，我这个我确认了，是正常的实际的状态。  
**陈良**  VOIP中间的程序已经出来了,小蔡正在验证合版本,郑达这边正在实现VOIP  APN的功能.  
实网下进行测试,同时启动还是有些问题,后检查发现是防火墙导致的,修改之后同时启动没有问题,但是启动时间变的和华为一样了,需要4分30秒,
#### 2019.07.26
**任银善** 和iptv连接出现网口不断重启的现象。<hide>  
其中一个网口通过vlan配置为LAN2口，接入IPTV盒子，启动后，执行/etc/init.d/network restart 命令，发现串口就会一直打印 port 2 link up & down
</hide>
**李柱栋** 我测试了#30# (关闭呼叫用户显示)，但是呼叫出去对方还是能显示我的号码
**郑达**  去迪拜。
**陈良**  和客户那边确认需要做CE认证和5G WIFI的相关测试,和光达确认过了,测试周期需要3-4周
#### 2019.07.25
**陈良** [华为提供的定制化需求更新表](https://pan.wps.cn/l/sN8fbCwAh)
#### 2019.07.24
**任银善**  静态路由的功能要增加出口列表。  
防火墙 有各种情况导致没有加入，许多种情况可能会重建防火墙。  
小基站的组播>一直没有成功。  
**郑达**  volte有杂音，支持的人来看。  
要上一个新的sequans模块，需要在7621上占用4m空间。  
openwrt中的启动脚本如果没有退出，reboot就无法起作用。  
原来的apn和桥绑定严重，改清晰一点。  
宽翼空apn不能注册的问题宽翼还在看。  
volte有杂音，支持的人来看。
#### 2019.07.23
**陈良** 运营商希望我们能在8月底到货,目前我们还在华为确认具体的交期.  
实网环境下VOIP已经验证可以实现相互互打  
iptv重新添加了一条路由规则后,问题得到解决,但是在还原防火墙之后数据又上不去了
#### 2019.07.22
**陈良**  服务器已经可以注册上了,电话之间也可以互相拨打.  
[Test Cases IPTV](https://pan.wps.cn/l/sYx09efWQ)  　　
**郑达** 目前迪拜项目尚有以下问题需要解决： 1.voip功能  2周       2.关闭多余lan口　　3.iptv配置修正
#### 2019.07.20
**郑达**  s21_v1.13 主要实现支持４路apn，并支持iptv功能
#### 2019.07.19
**郑达**  宽翼模块当前空的apn不能上网了。
#### 2019.07.18
**陈良**  今天IPTV已经调通了,但是有些频道播放有些卡顿,
#### 2019.07.17
**任银善**  数据不能转发下去，是不是usb网卡和普通网卡不一样。
**郑达**  s21_v1.12请使用最新版本，解决了部分bug，还剩余2个。
目前迪拜项目尚有以下问题需要解决：2.tr069走单独一路  预计7-18实现        3.软件支持第4路apn       4.voip功能  3周
**喻潇**  附件为针对1.12程序验证的BUG表  
**董锡文**  很多bug其实是新的需求。  
**陈良**  对驻网时间过长的问题进行了修复,经验证已经修复了这个问题.  
#### 2019.07.16
**郑达**  发出生产工具需要的相关信息。
**任银善**  发出昨天抓包的情况分析，让华为确认下以下数据是否正常
**李柱栋**  给eddy发出板子使用方法、代码编译过程请参考 openwrt_cat6.readme.txt 里的说明。
#### 2019.07.15
**吴曦**  笔记本系统需win7以上.有些笔记本连接时不弹出pin码连接的.可以修改注册表
苏伟 发出是4路APN的更新包
**陈良**  新版本的主要解决的问题我都重新验证了,验证结果已经更新.   
iptv华为那边的专家有些顾忌也没有说清楚  
网页上显示出来的小区信息却和当前基站小区的信息对不上  
**郑达**   目前迪拜项目尚有以下问题需要解决<hide>
1. 解决前线发现的bug,还有8个。
2. tr069走单独一路  预计7-16实现
3. iptv（iptv走单独一个网口已经实现） 预计7-16实现（任工当前进度：看到wan口已经收到组播包数据，但数据并没转到lan口）
4. voip功能  一个月 
</hide>
- bm916模块目前还有以下问题没有解决<hide>  
- 模块支持4路apn 		2019-07-02: 4路apn有bug, 暂时无解决方案
- 3路apn概率性出现3路都ping不通现象 	07-15：1600次出现一次三路ping不通问题，出现kernel panic, 模块还重启了。
- 模块bin包太大需裁剪问题 		06-28: 秦工反馈先内部沟通
- 模块重启问题 		07-15: 已经抓取modem侧log分析
</hide>
#### 2019.07.14
**陈良**  运营商向华为那边投诉了,对我们室内CPE的测试进度很不满意,要求我们尽快给出一个详细的完成时间表出来.  
IPTV,抓了下WAN口和LAN口的包,发现还是有包可以下来,但是WAN口到LAN口的包好像还有写问题,明天再试一下.
#### 2019.07.13
**郑达**  s21_v1.11, 新版本主要解决部分bug
#### 2019.07.12
**陈良**  发出现场测试bug表。  
**郑达**  有些bug在公司无法复现，需要现场详细信息。其他在修改。  
目前迪拜项目尚有以下问题需要解决： <hide>  
1.解决前线发现的bug（针对bug表另行发起邮件）
2.tr069走单独一路  预计7-16实现
3.iptv（iptv走单独一个网口已经实现） 预计7-16实现（需任银善配合调通）
4.voip功能  一个月
</hide>
#### 2019.07.11
**郑达**  测试版s21_v1.10.x2，使用一起的模块驱动，解决有时候无法注册网路问题
#### 2019.07.10
**郑达**  7月3日提出的25个bug，还有3个，一个和wps相关，两个无法复现。  
wps使用的是gps这个软件进行的测试，和吴曦使用的jumpstart不同。  
陈良在迪拜，有两天模块在不断重启，第三天又不出现了。  
宽翼一直没有解决概率性ping不通问题。特别是设备作为网关，有数据出去的情况更容易出现。  
网页安全测试，只用Sql注入了。
#### 2019.07.09
**郑达**  宽翼的人似乎没有什么好办法。
**陈良**  设备能正常注册,从设备里面PING外网可以通,接电脑后一打开网页,网络就断了.
**封远钊**  在公司复现了陈良的情况。
**任银善**  在7621上运行igmp代理程序，可以对br-lan的设备进行组播控制。
#### 2019.07.08
**郑达**  新版本解决了模块时常拨不上号的问题，但是引发了新的ping不通问题，在国内这是概率时间，但在国外居然成了必现。我们和宽翼的人正在看这个问题，等会测试验证下。  
**陈良**  设备升级到最新的v1.09.3 版本之后,发现设备无法上网,降回s21_v1.09.1之后可以正常上网,  
**郑达**  网页安全测试董正在做，早上开晨会他反馈要一周时间做完第一遍。然后我和向杰评估，是要这两天做完。  
宽翼苏工过来了。  
我们与苏工对bm916模块进行了挂测，4台设备出现的现象都不一样
#### 2019.07.06
**封远钊**  宽翼的人还是要过来，昨天给的patch貌似不工作。
#### 2019.07.05
苏伟(宽翼） 目前用的移动，请使用at+cimi，不要使用qcmi，
邹春来  下午我司会发新的gobinet驱动给到贵司挂机，请安排挂机，谢谢。如果这次挂机还是有复现到问题，我司苏工或者乔总周末会从西安出发，下周一直接到贵司现场，跟贵司同事一起排查和解决Gobi的问题  
**陈良**  更新了新的程序,但是之前不读卡/驻网的问题还是存在,不读卡时输入AT指令显示端口打开错误.  
新的程序无法读卡/驻网.无法验证修复的一些问题.
#### 2019.07.04
**郑达**  bug表完成度：8/总24  
**徐刚雄**  wifi基本调完，5.8G在稳定性上比华为差一些。
#### 2019.07.03
**喻潇**  发出新的bug表，WIFI连接数2.4G总共32个，5G总共32个，暂未实测。
#### 2019.07.02
**郑达**  宽翼现存问题 at冲突问题 模块支持4路apn 启动时候概率性出现at不通情况，需要重启916模块才能解决 3路apn概率性出现3路都ping不通现象 3路apn概率性出现2路能ping通，但有1路ping不通现象  
**董锡文** 开始做安全测试的修改，很多要改的地方。  
**陈良**  无法驻网的问题已经抓了包  
CA环境需要客户那边审核才能开放  
防火墙和系统功能这两块还存在很多问题
#### 2019.07.01
**陈良** 样机在现场测试的时候,发现过1-2次注册不到网络,重启下能恢复  
性能方面无CA环境下速率略好于华为的室外机,外置天线效果比内置天线的效果要好一些,WIFI部分测试发现了一些问题 <hide>
项目|问题|处理建议
---|----|------
主页LOGO|1.LOGO缩小后有些变形,用户感官差|1.去掉方框,缩小图标
4G Information|1.SINR值显示错误,页面显示300dB,实际AT读出来的值为30dB.|1.按AT读出来的值显示
""|2.页面不会自动刷新|2.建议做成自动刷新3s/次
Wan Information|1.页面不会自动刷新|1.建议做成自动刷新3s/次
WIFI-2.4G/5G Setting|1.SSID Broadcast关闭后,重新打开无法生效,需重启之后才能生效|
""|2.Encrypt Algorithm默认为AES|1.默认建议设置成TKIP/AES
""|3.副的SSID开启之后无法正常连接,需要同时开启副的DHCP才可以|1.建议在用户开启副SSID之后给用户一个提示 <br>指导客户开启副的DHCP,或默认自动开启.
""|4.WPS功能开启之后无法正常使用|
Wi-Fi Advanced Settings|1.Max Station设置成1之后,Connected List无法显示任何设备信息.|
""|2.Max Station的设置参数没有起效.|
ECGI Lock|1.需限制最大的小区个数,目前运营商这边要求最大6个|增加一个可设置最大小区个数的设置项
""|2.需提供下ECGI和当前注册小区的对应关系,方便测试|
</hide>

#### 2019.06.29
**郑达**  约宽翼的周一来现场调试。
#### 2019.06.28
**郑达**  S21软件版本发布临时版本 v1.09.1
**余小虎**  dialog添加3条TR069要求
<hide>
- 网页TR069菜单中，修改心跳需要马上生效，且以新设置的心跳时间开始倒计时，而不能等到当前心跳周期结束才生效
- 网页TR069菜单中，修改参数应该重启TR069服务，而不应该要求用户重启机器
- 交互流程中，终端上报第1个包需要是BOOT消息，而不能是空包。空包会导致服务器报错，后续流程无法继续进行。
</hide>

#### 2019.06.27
**徐刚雄**   5.8G还在调。
宽翼 放出BM916R  B41 200M的软件版本
#### 2019.06.26
**郑达**  b41的模块无法在小基站注册到载波聚合。
#### 2019.06.25
**李柱栋**  吕强发的对于pcm格式数据调试可以参考文档pdf并没有什么用。
宽翼：
两路发at命令导致模块异常：需要高通新基线解决，目前高通最新回复是本周末前会把基线释放出来。
锁小区功能问题：高通方案决定的，所有使用高通方案的竞品都遵循同样的规则
ECI 与小区id对应关系 AT指令bmtcellinfo里面的这个cell id就是eci，该值除以256  得到的是eNode ID   对256求余  得到cell id，也就是：ECI (28 Bits) = eNB ID(20 Bits) + Cell ID(8 Bits)
模块支持4路apn 研发已经在开始调试，大概需要2周时间
ipv6断掉其中一路会影响其他的链路 Gobi的问题我们一直在分析解决，我们计划此问题在本周内解决掉
#### 2019.06.24
**郑达**  S21最新版本v1.09 <hide>
- web: 在防火墙中添加url默认设置（向杰）
- 修改设备型号为S21（郑达）
- web: 修复wifi页面隐藏问题（董锡文）
- web: 实现了Login页面型号和SN号的内容显示（董锡文）
- web: 修复了DHCP Settings页面Main DHCP Setting分页的Main DNS和Vice DNS字段命名不规范问题（董锡文）
- web: 修复了Version Infomation页面的Memory字段显示问题，将Memory字段拆分为Memory Total、Memory Free以及Memory Cache三个字段（董锡文）
- web: 修复了WiFi-2.4G Settings和WiFi-5G Settings页面的WPS Settings分页弹窗倒计时到0秒自动关闭弹窗后再次点击所有弹窗会造成当前弹窗立刻闪退的问题（董锡文）
- web: 添加配置控制 WAN配置的显示和隐藏（董锡文）
- web: 修复了Advanced Settings页面Remote Ping分页点击Edit弹窗异常的问题（董锡文）
- web: 优化了WiFi-2.4G Settings和Wifi-5G Settings页面的WPS Settings分页的定时器（董锡文）
- web: 去除了WiFi-5G Settings页面Connected List分页表体的Edit列（董锡文）
- 解决url默认规则获取错误问题（封远钊）
- 产测工具：升级和升配置后通过亮灯来标记状态（封远钊）
- 实现ipv6 多路拨号并分配Global ipv6 地址到底下lan设备、下发dns（封远钊）
- web: 优化了首屏加载速度（董锡文）
- web: 优化了登录页的加载速度（董锡文）
- ipv6 添加无线网络策略路由（暂时不包括有线V6，有线V6 未测试）（封远钊）
- 添加ipv6 nat（封远钊）
- 添加判别V4 V6 网口，防止ipv4 v6 配置冲突重叠（封远钊）
- web: 修复了WiFi-2.4G Settings和WiFi-5G Settings页面的Auxiliary Wi-Fi1 Settings和Auxiliary Wi-Fi2 Settings分页选择Encrypt Algorithm的TKIP/AES并保存后并不是选择TKIP/AES而是选择AES的问题（董锡文）
- web: 去除了Wan Infomation页面主辅APN的MAC Address字段（董锡文）
- web: 修复了登录页分辨率过低时登录有右侧部分信息和左侧登录背景图部分看不到的问题，实现成可滚动（董锡文）
- tr069: 实现编辑主动上报时间不用重启tr069客户端功能，添加https节点（江义波）
- 实现了登录后的会话超时的时间可配置（董锡文）
- 实现sip alg功能（郑达）
- web: 修复了WiFi-5G Settings页面Wi-Fi Advanced Settings分页选择Wi-Fi Mode字段的值不为11AC时仍然可以在Bandwidth字段选择80MHz的问题（董锡文）
- 配置: 支持配置网页的https端口.（郑达）
- 添加wan访问列表权限控制配置，并且只允许通过https访问设备web.（郑达）
- web: 将WiFi-2.4G Settings和WiFi-5G页面的Main WiFi-Settings、Auxiliary Wi-Fi1 Settings、AuxiLiary Wi-Fi2 Settings以及Wi-Fi Advanced Settings分页Save之后先set再get数据回来更新页面状态，修改为只将当前页面的分页所修改的数据set之后不用把数据get回来更新页面状态（董锡文）
</hide>
#### 2019.06.22
**郑达**  宽翼存在的问题：两路发at命令导致模块异常，锁小区功能会注册到非指定小区，启动时候概率性出现at不通情况，需要重启916模块才能解决，加载gobinet驱动后，概率性出现拨不上号问题。
用户的新要求：ECI 与小区id对应关系，模块支持4路apn
#### 2019.06.21
**何旭晨**  5.8G 还在调。
**罗厅**  江义波完成上报RSRP/RSRQ/RSSI/SINR/CQI/MCS/IMEI/IMSI/ICCID/CellID,dhcp修改等。
#### 2019.06.18
**董锡文**  登录页的速度可以在1s左右了。ie的体验会好一些。  
**郑达**  siproxd可以运行了。openwrt系统中的sip alg看起来是关闭的。  
**何旭晨**  板子已回，在调试。  
**刘云**  [规格书1.2](http://192.168.1.93:8000/%E8%A7%84%E6%A0%BC%E4%B9%A6/ZLT%20S21%20Datasheet%20V1.2.docx)  
**王伍**  [规格书1.21](http://192.168.1.93:8000/%E8%A7%84%E6%A0%BC%E4%B9%A6/ZLT%20S21%20Datasheet%20V1.21.docx) 加上了眉批
#### 2019.06.17
**陈良**  迪拜CAT6项目有锁小区的需求<hide>  

   1. 设备里面可预设6个(暂定)小区ID信息,小区ID信息可通过配置,TR069方式来设置.
   2. 小区的ID信息按以下格式来保存,这个和我们之前的格式不一样需要确认一下ECI是否可以区分小区ID.
   3. TR069服务器可通过远程来解锁/重置锁小区功能,目前这部分功能还在沟通之中.
</hide>

**封远钊**  发出多apn下的ipv6疑问：<hide>

- 在三路的apn都拨上号 的情况下，去查ipv6的路由表，发现默认路由设置的是bmwan2 那一路的
- 使用ping6 -I bmwanX 2400：da00::6666 ，只有bmwan2 那路能通。
- 使用 at$qcrmcall=0,1,2 把bmwan0 那一路的V6 断拨号之后，再用ping6 -I bmwan2  2400：da00::6666 ，此时就已经不能ping通了
</hide>

**何旭晨**  板子在贴，晚上或明天回。  
**董锡文**  首页发送的请求太多，有些慢，准备改成一个接口，并且做到最精简。  
当前js代码的耦合太高，命名也非常不规范。  
**李柱栋**  给eddy准备cat6编译环境。给他标准的openwrt 1505。  
**罗厅**  江义波Openwrt cat6 tr069数据节点当前问题修正（预计3天）<hide>
1. Web管理员账号下显示TR069设置页面，user账号不显示TR069
2. 仅修改心跳时间后，TR069服务应当以设定的心跳时间重新倒计时，并在倒计时完毕后主动上报；（需要web 和 tr069 进程间通讯的接口？）
3. 上报RSRP/RSRQ/RSSI/SINR/CQI/MCS
IMEI/IMSI/ICCID/CellID
已经实现，（锁物理小区设置 这个具体还需要确认）
4. 多SSID设置 SSID/密码/开放WiFi,
多DHCP设置 IP/掩码/网关,
多APN设置 APN名称/APN协议（IPV4、IPV6、IPV4/V6）,
多NAT设置 开启/关闭 ,
多APN读取 对应WAN IP
已经实现（多nat设置开启关闭 这个还需确认）
5. 设置Wan访问WEB的端口，缺省8888（需要新增接口）
6. 使能禁止Wan接口登录Web，缺省开启（需要新增接口）
</hide>
at冲突还要等本周高通出patch。
#### 2019.06.15
**余小虎**  发出[dialog技术要求](http://192.168.1.93:8000/Tozed-CAT6-Dialog-Requirement_20190614.xlsx)  
**何旭晨**  周一才能贴板。  
**郑达**  一起过了一遍dialog技术要求，语音占了一大块。  
zte7520使用全包过滤字符串的方式来做url过滤功能，不使用dns解析过滤的方式。应该还是存在问题，如果包内存在qq.com，那么也是会过滤掉。  
陈良那里提出的要求是对业务不同走不同的apn，对多ssid无要求。  
#### 2019.06.13
**余小虎**  测试发现的问题
<hide>

1. System Status > Version Information > Device & Version Information， 建议 Item改为Model，型号s21改为S21；
2. System Status > Version Information > Running Status，Memory信息为MemTotal 255012 KBMemFree 201132 KBCached 13768 KB，中间因为用分隔符分开；
3. 从如上第2项看，系统可用内存还算比较大，建议TCPDUMP文件内置，就不要每次上传tcpdump到内存来抓包了；
4. SN号建议从s21+IMEI改为S21+IMEI；
5. 登录页面除了IMSI，还需显示SN号；
6. Device Settings > DHCP Settings ， Vice DNS不合适，建议Main DNS改为Primary DNS，辅DNS改为Secondary DNS；
7. Device Settings > WiFi-2.4G Settings和WiFi-5G Settings中，弹出的WPS Settings显示的位置和效果不佳；
8. WiFi带宽20or40MHz，建议改为20/40MHz；
9. WiFi多SSID1广播建议默认开启；
10. 2.4G SSID1开启后，切换到其他页面再切回来，又显示关闭状况，实际SSID1已开启；
11. 主APN配置路由模式后，手机连主SSID可以正常路由；APN1和APN2配置路由模式时，手机连SSID1和SSID2路由不成功；
12. 手机连接SSID2，从WiFi Connected List中看到IP是DHCP1的IP，即由SSID1的DHCP分配IP；
13. 关闭APN1，CPE显示无移动网络，Connection Network Status状态显示为fail；
</hide>

#### 2019.06.12
**郑达**  多apn功能已经完成，麻烦安排下时间在兰卡对该功能进行测试  
S21最新版本v1.08 <hide>  

- web: 修复了Login页左侧在小屏幕显示不完整的问题（董锡文）
- web: 完善wps功能，在wps功能中添加随机PIN码,在手机端可以输入连接(2.4g和5.8g)（向杰）
- web: 如果SIM卡锁PIN,在状态栏提示解PIN所在的地方（向杰）
- tr069: 修改MNO_WANNetConfigInfo 下节点数据 ECGI SignalQuality FrequencyPoint CQI（江义波）
- lanrecord: 解决经过lanrecord的数据包默认accept的问题，改为return（封远钊）
- 防火墙：解决默认规则为拒绝时端口过滤不生效问题（封远钊）
- 防火墙：解决默认规则为DROP时不生效问题（封远钊）
- 防火墙：修复pin puk次数更新慢问题（封远钊）
- 防火墙：解决默认规则为拒绝时ip过滤不生效问题（封远钊）
- 配置：增加ntp配置（封远钊）
- web: 解决2.4G和5.8G在IE下显示不出来(由switch关键字导致)（向杰）
- web: 解决静态IP绑定和upnp在IE8不显示问题（向杰）
- 防火墙：增加读取/设置 url默认规则的接口（封远钊）
- web: 实现了一个新增的System Log页面，包括读取显示系统日志和清除日志的功能（董锡文）
- web: 在开启PIN码验证和关闭PIN码验证给提醒次数，以及puk（向杰）
- dialtool2: 实现ipv4v6双栈情况下的ipv4,v6同时拨号，并支持断拨号重连.（郑达）
- web: 修复tr069和dmz等页面保存没有提醒bug（向杰）
- 配置：解决锁band配置不对问题（封远钊）
- 配置：增加设备型号、sn可配置字段（封远钊）
- web: 修复了页面弹出框部分显示不全的问题（董锡文）
- 新增lan/wan模式切换功能（封远钊，向杰）
- web: 优化状态栏的Lan和wan，只显示对应的Lan和Wan（向杰）
- tr069: 解决SignalQuality为空的bug（江义波）
- web: 修复了main.js文件SYS_LOG重命名的问题（董锡文）
- web: 优化登录界面Login框（向杰）
- 增加wan mac地址设置功能（封远钊）
- web: 解决wps设置重启wifi的bug（封远钊）
- web: 修复了状态栏内容显示不正常的问题（董锡文）
- web: 实现了APN Settings页面所有分页的Help信息内容（董锡文）
- web: 实现了新增的TR069页面右侧的的Help内容显示（董锡文）
- web: 修复了多个页面弹窗的标题内容显示问题（董锡文）
- web: 修复了Advanced Settings页面的NetWork Setting分页的字段名显示不正确问题（董锡文）
- ipv6: 在添加ipv6路由规则时，去掉匹配v6前缀从wan口出去的规则.（郑达）
- web: 解决显示sn不对问题（郑达）
- web: 实现了新增的WiFi-2.4G Settings页面的Wi-Fi Advanced Settings分页的所有内容显示（董锡文）
- web: 优化系统信息中状态信息没加载数据前，帮助信息跑到右边来（向杰）
- web: 配置控制2.4g和5.8g辅wifi（向杰）
- wifi: 设置2.4g wifi默认规则,ZLT S21-2.4G-XXXXXX（郑达）
- wifi: 完善5.8g wifi的配置设置（郑达）
- web: 修复了WiFi Infomation页面右侧的内容显示不正确问题（董锡文）
- web: 修复了WiFi-2.4G页面所有分页右侧的help信息显示问题（董锡文）
- web: 实现了新增的WiFi-5G Settings页面的Wi-Fi Advanced Settings分页的所有内容显示（董锡文）
- web: 修复了WiFi-2.4G Settings页面和WiFi-5G Settings页面的Wi-Fi Access Control分页和WPS Settings分页点击保存会跳转页面的问题 （董锡文）
- 产测工具：解决写sn号位置不正确问题（封远钊）
- 设置自动拨号为默认拨号方式（封远钊）
- tr069: 解决cpe_set_EnableCWMP函数不能被调用问题（江义波）
- tr069: 解决PeriodicInformEnable设置问题（江义波）
- web: 实现了将Firewall模块下的Default Settings页面和MAC Filter页面合并到Filtering Rules页面（董锡文）
- web: 整理了WiFi-2.4G Settings页面的Wi-Fi Advanced Settings分页的Wi-Fi Mode字段（董锡文）
- web: wps功能中PBC和PIN码分开设置（向杰）
- web: 在设备设置中添加WAN配置网页(即MAC克隆)（向杰）
</hied>
#### 2019.06.10
**喻潇**  升级后tr069不能上报了。
#### 2019.06.04
7621的datasheet中未提及， 9341中有igmp相关寄存器说明。  
**张悦玲**  考虑开始合并电话程序，准备把界面部分和控制部分完全分开。这样在不需要界面的情况下，不用增加字库等，可以非常精简。  
**郑达**  封远钊感觉原来的url白名单不对。其实防火墙各个功能之间存在互斥和干扰。这里设置了黑名单，其他的要设置白名单就有些难。  
**何旭晨**  主芯片还在香港报关。
#### 2019.06.03
**董锡文**  写系统日志的界面，要写后台，觉得lua不难，业务有些不立即。  
**江义波**  正在进行评估确定需要完善开发的数据节点以及时间  
**郑达**  准备用python写一个tr069的输出分析汇总给喻潇，方便测试。有400多项，测试很困难。  
发布1.07版本：<hide>  
- web: 新增info页面（董锡文）
- web: 修正login页面内容显示（董锡文）
- 解决ie浏览器崩溃问题（封远钊）
- 优化解pin码流程（封远钊，向杰）
- web: 给锁物理小区页面增加提示（董锡文）
- web: 移除快速设置页面（董锡文）
- web: 修正wan info页面的内容显示（董锡文）
- dialtool2: 修正读网络模式bug（封远钊）
- web: 修正解物理小区失败bug（封远钊）
- wps: 修改 wps接口（封远钊）
- web: 解决静态arp绑定页面弹出框显示不全问题（董锡文）
- tr069: 解决imei读取不对问题（江义波）
</hide>

#### 2019.05.31
[上网+IPTV直播点播+任意设备看直播+IPTV抓包地址心得](https://www.right.com.cn/forum/thread-307948-1-1.html)  
**何旭晨**  S21的CPE，我们的页面目前还有发射功率，WIFI工作模式等等，选择越多，最终用户应该会越烦，建议做得最简单；  
向吕强问：MT7621A的LED点灯，有没有相关的说明文档？规格书上面没有写清楚。我们想要用PORT0和PORT1，每个PORT需要点两个灯  
**郑达**    宽翼 bug：1. 锁小区只在4g only下有效，设置成4g优先会有概率锁不上  
2. 锁的频点不能超过模块所支持的频段支持的频点范围，如果锁上超出范围的不存在的小区，就会锁失败。（会注上其它小区）  
需求/问题 | 提出时间 |  解决时间 | 解决方案 | 目前进 度
------|---|----|----|------
两路发at命令导致模块异常 | 2019.04.03 | |高通回复需要升级最新3.1基线才能解决，高通计划新基线要到6月12才能出来|
三路数据apn外，请多提供一路专门拨volte apn | 2019.05.30 ||这个一直支持的|
锁小区功能 | 2019.05.31 ||正在跟你们封工一起分析和处理这个问题|
#### 2019.05.30
**喻潇**  TR069和WIFI还没测完，问题也提交禅道，请将浏览器问题、网页问题、配置问题先修正，方便测试。  
**江义波**  配置升级的没做  
**郑达**  禅道用起来不错，喻潇已经把bug提交上去，有配图。ipv6,pc已经得到了公网的ip.  
ie阻塞的问题，实在没有办法，改用c写了fread，就没有问题。
#### 2019.05.29
**王伍**  BRIDGE目录下有[IGMP的代码](http://192.168.1.93:8000/s21_cat6/VT6526.rar), [ds6526100datasheet](http://192.168.1.93:8000/s21_cat6/DS6526100.pdf)  
**郑达** 最新版本v1.06<hide>  
- web: 高级设置页面下新增DDNS分页（董锡文）  
- 产测软件：升级程序，配置使用md5进行包校验（封远钊）  
- 增加upnp功能并添加调用接口（封远钊）  
- 解决tr069 wan口检测失败问题（江义波）  
- web: 添加upnp网页（向杰）  
- web: 更改登录界面（董锡文）  
- web: 解决网页不断刷新问题（向杰）  
- web: 解决登录页4G info名称不规范问题（董锡文）  
- web: 修改wan info页面内容显示（董锡文）  
- 增加读工厂区imei的接口（郑达）  
- 新增解puk接口和修改pin码的接口（封远钊）  
- 默认tr069为关闭状态（江义波）  
- web: 移除了HOME页面，登录后显示页面为4G Information页面（董- 锡文）  
- web: 优化4G Info页面显示（董锡文）  
- web: 调整upnp界面（向杰）  
- web: 添加pin码功能，包括解pin，锁pin，更改pin，解puk（向杰）-   
- web: 实现了WAN Info页面右侧的help内容显示（董锡文）  
- web: 实现了DHCP Settings页面LAN Device List分页右侧的help内容显示,同时修复了DHCP Settings页面的Main DHCP Settinga分页、Auxiliary DHCP1 Setting分页以及Auxiliary DHCP2 Setting分页右侧的help内容显示问题（董锡文）  
- web: 修改version info页面的imei, sn显示（董锡文）
</hide>
#### 2019.05.28
**郑达**  tr069江义波修改后可以在服务器上看到数据了。  
ie卡住的问题，封远钊跟踪代码，认为是mini_httpd没有给cgi标准输入。  
网关消失的问题，是自己的程序的问题，已解。  
宽翼还要2个问题，apn数量包括volte也只有3个。at并发会挂。  
ipv6 设备可以ping到google和dns。在看给pc分配ip的部分。  
#### 2019.05.27
**何旭晨**  第三板，wifi部分要重新调整，估计要到6月下旬。
#### 2019.05.24
**何旭晨**  [规格书](http://192.168.1.93:8000/%E8%A7%84%E6%A0%BC%E4%B9%A6/ZLT%20S21%E8%A7%84%E6%A0%BC%E4%B9%A6V1.0.docx)  
**郑达**  [IPv6技术详解：基本概念、应用现状、技术实践（上篇）](https://www.cnblogs.com/imstudy/p/9056334.html)
#### 2019.05.23
**郑达**  看起来拿到ipv6地址了，但是路由等怎么设置还是问题。  
**江义波** 是imei相同导致上报没有发现。
#### 2019.05.22
**李柱栋** 打流试图分流网络数据到其他cpu没有成功。修改usb buff，如果太大，不能加载。  
**何旭晨** 已经发第三板。  
**郑达**  昨天修正了测试的大部分bug, 出了测试程序继续测试。生产工具方面赵金估计要下周。ipv6还在验证。发出版本1.05<hide>  
- web: 在设置tr069服务器后，重启tr069应用（向杰）  
- web: 网页读取/设置配置都直接与配置的语言选项挂钩（向杰）  
- web: 添加ddns数据交互接口（向杰）  
- 产测: 添加写sn接口，升级系统接口，配置升级接口（封远钊）  
- web: 解决锁物理小区代码冲突导致的网页不能刷新问题（向杰）  
- web: 解决ie浏览器崩溃问题（向杰）  
</hide>
#### 2019.05.21
**徐刚雄** 发出LT30模块引脚使用配置列表(P19H)_v1.0 <http://192.168.1.93:8000/LT30模块引脚使用配置列表(P19H)_v1.0.xlsx>  
**喻潇** 存在ie崩溃问题。华为设备铭牌上没有mac，设备有多个mac，写的时候要写wifi的mac。  
**向杰** 改bug表，登录界面还要美化一点。发出添加网页步骤流程 http://192.168.1.93:8000/网页添加步骤说明.docx  
**郑达** 希望把禅道这个系统用起来。  
**李柱栋**  usb驱动比较复杂，不容易看。  
**宽翼** ipv6还需要另外一个opkg的软件包, 不要用dhcp，是无状态地址转换。  
#### 2019.05.20
**陈良**  郑达 sn是否需要定制化，：一般自己使用设备类型+imei，如果客户需要定制化，需要生产工具配合写入。  
**郑达** bug还剩下4条：<hide>web显示	2.4g wifi鉴权方式简化  
web设置	防火墙->filtering rules 几个按钮规则没有实现  
系统	IE浏览器，以及360的兼容模式，待机1分钟浏览器就崩溃了  
web设置	TR069开启设置后，服务器没收到上报；TR069无法测试  
</hide>
**郑达** 发出版本1.04<hide>
- web: 添加nat loop back（向杰）  
- web: 添加静态arp绑定（向杰） 
- 实现wps产生随机pin码（封远钊）  
- web: 添加备份还原网页功能（向杰）  
- 添加ddns功能（封远钊）  
- 产测：产测工具支持测试外设: 灯, 按键, 天线（郑达）  
- web: 修正apn用户名密码不能为空的bug（向杰）  
- web: 限定dhcp地址池规则（向杰）  
- web: wifi 设置 wifi disable 时，隐藏wifi开关以下的内容（向- 杰）  
- web: 设置dmz, 远程ping时重启防火墙（向杰）  
- web: 增加０格信号图标（向杰）  
- web:5g设置 wifi disable 时，隐藏wifi开关以下的内容（向杰） -  
- 解决设置静态路由表时的掩码错误（封远钊）  
- web:防火墙中端口映射启用规则会退出登录bug（向杰）  
- web: 解决4g注册状态不对的bug（封远钊）  
- wps按键：对该按键的时长进行重新定义（封远钊）  
- wps灯: 根据不同状态显示不同的闪亮情况（封远钊）  
- tr069: 支持https（江义波）  
- 修正限速不准的bug（封远钊）  
- 解决主apn配置修改不生效bug（封远钊）  
- 修改配置不能开关dhcp server的bug（封远钊）  
- 配置：支持timezone设置（封远钊）  
- web: 网口显示wan口改为Lan4/Wan（向杰）  
- web: 2.4g wifi右侧帮助信息描述不正确的bug（向杰）  
在未登录界面，将固件版本换成软件版本（向杰）  
- web: dhcp设置页面，vice dns设置，应该允许为空（向杰）  
- web: 解决wifi information页面右边注释名不正确bug（向杰）  
- web: 对一些描述不正确的注释信息进行修改（向杰）  
- web: 解决wifi 信道不能设置为auto的bug（封远钊）  
- web: apn IP --> IPV4（封远钊）  
- web: 解决防火墙清空按钮会清空所有防火墙规则的bug（封远钊）  
- web: 防火墙设置中，去掉ipv4/6的列（封远钊）  
- web: 修改默认防火墙设置页面（封远钊）  
- web: 解决wan信息为空时显示为空的bug（封远钊）  
- web: 版权日期2018改成2019（向杰）  
- web: 解决部分网页在默认英文环境下仍然显示中文（向杰）  
- web: 快速设置中密码添加规则以及优化点击保存时每次保证只能点击一次（向杰）  
- web: 防火墙清空所有规则时，重启防火墙（向杰）  
- web: 在本地物理小区中，给频点和物理小区ID取值范围给客户。供客户- 填写（向杰）  
- 防火墙：ip过滤增加ip范围功能（封远钊）  
- web: 网页优先显示客户指定软件版本号（封远钊）  
- 多apn支持设置mtu（封远钊）  
- tr069: 解决bug（江义波）  
- 配置：解决配置名称不正确bug（封远钊）  
- 系统: 计算用户密码时使用wifi mac来计算.（郑达）  
</hide>
#### 2019.05.17
**何旭晨**  s12+这个板子接收灵敏度是正常的，如果这个是好的，那么s21就按照这个再发一板。
#### 2019.05.16
**陆洪丹** 明天要带2台样机走。需求是今天下午5点客户才提的。  
**郑达** 有些定制内容无法使用配置进行，必然sn，以后会加上。  
**李柱栋**  宽翼的usbnet驱动是标准的。去掉一些延时之类的东西，对速度看起来没有影响。  
所有的处理都在一个cpu上，即使使用不用的程序，也没有分散到不同的核上。  
**郑达**  修改tcp窗口等参数，对速度也没有影响。
#### 2019.05.13
**郑达** 提醒江义波更换使用4g后，设备tr069可以正常连接https。
#### 2019.05.12
**郑达**  发出bug整理表。
#### 2019.05.12
**郑达** 在北京，小基站设置b40设置2载波，设备一直注册不上。  
**邹春来** 我们明天上班第一时间分析处理  
#### 2019.05.11
**郑达**  拿到调好的fdd板子了，现在要去坐高铁去北京看看能否提高小基站的速度。  
**李柱栋** 考虑主频从880MHz提高到1080MHz，看看数据包处理有没有改善  
**何旭晨** 现在散热片不热，可以升频  
#### 2019.05.10
**郑达**  使用修改驱动内部宏的方式，对速度似乎没有影响。给mtk支持发出了邮件，询问usb能力问题。准备明天乱改试试。再去北京看看小基站能调到什么样的速度。另外带2个band3的去测试。upnp在余辉的电脑上使用也不行。
**何旭晨**  USB2.0的眼图很好，所以USB走线是没有问题的。3.0没有办法测试
#### 2019.05.09
**郑达**  何旭晨 band 40 udp打流可以到234M，和插在电脑上相同。tcp能到200-210.  band 3 也差不多。  
测试的几个结论：  
S21板子处理UDP报文的能力同笔记本相同，但S21处理TCP报文的能力要比电脑差；  
WIFI的打开和关闭对CAT6测试速率无影响；  
S21的USB为USB3.0和USB2.0，对CAT6测试速率无影响；  
更换速率更高的FDD模块和频段，CAT6的处理TCP报文的速度也上不去；  
之前他们测试我们的板子，说速率只能达到180Mbps,是因为他们用FTP下载的方式。今天用Iperf的方式，TCP速率可以达到200-210Mbp  
<font color=red>软件有办法看usb收发问题吗</font>  
**蒋世富**  5G的TX1调试rx还是有问题 还要看。  
**喻潇**  发出测试bug表，主要集中在网页显示部分。
#### 2019.05.08
**何旭晨** 5.8G在30米处测试速度还是会到0应该和的灵敏度是一个问题。  
**郑达**  小基站给的配置无法注册。和何工今天一起去西安验证速度。
#### 2019.05.06
**何旭晨**  5.8G的灵敏度还不行，在30米处测试速度还是会到0。主要是电路修改太大。和软件貌似没有关系。第一版的问题是5.8G天线不行。  
**郑达**  昨天的工作基本完成，upnp没有起作用。余辉试过关闭防火墙就可以了。要追测试的开始大量测试。  小基站测速下午开始搞。发布版本1.03  <hide>
实现多nat，并提供设置接口（封远钊）  
实现nat lookback功能，并提供接口设置（封远钊）  
实现arp绑定功能，并提供接口设置（封远钊）  
tr069: 实现apn设置（江义波）  
防火墙：解决某些接口读取ip地址不正确的bug（封远钊）  
web: 实现2.4g 5.8g wifi的快速设置页面（向杰）  
web: apn添加nat功能（向杰）<hide>
#### 2019.05.05
<font color=red>需要按照 zs321的样子之类写一个规格书。</font>
mtk提供的openwrt bb的代码在git@192.168.1.249:mtk7621_sdk中。看看李柱栋能否在其中找到pcm的相关代码。必须使用smb://192.168.1.93/mysite/dl.rar 中的dl文件才能编译，就不管了。它的版本较di  
**郑达**  今天和封远钊，江义波，向杰开了晨会，讨论今天的任务 <font color=red>当前模块和wifi不支持单天线的信号检测</font> 发出版本1.02， <hide>web: 修改主页，拆分为主页,wan状态信息,lan状态信息,4g信息,wifi状态信息（封远钊）  
默认关闭telnet功能，配置可开启（郑达）  
web: 解决网页多apn设置不正确问题（封远钊）  
实现多dns功能（郑达）  
web: 导航栏隔10s刷新一次（向杰）  
web: 解决时间读取问题（向杰）  
web: 优化apn设置（向杰）  
添加读两个4g天线的内外置状态接口（郑达）  
web: 静态路由接口名称改成指定接口（向杰）  
web: WAN information中信息展示进行修改（向杰）  
web: 将路由设置添加到主菜单栏（向杰）  
web: 将tr069添加到主菜单（向杰）  
web: DHCP中添加Main DNS 和 Vice DNS（向杰）  
修改wifi wps的接口（封远钊）  
解决防火墙端口转发问题（封远钊）  
web: 增加dmz功能（向杰）  
解决dmz设置问题（封远钊）  
产测: 完成写imei, mac功能（郑达）  
新增tftp alg功能（郑达）  
修改lanrecord历史记录问题（封远钊）  
新增miniupnpd（郑达）  
tr069: 增加历史上报节点, 和多ssid apn的节点（江义波）  
重启设备时，在uboot去复位modem.（封远钊）  </hide>
#### 2019.4.29
<font color=red>wifi测试的时候要测一下实网  
是否可能从软件上设置usb3.0降为2.0  
    宽翼的小转接板是否有外接电源  
    板子要做emc  
    cpu是否存在降频的可能，导致速度不足？  
    cpu是否双核都在工作，还是只有单核在工作？  
    以太网udp只有200M，和变形金刚比较一下。取到nat比较一下  
    需要验证igmp v3是否支持
    </font>

上午开会讨论cat6测速问题：  
usb3.0其实对2.4g, 5.8g有干扰，可能wifi不能用的。 何旭晨：测试的时候有卡，应该还是可用。  
宽翼认为在pcie下方需要加泡棉，散热。  
宽翼认为手压住模块能明显提高速度，可能是接地和散热的问题。只有某个人按才有效果。  
去掉屏蔽罩，效果有改变  
在我们的板子上，比模块直接连接到pc要慢  
陶嵩 我们租的机器没有打流的license  
使用usb是因为简单，如果用pcie，很多模块都没有驱动。  
#### 2019.04.28
**郑达** udp问题确实解决了，iperf3可以打流到80多M，但是wget变得非常不稳定，使用多个wget，速度反而下降了。最高能到30MB。  
**向杰**5.1前可能没有空。人事招人那里没有动静。问tftp alg是啥东西。  usb 2.0 理论速度可以到450M，貌似没有必要使用3.0的样子。  
使用以太网卡lan wan打流，tcp两个方向可以到600-700M，udp两个方向都只能打到200M的样子，在udp的模式下，softirq的占用率会非常高。  
开始测试upnp。上次余辉测试的情况是只有汪光华那台电脑能出现额外的端口转发指令，自己的和测试的电脑都不能。
**江义波** 上周来了3天，调了2天的p59。
**何旭晨**：2.4g 指标已经调好了，5.8g pa厂家还要调。距离还没有测试。第一版测试的情况在110m左右2.4g能用1MB的样子。
#### 2019.04.27
宽翼乔总发了新的驱动，解决iperf3 打流问题，之前没有考虑到一个报文中有多个skb子报文的情况。
#### 2019.04.26
硬件部分，wifi部分改动较大，今天设备来了，开始调整。主要是高信道接收灵敏度不行，距离也不行。提到修改软件参数的问题，以前郑达已经对照变形金刚版修改过一次了。  
**向杰** 需要增加wps 2.4G 5.8G, home空白界面填充， 增加sn等  
**封远钊** 解bug, 增加arp绑定，upnp， 防ddos，快速设置等  
**江义波** tr069 升级事件上报，对数据，还有https支持验证，需要连到罗厅的平台。原来国外的某个平台的https已经访问不了了。  
模块打流挂掉的情况，宽翼那里没有仪器了。节后乔总过来深圳调。  
开关机测试已经超过1000多次，如果直接ping 互联网ip可以在60秒内完成。如果ping域名会有失败的情况。  
**多apn和多ssid已经完成，需要斯里兰卡验证一下。**  
开机的时候硬件并没有去reset模块，所以重启的时候模块并没有重启，可以考虑在uboot中完成重启模块的操作。  
厂测工具正在做，需要完成imei， mac， 升级，4g信号等。  
这10多天碰到一次模块重启的现象，出现usb disconnect。  
**李柱栋** slic部分操作看起来正常，现在需要at打电话的指令，看看音质如何。pcm部分需要加上alsa支持，需要至少3周的时间。  
**王伍** **要测试一下纯路由情况下的以太网的打流情况。**
#### 2019.04.22
**罗厅** 江哥明天w20那边有点事情要弄，周三过来
#### 2019.04.11
**何旭晨** 网上买华为的cat6都没有增值税发票，今天下了一个900多的。
#### 2019.04.09
**郑达**  cat6当前主要问题是模块不稳定，现场测试会从cat6脱离。
#### 2019.03.13
李柱栋：mtk没有对pcm的支持，估计做voip的时间就很难估计了。
#### 2019.03.12
郑达去了西安。准备了在宽翼需要完成的任务
李柱栋：看起来宽翼模块的时钟出来了。
#### 2019.03.11
郑达：联系了宽翼，还是明天飞到西安去一起调试模块。和封远钊一起去，把余辉的电脑带走。他开始想重新用一个sshkey。忘记了com邮箱的密码，重置它刘汉琴说要找彭丽玲。
#### 2019.03.09
何旭晨：宽翼没有回复模块的交期。6号已经投板，大约在18日可以回到研发部。
郑达：喻潇这段时间一直在做v10方面的事情，还没有时间进行cat6的测试。李柱栋推的那个内核代码是为了自己调试方便的，否则每次clean太慢了。说搬近了.
#### 2019.03.06
郑达：2.4g的wifi性能应该改了参数就有效果了。修改的是apcwimin, apcwmax, aptxop这几个参数，这几个参数在atheros中的配置是在WMM Parameter Definitions中。王伍让他再去招一个做web的人。
#### 2019.03.05
李柱栋的spi切换的还在看dts这个东西。
#### 2019.03.04
李柱栋对spi的复用还有疑惑。
#### 2019.01.09
**郑达**  [MTK多SSID配置说明](http://192.168.1.93:8000/s21_cat6/MTK%20%E5%A4%9ASSID%E9%85%8D%E7%BD%AE.docx)
