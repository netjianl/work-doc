

#### 2019.10.16

**余小虎** 给中兴发邮件询问向南京发包的问题。

**皮晓聪** p53的更换strongswan可以使用ipsec了，发现当前编译的程序dnsmasq在dns解析上错误，只有不使用nobody这个模式，才能正常。而以前编译的都没有这个问题。
在7520上是指定了dnsmasq的用户和组的。

**白俊剑** 发出m60和p28版本：
针对DIALOG提出的隐藏普通用户下多SSID设置的需求，现发布M60 V3.26和P28 V1.33版本程序。
由于从上一次版本发布时间2019年1月到现在，软件做了一些容错性质的修改，所以这次我一并合入了新版本，更新和说明如下：
更新说明:
1，boa:由于chrome更新后不识别Content-Length中带空格，修改组包方法
2，tr069: 针对cwmp.conf做一些保护及恢复措失
3，tr069: 优化配置上传功能
4，tr069: 完善transfer complete规范
5，应dialog要求，将普通用户的多SSID相关功能隐藏，operator下保留设置
重点测试：
1，验证“多SSID设置，多APN设置，多DHCP设置，多NAT设置”这几项是否在普通用户下隐藏，在管理员用户下可用
2，程序可正常通过TR069、WEB升级

#### 2019.10.15

[Windows 支持 OpenSSH 了！](https://www.cnblogs.com/sparkdev/p/10166061.html)

**吴曦**  余小虎节前催的急，现在还没有送测。

**皮晓聪**  换strongswan版本试试。

**梁柏华**
您好，附件是Newww客户S10 Pro初版程序版本信息表格，请查收，路径：
\\192.168.80.107\V3R06_新flash分区\S10Pro\墨西哥_Newww\20191015_master

配置版本：S10_V3.3-0466
软件版本：V1.03

todo:
10.19 中信银行信用卡
10.15日开始扣贷款的费用了。银行在东涌吉祥东路2号。坐车过去要好久。二楼面签室。
做一个脚本，得到链接上三个楼盘的卖盘放盘情况。
在脚本中增加一个统计功能，放盘的退出时间。
让皮晓聪开放我的机器对路由器的管理权限。看看华三是否可以对不同账号的l2tp拨号进行相应的网络处理。
我的s21貌似不能上网
win7,win10 必须能拨上这里的vpn，否则出差非常麻烦。
学会如何对java平台编译，部署。
写一个自动下载，自动编译的脚本，检查每个仓是否可以一次编译。每个仓轮着来编译。
重新摄像头android app，看看事件列表是不是自动有了缩略图。
p53 EM7455 问徐工是否要改电路
把新增加的东西加入到测试表格中。

#### 2019.10.14

**皮晓聪**  使用p53的编译器，编译ipsec运行会出seqment fail的错误。在p59上运行正确。

**梁剑**  摄像头现在可以做到，如果没有授权文件，那么推流会有随机延时。

**罗厅**  手环的软件结构是以接入程序为中心点，其他网页平台，app，设备都是和接入程序交互，并且是长连接。
tot张悦玲还没有时间搞。
罗鹏还可以，已经上手了，

**任银善**  还在看那个vpn为什么会报错。

**郑达**  安排杨谋均改写一些程序，看如何在程序中不使用system执行iptables的命令。模块重启还在挂测。

**陶嵩** ：不注册网络的机器之前信可有发现是用户锁频的原因，为了杜绝这部分机器，
将不注册网络的机器加载一下空配置后再试一下。


#### 2019.10.11

**梁柏华** 
S30程序更新，路径： \\192.168.80.107\zte7520v3E\程序\S30\20191011
修改：
1.反转电池充电开关
2.网页显示电池格数
3.修复电池灯在低电状态下，接外电，然后再断外电，电池灯无法还原到应有状态

S30程序路径： \\192.168.80.107\zte7520v3E\程序\S30\20191011
修复wifi灯相关的bug
电池灯7.2V亮黄灯，6.7V闪黄灯，7.2V以上蓝灯

**叶川** 在没有存储频点的情况下（比如第一次开机），对UE支持的band进行全扫描。
在有频点的情况下（比如全band的扫描结果、系统信息配置的频点等），对各个频点进行小区搜索，主要是PSS\SSS的探测。
全频段下的FDD\TDD扫描优先顺序可以通过AT设置 

**余辉**  v3e平台柬埔寨Smart S10版本1.11程序路径：zte7520v3E\程序\S10\菲律宾-新主分支\S10\20191011_smart

#### 2019.10.10

**梁柏华**
 附件是给PINGCOM客户，带生产配置的程序，ACS URL为 10.160.254.9
 生产配置为Pingcom-CONFIG-V1.17， 客户能在网页上看到的版本是Pingcom V1.05
 以下两个程序是给客户测试tr069升级功能使用，在网页上能看到的版本分别为：Pingcom V1.06.1 、Pingcom V1.06.2 
 P21_v3_Pingcom-V1.18.1-updatecfg_ML100+_CPE_1E0XXX_V1R05B01T02P34_1.41.zip
 P21_v3_Pingcom-V1.18.2-updatecfg_ML100+_CPE_1E0XXX_V1R05B01T02P34_1.41.zip
说明：
 1.客户需要测试URL为 10.160.254.9 设备是否也能正常工作
 2.先通过网页升级附件中的程序：P21_v3_Pingcom-CONFIG-V1.17cfg_ML100+_CPE_1E0XXX_V1R05B01T02P34_1.41.zip
 3.然后再使用测试程序测tr069升级功能：       
      P21_v3_Pingcom-V1.18.1-updatecfg_ML100+_CPE_1E0XXX_V1R05B01T02P34_1.41.zip
      P21_v3_Pingcom-V1.18.2-updatecfg_ML100+_CPE_1E0XXX_V1R05B01T02P34_1.41.zip

**梁柏华**
您好，附件是VOLACOMM客户版本信息，请查收，程序路径如下：
 \\192.168.80.107\程序\V3R06_新flash分区\M60a\VOLACOMM\M60a_volacom_20191010
  M60a_volacom_20191009 程序已删除      
修改：
1.添加配置控制自动呼出时长
2.在状态页Status中添加3G Signal Strength和LTE Signal Strength
3.GUI上的"Wifi Mac" 改成Wi-Fi MAC, Lan Mac 改成LAN MAC, 且两个值都为同一个值
4.serial number只上报完整的IMEI
5.配置主题色改成可选模式
6.添加隐藏wifi菜单的配置和功能
7.避免开启pass_route以后，tr069无法正常运行
8.登录密码最小长度不做限制
9.修改当升级文件不存在时，脚本没有检测报错，升级程序也没有检测就先擦除uboot的flash，导致M60A设备起不来的bug。

**梁柏华**
 您好，附件为PINGCOM 程序版本信息，请查收
 给客户测试的程序有两个，方便客户互升测试， 程序路径：
 //192.168.80.107/zte7520/程序/V3R05_老flash分区/P21K/20191010_master(Pingcom)/
生产程序：
   //192.168.80.107/zte7520/程序/V3R06_新flash分区/P21K/PINGCOM/20191010_master/
修改:
1. Revert "Pingcom: 根据客户需求，升级带配置程序，不更改ACS URL"
2.升级的配置中不没有ACS URL，ACS username, ACS password, CPE username, CPE password

**梁柏华**
 您好，附件是科迪瓦特Orange程序版本信息，请查收，程序路径：
 \\192.168.80.107\程序\V3R06_新flash分区\M60a\科特迪瓦Orange\orange_20191010
 orange_20191009 程序已删除
修改：
 1.修改当内核分区出现坏块的时候，网页升级包会升级失败同时会把设备升死的bug
 2.修改当升级文件不存在时，脚本没有检测报错，升级程序也没有检测就先擦除uboot的flash，导致M60A设备起不来的bug
 3.tz_phone: 网络设置菜单实现不正确，先去掉

**祁俊平**
１.以下是低电的情况，不建议特别修改设置，因为电池低电时会掉的比较快，差的电池会更明显，关电太晚不定会走完关机流程。
nvram_user_config.c 中
kal_uint32 const NVRAM_EF_CUST_HW_LEVEL_TBL_DEFAULT[] = {
下面  /* Battery voltage Level */
                  3350000, /* Low Battery Power off */
                  3550000, /* Low Battery */
                  /* battery level 1 ~ 8 */
                  3600000, 3700000, 3800000, 3900000,
低电关机是3.35Ｖ，低电报警是3.55
２.控制是否允许禁止休眠，对每个模块都是公平的，需要不休眠时就禁止，完成事务要休眠就允许休眠。没有所想的接口。
L1SM_SleepEnable
bt_uart_sleep_handle= L1SM_GetHandle();
L1SM_SleepDisable(bt_uart_sleep_handle); 
３.按键周期的设置目前还没有客户特别去修改，不建议贵司随意去更改。

**汪光华**
1.目前3.6v左右低电量自动关机，在哪修改3.6v这个变量,比如我们想改成3.5v自动关机；
2.有没有接口使终端直接进入低功耗状态；
3.按键KEY_LONG_PRESS长按大概2秒，由于怕用户误操作，有方法改成3秒吗

邮件服务器容易收到伪冒发件人的邮件。
**江健** 1.系统运行缓慢，清理了C盘垃圾文件，腾出虚拟缓存空间。
2.SQLserver数据库运行异常，4个数据库占用了高大1.7G的内存，修复后占用学50M
3.卸载了360杀毒，替换成了腾讯管家，卸载了一些服务器上用不到占用内存的桌面系统插件
目前cpu和内存常用占有率很少超过30%了。运行很流畅
4.修改了邮件服务器的几项策略包括
a. 启用了国际反垃圾邮件的nbl, MDaemon自带的spamhaus
b.因为邮件系统版本比较老，11.03，现在好像有19的了。不支持DMARC协议。只开启了自带的spf, IP黑白名单，垃圾邮件学习，内容过滤规则。
a规则可能带来的负面影响是，如果对方服务器进了垃圾邮件服务器列表，不去处理，就会被我们的邮件服务器拒收，所以如果有客户反应的时候，可以建议他们去移除或者将客户加入我们的白名单
b规则需要样本学习，需要时间慢慢生效，MDaemon自带有学习功能

10.10 还建行信用卡
杨谋均的硬件调试貌似没有动静。杨谋均正在做v10的东西。
https://blog.csdn.net/russell_tao/article/details/9171375

继续收到伪冒的邮件，江健认为是我们的服务器需要调整MDaemon的策略，启用它的垃圾邮件过滤器，启用DNS-BL这些。

s30的wifi按键似乎有些问题。

http://ftp.gnu.org/gnu/gdb 是所有版本的gdb下载地址。

结合白俊剑的邮件，写分组的详细划分信息，算了。

#### 2019.10.08

天门新增省直辖市，我们的平台中没有该行政区，需修改平台（9/11已完成）这个修改看起来没有在代码仓中体现。
江健 从高德地图上取的点是按照画折线的方式的数据，要改造成画多边形的数据，在我们的平台上就没有问题了。

#### 2019.09.30

**刘云** L2TP BCP功能 前方反馈1.2版本不能TR069降级到1.1，我们这边验证好是可以正常升降级的，而且升降级前都有上报TransferComplete.已让前方进一步帮忙确认。

java_tot中，罗鹏有提交，郭伟没有。
**罗厅**  看他们的情况 应该还在熟悉代码，比之前那个开发进度会慢

**吴曦**   P11M与W13+的语音方式主体框架如下：
1.控制流，通过TCP/IP实现，命令格式通过JSON来做。
室外机作为server端，室内机作为client端，保持长连接，并且有心跳检查，断线必须重连。
室内机将所有按键上报室外机，由室外机根据不同按键下发指令给室内机播放声音或者发往cp协议侧完成拨号、切换等
如DTMF音不能去除带内模式，那么就将协议层的dtmf音做接口保留，默认使用带内透传。
2.数据流，通过UDP实现
室外机作为server端，室内机作为client端，保持长连接，并且有心跳检查，断线必须重连。
上行：室内机将音频数据包直接发给室外机，室外机再通过核间通信丢给cp（具体接口参照VOIP实现）。
下行：反向执行
暂时数据流使用8K 16位 PCM数据传输。
个人感觉此方案与voip非常相似，所以建议使用TZPHONE来实现，替换原来的按键获取接口，基本可以完成控制流。
室内机的pcm可以完全放给数据流来使用，应该不需要考虑语音切换等问题，具体得看实际情况。
如P11M设备不够，可以使用P25K设备下载P11M程序进行调试，分支在fonap_slt的基础上创建。
初期内部调试可以将音频文件导入室外机，再传输到室内机进行测试。信可预计10月20号左右能提供测试联调程序。

#### 2019.09.29

找一个有app的华为设备，做一个设备管理的app。已经买到了。

**余小虎** 11X送测首版程序报告 9.26 Dialog已提供测试报告，部分已解决；

**刘云**  柬埔寨Smart-S10(V3E) 端口转发菜单命名改成虚拟服务器后，客户很接受。

**苗立双** 使用华域9x07模块开发的ZLT P56 V36程序; 主要修改:
基于V34版本;
升级版本到V36;
增加对配置命令cfg调试的支持;
优化网页修改语言的处理,将修改语言后的网页放到内存中,减小写入FLASH次数,降低FLASH坏掉的概率;
优化连接跟踪无交互保留的时长为10分钟,优化对视频数据的处理;
修改语音优选项,变为PS ONLY;
修正检测程序是否正在运行的函数潜在的bug;

**余辉** SLT P28 2.00 版本
        1.配置控制隐藏多DHCP,多nat，多apn的菜单 
        2.添加隐藏wifi菜单的配置
        3.voip:修改按flash+4后没有进行转接的bug
        4.需要将配置  DTMF模式  设置为slic 透传    此设置解决voip 1212DTMF问题
        5.去掉goahead进程中，当wifi关闭或者裁剪掉后，还会去获取连接个数，同时会导致不断吐fail的log。

**梁柏华** 
M60A SLT 投标版本V1.51
1.修改当升级文件不存在时，脚本没有检测报错，升级程序也没有检测就先擦除uboot的flash，导致M60A设备起不来的bug

**郑达** 这是s21 版本：1.36
封远钊：修复工厂生产时生成校验页面概率出现模块信息读不到问题
蔡松延：tz_phone:tz_phone关闭时也把srsip、mislic关闭
董锡文：实现了Advanced Settings页面PCI Lock分页点击PCI SCAN按钮post请求成功之后2秒钟过后才可以再次点击的功能
封远钊：修复型号配置项带空格时配置生成失败bug
巢丽媛：修改WiFi2.4g和WiFi5.8g--主WiFi设置功能关闭时，辅WiFi标签的隐藏规则
巢丽媛：隐藏WiFi设置页面中帮助信息的加密算法提示句
郑达：防火墙: 解决防火墙设置规则丢失导致的INPUT OUTPUT FORWARD全都为drop的bug.

**苗立双** ZLT_P19H_V2.9.1_for_web_upgrade_2019_09_27_15_45_32_V2.9-Zambia.sfp
V2.9基础上编译的赞比亚专用程序;
修改版本为2.9.1;
首先扫描频点41692,然后在扫描Band 42,Band 43;

**徐刚雄** 由于硬件和结构之前的第一版都有问题，后面紧急改PCB板，改结构手板
给客户的样机就推迟到了10月10日，之前有微信跟你沟通，
10月10号是目前现有状态的样机的送样时间，
后面改成跑马灯的客户需求，硬件还需要再改一版，给出控制方式和管脚后，软件也可以评估一个完成时间。

那个旧仓在249上要换位置。

#### 2019.09.27

手环的仓已经推。9x07仓已经推
去掉曹志远git权限
cat6上的tracert貌似完全没有用
2019.9.27 还招行信用卡

[正则表达式30分钟入门教程](https://deerchao.cn/tutorials/regex/regex.htm) 看起来有些复杂。
[正则表达式在线判断](https://deerchao.cn/tools/wegester/)
 \| {1,6}Bin\b  这个可以匹配git show --stat里面对bin文件输出。

**蔡松延** 光项目已经编译通过。

#### 2019.09.26
todo:

写一个代码仓验证脚本，找到以下问题: 一次提交太多文件，提交bin文件，代码仓太大。一次编译失败。
下次执行11月，清理249的git仓，去掉3年前的仓。
去掉voip那台机器上的我的私钥。

vim和cat看到的居然不是一个编码。

**刘永辉** 客户要的预期结果是user账户下隐藏，Operator下要开放

**苗立双** 中东客户P21 B42/B43 三级账户还没有开发;

**李光达** 菲律宾S10G最新程序，隐藏了电池图标和修改了客户反馈的问题。

**刘永辉**
P21K_SLT_05 voip 拨打1212热线电话，依次输入3>2>1>1>10位号码；出现异常现象
1、热线电话的智能语音播报断断续续
2、输入10位号码的时候会重复；例：输入1234567890，播报1122334566或播报1223345667
（M60A表现正常）
P21K_SLT_06 一路保持一路通话；按flash+4转接失败

**郑达** 这是V10当前最新版本：v1.95
增大清cache力度：每10s检查一次，小于4.5M就清一次cache.

**蔡松延** w13+V2.7程序发布
        1、新增使用交换机批量升级的功能；
        2、新增voip功能，包括页面和产测功能（授权和室外机设置参数还没有）；
        3、连接上室外机时，会把自身web关闭，此时如果IP与室外机冲突，会将自身的IP清零。
        4、升级配置页面允许文件名带‘+’号

#### 2019.09.25


find没有忽略大小写的写法，使用管道代替 例如 find / |grep xxx -i

**喻潇**  按照提供的PDF文档，转成WORD后大部分格式、表格都乱了；所以只是采用了一部分，已经尽力完善了；VOIP没动；

**罗厅**  在买华为的设备。

**刘永辉**  西班牙Fon认证指导说明书

**刘永辉**  M60A我尝试修改配置
       隐藏SSID1，SSID2，APN1，APN2，DHCP1，DHCP2（配置没找到多NAT隐藏）
   测试结果为：除了SSID1，SSID2，其他菜单均无法隐藏

**Louis**  发出bcp修改要求。

#### 2019.09.24

这样可以折腾一个带时间输出的ping
ping 127.0.0.1 | gawk '{print strftime("%Y-%m-%d %H:%M:%S") "\t" $0}'

120.197.116.46 huarun huarun 还能拨入。

**巢丽媛** 一、S21项目
	（1）修改设备升级后概率出现登录页卡死的问题
	（2）查设备运行时间长的时候出现页面响应时间过长的问题
二、V3项目
	（1）熟悉V3项目前端代码

**董锡文**
时间	项目	工作内容	人员
2019/9/18	S21	解决了整个lua接口请求和响应cmd的问题	董锡文
2019/9/19	S21	实现了WiFi-2.4G和WiFi-5G页面主和辅wifi修改字段值点击Save按钮之后仅post对应字段的数据的功能	董锡文
2019/9/20	S21	实现了新增的Advanced Settings页面PCI Lock分页的PCI Scan Range字段的内容显示及其功能	董锡文
2019/9/23 - 2019/9/24	M60a	正在熟悉M60a项目和实现SIP Server页面新增的双账号及每个账号的server1和server2的部分页面功能	董锡文

**向杰**
V3：
1.升级过程中返回添加version_error状态
2.LTE INFO添加L2TP连接状态
3.添加中东客户MTN定制化需求
V3E:
1.处理菲律宾客户安全测试
2.合大版本之后导致页面中定时刷新的数据请求概率性报错问题。
3.添加配置控制网络设置中WAN模式的显示隐藏
4.添加WAN口，PPPOE功能。
5.修改smart客户定制化需求

**余小虎** dialog V10S
用户投诉：CPE hand till reset  客户反馈该问题的现象是“长时间使用无法呼入呼出，重启后正常”，应该是软件问题，而不是之前的PA问题；由于该问题很难复现，而上周中兴/尧远提供了测试程序，今天发给Dialog，请他们找几个容易复现问题的用户推送升级，看是否能复现。
使用市场投诉机器，复现掉VOLTE问题  Dialog反馈很多方投诉V10放置一段时间出现无法呼入呼出问题，网络侧查看无volte pdp；今天提供尧远测试程序给dialog挂测；

**刘云** BCP功能已连通，网页状态显示问题需要修改判断条件，同时完善SNMP里面L2TP节点上报。明天出版本到前方测试。

**何旭晨**  在找每个ddr寄存器的值。

**李建华** 明天看看华为b310有没有手机端管理。

**毛祖潇**  喻姐在8月28日在公司内部测试过2.12 tr069升级到 2.15，是可以正常升级的
**余小虎** 客户是通过TR069升级。
**白俊剑** 这个问题之前不是已经确认了么？SLT使用的浏览器版本低导致。
**余小虎**  SLT准备将旧版本M60升级到V2.15，现发现从2.08升级2.15失败

**喻潇** v10s信号格数SLT需求验证完毕.

**郑达**  V10当前最新版本：v1.94
更新说明：
新增配置选项：信号格数计算方式选择 dialog/slt
实现信号格数通过rsrp和sinr计算得出，并更新到话机侧显示。

**叶京平**  秘鲁客户的技术需求表，我填了一下，我们的CAT6 CPE-S21可以满足

**林琼宜** pingcom出货模块选择 出货要用E.1的模块。

**任银善**  早晨用mikrotik模拟了l2tpd server不分配ip给client的情况，用s12测试了一下。确认ppp0没有地址，也没有up。但是再ppp0 down的状态下，我测试是OK的。
中东那边，我们可以再次确认下，ppp down的状态下，是否可以通。我昨天测试好像确认不行

**王丽娟** 板卡还没有买。

**吴曦** 给陈伟平邮件，确定是否可行。我看你这边和中兴微改动会比较大，我们这里的话，只是调用你们的接口就好了。

**苗立双** 苗(Miao):没有这样试过,一直是远程抓包,因为阿根廷的人也没有说过这个事情
苗(Miao):因此怀疑是他们那个环境有问题
苗(Miao):并且公司环境经常有人要进行测试
苗(Miao):很难持续性抓包查看

**王壮**  客户反馈的CPE disconnect 
从抓的log以及你的截图对应位置， 我没有发现LTE这边有断线或者包被丢弃的问题、 
你的测试是持续ping wan IP。 这种丢一个包的情况也是有可能由于系统调度随机丢弃了， 
这个跟下面客户反馈的情况似乎并不是一个问题。 客户说是短线2分钟后恢复， 而你这边的测试我觉得并没有复现他的情况， 因为LTE这边如果因为某种原因开始丢包， 但是wan IP 还在， 
你从lan口去ping wan ip。 不会走LTE链路， 所以就算问题发生了， 你这边的ping也不会有长时间的断开。

**刘云**  和前方远程分析，发现连接建立中PPP0是无IP状态，手动拉起PPP0后就可以了。需要和英国那边讨论下noip如何设置配置下。另外，BCP连通后，记得同步snmp里面相应L2TP BCP状态参数的上报。


**毛祖潇** 中东客户P21 B42/B43 3-4个用户连接P21并开始下载，速度达到40Mbps，CPE freezing或者重启。苗工认为可能是内存占用过大，需要小基站到公司时进行模拟

**余辉** S10G网页安全测试修改：
        1.修改火狐插件显示隐藏界面bug
        2.将22和5555端口由DROP改为REJECT，修改网络安全扫描的端口问题。
        3.菲律宾安全测试去掉443,52881,5060端口

**余小虎** 提到主路比辅路低30dB，是RSRP吗？ 有没有AT可以查询主辅两路的值？

**马岳振**  V10S Dialog B40注网失败-0923 这台机子，主路有问题，比辅路低了30+db。是不是主天线没接好啊？

**刘云** 中东第三家运营商V3.x程序需求 根据运营商需求出第一版V3.1程序。同样要求V3.x只能和V3.x互升，不能和V1.x/V2.x/V4.x互升。
09.23:收到需求，和吴曦初步讨论，对程序包里面配置带的版本号进行判断。单独升级配置的改动太大，先通过隐藏Root账户下的升级配置菜单来实现。
菲律宾S10G:
1，安全测试的问题研发新发了版本，光达晚上10点还在挂测，顺利的话24号可以发个版本过去前方测试。
2，晚上和Jef碰了下，他那边已经准备好了用于NTG网络部门的测试的机器，但是NTG还未启动，已让他帮忙推动。
#### 2019.09.23

**赵金** 已完成的工作：
1、福智服务器数据库重新部署                                                                   
2、配置工具批量多需求的添加
3、P19机型新增SN号写入及校验测试
4、S21机型修改天线测试方式及增加语音测试工位
5、智能手环的开关机串口测试工具
6、C78摄像头的产测工具和配置工具的测试和调整以及工厂的工具使用部署

后续开展的工作：
1、查找在线打印慢问题的原因                                                                   
2、通用打印机身标工具的编写测试                                                               
3、WIFI连通性功能工位的修改测试                                                               
4、智能手环生产工具的编写准备
5、深科数据库服务器的更新及部署
5、各加工厂各种生产机型技术支持（数据清理、数据上传、问题配合解决等）   

**余小虎** 53端口需要开启、可以跟客户解释，443/5060/22/5555几个端口要处理。
修改的时候，建议大家帮忙一起审查代码，并进行自测。Globe要求高，且这次出版本预计只有安全测试重测，其他已完成测试不会重测，务必确保修正bug的同时，不引入新问题。
V10S Dialog B40注网失败-0923 返修问题是（B8+B40）无法驻网，我们更换新模块后仍然有Band 40驻网问题，Band8驻网正常。
B40驻网问题，除如下描述的“有时开机不驻网“外，有时还有“开机能驻网，信号质量正常，放置一段时间后RSRP会从-80dBm掉到无信号，尝试抓包时又不复现”。

**杨谋均**  关于apn注册状态的系统日志显示，上周三也已经加上了。

**蔡松延**  关于voip状态的系统日志显示，上周三已经加上了。

**郑达**
>>>>>>>>>>蔡松延：
voip 開機註冊問題:
    voip 會註冊不上,要求addy加上註冊失敗碼, 並處理註冊不上問題  -- 據稱定位到問題，是多個設備共用一個賬號導致，需要在掛測該問題的時候，重啓設備前先註銷掉再重啓。目前迪拜掛測中。
串口服務程序　--預計今天能出初版
tz_phone volte功能   --串口服務程序初版後，預計明天開始。

>>>>>>>>>>封远钊:
wifi 5.8g tkip方式連接不上問題查看(解決問題之前,會先把網頁tkip和auto兩種方式先去掉)   -- 光貓上的驅動與s21是一樣的，對比驅動本身無區別，但中興tkip可以正常使用，小蔡稱中興對wifi有修改。建議远钊對比中興編譯路徑下的5.8g wifi驅動，可是否編譯時才打上了一些有用補丁。
tr069遠程重啓功能，客戶反饋有時候重啓的event事件沒有回到。----昨天諾基亞人員沒有時間，看今天能有機會測試不。
s21 plus: 本週開始對新硬件進行調試。

>>>>>>>>>>杨谋均:
s21 plus: 本週開始對新硬件進行調試。
項目遇到的問題：

1.發現最新版本還是會發生重啓問題 優先級： 最高
        觀看dmesg頭部, 覺得還是有點不太對, 目前掛兩臺去年12月份的版本中.
　　 還得看如何加速排查問題，加大測試量，以及查找openwrt資料
         去年12月份版本：2臺帶modem跑4天多未重啓
         今年2月26日版本: 2臺未重啓，跑2天15小時； 1臺發生重啓，看的時候跑了2天5小時
         今年9月份版本：跑4天多未重啓。

2.設備運行越久,網頁返回時間越慢
　　有兩個可能：接口返回慢；長時間跑系統性能下降，http服務能力下降，目前從接口入手分析
　　觀察到那臺非常慢的設備，文件描述符增多很厲害，有1800多。但是我手中掛的這臺，跑了4天多，就280多。
　　預計操作：
　　　　　　1. 找兩臺設備，升級到最新版本，測出該問題。
                            1. 通過砍應用去確認範圍。

3.在編譯服務器上編譯s21, 還編譯不過
　　開遠程給搞加密的人去編譯看這個問題。而且反饋是小文件出了亂碼問題，還不會去解決的。

4.產測反饋的網口連接口，50多秒後才能ping通．
　　網口驅動的加載要在22+5s(uboot時間)，同時可能重啓了network，導致這個ping很慢，考慮如何優化

5.拉取最新版本openwrt程序
　　已經編譯成功，但dts文件裏沒有內存配置，決定先下載到板子裏去運行，掛測看能否正常運行跑起來．
　　跑起來後，reset 到最新正式發佈版本，嘗試移植wifi驅動．（看了下前前個release版本，會存在2.4Gwifi不穩定情況，所以儘量收集些資料，看目標release版本存在的一些潛在風險）

6.防火牆問題　優先級： 最高
　　迪拜反饋input 和output有時候被設置成drop，導致數據出不去問題。
　　計劃分步驟同步進行：
　　　　1. 查看openwrt firewall程序，查看drop是否是讀不到配置或者是讀出錯時的默認操作
　　　　2. 復現迪拜出現的規律，看是否特殊操作導致。

7.配置保護問題
        思考並實現配置保護功能。

2.4g wifi速率慢
        需確認wifi打流速率問題，需與何工討論。

**余辉** S10G网页安全测试修改：
1.修改火狐插件显示隐藏界面bug
2.将22和5555端口由DROP改为REJECT，修改网络安全扫描的端口问题。

**刘永辉** V10S Dialog B40注网失败的log
    步骤1. CPE1装SIM1开机，无法驻网
    步骤2. CPE1装SIM2开机，可以驻网
    步骤3. CPE2装SIM1开机，可以驻网
    步骤4. CPE1装SIM1开机，可以驻网
请尧远的兄弟帮忙看下【1. B40开机注网失败-CPE1_SIM1.zlf】为什么会注网失败

**陈良** 验收测试已经接近尾声，目前已经发现的比较严重的问题就是防火墙启动的时候有概率性的会把路由参数写反，从而导致设备LAN口和WAN口的数据都不通，暂时还未定位到问题在哪里，请各位抓紧时间修复
基本功能相关：1.34版本测试
1. WIFI工作异常，5GWIFI无法连接，手机上连接后显示网络拒绝连接,2.4GWiFi可以连接，但是测速速率偏低.--重点
---新版本使用手机测试，5G可以正常连接，测速可达112Mbps/7.09Mbps, 2.4G测速可达62.3Mbps/9.91/Mbps
2. CA切换激活/关闭状态，设备无法自动恢复,需要重启设备才可以.---相关日志和截图已经发给宽翼那边.
---在实网下测试设备可以自动恢复，已经抓取了相关的日志和视频，视频已经发给华为确认。
3. 实验室这边就一个B41的测试基站，物理小区ID是356，但我们的设备经常能扫出ID为87的小区出来.
---宽翼那边没有什么好的办法可以证明这个基站的存在，只能加了一个过滤条件，把RSRP小于-110的领区都过滤掉。
4. 锁PCI功能，设备在被锁定的情况下，如果VOIP正在通话的情况下,没有完全禁止掉,还是可以听到对方的声音,应该是只拦截了出去的包.
设备在被锁定的情况下，IPTV需要4分钟左右才能被禁用,这个需要优化下.明天上午再找时间远程看下.
---这个功能还有些问题，今天远程让郑达手工改好了，明天好需要出个正式版本.@郑达 
5.系统日志,需要添加一些日志,类似于APN注册失败,重新注册成功,VOIP注册失败,重新注册成功这些,有助于故障排查.
---这个还没有加上去。

小汽车竞价密码sosolong

把mtk手环的仓推到南沙。这个仓太大，居然到1.65g，代码仓尽量只管代码，编译器，工具，资源等尽量写脚本，编译前去下载。
7520的tr069编译错误，使用原始的方式，应该是可以了。
周五晚上开始这里的p59和公司就没有断过了。


#### 2019.09.22

**余小虎** GLOBE S12海外样机需求表-S12--5台 S12是作为后付费(Postpaid)CPE，有频段和短信/通讯录定制要求，对此需求表里已经标注。

#### 2019.09.21

docker run -d --name boinc --net=host -v /home/jian/boinc:/var/lib/boinc -e BOINC_GUI_RPC_PASSWORD="123" -e BOINC_CMD_LINE_OPTIONS="--allow_remote_gui_rpc" boinc/client

**余小虎** 针对P21K和P11M，请务必确保LTE和WiFi性能，这是招标测试很关键的部分，其中WiFi性能建议使用Netpersec工具测试，务必确保速率稳定。
SLT 测试工程师反馈：2017年投标测试中，1860 P28的LTE和WiFi性能不佳，其中WiFi速率不稳定。

#### 2019.09.20

找王伍2件事情，一个中试不回测试表格。一个是给皮加薪。找了单总，年底有计划。
下载boinc的docker，设置只运行某段时间然后退出。
给单总回消息，表示看过了那个东西
把赵金的仓推到广州， 使用暂时没有碰到问题。
蔡松延: 修好了socket端口被占用的问题 现在注册不上就剩srsip注册不上的问题 差异就是socket端口不写死了，被占用会尝试换端口
吴曦  余辉和梁柏华已经在做张悦玲的事情了。可以考虑让做app的做一些其他的功能。
皮晓聪看起来已经把uuid编译的问题解决了。
陶嵩 明天开始休假
刘永辉  SLT P28(P21K) 今天简单过了下，现有以下两个问题：未登录页 无天线状态显示 需添加主辅天线状态
volte SLT“#92#”等#开头语音业务设置失败 建议不处理首个#按键

**封远钊** 附件是 S21 V1.34.

**吴曦**  中兴微海外项目未完成表											
优先级	机型	国家或地区	运营商名称/代理商名称	未完成需求	测试反馈bug	目前状态	需要完成时间	销售人员	海外技术支持人员	软件人员	备注
高	P21K	瑞士	PINGCOM	TR069 0 BOOTSTRAP ISSUE	tr069还会出现重启问题	9/20下午已解决TR069所有问题，等出新程序给客户最终确认	2019/9/6	林琼宜	无	梁柏华	
中	P25K(V3)	加纳	BUSY	信号比其他家差		等待修改	2019年9月5日	叶京平	无	吴曦	
高	S10G(V3E)	菲律宾	GLOBE	无	已更新新的网页安全报告，需要修改	安全测试修改完成，提交测试	2019年9月2日	陈玉	余小虎	吴曦	
高	LT90S(V2)	菲律宾	GLOBE	无	已更新新的网页安全报告，需要修改	安全测试修改完成，提交测试	2019年9月2日	陈玉	余小虎	吴曦	
高	S12(V3E)	菲律宾	GLOBE			等待中试测试反馈	2019年9月15日	陈玉	余小虎	软件：吴曦；   硬件：模块：陶嵩，底板：梁官	
高	S10(V3)	斯里兰卡	Mobitel		4G ONLY注不上网，4G优先可以				刘永辉	吴曦	
高	M60A(V3)	斯里兰卡	SLT			招标测试，准备程序中	2019年9月10日	陈玉	余小虎/毛祖潇	张悦玲	
高	V10S（V3）	斯里兰卡	SLT			招标测试，准备程序中		陈玉	余小虎/毛祖潇	张悦玲	
中	S12	加纳	Surfline		"偶尔出现无法注网的问题。虎哥远程抓log给中兴分析后，认为一个是可能频偏不对，偏差比较大，导致扫频性能差，扫不到，一个是信号弱导致扫不到"	"客户使用华为CPE做对比测试，华为未出现问题；同时客户使用我们的其他机型对比测试S10，P11，都未出现问题；"	9月13日	陈玉/陆洪丹	余小虎	吴曦	
中	P25K	加纳	Surfline				9月13日	陈玉/陆洪丹	余小虎	吴曦	
高	S12	中东	ARG		BCP试行失败，待客户提供测试环境			陈玉/陆洪丹	刘云	吴曦	
低	P11X	乌克兰	Anteniti	无	4G刚开始界面显示有信号，但是实际没有。3G可以用，切换到4G的时候，显示没信号，实际也没有。	测速视频已经收到，待分析	待定	欧阳菁华	无	余辉	
低	P21K			无	4G刚开始界面显示有信号，但是实际没有。3G可以用，切换到4G的时候，显示没信号，实际也没有。			欧阳菁华	无	余辉	
低	S10(V3)			无	外置天线切换不了			欧阳菁华	无	余辉	
低	S12			无	网速3-5MB			欧阳菁华	无	余辉	
低	M60A 	尼日利亚	Mobile eye 	SIP Server: sip.n2ncall.com; Port: 5060  Protocol: UDP  Codec Supported: Codec2, G723, G729, G711u, G711a and GSM.                                       测试账号1：username: tozed1    password: n2ncall Local Extension: 100                  iNum Number: +883510012860214                  测试账号2: Username: tozed2  Password n2ncall Extension: 102                        iNum Number: +883510012860283		等待样机支持G723 	2019年9月9 	廖媛	暂无	梁柏华	
低	S10 V3E  	尼日利亚	VDT 			客户提出需求 ：设备关机状态下，电池能充电， 并且能现在电池充电状态。 研发反馈要改硬件 ，和客户沟通中。--------------下一批货需要改 		廖媛		吴曦	
高	S10(V3E)	柬埔寨	Smart	网页和软件配置参数定制化	暂无	WPS PIN已经完成，还需添加生产的pin码生成工具，网页界面还在等客户确认，其他等客户确认后一项一项落实完成	其他的等需求确认再定时间。	陈玉	刘云	吴曦	
低	P10X	墨西哥	TELCEL	最新基线合上CPC功能的版本	无	版本按计划在P30上面合并，不过目前前方暂时没有测试资源。	优先级中等	陈玉	刘云	吴曦	
中	M60A 	泰国	TOT	完成《ZLT M60A - Project Tracking.xlsx》的所有需求	无	修改中		胡媛媛		张悦玲	
高	S30(V3E)	墨西哥	ALTAN	LTE与有线拨号自由切换；设计多个灯的功能	无	PPPOE功能基本调通在添加网页设置及优化。硬件需要再投板，wan口有问题	2019年9月25日	胡媛媛		吴曦；模块：陶嵩；底板：梁官	
高	P21K(V3)	斯里兰卡	SLT	根据招标需求修改相关内容		VOLTE特殊拨号需要处理；招标测试，与前方测试联调	2019年9月21日	陈玉	余小虎/刘永辉	吴曦	
高	P11M(V3)	斯里兰卡	SLT	根据招标需求修改相关内容		招标测试，与前方测试联调	2019年9月21日	陈玉	余小虎/刘永辉	吴曦	


**刘云**  安全测试还是扫出来了几个网页和端口问题，已发给向杰整改，周一再发个版本测试。这边工程师培训后测试比之前要严格点了，不能掉以轻心。

**何旭晨** 帮忙搞一下S12-PLUS的GPIO，电池充电等等；这个项目就是把S21放进S12的模具里面，改动点主要是GPIO，增加了电池充电电路等

**郑达**：
>>>>>>>>>>蔡松延：
voip 開機註冊問題:
    1.voip socket端口被佔用, 要求addy提供端口配置方法   --addy給了方法做配置，目前掛側正常．
    2.voip 會註冊不上,要求addy加上註冊失敗碼, 並處理註冊不上問題-- voip註冊不上是sip包達到不了sip服務器，國內和迪拜都會出現．但ntp包和http包能正常交互（wget www.baidu.com）．準備在小基站復現並抓包，確認數據包能到達基站側，從而縮小問題懷疑範圍．
串口服務程序 進行中　--與addy解決voip中，放緩．

>>>>>>>>>>封远钊:
查看迪拜tr069連不上問題　--查出是mtu問題，1500的mtu會被上層發icmp不可達包，目前設置爲1200正常．
wifi 5.8g tkip方式連接不上問題查看(解決問題之前,會先把網頁tkip和auto兩種方式先去掉)-- 網頁已經去掉不正常方式，tkip問題正在查找．
分支上實現新配置方式,準備出程序給喻蕭驗證方案可行性 --未出版本．

>>>>>>>>>>杨谋均:
多apn撥號整理到diatool2中　-- 多apn撥號部分挪至dialtool2，會導致整體撥號時間過久，現決定保留之前做法，轉而去修改sendat程序，讓該程序與atd進行交互．（考慮讓楊輔助蔡工搞atd程序）

>>>>>>>>>>巢丽媛:
查找第一次登錄界面可能會卡住問題 -- 上週四排查出問題，是新增天線檢查接口導致，我掛側舊版本存在這個問題，所以提出．
查看長時間掛側網頁返回很卡頓問題 --當前看出是某些接口返回很慢，排查是哪些接口問題導致總體時間非常長．

>>>>>>>>>>董錫文
wifi網頁去掉tkip這種加密方式
思考如何做到不同型號網頁公用問題．
    

1.發現最新版本還是會發生重啓問題
        觀看dmesg頭部, 覺得還是有點不太對, 目前掛兩臺去年12月份的版本中.　--去年版本已跑一天多，目前正常運行
　　 還得看如何加速排查問題，加大測試量，以及查找openwrt資料
2.設備運行越久,網頁返回時間越慢
　　有兩個可能：接口返回慢；長時間跑系統性能下降，http服務能力下降，目前從接口入手分析
3.在編譯服務器上編譯s21, 還編譯不過
　　有個文件得查找如何生成，他們有辦法遠程過來編譯嗎？
4.產測反饋的網口連接口，50多秒後才能ping通．
　　網口驅動的加載要在22+5s(uboot時間)，同時可能重啓了network，導致這個ping很慢，考慮如何優化
5.拉取最新版本openwrt程序
　　已經編譯成功，但dts文件裏沒有內存配置，決定先下載到板子裏去運行，掛測看能否正常運行跑起來．
　　跑起來後，reset 到最新正式發佈版本，嘗試移植wifi驅動．（看了下前前個release版本，會存在2.4Gwifi不穩定情況，所以儘量收集些資料，看目標release版本存在的一些潛在風險）

#### 2019.09.19

tutk代码仓处理, 已经有提交
发出例会邮件
还中信信用卡
从证券中取回一点钱。
ath9.5上好久没有buildall了。会有从bigap_web得到网页错误的问题。
单总发出了个硬件加速的资料。
https://www.howtogeek.com/164570/HOW-TO-INSTALL-ANDROID-IN-VIRTUALBOX/

**刘云** S10G UAT测试已经OK，TR069服务器不能降级的截图证明Jef也已经发给了Frisco,Frisco回复会更新后发布报告。这样看就剩下新增加的NTG网络部门的测试了，Ross在负责协调和推动这个测试启动。 
gpon:
1，烽火这边对我们提出提供OMCI报文的需求不做正面回答，转而问我们要芯片和光模块资料，我邮件再次客气的重申了下，运营商也邮件回复让烽火提供相应报文LOG，目前烽火还没回邮件。
2，华为这边今天更新了状态，说发现ONU连他们OLT有些问题，但邮件并没有说什么问题，让大家等后续分析的结果。

**eddy** 发出新的voip版本，增加TCP_CONTROL_PORT=1999  TCP_CONTROL_PORT_SRSIP2=3999 两个设定。

**刘永辉** 以下为M60A SLT Fon 9月18日程序问题
通过修改hotspotd参数，wq! 保存并退出后不会立即生效 Fon认证过程就是修改hotspotd去测试，需要做成立即生效
通过nv或TR069修改Fon ssid当前程序需要重启Fon进程才能生效 需做成自动重启进程并使之生效

**吴曦** slt招标的信号格式要求太高，估计最多到4格。不太可能满格。

#### 2019.09.18

**陈良**  cat6 WIFI工作异常，5GWIFI无法连接，手机上连接后显示网络拒绝连接,2.4GWiFi可以连接，但是测速速率偏低.--重点

**罗美芳** 库存查询新增加了功能，查询物料信息/库存/在途会更加方便

**白俊剑** 配置工具V2.3
更新内容：    1，支持在搜索结果表中右键添加配置项功能。
右键对已添加项（已标绿项）无效，添加后会将当前项标绿。
主配置表中如果有增减动作，建议重新点击“搜索”。

**张悦玲** ZLT_P19H_v2.8_web_upgrade_20190918_1208.sfp
修改版本为V2.8;
更新bootrom版本45334（并开放GPIO41（PHY reset）,GPIO40（PHY irq），及修改温补参数）
为解决ping有时不通，开机时对PHY芯片LAN8710a进行软复位操作;

**毛祖潇**
客户反馈网络注册等概率性问题时，往往难以复现，当复现时可能未抓取到有效的log或者提供给研发的log文件比较大 
针对该类情况，下面用我在兰卡遇到的问题为案例，把我解决该类问题的方法分享给大家

让郑达安排人在1.9上 编译cat6, 下午开始了。

问杨某均的任务情况。s21的这个:5.系统日志,需要添加一些日志,类似于APN注册失败,重新注册成功,VOIP注册失败,重新注册成功这些,有助于故障排查.
把sequans的仓推到80.4, 让张悦铃尝试编译。认为不能在16.04上编译。

我的笔记本的无线ip是192.168.82.85 记录一下。
在80.4上安装docker，编译ath9.5看看。看起来是编译完成了：
docker run -it --user $UID:$(id -g $USER)  --name ath -v /home/jian/work/ath9.5:/ath9.5 -v /home/jian/.ccache:/.ccache  ath9.5

余小虎 V10S客退机原因了解 	9.19 尧远仍未反馈PA分析结论，
M60A 	Dialog测试报告问题解决 	9.19 研发已经解决NTP同步问题，预计本周完成版本测试验证；
V10S 客户投诉:结束通话后，未对话机进行操作，话机自动重拨 	9.19 Siyol答应与SLT沟通并在下周四之前收集5-10台机器，由我们带回国分析；
Kandy反馈很多机器开机按键卡死，要拔电才恢复正常 要找到源头，并且规避掉 这样看起来就完全不是我们的问题了，如果我们要求升级，那从别人理解，就是我们的问题 而且干扰之下，经常无法升级 。
 9.19 SLT Kandy营业厅还未与楼下培训机构沟通好，等沟通好我们再过去排查；9.10 尧远和RTL定位到问题根源是WiFi被攻击，以及被攻击后频繁输出log。尧远已经合并RTL防攻击patch，并屏蔽频繁log输出。
M60A 	FON程序准备 9.19 研发已经解决“修改参数后不生效”问题，但仍未出版本

刘云 

#### 2019.09.17

**李光达** 立陶宛 NRO361 程序 P11X 5.9程序测试问题：
1:Connect to any available cell功能没用
2：EARFCN频点有4位数的，但是只能输入5位
3：turn off代表关闭，但是实际上菜单是清除作用。
4：Ping WatchDog失败2次后，没有重启LTE模块的动作。
5：刚升级时候CPE的LAN IP会变化，然后重启又变回正常值。
6：点击首页的disconect按钮，信号和SIM卡灯都会变红，应该SIM卡不能变红。
7：TR069推送升级后，CPE升级成功，但是TR069服务器上的推送升级一直不消失；WAN IP上报为00:00:00:00:00:00是否正常？

**马岳振** 开机收不到网的log 原因是imsi 不合法 搜网后掉网的原因我怀疑也是这个
你们得确认下这块 imsi是否已经加入了HLR 就是运营商加进去没有

**喻潇** SLT多了一种SIM卡，有以下问题
    测试中发现无法正常注网，现有以下现象；
        1、新sim卡首次使用注网失败
        2、新sim卡注网成功后掉网
        3、若开启了pin码。重启后马上输入pin码则能成功注网（过一会就掉网）；重启后放个5秒以上再输入pin码则注网失败

**白俊剑** 配置工具V2.2 更新内容：
1，“导入配置文件”可选择.src.conf和.src.txt文件，由此文件可反向生成.new.conf二进制配置文件。
用于当.conf二进制配置文件出问题情况下，恢复.conf的操作。
建议在确认.new.conf无误后，将.new.conf后缀删除。

**吴曦** 2019年-2020年SLT投标事宜-软硬件定制 SLT的信号显示与Dialog不一致，需要修改。

**江健** 高唐司法局手环充电情况报告备忘，都是可以充电。

**向杰** V3： 中东分支添加BCP状态
V3E: 1.给S10和S10G添加电池功能
2.编写手机端页面短信聊天对话功能
3.解决wps界面不显示问题
4.防止样式错乱，在制作主题配置时，可能会配置一个没有的主题，这时会导致页面错乱，现已做兼容。

时间	项目	工作内容	人员
2019/9/11	S21	解决了登录之后存在退出登录的问题	董锡文
2019/9/12	S21	解决了系统升级页面在升级大于30MB文件的时候，进度条走完而设备还在很长时间没升级完的问题	董锡文
2019/9/16	S21	修改了普通用户和高级用户的显示隐藏标志位的默认值	董锡文
2019/9/17	S21	修改了恢复出厂设置页面点击Restore按钮之后恢复出厂的流程	董锡文
2019/9/17	S21	实现了新增的语音设置页面SIP服务器分页的VOIP注册状态的部分状态显示	董锡文

**巢丽媛** 工作汇报
S21：
	1、处理WiFi Info 页面MAC地址未读取时显示的值为“-”；
	2、在4g Info 页面增加 CA 激活状态的显示；
	3、在高级设置——PCI 锁定页面的PCI 扫描的列表中增加一列用来显示EARCFN 信息；
	4、在版本信息页面——设备和版本信息这一栏目中增加一个仅仅在登录用户为sztozed才显示的参数“voip软件版本号”；
	5、修改Wan Info 页面中APN_Name的值加载时间过长的问题。
V3：
	熟悉V3项目的代码和功能。

梁剑是否开始了手环方面的工作。还在做手机广播包的接收。tcpdump可以抓到。
问黄成是否可以插2张卡。可以，价格13000
10:15 如果郑达下午没有回陈良的邮件，就催他回。已催
10:13 发出分组邮件：
8:00 陈良好久没有发进度了。16号发了测试情况。

w3m使用m键后，才能使能鼠标。不知道为什么要默认不能用鼠标选择词语。
/proc/net/nf_conntrack  这个文件里面是nat的连接

#### 2019.09.16

**皮晓聪** p53 Version: V6.13.33
Date   : 2019-09-16
Changes:
        P53:Release P53 V6.13.33
P53:修复配置设备为路由模式不生效问题 <PiXiaocong>
P53:默认选中编译BM816模块驱动 <PiXiaocong>
P53:修复在新服务器上编译cgi时无法创建/var/run软链接而编译失败问题 <PiXiaocong>
Makefiles:use local tftpboot dir. <jianliang>
compile scripts: mv tftpboot to local <jianliang>
compile scripts: fix cp file error dir <jianliang>
compile, tftpboot in user dir, to fix build error many people in single pc <jianliang>
pppd: 解决重复编译pppd报错的问题 <renyinshan>
apps/dialtool2:修复使用MC7455模块时查询拨号状态失败后没有重新拨号处理问题 <PiXiaocong>
修改 miniupnpd 编译出错 <jiangyibo>
1.添加miniupnpd upnp功能的uuid库 2.添加miniupnpd 功能 3.添加snmptrap 功能，net-snmp 功能编译时去掉app/snmpping.c 编译 4.修改quagga 编译动态库为静态库，默认用户为root用户 <jiangyibo>
修复使用BM816,BM817C,MC7455模块时网页上无法配置PIN码问题 <PiXiaocong>
apps/dialtool2:添加程序外部AT指令处理,避免有的模块只有一个AT指令串口而造成其它进程无法发AT指令问题 <PiXiaocong>
apps/dialtool2:修复使用MC7455模块时重复的发SCACT指令造成一些模块信息获取失败问题 <PiXiaocong>
apps/dialtool2:MC7455模块查询PIN和PUK剩余输入次数 <PiXiaocong>
修复使用MC7455模块时WEB页面PIN码配置失败或无响应问题 <PiXiaocong>
修复WEB页面设置频带响应慢或有时不响应问题 <PiXiaocong>
apps/dialtool2:修复MC7455模块有时获取IMSI失败造成无法注册网络问题 <PiXiaocong>
apps/dialtool2:修复使用MC7455模块时未查询当前已锁定判断信息 <PiXiaocong>
cmdlib: 上传一个单独调试cmdlib的c文件（如果cmdlib接口有问题，可以直接用此文件使用gdb进行单步调试） <renyinshan>
document: 上传一份P5x GDB调试的文档说明 <renyinshan>
gdb: Add installgdbserver directory to .gitignore <renyinshan>
Modem Log： 底层脚本增加启动判断（支持直接编译到系统和临时上传） <renyinshan>
cmdlib: 增加bmlogproxy是否运行的判断，如果是临时上传的，则需要增加/tmp/bmlogproxy的判断（底层接口判断比较严谨） <renyinshan>
web[Modem Log]: 解决开启log提示失败的错误。（响应太快，cgi还没收到判断结果） <renyinshan>
Modem Log： 增加抓取宽翼模块log的底层脚本，供网页调用。（至此，此功能在管理页面和普通页面都可正常工作） <renyinshan>
web [Modem Log]: 普通页面增加抓取模块log的功能 <renyinshan>
cmdlib: 增加抓取宽翼模块log的代理程序"bmlogproxy"是否运行的判断。 <renyinshan>
apps/switchwan:修复WAN模式为doublewiredlte模式时由于有些LTE模块网络接口不为usb0没有删除多出默认路由而无法上网问题 <PiXiaocong>
apps/dialtool2:输出当前LTE模块网络接口名称到/tmp/.system_info_static文件 <PiXiaocong>
修复使用BM816模块(网络接口为wwan0)WEB页面不显示4G网口信息问题 <PiXiaocong>
apps/dialtool2:增加P59(TZ7.823.317板型)支持BM816模块处理 <PiXiaocong>
添加BM816模块驱动 <PiXiaocong>
bmlogproxy: Fix a build error. <renyinshan>
.gitignore: 增加build_dir到.gitignore文件中 <renyinshan>
bmlogproxy: 增加宽翼模块的抓包工具bmlogproxy. 并更新一个比较通用的Makefile，以后新增加的app可以以此来参考 <renyinshan>
compile.mk: 增加一个编译app所需的mk文件 <renyinshan>
apps/dialtool2:暂不启用GPS,以修复启用GPS后MC7455模块初始化失败问题 <PiXiaocong>
apps/dialtool2:修复不能配置MC7455模块工作在3G网络和4G模式时无法获取信号强度问题 <PiXiaocong>
P53: 内核支持MC74xx模块 <CONFIG_4G_MODULE_MC74xx=m> <renyinshan>
version: 解决version文件中os参数为空的bug. <renyinshan>
修复增加MC7455模块后WEB页面不显示4G网口信息问题 <PiXiaocong>
apps/dialtool2:P59(TZ7.823.317板型)增加MC7455模块处理 <PiXiaocong>
P53: 手机APP默认不升级boot <renyinshan>
添加MC74xx系列4G模块驱动 <PiXiaocong>
P53: rc.network 提交时错误导致系统启动异常 <renyinshan>
P53: 修复rc.network文件的错误，导致启动网络异常 <renyinshan>
Revert "Revert " p53: this is version 6.13.32"" <renyinshan>
Lan 多ip配置 默认隐藏bug修复 <Luoting123456>
修改version文件中os的值为"uname -a" <renyinshan>
P53: 修改开机后静态路由不生效的bug <renyinshan>

**吴曦** V3E S10 生产wifi起不来 
有两个文件是开机过程中，由一个default脚本判断文件在不在，不在的话就去写的一些参数进去，然后后面的脚本会用到这两个文件的内容。但是现在这个文件存在，里面的内容为空。导致后面的脚本调用不到里面的参数。从而导致后面的脚本异常退出了。
这个应该是Realtek的脚本不够健壮导致的，我把这部分的判断再严谨一点，应该可以规避这个问题。
基本排除V3有同类问题，V3的这两个文件是默认文件系统写死的，不是生成出来的。


#### 2019.09.10
docker 使用--network=host可以看到所有的网卡。

没有ifconfig
sudo apt install net-tools 

airmon-ng 在这里:
apt-get install aircrack-ng
apt-get install pciutils

RTL8188cus开启监听模式 
https://www.findhao.net/easycoding/1498.html
感觉好麻烦的样子，以后再说。

某台机器的多选鼠标居然没有用了，只好改快捷键，还不知道被什么程序占用的。

#### 2019.09.05
=CONCATENATE(A1,"|",B1,"|",TEXT(C1,"[h]:mm"),"|",TEXT(D1,"[h]:mm"),"|",TEXT(E1,"[h]:mm"),"|",TEXT(F1,"[h]:mm"),"|",TEXT(G1,"[h]:mm"),"|",H1)

#### 2019.07.25
sudo iptables -t nat -D INPUT -i eth0 -p tcp -m tcp --dport 110 -j SNAT --to-source 220.181.72.229
这样好像没有用的。

sudo iptables -t nat -A PREROUTING -i eth0 -p tcp -m tcp --dport 25 -j DNAT --to-destination 220.181.97.150
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp -m tcp --dport 110 -j DNAT --to-destination 220.181.72.229

#### 2019.07.23
win7下的ssh也可以进行端口转发。

#### 2019.07.20
apt-get install gcc g++ liblzma-dev zlib1g-dev libncurses5-dev ia32-libs 

77上的xl2tp貌似没有日志了。


#### 2019.07.10
vscode 清除多余空行:
https://blog.csdn.net/qq_36051316/article/details/84136805
^\s*(?=\r?$)\n

#### 2019.07.01
HTML 段落是通过 <p> 标签进行定义的。
<a> 标签定义超链接，用于从一张页面链接到另一张页面。
.aaa 是class选择器， #aaa是id选择器。

#### 2019.06.05
gdbserver 居然用的是c++，而且需要texinfo支持。

2019.5.30
GB 2312 是參考 JIS 的字符集。
GBK 是在 GB 2312-EUC 的基礎上按當時的 Unicode CJKV 擴充的。但是有很重要的一點，就是「鍾」被修改成了「锺」。
GB 18030 是對 GBK 的擴充，是一種 UTF。

2019.5.28
:s#vivian/#sky/# 替换当前行第一个 vivian/ 为 sky/

2019.5.23
python 多行注释是用三引号'''   '''

2019.5.20
连接到win2012上，用这个软件：
sudo apt-get install freerdp2-x11
https://www.linuxquestions.org/questions/linux-networking-3/failed-to-connect-credssp-required-by-server-4175611983/

使用python共享文件
python -m SimpleHTTPServer 8000

2019.5.9
c99标准已经支持变长数组
https://blog.csdn.net/hannick/article/details/2119223

2019.5.8
这样就可以直接把那个工时的execl的每行变成markdown的表格了。
=CONCATENATE(C45,"|", D45,"|",TEXT(E45,"[h]:mm"),"|",TEXT(F45,"[h]:mm"),"|",TEXT(G45,"[h]:mm"),"|",TEXT(H45,"[h]:mm"),"|",TEXT(I45,"[h]:mm"),"|",J45)

这个我机器上运行tf的命令。
docker run  -it -u $(id -u):$(id -g) --rm -v $(realpath .):/tf/notebooks -p 8888:8888 tensorflow/tensorflow:latest-py3-jupyter

2019.05.05
L2TPv3简单测试脚本
https://blog.csdn.net/bingyu9875/article/details/79075828

2019.4.29
putty+xming远程登录Ubuntu16.04图形界面
https://www.cnblogs.com/xuanxufeng/p/6243244.html


2019.4.24
世界各国时区表以及与北京时差
https://www.cnblogs.com/mq0036/p/4837102.html

2019.4.18
linux下查看显卡。
查看显卡使用
lspci |grep VGA

2019.4.15
线性代数学习：
视频：
http://open.163.com/special/opencourse/daishu.html
笔记
https://nbviewer.jupyter.org/github/zlotus/notes-linear-algebra/blob/master/ReadMe.ipynb

Python关于%matplotlib inline
https://www.jianshu.com/p/2dda5bb8ce7d
是在使用jupyter notebook 或者 jupyter qtconsole的时候，才会经常用到%matplotlib，也就是说那一份代码可能就是别人使用jupyter notebook 或者 jupyter qtconsole进行编辑的。关于jupyter notebook是什么，可以参考这个链接：[Jupyter Notebook介绍、安装及使用教程][1]
而%matplotlib具体作用是当你调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，可以直接在你的python console里面生成图像。

在vscode中，要用plt.show来显示图，而在jupyter中draw和show都可以。

python3中file不见了，要改用open
https://blog.csdn.net/menuconfig/article/details/8672118


这样就可以根据函数画线，不明白为什么那个线性代数的笔记中使用若干个点的方式，不容易懂。
x = np.arange(-2, 2, 0.1)
y = x * 2
plt.plot(x,y)

y = (3+x)/2
plt.plot(x,y)
plt.draw()

functools.partial的主要作用是简化调用过程：
import functools

def add(a,b):
    return a + b

add3 = functools.partial(add,3)
add5 = functools.partial(add,5)

print add3(4)
print add5(10) 

控制台输出，

7
15

jupyter支持markdown和LaTex数学表达式。
像代码单元格一样，按 Shift + Enter 或 Ctrl + Enter 可运行 Markdown 单元格，这会将 Markdown 呈现为格式化文本。

LaTex
LaTeX 中有两种数学公式的表达方式: 行内公式和行间公式. 第一种方式直接将公式作为放在句子里面作为其一部分. 第二种则将公式单独放在一行, 通常居中显示.
行内公式的分隔符通常为: \( \), $ $ 或者 \begin{math} \end{math}. 这些都可以达到同样的效果. 理论上第一种最好用, 但是输出比较麻烦(毕竟多两个字符😄), 所以通常会使用第二种方式.

2019.4.11
使用机器学习来发掘表示本身,而不仅仅把表示映射到输出。这种方法我们称之为 表示学习(representation learning)。
深度学习(deep learning)通过其他较简单的表示来表达复杂表示,解决了表示学习中的核心问题。
深度学习让计算机通过较简单概念构建复杂的概念。
输入展示在 可见层(visible layer),这样命名的原因是因为它包含我们能观察到的变量。
然后是一系列从图像中提取越来越多抽象特征的 隐藏层(hidden layer)。
深度学习模型的典型例子是前馈深度网络或 多层感知机(multilayer perceptron, MLP)。多层感知机仅仅是一个将一组输入值映射到输出值的数学函数。

三次发展浪潮:
20 世纪40 年代到 60 年代深度学习的雏形出现在 控制论(cybernetics)中
20 世纪 80 年代到 90 年代深度学习表现为 联结主义(connectionism)
直到 2006 年,才真正以深度学习之名复兴。

大家不应该认为深度学习在尝试模拟大脑。现代深度学习从许多领域获取灵感,特别是应用数学的基本内容如线性代数、概率论、信息论和数值优化。

联结主义是在认知科学的背景下出现的。认知科学是理解思维的跨学科途径,即它融合多个不同的分析层次。
联结主义的中心思想是,当网络将大量简单的计算单元连接在一起时可以实现智能行为。
分布式表示 系统的每一个输入都应该由多个特征表示,并且每一个特征都应该参与到多个可能输入的表示。
联结主义潮流的另一个重要成就是反向传播在训练具有内部表示的深度神经网络中的成功使用以及反向传播算法的普及

anaconda的下载列表在这里：
https://repo.continuum.io/archive/

2019.3.24
VIM 打开文件，光标定位到上次退出的位置
vim ～/.vimrc 添加下面几行

if has("autocmd")
  autocmd BufReadPost *
    \ if line("'\"") > 0 && line("'\"") <= line("$") |
    \   exe "normal g`\"" |
    \ endif
endif 
https://blog.csdn.net/u011383474/article/details/46953177


2019.3.18
sequans的新cloud信息。
https://cloud.sequans.com
login：dl-tozed@sequans.com
password：tozed369147258

2019.2.27
SSH服务修改默认22端口或同时监听多个端口
http://blog.licess.com/sshd_listen_address/

2019.01.09
华泰  020 900 256 538

2019.01.03
解决Could not get lock /var/cache/apt/archives/lock
sudo rm -rf /var/cache/apt/archives/lock
sudo apt-get update
http://www.cnblogs.com/kym/archive/2011/01/17/1937825.html

Linux通过Shell脚本命令修改密码不需要交互:
https://www.cnblogs.com/crxis/p/9077313.html

2018.12.28
https://www.geeflex.com/Blog/2018-03-12-srsLTE/

2018.12.20
这样可以显示所有文件的内容，不能用xargs。
 find -type f -print -exec cat {} \;
这样也可以：
ls | xargs -n1 -t cat

2018.12.14
linux grep 正则表达式
http://www.cnblogs.com/xiaouisme/archive/2012/11/09/2762543.html
^ 锚定行的开始 如：'^grep'匹配所有以grep开头的行。 

ip -6 route add ::1/0 via 240e:ff:b353:4e6b:1:1:703d:f994 dev usb0

2018.12.13
0755000011848342	263088

2018.12.11
这样还能得到本机ip
curl  http://2018.ip138.com/ic.asp
ip.cn貌似封锁了sim卡的地址。

2018.12.4
sublime License
----- BEGIN LICENSE -----
sgbteam
Single User License
EA7E-1153259
8891CBB9 F1513E4F 1A3405C1 A865D53F
115F202E 7B91AB2D 0D2A40ED 352B269B
76E84F0B CD69BFC7 59F2DFEF E267328F
215652A3 E88F9D8F 4C38E3BA 5B2DAAE4
969624E7 DC9CD4D5 717FB40C 1B9738CF
20B3C4F1 E917B5B3 87C38D9C ACCE7DD8
5F7EF854 86B9743C FADC04AA FB0DA5C0
F913BE58 42FEA319 F954EFDD AE881E0B
------ END LICENSE ------
修改hosts:
127.0.0.1 www.sublimetext.com
127.0.0.1 license.sublimehq.com
127.0.0.1 45.55.255.55
127.0.0.1 45.55.41.223
https://www.cmsky.com/sublime-text-key/

2018.11.30
所有的mac地址公司在这里:
http://standards-oui.ieee.org/oui/oui.txt

2018.11.14
在77上这样设置后， 77上可以ping到p53的lan口。
sudo ip route add 192.168.19.0/24 dev ppp1 

2018.11.3
我当前用的移动卡是136 0041 8516

2018.10.31
mini_httpd 1.30这个版本，我们的cgi还是无法输出的。

我应该曾经使用过3.18.23的内核和wlan_v10配合，好像编译错误太多，已经不这样折腾了。

2018.10.26
undefined reference to `_Unwind_Resume'
加上编译参数“-Wl,-Bdynamic -lgcc_s”
https://blog.csdn.net/gunwithrose/article/details/1922741
https://stackoverflow.com/questions/5400500/makefile-how-to-fix-libc-dependency

undefined reference to `__libc_setup_tls'
要把-lpthread改为-pthread
http://chaoslawful.iteye.com/blog/568602


2018.10.25
python 使用len来去list的长度，为什么不是xxx.len呢？
http://s9899.blog.163.com/blog/static/3062228820110159182166/

2018.10.24
cisco 使用exit来退出一级config.

这个网站的书貌似不少。
https://sk.kindleshare.cn/index.php

2018.10.23
使用airdoid可以把android屏幕在windows下显示。
配置cisco的telnet
https://zhidao.baidu.com/question/244679495.html

2018.10.21
这里能下载一些m4r的音乐，直接拖到itunes中连接的iphone，就可以在铃声列表中出现。
http://www.lnpan.com/htmls/format/id/1_10.html

2018.10.19
这样就可以显示列表了：
./smbclient -c "ls" //192.168.1.123/f$ -U jian%tellmemore
http://man.linuxde.net/smbclient

2018.10.16
8905中:
8905有若干部分，其中ap是a7双核，8909是4核。qdsp是

cisco 要在加电的时候按住reset键，才可以reset系统。默认密码是cisco,cisco
https://dcloud-cms.cisco.com/help/reset-router

77上的docker网络居然不通。把它的docker0 up一下就好了。
在77上居然编译了2个小时。

2018.10.15
这个adb interface的驱动看来是好的。
http://www.121down.com/soft/softview-80135.html

cisco 串口的波特率居然只有9600.
https://blog.csdn.net/yingchun2915/article/details/50748844

2018.10.14
下午电脑居然停止不动了，但是耳机里面的音乐还能响，从其他电脑登录过去，有两个进程占了100%的cpu, 一个是firefox, 一个是gnome-shell。sudo killall -9 后就能操作了。

2018-10-10
linux下使用命令行发送消息和弹窗消息
https://www.52os.net/articles/linux-shell-send-message-and-gnome-popup-box-message.html

2018-10-9
18.04安装smba似乎不难：
并非按照这个连接做的。
https://blog.csdn.net/yuanjinshenglife/article/details/81122132

防火墙要增加如下端口：
四个  137 udp  138 udp    139 tcp  445 tcp。

curl -s   --interface usb0 http://ip.cn
这样就能到当前公网的ip

User ID:  LeadcoreTech
Password:  472ktm6
Admin Key:  11642

2019-10-8
139这个邮箱不知道是和the bat的配合还是怎么样，出现了2次无法收邮件的情况。
报错情况：
 2018/10/8, 15:03:43: FETCH - 1822 封邮件在邮箱内，23 封新的
!2018/10/8, 15:04:15: FETCH - 连接到主机中断（最后发送的命令为："UIDL", "RETR 1800"）
这个时候，可以使用telnet mail.139.com 110来进行删除操作。
telnet mail.139.com 110
Trying 221.176.9.121...
Connected to mail.139.com.
Escape character is '^]'.
+OK richmail system v10(32d35bbb01d5c43-1c528)
user jianliang
+OK
pass xxxxxxxxxxxx
+OK login success
dele 1800
+OK deleted successful
quit
+OK dewey POP3 server signing off
Connection closed by foreign host.
然后就可以继续收邮件了。

又一个错误：
#0  0x77a48cc0 in popen () from /home/jian/work/ath9.5/staging/rootfs-tozedap-p59_ap143.build/lib/libuClibc-0.9.30.1.so
#1  0x00477808 in read_memory (shellcmd=0x7f1fef2c "hostapd_cli -i ath0 all_sta | grep  wpsDeviceName | wc -l", out=0x7f1feeac "", size=128) at cwmp.c:3698
#2  0x0044ae7c in read_wps_registrar_info (read_wps_device_info=0x7f1fefe0) at modules/InternetGatewayDevice/LANDevice/LANDevice.c:2567
#3  0x0044b938 in make_wps_associated_table_lists () at modules/InternetGatewayDevice/LANDevice/LANDevice.c:2661
#4  0x0044bc94 in refresh_device_info_porcess () at modules/InternetGatewayDevice/LANDevice/LANDevice.c:2694
warning: GDB can't find the start of the function at 0x77ad13c7.

    GDB is unable to find the start of the function at 0x77ad13c7
and thus can't determine the size of that function's stack frame.
This means that GDB may be unable to access that stack frame, or
the frames below it.
    This problem is most likely caused by an invalid program counter or
stack pointer.
    However, if you think GDB should simply search farther back
from 0x77ad13c7 for code which looks like the beginning of a
function, you can increase the range of the search using the `set
heuristic-fence-post' command.
#5  0x77ad13c8 in ?? () from /home/jian/work/ath9.5/staging/rootfs-tozedap-p59_ap143.build/lib/libpthread-0.9.30.1.so

tr069还是出现了错误:
#0  0x77740cc0 in popen () from /home/jian/work/ath9.5/staging/rootfs-tozedap-p59_ap143.build/lib/libuClibc-0.9.30.1.so
#1  0x00477808 in read_memory (shellcmd=0x4cc8f4 <shellcmd> "cfg -g TZ_DEVICE_TYPE", out=0x4cca38 <param> "", size=256) at cwmp.c:3698
#2  0x00477c8c in get_single_config_attr (name=0x4aa614 "TZ_DEVICE_TYPE", value=0x4cca38 <param> "", value_size=256) at cwmp.c:3800
#3  0x0047f510 in get_sys_parameter (name=X_SYS_ProductClass, value=0x7fcdcbc4) at cwmp.c:6034
#4  0x0046f8d0 in cwmp_create_device_id_node (env=0x7e39fc, parent=0x75cf9c, deviceid=0x7de470) at cwmp.c:2185
#5  0x0047072c in cwmp_create_inform_message (env=0x7e39fc, header=0x7de464, deviceid=0x7de470, events=0x75c97c, currentt=0x75c964, max_envelope=1, retry_count=0, 
    pl=0x7de488) at cwmp.c:2323
#6  0x00490630 in cwmp_session_create_inform_message (session=0x7ebf60, pool=0x7de440) at session.c:953
#7  0x0042f310 in cwmp_agent_start_session (cwmp=0x73e174) at agent.c:342
#8  0x00430808 in cwmp_agent_session (cwmp=0x73e174) at agent.c:755
#9  0x0042e234 in cwmp_worker_thread_start (cwmp=0x73e174) at thread.c:122
#10 0x0042df94 in cwmp_process_start_master (cwmp=0x73e174) at process.c:37
#11 0x0042cf9c in main (argc=1, argv=0x7fcdd6b4) at cwmpd.c:339


2018-9-27
PV 由Andrew Wood 开发，是 Pipe Viewer 的简称，意思是通过管道显示数据处理进度的信息。
https://linux.cn/article-6734-1.html

把这个加入注册表，那个恼人的expleror.exe没有关联的弹出框就没有出现了。
Windows Registry Editor Version 5.00
[[HKEY_CLASSES_ROOT\Folder\shell\explore\command]
"DelegateExecute"="{11dbb47c-a525-400b-9e80-a54615a090c0}"
[HKEY_CLASSES_ROOT\Folder\shell\opennewwindow\command]
"DelegateExecute"="{11dbb47c-a525-400b-9e80-a54615a090c0}"

2018-9-26
==8071== Process terminating with default action of signal 11 (SIGSEGV): dumping core
==8071==  Access not within mapped region at address 0x652F6163
==8071==    at 0x652F6163: ???
==8071==    by 0x652F615B: ???
==8071==  If you believe this happened as a result of a stack
==8071==  overflow in your program's main thread (unlikely but
==8071==  possible), you can try to increase the size of the
==8071==  main thread stack using the --main-stacksize= flag.
==8071==  The main thread stack size used in this run was 2088960.
/tmp/valgrind # /tmp/cwmpd: can't resolve symbol '__libc_freeres'

    valgrind: it works:
    upload apps/valgrind-3.11.0/valgrind.tar.gz
    mkdir -p /tmp/valgrind
    cd /tmp/valgrind
    tar xzvf ../valgrind.tar.gz
    /tmp/valgrind/bin/valgrind xxxx
    
    and, compile xxxx with -g option, and do not strip it.

2018-9-19
docker安装：
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh --mirror Aliyun


2018-9-18
apt‐get install git‐core gnupg flex bison gperf build‐essential zip curl zlib1g‐dev gcc‐multilib g++‐multilib libc6‐dev‐i386 lib32ncurses5‐dev x11proto‐core‐dev libx11‐dev lib32z‐dev cache libgl1‐mesa‐dev libxml2‐utils xsltproc unzip
apt install git-core gnupg flex bison gperf build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev ccache libgl1-mesa-dev libxml2-utils xsltproc unzip

2018-9-17
docker run -it --rm --mount type=bind,source=/home/jian,target=/home/tozedsoft gm8136s

解决在docker中git log显示乱码
export LESSCHARSET=iso8859    #或者utf-8、gbk
http://www.cnblogs.com/diyingyun/archive/2012/11/20/2778889.html

2018-9-14
win10专业版激活方法——亲测可行！！！
slmgr.vbs /upk
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
slmgr /skms zh.us.to
slmgr /ato
https://blog.csdn.net/AinUser/article/details/79247841

ideapad f2进入bios设置。

关于bcp的资料不是很多：
[Bridge] BCP code ported to pppd 2.4.2
https://lists.linux-foundation.org/pipermail/bridge/2005-May/004523.html
ppp: Bridge Control Protocol 
https://lwn.net/Articles/376761/

这个地方介绍docker，应该是阿里的人写的：
https://yeasy.gitbooks.io/docker_practice/content/install/ubuntu.html


2018-9-10
启用Win10家庭版中被阉割的远程桌面服务端
https://www.jianshu.com/p/bf3001099cc4

2018-9-5
vscode缩进快捷键：
   选中文本；
     Ctrl  +  [      和   Ctrl  +  ]     实现文本的向左移动或者向右移动；

2018-9-4
../apps/gdb/install/bin/mips-linux-gdb ../staging/rootfs-tozedap-p59_ap143.build/usr/sbin/cwmpd core.cwmpd.1815
set solib-search-path /home/jian/work/ath9.5/staging/rootfs-tozedap-p59_ap143.build/lib
这样bt就可以有东西了。

2018-8-25
steam 在18.04上不能运行，要这样：~/.local/share/Steam/ubuntu12_32/steam
https://askubuntu.com/questions/966373/steam-doesnt-open-on-ubuntu-17-10

使用vim进行二进制文件编辑
vim -b file
:%!xxd     to change
:%!xxd -r   back to vim

wq

2018-8-21
对于python中的循环变量告警，把变量变为_， 就可以了:
 for循环，pydev提示未使用的变量，解决办法 http://www.cnblogs.com/testlife007/p/4514491.html

这个python代码可以从p59上取下dhcp客户端列表了：
    loginpayload={'cmd':100,'method':"POST", 'language':'EN', 'username':'admin', 'passwd':'f6339c4179e7b9b4b7c9da08502184ec', 'sessionId':'a6083050f134e86e79a7af2a5217ab4ea0ff26b8b1a25ea4b45fb969aa49d457' }
    test = 'test=test'
    headers = {'Content-Type' : 'multipart/form-data'}
    login = requests.post('http://192.168.19.1/cgi-bin/http.cgi', params=loginpayload, headers=headers)
    print(login.json())
    json1={"cmd":122,"method":"GET","language18:a9:05:91:e3:c2":"CN","sessionId":"a6083050f134e86e79a7af2a5217ab4ea0ff26b8b1a25ea4b45fb969aa49d457"}
    r = requests.post('http://192.168.19.1/cgi-bin/http.cgi', json=json1)
    print(r.status_code)
    macs=r.json()['data']
    print(macs)


2018-8-16
strongswan中出现/bin/bash: line 1: -N: command not found 这样的错误，因为gperf没有安装，那么在一天新的ubuntu 18.04的server上这个东西居然装不了，说没有。看/etc/apt/sources.list文件里面只要三行。难道是第一次启动的时候没有联网？

当前电脑出现第二次界面完全没有响应了。是不是要重新安装个系统？

2018-8-15
Eye of GNOME
Eye of GNOME 是 Ubuntu 系统默认的图片查看器，它集成在 GNOME 桌面环境中，尽管它界面简单，但是支持多种图片格式，并且可以用幻灯片模式查看图片。
sudo apt-get install eog

2018-8-14
pdfgrep可以搜索多个pdf中的文本。

这样可以把文件转为想要的c语言格式。
hexdump -v -e '16/1 "0x%02x,"' -e '"\n"' ascii.txt

2018-8-13
采购部的打印机是192.168.1.15

这个脚本，esim的模拟服务器返回500错误了。
curl -v -H "X-Admin-Protocol: gsma/rsp/v2.1.0" -H "Content-Type: application/json" -H "Accept: application/json" --data '{"euiccChallenge":"AAECAwQFBgcICRAREhMUFQ==","eUICCInfo1":"vyBLggMCAQCpLAQU84P+PGWXPa/QDqbdiktT1iRT1qwEFGV84BIobqFx3TPQ1Mqp02hB9N66qhYEFPOD/jxllz2v0A6m3YpLU9YkU9as","smdpAddress":"samba5-json.demo.gemalto.com" }' http://192.168.17.171:8080/gsma/rsp2/es9plus/initiateAuthentication

POST /gsma/rsp2/es9plus/initiateAuthentication HTTP/1.1
Host: 192.168.17.171:8080
User-Agent: curl/7.58.0
X-Admin-Protocol: gsma/rsp/v2.1.0
Content-Type: application/json
Accept: application/json
Content-Length: 211

{"euiccChallenge":"AAECAwQFBgcICRAREhMUFQ==","eUICCInfo1":"vyBLggMCAQCpLAQU84P+PGWXPa/QDqbdiktT1iRT1qwEFGV84BIobqFx3TPQ1Mqp02hB9N66qhYEFPOD/jxllz2v0A6m3YpLU9YkU9as","smdpAddress":"samba5-json.demo.gemalto.com" }
HTTP/1.1 500 
X-Admin-Protocol: gsma/rsp/v2.0.0
Content-Length: 0
Date: Mon, 13 Aug 2018 12:30:35 GMT
Connection: close

2018-8-8
vsftpd.service: Main process exited, code=exited, status=2/INVALIDARGUMENT
这个问题可能是不能去监听ipv6，导致的：
配置文件： /etc/vsftpd.conf 
解决办法：listen_ipv6=NO
https://blog.csdn.net/zhezhebie/article/details/78775008

解决github上传ssh-key后仍须输入密码的问题
上传pubkey后，remote改为git@github.com:netjianl/work-doc.git。
https://blog.csdn.net/baidu_35085676/article/details/53456884

2018-8-7
这里有mcc,mnc列表，但是我自己的电信卡居然是46011，找不到，找不到。
https://cellidfinder.com/mcc-mnc

linux统计文件夹某一些文件的大小总和
使用如下命令，-m 代表MB
du -m 20140507155000* | awk '{sum += $1}; END{print sum}'

2018-8-6
把旧的git移动的过程，能不能写个脚本来完成？

这个软件下载百度盘上的东西飞快。
http://pandownload.com/


2018-8-2
对于旧的ubuntu，也可以使用apt
关于非LTS版Ubuntu系统无法update的解决方法
https://jingyan.baidu.com/article/7c6fb42809854380652c9067.html

原来使用的mnc=2不返回数据了。
curl "http://api.cellocation.com:81/cell/?mcc=460&mnc=1&lac=10173&ci=180452649&output=json"
{"errcode":0, "lat":"22.53485107", "lon":"114.0249939", "radius":"580", "address":"广东省深圳市福田区沙头街道泰然五路;香蜜湖路与泰然六路路口东77米"}


ubuntu中文文件名乱码
https://blog.csdn.net/xiao888lin/article/details/7865359

2018-7-20
全国企业信用信息公示系统，网址：http://gsxt.saic.gov.cn/
做人脸识别的爱华盈通，居然是个新疆的公司。

2018-7-17
ARM DS-5.26.0安装及创建C程序
https://blog.csdn.net/qq_27295631/article/details/68582582
下载地址链接：http://pan.baidu.com/s/1bpMScFH 密码：dwf8

2018-7-16
几个项目的进度：
m60:2015.10.20拿到sdk, 1月给过中兴样机，但是问题很多，不稳定。4月提供的样机可用。仍有重启，掉网情况。直到7月联芯出了最后一个大版本。
    其中voip 2016.1月开始，7月底稳定。

p28:2016.12.20开始， 2017年4月送样机。时间主要在slic上。
    其中fax, 2017年2月底给第一个测试版，18年2月，放弃测试。

p59:2017年2月回板，4月开始， 11月调完wifidog，送样。

p56:2016年8月开始，12月送样机。

2018-7-15
在cpe-df上配置网络:
brctl delif br0 eth0
ifconfig eth0 down
ifconfig eth0 hw ether 18:a9:05:91:e3:c2
ifconfig eth0 192.168.1.93 
ifconfig br0 192.168.19.1 up  netmask 255.255.252.0 up
route add default gw 192.168.1.2
echo nameserver 192.168.1.2 > /etc/resolv.conf
echo nameserver 8.8.8.8 >> /etc/resolv.conf
iptables  -t nat -D POSTROUTING -o eth0 -j MASQUERADE
iptables  -t nat -A POSTROUTING -o eth0 -j MASQUERADE
echo "1" > /proc/sys/net/ipv4/ip_forward
iptables -t nat -D PREROUTING -d 192.168.1.93/32 -i eth0 -j DNAT --to-destination 192.168.19.199
iptables -t nat -A PREROUTING -d 192.168.1.93/32 -i eth0 -j DNAT --to-destination 192.168.19.199

2018-7-14
那个l2tpv3的，如果使用2.6.31的内核，存在2路的情况下，会出
Dropping packet:__nf_conntrack_confirm:467 0 2 0 :: 115 0 2 0 115
似乎加上：
iptables -A FORWARD -i br0 -o eth0 -s 192.168.19.199 -j ACCEPT
就好了，但是，删掉他，还是可以的。
但是，但是，如果重启了，再也不行了，真的很苦闷啊。

2018-7-13
fdupes这个工具可以查找同样的文件，不用自己去写脚本了。
https://linux.cn/article-6127-1.html

这个calc插件在某些情况下才计算，在很多地方不计算。

这个visual studio code 貌似升级很频繁。这两天下载的，就有新版本了。

2018-7-12
使用visual studio code这个软件，看起来还不错。长得和sublime差不多，打开大文件也没有什么压力。
升级到1.25后，也能输入中文了。用一段时间看看吧。

增加了一个calc插件，只要输入=以后，就自动计算了，不用再输入热键了。

吴曦那里的限速非常奇怪，昨天使用如下指令进行
-A FORWARD -s 192.168.19.199/32 -m limit --limit 714/sec --limit-burst 699 -j ACCEPT
-A FORWARD -d 192.168.19.199/32 -m limit --limit 714/sec --limit-burst 699 -j ACCEPT
-A FORWARD -d 192.168.19.199/32 -j DROP
-A FORWARD -s 192.168.19.199/32 -j DROP
根本不限速，如果去掉limit，直接drop，是有效果的。
今天早上吴曦再测试，又可以了，真的无法解释。

张悦玲调试电话，这个codec在电话上应该没有调试过。加上了codec的驱动后，电话就无法接通了。再加上cp的一个可以录音的参数区后，可以拨打电话了，但是，没有声音，而且20秒必断。

2018.7.4
iw - 3.17-1,  - 1-6, 8021xd - 1, ated - 1, libiwinfo-lua  liblua libpcap - 1.5.3-1
lua - 5.1.5-1  luci  reg rpcd switch uhttpd wireless-tools

not in 
libnvram, macwriter

2860sh

2018.7.2
at+ccho="A0000005591010FFFFFFFF8900000100"
AT+CSIM=42,01A4040010A0000005591010FFFFFFFF8900000100
AT+CSIM=22,81E2910006BF3E035C015A
AT+CCHC=1

AT+CGLA=1,4,001E
AT+CSIM=42,00A4040010A0000005591010FFFFFFFF8900000100

2018.6.11
OneNet网址： https://open.iot.10086.cn/
    帐号： ljdonenet
    密码： tz123456789

2018.5.27
在p53上使用新的openssl，库变小了，但是整个文件却变大了。好奇怪的事情。

2018.5.24
nemo这个文件管理器可以使用open terminal here了。
感觉现在这个系统除了si4不好用，其他都可以使用了。
deepin-terminal这个终端看起来不错，标题栏直接是最后的目录名称，还可以改。就先用它了。

2018.5.23
终于可以再次输入中文了。真不容易啊。

2018.5.16
Linux控制台终端下设置关闭声音的方法
https://www.linuxidc.com/Linux/2008-10/16969.htm

2018.5.15
cinnamon-settings: it seemed no works full functional.

linux find prune exec 排除某目录或文件 执行
https://blog.csdn.net/ysdaniel/article/details/7995681

在Ubuntu 18.04/16.04下隐藏FireFox标题栏
https://ywnz.com/linuxjc/1700.html

ubuntu 17.10 配置静态IP地址
http://www.mamicode.com/info-detail-2096944.html
my files:
network:
    ethernets:
        eno1:
            addresses: [192.168.19.199/22, 192.168.0.50/24]
            dhcp4: no
            gateway4: 192.168.19.1
            nameservers:
                addresses: [192.168.19.1]
    version: 2


2018.5.10
解决wine安装程序的乱码问题
env LC_ALL=zh_CN.UTF-8 wine xxx.exe

2018.5.9
export LD_LIBRARY_PATH=~/work/yaoyuan_phone/arm-gcc/usr/lib

2018.4.21
VIM 蓝色注释看不清楚:https://blog.csdn.net/beiquandeng/article/details/43341651
vi ~/.vimrc 加入如下内容
hi Comment ctermfg =blue



2018.4.20
当存在多个adb设备时: 用adb device, adb -s xxxx shell
https://blog.csdn.net/gaojinshan/article/details/9455193

2018.4.14
cd /sys/module/usbserial/drivers/usb-serial:generic
echo 19d2 0536 > new_id
就可以在pc上出现v10的串口了.

2018.4.3
通过usb转的网卡连接v10话机.
sudo route add -host 192.168.0.1 dev eth2


2018.3.13
桌面上的p59的2.4gwifi不能连接了. 运行了48天.
使用ifconfig ath0 down && ifconfig ath0 up 看起来没有作用.

rdesktop可以把本地磁盘带到远程计算机.
rdesktop 192.168.19.212 -g 1540x830 -u jian -p solong123 -r disk:f=/media/jian/518C138300565C98,g=/
http://www.coolcode.org/?action=show&id=88

2018.3.12
sudo yum install glibc-devel.x86_64

为什么fedora每次安装, 都使用15g空间?

devmem 0x90c00000
0x08136110

ID Number (IDNMBR, Offset = 0x00)
Table 4-2. ID Number (IDNMBR, Offset = 0x00)
Bit     Name          Type          Description    Reset Value Reset Type
[31:28] -              -            Reserved - -
[27:12] product ID     RO           Product ID     0x8136 -
[11:8]  version ID     RO           Version ID     0x1 -
[7:0]   ID[7:0]        RO           ID[6:2]:       Package ID I/O trimming -

8136有4个软件寄存器:
devmem 0x90c000dc 32 0x02
重启后不保存, 没有多少作用了.

bc的使用
http://blog.chinaunix.net/uid-23929712-id-2650421.html
主要是如果要小数点, 那么需要这样设置:
scale=5

这里有讲解如何计算实际利率的.
https://www.rong360.com/gl/2017/09/18/142854.html
公式是这样的:
实际年利率=a*n*24/(n+1)(*这个符号代表乘号)。
a代表月费率，n代表借了几个月。

2018.3.9
mount -t nfs 192.168.19.199:/opt/work/ /mnt/nfs --nolock
cd /mnt/nfs/gm8136s/apps/tzvideo-OneNet-2.0/
ps | grep rc.onenet | grep -v grep | awk '{print $1}' | xargs kill -9
killall tzvideo
./tzvideo -c /etc/config/config.base.json

2018.3.6
ubuntu增加exfat支持:
sudo apt-get install exfat-utils
没有必要重启, 直接可以使用了.
不过, gm系列的uboot似乎不支持exfat啊.

deepin这个系统安装到虚拟机之后, 编译ath9.5的buildall居然会挂掉, 如果一直待机, 倒没有发现这样的现象.
应该是休眠了? 刚才把窗口最小号之后, 过了一段时间后还响了一下, 先关闭半小时待机吧. 就是休眠的问题了.

2018.3.3

在联想的笔记本上安装一个操作系统好像好困难的样子. 还是郑达终于把它装起来了.
安装后virtualbox还有问题, 启动虚拟机就报出什么不能创建进程之类的, 后来使用"分离式启动"才跑起来.

使用一个新deepin来编译系统吧:
ssh jianliang@192.168.19.41 -F ~/work/jian-doc/work/env/ssh_config

2018.3.1
对dd的pid发送USR1指令，然后在dd窗口就可以看到当前I/O信息。命令如下，
kill -USR1 `pgrep '^dd'`

sort -r 是反排序.

在linux下dd写iso到u盘中, 在windows下显示的是没有格式化.

2018.2.7
RTP与RTCP协议介绍
http://www.cnblogs.com/jiayayao/p/6218503.html

2018.2.2

这样写100个参数居然要14秒
#set -x
export ECHO_STYLE_00="\033[0m"        # default style(black background, white foreground)
export ECHO_STYLE_01="\033[41;33;1m"  # red background, yellow foregound bold
export ECHO_STYLE_02="\033[42;33;1m"  # red background, yellow foregound bold
date_start=$(date +%s)
count=0
while [ true ] ; do
        cfg -a test_$count=$count
        count=$(($count+1))
        if [ $count -eq 100 ] ; then
                break
        fi
done
date_end=$(date +%s)
echo  -e "${ECHO_STYLE_00}本次操作运行了：$((date_end-date_start))秒${ECHO_STYLE_00}"



curl "http://api.cellocation.com:81/cell/?mcc=460&mnc=2&lac=10173&ci=180452649&output=json"
{"errcode":0, "lat":"22.53485107", "lon":"114.0249939", "radius":"580", "address":"广东省深圳市福田区沙头街道泰然五路;香蜜湖路与泰然六路路口东77米"}

2018.1.30
这个可以运行并转换成功, 看看能不能减少一些体积.
TransformMP4 -v video_20180126231056.h264 video_20180126231056.aac 1.mp4

2018.1.25
ddr 590   290ma  15fps.

2018.1.23
来清除原来的svn吧, 把这些svn改为git, 保存到本地硬盘, 百度云盘上就好了. 其他就不管了.
第一次没有输入密码, 第二次居然自己就开始了. 好奇怪的事情呢.
git svn clone --mirror http://192.168.1.123/svn/ZLT2830


ZLT2830 里面只有白俊剑了. 更新时间2012/11/9--2012/11/15 里面只有肖智威的几次提交.
zlt2815 里面只有苗立双, 更新时间2010/10/27--2011/4/1  里面有肖智威, 苗立双 lixuan的提交.

2018.1.19
dnsmasq貌似不能关闭监听的tcp 53端口. 按道理也完全没有必要监听.

2018.1.12
{
	"type":"update", "url":"http://192.168.0.50/elevator_v1.00.zip"
}

function readdata(filename)
	file = io.open(filename, "r")
	jsondata = file:read("*a")
	file:close()
end

function update(url)
	os.execute("curl"..url)
	os.execute("/etc/init.d/rc.update")
end


local cjson = require "cjson"
readdata("/tmp/onenet_cmd.json")
local onenet_cmd=cjson.decode(jsondata)
print(onenet_cmd["type"])
if (onenet_cmd["type"] == "update") then
	print("a update cmd")
end



2018.1.11
local cjson = require "cjson"
local file = io.open("/tmp/onenet.json", "r");
assert(file);
local onenet=file:read("*a");
file:close();
screen:print(10,10,onenet,white);

-2018.1.8
-在没有咪头的情况下, 采集的声音居然是噪声.
-在audacity中引入, 那么使用8k和44.8k, 听起来没有什么不同.
-
-2018.1.5
-sensor的源码在isp328/input_module中.
-那个博客园的密码改为Oo0keeper

2018.1.2
计算机的速度又开始变慢, 那个xorg又开始狂占cpu.
乱改了参数后, 只有桌面图, 什么都没有啦, 最后解决的方法居然是插入一个u盘, 然后右键, open一个terminal, 运行
dconf reset -f /org/compiz/
setsid unity




我的iphone mac fc:e9:98:14:58:1f
待解决问题：
ap-cp:
保存无线参数后断网, 看起来只有重启.
加上nob选项
继续减少wifi的选项.

每次重新安装的机器要:
git config --global user.email jianliang@szotzed.net
git config --global user.name jianliang
git config --global push.default simple



2017-12.28
killall wpa_supplicant
192.168.19.1的网页密码改为123456



2017-12.26
这篇文章写了如何解决sh脚本异常：/bin/sh^M:bad interpreter: No such file or directory
http://www.cnblogs.com/pipelone/archive/2009/04/17/1437879.html
就是使用vi 进行::set ff=unix


2017-12.24
还是关闭shift按键进行输入法切换, 太扰民了. 直接使用ctrl+space吧. 不过这在中英文切换时貌似又不少非常方便了.

2017-12.23
7520使用usb打流:
7520侧
/iperf # ./iperf -c 192.168.0.157 -i 1
------------------------------------------------------------
Client connecting to 192.168.0.157, TCP port 5001
TCP window size: 21.3 KByte (default)
------------------------------------------------------------
[  4] local 192.168.0.1 port 58460 connected with 192.168.0.157 port 5001
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0- 1.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  1.0- 2.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  2.0- 3.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  3.0- 4.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  4.0- 5.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  5.0- 6.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  6.0- 7.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  7.0- 8.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  8.0- 9.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  9.0-10.0 sec   128 KBytes  1.05 Mbits/sec
[  4]  0.0-10.1 sec  1.38 MBytes  1.15 Mbits/sec
/iperf # iperf -s
-sh: iperf: not found
/iperf # ./iperf -s
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  5] local 192.168.0.1 port 5001 connected with 192.168.0.157 port 35288
[ ID] Interval       Transfer     Bandwidth
[  5]  0.0-10.1 sec  52.8 MBytes  43.9 Mbits/sec


pc侧:
jian@jian-OptiPlex-9020:/opt/work/ath9.5/build$ iperf -s
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  4] local 192.168.0.157 port 5001 connected with 192.168.0.1 port 58460
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0-10.4 sec  1.38 MBytes  1.11 Mbits/sec
^Cjian@jian-OptiPlex-9020:/opt/work/ath9.5/build$ iperf -c 192.168.0.1 -i 1
------------------------------------------------------------
Client connecting to 192.168.0.1, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.0.157 port 35288 connected with 192.168.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0- 1.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  1.0- 2.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  2.0- 3.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  3.0- 4.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  4.0- 5.0 sec  5.12 MBytes  43.0 Mbits/sec
[  3]  5.0- 6.0 sec  5.38 MBytes  45.1 Mbits/sec
[  3]  6.0- 7.0 sec  5.38 MBytes  45.1 Mbits/sec
[  3]  7.0- 8.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  8.0- 9.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  9.0-10.0 sec  5.25 MBytes  44.0 Mbits/sec
[  3]  0.0-10.0 sec  52.8 MBytes  44.1 Mbits/sec




iptables -vnL -t nat
可以看到每个链通过的流量.


2017-12.22
这个侠诺的路由器连dhcp都不能用了, 搞了半天.

一开始iperf3不能运行, 重新编译一次就好了, 难道前面编译的有问题?

这个8188的模块上行下行iperf3打流的速度都在17Mb左右.

2017-12.21
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 tz8135.bin
sf probe 0; sf erase 0x0 ${filesize}; sf write 0x2000000 0x0 ${filesize};
写全文件总是不知道什么时候写完呢.

vi中这个指令可以轻松替换掉粘贴进去的tab变成了空格
20,33s#        #\t#

wget这样下载更好:
wget ftp://192.168.1.123/qsdk/docs -nv -m --cut-dirs=2 -nH --restrict-file-name=nocontrol

curl居然不能下载整个ftp目录.

密码改为solong123

2017-12.20
得到imei:
curl -s "http://192.168.0.1/goform/goform_get_cmd_process?isTest=false&cmd=imei" | awk -F '"' '{print $4}'

这样可以快速关掉摄像头的电源
sshpass -p keep0It3 ssh admin@192.168.0.1 -p 8357 "echo 0 >  /sys/class/leds/camera/brightness"

curl "http://192.168.0.1/goform/goform_get_cmd_process?isTest=false&cmd=imei"

2017-12.19
这样来取 imei号.
curl -F test=test "http://192.168.0.1/goform/goform_set_cmd_process?isTest=false&goformId=LOGIN&username=YWRtaW4=&password=YWRtaW4="
好像不用登录过程呢:
curl -F test=test "http://192.168.0.1/goform/goform_get_cmd_process?isTest=false&cmd=imei"

p25中
AT^MODIMEI=123456789012347
读取imei           AT^READIMEI

tz_test
mount -t nfs 192.168.0.50:/opt/work/ /mnt/nfs --nolock
cd /tmp
cp /mnt/nfs/gm8136s/images/tz_test/rootfs-cpio_master.squashfs.img .
flashcp -v rootfs-cpio_master.squashfs.img /dev/mtd2



mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 elevator.bin
sf probe 0; sf erase 0x0 ${filesize}; sf write 0x2000000 0x0 ${filesize};



这样可以执行简单的程序:
sshpass -p keep0It3 ssh root@192.168.0.2 -p 8357 "ls /"

这样来kill脚本:
ps | grep rc.onenet | grep -v grep | awk '{print $1}' | xargs kill -9

这样就可以简单的向系统推一个文件了:
sshpass -p keep0It3 scp -P 8357 elevator_v1.00_flash.zip root@192.168.0.2:/tmp/

                        nsboot.bin
00010000 00050000 UBOOT u-boot.bin
00060000 00200000 LINUX uImage
00260000 00AA0000 FS    rootfs-cpio_master.squashfs.img
00D00000 00200000 USER0 GM8135_2MP.SPI.jffs2.img

这个启动非法错还是有时候会发生.
传一个16m的文件太大了,还是要使用升级的方式传zip包上去, 现在只有3m多, 后面估计会到10m左右.

2017-12.18
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 rootfs-cpio_master.squashfs.img　
sf probe 0; sf erase 0x260000 ${filesize}; sf write 0x2000000 0x260000 ${filesize};


centos中把ls目录的颜色改为黄色:
http://www.linuxprobe.com/centos-directory-color.html
直接改/etc/DIR_COLORS就可以了:
找到下面这一行：
      DIR 01;34（01：粗体，34：蓝色）
改为：
      DIR 01;33（01：粗体，33：黄色）
在黑色背景下蓝色几乎无法看清.

2017-12.14
centos 最小化版设置静态ip:
vim "/etc/sysconfig/network-scripts/ifcfg-enp0s3"
增加:
BOOTPROTO=static
IPADDR=192.168.19.99
NETMASK=255.255.252.0
GATEWAY=192.168.19.1
ONBOOT=yes
再修改一次resolv.conf就可以上网了

gm的pc工具每次会重新读文件, 貌似大部分工具都是这样做的.

2017-12.13
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 flash.bin　
sf probe 0; sf erase 0x0 ${filesize}; sf write 0x2000000 0x0 ${filesize};

在虚拟机上编译gm8136s, 第一次需要500多秒. clean后要163秒.

2017-12.12
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 rootfs-cpio_master.squashfs.img　
sf probe 0; sf erase 0x260000 ${filesize}; sf write 0x2000000 0x260000 ${filesize};
这次成功了.

又出现了flashcp的时候挂了, 难道是在运行tzvideo?

dropbear居然不执行了?
dropbear -E -F
[335] Jan 01 00:18:17 Failed loading /etc/dropbear/dropbear_rsa_host_key
[335] Jan 01 00:18:17 Failed loading /etc/dropbear/dropbear_dss_host_key
[335] Jan 01 00:18:17 Early exit: No hostkeys available. 'dropbear -R' may be useful or run dropbearkey.

这次居然擦除的过程中出现了panic，悲催了．来测试如何在串口时使用sd卡升级吧．
fatls mmc 0　这个命令可以列出mmc上的文件．
mw.b 0x2000000 0xFF 0x800000　这个不知道是什么，每次都会调用
fatload mmc 0 0x02000000 rootfs-cpio_master.squashfs.img　　这个读到文件了：
reading rootfs-cpio_master.squashfs.img
2113536 bytes read in 994 ms (2 MiB/s)

这样写看看：
sf probe 0; sf erase 0x260000 0x300000; sf write 0x2000000 0x260000 0x300000;
好像不动了，郁闷了．
分解执行，那么其实是写成功的，但在最后一步感觉死机，断电后，启动系统成功了．
sf probe 0; sf erase 0x260000 ${filesize}; sf write 0x2000000 0x260000 ${filesize};


这次flashcp为什么没有擦除动作？ 只有在把所有的命令输入的情况下，　才出现了这个不擦除的现象．

2017-12.11
在当前的运行环境下，　从pc到8136进行打流非常慢，　只有１.3左右，　而8136向pc打包，　有40多ｍ

p25的超级用户：sztozed 85383000

2017-12.10
从flash中读出sysheader:
dd if=/dev/mtd4 of=sysheader.bin bs=256 count=1

只要简单的向头256字节写一串数据, 那么系统就不启动了.
cd /tmp && flashcp -v template_8136 /dev/mtd4

为什么有时候有mtd4, 有时候又没有?
把user区扩大一点, 到2m吧:
gm8136默认刷机配置, 这个配置不会报错了.
                        nsboot_8136S_1146_860.bin
00010000 00050000 UBOOT u-boot_spi.bin
00060000 00200000 LINUX uImage
00260000 00AA0000 FS    rootfs-cpio_master.squashfs.img
00D00000 00200000 USER0 GM8135_2MP.SPI.jffs2.img

2017-12.9
使用ccache编译gm8136s也能快很多,应该从250秒左右到了55秒, 简直惊人.

在mini 18.3上要运行:
sudo apt install libssl-dev
libevent才能编译出带有ssl的库, 貌似它的检查机制问题比较多.

gm8136s有时候会莫名其妙的完全重新编译, 好奇怪的事情.

有时候串口线会停止工作. 重新拔插就好了.

git log 支持--since参数:
git log --pretty='%aN' --since="2017-06-22" | wc -l

2017-12.8
gm8136默认刷机配置
                        nsboot_8136S_1146_860.bin
00010000 00050000 UBOOT u-boot_spi.bin
00060000 002A0000 LINUX uImage
00300000 00C00000 FS    rootfs-cpio_master.squashfs.img
00E00000 00100000 USER0

2017-12.7
usb的颜色是红, 白, 蓝 黑

2017-12.6
chrome中设置插件貌似没有看到从界面直接进去的地方, 需要输入:
chrome://extensions
然后在这个界面把插件拖进去就可以了.

这里有一个marddown preview plus的:
http://www.ooso.net/archives/611
下载代码:
git clone git://github.com/volca/markdown-preview.git
下载后make一下,产生一个zip报, 拖到chrome的插件窗口中就安装上了, 这个支持md后缀名, 总算可以使用chrome直接看md文件了. sublime中的插件总是报错, 考虑删掉.

在内核方面, 貌似8135和8136没有区别.
使用gm8136tool这个工具, 那么对于8135, 需要将bootcode file这个文件改为:nsboot_8135S_950_712.bin, 内核和文件系统看起来不需要修改.
好像内存自动处理了.

2017-11.29
chrome 设置为默认的浏览器后, sublime查看md, 仍然会出非法错误.

firefox又有三个进程占用100%的cpu啊, 太强悍啦.

.git占用的空间有时候会超级大:
jian@jian-OptiPlex-9020:~/work/jian-doc$ du .git -sh
35M .git
jian@jian-OptiPlex-9020:~/work/jian-doc$ git gc
Counting objects: 1512, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (861/861), done.
Writing objects: 100% (1512/1512), done.
Total 1512 (delta 946), reused 1048 (delta 624)
jian@jian-OptiPlex-9020:~/work/jian-doc$ du .git -sh
5.7M  .git


2017-11.28
firefox居然占用了所有的cpu, 导致p59的编译时间高达1172秒.

2017-11.27

还有若干个ko根本不知道从那里编译出来的:
codec.ko                  ---
favc_rc.ko                ratecontrol/favc_rc.ko
fisp_algorithm.ko         ---
flcd200-pip.ko            LCD200_v3
frammap.ko                frammap
ftpwmtmr010.ko            ---
log.ko                    ---
pmonitor.ko               pmonitor
vcap0.ko                  vcap300
vpd.ko                    ---
adda308.ko                adda308
em.ko                     ---
fe_common.ko              front_end
fisp_ov2715.ko            ---
fmcp_drv.ko               ftmcp100
fscaler300.ko             scaler300和 pseudo_scaler300都有...
gm2d.ko                   gm2d和pseudo_gm2d都有...
ms.ko                     ---
sar_adc.ko                SAR_ADC
vcap300_common.ko         vcap300
audio_drv.ko              audio_drv
favc_enc.ko               ----
fisp328.ko                ----
flcd200-common.ko         LCD200_v3
fmjpeg_drv.ko             ftmcp100/fmjpeg_driver
ft3dnr200.ko              ft3dnr200
gs.ko                     ----
osd_dispatch.ko           osd_dispatch
sw_osg.ko                 swosg
vcap300_isp.ko            vcap300/input_module


2017-11.26
export LANG="en_US.UTF-8"

2017-11.25
把p11-gcc和mips-gcc改成系统的ccache, 第二次全编译, 就快了.
ap-cp clean: 31秒 build: 257秒
cpe-ap clean: 16秒 build: 243秒
ap-router_4g_industry clean: 24秒 build: 522秒
ap-p11_4g_router clean: 51秒 build: 383秒
ap-p51_4g_router clean: 24秒 build: 371秒
tozedap-p59 clean: 22秒 build: 492秒
cpe-5g2g clean: 19秒 build: 227秒
cpe-df clean: 18秒 build: 268秒

2017-11.24
当前开发板上的ko
-rw-rw-r--    1 1000     1000         42900 Nov 23  2017 adda308.ko
-rw-rw-r--    1 1000     1000        118620 Nov 23  2017 audio_drv.ko
-rw-rw-r--    1 1000     1000        190432 Nov 23  2017 codec.ko
-rw-rw-r--    1 1000     1000        193796 Nov 23  2017 em.ko
-rw-rw-r--    1 1000     1000        172640 Nov 23  2017 favc_enc.ko
-rw-rw-r--    1 1000     1000         22012 Nov 23  2017 favc_rc.ko
-rw-rw-r--    1 1000     1000         10812 Nov 23  2017 fe_common.ko
-rw-rw-r--    1 1000     1000        199132 Nov 23  2017 fisp328.ko
-rw-rw-r--    1 1000     1000        132040 Nov 23  2017 fisp_algorithm.ko
-rw-rw-r--    1 1000     1000         16468 Nov 23  2017 fisp_ov2715.ko
-rw-rw-r--    1 1000     1000         37004 Nov 23  2017 flcd200-common.ko
-rw-rw-r--    1 1000     1000        126476 Nov 23  2017 flcd200-pip.ko
-rw-rw-r--    1 1000     1000         95980 Nov 23  2017 fmcp_drv.ko
-rw-rw-r--    1 1000     1000         52148 Nov 23  2017 fmjpeg_drv.ko
-rw-rw-r--    1 1000     1000         30344 Nov 23  2017 frammap.ko
-rw-rw-r--    1 1000     1000        270368 Nov 23  2017 fscaler300.ko
-rw-rw-r--    1 1000     1000        117288 Nov 23  2017 ft3dnr200.ko
-rw-rw-r--    1 1000     1000         13144 Nov 23  2017 ftpwmtmr010.ko
-rw-rw-r--    1 1000     1000         26264 Nov 23  2017 gm2d.ko
-rw-rw-r--    1 1000     1000        214968 Nov 23  2017 gs.ko
-rw-rw-r--    1 1000     1000         70432 Nov 23  2017 log.ko
-rw-rw-r--    1 1000     1000        169688 Nov 23  2017 ms.ko
-rw-rw-r--    1 1000     1000         14980 Nov 23  2017 osd_dispatch.ko
-rw-rw-r--    1 1000     1000          5384 Nov 23  2017 pmonitor.ko
-rw-rw-r--    1 1000     1000         24796 Nov 23  2017 sar_adc.ko
-rw-rw-r--    1 1000     1000         34868 Nov 23  2017 sw_osg.ko
-rw-rw-r--    1 1000     1000          6508 Nov 23  2017 vcap0.ko
-rw-rw-r--    1 1000     1000        362716 Nov 23  2017 vcap300_common.ko
-rw-rw-r--    1 1000     1000         12444 Nov 23  2017 vcap300_isp.ko
-rw-rw-r--    1 1000     1000        504668 Nov 23  2017 vpd.ko


在77上记录的编译时长, 还是7月的数据, 当时p59还不存在, 晚上再试试.
ap-cp                  clean: 8秒  build: 914秒
cpe-ap                 clean: 5秒  build: 623秒
ap-router_4g_industry  clean: 9秒  build: 1226秒
ap-p11_4g_router       clean: 6秒  build: 1279秒
ap-p51_4g_router       clean: 10秒 build: 1281秒
cpe-5g2g               clean: 7秒  build: 559秒
cpe-df                 clean: 5秒  build: 976秒

在联想的虚拟机上的情况是:
ap-cp                  clean: 26秒 build: 652秒
cpe-ap                 clean: 11秒 build: 379秒
ap-router_4g_industry  clean: 22秒 build: 933秒
ap-p11_4g_router       clean: 22秒 build: 748秒
ap-p51_4g_router       clean: 21秒 build: 692秒
tozedap-p59            clean: 19秒 build: 897秒
cpe-5g2g               clean: 17秒 build: 327秒
cpe-df                 clean: 14秒 build: 588秒

ap-cp clean: 27秒 build: 239秒
cpe-ap clean: 17秒 build: 376秒
ap-router_4g_industry clean: 19秒 build: 900秒
ap-p11_4g_router clean: 20秒 build: 690秒
ap-p51_4g_router clean: 23秒 build: 678秒
tozedap-p59 clean: 21秒 build: 874秒
cpe-5g2g clean: 17秒 build: 338秒
cpe-df clean: 13秒 build: 522秒

2017-11.23
sublime使用ctrl+end到文件尾部.

2017-11.22
为什么我这个p59没有看到5.8g的ssid了? 不是没有5.8g, 而是2.4g的消失了, 难道是需要完全重新编译的原因.

要把alias放在~/.bash_aliases中, 放在.profile中没有效果.

每次重新启动机器tftp看起来都没有开:
sudo service tftpd-hpa restart

p59又跑了两天了, 没有重启, 那么再升级一个版本吧. 编译的时间长达643秒, 第二次编译也多达99秒.

p59的编译中, Making uboot tools...里面还有clean的动作.

mksquashfs使用系统自带的就可以用了, 不需要在仓内保留一个bin档.

升级了firefox, 居然不能用了. 但是那个markdown viewer不能用了, 其他的要用mdown这样的后缀, 而且看起来是乱码.

2017-11.21
使用这个指令来修改一下vim的配色方案，默认的配色注释是蓝色的，在黑底的情况下根本看不清
 echo "colorscheme koehler" >> $HOME/.vimrc

使用硬链接可以简单的把每个工作目录中的需要写的文档文件链接到我的这个目录文档中, 只有在sublime中修改后, 各个目录中也看起来修改了.
说明在这里:
http://www.cnblogs.com/sonic4x/archive/2011/08/05/2128543.html

为什么直接预览md, firefox直接挂掉了, 用file:///home/jian/work/gm8136s/document/read.md这样的方式好像还能用.

找到空目录:
find -type d -empty

这个脚本给每个空目录加一个.gitignore
#!/bin/sh
empty_paths=$(find -type d -empty)
for i in ${empty_paths}
do
  touch ${i}/.gitignore
done


2017-11.20
#!/bin/bash
CURRENT_PATH=$(cd "$(dirname "$0")"; pwd)
LD_PRELOAD=$CURRENT_PATH/libsublime-imfix.so subl
这样就取得了当前目录,

sublime升级到了3143. 感觉也没啥区别.
VMware-player版本都到14了, 为什么我还在使用12这个版本.

2017-11.19
win7的共享不知道什么时候出了问题:
https://jingyan.baidu.com/article/9c69d48f603d4013c9024e2b.html

使用2014年的arm gcc 4.8的版本编译的内核也可以使用, 并且大小减小了40k.
最新的编译器在这里可以下载: 下次下载一个最新的试试.
https://releases.linaro.org/components/toolchain/binaries/latest/

2017-11.15
如果要换行, 在markdown中的行最后增加两个空格就可以了.

使用这个命令可以看看image下面的包是否都有了:
tree ../images/ -L 1
不过这样似乎也不算太好, 我实际想看每个zip文件的大小.

sublime 快速查找文件, 还是很实用的, 不用鼠标点半天到目录树中寻找, 当然, 要记得文件名称.
Ctrl+P 打开搜索框。举个栗子：1、输入当前项目中的文件名，快速搜索文件，2、输入@和关键字，查找文件中函数名，3、输入：和数字，跳转到文件中该行代码，4、输入#和关键字，查找变量名。
http://blog.csdn.net/cywosp/article/details/31791881

当前ath9.5仓的大小是3.1G, 还是不小啊.

p59的reset健, 看起来是起作用了.

在centos7 1708这个版本上strongswan总是编译不了. 算了, 先放放.
在mini上面的不行, 但是用普通的那个, 就没有问题, 奇怪啊.

2017-11.14
minicom最近的一次更新在今年, 增加的是一个漏洞的修补, 而上一次的更新在2013年.

minicom可以自动换行的:
在minicom中自动换行：Ctrl+A Z W
组合键的用法是：先按Ctrl+A组合键，然后松开这两个键，再按Z键。另外还有一些常用的组合键。
S键：发送文件到目标系统中；
W键：自动卷屏。当显示的内容超过一行之后，自动将后面的内容换行。这个功能在查看内核的启动信息时很有用；
C键：清除屏幕的显示内容；
B键：浏览Minicom的历史显示；
X键：退出Minicom，会提示确认退出。
http://blog.sina.com.cn/s/blog_6d2a0a1a0100vyoz.html

如何在win7上安装rndis:
http://developer.toradex.com/knowledge-base/how-to-install-microsoft-rndis-driver-for-windows-7
可以在win7的机器上看rtspd的流媒体图像了.

使用自己编译的busybox, 出错了
/squashfs_init: line 24: echo: not found
/squashfs_init: line 25: mdev: not found
/squashfs_init: line 26: ln: not found
/squashfs_init: line 27: /bin/linuxrc: not found
/squashfs_init: line 28: can't open /dev/console: no such file
增加一些busybox的选项, 这些错误消失了, 但是继续错误:
Kernel panic - not syncing: [ISP] failed to open cfg file: /mnt/mtd/isp328.cfg

p59又重启了, 忘记开重启记录了.

这样来设置p59的上网吧:
ifconfig br0:2 192.168.19.41
route add default gw 192.168.19.1
echo nameserver 192.168.1.2 >> /etc/resolv.conf


2017-11.13
cenos 下要安装yum install gettext-devel, 否则会出现
error: possibly undefined macro: AC_LIB_PREFIX这样的错误.

centos中居然没有ccache?
sudo yum install epel-release
sudo yum -y install yum-utils
这样之后, 就有ccache 了.


gitk中在右边选择了某个文件, 右键, highligth this too, 那么, 所有这个文件的修改的commit都会加粗, 看起来非常实用的功能.

下午又看到nautilus这个进程狂占cpu, 这个居然是Browse the file system with the file manager, 有一个窗口开着, 里面在浏览wget下载的无数个文件, 这些文件又已经被删除了...

使用iftop可以看到从哪个ip有比较大的流量,
Display paused       191Mb      381Mb                      572Mb    763Mb                 954Mb
└─────────────────────┴──────────┴──────────────────────────┴────────┴──────────────────────────
jian-OptiPlex-9020               => 151.101.64.194                       30.7kb  30.7kb  30.7kb
                                 <=                                      1.13Mb  1.13Mb  1.13Mb
再使用这样的指令
sudo netstat -tpn | grep 151.101.64.194
tcp        0      0 192.168.19.199:58996    151.101.64.194:80       ESTABLISHED 2258/wget
就找到是哪个程序在使用网络了.

这样就可以实现不输入密码登录了:
alias s='sshpass -p sztz369147258 ssh root@192.168.0.1 -p 8357'

2017-11.10
这样连接我的机器:
mount -t nfs 192.168.19.199:/opt/work/ /mnt/nfs --nolock

p59上网:
ifconfig br0:1 192.168.19.198
route add default gw 192.168.19.1
echo nameserer 192.168.1.2 > /etc/resolv.conf

154这台机器居然又不能发邮件了, 远程桌面不能连接, 连接显示器有图, 但移动鼠标, 敲击键盘无响应, 直接关机吧.

桌面这台p59居然在5个小时之前重启了, 什么原因呢?

现在报错:
ierror while loading shared libraries: libz.so.1: cannot open shared object file: No
这样试试, 可以开始编译了.
sudo apt-get install lib32z1

2017-11.9
这样就可以运行32位的程序了:
sudo apt install libc6:i386

下载整个网站
wget -r -p -np -k http://xxx.com/xxx

吴曦:
当前p25情况, 陈良去菲律宾场测, 上次是在信号差的情况不能用, 现在改了天线, 在信号差的情况可以用了. 对比以前的硬件有改进.
尼加拉瓜的p27在招标测试. 尼加拉瓜在南美.
斯里兰卡的p27也在测试.
p25的生产并不多, 有了3-4次, 最多的一次只有500台. 第一次试产并没有出现烧掉模块的事情, 虽然硬件的保护电路都是去掉的.
m60的验证软件赵金还在做, 看能否复现复制了文件, 又消失的情况.

还有一种特别的情况, 两台pc连上p25, 一台有线, 一台无线, 两台机器不能ping通, iperf可以使用. 把p25换成其他设备, 就可以ping通了.同样, 如果把无线连接的pc换为一个手机, 又可以ping通.


使用这个指令可以看到和目摄像头的数据流:
./tcpdump -i br0 host 192.168.19.21

当前使用
192.168.19.21.52992 > 120.27.152.80.50920
会不会断线后变掉呢? 先关掉2.4g看看.
断线后变成了:
12:23:20.909491 192.168.19.21.41469 > 114.55.236.207.50920
连服务器都变了啊.
这样可以简单的只查看ip和端口信息:
./tcpdump  -i br0 src 192.168.19.21 -nqt -c 1 2>/dev/null
IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 186
那么用这个脚本来记录吧:
# cat 1
while [ true ] ;
do
  ./tcpdump  -i br0 src 192.168.19.21 -nq -c 1 2>/dev/null
  sleep 60
done
现在非常不稳定呢:
13:56:15.975468 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1041
13:57:16.009342 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1448
13:58:16.050067 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1448
13:59:16.103563 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 389
14:00:16.135934 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1448
14:01:20.048735 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 186
14:02:24.041165 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1448
14:03:27.959077 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1448
14:04:31.095798 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 39
14:05:31.137033 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 389
14:06:31.180022 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 1448
14:07:31.811782 IP 192.168.19.21.41469 > 114.55.236.207.50920: tcp 186
14:08:38.820705 IP 192.168.19.21.41470 > 114.55.236.207.50920: tcp 31
14:09:38.918665 IP 192.168.19.21.41471 > 114.55.236.207.50920: tcp 1309
14:10:40.075863 IP 192.168.19.21.41471 > 114.55.236.207.50920: tcp 1448
14:11:43.760023 IP 192.168.19.21.41473 > 114.55.236.207.50920: tcp 0
14:12:45.912293 IP 192.168.19.21.41474 > 114.55.236.207.50920: tcp 1448
14:13:52.801992 IP 192.168.19.21.41475 > 114.55.236.207.50920: tcp 1448
14:14:53.214129 IP 192.168.19.21.41476 > 114.55.236.207.50920: tcp 1448
14:16:00.865656 IP 192.168.19.21.41477 > 114.55.236.207.50920: tcp 1448
14:17:03.922944 IP 192.168.19.21.41478 > 114.55.236.207.50920: tcp 1448
14:18:14.428582 IP 192.168.19.21.41479 > 114.55.236.207.50920: tcp 0
难道tcpdump会有影响么? 应该也没有道理吧.
好像特别不稳定的样子.

要显示曾经修改过的文件, 包括删除的, 可以使用git whatchanged 列出来.
其他的:
git log --name-status 每次修改的文件列表, 显示状态
git log --name-only 每次修改的文件列表
git log --stat 每次修改的文件列表, 及文件修改的统计
git whatchanged 每次修改的文件列表
git whatchanged --stat 每次修改的文件列表, 及文件修改的统计
git show 显示最后一次的文件改变的具体内容
http://rickie622.blog.163.com/blog/static/2123881120144305217106/

今天这个开发板的rtspd好像比较正常.
在firefox中增加markdown view可以直接查看markdown文件:
https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer/

2017-11.8
cp -n 就不覆盖文件了.

lede中的tcpdump有mini的选项, 但是好像不能编译啊.

在编译.o文件的时候也加上-g选项, 执行:
/usr/share/p11-gcc/staging_dir/usr/bin/mips-linux-gdb dialtool_new core.dialtool_new.6370
Program terminated with signal 11, Segmentation fault.
[New process 6370]
[New process 6357]
[New process 6368]
[New process 6369]
#0  0x77c533b4 in ?? ()

执行bt, 出现了代码: 有一个指针没有判null
#0  0x77b473b4 in ?? ()
#1  0x0040b400 in strip_head_tail_space (str=0x0) at common.c:18
#2  0x00406990 in bm806_report_handle (buffer=0xa57268 "\r\n+SIGNALIND:1,-105,255\r\n") at bm806.c:2861
#3  0x0040195c in thr_process (args=<value optimized out>) at main.c:619
#4  0x77bc83c8 in ?? ()
Backtrace stopped: previous frame inner to this frame (corrupt stack?)

162机器的对外映射端口由13306改为13300-13400。

建一个alias吧, 每次输入好像有点累.
alias s='ssh -p 8357 root@192.168.0.1'

sublime Ctrl+G：跳转到第几行

wget可以安装服务器上的目录进行下载, 然后砍掉目录, 就可以在docs中出现比较好的目录结构了.

在<H264_Rate_Control_User_Guide_V1.0>这个文档中
insmod favc_rc.ko后,
可以看到
cat /proc/videograph/favce_rc/info
在开发板上:
H264 rate control(VG) version: 1.1.11, built @ Jan  9 2015 13:55:18
 chn   mode         fps          bitrate    max.br    init.q  min.q  max.q   qp   I.qp  ip.r
=====  ======  ===============  =========  =========  ======  =====  =====  ====  ====  ====
   0     CBR        30/1            256          0      25      20     51    29    28   25.5
   1     CBR        30/1           2048          0      25      20     51    22    21    8.4
   2     CBR        30/1           4096          0      25      20     51    31    31    9.0
在卡片机上:
H264 rate control(VG) version: 1.1.12, built @ Aug 26 2016 14:21:34
 chn   mode         fps          bitrate    max.br    init.q  min.q  max.q   qp   I.qp  ip.r
=====  ======  ===============  =========  =========  ======  =====  =====  ====  ====  ====
   0    EVBR        25/1              0        600      32      28     51    32    30   108.5
   1     VBR        25/1              0          0      32      28     51    32    30    0.0
两个看起来有比较大的区别, 一个30frame/sec, 一个25frame/sec.


2017-11.7
如何使用快捷键预览markdown文件：
https://www.bbsmax.com/A/MAzAWGqM59/


刘云:
p53的bug修复速度太慢了.

任银善:
使用苗立双的程序挂了2天, 并没有出现某个程序内存增长的情况.

郑达:
dialtool2, 某些情况下会增加cache内存. 还在看.

郑荣俊, 李柱栋:
菲律宾说的wifi参数问题, 应该是原来就没有测试过. 而且没有告诉节点信息, 很多东西要猜.


颜斌 翟志华 李金龙:
车载路由器还要本地广告推送.

王伍:
问是否在局域网测试过.

2017-11.6
早上的碰头会:
吴曦还不知道如何进行iperf,
徐刚雄: p59的wan似乎不太稳定. 新版带看门狗的p53下周5回来. 摄像头的路由器回来, 还要在摄像头板上增加驱动.

江健:
海思方案的机器用户名密码: root klv123
rtsp://ip/11

向杰:
c语言指针比较难懂.

2017-11.5
可以做一个简单的ssh登录器.

2017-11.3
关闭一部分特效, 貌似机器xorg的占有率降低了一点点.
参考这里:https://www.2cto.com/os/201301/181597.html

机器用着用着总觉得好慢, xorg占的cpu比较多, kill掉它, 机器就重新登录了.

atom的流畅度还是没有sublime好吧, 算了, 还是用sublime text吧.

开机后mediascanner-se这个进程总是占用比较大的cpu, 还是把它关掉把:
sudo sh -c "echo manual >> /usr/share/upstart/sessions/mediascanner-2.0.conf"
stop mediascanner-2.0
参考:https://binli.github.io/posts/upstart-skill.html

wget http://192.168.19.199/files/rtspd
chmod +x rtspd

金晶: 当前的漫游仍然会弹portal, 想要去掉, 使用探针的数据, 由于10s, 好像有些慢.

陶嵩: 其他公司的人做的多台同时校准工具, 无法做的自动下载校准程序.

在vlc软件中, 设置:rtsp-tcp之前, 要增加空格, 这样就变成tcp协议.

exceltk这个工具看起来还不错:
exceltk.exe -t md -xls example.xls
exceltk.exe -t md -xls example.xls -sheet sheetname
exceltk.exe -t md -xls example.xlsx
exceltk.exe -t md -xls example.xlsx -sheet sheetname

2017-11.2
在开发板上运行
/mnt/flash/rtspd
会有输出:
/mnt/mtd # ./rtspd
  Usage:
  Multiple streams:
    #./rtspd
  Max single h264 stream:
    #./rtspd -s
  Max single mpeg4 stream:
    #./rtspd -m
  Max single mjpeg stream:
    #./rtspd -j
Error! Abnormal AP exit under chipid(0),cpuid(1),graph(1),query_id=0x10001

##### Apply #4 #####

##### Apply #5 #####
GM RTSP Library [build - Oct  2 2014 15:03:35]
Connect command:
    rtsp://192.168.19.55/live/ch00_0
    rtsp://192.168.19.55/live/ch00_1
    rtsp://192.168.19.55/live/ch00_2
Press 'q' to exit.
/live/ch00_0: cap0_0   320x240 H264  31.44fps 315kbps
/live/ch00_1: cap0_0   640x480 H264  31.24fps 2213kbps
/live/ch00_2: cap0_3 1920x1080 H264  31.24fps 5328kbps

然后在ubuntu video中open locatin:
rtsp://192.168.19.55/live/ch00_0
就可以看见视频了.

在windows上的vlc也可以.

在当前的板子里面有个rtspd20这个程序, 运行它,
rtsp://192.168.19.175/live/ch00_0
通过无线方式看, 还是存在丢帧的情况, 屏幕可能存在花屏的情况.应该是有中间帧丢掉了.

感觉ubuntu上的video这个程序, 会停止播放, 上次播放了3分钟. widnows下面的vlc播放器, 貌似可以坚持的比较久.那么在ubuntu下面vlc播放器看看吧. vlc播放器看起来好很多, 播放了1小时50分钟.

在使用录制的功能过程中, vlc居然挂掉了. 也太容易挂了吧.

为啥参考板上会不断报错? 算了先不管吧.

30帧确实会出现闪烁的确情况.

开发板上有跳针选择spi flash的3/4字节模式.

即使在alc中设置 rtsp-tcp方式, 从抓包来看, 还是udp的包. 是不是不支持?
rtsp 是控制协议

郑达: 有一块p53使用联通2g的情况下拨号就复位, 和板子相关, 换模块也一样. 其他两块板子正常.
刘永辉: 只有一块板, 使用开关电源, 使用2a的电源也是一样的. 使用开关电源看电流并没有发现电流变大的情况.

感觉这个atom编辑大文件的时候输入有些延时,那么还是把日志先分为月文件, 后面再合并吧.
atom的多光标还是有些麻烦, 要一个一个去点.
可以用shift+alt+up/down进行, 还不错, 就是好多地方没有对齐就不好用.
把一些文档整理成md表格其实也比较费时间.

0keeper这个ap在4:30到5点左右的时间里面断掉了20分钟左右. 然后自己恢复了. 为什么会这样?

吴曦:
m60仍然存在写文件会错误的情况. 还是要想办法通过实验的方式模拟出来.
p25会出一个大的版本来, 用户又希望这两天有个新版本.

2017-11.1
atom在安装了.net 4.6上的机器上直接安装不了啊, 只有删除4.6, atom就开始安装4.0(4.5?)了.

p53:
libz.a /usr/include 可以删除.
libcrypto.so非常大, 2163668 而在openwrt_ath中, 1392196,
考虑去掉tzupdate
其他库也非常大:
          p53    openwrt_ath
liburl   359564   162668
libgmp   507448   432116
libssl   521364   316424

任银善：问为什么acl设置中使用input output规则无效，这个确实会让人迷惑。

郑达：在写udp网管的时候，建立了一个简单的取数据的机制，从什么文件中读取，上送的json字段名称， 读取方式， 读取内容。

郑荣俊: 正在建立mtk的仓, 做自定义的升级网页. 抱怨点在出一个m60, p25, p21的程序就要测试一遍tr069.

江健: 想在服务端建立udp的语言缓存.




2017-10.31
姚国梁: upnp开始连自己的计算机, 没有规则出现, 移到汪光华那里, 出现了, 回来自己的计算机, 也好了.

江健: 后面的工作还有双向语音, 奥远驱动, p2p代码.

gm8136存在pin指定从spi还是nand启动.

ubuntu下升级flash
选择tar方式,解压文件
sudo cp ~/111/libflashplayer.so ./usr/lib/flashplugin-installer/libflashplayer.so
sudo cp ~/111/usr/* /usr
还需要重新启动firefox, 这样就不会报flash过期了.

已经处理的地址:
211.143.218.108 - 126 已经处理, 118不存在.
211.143.218.35 211.143.218.54已经处理.
福建的登录信息:
远程桌面登陆地址:211.143.218.55,
账号:administrator
密码:Yrf2017!a
网管服务器登陆:211.143.218.55:8000
账号:admin
密码:ND_HSWXKD
ap-si的网页登录密码 NDHSWXKD


2017-10.30
刘云 周湘理: ap客户端不用处理repeator的情况.

运行rtspd20 , 结果重启了.
Usage:
  Multiple H.264 streams (1080p + VGA):
    #./rtspd
  Single H.264 stream (max resolution):
    #./rtspd -s
Error! Abnormal AP exit under graphid=0x1
Error! Abnormal AP exit under graphid=0x2
Error! Abnormal AP exit under graphid=0x3
Poll timeout!!Poll timeout!!GM RTSP Library [build - Oct  2 2014 15:03:35]
Connect command:
    rtsp://104.191.138.126/live/ch00_0
    rtsp://0.0.0.0/live/ch00_1
Press 'q' to exit.
Connection closed by foreign host.

向杰重新安装了机器,生成了新的key.
刘云: 还需要周湘理分析一些网页的问题.
姚国梁: 陶嵩问一拖多的时候如何下载校准文件, 想起来有些困难啊.

金晶: 一个阳光万峰的项目, 是连接若干个传感器, 不同车间显示本车间的传感器, 还有一个总的显示, 取代巡检的功能. 问陈良是否有空.

任银善: wpa2的补丁似乎还没有.
netcwmp软件已经移植, 但是感觉以前的软件做的有些乱, 好多东西揉在了一起. 本周预计完成可以进行portal的配置.
wifidog已经可以使用, 验证过的手机能上网, 没有验证的出现portal页面, 但是感觉有些奇怪的是, 删除了相应的iptables规则,验证的手机仍然可以上网. 重新启动wifidog后, 规则又加入了, 没有找到wifidog保存白名单的地方.
郑达开始做tr069.
赵钢因为在做watchdog, 还没有在做.
现在测试出来的问题主要集中在wifi做客户端的时候, 有时候不能保存, 有时候保存错误. 其他网络做wan的时候, p59的显示看起来是正常的,但p53可能错误.
性能方面, 李建华测试说在p59距离上比p21要差. 吞吐量ok, 另外做客户端的情况下, 不能增加nob这个选项, 否则很多ap都连不上.
华润方面, 在做一个简单的命令行接口. mpls, 移动的已经过了测试期, 不能测了. 电信的没有测试线路, 也没法测. snmp只提供了private等设置, 没有要求mib等.


2017-10.27
当前我的串口线,白线是地线.
连接后uboot可以显示一点内容,然后就全部是乱码了.

2017-10.23
17：11:43

2017-10.20
rm ChinaMobile -rf
killall ChinaMobile
wget ftp://192.168.1.103/ChinaMobile
chmod +x ChinaMobile
date
./ChinaMobile


gpio是: 1 20-21

echo rm ChinaMobile -rf >> 1
echo killall ChinaMobile >> 1
echo wget ftp://192.168.99.100/ChinaMobile >> 1
echo chmod +x ChinaMobile >> 1
echo date >> 1
echo ./ChinaMobile >> 1
chmod +x 1

换宾馆
ID	客户端名	MAC地址	IP地址	有效时间
1	Mike-iPhone	64-B0-A6-CE-B1-EE	192.168.99.100	01:26:30
2	android-3738671a589436c	7C-70-BC-00-08-19	192.168.99.101	01:21:30
3	GJSROX0FSVCLWJ8	2C-6E-85-2D-18-74	192.168.99.102	01:22:12
4	Liangde-iPhone	FC-E9-98-14-58-1F	192.168.99.103	01:59:49
5	SmartHome-ZLT-CM11-001	EC-3D-FD-BD-90-61	192.168.99.104	01:41:19
6	MacBook-Pro	78-31-C1-C0-C5-8E	192.168.99.105	01:37:41
7	android-dc2d0b43308d7f5b	F4-E3-FB-BB-A9-1D	192.168.99.106	01:32:42
8	SmartHome-BRUBADSRTGG6ZZXU111A	00-6C-FD-82-22-0D	192.168.99.107	01:49:08
9	ubuntu	08-00-27-C2-BC-E1	192.168.99.108	01:44:1



权重	时间	问题描述	解决情况	负责人	补充
重	2017.10.17	不规律断开服务器连接，卡顿	Pending	简亮
重	2017.10.17	视频达到25帧	已解决	黎汝祥
重	2017.10.17	关闭移动侦测，关闭声音侦测依然有。	已解决	梁剑
重	2017.10.17	移动侦测区域布防设置无效	Pending	黎汝祥
较重	2017.10.17	自动获得MAC地址及手动写入IMEI号	已解决	梁剑
较重	2017.10.17	WifiTool连接无密码SSID无法完成	已解决	简亮
重	2017.10.17	声音有背景噪音	已解决	黎汝祥
轻	2017.10.17	仅第一次提示连接成功，其余断线不提示语音。	已解决 简亮
轻	2017.10.17	SD卡插入加载生效时间较长（约10秒）	Pending	黎汝祥
轻	2017.10.18	没有IMEI号直接启动提示（文件名修正：IEMI）	Pending
轻	2017.10.19	正在连接路由器语音报半截共两次	Pending
轻	2017.10.19	下发语音再次卡顿	已解决	简亮
轻	2017.10.19	增加恢复默认参数语音提醒	已解决	简亮
轻	2017.10.19	测试说明文件	已解决	江健
轻	2017.10.19	第一张抓图有绿色线，且尺寸很小	已解决	简亮
轻	2017.10.19	收到配置信息偶现程序不往下跑	Pending
以下为平台建议
轻	2017.10.19	了解断网续传时间条刷新机制	Pending
较重	2017.10.19	流量优化15分钟静态，5分钟动态。50M流量得8分	Pending	画质跟码率的折中点
轻	2017.10.19	核实下丢帧策略（P帧发送失败，则主动丢弃后面整个GOP）	Pending		个人理解：有利于缩减延时以及保持时间戳跟平台同步
轻	2017.10.19	音频帧检查是否发送了音频格式类型	Pending
较重	2017.10.19	检查缓存了多少帧，建议100帧为佳（也有50帧的）	Pending
轻	2017.10.19	缓存策略（队列后打包，目前是打包后队列）	Pending
较重	2017.10.19	保持长时间运行，需要保证RTP时间戳的增量和系统时间的增量是匹配的	Pending		这个怎么理解？
轻	2017.10.19	每次发送应该先发视频I桢再发音频	Pending
重	2017.10.19	麦克风静音时，发送声音进程不能停止，仅发送静音数据	Pending
重	2017.10.19	事件要通知到手机通知栏（同时通知OPENAPI）	Pending
较重	2017.10.19	切换视频流时，Rtp时间戳要重取，重新步增（平台分文件存储）	Pending
重	2017.10.19	全双工能力集可以打开，平台要求全双工	Pending
较重	2017.10.19	语音提示要严格按照平台要求做	Pending
较重	2017.10.19	指示灯指示和颜色要严格按照平台要求做	Pending
轻	2017.10.19	按键偶尔引起掉线	Pending
轻	2017.10.19	Wi-Fi模组性能是否可能影响了发送性能，造成断线	Pending
重	2017.10.19	客流统计算法（线性和非线性，平台采用的是矩形非线性）	Pending		矩形结合线性
轻	2017.10.19	音频下发，建议存文件后再播放	Pending
较重	2017.10.19	明早安排寄出双向语音版本机器	Pending
重	2017.10.20	机器断线后，机器缩略图不会自动刷新。	Pending
重	2017.10.20	打开关闭摄像头，实时视频未能恢复，未收到打开消息	Pending
较重	2017.10.20	更换6灯板参加测试，寄6灯灯板	Pending
重	2017.10.20	机器断线后，机器缩略图不会自动刷新。	Pending
轻	2017.10.20	恢复默认参数时间太短	Pending
重	2017.10.20	声音告警不起作用	Pending
轻	2017.10.20	图像瞬间加速	Pending
较重	2017.10.20	发送离线及断线日志	Pending




2017-10.19
序号	中文	英文	文件名
1	正在连接无线路由器。	Y Fi Connecting.	NetInitting
2	无线网络断开。	Y Fi Disconnected.	Disconnected
3	连接无线网络失败。	Connecting Y Fi failed.	DontConnect
4	连接无线网络成功,信号很好。	Connecting Y Fi successfully, signal is excellent.	ConnectedOK_VeryGood
5	连接无线网络成功,信号好。	Connecting Y Fi successfully, signal is good.	ConnectedOK_Good
6	连接无线网络成功,信号一般。	Connecting Y Fi successfully, signal is normal.	Connected_Ordinary
7	连接无线网络成功,信号差。	Connecting Y Fi successfully, signal is poor.	Connected_Poor
8	连接无线网络成功,信号很差。	Connecting Y Fi successfully, signal is very poor.	Connected_VeryPoor
9	请用手机客户端连接设备。	Please use your mobile to connect the device.	ConnectAP
11	设备正在恢复默认参数，请等待。	Device resotring to factory default, please wait.	FactoryCfg
12	云设备升级中。	Device's upgrading, please keep the power on.	update
13	初始化无线AP模式。	Initializing Y Fi AP mode.	InitAPmode
16	无线网络设置失败，请重新设置。	Y Fi setting incorrect, please retry.	ConfigFault
17	无线网络设置成功 	Configure Y Fi successfully.	NetConfigOK
18	收到设置无线网络设置参数，正在连接无线路由器，请等待。		ObtainNetConfigParam




2017-10.18
重庆宾馆：
git remote add tozed ssh://git@113.98.195.201:10003/gm8136s

echo rm ChinaMobile -rf >> 1
echo killall ChinaMobile >> 1
echo wget ftp://192.168.43.66/ChinaMobile >> 1
echo chmod +x ChinaMobile >> 1
echo date >> 1
echo ./ChinaMobile >> 1
chmod +x 1

ubuntu 192.168.43.155
smart-home 192.168.43.165
pc: 192.168.43.66

查看局域网内机器：nmap -sP 192.168.1.0/24

error while loading shared libraries: libmpfr.so.1: cannot open shared object
file: No such file or directory
解决方法：
$ sudo apt-get install libmpfr4:i386


2017-10.15
这样可以做的tcpdump循环抓包.
/tmp/tcpdump -w /tmp/tcpdump_log.cap -i br0 -C 20M -Z root -W 1


FactoryDefault

tftp -g 192.168.19.199 -l iperf3
tftp -g 192.168.19.199 -l libiperf.so.0.0.0
chmod +x iperf3
ln -sf libiperf.so.0.0.0 libiperf.so.0.0
ln -sf libiperf.so.0.0.0 libiperf.so.0
export LD_LIBRARY_PATH=/root


net.core.wmem_max=12582912
net.core.rmem_max=12582912
net.ipv4.tcp_rmem= 10240 87380 12582912
net.ipv4.tcp_wmem= 10240 87380 12582912
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_sack = 1
net.ipv4.tcp_no_metrics_save = 1
net.core.netdev_max_backlog = 5000

2017-10.13
各个仓编译错误：
sequans3220: 真悲催，编译失败！
lc1860: 修改了啥？出错了吧。
zte7520_ap: 不如意事常八九，可与语人无二三。
ath9.5: 路漫漫其修远兮....
gm8136s: 举杯邀明月, 对影成三人...
yaoyuan_phone: 江东子弟多才俊，卷土重来未可知。

2017-9.29

rm ChinaMobile -rf
killall ChinaMobile
wget http://192.168.19.199/ChinaMobile
chmod +x ChinaMobile
date
./ChinaMobile

cp ChinaMobile /usr/share/nginx/html

gm8136s 如果使用wget那么速度还是比较快的, 一般在2秒左右.
但昨天使用nfs好像还是慢得很.
使用tftp就要1分多钟的时间穿一个文件.
nginx的文件可以放在/usr/share/nginx/html目录中, 就可以使用wget进行下载了.

2017-9.28
ATH_SUPPORT_TX99=1

2017-9.23
看起来没有的wfi选项:
ATH_SUPPORT_ICM=1
IEEE80211_MCAST_ENHANCEMENT=1
ATH_TXQ_BH_LOCK=1

2017-9.20
这个脚本分裂文本:
#!/bin/bash
arr=$(cat $1)
echo 111111111111111 > $2
for s in ${arr[@]}
do
    echo "$s" >> $2
done


2017-9.18
编译3.18.23的内核居然要使用到bc这个计算器工具
http://blog.csdn.net/wulantian/article/details/11976511
这里有个使用指南:
http://www.cnblogs.com/lovevivi/p/4359296.html
好像好复杂的样子.

2017-9.17
ATH_SUPPORT_DYNAMIC_VENDOR_IE
DBDC_REPEATER_SUPPORT UMAC_SUPPORT_TXDATAPATH_NODESTATS AH_PRIVATE_DIAG
QCA_OL_NAPI_SUPPORT
ATH_SSID_STEERING
ATH_SUPPORT_FIPS
PEER_FLOW_CONTROL
ATH_SUPPORT_GREEN_AP
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4548      2428  65% /

这个脚本可以删除scritps中的东西, 并且自动提交.
if [ "$1" == "" ] ; then
        echo what you want del?
        exit
fi
git rm scripts/$1 -r
git rm ../rootfs/$1 -r
git rm ../apps/busybox-1.01/defconfig-$1
git commit -m "byebye $1, whick want gcc-3.4.4"


2017-9.16
为什么做了buidall.sh clean之后,  ap-cp的driver编译还是报错了, 看来这个脚本出现问题了?
感觉是换了版型后, 出现的问题. 应该是

2017-9.15
ap-cp中继续砍砍砍:ATH_SUPPORT_11N_CHANWIDTH_SWITCH MESH_MODE_SUPPORT DBG_LVL_MAC_FILTERING UMAC_SUPPORT_VI_DBG QCA_OL_VLAN_WAR

ath9.5里面的scripts大部分是无法编译的, 先每天删除一个使用gcc-3.4.4的吧.
ap101-2.6.31              ok
ap101-small               make: *** [toolchain_build] Error 2
ap111-2.6.31              ok
ap111-2.6.31-clean        make: *** [art_mod] Error 127
ap113                     ok
ap120                     make: *** [uboot_mainline] Error 2
ap121-2.6.31              make: *** [sqlzma_build] Error 2
ap121-2.6.31-2MB          make: *** [sqlzma_build] Error 2
ap91-2MB                  make: *** [toolchain_build] Error 2
ap91-2x8                  make: *** [sqlzma_build] Error 2
ap91-small                make: *** [toolchain_build] Error 2
ap93-small                make: *** [toolchain_build] Error 2
ap96-small                make: *** [toolchain_build] Error 2
ap99-2.6.31               ok
ap99-small                make: *** [toolchain_build] Error 2
board953x                 make: *** [kernel_build] Error 2
board955x                 make: *** [kernel_build] Error 2
board955x-offload-host    make: *** [config_fix] Error 1
board955x-offload-target  make: *** [config_fix] Error 1
CaviumFus                 make: *** [wpa2] Error 2
db12x                     ok
db12x-aow                 make: *** [athr-wpa_supplicant] Error 1
db12x-carrier             ok
db12x-db12x-master        make: *** [athlogger_build] Error 2
db12x-enterprise          ok
db12x-extender            make: *** No rule to make target 'uboot_build', needed by 'common_mainline'.  Stop.
db12x-hybrid              Makefile:123: *** "Must specify TOOLCHAIN value".  Stop.
db12x-offload-gmac        make: *** [driver_build] Error 2
db12x-offload-gmac-flash  make: *** [driver_build] Error 2
db12x-offload-pcie-flash  make: *** [driver_build] Error 2
dhp1565                   cp: cannot stat '../rootfs/dhp1565/*': No such file or directory
ika-vox180                scripts/ika-vox180/config.ika-vox180:2: *** "You have to define BSP_VERSION to use this Makefile. 0:BSP 5.8 1:BSP 6.0 2:BSP 6.1 3:BSP 8.0 4:BSP 8.1&8.2&8.3" .  Stop.
pb44-carrier              make: *** [toolchain_build] Error 2
pb44-ce                   cd: can't cd to /home/jian/work/ath9.5/build/../linux/kernels/mips-linux-2.6.15/
pb44-clean                make: *** [toolchain_build] Error 2
pb44-p2p-small            make: *** [toolchain_build] Error 2
pb44-small                make: *** [toolchain_build] Error 2
pb44-usb-p2p-small        can't cd to /home/jian/work/ath9.5/build/../linux/kernels/mips-linux-2.6.15/
pb44-usb-small            make: *** [toolchain_build] Error 2
pb47-xmii                 make: *** [config_fix] Error 1
pb47-xmii-2.6.31          make: *** [kernel_build] Error 2
pb90                      make: *** [toolchain_build] Error 2
pb92                      make: *** No rule to make target 'uboot_build', needed by 'common_mainline'.
pb9x                      make: *** [toolchain_build] Error 2
pb9x-2.6.31               ok
pb9x-aow                  make: *** [toolchain_build] Error 2
pb9x-carrier              make: *** [driver_build] Error 2
pb9x-ce                   make: *** [toolchain_build] Error 2
pb9x-clean                make: *** [driver_build] Error 2
pb9x-offload-gmac-flash   make: *** [acfg_build] Error 2
pb9x-offload-pcie-flash   make: *** [acfg_build] Error 2
pb9x-offload-ub124        make: *** [wpa2] Error 2
pb9x-sta                  make: *** [athr-wpa_supplicant] Error 1
ub124-offload             make: *** [driver_build] Error 2
x86-usb                   make: *** [fusion_hal_build] Error 2

2017-9.16
去掉AH_SUPPORT_WASP=1, 系统启动到这里停止了.
Created ath0 mode ap for 0keeper
wifi0     no wireless extensions.
lo        no wireless extensions.
br0       no wireless extensions.
eth0      no wireless extensions.

2017-9.14
鼎桥工业路由器电话会议:
1 貌似没有通过网络抓log的模式. 需要做硬开关.
2 GE应该不是强制要求.

去掉ATH_SUPPORT_CAL_REUSE, 非常微弱的少了一点点.

占永平
只有p28某个版本后才存在url过滤后网页变慢的现象.

iperf如果采用udp方式, 如果没有加上-b参数指定带宽, 那么速度只有1Mb

2017-9.13
摄像头那个编译器运行报错, 要安装这个:
sudo apt-get install libmpfr4:i386

好像已经很难把qca-wifi-10.4的option减少了, 都是一大堆的编译错误.

郑达
在内核中增加32m支持还非常复杂, 3.15以后的内核修改了mtd接口, 修改非常大. 而只有3.15后的内核才有人打增加nor flash到32m的补丁.

任银善
修改了cfg -e的问题, 但是ipsec放在启动脚本中, 也是不正常的.

2017-9.12
江健
一些基本的摄像头概念:
mipi 这个是sense 和mpu的接口, 还有并行 parallel, sub-LVDS
WDR 宽动态范围.
FHD 全高清输出.
3D de-intenlace 隔行扫描
isp image signal processor.
video scalier 缩放

硬件上主要组成:
镜头: 指标有焦距, 口径, 定焦变焦
传感器 sense,
光敏 感应环境亮度, 可读, 是个adc
红外led灯 6-10m 图像改变为黑白.
白光灯 补光

存储:
tf卡
nvr: 网络存储 rtsp 国际标准
     onvif
云存储: hls 苹果的标准
       rtmp adobe的标准

音频 speaker+mic
双向语音: 半双工, 全双工. 回声消除, 背景噪音, 电路声.

摄像头:
长按5秒恢复出厂的状态. ssid以smart开头, 密码是6个9.

刘汉琴
赵金加班在玩魔方.问上报是否有效的. 李总让她了解企业亏损是否对情绪有影响.

李柱栋
fon那里主要是两个问题, 一个是热点, 一个是控制. 控制使用的tr069, 但fon还没有服务器进行测试. 热点方面还有

苗立双将开始联芯提供一个8905的cpe, 但还没有多少资料.

2017-9.11
AH_SUPPORT_AR5416
ATH_SUPPORT_WIFIPOS
UMAC_SUPPORT_WIFIPOS_LEANCC
ATH_SUPPORT_HYFI_ENHANCEMENTS
ATH_SUPPORT_DSCP_OVERRIDE
UNIFIED_SMARTANTENNA
ATH_BAND_STEERING
ATH_TX_OVERFLOW_IND
ATH_SUPPORT_WIFIPOS_ONE_VAP
WMI_RECORDING
ATH_SUPPORT_LOWI

洛晓峰
有个客户只要工业路由器的pppoe功能.

江健:
卡片机和摇头机主要给海外, 需要对视频数据进行加密.

叶京平
欧洲那个车载的对方已经找了一个有现成软件的, 还有欧洲认证的广州公司. 报价也低很多, 只报了100多美金, 我们报了300多.

赵金
没有明白怎么样一个pc访问多个m60.

摄像头监听了这些端口:
Discovered open port 80/tcp on 192.168.19.175
Discovered open port 7001/tcp on 192.168.19.175
Discovered open port 7070/tcp on 192.168.19.175
Discovered open port 8011/tcp on 192.168.19.175

AH_SUPPORT_KITE_x 这几个参数看起来也是在5416内部, 或者是2133内部. 从makefile.inc的结构来看, 必须有AH_SUPPORT_KITE_10或者AH_SUPPORT_KITE_12为1才会把这个any设置, 所以那个any是没有意义的.
AH_SUPPORT_EEPROM_AR9287这个参数貌似在5416内部, 既然去掉AH_SUPPORT_AR5416支持, 那么大小应该不会改变吧. 确实是这样的.

去掉ATH_SUPPORT_WRAP, 有很多的错误啊.

ATH_TX_OVERFLOW_IND=0 没有什么变化:
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4704      2272  67% /

ATH_BAND_STEERING=0
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4704      2272  67% /

WMI_INTERFACE_EVENT_LOGGING这个东西在qca-wifi-10.4目录中找不到.

WMI_RECORDING=0
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4724      2252  68% /
感觉没有变化

ap-cp中设置ATH_SUPPORT_LOWI=0, 再次减少一点点: 没有减少之前是4732
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4724      2252  68% /
默认情况REMOVE_INIT_DEBUG_CODE这个值看起来就是1, 可以不用管它. 按照文档中, 可以忽略这些功能, 现在, UMAC_SUPPORT_ACFG, AH_SUPPORT_AR5416 ATH_SUPPORT_WIFIPOS  ATH_SUPPORT_LOWI ATH_SUPPORT_DSCP_OVERRIDE已经去掉了,剩下的放在文档最前面吧. REMOVE_INIT_DEBUG_CODE默认就是1.
      the following features not only increase the Host Driver package size, but also need user space utility to provide the
      support.
      AH_SUPPORT_AR5416=0
      ATH_SUPPORT_SPECTRAL=0
      ATH_SUPPORT_WIFIPOS=0
      UMAC_SUPPORT_WIFIPOS_LEANCC=0
      ATH_SUPPORT_HYFI_ENHANCEMENTS=0
      ATH_SUPPORT_WRAP=0
      UNIFIED_SMARTANTENNA=0
      UMAC_SUPPORT_ACFG=0
      QCA_AIRTIME_FAIRNESS=0
      ATH_BAND_STEERING=0
      ATH_TX_OVERFLOW_IND=0
      ACFG_NETLINK_TX=0
      ACFG_MON_FILTER=0
      WMI_RECORDING=0
      REMOVE_INIT_DEBUG_CODE=1
      ATH_RXBUF=256
      ATH_SUPPORT_LOWI=0
      WMI_INTERFACE_EVENT_LOGGING=0


复制黎汝祥的虚拟机, 会出现这样的提示:
This virtual machine's snapshot is expecting graphics features that VMware is unable to provide on this host. Restoring the VM might be possible, but could cause serious problems if the guest OS is relying on any of the missing features.
先continue吧. 还有告警:
VMware Player is unable to provide all of the graphics features expected by this VM. The graphics hardware, graphics drivers, or version of VMware software might have changed since this VM was booted. The VM will continue running but some graphics operations might behave unpredictably until the VM is shut down.
然后是黑屏.重启看看吧.
总是提示要安装什么vmware tools for linux version 10.1.6, 那么先安装一个吧.
进去了, 进去了.

这个是黎汝祥写的readme, 貌似太简单了一点:
    1：ubuntu:
      user:root
      password:1234

    2：和目云与onenet平台应用：ChinaMobile
    /usr/src/lrxPrj/APP-ChinaMobile/OpenAPUPD-rtmp
     make 得到ChinaMobile
      其中:1)onnet代码目录:rtmppp
          ont_mqtt_sample_main.c
          rtspmain()
           2)和目代码目录:soure
          main.cpp
    3:卡片机固件打包:
     /root/share/image/target/SmartBell/TZK61-ChinaMobile
      运行：SmartHome136.sh 得到固件Smarttzk61.bin

    4:设备系统命令升级: sysupdate -d -f Smarttzk61.bin


王伍:
赵金正在做m60一拖n的生产工具,这个是袁阳提出的需要, 需要有个计划, 不能做得没有边.
想着用anychat来完成摄像头部分的视频通话工作. 江键的邮件回复:看了下，LINUX平台没有ARM的SDK，在摄像机端无法使用。价格授权好黑。一台服务器下来60几万。

陈玉告诉王伍: dialog的m60天线反馈不好, 在没有信号的地方, 换用华为的cpe, 就能用. 影响了销量. 下一批货推迟一个月.

今天的tftp又不能用了,为什么有时候可以,有时候不可以?
sudo service tftpd-hpa restart


2017-9.3
onenet密码: keeper90

郑达
p53重启测试: 3台测试了 2-3天. 1台测试了6-7天. 无异常.
升级: 1台机器40多小时, 上报就升级, 无异常.

libnetlink.h No such file or directory这个是怎么解的?忘记了.
冲掉
mkfs.jffs2没有增加lzma之前
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 6.8M      5.6M      1.3M  82% /
增加之后
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 6.8M      4.8M      2.0M  70% /


2017-9.1
#!/bin/bash
a="one,two,three,four"
#要将$a分割开，可以这样：
OLD_IFS="$IFS"
IFS=","
arr=($a)
IFS="$OLD_IFS"
for s in ${arr[@]}
do
    echo "$s"
done

2017-8.31
set ipaddr 10.8.0.33 && set serverip 10.8.0.100
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=jffs2 rw init=/sbin/init mtdparts=spi0.0:64k(u-boot),6720k(rootfs),1280k(uImage),64k(mib0),64k(ART) machtype=DB120"

set ipaddr 10.8.0.33 && set serverip 10.8.0.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6a0000 +$filesize&&cp.b $fileaddr 0x9f6a0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-jffs2 && erase 0x9f010000 +0x690000&&cp.b $fileaddr 0x9f010000 $filesize
bootm 0x9f6a0000


   insmod $MODULE_PATH/adf.ko
    insmod $MODULE_PATH/asf.ko
    insmod $MODULE_PATH/ath_hal.ko
    insmod $MODULE_PATH/ath_spectral.ko $SPECTRAL_ARGS
    if [ "${AP_NO_A_BAND}" != "1" ]; then
        echo AP_NO_A_BAND=${AP_NO_A_BAND}
        #load DFS if A band is supported,default is supported and set AP_NO_A_BAND=1 if not supported
        insmod $MODULE_PATH/ath_dfs.ko $DFS_ARGS
    fi
    insmod $MODULE_PATH/hst_tx99.ko
    insmod $MODULE_PATH/mem_manager.ko
    insmod $MODULE_PATH/umac.ko
    insmod $MODULE_PATH/ath_rate_atheros.ko
    insmod $MODULE_PATH/ath_dev.ko
    insmod $MODULE_PATH/ath_pktlog.ko
    insmod $MODULE_PATH/qca_da.ko
    insmod  $MODULE_PATH/tm.ko


/lib/modules/3.18.23/net # /tmp/busybox depmod -n
net/ath_rate_atheros.ko: net/ath_hal.ko net/umac.ko net/adf.ko net/ath_dfs.ko net/ath_spectral.ko net/asf.ko net/mem_manager.ko
net/ag71xx.ko:
net/ath_dev.ko: net/hst_tx99.ko net/ath_rate_atheros.ko net/ath_hal.ko net/umac.ko net/adf.ko net/ath_dfs.ko net/mem_manager.ko net/ath_spectral.ko net/asf.ko
net/tm.ko: net/umac.ko net/adf.ko net/ath_dfs.ko net/ath_spectral.ko net/asf.ko net/mem_manager.ko
net/ath_pktlog.ko: net/umac.ko net/adf.ko net/ath_dfs.ko net/ath_spectral.ko net/mem_manager.ko net/asf.ko
net/ath_dfs.ko: net/asf.ko
net/mem_manager.ko:
net/ath_spectral.ko: net/asf.ko
net/ath_hal.ko:
net/asf.ko:
net/umac.ko: net/adf.ko net/ath_dfs.ko net/ath_spectral.ko net/asf.ko net/mem_manager.ko
net/adf.ko:
net/hst_tx99.ko: net/adf.ko net/ath_hal.ko


2017-8.30
看看这个文件吧:
jian@jian-OptiPlex-9020:~/work/ath9.5/build$ cat ../drivers/qca-wifi-10.4/lmac/tx99/.ath_tx99.o.cmd
这个区别巨大.

比较offload/htt/.htt_h2t.o.cmd文件看起来没有太多的不同,只有两个.
@@ -256,7 +256,7 @@ export AR5416_INT_MITIGATION=1
 export ATH_SUPPORT_GREEN_AP=1
 export ATH_SUPPORT_DYN_TX_CHAINMASK=1
 export AH_DESC_NOPACK=1
-export UMAC_SUPPORT_OPMODE_APONLY=1
+export UMAC_SUPPORT_OPMODE_APONLY=0
 export UMAC_SUPPORT_STATS_APONLY=1
 export ATH_SUPPORT_STATS_APONLY=1

@@ -375,7 +375,7 @@ export ATH_TXBUF=540

 export KBUILD_MODPOST_WARN=y
 export JUMPSTART_GPIO=16
-export ATH_SUPPORT_TIDSTUCK_WAR=1
+export ATH_SUPPORT_TIDSTUCK_WAR=0
 export ATH_SUPPORT_KEYPLUMB_WAR=1


为什么现在出现的是这样的错误:/home/jian/work/ath9.5/build/../linux/kernels/linux-3.18.23/arch/mips/include/asm/war.h:12:17: fatal error: war.h: No such file or directory?
都是config里面东西搞的,非常非常多的选项.

:set nu可以在vi中显示行号.
http://blog.csdn.net/chuanj1985/article/details/6873830

:89,102s#insmod#modprobe#
在89到102行进行替换
https://segmentfault.com/q/1010000002552573/a-1020000002552589


2017-8.29
任银善
问防火墙设置和操作.

刘云
p59貌似升级挂了. 原因是刘云的机器uboot没有升级.

王伍
工业路由器:
6台坏机器的说明.
p53的测试表格.
p53的丝印要改.
-40度,要加加热芯片
天线要防雷
不知道的概念:冷压端正, igmp代理, 后路由.

李柱栋
可以在mini-snmp中增加设置操作了.
郑荣俊没有时间来改i2c的芯片了.

吴曦
信可认为找到了写mac等失败的原因, 写mac,imei等是cp侧处理的,而写usb网卡的mac是ap测处理, 写在同一个位置,这样如果同时写,就会出现一个冲突. 但晚上去掉,还有同样的问题.

2017-8.28
C语言实现程序跳转到绝对地址0x100000处执行： ((void(*)(void))0x100000)();
http://blog.csdn.net/jipingyuan/article/details/39297409
跳转到0处，无论放在应用程序还是内核中，都是非法错。


2017-8.27
来来来，做消除吧:
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/../adf/include/os/adf_os_defer.h:101:1: note: expected 'adf_os_defer_fn_t' but argument is of type 'void * (*)(void *)'


/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm_sta.c: In function 'ieee80211_recv_fms_rsp':
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm_sta.c:331:1: warning: the frame size of 5096 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm_sta.c: In function 'ieee80211_add_tfs_resp':
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm_sta.c:447:1: warning: the frame size of 5328 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm_sta.c: In function 'ieee80211_recv_tfs_recv_notify':
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm_sta.c:481:1: warning: the frame size of 4128 bytes is larger than 1024 bytes [-Wframe-larger-than=]

/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm.c:1121:1: warning: the frame size of 4136 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm.c: In function 'wlan_wnm_set_fms':
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/wnm/ieee80211_wnm.c:1254:1: warning: the frame size of 4144 bytes is larger than 1024 bytes [-Wframe-larger-than=]
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../umac/../os/linux/src/ald_netlink.c:151:1: warning: the frame size of 3688 bytes is larger than 1024 bytes [-Wframe-larger-than=]



WARNING: /opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/ath_dev: 'bus_dma_sync_single' exported twice. Previous export was in /opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/ath_dev.ko
WARNING: /opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/ath_dev: 'bus_unmap_single' exported twice. Previous export was in /opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/ath_dev.ko
WARNING: /opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/ath_dev: 'bus_map_single' exported twice. Previous export was in /opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/ath_dev.ko

/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ratectrl/if_athrate.c:1084:46: warning: 'rix' may be used uninitialized in this function [-Wmaybe-uninitialized]
         pRc->TxRateInMbps += pRateTable->info[rix].rateKbps / 1000;
/opt/work/ath9.5/drivers/wlan_v10/os/linux/../../lmac/spectral/spectral.c:1362:1: warning: the frame size of 10120 bytes is larger than 1024 bytes [-Wframe-larger-than=]






使用3.18.23的
In file included from ./arch/mips/include/asm/page.h:15:0,
                 from /opt/work/temp/ath9.5/drivers/wlan_v10/os/linux/ath_hal/../../../include/compat.h:101,
                 from <command-line>:0:
./arch/mips/include/asm/mipsregs.h:769:33: error: unknown type name 'u16'
 static inline int mm_insn_16bit(u16 insn)
内核，4.8编译器，wlan_v10的无线驱动，好像报错也是一大堆。

这个文章要求改 mipsisa32-be-elf.inc这个文件：
https://codedump.io/share/fPhSVNKO0bjT/1/compiling-a-driver-for-mips-architecture-on-44-kernel
去掉这个system是可以去掉这个错误的，不过：
wlan_v10/os/linux/../../adf/net/linux/adf_net.c:424:38: error: macro "alloc_netdev" requires 4 arguments, but only 3 given
                           ether_setup);
                                      ^
/opt/work/temp/ath9.5/drivers/wlan_v10/os/linux/../../adf/net/linux/adf_net.c:423:14: error: 'alloc_netdev' undeclared (first use in this function)
     netdev = alloc_netdev(sizeof(struct __adf_softc), info->if_name,

按照这个文章的说明，是3.17以后的内核修改了这个函数的定义
http://rglinuxtech.com/?p=1184
Thanks to Erwin Zoer (see his comment below the earlier post for 3.17-rc1..), there is a fix available – for ~/vmware-only/netif.c
For kernel 3.17-rc3 and later, change line 152 from
dev = alloc_netdev(sizeof *netIf, deviceName, VNetNetIfSetup);
to
dev = alloc_netdev(sizeof *netIf, deviceName, NET_NAME_UNKNOWN, VNetNetIfSetup);
那样这样改看起来是不会报错的：
#if LINUX_VERSION_CODE > KERNEL_VERSION(3,17,0)
    netdev = alloc_netdev(sizeof(struct __adf_softc), info->if_name,NET_NAME_UNKNOWN,
                          ether_setup);
#else
    netdev = alloc_netdev(sizeof(struct __adf_softc), info->if_name,
                          ether_setup);
#endif

然后是这个：
error: incompatible types when assigning to type 'u_int32_t' from type 'kuid_t'
这样的问题，强制转换怎么样？
http://blog.csdn.net/CSDN5741/article/details/38637641
这样不行，变成了这样的错误：
os/linux/src/ath_netlink.c:97:30: note: in expansion of macro 'NETLINK_CREDS'
          uid = *(u_int32_t *)NETLINK_CREDS(skb)->uid;
注释掉算了，反正只是一个为了print，赋值没有其他作用。

然后变成了：
/opt/work/temp/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_dev/../../os/linux/src/if_bus.o:(___ksymtab+bus_dma_sync_single+0x0): multiple definition of `__ksymtab_bus_dma_sync_single'
直接注释掉aponly中的export，不知道有没有问题。

还有，此恨绵绵无绝期啊：
/opt/work/temp/ath9.5/drivers/wlan_v10/os/linux/../../lmac/ath_pktlog/../../os/linux/include/osdep_adf.h:188:3: error: unknown type name 'ctl_table'
 f(ctl_table *ctl, int write, void *buffer,
加一个struct解决了。

还有：
os/linux/src/if_ath_ahb.c:409:75: error: macro "alloc_netdev" requires 4 arguments, but only 3 given
     dev = alloc_netdev(sizeof(struct ath_ahb_softc), "wifi%d", ether_setup);
和上面的一样，
继续：
/osif_umac.c:6009:59: error: macro "alloc_netdev" requires 4 arguments, but only 3 given
     dev = alloc_netdev(sizeof(osif_dev), name, ether_setup);

换了：
/opt/work/temp/ath9.5/drivers/wlan_v10/os/linux/../../umac/../os/linux/src/adf_net_vlan.c:83:19: error: 'NETIF_F_HW_VLAN_TX' undeclared (first use in this function)
  dev->features |= NETIF_F_HW_VLAN_TX | NETIF_F_HW_VLAN_RX
这个宏可能已经修改了名字：
文件中drivers/net/ethernet/realtek/8139cp.c
 if (features & NETIF_F_HW_VLAN_CTAG_RX)
那么改成这样吧：
#if LINUX_VERSION_CODE > KERNEL_VERSION(3,18,0)
        dev->features |= NETIF_F_HW_VLAN_CTAG_TX | NETIF_F_HW_VLAN_CTAG_RX |
                NETIF_F_HW_VLAN_CTAG_FILTER;
#else
        dev->features |= NETIF_F_HW_VLAN_TX | NETIF_F_HW_VLAN_RX |
                NETIF_F_HW_VLAN_FILTER;
#endif

还有：
os/linux/src/osif_proxyarp.c:40:19: error: conflicting types for 'ipv6_addr_is_multicast'
 static inline int ipv6_addr_is_multicast(const struct in6_addr *addr)
应该是内核中已经存在了，加上
#if LINUX_VERSION_CODE < KERNEL_VERSION(3,18,0)
不编译就可以了。

终于编译通过了。

怎么又有问题了？
/home/jian/work/temp/ath9.5/build/../linux/kernels/linux-3.18.23/include/linux/sysfs.h:457:2: error: pointer targets in passing argument 2 of 'kernfs_find_and_get' differ in signedness [-Werror=pointer-sign
这里有同样的问题，但没有解答https://pastebin.com/gbjTKwSy
干脆让告警通过吧。

可以了，可以了。but连不上了。悲催啊。算了，不管这个分支了。从代码看，还是应该使用10.4的那个wlan驱动。


2017-8.26
[   43.230000] [<801ab2c0>] 0x801ab2c0 ffffffff801ab2c0 t mem32_serial_out
[   43.230000] [<80075794>] 0x80075794 ffffffff80075c90 T sys_syslog
[   43.230000] [<80091af0>] 0x80091af0 ffffffff800918f8 T hrtimer_interrupt
[   43.230000] [<865a8510>] 0x865a8510
[   43.230000] [<865a8548>] 0x865a8548
[   43.230000] [<865b0f70>] 0x865b0f70
[   43.230000] [<865b0000>] 0x865b0000
[   43.230000] [<8582216c>] 0x8582216c
[   43.230000] [<85871a88>] 0x85871a88
[   43.230000] [<801ab9a4>] 0x801ab9a4 ffffffff801ab9a4 t serial8250_console_putchar
[   43.230000] [<80205814>] 0x80205814 ffffffff802057c8 T dev_addr_init
[   43.230000] [<858722a8>] 0x858722a8
[   43.230000] [<801b4cac>] 0x801b4cac ffffffff801b4bf4 T driver_probe_device
[   43.230000] [<801b4e54>] 0x801b4e54 ffffffff801b4ddc t __driver_attach
[   43.230000] [<801b3298>] 0x801b3298 ffffffff801b3288 t next_device
[   43.230000] [<801b4ddc>] 0x801b4ddc ffffffff801b4ddc t __driver_attach
[   43.230000] [<801b3340>] 0x801b3340 ffffffff801b32b0 T bus_for_each_dev
[   43.230000] [<801b3138>] 0x801b3138 ffffffff801b3110 t bus_get
[   43.230000] [<801b4510>] 0x801b4510 ffffffff801b43f4 T bus_add_driver
[   43.230000] [<80094bf0>] 0x80094bf0 ffffffff80094bcc T __wake_up
[   43.230000] [<80089304>] 0x80089304 ffffffff800892d0 T queue_work_on
[   43.230000] [<801b532c>] 0x801b532c ffffffff801b5264 T driver_register
[   43.230000] [<85bff030>] 0x85bff030
[   43.230000] [<85bff000>] 0x85bff000
[   43.230000] [<80060904>] 0x80060904
[   43.230000] [<800db318>] 0x800db318
[   43.230000] [<80092db8>] 0x80092db8
[   43.230000] [<800a6290>] 0x800a6290
[   43.230000] [<800e573c>] 0x800e573c
[   43.230000] [<8006b0b0>] 0x8006b0b0
[   43.230000] [<8017a3bc>] 0x8017a3bc

2017-8.25
编译双wan的p53新程序，使用以太网做为wan，自动获得ip成功，上网成功，拔掉网线自动切换到了4g，换成了静态地址后，如果不是设置的上次获得的地址，就不能ping到192.168.19.1,能ping到其他机器。只好换成上次分配的地址，这样上网后，第一次拔网线sub，出现问题，两个路由都存在，那么check_nat那个脚本出现了问题，不知道该伪装到哪个网卡。再插上网线对了，后面没有再次出现这样的情况。

王伍
工业路由器考虑后面是加一个硬件看门狗。
要郑达做重启测试。

2017-8.24
[   20.390000] usb 1-1.2: FTDI USB Serial Device converter now attached to ttyUSB0
[   20.490000] usb 1-1.3: new high-speed USB device number 4 using ehci-platform
[   20.700000] usb 1-1.4: new high-speed USB device number 5 using ehci-platform
[   20.820000] cdc_ncm_probe : InterfaceNumber = 0
[   20.820000] USBNCM cdc_ncm_probe : usb\vid_1ab7&pid_1761&mi_00
[   20.830000] cdc_ncm_probe : InterfaceNumber = 1
[   20.830000] USBNCM cdc_ncm_probe : usb\vid_1ab7&pid_1761&mi_01
[   20.850000] option 1-1.4:1.2: GSM modem (1-port) converter detected
[   20.850000] usb 1-1.4: GSM modem (1-port) converter now attached to ttyUSB1
[   20.870000] option 1-1.4:1.3: GSM modem (1-port) converter detected
[   20.870000] usb 1-1.4: GSM modem (1-port) converter now attached to ttyUSB2
[   20.890000] option 1-1.4:1.4: GSM modem (1-port) converter detected
[   20.890000] usb 1-1.4: GSM modem (1-port) converter now attached to ttyUSB3


2017-8.23
ubuntu的wine版本应该比较老吧，装这里的看看：
https://wiki.winehq.org/Ubuntu
jian@jian-OptiPlex-9020:~/work/temp/ath9.5/build$ wine --version
wine-1.6.2
jian@jian-OptiPlex-9020:~/work/temp/ath9.5/build$ wine --version
wine-2.0.2

2017-8.22
是不是这样就解决问题了？
echo 1 > /proc/sys/net/netfilter/nf_conntrack_tcp_no_window_check

在/proc/sys/net/ipv4/conf/default，p53和p25是一样的。
/proc/sys/net/ipv4/conf/all这里也一样

桌面上这个9344的0keeper运行了38天，今天下午3点不能连接了，是不是这段时间连接的客户端超级多？

TOZED_SOFTVERSION TOZED_VERSION
 Symbol: IP_ROUTE_MULTIPATH [=y]                                                                                                │
  │ Type  : boolean
  │ Prompt: IP: equal cost multipath                                                                                               │   Defined at net/ipv4/Kconfig:84                                                                                               │   Depends on: NET [=y] && INET [=y] && IP_ADVANCED_ROUTER [=y]                                                                 │   Location:                                                                                                                    │     -> Networking support (NET [=y])                                                                                           │       -> Networking options                                                                                                    │         -> TCP/IP networking (INET [=y])                                                                                       │           -> IP: advanced router (IP_ADVANCED_ROUTER [=y])


2017-8.21
qsdk中qca/src/qca-wifi-10.4/os/linux/configs/目录中看起来是wifi的配置文件。

看起来区别也不是非常大。
~/work/ath9.5/linux/kernels/linux-3.3.8$ meld .config ~/work/zte7520_ap/linux_plat/base/linux/linux-3.4.x/.config

 Symbol: NF_NAT_SNMP_BASIC [=m]

这个CONFIG_ARCH_HIBERNATION_POSSIBLE=y看起来没有任何地方用到了。

这个TRAD_SIGNALS也不知道是什么
 Symbol: TRAD_SIGNALS [=y]                                                                                                      │
  │ Type  : boolean                                                                                                                │
  │   Selected by: 32BIT [=y] && <choice> && CPU_SUPPORTS_32BIT_KERNEL [=y] && SYS_SUPPORTS_32BIT_KERNEL [=y]

2017-8.20
CONFIG_SLUB=y改为slab，貌似也没有什么效果。

这些选项需要开么：
CONFIG_PERF_EVENTS=y
CONFIG_SLUB=y
CONFIG_TRAD_SIGNALS=y
CONFIG_ARCH_HIBERNATION_POSSIBLE=y
CONFIG_ETHERNET_PACKET_MANGLE=y
CONFIG_XFRM_IPCOMP=m
CONFIG_IP_ROUTE_MULTIPATH=y
CONFIG_NET_IPIP=m
CONFIG_ARPD=y
CONFIG_SYN_COOKIES=y
CONFIG_INET_AH=m
CONFIG_INET_IPCOMP=m
CONFIG_INET_XFRM_TUNNEL=m
CONFIG_TCP_CONG_ADVANCED=y
CONFIG_IPV6_PRIVACY=y
CONFIG_INET6_AH=m
CONFIG_INET6_XFRM_TUNNEL=m
CONFIG_NF_CONNTRACK_EVENTS=y
CONFIG_NF_CONNTRACK_SNMP=m
CONFIG_NETFILTER_XT_TARGET_CONNMARK=m
CONFIG_NETFILTER_XT_TARGET_CT=m
CONFIG_NETFILTER_XT_TARGET_NOTRACK=m
CONFIG_NETFILTER_XT_MATCH_COMMENT=m
CONFIG_NETFILTER_XT_MATCH_CONNBYTES=m
CONFIG_NETFILTER_XT_MATCH_ESP=m
CONFIG_NETFILTER_XT_MATCH_HASHLIMIT=m
CONFIG_NETFILTER_XT_MATCH_HELPER=m
CONFIG_HAVE_IDE=y
CONFIG_INPUT=y

貌似p25开了的

# CONFIG_NETFILTER_NETLINK is not set
# CONFIG_NETFILTER_NETLINK_ACCT is not set
# CONFIG_NETFILTER_NETLINK_QUEUE is not set
# CONFIG_NETFILTER_XT_MARK is not set
# CONFIG_NETFILTER_XT_TARGET_CLASSIFY is not set
# CONFIG_NETFILTER_XT_TARGET_MARK is not set
# CONFIG_NETFILTER_XT_MATCH_DSCP is not set
# CONFIG_NETFILTER_XT_MATCH_LENGTH is not set

2017-8.17
/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/../os/linux/src/if_ath_ahb.c:35:21: error: ath_pci.h: No such file or directory
/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/../os/linux/src/if_ath_ahb.c: In function 'ath_ahb_probe':
/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/../os/linux/src/if_ath_ahb.c:202: error: implicit declaration of function 'ol_ath_ahb_probe'
/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/../os/linux/src/if_ath_ahb.c: In function 'ath_ahb_remove':
/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/../os/linux/src/if_ath_ahb.c:249: error: implicit declaration of function 'ol_ath_ahb_remove'


/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/mlme/ieee80211_mgmt_sta.c: In function 'ieee80211_recv_beacon_sta':
/opt/work/ath9.5/drivers/wlan_v10.4/os/linux/../../umac/mlme/ieee80211_mgmt_sta.c:666: error: 'struct ieee80211com' has no member named 'ic_dfs_cancel_waitfor_csa_timer'

今天使用联芯模块，没有出现在win7下载网易iso下载一段时间，几秒钟，就停止的情况。
使用手机连到wifi，看微博视频貌似也是没有异常。

昨天的情况是用联芯模块，在win7下下载文件，很快就会停止，地址如下
wget http://mirrors.163.com/ubuntu-releases/17.04/ubuntu-17.04-desktop-amd64.iso
其实其他地址也差不多。

QGDW 11009-2013 电能计量封印技术规范
QGDW 11009-2013 电能计量封印技术规范_文库下载http://www.wenkuxiazai.com/doc/b2aa9c81cc175527072208dc-7.html
科陆电子RFID计量封印管理系统
http://solution.rfidworld.com.cn/2013_10/2d2ef4b90af72c28.html

2017-8.14
王伍
电话主要说工业路由器的事情，问2个新人的情况，我需要再次

2017-8.10
当前p53大小，增加了pppoe这个程序。
Filesystem           1K-blocks      Used Available Use% Mounted on
rootfs                    3904      3904         0 100% /


2017-8.9
陈良计划和总结：
菲律宾GLOBE P25项目: 升级还会出现升挂的情况,短消息会出现重复读取的情况。TR069还没有完成。

这几天的提交看起来非常多，应该出一个版本了。

早上过来的时候，桌面上的联芯模块的p53已经不能ping出去了。结果直接升级了。

编译有如下错误：
rm: cannot remove ‘nart.tar.gz’: No such file or directory

2017-8.3
http.cgi居然很容易错误：
/usr/share/p11-gcc/staging_dir/usr/bin/mips-linux-gdb --exec=/home/jian/work/ath9.5/staging/rootfs-tozedap-router_4g_industry_ap123.build/tzwww/cgi-bin/http.cgi -c core.http.cgi.9957 看不到什么。
只要刷新主页就能刷出来。


华润的邮件服务器地址 168.1.2.117
好像pptp和l2tp拨入的速度完全不同。一个正常，另外一个ping值高达几秒.

Ethernet MinSize = 512bit = 64 Byte
Ethernet MaxSize = 1518 Byte
so Ethernet IP MTU = 1518 - 18 ( 6 SRCMAC+ 6 DSTMAC+ 2 TYPE+ 4 CRC) = 1500 B
so Ethernet IP TCP MSS = 1500 - 40 ( 20 IP_HEADER + 20 TCP_HEADER) = 1460 B
so Ethernet IP UDP MTU/MRU = 1500 - 28 ( 20 IP_HEADER + 8 UDP_HEADER ) = 1472 B
so PPPoE MTU/MRU = 1500 - 8 ( 6 PPPoE_SESSION + 2 PPP_HEADER ) = 1492 B
so TCP over PPPoE MSS = 1492 ( PPPoE MTU/MRU ) - 40 ( 20 IP_HEADER + 20 TCP_HEADER) = 1452
so PPTP MTU/MRU = 1500 - 56 ( 20 IP_HEADER + 20 TCP_HEADER + 12 GRE_HEADER + 4 PPP_HEADER ) = 1444 B
so TCP over PPTP MSS = 1444 ( PPTP MTU/MRU ) - 40 ( 20 IP_HEADER + 20 TCP_HEADER) = 1404
so L2TP MTU/MRU = 1500 - 40 ( 20 IP_HEADER +8 UDP_HEADER + 8 L2TP_HEADER + 4 PPP_HEADER ) = 1460 B
so TCP over L2TP MSS = 1460 ( L2TP MTU/MRU ) - 40 ( 20 IP_HEADER + 20 TCP_HEADER) = 1420 B
so PPTP over PPPoE MTU/MRU = 1492 ( PPPoE MTU/MRU ) - 56 ( 20 IP_HEADER + 20 TCP_HEADER + 12 GRE_HEADER + 4 PPP_HEADER ) = 1436 B
so PPTP over PPTP MTU/MRU = 1444 ( PPTP MTU/MRU ) - 56 ( 20 IP_HEADER + 20 TCP_HEADER + 12 GRE_HEADER + 4 PPP_HEADER ) = 1388 B
so PPTP over L2TP MTU/MRU = 1460 ( L2TP MTU/MRU ) - 56 ( 20 IP_HEADER + 20 TCP_HEADER + 12 GRE_HEADER + 4 PPP_HEADER ) = 1404 B
so L2TP over PPPoE MTU/MRU = 1492 ( PPPoE MTU/MRU ) - 40 ( 20 IP_HEADER +8 UDP_HEADER + 8 L2TP_HEADER + 4 PPP_HEADER ) = 1452 B
so L2TP over PPTP MTU/MRU = 1444 ( PPTP MTU/MRU ) - 40 ( 20 IP_HEADER +8 UDP_HEADER + 8 L2TP_HEADER + 4 PPP_HEADER ) = 1404 B
so L2TP over L2TP MTU/MRU = 1460 ( L2TP MTU/MRU ) - 40 ( 20 IP_HEADER +8 UDP_HEADER + 8 L2TP_HEADER + 4 PPP_HEADER ) = 1420 B

p53的端口映射是不起作用的。

好像总是很多事情，然后没有时间记录，这样也不好吧。

郑达：
udpserver的基本功能有了，数据库也建了，但是由于sql server 2008没有内存表这样的东西，所以要考虑一个复杂的内存结构来实现。考虑还是在2016上直接完成。

2017-8.1
去掉recovery程序后的9341，继续测试了792次，停止响应了。

2017-7.31
去掉recovery程序后的9341，已经测试了779次，转到笔记本继续吧。


 Symbol: IP_VS_PE_SIP [=n]                                                                                                                                          │
  │ Type  : tristate                                                                                                                                                  │
  │ Prompt: SIP persistence engine                                                                                                                                     │
  │   Defined at net/netfilter/ipvs/Kconfig:274                                                                                                                        │
  │   Depends on: NET [=y] && NETFILTER [=y] && IP_VS [=n] && IP_VS_PROTO_UDP [=n] && NF_CONNTRACK_SIP [=m]                                                            │
  │   Location:                                                                                                                                                        │
  │     -> Networking support (NET [=y])                                                                                                                               │
  │       -> Networking options                                                                                                                                        │
  │         -> Network packet filtering framework (Netfilter) (NETFILTER [=y])                                                                                         │
  │           -> IP virtual server support (IP_VS [=n])

9531已经测试了2803次，加上前面的700多次，已经超过300次了。
去掉recovery程序后的9341，已经测试了494次。

2017-7.30
...............................................................................2017-07-28 19:18:50
reboot  68 times
conneting...ok
 uptime
 08:01:09 up 1 min,  load average: 0.69, 0.22, 0.07
/tmp/tools #
wait 80 sec.
...............................................................................2017-07-28 19:20:10


2017-7.28
貌似终端寄存器很多，一个一个看看：

GPIO Interrupt Mask (GPIO_INT_MASK)                      18040024 值 0
Miscellaneous Interrupt Mask (RST_MISC_INTERRUPT_MASK)   18060014 值 c
LUTs Ager Interrupt Mask (LUTS_AGER_INTR_MASK) Address:  18070008 值 f
Primary Interrupt Mask (IMR_P)                           181000A0 值 81810175
Secondary Interrupt Mask 0 (IMR_S0)                      181000A4 值 3cf
Secondary Interrupt Mask 1 (IMR_S1)                      181000A8 3cf
Secondary Interrupt Mask 3                               181000B0 0
Secondary Interrupt Mask 4 (IMR_S4)                      181000B4 0
Secondary Interrupt Mask 5 (IMR_S5)                      181000B8 0
Synchronous Interrupt Mask                               1810401C 5c
Asynchronous Interrupt Mask                              18104020 0
Asynchronous Priority Interrupt Mask                     1810408c 0
Synchronous Priority Interrupt Mask                      18104090 0
RTC Interrupt Mask                                       18107058 0
Checksum Interrupt Mask                                  18400044 0
Interrupt Mask (DMAINTRMASK)                             19000198 0
                                                         1A000198 d9


使用9531做复位动作，已经做了728次，现在增加了查看启动时间，继续做吧。


2017-7.27
p59命令升级：
tftp -g 192.168.0.50 -l tozedap-p59_ap143-squashfs
update tozedap-p59_ap143-squashfs /dev/mtd3
tftp -g 192.168.0.50 -l vmlinux_routing.lzma.uImage
flashcp tozedap-p59_ap143-squashfs /dev/mtd3
7.26
只要系统设置为中文版，编译就会出现
/mkimage: invalid entry point -n
这样的东西。

【fedora】设置中文为默认语言
安装Fedora时，界面语言是英语，手动安装简体中文语言包：
1、打开终端，执行yum install system-config-language命令来安装语言套件；
2、然后执行system-config-language
选择中文简体。
在重启后会自动设置成中文。
http://www.cnblogs.com/lizunicon/p/3509559.html
换成英文也要狂下载一堆东西么？


2017-7.24
p25的
 find -type f -print -exec cat {} \;
./ip_conntrack_buckets 	1024
./ip_conntrack_checksum 	1
./ip_conntrack_count 	6
./ip_conntrack_generic_timeout 	600
./ip_conntrack_icmp_timeout 30
./ip_conntrack_log_invalid 0
./ip_conntrack_max 7248
./ip_conntrack_tcp_be_liberal 0
./ip_conntrack_tcp_loose 1
./ip_conntrack_tcp_max_retrans 3
./ip_conntrack_tcp_timeout_close 120
./ip_conntrack_tcp_timeout_close_wait 60
./ip_conntrack_tcp_timeout_established 7200
./ip_conntrack_tcp_timeout_fin_wait 120
./ip_conntrack_tcp_timeout_last_ack 30
./ip_conntrack_tcp_timeout_max_retrans 300
./ip_conntrack_tcp_timeout_syn_recv 60
./ip_conntrack_tcp_timeout_syn_sent 120
./ip_conntrack_tcp_timeout_syn_sent2 120
./ip_conntrack_tcp_timeout_time_wait 120
./ip_conntrack_udp_timeout 120
./ip_conntrack_udp_timeout_stream 180

p53的
 find -type f -print -exec cat {} \;
./ip_conntrack_generic_timeout 600
./ip_conntrack_tcp_timeout_syn_sent 120
./ip_conntrack_tcp_timeout_syn_sent2 120
./ip_conntrack_tcp_timeout_syn_recv 60
./ip_conntrack_tcp_timeout_established 1200
./ip_conntrack_tcp_timeout_fin_wait 120
./ip_conntrack_tcp_timeout_close_wait 60
./ip_conntrack_tcp_timeout_last_ack 30
./ip_conntrack_tcp_timeout_time_wait 120
./ip_conntrack_tcp_timeout_close 10
./ip_conntrack_tcp_timeout_max_retrans 300
./ip_conntrack_tcp_loose 1
./ip_conntrack_tcp_be_liberal 0
./ip_conntrack_tcp_max_retrans 3
./ip_conntrack_udp_timeout 30
./ip_conntrack_udp_timeout_stream 180
./ip_conntrack_icmp_timeout 30
./ip_conntrack_max 8000
./ip_conntrack_count 13
./ip_conntrack_buckets 1024
./ip_conntrack_checksum 1
./ip_conntrack_log_invalid 0


p56
./ip_conntrack_buckets 1024
./ip_conntrack_checksum 0
./ip_conntrack_count 45
./ip_conntrack_generic_timeout 600
./ip_conntrack_icmp_timeout 30
./ip_conntrack_log_invalid 0
./ip_conntrack_max 1964
./ip_conntrack_tcp_be_liberal 1
./ip_conntrack_tcp_loose 1
./ip_conntrack_tcp_max_retrans 3
./ip_conntrack_tcp_timeout_close 10
./ip_conntrack_tcp_timeout_close_wait 60
./ip_conntrack_tcp_timeout_established 432000
./ip_conntrack_tcp_timeout_fin_wait 120
./ip_conntrack_tcp_timeout_last_ack 30
./ip_conntrack_tcp_timeout_max_retrans 300
./ip_conntrack_tcp_timeout_syn_recv 60
./ip_conntrack_tcp_timeout_syn_sent 120
./ip_conntrack_tcp_timeout_syn_sent2 120
./ip_conntrack_tcp_timeout_time_wait 120
./ip_conntrack_udp_timeout 30
./ip_conntrack_udp_timeout_stream 180

如下1860平台的M60和P28参数。
./ip_conntrack_buckets                  2048
./ip_conntrack_checksum               1
./ip_conntrack_count                     26（M60：164）
./ip_conntrack_generic_timeout     600
./ip_conntrack_icmp_timeout         30
./ip_conntrack_log_invalid              0
./ip_conntrack_max                       8012
./ip_conntrack_sctp_timeout_closed                      10
./ip_conntrack_sctp_timeout_cookie_echoed         3
./ip_conntrack_sctp_timeout_cookie_wait              3
./ip_conntrack_sctp_timeout_established               432000
./ip_conntrack_sctp_timeout_shutdown_ack_sent  3
./ip_conntrack_sctp_timeout_shutdown_recd         0
./ip_conntrack_sctp_timeout_shutdown_sent         0
./ip_conntrack_tcp_be_liberal                                 0
./ip_conntrack_tcp_loose                                       1
./ip_conntrack_tcp_max_retrans                            3
./ip_conntrack_tcp_timeout_close                      10
./ip_conntrack_tcp_timeout_close_wait              60
./ip_conntrack_tcp_timeout_established            432000
./ip_conntrack_tcp_timeout_fin_wait                 120
./ip_conntrack_tcp_timeout_last_ack                 30
./ip_conntrack_tcp_timeout_max_retrans          300
./ip_conntrack_tcp_timeout_syn_recv                60
./ip_conntrack_tcp_timeout_syn_sent                120
./ip_conntrack_tcp_timeout_syn_sent2              120
./ip_conntrack_tcp_timeout_time_wait              120
./ip_conntrack_udp_timeout                             30
./ip_conntrack_udp_timeout_stream                 180

2017-7.22
pptpd的程序貌似只有在这里才找到
https://sourceforge.net/projects/pptpclient/files/pptp/

2017-7.21
+l2tp拨号修正4g网络断线重连后可能无法再次拨入（梁剑）
+加上对poweon的操作，兼容联芯L1761模块（刘云）
+pptp拨号修正4g网络断线重连后可能无法再次拨入（梁剑）
+修正新的拨号程序后，tcp网管程序tzupdate不上报数据。（郑达）
+将有线中的IP地址与WIFI客户端中的IP地址分开保存在不同的配置中（向杰）
+当使用以太网客户端模式时，两个网口，左边为wan，右边为lan（梁剑）
+以太网客户端网页配置（向杰）
+增加以太网客户端模式，支持动态地址和静态地址（梁剑）
+pppd参考openwrt中的配置，删除ipx,tdb支持。（简亮）
+udp网管新程序增加上报参数（郑达）
+使用pptp 1.9.0，pptp 1.8.0太老了（任银善）


2017-7.20

./cool ap-p11_4g_router switchwan_build
./cool p10p switchwan_build


只做复位，做到340次的时候没有响应了。
/tmp/tools #
wait 80 sec.
...............................................................................reboot  340 times
conneting...ok
BusyBox v1.24.2 (2017-07-18 09:20:31 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.
/tmp/tools #
wait 80 sec.
...............................................................................reboot  341 times
conneting...[Errno 110] Connection timed out
wait 80 sec.
...............................................................................reboot  342 times
conneting...[Errno 113] No route to host
wait 80 sec.



2017-7.19
昨天的测试到了74次还是挂了。

2017-7.18
[  126.660766] Kernel panic - not syncing: ERR: send to CP skb->data% != 0
[  126.666839] [<c000d4cc>] (unwind_backtrace+0x0/0xf8) from [<c04d4a24>] (panic+0x78/0x1ac)
[  126.674987] [<c04d4a24>] (panic+0x78/0x1ac) from [<c038cf24>] (insert_toext_dbg+0x15c/0x17c)
[  126.683380] [<c038cf24>] (insert_toext_dbg+0x15c/0x17c) from [<c038d750>] (insert_toext_mem+0xc/0x18)
[  126.692596] [<c038d750>] (insert_toext_mem+0xc/0x18) from [<c02b9d2c>] (ddrnet_tx_packet+0x60/0xe0)
[  126.701629] [<c02b9d2c>] (ddrnet_tx_packet+0x60/0xe0) from [<c03716e8>] (dev_hard_start_xmit+0x3dc/0x63c)
[  126.711181] [<c03716e8>] (dev_hard_start_xmit+0x3dc/0x63c) from [<c0397008>] (sch_direct_xmit+0xa4/0x198)
[  126.720733] [<c0397008>] (sch_direct_xmit+0xa4/0x198) from [<c0371b10>] (dev_queue_xmit+0x1c8/0x518)
[  126.729858] [<c0371b10>] (dev_queue_xmit+0x1c8/0x518) from [<c03db790>] (ip_finish_output+0x138/0x2bc)
[  126.739135] [<c03db790>] (ip_finish_output+0x138/0x2bc) from [<c03dbce0>] (ip_local_out+0x28/0x2c)
[  126.748077] [<c03dbce0>] (ip_local_out+0x28/0x2c) from [<c03dbe1c>] (ip_queue_xmit+0x138/0x394)
[  126.756774] [<c03dbe1c>] (ip_queue_xmit+0x138/0x394) from [<c04ab288>] (l2tp_xmit_skb+0x2fc/0x524)
[  126.765716] [<c04ab288>] (l2tp_xmit_skb+0x2fc/0x524) from [<c04ad45c>] (pppol2tp_xmit+0x140/0x1d0)
[  126.774658] [<c04ad45c>] (pppol2tp_xmit+0x140/0x1d0) from [<c01edd14>] (ppp_channel_push+0x48/0x94)
[  126.783660] [<c01edd14>] (ppp_channel_push+0x48/0x94) from [<c01ede58>] (ppp_write+0xf8/0x138)
[  126.792266] [<c01ede58>] (ppp_write+0xf8/0x138) from [<c007e6cc>] (vfs_write+0xa0/0x144)
[  126.800354] [<c007e6cc>] (vfs_write+0xa0/0x144) from [<c007e958>] (sys_write+0x38/0x70)
[  126.808349] [<c007e958>] (sys_write+0x38/0x70) from [<c0009020>] (ret_fast_syscall+


 killall wlan-server zte_usbCfgMng hotplugnl zte_rj45

各位同事请注意，把开票资料保存好！从7月1号开始无论是普通发票还是专用发票，发票上的这些信息一条都不能少。

公司名称：深圳市通则技术股份有限公司
地址电话：深圳市福田区车公庙天安工业区天吉大厦4楼A1、A2
          0755-83583715
税    号：91440300734188444E
开户银行：建设银行深圳泰然支行
银行帐号：44201530300052506208


早上来，145次挂了，最后一次看起来是
Writing kb: 408/6848 (5%) ntpd: setting time to 2017-07-18 08:43:49.747861 (offset +1500338536.021268s)
Writing kb: 6848/6848 (100%)
Verifying kb: 6848/6848 (100%)
sysfile vice recover end
2048+0 records in
2048+0 records out
1048576 bytes (1.0MB) copied, 0.499123 seconds, 2.0MB/s
Erasing block: 16/16 (100%)
Writing kb: 1024/1024 (100%)
Verifying kb: 868/1024 (8[  123.010000] setting phy reg 180600b8 to value 0...
Verifying kb: 1024/1024 (100%)
ker vice recover end,recover vice successful
write nart flag :ff
[  242.260000] setting phy reg 180600b8 to value 0...
[  284.380000] setting phy reg 1806001c to value 0...
[  287.390000] setting phy reg 1806001c to value ffffffff...



2017-7.16
为什么我的电脑tftp不能默认启动了？
sudo service tftpd-hpa restart

即使使用mtd-util 2.0,mkfs.jffs2里面还是没有对其他压缩格式的支持。

77上面echo 1 >  /proc/sys/net/ipv4/ip_forward 居然没有开。

即使不加开机复位，p53仍然存在开发停住的情况。

Filesystem                Size      Used Available Use% Mounted on
rootfs                    3.8M      3.8M         0 100% /
rootfs                    3840      3840         0 100% /
比zlib算法少了1m。
如果是gcc-4.6编译的，就还要小一点
Filesystem           1K-blocks      Used Available Use% Mounted on
rootfs                    3776      3776         0 100% /


使用xz压缩算法后，p53的文件系统变得小到惊人：


p53上访问/mnt内部的文件
/mnt/etc # cat iptables_config
[  113.210000] JFFS2 compression type 0x06 not available.
[  113.210000] Error: jffs2_decompress returned -5



让vim记住上次编辑的位置
以下内容，保存到 ~/.vimrc 文件即可，以作备份。
" ======= 恢复上次文件打开位置 ======= "
set viminfo='10,\"100,:20,%,n~/.viminfo
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm'\"")|else|exe "norm $"|endif|endif
https://my.oschina.net/dogstar/blog/911998



2017-7.15
铜川电信的测试地址是61.134.53.2
用户： ceshi,密码123456？

现在测试了187次了，应该问题不大了，加强了300次啦。

在ubuntu16中的vi 替换指令要这样写了：:%s#us\.#cn\.#
如果点号前不加\，那么所有的us都变成了cn.

2017-7.14

p53升级了148次，停留写复位寄存器这个地方了。
在复位之前停止3秒，停电之前92次，现在继续吧。

2017-7.13
现在7520升级了139次，看起来还是正常的。
p53升级了123次，看起来还是正常的。

何文秋
看起来解决了wifi作为客户端不能存储参数的问题。

余小虎
发现一个cherry-pick，不仅仅加入了那个commit-id的东西，还增加了若干个函数，看起来我们对cherry-pick的理解有误。

任银善
使用pc2site的方式，也可以拨入tplink，可以简化测试，当然，在线监控就难一点了。

轰天炮旗舰店:娇娇 (08:24:22):
简亮   719819175170中通，发票注意查收

federo下的iptables貌似需要这样处理一下：
sudo yum install perl-Errno --best --allowerasing
sudo yum install perl-threads.x86_64 --best --allowerasing

把web_update改为update的方式，recovery这个程序仍然在112次的时候，进入了停住响应的模式。
那么不要关看门狗试试吧。
这次是死在了升级过程中的setting phy reg 1806001c to value ffffffff...
只有20次，只有20次。
那么web中直接写吧，不用转到脚本中去了。

2017-7.12
p25更加10就挂了，不断重启中。

工业路由器今天去掉lteup的重复调用，也拔掉了模块，仍然会出现write 101系统停住的问题。换一个板子来测试吧，现在没有卡，测试了78次了。

fedora 直接安装居然失败：
先更新了下vi，再装vim就好了 就是yum update vi 然后yum install vim
http://www.cnblogs.com/flyfish919/p/7152005.html

2017-7.11
直接写复位寄存器都会失败？
[  243.180000] setting phy reg 1806001c to value ffffffff...

2017-7.10
#
# AP91 -- Kernel configuration file for FreeBSD/mips for Atheros AP91 reference
#         board (AR7240)
#
# $FreeBSD$
#


Atheros Reference AP93
Clone this wiki locally

The Atheros AP93 is an AR7240 MIPS24k SoC enterprise reference design.
Overview

It has:

    AR7240 SoC, 400MHz
    64MB RAM
    16MB NOR flash
    USB 2.0 EHCI port
    on-chip 10/100 ethernet switch (LAN ports)
    10/100/1000 WAN port
    AR9280 2x2 2GHz wifi NIC



Atheros AP96 Reference board
Introduction

The Atheros AP96 is an AR7161 based, dual-AR9280 (2GHz + 5GHz) reference design.
Hardware

    AR7161, 680MHz
    64MB RAM
    8MB SPI flash
    1 x AR8316 10/100/1000BaseT ethernet switch
    2 x USB ports
    1 x AR9280 5GHz NIC
    1 x AR9283 2GHz NIC


The AP135 is a Qualcomm Atheros reference board, with:

    QCA9558 SoC (Scorpion) - 720MHz MIPS74kc; 600MHz DDR2 RAM; 3x3 2GHz 11n wifi;
    128MiB RAM;
    16MiB NOR flash (boot);
    128MiB NAND flash;
    AR8327 ethernet switch;
    QCA9880v2 3x3 11ac PCIe NIC.


Atheros PB47 Reference board
Introduction

The Atheros PB47 is an AR7161 based, single Mini-PCI+ slot reference board.
Hardware

    AR7161, 680MHz
    64MB RAM
    8MB SPI flash
    1 x AR8021 10/100/1000BaseT ethernet PHY (attached to arge1)
    1 x Akros Silicon AS1834
    2 x USB ports
    1 x Mini-PCI+ slot (see blow)
    1 x xMII slot



2017-7.7
当前的工业路由器的大小
Filesystem           1K-blocks      Used Available Use% Mounted on
rootfs                    4800      4800         0 100% /

2017-7.6
system_moniter -s /tmp/.system_protect.config

spectraltool这个进程会导致一个segmentation fail, 并导致其他登录的ifconfig 都停住不动。不知道是什么原因了。

2017-7.5
吴曦
信可的说看门狗的做法是一个单片机的核，来监控其他的几个核。发过来的cp程序包括了这个功能，所以升级cp侧程序后，就不断在重启了。

为什么把rootfs改为staging目录就有问题？
cp ../apps/pptp-1.8.0/pptp /home/jian/work/ath9.5/build/../staging/rootfs-tozedap-cp_ap123.build/usr/sbin/
cp: failed to access ‘/home/jian/work/ath9.5/build/../staging/rootfs-tozedap-cp_ap123.build/usr/sbin/’: Not a directory
前面的pppd和chat都没有报错啊。
前面的把pppd和chat复制为sbin这个文件了。
但是，没有加上staging这个文件夹的时候是对的。

2017-7.3
叶京平
问单ap的事情，认为2.4+5.8可以使用300m的带宽。

在没有开启dhcp的情况下，修改ip地址无效果。

当前ath9.5仓 2481464

姚国梁
查80端口默认没有屏蔽
电信卡选择3g还是在4g
把telnet换为ssh方式

2017-7.2
9531 openwrt上
lrwxrwxrwx    1 root     root            16 May  8  2017 dbclient -> ../sbin/dropbear
lrwxrwxrwx    1 root     root            16 May  8  2017 dropbearkey -> ../sbin/dropbear
lrwxrwxrwx    1 root     root            16 May  8  2017 scp -> ../sbin/dropbear
lrwxrwxrwx    1 root     root            16 May  8  2017 ssh -> ../sbin/dropbear
-rwxr-xr-x    1 root     root        160821 Dec  6  2016 dropbear
真的小到离谱啊。


2017-6.30
华润的早上一来就报不能使用了，

当前ath9.5仓大小
du . -s
2537636	.

2017-6.29
王伍
斯里兰卡电信还要做一个类似wifidog的东西。

向杰
越南文版本已经发出。

14:59 手上的这个p53居然串口停止响应，然后复位了。

喻潇
p53的新程序wifi灯不亮了。

李柱栋
斯里兰卡那里的tr069有多发消息，修改了代码还是有，只有先加log，在根据log来分析。
还要做wifidog这个东西。

早上华润就报不能用了。重启了一下tplink，貌似有4个在线了。
发现那个aaa账号的不会一直断线，而其他的账号在日志中总是有不断的上线消息。

2017-6.28
华润我们的地址是120.197.116.46:8100
tozed 1qazxsw2

当前卡是13602680403

刘云
如果在写文件的时候断电，非常容易出现不能启动的情况。

吴曦
cp侧升级，信可说有进展了，下午去看看。
锁运营商，锁机，锁卡等，不记得是中兴做的还是后面加的。
4g使用speedtest掉网的情况，下午去看看。
锁band，要把当前支持的band在网页上列出来。网页上采用读nv的方式，不直接发生at指令。
apn增加，王伍觉得操作流程不好。
生产，王伍要求加生产页面，其实在生产工具中有各种检查，各种绿色的pass.
生产工具：4g天线，如何读出每个天线的rssi值
重启是设置at+reset
看门狗
开机过程中拔电，看看这个ubi是否正常。

汪光华
感觉可以开始折腾l2tp了。

郑伟峰
柬埔寨的10台样机没法很快出。

王伍
ubi是andriod的标准系统， 所以理论上是没有问题的。

2017-6.27
当前ath9.5仓大小是2.5G ，目标考虑减少到1g。
jian@jian-PowerEdge-2950:~/work/ath9.5$ du . -s
2586872 .

工业路由器增加了什么东西？
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 4864      4864         0 100% /


白俊剑
正在搬家，北站那里1房1厅要到3000了。

刘汉琴
问职称的事情。

任银善
要宽翼的at指令。

喻潇
p53中的智能重启，工具的默认值和设备的默认值是不同的。

河北办 史军龙
没有对cpe 5g升级过。
说升级后也不能搜索到其他厂商的ap.

王伍
认为内核中的ubi系统可能太老了。
说让李柱栋去先折腾p25上的slic程序，如何能够支持voip, 要用7520做一个m60出来。

使用我的机器buildall一次ath9.5，大约需要40分钟吧。

有些进程看起来ctl+c不能停止，即使kill -9了，还是在ps中存在：
jian@jian-OptiPlex-9020:~/work/ath9.5/build$ ps
  PID TTY          TIME CMD
 6101 pts/0    00:00:01 bash
10228 pts/0    00:00:00 bash
10230 pts/0    00:00:00 bash
10326 pts/0    00:00:00 wget <defunct>
21462 pts/0    00:00:00 ps

嗯，这个里面貌似是我在编译的时候退出了？
jian@jian-OptiPlex-9020:~/work/ath9.5/build$ ps -l
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000  6101  6093  0  80   0 -  7840 wait   pts/0    00:00:01 bash
0 R  1000  9552  6101  0  80   0 -  4069 -      pts/0    00:00:00 ps
1 T  1000 10228  6101  0  80   0 -  7840 signal pts/0    00:00:00 bash
1 T  1000 10230 10228  0  80   0 -  7840 signal pts/0    00:00:00 bash
0 Z  1000 10326 10230  0  80   0 -     0 exit   pts/0    00:00:00 wget <defunct>
jian@jian-OptiPlex-9020:~/work/ath9.5/build$ kill -9 10228
jian@jian-OptiPlex-9020:~/work/ath9.5/build$ ps
  PID TTY          TIME CMD
 6101 pts/0    00:00:01 bash
 9901 pts/0    00:00:00 ps
[1]+  Killed                  ./buildall.sh  (wd: ~/work/temp/ath9.5/build)
(wd now: ~/work/ath9.5/build)

河北 翟福坤
河北发了10台5.8g的cpe，但是扫描不到其他公司的ap，把115版本，国家代码改成菲律宾的版本发给他试试。

鄂尔多斯移动李工
服务器已经安装，需要安装网管软件了。

何文秋
居然知道tamper，1 (未经许可擅自) 变更 [原文等] ,窜改[with]这个词。
认为p25虽然在扫描过程中会改变语言，但是扫描后就没事了。

吴曦
联通和柬埔寨的修改已经改成了配置。
升级nv还是存在问题。

金晶
定位需要这些内容：cellid, lac, mnc mcc.
谷歌提供开发的api
在江西永新的设备有奇怪的现象，使用了vlan，上端是华为的交换设备。设备会掉线，开始认为是设备问题，后来发现设备断电重开还是不能连接，连接到交换设备的那些设备在线的口，正常。关电10分钟再开，正常。其他电脑连接，正常。
测试了一下派联的软件，做压力测试非常不满意，每秒写的次数只有30个，应该达到1000个/s才合适。使用的是mysql数据库。

朱卫平
要在wifi覆盖中增加审计软件，需要任银善或赵刚支持。

openwrt里面的程序非常非常小啊。
使用里面的busybox的.config编译的文件
-rwxrwxr-x 1 jian jian 361352  6月 27 10:45 busybox*
而9531中的更小，而且vi sed之类也不缺
-rwxr-xr-x    1 root     root       292928 Jun 26 12:33 busybox

2017-6.26
向杰
明天请假。

刘汉琴
程洪卫问为什么研发一下走了多个人，把我说的顶不住压力的话说了出来。

叶京平
柬埔寨认为我们的工业路由器wifi性能很好，在别墅中比tplink的要好很多，希望我们去掉4g模块，直接出路由器产品给他们。

郑达
还没有验证pin功能是否有效果
大连奥远的来问网管的事情。

陈良
让大连的人去看tr069,建议他们用tr069

吴曦
从04升级到06版本，不升级nv，可以启动，升级nv，进入trap模式。

mini-snmp的1.4版本，比起当前仓中的版本，貌似没有改变。

何文秋：
毕业证已经拿到了。

王伍
为什么p21使用安全工具扫描之后网页不能看到了？
查找了一些ubi系统崩溃的文章。

姚国梁 何文秋
扫描之后确实网页不能打开了，是切换到了中文版本，而中文版本不对，少了个逗号，导致网页无法显示了。

汪光华 吴曦
看起来dnsmasq好像不能只分配一个ip。

2017-6.25
这样openvpn就可以编译了。
OPENVPN_DIR=../apps/openvpn/openvpn-2.3.6
openvpn_build:polarssl-1.2.19_build
        if ( test ! -e $(OPENVPN_DIR)/Makefile );then \
                cd $(OPENVPN_DIR) && ./configure  --host=mips-linux --disable-lzo --disable-plugin-auth-pam --with-crypto-library=polarssl POLARSSL_CFLAGS=-I$(TOPDIR)/apps/polarssl-1.2.19/include POLARSSL_LIBS=$(TOPDIR)/apps/polarssl-1.2.19/library/libpolarssl.a; \
        fi
        make -C  $(OPENVPN_DIR) CC=$(TOOLPATH)/bin/mips-linux-uclibc-gcc

为什么在77上cpe-ap的tozedmgr还是编译报错？

任银善：
第一家企业是做地震监测的。这样在各种地方安装个比较大的铁盒子，里面是陀螺仪监测数据，通过网络发送出去，然后通过计算及时算出结果，在地震发生时对边缘地带进行预警，能提前10多秒的样子。据说很多人都是在家门口被压住，即使只提前1s也能挽救不少。这个还需要很多的志愿者来发送消息。


2017-6.23
向杰
正在改越南文的。

汪光华
增加了ip passthrough的脚本，pc设置ip后可以上网，自动获得还有问题。

郑达
找到了输入的pin的代码，但是网页上输入pin这个功能在工业路由器上从来都是不能用的。
觉得增加一个lt10的程序自己做更快一些，可能给赵金做有些失望。

2017-6.22
吴曦
如果使用系统升级，那么升级后不能发送at指令，后面单独升级一次nv，就好了。这样，说明至少有可以用的情况。

李柱栋
中兴的无法使用便宜的slic，还是要用那颗贵的。


2017-6.21
何文秋
明天下午请假，后天毕业典礼。

任银善
昨晚有太断了，确认了一下，连不上的主要原因好像是服务器的问题，端口不能访问。昨晚0点，我重启了服务器，早晨查看都连接上了。

2017-6.20


喻潇
国内的一些联系都是直接到喻潇这里，国外的也可以先走李光达。
软件著作权和宿新艳讨论。

廖媛
问客户支持的内部流程。对于小的项目，没有明显的项目负责人的项目，会出现推责任的现象。

陈良：
p21的sn号原来是tz+0406(日期)+imei(后若干位组成)， tr069要上报sn号。估计要一直采用这个规则了。
要安排软件著作权的事情。

刘云
来要工业路由器的机器。

2017-6.19
郑达
来提加薪的事情，他的同学，一般转正是7k左右，一年左右能加2-3k。最高的那个有14k，觉得自己不比这些同学差，薪水却要低，心里比较失落。

廖媛
意大利的p10出现某些ip ping包周期性掉包的情况。貌似这样的情况不好分析。

李柱栋
p28接到m60后面，发现ping非常慢，两次间隔会到好多秒。但是p28直接连接到公司网络，ping出去没有异常，使用pc连接到m60去ping没有问题，使用busybox的正常。

刘云
bigap1总是编译不过去，还是苗立双手工改了一下。
余小虎发现恢复出厂的情况下pc可能无法得到正常的ip地址，后来王伍发出邮件，如果找不到w13断网口的地方，就不要解了。



吴曦
湖北：需要锁物理小区，汪光华处理，有at指令
	 登录后直接跳转到apn页面，完成，以后是不是考虑做到配置中去。
	 apn需要登录，这个要在本地测试。
	 band1/3 模块不够，考虑把手头上的模块当做样机发出。信可估计要到周三后才能到。
柬埔寨：叶京平已经把设备带到了现场。这些修改需要变成配置。
基本：cp侧升级。当前升级了几个区，貌似也成功了，但是读取moden的版本还没有变化。
	 感觉每次开机，nv都会改变。
     trap状态通过ap指令关闭后，出现问题机器会重启。
生产：wifi校准工具，郑伟峰认为使用这个工具灵敏度较差。
短信：存储修改，重复显示问题。
通讯录：也出现过重复显示的问题。

工业路由器免密码登录：
改成这样看起来是可以用了：
ttyS0::respawn:/bin/sh

如果改成：
::respawn:/bin/sh
那么会出现这样的提示：
/bin/sh: can't access tty; job control turned off

在inittab这个文件去掉
::respawn:/sbin/getty ttyS0 115200
加上
::askconsole:/bin/ash --login
串口不会出现任何提示。

2017-6.16
inittab改成这样，那么串口登录不了：
::respawn:/sbin/getty -l /bin/sh ttyS0 115200

iperf3的最新版本增加了ssl，还不知道如何砍掉。
感觉是iperf_auth.c这个文件导致的。

/usr/sbin/httpd -h /tzwww -c /etc/httpd.conf
cat /etc/httpd.conf
/moduleinfo.txt:module:info
这个文件什么概念？


网页的wan配置中
PIN码验证: 	已关闭
PIN操作: 	开启PIN码验证
似乎是网页去发at进行pin查询的，在sim7000c时，会出现这样的情况：
12471 root      1476 S    http.cgi
12498 root      1196 S    sh -c sendat -d/dev/ttyUSB1 -f/tmp/at_send -o/tmp/at
12502 root      1120 S    sendat -d/dev/ttyUSB1 -f/tmp/at_send -o/tmp/at_recv
12506 root      1120 S    sendat -d/dev/ttyUSB1 -f/tmp/at_send -o/tmp/at_recv
12507 root      1120 S    sendat -d/dev/ttyUSB1 -f/tmp/at_send -o/tmp/at_recv
~ # cat /tmp/at_send
AT+CPIN?
网页为什么要查cpin?貌似有些搞笑。

2017-6.15
CQ17051111
allrun1111

当前的ath0中，txbyte还是错误的，永远都是0.
recover config.tozedap-cp,and repair RX error

去掉checkmoduletype_build checkusbnet_build checksysmanagetool_build system_updater_build monitortool_build后
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 4672      4672         0 100% /

ntpclient这个应用貌似已经被放弃，还有rc.date这个脚本。

whatsapp经常提示更新，现在的版本是2.17.221

如果去掉libm这个数学库，那么这些函数就没有实现了：
cJSON.o: In function `parse_number':
cJSON.c:(.text+0xc00): undefined reference to `pow'
cJSON.o: In function `print_number':
cJSON.c:(.text+0xef0): undefined reference to `floor'
collect2: ld returned 1 exit status

2017-6.14
周连鹏 打流的效果：
7620 单流 20m： 56m
7628 单流 20m： 只有40-50m
从编码上看，7628是ofdm，而7620是ht。

王伍
sip-alg的实现方式有两种，一种是使用内核的方式，加上sipalg的支持，并且加上iptable的命令就可以实现。
另外一种方式是在应用级别的程序，这样做的问题可能是本地的sip程序就无法监听5060?端口了。



刘云
如果不开设备网页，那么运行正常，一开设备页面，内存马上下降。

菲律宾的5g看来是全的：
cfg -a ATH_countrycode=608

喻潇
p21的测试是在李光达，没有进行屏蔽房不断开关门测试。

苗立双
开始编译1826程序。另外一个压缩包中有编译的说明。

赵金去掉了busybox中的静态库
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 4800      4800         0 100% /
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 4.7M      4.7M         0 100% /
去掉iproute2,使用busybox中的ip
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 4736      4736         0 100% /

吴曦
没有看到升级脚本中升级内核的地方。
对升级nv有些担忧。

curl的功能还是强大的：
http://flyheaven.blog.163.com/blog/static/7401172201193111112273/

廖媛
那个sip alg还是enable不能用,disable可以用.

2017-6.13
余小虎
v10:
要增加会议和转接

p11s:
测试出修改室外单元的dhcp后,pc获得ip存在不正常的情况。
gre算通过了，需要写一个说明。

p28
存在硬件问题，充电ic，电池不供电了。有重启问题，电路要改。
软件上voip有回声。
三个运营商都有送。dialog: fax要匹配华为的设备。
斯里兰卡电信：测试voip, fax。要想办法换掉客户手中的机器。
兰卡贝尔：已经发现重启问题，修改后在挂测。

m60:
dialog还有检查2000台，1500台很难收回来。物料可能今天到，没有物料，检查也没有用。
整体的故障率在8-9%.
本月下旬，m60的新版本算完成了，要自测。

斯里兰卡电信 上voip+volte，程序+配置进行升级。
外置天线要测试。
扯皮中。

赵金去掉了剩下的几个cmdlib.c
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 4864      4864         0 100% /

tftp $loadaddr $firmware_name && erase 0x9F000000 +$filesize && cp.b $loadaddr 0x9F000000 $filesize

周连鹏
使用nmap扫描在公网上的路由器，会出现这样的情况：
Completed NSE at 14:08, 16.16s elapsed
Nmap scan report for 122.190.248.194
Host is up (0.13s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE        VERSION
53/tcp   open     tcpwrapped
80/tcp   filtered http
135/tcp  filtered msrpc
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
593/tcp  filtered http-rpc-epmap
4444/tcp filtered krb524
8080/tcp filtered http-proxy
这几个filtered有些奇怪，看解释是这样：

filtered(被过滤的)
    由于包过滤阻止探测报文到达端口， Nmap无法确定该端口是否开放。过滤可能来自专业的防火墙设备，路由器规则 或者主机上的软件防火墙。这样的端口让攻击者感觉很挫折，因为它们几乎不提供 任何信息。有时候它们响应ICMP错误消息如类型3代码13 (无法到达目标: 通信被管理员禁止)，但更普遍的是过滤器只是丢弃探测帧， 不做任何响应。 这迫使Nmap重试若干次以访万一探测包是由于网络阻塞丢弃的。 这使得扫描速度明显变慢。



郑达
手机上连接wifi后，直接出登录界面的情况，苹果和android的实现是不同的。
苹果的做法是使用http 1.0的方法去访问apple的网站，如果发现访问的和预期的不一样，那么就认为这个wifi需要登录，弹出登录的页面。
android的情况比较复杂，有些是使用url转移的。
还是要使用dns劫持来完成，这样这个系统无法这样做。

另外存在p28的中文ssid无法连接的情况，这个发现p28使用的是gbk编码，手机支持显示他的中文。

这个板子上的灯是折腾，有些板子的灯是错的，不同的板子灯gpio不同。
cd /sys/class/leds
# disable everything
echo none > ap123\:green\:lan/trigger
echo none > ap123\:blue\:wan/trigger
echo none > ap123\:green\:wan/trigger
echo none > ap123\:red\:wan/trigger
# then do tests
echo default-on > ap123\:blue\:wan/trigger
echo none > ap123\:blue\:wan/trigger
echo default-on > ap123\:green\:wan/trigger
echo none > ap123\:green\:wan/trigger
echo default-on > ap123\:red\:wan/trigger
echo none > ap123\:red\:wan/trigger

领佳板子刷个topap的程序吧
setenv ipaddr 10.8.0.33 && setenv serverip 10.8.0.100
tftpboot 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftpboot 0x80060000 tozedap-cp_ap123-jffs2 && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
bootm 0x9f6e0000

2017-6.12
周湘理
要开始9x07的tr069, 要求有7000多行，可能需要1000多个参数。当然存在可选项。菲律宾当前做了300多个。

李柱栋
新的slic已经调通，但是由于在驱动部分和原来的slic行为不同，这个slic必须发空，所以不能兼容，准备先用一种方式读id，如果读不到，就使用另外一种方式。


2017-6.11
去掉：UMAC_SUPPORT_WNM
-rw-rw-r--    1 1000     normal       18112 Jun 11  2017 adf.ko
-rw-rw-r--    1 1000     normal       47120 Jun 11  2017 ag71xx.ko
-rw-rw-r--    1 1000     normal       10228 Jun 11  2017 asf.ko
-rw-rw-r--    1 1000     normal      305940 Jun 11  2017 ath_dev.ko
-rw-rw-r--    1 1000     normal       64260 Mar 20  2017 ath_dfs.ko
-rw-rw-r--    1 1000     normal      732800 Jun 11  2017 ath_hal.ko
-rw-rw-r--    1 1000     normal       20988 Jun 11  2017 ath_pktlog.ko
-rw-rw-r--    1 1000     normal       38948 Jun 11  2017 ath_rate_atheros.ko
-rw-rw-r--    1 1000     normal       36680 Mar 20  2017 ath_spectral.ko
-rw-rw-r--    1 1000     normal       13100 Jun 11  2017 hst_tx99.ko
-rw-rw-r--    1 1000     normal     1094860 Jun 11  2017 umac.ko

sar的用法：
整体CPU使用统计(-u)   sar -u 1 2cd
各个CPU使用统计(-P)   sar -P ALL 1 1
内存使用情况统计(-r)   sar -r  1 2
整体I/O情况(-b)       sar -b 1 2
各个I/O设备情况(-d)    sar -d -p 1 1
网络统计(-n)          sar -n DEV 1 1
http://www.cnblogs.com/bangerlee/articles/2545747.html

2017-6.9
为什么新的程序会变成这样？
Jan  1 08:09:29 (none) daemon.err pppd[9812]: Can't create lock file /var/lock/LCK..ttyUSB3: No such file or directory

工业路由器中一开始就加载了所有的ko，貌似这样内存占用就太大了。

kate这个文本编辑器，198.4mb when installed，好像超大的样子。
ubuntu带的居然是4.x,而官网上已经到了16了，貌似也不是那么好用的样子，算了，还是用这个subline text吧。

李柱栋
认为没有必要去
认为支持验证是所有acs服务器必须遵循的标准。不过maik貌似对他这样搬标准的行为有些不满：
It supports both but globe production does not use unauthenticated http, so regardless, your device must support unauthenticated http
Every other device does and your last firmware did as well
So.... ? Let's please not push standard papers onto each other?

吴曦
开始进行版本合并操作，有些不敢动手

郑达
repeator 直接使用静态网页，也会出现错码。
有时候这些错误又非常非常难出现。wep不管，那么就只有dns劫持后出现的问题。也许使用wifi连接后出现的登录页面也是个不错的选择。

王伍
把周连鹏的机器用nmap扫描一下。
认为领佳已经知道了那个板子后面的黄绿灯已经修改。
有板子还是会重启。

屈峥嵘
不知道那个板子已经改了gpio。

何文秋
把那些js优化了一下，减少到几百k，那个晚显示的问题没有明显的改善。

2017-6.8
汪光华
gre配置已经可以手工ping到pc了。

吴曦 7520
1 wifi 校准工具，如果使用信可提供的工具，需要升级两次。
2 升级cp
3 陈良提出的短信修改
4 改logo
5 配置问题
6 监控网络的容错程序，reboot需要重启cp侧
7 挂测

set bootargs "root=/dev/nfs rw nfsroot=192.168.0.50:/opt/work/ath9.5/rootfs-tozedap-router_4g_industry_ap123.optbuild,nolock  init=/sbin/init noinitrd ip=192.168.0.1:192.168.0.50:192.168.0.1:255.255.255.0::eth0::off console=ttyS0,115200 machtype=DB120"

set bootargs "root=nfs nfsroot=192.168.0.50:/opt/work/ath9.5/rootfs-tozedap-router_4g_industry_ap123.optbuild,nolock   ip=192.168.0.1:192.168.0.50:192.168.0.1:255.255.255.0::eth0:off console=ttyS0,115200 machtype=DB120"

set bootargs "root=nfs nfsroot=192.168.0.50:/opt/work/ath9.5/rootfs-tozedap-router_4g_industry_ap123.optbuild,nolock   ip=dhcp::eth0:off console=ttyS0,115200 machtype=TZ-9341"

setenv bootargs board=AP143 console=ttyS0,115200 nfsroot=192.168.0.10:/tftpboot/rootfs rw ip=192.168.0.99:192.168.0.10:196.168.0.1:255.255.255.0::eth1:off
解释：

    board=AP143，板子类型最好设对，不然kernel可能启动失败；
    nfsroot=192.168.0.10:/tftpboot/rootfs，就是tftp server ip: + rootfs路径，解压xxx-rootfs.tar.gz出来的；
    rw设置可读可写权限；
    ip=板子IP: tftp server ip :网关ip(都在同一网段，网关ip随意填写):掩码：板子eth接口；（这里使用的是静态IP，如果想设置成dhcp，需要在make kernel_menuconfig中，在Networking support里，打开IP: kernel level autoconfiguration的dhcp支持）

set bootargs "console=ttyS0,115200 root=31:01 rootfstype=squanshfs ro init=/sbin/init mtdparts=spi0.0:64k(u-boot),6848k(rootfs),1152k(uImage),64k(mib0),64k(ART) machtype=DB120"

Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 5184      5184         0 100% /

2017-6.7
何文秋
使用js控制的按键，会在页面出来1-2秒才会出现。

当前工业路由器的内核还是有些大：
-rw-rw-r-- 1 jian jian  1034294  6月  6 18:02 vmlinux_routing.lzma.uImage
去掉乱七八糟的板子的支持：
-rw-rw-r-- 1 jian jian  1019593  6月  7 14:17 vmlinux_ap123.lzma.uImage

2017-6.6
为什么每次都会重启：
4g disconnect reboot

菲律宾功能测试第一次反馈

1.logo修改，具体由陈良提供
2.支持3G，shpa+显示为4G，LTE还是显示为LTE
3.internet 设置按钮没有下划线，与其他不一样
4.快速设置与短信之间添加“device setting”
5.主菜单中的导航菜单列表，需要在每个子菜单可见可选
6.connected devices 下添加帮助信息，告知wifi的operation功能如何使用
7.短信，发送短信多号码时不要分开存储，列表显示时多号码都要显示出来
8.流量统计：
  关闭流量统计功能时清除已使用流量;
  禁止编辑，只能打开或者关闭;（陈良确认一下是不是只是用户禁止编辑）
  单位与数字之间加个空格
9.一键自检的运行时间显示格式不对
10.网页上有实时参数的，需要实时刷新
11.apn做两套参数，不让编辑，仅能勾选测试或默认。（具体默认参数由陈良提供）


空闲时：
CPU:  0.8% usr  5.0% sys  0.0% nic 93.3% idle  0.0% io  0.0% irq  0.8% sirq
Mem: 22504K used, 18008K free, 0K shrd, 0K buff, 3736K cached

使用sweetspot
Mem: 22444K used, 18068K free, 0K shrd, 0K buff, 3736K cached
CPU:  0.2% usr 36.8% sys  0.0% nic 46.5% idle  0.0% io  0.0% irq 16.3% sirq
Load average: 8.42 7.39 4.31 1/137 1651
  PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
  598     2 admin    DW       0  0.0   0 24.4 [sdio_thread0/mm]
 1109     2 admin    DW       0  0.0   0 14.6 [ksdioirqd/mmc0]
  614     2 admin    DW       0  0.0   0 11.8 [rtw_rx/wlan0]

iperf
Mem: 23128K used, 17384K free, 0K shrd, 0K buff, 4044K cached
CPU:  0.6% usr 45.5% sys  0.0% nic 40.2% idle  0.0% io  0.0% irq 13.5% sirq
Load average: 8.36 8.01 5.70 1/142 1663
  PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
  598     2 admin    DW       0  0.0   0 29.1 [sdio_thread0/mm]
 1109     2 admin    SW       0  0.0   0  9.1 [ksdioirqd/mmc0]
  614     2 admin    DW       0  0.0   0  7.9 [rtw_rx/wlan0]



192.168.1.154 c盘满了。
把 ErrorLog scss10 转移到F盘
c.inetpub.logs.LogFiles.W3SVC3里面的文件超级大，移动到F盘。

2017-6.5
华润的招标的技术部分，任银善做了备注，请查看:
路由器_设备应用标准
指标类别	指标名称	指标说明	应用场景	是否核心指标	是否必须满足项	备注	说明
硬件要求	产品类型	企业级路由器（支持4G，可直接插卡）	门店、DC内外网连接	是	是	适用于大超门店、DC、小业态门店内外网连接
	内存	容量：16-512MB	门店、DC内外网连接	是	是
		FLASH:16-512MB	门店、DC内外网连接	是	是	必填项
	线速转发能力	转发性能：350-550Kpps	门店、DC内外网连接	是	是	必填项
		带业务转发性能：150Mbps	门店、DC内外网连接	是	是
	固定WAN端口	2*GE(其中1个GE由以太网交换端口提供)	门店、DC内外网连接	是	是	必填项
	固定以太网交换端口	4*GE	门店、DC内外网连接	是	是
	内置LTE	FDD LTE	A4文件打印	是	是	必填项
	USB2.0端口	1个	A3文件打印	是	是
	串行辅助/控制台端口	1个
	串行辅助/控制台端口	1个
软件要求	基础功能	DHCP server/client/relay，PPPoE server/client，PPPoA server/client，PPPoEoA server/client，NAT，子接口管理	门店、DC内外网连接	是	是		PPPoE无server,PPPoA无server，无子接口管理
	无线局域网(AP)	AP设备管理（VAP管理），WLAN QoS（WMM），WLAN安全（WEP/WPA/WPA2/密钥管理），WLAN射频管理（802.11 b/g/n），WLAN用户管理(AP功能仅W无线款型支持)	门店、DC内外网连接	是	是		无用户管理，只能查看
	无线局域网(AC)	AP设备管理(AC发现/AP接入/AP管理)，CAPWAP协议, WLAN用户管理，WLAN射频管理（802.11 b/g/n），WLAN QoS（WMM），WLAN安全（WEP/WPA/WPA2/密钥管理）	门店、DC内外网连接	是	是	必填项	AC先只有派联的平台，无WLAN Qos（WMM），WLAN安全（WEP/WPA/WPA2）
	局域网功能	IEEE 802.1P，IEEE 802.1Q，IEEE 802.3，VLAN管理，MAC管理，MSTP等	门店、DC内外网连接	是	是	必填项	无IEEE 802.1P，IEEE 802.1Q，IEEE 802.3，VLAN管理，MSTP等
	IPv4单播路由	路由策略，静态路由，RIP，OSPF，IS-IS，BGP	门店、DC内外网连接	是	是	必填项
	IPv6基本功能	IPv6 ND，IPv6 PMTU，IPv6 FIB，IPv6 ACL	门店、DC内外网连接	是	是	必填项	？
	IPv6隧道技术	手工隧道，自动隧道，GRE隧道，6to4，ISATAP	门店、DC内外网连接	是	是	必填项	？
	IPv6单播路由	路由策略，静态路由，RIPng，OSPFv3，IS-ISv6，BGP4+	门店、DC内外网连接	是	是	必填项	？
	组播功能	IGMP version1/2/3，PIM SM，PIM DM，MSDP	门店、DC内外网连接	是	是	必填项	无
	QoS	Diffserv模式，优先级映射，流量监管（CAR），流量整形，拥塞避免（基于IP优先级/DSCP WRED），拥塞管理（LAN接口：SP/WRR/SP+WRR；WAN接口：PQ/CBWFQ），MQC（流分类，流行为，流策略），端口三级调度和三级整形（Hierarchical QoS），智能应用控制（SAC	门店、DC内外网连接	是	是	必填项	无
	安全	ACL，防火墙，802.1x认证，AAA认证，RADIUS认证，HWTACACS认证，广播风暴抑制，ARP安全，ICMP反攻击，URPF，CPCAR，黑名单，攻击源追踪，PKI	门店、DC内外网连接	是	是	必填项	无
	管理维护	升级管理，设备管理，Web网管，GTL，SNMP（v1/v2c/v3），RMON，NTP，CWMP，Auto-Config，U盘开局，NetConf，命令行	门店、DC内外网连接	是	是	必填项	无GTL，RMON，Auto-Config，NetConf，U盘开局
	VPN	PSec VPN，GRE VPN，DSVPN，SSL VPN，L2TP VPN	门店、DC内外网连接	是	是	必填项	无DSVPN，SSL VPN
功率及保修信息	电源及功率	电源：100-240V	门店、DC内外网连接	是	是	选填项
		支持最大功率：24W	门店、DC内外网连接
	环境参数	工作温度：0-45℃，工作湿度：5-95%	门店、DC内外网连接
	售后	一年标准维保	门店、DC内外网连接	是	是



~ # cat /proc/meminfo
MemTotal:          40512 kB
MemFree:           15976 kB
Buffers:               0 kB
Cached:             5876 kB

[New process 9776]
#0  0x004041c0 in main (argc=3, argv=0x7fedcbf4) at main.c:546
warning: Source file is more recent than executable.
546				if(ids_module->idVendor==modules_info_summary[i]->module_serial.idVendor &&

[ 2055.170000] rc.check_reboot invoked oom-killer: gfp_mask=0xd0, order=1, oom_adj=0, oom_score_adj=0
[ 2055.180000] Call Trace:[<80077f88>] 0x80077f88
[ 2055.190000] [<802b0b98>] 0x802b0b98
[ 2055.190000] [<802b0b98>] 0x802b0b98
[ 2055.190000] [<800c09cc>] 0x800c09cc
[ 2055.200000] [<800ccbc4>] 0x800ccbc4
[ 2055.200000] [<800c0ddc>] 0x800c0ddc
[ 2055.210000] [<800c0d28>] 0x800c0d28
[ 2055.210000] [<800c129c>] 0x800c129c
[ 2055.210000] [<800c4be4>] 0x800c4be4
[ 2055.220000] [<80075740>] 0x80075740
[ 2055.220000] [<800ef1ec>] 0x800ef1ec
[ 2055.220000] [<80101d90>] 0x80101d90
[ 2055.230000] [<8007642c>] 0x8007642c
[ 2055.230000] [<800f5a04>] 0x800f5a04
[ 2055.230000] [<800f5f18>] 0x800f5f18
[ 2055.240000] [<80068fac>] 0x80068fac
[ 2055.240000] [<8006c6a4>] 0x8006c6a4
[ 2055.250000]
[ 2055.250000] Mem-Info:
[ 2055.250000] Normal per-cpu:
[ 2055.250000] CPU    0: hi:   18, btch:   3 usd:   1
[ 2055.260000] active_anon:560 inactive_anon:1 isolated_anon:0
[ 2055.260000]  active_file:10 inactive_file:11 isolated_file:0
[ 2055.260000]  unevictable:8129 dirty:0 writeback:0 unstable:0
[ 2055.260000]  free:1082 slab_reclaimable:236 slab_unreclaimable:2809
[ 2055.260000]  mapped:2 shmem:1 pagetables:77 bounce:0
[ 2055.290000] Normal free:4328kB min:1016kB low:1268kB high:1524kB active_anon:2240kB inactive_anon:4kB active_file:40kB inactive_fils
[ 2055.330000] lowmem_reserve[]: 0 0
[ 2055.330000] Normal: 954*4kB 58*8kB 3*16kB 0*32kB 0*64kB 0*128kB 0*256kB 0*512kB 0*1024kB 0*2048kB 0*4096kB = 4328kB
[ 2055.340000] 8151 total pagecache pages
[ 2055.350000] 0 pages in swap cache
[ 2055.350000] Swap cache stats: add 0, delete 0, find 0/0
[ 2055.360000] Free swap  = 0kB
[ 2055.360000] Total swap = 0kB
[ 2055.370000] 16384 pages RAM
[ 2055.370000] 1012 pages reserved
[ 2055.370000] 26 pages shared
[ 2055.370000] 14176 pages non-shared
[ 2055.380000] [ pid ]   uid  tgid total_vm      rss cpu oom_adj oom_score_adj name
[ 2055.390000] [ 1447]     0  1447      289       22   0       0             0 macwriter
[ 2055.390000] [ 1452]     0  1452      216       10   0       0             0 httpd
[ 2055.400000] [ 2260] 65534  2260      261       21   0       0             0 dnsmasq
[ 2055.410000] [ 2324]     0  2324      370       20   0       0             0 hostapd
[ 2055.420000] [ 2325]     0  2325      524      120   0       0             0 autoset_channel
[ 2055.430000] [ 2326]     0  2326      296       16   0       0             0 tzupdate
[ 2055.430000] [ 2370]     0  2370      217       11   0       0             0 syslogd
[ 2055.440000] [ 2480]     0  2480      217       12   0       0             0 logread
[ 2055.450000] [ 2822]     0  2822      218       12   0       0             0 dialtool_d
[ 2055.460000] [ 2823]     0  2823      279       21   0       0             0 flowstat
[ 2055.470000] [ 2824]     0  2824      218       13   0       0             0 rc.check_reboot
[ 2055.480000] [ 2835]     0  2835      277       19   0       0             0 ntpsupplicant
[ 2055.480000] [ 2837]     0  2837      523      118   0       0             0 autoset_channel
[ 2055.490000] [ 2845]     0  2845      235       34   0       0             0 system_moniter
[ 2055.500000] [ 3126]     0  3126      267       12   0       0             0 tzresetd
[ 2055.510000] [ 3127]     0  3127      218       13   0       0             0 rc.check_nat_is
[ 2055.520000] [ 3151]     0  3151      217       11   0       0             0 telnetd
[ 2055.530000] [ 3945]     0  3945      222       20   0       0             0 sh
[ 2055.530000] [ 6242]     0  6242      217       11   0       0             0 getty
[ 2055.540000] [ 1526]     0  1526      220       15   0       0             0 sh
[ 2055.550000] [ 3135]     0  3135      220       15   0       0             0 vi
[ 2055.560000] [16926]     0 16926      216       10   0       0             0 sleep
[ 2055.570000] Out of memory: Kill process 1447 (macwriter) score 1 or sacrifice child
[ 2055.570000] Killed process 1447 (macwriter) total-vm:1156kB, anon-rss:88kB, file-rss:0kB

占永平
菲律宾p21，有时会出现中英文选择的选项出来。

廖媛：
2017年6月5日  P21 会议记录 ------尼日利亚
待解决问题 :
1. Key 测试，确认生产工具 ，并且给到生产。
2.内部搭建VOIP 服务器。
3.WIFI 掉线原因分析。
4. 出最后一版本“ 生产程序 ” 给客户测试。
5.TRO69 远程升级：请姚协调同事安排本地远程测试，同时我会再次跟客户确认 "ZIP “文件 是否可行 。

最近发现越来越多的office里过多的在上班时间滥用视频网站，可能是由于脑残会的影响，但必竟是上班时间，不应该做与工作无关的事，也过多地影响了office的工作带宽。我在路由上测试了一条规则来block视频网站的访问请求，发现非常有效：
iptables -A FORWARD  -m string –-string “ku6.com” --algo bm -j DROP
iptables -A FORWARD  -m string –-string “tudou.com” –-algo bm -j DROP
iptables -A FORWARD  -m string –-string “ouou.com” –-algo bm -j DROP
http://blog.sina.com.cn/s/blog_690b92530100zggp.html

2017-6.2
p25 测试 占永平
ID	缺陷名	现象	修复状态	备注
P25	版本:v15	配置版本：P25_1.17	模块	信可
1	导入功能不可用	将备份好的防火钱文件加载进去，直接返回失败	未修复
2	在网络工具长时间pnig，仍会出现超时	在网络工具中ping外网，一直ping下去，十五分钟后仍会显示超时	未修复
3	网络工具中的trace无法使用	URL中输入“www.baidu.com”,端口为“1-65535”或者80，网页 上没有显示路由信息	未修复
4	网络工具中抓包功能用不了		未修复
5	APN设置手动下无法编辑		未修复	这个不确定是不是bug,不知道实际的实现方式
6	PIN无法开启	输入当前PIN码，网页上一直返回失败的提示	未修复
7	PIN码设置为disable下仍可以输入	开始在默认下输入会有禁止输入提示，点击PIN码开启，再关闭，就一直没有禁止输入的提示	未修复
8	流量到达阈值后，页面提示是否断开网络，点击确定，页面返回失败		未修复


只编译squashfs_build貌似修改的文件没有合并到squashfs中去。

killall  sh
killall dialtool_new
rm /tmp/.dialtool_indicator
cd /tmp
tftp -g 10.8.0.100 -l dialtool_new
chmod +x dialtool_new
./dialtool_new -s /tmp/dialtool_config &

sim卡的pin相关指令，好久了。
1.AT+CLCK="SC",1,"1234"		使用SIM卡锁功能,密码为为上次设置的(或初始密码),或者使用CPWD更改后的密码
2.AT+CLCK="SC",2				查询SIM卡锁功能
3.AT+CLCK="SC",0,"1234"		关闭SIM卡锁功能
4.AT+CPWD="SC","1234","4321"	修改PIN码
5.AT+CPIN?					查询PIN码的状态,是否需要输入PIN码
6.AT+CPIN="1234"				输入PIN码
7.AT+CPIN="88139522","1234"	输入PUK码和新的PIN码

2017-6.1
郑达
那个写了mac后ssid无法搜索的问题，是不但要写wifi的地址，还要写wan,lan等地址，还要按照规则写。

还有若干个端口是开放的。
nmap 192.168.254.254 -v -A -p1-65535
Scanning 192.168.254.254 [65535 ports]
Discovered open port 80/tcp on 192.168.254.254
Discovered open port 53/tcp on 192.168.254.254
Discovered open port 10020/tcp on 192.168.254.254
Discovered open port 4719/tcp on 192.168.254.254
Discovered open port 3535/tcp on 192.168.254.254
Discovered open port 10005/tcp on 192.168.254.254

netstat -lnp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:5037          0.0.0.0:*               LISTEN      1491/adbd
tcp        0      0 0.0.0.0:3535            0.0.0.0:*               LISTEN      1500/chkSvr
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1486/goahead
tcp        0      0 0.0.0.0:10005           0.0.0.0:*               LISTEN      1445/zte_tools_agen
tcp        0      0 0.0.0.0:53              0.0.0.0:*               LISTEN      1239/dnsmasq
tcp        6      0 192.168.254.254:10020   0.0.0.0:*               LISTEN      1448/pc_server
tcp        0      0 :::4719                 :::*                    LISTEN      1515/telnetd
tcp        0      0 :::53                   :::*                    LISTEN      1239/dnsmasq
udp        0      0 0.0.0.0:53              0.0.0.0:*                           1239/dnsmasq
udp        0      0 :::53                   :::*                                1239/dnsmasq
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING       1514 1491/adbd           @jdwp-control

goahead，有网页连接，那么有非常多的TIME_WAIT存在。

我这里网卡不能自动起来的事情，应该是：
linux_plat/base/linux/lib/zte_libs/libnetapi这个so里面的MSG_NET_PLUGIN消息，变成了MSG_STATIC_DHCP这个消息。

苑德强
要p21的root密码。以后的程序要默认关闭telnetd

吴曦
1 信可说，可以关闭trap模式，碰到问题直接重启。
2 nv 坏掉， 反复重启不能上网的，需要在信可模拟出来
3 未来几天将在信可上班，一起工作。

每次上传github都要输入用户名密码么？

2017-5.31
王伍：
姚国梁：陈良测的锁频有问题，要使用屏蔽房不断开门关门来测试。

更换内核，还是可以自动把eth0起来的。

比较一下，我编译的系统在这几个程序大小和汪光华的不一样：
unzip
zte_fota_reco
zte_topsw_dmapp
dhcp6c
这些和网卡有什么不同呢？

这个地址还能用，还是用起来吧，多一个备份的地方。
https://github.com/netjianl/work-doc.git

升级到汪光华编译的程序就可以自动把eth0起来，奇怪的事情，从脚本来看是没有什么区别的，但是有些程序的大小不一样。但是二进制也看不出来啊。原来是没有加上执行权限。

廖媛
抱怨白俊剑ip passthrogh出的太慢了。

白俊剑
ippassthrogh只剩下默认网关没有设置了。

刘凯内蒙办
问网管服务器变得很慢了。

吴曦
问明天去信可的情况，当前主要的问题是搜网锁band，下at有时候正常，有时候不正常。
还有就是校准区被冲掉的情况了。

吴开利
问内蒙联通和湖北联通的模块是否一样，我印象中是不同的。

我这里编译的程序以太网默认就没有启动。奇怪的事情。

郑达
中继器网页升级是可以的。
现在问题还有有一个ap无法连接，但是其他的手机，我的9341的cpe是可以连这个ap的。
还有一个ap，是魏启婷的，无法搜索到它。
riltek说无法做的检查一个天线能否联通。
还修改了原有的自动信道，是处于自动信道时无法搜索到repeator的ssid，改成了即使在client情况下也设置固定信道，而这个固定信道是在搜索的设置设置的。但这样对那些20/40的ap就有问题。
现在修正了自动信道的问题，但是那个无法连接的ap还是无法连接。

使用这个5.15版本似乎也是正常的，那么这个问题可以采用2分法去查了。
汪光华找了一遍，是b3bb6246ee39e81ac97e3d74a5387851cd75a393这个提交，那么认为是赵刚没有判断(wp->path)是否为空造成的。

赵金的生产工具又很久没有上传了。

2017-5.27
吴曦
1 wep加密选择非第一组秘钥错误，建议只有一组给用户输入。
2 锁band ，已手工验证，无异常，继续加入到程序中
3 生产工具 imei, mac 灯，按键， wifi信号
  出现冲掉校准区的问题，严重问题。
4 网络选择，需要关闭数据再设置，可以在后台这样执行， 不行重启。
5 进入trap状态 信可未解决
6 有一次nv所在的cfg文件不能访问，导致系统工作不正常，继续复现
7 有一次上网显示正常，但无数据，使用cfun=0,cfun=1解决。后续增加监控程序。
8 wifi 校准工具 信可未提供
9 watchdog 信可未解决
10 使用nmap -v -A 192.168.254.254会导致goahead挂掉，继续查找原因
11 安全问题，还有一个，继续修改。

郑达
去连接派联的Scorpius无线，显示的是wpa2，但它页面设置的是wpa，不能连接。

现在NET_ZX29_GMAC_SWITCH这个选项在内核中被删除了，即使加上，会出现sw0，但是ping没有作用。

这样来删除地址：
sudo ip addr del 192.168.254.50/32 dev eth0

使用 nmap -v -A 192.168.254.254这样的指令，在
tz_version:P25_1.09
tz_real_version:P25_1.09
tz_build_time:2017-05-18_16:05
tz_build_by:wgh@wgh-ThinkPad-E550
tz_branch:master
tz_sha1:1f9dd5d71b3198dc7bf07a1a40cd3fd3bbd1698b
tz_commit_by: hewq/2017-05-18 15:56:00 +0800
tz_commita:prefect traffic alarm page
这个版本上貌似是正常的。

2017-5.26
魏启婷
测试一个p11，出现断网后无法再次上网的情况，

汪光华
中兴7520低成本cpe方面写生成工具碰到了一些奇怪的问题，其中一个问题是由于参数变量名和吴曦原来的变量名一样，导致奇怪的行为。另外的估计和写mac, imei一起进行时，中兴底层的保护没有做好，会出现校准区不正常的情况。估计后面只写imei，mac等自己处理。

貌似在ath9.5中的cpe-df的apup中还没有对extap的支持。
        if [ "${EXTAP}" = "on" ]; then
            iwpriv ath0 extap 1
        fi

以前的文档貌似有错误，1860的要这样设置
WANIP=`ifconfig lmi40 | grep inet | busybox cut -d : -f 2 | busybox cut -d ' ' -f 1`
echo $WANIP
ifconfig lmi40 0.0.0.0 up
busybox route add -host $WANIP dev br0
busybox route add default dev lmi40
echo "1" > /proc/sys/net/ipv4/conf/lmi40/proxy_arp
echo "1" > /proc/sys/net/ipv4/conf/br0/proxy_arp
iptables -F -t nat
iptables -t nat -I POSTROUTING -s 192.168.1.1/255.255.255.0 -o lmi40 -j SNAT --to-source $WANIP

pc这样设置，要删掉那个masq的规则，现在有个容错的程序，要砍掉。
ip  10.42.39.122
netmask  255.255.255.255
dns 221.179.38.7 120.192.165.7

可以这样设置是可以的
ip  192.168.0.100
netmask  255.255.255.255
dns 221.179.38.7 120.192.165.7

汪光华
对makefile, 编译中-l的使用还不了解。

王伍
还有加强web的人手

2017-5.25
领佳 屈工
来拿走了一个刷过uboot的板子。

郑达
突然，中继器的软件不能申请内存了，只有编译到10几号向杰增加的大量网页前才不报错，这样，基本不能使用了。

李金龙
问了一下各个项目的情况，说将在自助，工业路由器， ict上加大力量。ict主要是wifi覆盖。今年过关，不亏本，信心能够提示一个层次，下决心重启上市。

这个sublime打开有些文本文件，里面的双字节的符号似乎总是乱码。

郑达 赵金
问中继器是否所以的命令从串口出。

姚国梁
那个不读卡的p11，通过加上拉电阻解决的。

王凯
有一台cpe显示wifi 未启动，重新升级无效。可能要试试换校准区了。

2017-5.24
王伍
居然没有和李总提加工资的事情。

算下来工业路由器p53的剩余空间只有1m了。

吴开利
问研发是否给出正在开发的产品的简单说明。

王伍
cat-m，在华为测试通过后就要在其他地方使用了。

吴曦
昨天的trap后，抓包后认为是goahead进程造成的。

占永平
p21的ip passthrough，使用联芯的模块可以，宽翼的不行。

孙先锋 内蒙工程
在网管平台增加设备后，点击获取参数不能得到数据。保存后，都是红色。但是点击其ip，能够看到设备的网页。
后来说知道问题了，也不知道是什么问题。

2017-5.23
setenv ipaddr 10.8.0.33 && setenv serverip 10.8.0.100
tftpboot 0x80060000 uboot.1 && erase 0x9f000000 +0x20000&&cp.b $fileaddr 0x9f000000 $filesize
u-boot> md 18050000

喻潇
派联的要把平台的使用培训一下。

苗立双
1 赞比亚iperf，
  1761 会自动重启，安徽出现过，胡媛媛在现场，刘云处理
2 阿根廷 三旗模块
  加ssh，原来加过。
  锁物理小区 刘云处理
3 四川联通标书

2017-5.22
换w10这个板子来吧：
setenv ipaddr 10.8.0.33 && setenv serverip 10.8.0.100
tftpboot 0x80060000 uboot.bin.topap && erase 0x9f000000 +0x20000&&cp.b $fileaddr 0x9f000000 $filesize
tftpboot 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftpboot 0x80060000 tozedap-cp_ap123-jffs2 && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize

第12次
Booting image from 0x9F020000...

   Image name:    MIPS OpenWrt Linux-3.18.36
   Build date:    2016-09-28 16:05:46 UTC
   Architecture:  MIPS
   OS/image type: Linux Kernel
   Compression:   LZMA
   Data size:     1003.8 kB (1027913 bytes)
   Load address:  0x80060000
   Entry point:   0x80060000

   Header CRC...  OK!
   Data CRC...    skipped

Stopping network... OK!
Uncompressing Kernel... ERROR
## Error: LZMA error '1'!

第22次
[    1.980000] SQUASHFS error: xz decompression failed, data probably corrupt
[    1.990000] SQUASHFS error: squashfs_read_data failed to read block 0x604f6
[    2.030000] SQUASHFS error: xz decompression failed, data probably corrupt
[    2.040000] SQUASHFS error: squashfs_read_data failed to read block 0x604f6
[    2.040000] Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000a
[    2.040000]
[    2.040000] ---[ end Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000a
[    2.040000]



# $(1): vendor, board name/model
# $(2): hostname
# $(3): default FLASH size in MB
# $(4): reset button GPIO number
# $(5): 1 if reset button is active low
# $(6): SOC_TYPE
define config_init

lsdk_kernel:
        @$(call define_add,CONFIG_LSDK_KERNEL,1)
#if defined(CONFIG_LSDK_KERNEL)
                "lsdk_kernel=1\0"
#endif

法国佬的uboot似乎加了CONFIG_FOR_TPLINK_WR842N_V3这个类型。也许应该是tp-link_tl-wr842n_v3这个？
setenv ipaddr 10.8.0.33 && setenv serverip 10.8.0.100
tftpboot 0x80060000 u-boot.1 && erase 0x9f000000 +0x20000&&cp.b $fileaddr 0x9f000000 $filesize

setenv bootargs "console=ttyS0,115200 root=31:02 rootfstype=squashfs rw init=/sbin/init mtdparts=mtdparts=ath-nor0:128k(u-boot)ro,1280k(uImage),6656k(rootfs),64k(mib0),64k(ART)"

u-boot> md 18050000
18050000: 00021580 00214000 01308000 00000000    .....!@..0......
18050010: 40010400 C009FFFE 0009F33A 00000014    @..........:....
18050020: 00000000 00000271 00098000 00000101    .......q........
18050030: 000010B3 0A47F028 00004000 0523F828    .....G.(..@..#.(
18050040: 41020CCC 781003E8 0050103C 00000000    A...x....P.<....
18050050: 00000000 00000000 00000000 00000000    ................
18050060: 00000000 00000000 00000000 00000000    ................
18050070: 00000000 00000000 00000000 00000000    ................


uboot> md 18050000
18050000: 00021580 00214000 01308000 00000000    .....!@..0......
18050010: 00000800 C013FFFE 00138000 00000014    ................
18050020: 00000000 00000271 0013BB10 00000101    .......q........
18050030: 000010B3 0A47F028 00004000 0523F828    .....G.(..@..#.(
18050040: 41020CCC 781003E8 0050103C 00000000    A...x....P.<....


第8次：
[    1.250000] Freeing unused kernel memory: 248K (80332000 - 80370000)
[    1.980000] SQUASHFS error: xz decompression failed, data probably corrupt
[    1.990000] SQUASHFS error: squashfs_read_data failed to read block 0x604f6
[    2.030000] SQUASHFS error: xz decompression failed, data probably corrupt
[    2.040000] SQUASHFS error: squashfs_read_data failed to read block 0x604f6
[    2.040000] Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000a
[    2.040000]
[    2.040000] ---[ end Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000a
[    2.040000]

第12次 哪里不对的样子，modem没有看到起来。
[    1.990000] init: Console is alive
[    1.990000] init: - watchdog -
[   81.700000] random: nonblocking pool is initialized
[  122.010000] init: - preinit -
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[  126.330000] eth0: link up (100Mbps/Full duplex)
[  127.010000] jffs2: notice: (310) jffs2_build_xattr_subsystem: complete building xattr subsystem, 0 of xdatum (0 unchecked, 0 orphan.
[  127.020000] mount_root: switching to jffs2 overlay
[  127.100000] eth0: link down
[  127.110000] procd: - early -
[  127.110000] procd: - watchdog -
[  128.090000] procd: - ubus -
[  129.280000] procd: - init -
Please press Enter to activate this console.

第22次：
Booting image from 0x9F020000...

   Image name:    MIPS OpenWrt Linux-3.18.36
   Build date:    2016-09-28 16:05:46 UTC
   Architecture:  MIPS
   OS/image type: Linux Kernel
   Compression:   LZMA
   Data size:     1003.8 kB (1027913 bytes)
   Load address:  0x80060000
   Entry point:   0x80060000

   Header CRC...  OK!
   Data CRC...    skipped

Stopping network... OK!
Uncompressing Kernel... ERROR
## Error: LZMA error '1'!

何文秋
又碰到了速度慢的问题。关闭网页一段时间后，貌似正常了，他前几天还以为是nv导致的，今天又不知道是什么导致的，看的时候不停的有ifconfig wlan0 up的命令出现。从top 命令追源，发现是wlan-sever发出的命令。他现在觉得是不是他折腾了一天，就出现了这个情况。

陶嵩
1860的机器，现在不能不插卡测信号了，原来是可以的。

吴曦
信可的说trap拔电可以恢复，实际上貌似不是这样。或者使用watchdog进行恢复，但watchdog的操作当前是无效的。
1 锁band28后，不能搜网，加上41也不能搜到网。
2 reboot不能重启moden的还没有在init文件中尝试。
3 改风格准备让何文秋来做
4 汪光华还有生产工具和m60的一些东西要做。
 6 ussd还没有进行处理


王伍
工业路由器还有emtc，和加入sta模式两个功能。

喻潇
发邮件说那个p11s的支持电信拨号的程序在公司测试是可以用的，但是在用户那里还是说不行。

姚国梁
意大利的p10p： 今天向杰能改好。
越南多语言：周三开始
其他的事情是尼日利亚的voip还可能要进行程序更新。



郑达：
中继器搜索ssid时会出现一个for循环变量被改变而中途退出的情况，必然发生在某个中文ssid的情况。
是一个地方会对中文的ssid进行处理，变成0xE9...这样的模式。

占永平
三条电源线发了一个星期了，还没有动静。采购那边说今天才发到。
已经说去买了。

2017-5.19
setenv ipaddr 10.8.0.33 && setenv serverip 10.8.0.100
tftpboot 0x80060000 uboot.bin.lingjia && erase 0x9f000000 +0x20000&&cp.b $fileaddr 0x9f000000 $filesize
这样把老外的uboot写进去看起来正常启动了系统。

启动第三次发现
[    0.600000] libphy: ag71xx_mdio: probed
[    1.190000] ag71xx ag71xx.0: connected to PHY at ag71xx-mdio.1:00 [uid=004dd042, driver=Generic PHY]
[    1.200000] eth0: Atheros AG71xx at 0xb9000000, irq 4, mode:MII
[    1.200000] TCP: cubic registered
[    1.210000] NET: Registered protocol family 17
[    1.210000] bridge: automatic filtering via arp/ip/ip6tables has been deprecated. Update your scripts to load br_netfilter if you n.
[    1.230000] 8021q: 802.1Q VLAN Support v1.8
[    1.240000] VFS: Mounted root (squashfs filesystem) readonly on device 31:2.
[    1.250000] Freeing unused kernel memory: 248K (80332000 - 80370000)
[    1.980000] SQUASHFS error: xz decompression failed, data probably corrupt
[    1.990000] SQUASHFS error: squashfs_read_data failed to read block 0x604f6
[    2.030000] SQUASHFS error: xz decompression failed, data probably corrupt
[    2.030000] SQUASHFS error: squashfs_read_data failed to read block 0x604f6
[    2.040000] Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000a
[    2.040000]
[    2.040000] ---[ end Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000a
[    2.040000]

重新来的第5次：
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[    6.260000] eth0: link up (100Mbps/Full duplex)
[    7.170000] jffs2: notice: (327) jffs2_build_xattr_subsystem: complete building xattr subsystem, 0 of xdatum (0 unchecked, 0 orphan.
[    7.190000] mount_root: switching to jffs2 overlay
[    7.220000] eth0: link down
[   11.300000] usb 1-1.4: new high-speed USB device number 3 using ehci-platform
然后重启。

第6次：
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[    6.260000] eth0: link up (100Mbps/Full duplex)
[    7.170000] jffs2: notice: (327) jffs2_build_xattr_subsystem: complete building xattr subsystem, 0 of xdatum (0 unchecked, 0 orphan.
[    7.190000] mount_root: switching to jffs2 overlay
[    7.220000] eth0: link down
[   11.300000] usb 1-1.4: new high-speed USB device number 3 using ehci-platform
[   82.560000] random: nonblocking pool is initialized
好像也不动了，拔电继续。

第14次：
[    0.000000] NR_IRQS:51
[    0.000000] Clocks: CPU:550.000MHz, DDR:400.000MHz, AHB:200.000MHz, Ref:25.000MHz
[    0.000000] Calibrating delay loop... 274.02 BogoMIPS (lpj=1370112)
[    0.070000] pid_max: default: 32768 minimum: 301
[    0.070000] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.080000] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
停止了，拔电继续。

第16次：
[    0.000000] Calibrating delay loop... 274.02 BogoMIPS (lpj=1370112)
[    0.070000] pid_max: default: 32768 minimum: 301
[    0.070000] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.080000] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
停止了，拔电继续。好像和上一次一样。





看起来换了那个uboot，跑了一个晚上，另外一台机器，连续拔插，也都正常启动了。

何文秋：
他的板子插了卡后，看起来也跑到了那个trap状态去了。

郑达：
在dns劫持中，手机发送了大量的dns请求，造成需要50秒手机才能自动转到中继器的界面。

5.18
苗立双
在9341原来的系统中echo 3 > /proc/sys/vm/drop_caches不返回，看代码是被改为使用内核定时器的方式来做了，也没有起到左右，cache一直有30多m

雒晓峰
问关于apn的问题。
上海那个1400台工业路由器的单，是一个代理给人民日报社上海分社，由于党报已经没有没有人看了，所以搞一个大屏，推送新闻或社论用。而这样的自助，安徽也要做，并且可以自助+工业路由器全给我们做，只是已经转了2次手，所以安徽利润会受影响。
上海的报价是535 7模， 5模 505？
在微信上看起来对方还有还价。

金晶
看起来已经说动了郑杏泉，给他来做app。
要在派联的对路由器的app中增加对摄像头的控制。

eddy
要9341的cpuid，貌似没有找到这样的东西。

王伍
折腾给领佳死机的问题

ar7240> md 18050000
18050000: 40021540 40818000 01308000 00000000    @..@@....0......
18050010: 40010400 c009fffe 0009f33a 00000014    @..........:....
18050020: 00000000 00000271 00098000 00000101    .......q........
18050030: 000010b3 0a47f028 00004000 0523f828    .....G.(..@..#.(
18050040: 41020ccc 78100000 00ac0000 00000000    A...x...........

uboot> md 18050000
18050000: 00021580 00214000 01308000 00000000    .....!@..0......
18050010: 00000800 C013FFFE 00138000 00000014    ................
18050020: 00000000 00000271 0013BB10 00000101    .......q........
18050030: 000010B3 0A47F028 00004000 0523F828    .....G.(..@..#.(
18050040: 41020CCC 781003E8 0050103C 00000000    A...x....P.<....

bootargs=console=ttyS0,115200 root=31:02 rootfstype=squashfs init=/sbin/init mtdparts=ath-nor0:128k(u-boot)ro,1280k(uImage),6656k(rootfs),64k(mib0),64k(ART),7936k@0x20000(firmware),8192k@0x0(all)ro
bootcmd=bootm 0x9F020000

console=ttyS0,115200 root=31:02 rootfstype=squashfs init=/sbin/init mtdparts=ath-nor0:128k(u-boot)ro,1280k(uImage),6656k(rootfs),64k(mib0),64k(ART),7936k@0x20000(firmware),8192k@0x0(all)ro mem=64M rootfstype=squashfs,jffs2 noinitrd

setenv ipaddr 10.8.0.33 && setenv serverip 10.8.0.100
tftp 0x80060000 tuboot.bin && erase 0x9f000000 +0x10000&&cp.b $fileaddr 0x9f000000 $filesize

tftp 0x80060000 uboot.bin.lingjia
go 0x80060000 也是一样挂掉，应该没有成功过的。

汪光华：
来说不愿意去开会，觉得无非是说要努力工作的事情。谈到他弟弟的孩子都已经3岁了，他父母会用一种感觉他对未来有一种焦虑，结婚，买房，小孩。

白俊剑：
tr069的ssl连接功能是自动适应的，给出的地址是http，那么就是普通的，如果是https，那么就是ssl加密的，也分别测试过，所以直接何必就可以了，不需要额外的设置。


2017-5.17
居然一个git checkout 把今天写的无数东西都清空了，那么是不是要重写呢？

吴曦：同学在平安金融， 14k，上班8小时，年终奖50k， 做android
另外一个在做coolb？手机，给国外供货，学妹，10+k， +6个月年终奖。

2017-5.16
看起来9344的主频比9341高一点。
SoC: Atheros AR9341 rev 1
Clocks: CPU:535.000MHz, DDR:400.000MHz, AHB:200.000MHz, Ref:25.000MHz
SoC: Atheros AR9344 rev 2
Clocks: CPU:560.000MHz, DDR:450.000MHz, AHB:225.000MHz, Ref:40.000MHz

编译ath9.5 #cool 3看起来也加sudo apt install squashfs-tools
15:37 和俄罗斯客户交流，他希望下一代工业路由器需要双频wifi， 4个千兆网口。问到了ipv6和slaac这样的问题。

周湘理看起来有点空，让他先处理一下工业路由器的网页。

洛晓峰：问上海的轮船的拨号问题，姚国梁今天请假。认为已经拖了太久。

占永平 p21曾经出现过一次wifi不能连接的情况，当时以太网也是不能得到地址的。所以和刚刚生产的100台p21的情况不一样，说有5台wifi不能起来，但是重新参数初始化之后就可以了。

2017-5.15
16:49 貌似最新的vmave player 12.5 可以安装ubunt17了。原来的12.1在头几步那里会报个错误，已经不记得是什么错误了。
居然安装的是32位系统，还需要重新来过。

telnetd -l /bin/sh 这样运行的telnet，就不用密码就进入系统了。
riltek这个wifi有无数的工具，包括了auth, utility, wsc,wireless_tools.25等
auth目录中有auth和iwcontrol， 貌似和scan都没有关系
utility中有flash和webs，貌似和scan也没有关系
wireless_tools.25中有iwlist这个工具，原生的makefile中没有复制进去，复制了scanning第一次运行没有结果，第二次就系统挂起了，从usb连接的电脑上显示了trap状态。
wscd这个工具从命令上来看是给wps使用的。

李柱栋：
http://blog.csdn.net/cnmilan/article/details/38369519
这个网页解决adb shell 报没有权限的问题。

王伍：
要吴曦每周发出需要信可解决的问题。
要工业路由器加快完成vpn等，完成这个项目

汪光华：
上午陈良那边开始出现网页不能出来的情况，发现是realtime_tx_xxxx什么值总是在报错。查看调用的地方，发现sizeof一个指针，那么就只取4个。修改gohead后，暂时没有报网页刷不出来的情况。不过也不对，已经做了保护，当取出来的值长度大于传入的值，那么只会复制相应的字节数出去，不应有错。

陈富军：
修改uboot的难度太大了。

2017-5.12
17:33 曾小星 问湖北联通减成本方案。就是中兴的方案。
17:07 毛浩明 问是否有中继的功能，原来的cpe是有的。他卖掉了200个使用cpe改成ap的小cpe, 现在还有200个的订单意向。
王伍 marval方案：
cat 6 只是在marval和 gct之间选择。
gct： 没有volte，需要买软件，费用在上百万。gct本身还要$2-3万，套片价格也到了$16. 优点是支持cat 5 6 7
marval： 报价$12,可能谈到$10
   但marval这个部门可能被卖掉，而且传言已经和asr谈好了。当前这个部门还有3-400人。
   asr这个公司几年就烧掉了几个亿。
   只支持4*2mimo。
cat 6 : 下行载波聚合
cat 7 : 上下行载波聚合
cat 5: 4*4mimo

2017-5.11
晚上发现网页无法刷出来，开始应该使用那个finder来抓包看看的。

9:48 姚国梁： 查看一下其他的应用，是否也编译了cmdlib但没有修改为so方式。
10:51  python的循环打印
for i in range(1300,1500) : print i

廖媛
尼日利亚 m60
1 bridge 2 ipsec 3 tr069+ssl

叶京平
南非p21 加wan口功能。

2017-5.10
程洪卫
关于5.20在海贝湾的研发大会，计划早上9：30出发，9点集合，中午左右到，吃饭，下午到晚上自由活动，晚上吃烧烤。21号早上留给李总，下午从1点半到4点留给研发部。
对于新人，要实时关注，合适不合适，及时换。看有没有进取心，有没有成长的愿望。


sudo apt-get install libgnomeui-dev
gcc -shared -o libsublime-imfix.so sublime_imfix.c  `pkg-config --libs --cflags gtk+-2.0` -fPIC
LD_PRELOAD=./libsublime-imfix.so subl
終於可以輸入中文了。
http://blog.csdn.net/cywosp/article/details/32350899
还要使用搜狗的输入法，这个输入法为什么输入框总是在屏幕的左下角？

2017-5.9
what? I could not input chinese in sublime text3. how bad.

2017-5.8
总是有人不写日志，给王伍发了个消息
通知：4月开始，日志每月少于15篇的，绩效直接在0.8以下，5月开始，由于日志少绩效低的，扣绩效不设豁免期，发放时直接扣除。6月开始，连续3个月日志少于15篇的，降岗降职。
他倒是没有什么意见。颜斌这边硬件基本上没有人写。如果这样发，不知道有没有麻烦。

2017-5.7
ARP daemon support的解释在：
http://linux.chinaunix.net/techdoc/net/2005/03/21/921746.shtml
不过去掉这个功能也只减少了内核3个字节的大小。

nfs:
sudo apt-get install nfs-kernel-server
sudo vi /etc/exports
/opt/work *(rw,sync,no_root_squash,no_subtree_check)
sudo /etc/init.d/rpcbind restart
sudo /etc/init.d/nfs-kernel-server restart
mkdir -p /tmp/1
mount -t nfs 192.168.254.50:/opt/work/ /tmp/1 --nolock

2017-5.3
任银善：
1 按键
2 灯
3 tf 卡
4 usb支持u盘
5 usb->serial
6 uboot   ok
7 16m的flash分区划分：考虑uboot到128k，去掉uboot-env区，内核1.5m，data区1m，art 64k，这样文件系统区能到13m，应该可以满足以后的需要。
8 网页升级修正
9 网页5.8g信息设置，查看
10 usb信息查看
11 校准操作流程

2017-5.2
tftp -g 10.8.0.100 -l ag71xx.ko
rmmod ag71xx
insmod ag71xx.ko
ifconfig eth0 up
brctl addif br0 eth0
brctl addif br0 eth1

余小虎去斯里兰卡的工作：
1 p11s 兰卡贝尔的gre测试跟进工作
2 dialog m60
  a 问题机器的跟进，dialog只发了不到6k的机器，只发了200台左右到客户那里，共有9台出现各种问题。通过查找生产imei号，其中6台机器是前面斯里兰卡电信的尾机。这样的尾机有200台。当前还无法确实是否是尾机造成的。
  b 培训
  c 多ssid和多nat 的验证
  d 外置天线测试
  e 合并moden后的验证
3 dialog p28
  a 测试跟进
  b 外置天线测试
 4 斯里兰卡电信
  a m60 p28  r12三个产品招标
  b 前期m60出货遗留的两个问题：ssid密码显示问题，斯里兰卡电信有提出不能在话机上看到wlan密码，一个是kandy的信号弱。

2017-4-27
为什么我的电脑tftp不能默认启动了？
sudo service tftpd-hpa restart

2017-4-25
board=AP147 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot-env),14528k(rootfs),1472k(kernel),64k(art),16000k@0x50000(firmware) rootfstype=squashfs,jffs2 noinitrd crashkernel=10M@20M


2017-4-22
arm编译出来的东西还是比mips要小好多：
jian@jian-OptiPlex-9020:~/work/ath9.5$ ll rootfs-tozedap-cp_ap123.optbuild/bin/update
-rwxrwxr-x 1 jian jian 6540  4月 15 21:59 rootfs-tozedap-cp_ap123.optbuild/bin/update*
jian@jian-OptiPlex-9020:~/work/zte7520_ap$ ll ./linux_plat/base/linux/romfs/bin/update
-rwxrwxr-x 1 jian jian 5048  4月 22 15:53 ./linux_plat/base/linux/romfs/bin/update*
居然能小15k。

2017-4-21
MemFree:            6708 kB MemAvailable:       9356 kB Cached:            10988 kB
MemFree:            7544 kB MemAvailable:       9500 kB Cached:            10144 kB
MemFree:            6640 kB MemAvailable:       8628 kB Cached:            10172 kB
MemFree:            7184 kB MemAvailable:       8948 kB Cached:             9816 kB
MemFree:            7044 kB MemAvailable:       8856 kB Cached:             9844 kB
MemFree:            6996 kB MemAvailable:       8816 kB Cached:             9848 kB
MemFree:            6976 kB MemAvailable:       8796 kB Cached:             9848 kB
MemFree:            7096 kB MemAvailable:       8920 kB Cached:             9856 kB
MemFree:            7084 kB MemAvailable:       8912 kB Cached:             9860 kB
MemFree:            7188 kB MemAvailable:       8956 kB Cached:             9804 kB
MemFree:            7096 kB MemAvailable:       8904 kB Cached:             9828 kB

2017-4-20
中兴中 HOST_NCPU=1 可以指定单cpu编译。

2017-4-19
        src/xlat/gen.sh src/xlat/blkpg_ops.in src/xlat/blkpg_ops.h
        src/xlat/gen.sh src/xlat/bpf_commands.in src/xlat/bpf_commands.h
        src/xlat/gen.sh src/xlat/bpf_map_types.in src/xlat/bpf_map_types.h
        src/xlat/gen.sh src/xlat/bpf_prog_types.in src/xlat/bpf_prog_types.h
        src/xlat/gen.sh src/xlat/bpf_map_update_elem_flags.in src/xlat/bpf_map_update_elem_flags.h
        src/xlat/gen.sh src/xlat/cap_mask0.in src/xlat/cap_mask0.h
        src/xlat/gen.sh src/xlat/cap_mask1.in src/xlat/cap_mask1.h
        src/xlat/gen.sh src/xlat/cap_version.in src/xlat/cap_version.h
        src/xlat/gen.sh src/xlat/clone_flags.in src/xlat/clone_flags.h
        src/xlat/gen.sh src/xlat/advise.in src/xlat/advise.h
        src/xlat/gen.sh src/xlat/at_flags.in src/xlat/at_flags.h
        src/xlat/gen.sh src/xlat/addrfams.in src/xlat/addrfams.h
        src/xlat/gen.sh src/xlat/af_packet_types.in src/xlat/af_packet_types.h
        src/xlat/gen.sh src/xlat/cap.in src/xlat/cap.h
        src/xlat/gen.sh src/xlat/adjtimex_modes.in src/xlat/adjtimex_modes.h
        src/xlat/gen.sh src/xlat/adjtimex_status.in src/xlat/adjtimex_status.h
        src/xlat/gen.sh src/xlat/audit_arch.in src/xlat/audit_arch.h



zte_libs/libnl_2这个目录看起来是完全重新编译了的。          ok
zte_apps/auth/src/dlisten里面也是做了clean操作。              ok
zte_apps/c-ares 								     ok
zte_web_util.c 这些文件警告太多。
/zte_apps/miniupnpd_linux               				     应该没有问题。
zte_apps/netdog/refcode/net_test		                             ok
zte_apps/netpcap                                                                 ok
zte_apps/zte_arp_proxy                                                        ok
zte_apps/zte_fota/zte_topsw_dmapp                                     应该没有问题。
zte_apps/zte_ipv6_addr_conver                                             ok
zte_apps/zte_ipv6_slaac                                                     ok
zte_apps/zte_ndp                                                         ok
zte_apps/zte_router                                                       ok
zte_apps/zte_topsw_qrcode                                        ok

lib的先记录下来：
	if [ -e libnl-2.0/Makefile ] ; then \
		echo libnl-2.0 configure seemed ok; \
	else \
	(cd libnl-2.0 && cp configure.linux configure && CFLAGS="-O2 -g -fomit-frame-pointer -pipe -msoft-float -fno-common -fno-builtin -Wall -DEMBED  -Dlinux -D__linux__ -Dunix " ./configure $(CONFIGURE_OPTS) $(CONFOPTS) --host=arm-linux --build=i686-pc-linux-gnu --target=arm-linux --enable-static --disable-shared ) ;\
	fi

为什么strace编译不了了：
-all: confcode
-       cd ./src && sh ./configure --host=arm-linux $(CONFIGURE_OPTS) $(CONFOPTS)
+all:
+       if [ -e ./src/Makefile ] ; then \
+               echo strace seemed configured.;\
+       else \
+               cd ./src && sh ./configure --host=arm-linux $(CONFIGURE_OPTS) $(CONFOPTS); \
+       fi
        $(MAKE) -C src

 confcode:
        -rm -rf *.o ./.deps

 clean:
-       -rm -rf ./src/strace ./src/*.o ./src/.deps
+       -rm -rf ./src/strace ./src/*.o ./src/.deps
+       -cat .gitignore | xargs rm -rf



2017-4-16
编译iptables 1.16.1
sudo apt-get install libmnl-dev

在ubuntu16 server上编译工业路由器的程序，编译到iptables的时候报
fatal error: libnfnetlink/libnfnetlink.h: No such file or directory
这样的错误。先留着吧。

我的机器上的tftp server居然不支持-r里面的路径，总是说文件未找到。

umount /fotaupdate
ubirmvol /dev/ubi2 -n 0

ubiattach /dev/ubi_ctrl -m 18
 ubimkvol /dev/ubi2  -s 55000000  -N fota_bui
mount -t ubifs ubi2_0 /fotaupdate/

/fotaupdate/busybox tar xzvf /fotaupdate/rootfs.tgz -C /
tftp -g 192.168.0.50 -l securefs.tgz
mount -o remount w /securefs
tar xzvf securefs.tgz -C /
update ap_cpuap.bin /dev/mtd12

开始只有3m的free内存，执行一下
echo 3 > /proc/sys/vm/drop_caches
就变成20m了。

程洪卫
5.20准备开研发大会， 李总讲企业文化，对研发的希望，要求。
过程： 谁来讲，讲什么，设计理念，怎么做。
碰到的问题，案例，下一步如何
去海外支持的分享

2017-4-15
新安装的ubuntu1610server的ssh总是无法登录，报22端口被拒接，重启虚拟机，重启虚拟机程序貌似都不行。

2017-4-8

11185快递：9974465912026 不知道是谁的东西，哦有可能是茶叶。
p21上联芯的模块吧：
行   								不行
10.150.239.124					10.79.224.41
10.29.182.46						10.92.218.43
10.21.13.132						10.31.237.99
10.172.131.151
10.3.61.107

用电脑吧：
行   								不行
10.101.107.127                               10.75.32.99
-							10.8.179.255
-							10.61.126.40


用工业路由器来测试吧：
c1的模块：
不行  1
行      1  2  3 4 5  6
记录ip吧：
行   								不行
10.9.14.184						10.13.69.237
10.7.188.139
10.41.37.102
10.6.254.189

可以不行10.100.47.23310.25.200.24510.146.69.16910.60.224.5210.1.122.1710.26.67.21810.26.79.7410.60.186.10310.159.127.199
换个模块吧
行   								不行
10.17.75.38                                            10.2.107.151
10.172.22.212						10.59.47.86
10.152.202.34						10.61.59.118
10.161.102.219					10.45.219.184
10.221.132.101


这样看工业路由器的版本貌似正常。
usb0      Link encap:Ethernet  HWaddr B2:D9:7A:D1:9E:C2
          inet addr:10.160.216.88  Bcast:10.160.216.95  Mask:255.255.255.240

cat /proc/version
Linux version 3.3.8- (zy@zy-OptiPlex-9020) (gcc version 4.3.3 (GCC) ) #92 Wed Mar 29 11:43:05 CST 2017
 # iptables -S
-P INPUT ACCEPT
-P FORWARD ACCEPT
-P OUTPUT ACCEPT
/tmp # iptables -S -t nat
-P PREROUTING ACCEPT
-P INPUT ACCEPT
-P OUTPUT ACCEPT
-P POSTROUTING ACCEPT
-A PREROUTING -i br0 -p udp -m udp --dport 5060 -j REDIRECT
-A POSTROUTING -o usb0 -j MASQUERADE

工业路由器使用宽翼模块：
/tmp # ./busybox traceroute -I www.163.com
traceroute to www.163.com (112.51.121.164), 30 hops max, 38 byte packets
 1  *  *  *
 2  *  *  *
 3  *  *  *
 4  *  *  *
 5  183.235.32.133 (183.235.32.133)  42.088 ms  22.033 ms  19.157 ms
 6  *  *  *
 7  221.183.18.217 (221.183.18.217)  40.263 ms  24.643 ms  25.926 ms
 8  *  *  *
 9  *  *  *
10  112.5.209.2 (112.5.209.2)  44.655 ms  30.321 ms  34.221 ms
11  *  *  *
12  183.252.196.52 (183.252.196.52)  45.431 ms  31.151 ms  34.833 ms
13  112.51.121.164 (112.51.121.164)  34.680 ms  33.753 ms  34.801 ms
/tmp # ./busybox traceroute  www.163.com
traceroute to www.163.com (112.51.121.164), 30 hops max, 38 byte packets
 1  *  *  *
 2  *  *  *
 3  *  *  *
 4  *  *  *
 5  183.235.32.133 (183.235.32.133)  43.120 ms  27.951 ms  22.489 ms
 6  211.136.240.205 (211.136.240.205)  21.373 ms  211.136.240.201 (211.136.240.201)  18.001 ms  211.136.240.205 (211.136.240.205)  17.924 ms
 7  221.183.38.141 (221.183.38.141)  24.634 ms  221.183.18.217 (221.183.18.217)  22.173 ms  221.183.12.117 (221.183.12.117)  23.554 ms
 8  *  221.176.16.133 (221.176.16.133)  45.342 ms  *
 9  221.183.27.230 (221.183.27.230)  44.268 ms  *  *
10  112.5.209.2 (112.5.209.2)  47.981 ms  31.370 ms  *
11  *  *  *
12  183.252.196.52 (183.252.196.52)  40.083 ms  34.790 ms  40.273 ms
13  112.51.121.164 (112.51.121.164)  34.839 ms  31.263 ms  34.809 ms

工业路由器上使用联芯的模块：
 ./busybox traceroute -I www.163.com
traceroute to www.163.com (112.51.121.165), 30 hops max, 38 byte packets
 1  *  *  *
 2  *  *  *
 3  *  *  *
 4  *  *  *
 5  183.235.32.101 (183.235.32.101)  52.618 ms  38.832 ms  39.799 ms
 6  211.136.240.197 (211.136.240.197)  39.809 ms  *  *
 7  221.183.19.233 (221.183.19.233)  56.656 ms  45.582 ms  49.939 ms
 8  *  *  *
 9  *  *  *
10  *  *  *
11  112.5.209.2 (112.5.209.2)  99.758 ms  65.345 ms  69.810 ms
12  *  *  *
13  183.252.196.52 (183.252.196.52)  75.398 ms  68.775 ms  69.839 ms
14  112.51.121.165 (112.51.121.165)  69.758 ms  64.691 ms  69.673 ms


2017-4-7
在仓中看起来没有的文件：
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/securefs/
看起来这些文件在 ./linux_plat/base/linux/user/zte_apps/zte_webui中
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/user/gdb/gdb/ada-exp.c 若干个
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/user/Kconfig
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/user/Makefile
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/vendors/ZXIC/zx297520v2/config.linux
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/vendors/ZXIC/zx297520v2/config.vendor

usbproxy中的文件确实有区别：
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/linux-3.4.x/drivers/staging/usbproxy/Kconfig
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/linux-3.4.x/drivers/staging/usbproxy/Makefile
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/linux-3.4.x/drivers/staging/usbproxy/cp_log_drv.c
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/linux-3.4.x/drivers/staging/usbproxy/f_adb.c
ZMPSDK7520V2V1.0.4B02P02_20170329/linux_plat/base/linux/linux-3.4.x/drivers/staging/usbproxy/ramdump_drv.c

2017-4-5
湖北联通p10p开箱10台有2台无配置问题：
同样的程序已经出过9000台，以前的设备没有报这样严重的问题。湖北联通的程序是去年8月发行的，一直没有做任何修改。wifi上已经去掉了prot-mode和软件强制提高功率。

2017-3-31
为什么要用git checkout -b sip-alg origin/sip-alg 这样来跟踪远程分支呢？

 insmod ip_gre.ko
 ip tunnel add tunnel0 mode gre remote 192.168.1.10  local 192.168.1.220  ttl 255
 ip link set tunnel0 up
 ip addr add  192.168.33.1 dev tunnel0
 ip route add 192.168.33.0/24 dev tunnel0

sudo ip tunnel add tunnel0 mode gre remote 192.168.1.220 local 192.168.1.10  ttl 255
sudo ip link set tunnel0 up
sudo ip addr add 192.168.33.2 dev tunnel0
sudo ip route add 192.168.33.0/24 dev tunnel0

考虑去掉的wlan参数：
export AH_SUPPORT_EEPROM_AR9287=1
export NUM_TX_CHAINS=2
export SA_NUMANT_PERCHAIN=2
export SA_11N_SUPPORT=1
export ATH_SUPPORT_TxBF=1

网易的这个云笔记体验也太差了，动不动就停止不动若干秒。

set ipaddr 10.8.0.33 && set serverip 10.8.0.100
tftp 0x80060000 u-boot.bin
好像不管什么样的地址，使用go都会直接复位。

2017-3-30
新的zte7520使用了ubi的文件系统，在build中增加了工具，所以要删除原来的build重新下载一个。
rm linux_plat/base/build -r

2017-3-29
这样的简历
１９８１－－１９８５东南大学无线电工程系。
１９８５－－１９８８北京理工大学电子工程系。南京十四所研究生。

１９８８－－１９９１南京十四所４０４室
１９９１－－１９９５南京康奇电子技术公司
１９９５－－１９９６巨龙通信公司南京办事处
１９９６－－１９９７新地网络公司南京办事处
１９９７－－１９９８南京光阳通信公司
１９９８－－１９９９南京自动化设备三厂
１９９９－－２０００江苏宏图高科技公司
２０００－－２００１中科院紫金山天文台华福数字视频公司
2001-2002苏源高科技公司
2002年9月-2002年12月南京西三艾电子公司
2002-2003年 南京汇翔自动化公司
2003-2003年8月金宁星拓电源设备研究所
2003年8月-2003年10月 科融数据系统有限公司
2003年10月-2004年2月 钢加远程数据系统有限公司
2004年8月--2005年8月苏州华硕电脑有限公司
2005年９月－2006年3月 上虞市胜昔信息科技有限公司
2006年4月-2006年7月北京正荣网际公司
2007年12月---2008年2月成都市佳灵电气制造有限公司
2008年2月---2009年12月十堰市华海达汽车安全技术有限公司
2010年1月---2010年11月北京固安信通铁路信号科技有限公司
2010年11月----2011年02月南京文采科技有限公司
2011年03月----2012年04月南京日新机电有限公司
2012年04月----2012年07月北京东方泰华投资有限公司
2012年07月-------2013年07月青岛日森机电有限公司
2013年07月-----2014年07月南京正銮电子有限公司 开发
2014 /7--2015 /7： 南京milink电子有限公司 （500-1000人）
2015 /7--2016 /11： 深圳维兴顺科技有限公司 （5-200人）

2017-3-28
周湘理
在公司认识了更多的人，学到更多的知识。
刚开始做网页的时候，太忙，吃力。当时是2月底，从伊朗的开始。
网页知识复杂在网页布局，javascript， JQuery封装。有点难。
何文秋： 还了解后端，能修改c语言
尚杰：c语言基础差，只能做前端。
以前是做控制电机的，使用C， fpga，stm32这样的cpu。其中fpga可以写逻辑，产生各种不同的波形，方波，三角波等。
还在arm9上做过控制面板，使用linux，qt系统。
对4g参数不了解，对网络了解有限。
其他公司的优势：管理措施多一些。强制性规定较多。比如要写周计划，每两周开会，每个人用几分钟说一下计划。每次一个多小时。
有其他培训，演讲，礼仪等。和领导见面沟通的机会多一些，经理会主动召集会议，主动关心进度。生产经常去，看看有什么问题。

2017-3-27
赵刚：
系统基于非openwrt的系统，比较底层，不太熟悉，升级等和openwrt都不同。
对fireware分区使用mtd命令，可能把必要的命令放到了tmp下。
主要认为做项目的交流比较少。
原来在成都瑞小博，技术氛围比较好，任务规划比较细，具体功能能细化出来，现做什么，后做什么，比较明确。
有完善的流程。
提交代码有code review过程。这个过程也是交流的过程。
这个公司固件4-5人，平台20多人以上。
在通则开始移植网页，很多东西不知道，没有文档，没有统一风格，标准。读状态都有若干种方式，配置，环境变量，tmp下的文件等。
希望对业务熟悉一些。希望基于openwrt系统开发。

jian@jian-OptiPlex-9020:~/work/zte7520_ap/apps/zte/common/apps$ find  . -name 'Makefile' | xargs cat | grep EXEC | grep =
EXEC = embms_data
EXEC    = fluxstat
EXEC    = sale_stat
EXEC = net_test
EXEC = igmpproxy
EXEC    += dhcp6c
EXEC 	+= dhcp6s
EXEC    = zte_tools_agent
EXEC = slictool
EXEC    = zte_blc
EXEC    = cfgnv_init
EXEC = tr069
EXEC = zte_router
EXEC = dnsmasq
EXEC    = zte_pcs
EXEC = clatd
EXEC    = zte_log_agent
EXEC = ipv6_addr_conver
EXEC = sntp
EXEC    = zte_rj45
EXEC    = at_cmd
EXEC = auto_connect
EXEC = zte_ipv6_slaac
EXEC    = nv
EXEC    = goahead
#EXEC = libwebuiwifi.a
#EXEC = libwebuinet.a
EXEC = hotplugnl
EXEC = eth_auto_connect
EXEC = nvserver
EXECUTABLES = testobsdrdr testpfpinhole
EXECUTABLES = testgetifstats
EXECUTABLES = testgetifstats testifacewatcher
EXECUTABLES = miniupnpd testupnpdescgen testgetifstats \
EXEC = zte_ipsec_proxy
EXEC    = at_main
EXEC    = zte_bip
EXEC = pc_server
EXEC = uart_proxy
EXEC = sd_hotplug
EXEC    = wl
EXEC = ccapp
EXEC    = embms_ctrl
EXEC = zte_ndp
EXEC = zte_arp_proxy
EXEC = zte_ipv6_addr_collect


2017-3-26
openwrt使用了#ifdef CONFIG_MTD_ROOTFS_ROOT_DEV

把那个padjffs2部分加载
mount -t jffs2 /dev/mtdblock2 /tmp/1
内容是存在的，但是为什么空间的容量有问题：
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 3.3M      3.3M         0 100% /
/dev/mtdblock2           56.0M      4.1M     51.9M   7% /tmp/1

set ipaddr 10.8.0.33 && set serverip 10.8.0.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-squashfs && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize

2017-3-25
这个东西好像没有使用：
ATH_SUPPORT_ICM=1
OL_ATH_SUPPORT_STATS

9341在3.3.8的内核中默认进行了端口隔离：
echo 10c 3e0000 > /proc/phys26/reg
echo 20c 3d0000 > /proc/phys26/reg
echo 30c 3b0000 > /proc/phys26/reg
echo 40c 370000 > /proc/phys26/reg
echo 50c 2f0000 > /proc/phys26/reg
echo 60c 1f0000 > /proc/phys26/reg


2017-3-24
9x07中snmp执行
 /usr/sbin/snmpd -Lsd -Lf /dev/null -p /var/run/snmpd.pid

./scripts/feeds update -a
接下来安装feeds包，只有安装之后，在make menuconfig的时候才能够对相关的配置进行修改：
http://www.cnblogs.com/rohens-hbg/articles/4969222.html

2017-3-23
mini_snmpd:
http://troglobit.com/mini-snmpd.html
https://github.com/troglobit/mini-snmpd/blob/master/README.develop
使用：
http://riceball.com/d/content/mini-howto-minisnmpd-small-snmpd-embedded-systems-openwrt
snmpwalk -v 1 -c public 192.168.0.1

2017-3-22
去掉了 ATH_SUPPORT_DFS
-rw-rw-r-- 1 jian jian   21704  3月 22 17:44 adf.ko
-rw-rw-r-- 1 jian jian   50844  3月 22 17:44 ag71xx.ko
-rw-rw-r-- 1 jian jian   11592  3月 22 17:44 asf.ko
-rw-rw-r-- 1 jian jian  332624  3月 22 17:44 ath_dev.ko
-rw-rw-r-- 1 jian jian   67828  3月 22 17:44 ath_dfs.ko
-rw-rw-r-- 1 jian jian  753748  3月 22 17:44 ath_hal.ko
-rw-rw-r-- 1 jian jian   22928  3月 22 17:44 ath_pktlog.ko
-rw-rw-r-- 1 jian jian   40616  3月 22 17:44 ath_rate_atheros.ko
-rw-rw-r-- 1 jian jian   13928  3月 22 17:44 hst_tx99.ko
-rw-rw-r-- 1 jian jian 1253880  3月 22 17:44 umac.ko
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4572      2404  66% /

2017-3-21
把修改了的文件列出来：
git status . | cut -c 14-  >my
cat my | xargs git checkout
cat my |xargs git rm
cat my >> .gitingore

2017-3-20
去掉ATH_SUPPORT_SPECTRAL
-rw-rw-r-- 1 jian jian   21704  3月 20 13:33 adf.ko
-rw-rw-r-- 1 jian jian   50844  3月 20 13:33 ag71xx.ko
-rw-rw-r-- 1 jian jian   11592  3月 20 13:33 asf.ko
-rw-rw-r-- 1 jian jian  337872  3月 20 13:33 ath_dev.ko
-rw-rw-r-- 1 jian jian   67828  3月 20 13:33 ath_dfs.ko
-rw-rw-r-- 1 jian jian  764664  3月 20 13:33 ath_hal.ko
-rw-rw-r-- 1 jian jian   22952  3月 20 13:33 ath_pktlog.ko
-rw-rw-r-- 1 jian jian   40616  3月 20 13:33 ath_rate_atheros.ko
-rw-rw-r-- 1 jian jian   40076  3月 20 13:33 ath_spectral.ko
-rw-rw-r-- 1 jian jian   13928  3月 20 13:33 hst_tx99.ko
-rw-rw-r-- 1 jian jian 1270656  3月 20 13:33 umac.ko
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4764      2212  68% /

/tzadmin/cgi-bin # df
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4824      2152  69% /
/tzadmin/cgi-bin # ls -l
-rwxrwxr-x    1 1000     normal      314860 Mar 20  2017 shakehand.cgi

web的shakehand改为使用so之后
/tzadmin/cgi-bin # df
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 6976      4816      2160  69% /
/tzadmin/cgi-bin # ls -l
-rwxrwxr-x    1 1000     normal      157980 Mar 20  2017 shakehand.cgi
如果一块是1k，那么省了8k吧。

2017-3-19
 tftp -g 10.8.0.100 -l /tmp/my.tar.gz -r my.tar.gz
tar zxvf /tmp/my.tar.gz

去掉hyfi
-rw-rw-r-- 1 jian jian   21704  3月 19 11:47 adf.ko
-rw-rw-r-- 1 jian jian   50844  3月 19 11:47 ag71xx.ko
-rw-rw-r-- 1 jian jian   11592  3月 19 11:47 asf.ko
-rw-rw-r-- 1 jian jian  344836  3月 19 11:47 ath_dev.ko
-rw-rw-r-- 1 jian jian   67828  3月 19 11:47 ath_dfs.ko
-rw-rw-r-- 1 jian jian  777392  3月 19 11:47 ath_hal.ko
-rw-rw-r-- 1 jian jian   22952  3月 19 11:47 ath_pktlog.ko
-rw-rw-r-- 1 jian jian   40616  3月 19 11:47 ath_rate_atheros.ko
-rw-rw-r-- 1 jian jian   40076  3月 19 11:47 ath_spectral.ko
-rw-rw-r-- 1 jian jian   13928  3月 19 11:47 hst_tx99.ko
-rw-rw-r-- 1 jian jian 1272460  3月 19 11:47 umac.ko

去掉wapi这个
-rw-rw-r-- 1 jian jian   21704  3月 19 11:18 adf.ko
-rw-rw-r-- 1 jian jian   50844  3月 19 11:18 ag71xx.ko
-rw-rw-r-- 1 jian jian   11592  3月 19 11:18 asf.ko
-rw-rw-r-- 1 jian jian  347240  3月 19 11:18 ath_dev.ko
-rw-rw-r-- 1 jian jian   67828  3月 19 11:18 ath_dfs.ko
-rw-rw-r-- 1 jian jian  777392  3月 19 11:18 ath_hal.ko
-rw-rw-r-- 1 jian jian   22952  3月 19 11:18 ath_pktlog.ko
-rw-rw-r-- 1 jian jian   40848  3月 19 11:18 ath_rate_atheros.ko
-rw-rw-r-- 1 jian jian   40076  3月 19 11:18 ath_spectral.ko
-rw-rw-r-- 1 jian jian   13928  3月 19 11:18 hst_tx99.ko
-rw-rw-r-- 1 jian jian 1292648  3月 19 11:18 umac.ko

原有文件大小
-rw-rw-r-- 1 jian jian   21704  3月 19 10:04 adf.ko
-rw-rw-r-- 1 jian jian   50841  3月 19 10:23 ag71xx.ko
-rw-rw-r-- 1 jian jian   11592  3月 19 10:04 asf.ko
-rw-rw-r-- 1 jian jian  347352  3月 19 10:04 ath_dev.ko
-rw-rw-r-- 1 jian jian   67828  3月 19 10:04 ath_dfs.ko
-rw-rw-r-- 1 jian jian  779664  3月 19 10:04 ath_hal.ko
-rw-rw-r-- 1 jian jian   22952  3月 19 10:04 ath_pktlog.ko
-rw-rw-r-- 1 jian jian   40848  3月 19 10:04 ath_rate_atheros.ko
-rw-rw-r-- 1 jian jian   40076  3月 19 10:04 ath_spectral.ko
-rw-rw-r-- 1 jian jian   13928  3月 19 10:04 hst_tx99.ko
-rw-rw-r-- 1 jian jian 1307668  3月 19 10:04 umac.ko

2017-3-18
那个升级错误居然是内核中的mtd错了，把内核扩大了些，问题是boot没有改，还是在同样的位置去启动，就不行了。

今天怎么dnsmasq 2.76不用修改任何东西就能编译通过了，奇怪的事情，原来谢世乐上传的时候总是编译不过。

 insmod ip_gre.ko
 ip tunnel add tunnel0 mode gre remote 10.8.0.100 local 10.8.0.103 ttl 255
 ip link set tunnel0 up
 ip addr add  192.168.33.1 dev tunnel0
 ip route add 192.168.33.0/24 dev tunnel0

2828  sudo ip tunnel add tunnel0 mode gre remote 10.8.0.103 local 10.8.0.100 ttl 255
 2831  sudo ip link set tunnel0 up
 2833  sudo ip addr add 192.168.33.2 dev tunnel0
 2835  sudo ip route add 192.168.33.0/24 dev tunnel0



cp ./net/ipv4/ip_gre.ko ~/tftpboot
cp ./net/ipv4/gre.ko ~/tftpboot
cp ./net/ipv6/ipv6.ko ~/tftpboot

strongswan使用mips-gcc4.3.3编译出的问题：
checking gmp.h version >= 4.1.4... no
configure: error: No usable gmp.h found!

 Symbol: ATH79_DEV_NAND [=y]                                                                                                    │
  │ Type  : boolean                                                                                                                │
  │   Selects: ATH79_NAND_CALDATA_FIXUP [=y]                                                                                       │
  │   Selected by: ATH79_MACH_AP135_DUAL [=y] && ATH79 [=y] || ATH79_MACH_CUS227 [=y] && ATH79 [=y] || ATH79_MACH_CUS531_NAND [=y] │
  │

Symbol: ATH79_MACH_AP135_DUAL [=y]                                                                                             │
  │ Type  : boolean                                                                                                                │
  │ Prompt: Atheros AP135 Dual reference board                                                                                     │
  │   Defined at arch/mips/ath79/Kconfig:98                                                                                        │
  │   Depends on: ATH79 [=y]                                                                                                       │
  │   Location:                                                                                                                    │
  │     -> Machine selection                                                                                                       │
  │       -> Atheros AR71XX/AR724X/AR913X machine selection

2017-3-17
为什么ap-cp改到qsdk版本网页升级不行了，网页执行了：
 update /tmp/vmlinux.lzma.uImage /dev/mtd2 > /tmp/updateboot
然后变成了：## Booting image at 9f6e0000 ...
Bad Magic Number

2017-3-14
好容易把cpe-df的软件改成了qsdk版本。为什么每次都这么复杂呢？
cpe-df qsdk版
set ipaddr 10.8.0.33 && set serverip 10.8.0.100
tftp 0x80060000 tozedcpe-df_ap123-jffs2 && erase 0x9f010000 +0x6d0000 && cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 vmlinux_ap123.lzma.uImage && erase 0x9f6e0000 +$filesize && cp.b $fileaddr 0x9f6e0000 $filesize

2017-3-13
ubuntu 运行32位程序
sudo apt-get install libc6:i386

libz.so.1: cannot open shared object file: No such file or directory

2017-3-11
tftp -g 10.8.0.100 -l ag71xx.ko
rmmod ag71xx
insmod ag71xx.ko
ifconfig eth0 up
brctl addif br0 eth0


2017-3-2
列出所有的用户和提交次数：
git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r

2017-3-1
找到所有的ko, 并复制到当前目录：find . -name '*.ko'  -exec cp  {} . \;

2017-2-25
终端颜色：
http://weakbrother.blog.163.com/blog/static/14067678120113125183337/

2017-2-23
使用：
Linux version 3.4.110 (jian@jian-OptiPlex-9020) (gcc version 4.7.2 (Buildroot 2013.02) ) #16 Wed Feb 22 18:08:26 CST 2017
tcp pc->cpe [  8]  0.0-10.1 sec   112 MBytes  93.3 Mbits/sec
tcp cpe->pc [  6]  0.0-10.0 sec   109 MBytes  91.4 Mbits/sec
udp pc->cpe [  3]  0.0-10.0 sec   114 MBytes  95.5 Mbits/sec  (-b 100M)
udp cpe->pc [  6]  0.0-10.0 sec   111 MBytes  93.2 Mbits/sec

Linux version 3.4.110 (zq@zq-ThinkPad-E450) (gcc version 4.7.2 (Buildroot 2013.02) ) #2 Wed Feb 22 10:30:56 CST 2017
tcp pc->cpe [  3]  0.0-10.1 sec  7.88 MBytes  6.53 Mbits/sec
tcp cpe->pc [  6]  0.0-10.1 sec  2.50 MBytes  2.07 Mbits/sec
udp pc->cpe [  3]  0.0-10.0 sec   114 MBytes  95.5 Mbits/sec
udp cpe-pc [  6]  0.0-10.0 sec  1.88 MBytes  1.58 Mbits/sec

2017-2-21
福建的ip从211.143.218.54,  211.143.218.35 211.143.218.108-122

2017-2-17
phy 0 reg =0x3100 	phy 1 reg =0x7849		phy 2 reg =0x243	phy 3 reg =0xc54
phy 4 reg =0x1e1	phy 5 reg =0x0	phy 6 reg =0x4	phy 7 reg =0x2001
phy 8 reg =0x0	phy 9 reg =0x0	phy 10 reg =0x0	phy 11 reg =0x0
phy 12 reg =0x0	phy 13 reg =0x0	phy 14 reg =0x0	phy 15 reg =0x0
phy 16 reg =0x2	phy 17 reg =0x700	phy 18 reg =0x6101	phy 19 reg =0x0
phy 20 reg =0x10	phy 21 reg =0x0	phy 22 reg =0x0	phy 23 reg =0x0
phy 24 reg =0x0	phy 25 reg =0x12	phy 26 reg =0x1249	phy 27 reg =0x12
phy 28 reg =0x1	phy 29 reg =0x182	phy 30 reg =0x0	phy 31 reg =0x1409

qsdk: uboot boot kernel ok.
adb shell mkdir /jian
adb push ./linux_plat/base/linux/user/busybox/busybox /jian/
adb shell chmod +x /jian/busybox

2017-2-16
adb push ./project/prj_cpe/bins/allbins/ap_cpuap.bin /tmp
adb push ./linux_plat/base/linux/user/updatesystem/update /tmp
adb shell cp /tmp/update /sbin
adb shell chmod +x /sbin/update
adb shell update /tmp/ap_cpuap.bin /dev/mtd10

2017-2-15
中兴平台上的fota分区还比较大，而且可以mount上来，作为升级使用。
mount -t jffs2 -o rw mtd:fotaupdate /tmp/1
这个是以前的kernel:
Linux (zx297510-A9) 3.4.110 #2 Wed Jan 4 13:48:29 CST 2017 armv7l GNU/Linux
使用update后，看来没有什么问题
Linux (zx297510-A9) 3.4.110 #2 Wed Feb 15 11:21:18 CST 2017 armv7l GNU/Linux

2017-2-14
zte7520的板子回来，第一个刷信可的程序貌似正常，第二个就没法启动了，从usb口上看，pc端总是显示两个trap口。

ccapp这个程序难道是控制slic的，里面又slic的消息。

zte7520中的nv set 后，nv save重新启动，设置的参数看起来没有保存。

Warning: nss-myhostname is not installed. Changing the local hostname might make it unresolveable. Please install nss-myhostname!
这个要安装：sudo apt-get install libnss-myhostname

看起来wifi也没有起来。

2017-2-13
赵刚 和李瑶一起，在pc上可以连接尼日利亚的tr069服务器了。还需要在板子上实现。

忙了3天，总算把ap-cp使用qsdk再次编译成功了，以太网部分的eth0和eth1也出来了，可以ping通了，那么还有其他的扩展的部分还不知道怎么做。编译上去的u11的以太网驱动报错：phy not found!

使用mount -t debugfs none /tmp/1可以把debugfs建立起来，不过看起来里面的东西不多。

任银善手上的工作：
1 巴西openwrt 9531, 拨号需要加容错
2 9531 lsdk版本 性能测试
3 9531+9887双频， 5.8g感觉还有不正常
4 vpn
5 4018 已经编译成功
6 32m 的双系统

工业路由器在测试中会出现概率性的启动后完全

2017-2-10
grep -n '\.$' pp     //小数点是特殊字符 需要用\进行转义

黄武 问p21生产能否和m60一样检查天线是否扣好。

任银善 这个2.4g+5.8g的机器修改了mac结果好像校准的内容后移动了一个字节，所以看到5.8g的txpower是off，这也是头一次看到。也没有搞过ipsec，但原来的公司有人做过。

早上华润的商务人员来了，希望尽快完成测试。

2017-2-9
好像非常忙的样子。
首先是李瑶 若干个产品都要改网页，当前已经成为阻碍节点。他终于愿意招一个人，只要愿意做网页就好了。
廖媛 尼日利亚的p21还差ssl方式的tr069, voip。

2017-2-7
zte为什么telnet进去速度响应非常慢，而使用adb则看起来是正常的。

2017-2-6
菲律宾使用的是一个叫做wifi sweetspot的软件进行测速，这个软件直接发送udp包，不需要其他软件支持，连接wifi后即可使用。使用我的华为手机一直平稳，而使用占永平的手机就会明显的有起伏的现象。如果农宽cpe改为ap使用，那么看起来是平稳的。

年前的5.8g cpe报的不好用的问题是距离远了就不行，原因还是天线的问题。

zte7520以前的记录：
mmi模块的主要功能对不同的业务进行lcd或lde显示，lde是什么？
mmi存在对关机充电的支持。
已经存在恢复出厂的实现
adb看起来一定是通过usb来实现的
busybox中，没有dmesg和uptime这些指令。
存在nv这个指令，nv get telnted_enable
atserver的at log在/etc_rw/config/satlog这个文件中，还有一个ratlog不知道是谁发的。

海外会议。


2017-1-22
上午王伍 白俊剑 等说m60相关产品后面的做的东西。

还是换一个本地的笔记吧，先用tomboy这个ubuntu自带的用着吧，其他都开始收费了。
折腾了半天，居然没有办法在win7上运行，算了，不能就不能吧。

2017-1-20
这次年度的汇报本来我准备多汇报一点的，但是通知出来后发现研发的汇报时间被减少了不少，真是人生不如意，十有八九。我这里不是抱怨，下一次也不用增加时间，而是以这个作为一个计划不如变化的例子。

2017-1-19
p21上的开机过一段时间天线检测错误居然是wifi驱动中ar9300Reset这个函数里面对这个gpio直接进行了操作。怎么会有这样的事情发生？
可以使用dd命令直接把iso文件写入u盘，简单的方法，不用找各种软件了。
http://www.veryhuo.com/a/view/80220.html

2017-1-18
任银善 还在编译wlan_10.4，有个奇怪的define，总是报没有定义，应该是某些配置的问题。在我这里试试，cool 5是编译成功的，原来编译的是v10的，而不是v10_4的无线驱动。
工业路由器当前报每周有3-4台安装的机器不能使用的情况。
王伍重新写了一个i2c的程序，开始没有加延时，后来读寄存器有问题，应该是gpio的读法有问题
苑德强 tplink也在做海外市场，巴西一半的路由器被它占领。tp的质量其实不算完美，但是管理上应该有独到的地方。他举了个例子，有客户需要生产后立即得到发货的产品的sn号，tp可以立即给出，而他上个公司，动用了好多人力，一个个去扫描sn码，费了非常大的力气。

赵刚 openwrt上的openssl比较小，不过也有1.5m
占永平 工业路由器断电48次也出现了不能ping到的情况，重启正常。要接串口看了。

p10刷工业路由器qsdk程序
set ipaddr 10.8.0.33 && set serverip 10.8.0.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedap-router_4g_industry_ap123-squashfs && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=squanshfs ro init=/sbin/init mtdparts=spi0.0:64k(u-boot),6848k(rootfs),1152k(uImage),64k(mib0),64k(ART) machtype=DB120"

2017-1-17
赵刚 可以使用在tr069中增加openssl的库了，但是openssl非常大，不是要裁减，就是要换库。

2017-1-16
下午把原来的以太网驱动在3.3.8下编译过去。

早上那个9531的机器出现不能连接wifi的问题，telnet进去发现系统响应也很慢。还是那个问题，ubusd已经无法运行了，导致hostapd无法运行，所以wifi能搜索到，但是不能连接。另外log中保存了dmesg.log这个文件，非常大，有19m，删除它以后，系统看起来响应没有那么慢了。对于tftp不能上传创建文件的事情，使用那个tftp-hpa，进行配置后，就可以了。参考这个网页：http://wiki.ubuntu.com.cn/Tftpd-hpa
当前使用的配置文件：
/etc/default$ cat tftpd-hpa
TFTP_USERNAME="tftp"
TFTP_DIRECTORY="/var/lib/tftpboot"
TFTP_ADDRESS="0.0.0.0:69"
#TFTP_ADDRESS="[::]:69"
#TFTP_OPTIONS="--secure"
TFTP_OPTIONS="-l -c -s"

2017-1-12
郑荣俊 河南人。从前在一个做后视镜的公司，主要做单片机的工作。

2017-1-9
上午王伍催着把9250分配下去，找来张勇和周湘理简单说了一下。
电梯里面的工业路由器存在拨号程序挂掉的情况，这样就有运行了一周多后不能上网的情况。先做一个容错吧。
把qsdk2.9中的nart编译成一个整个的文件看起来还比较繁琐，还是使用原来的方式吧。做makefile的时候跳过那些作为链接的so文件。
单总召开会议讨论南美和菲律宾的事情。

2017-1-6
lc1860这个仓的内核每次都会完全重新编译了。
王伍：7520是个优先级最高的项目。
7520编译boot也没有什么问题。
rdesktop 增加-x 0x80这个参数，那么字体就不会发虚了。这个被称为user experience level
使用rdesktop有个好处是窗口大小不变，这样避免了virtualbox窗口变化时，thebat跟着调整，每次都要拉，比较麻烦。
任赢善 搞定了校准。9341的qsdk驱动移植基本没有难点了。下面就要把p21的改成这个程序。
git commit --amend 可以修改最后一次 commit

2017-1-5


白俊剑 还是放周湘理来做7520的网页部分。

下午折腾了半天的虚拟机，试图安装一个64的win7，直接上win7 64位sp1的版本，出现了那个寻找驱动程序的界面就不走了。查找是说使用u盘安装才会有这样的错误。安装ghost版，选择第一项立即停止响应了。还是安装ghost版，先进入pe系统，然后选择ghost，这样就安装成功了。里面大量的各种软件，可以卸载。但是���页永远都在2345那个，算了，直接删除吧。受不了了。
主要是昨天开启了一次win7虚拟机器之后，xp就不识别那个1t的硬盘了。

Shell脚本中$0、$?、$!等的意义
http://www.sijitao.net/1613.html
$$
Shell本身的PID（ProcessID）
$!
Shell最后运行的后台Process的PID
$?
最后运行的命令的结束代码（返回值）
$-
使用Set命令设定的Flag一览
$*
所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
$@
所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
$#
添加到Shell的参数个数
$0
Shell本身的文件名
$1～$n
添加到Shell的各参数值。$1是第1参数、$2是第2参数…。

7520可以上网，但是看起来pc上无法得到ipv6的地址。貌似也没有radvd程序。
按照这个文章的修改，也不能使用linux下的adb来连接7520
http://wyoojune.blog.163.com/blog/static/57093325201452753323250/

2017-1-4

信可的成伟平过来，试图在虚拟机中使用刷机程序，看起来是无法成功的，直接使用笔记本才能成功。系统中adbd已经在运行。是不是要在9341上也移植一个看看，这样即使没有网络地址的情况下，是不是也能进入系统。如何单独编译某个模块，显然他们还没有折腾过。还不能在adb中直接发送at指令。后来何伟和王伍也过来，说的主要是升级的事情。不做差分，fota，只做全包升级。
对于存在大量空目录的系统，先这样折腾一下再git add, 这些空目录就保存下来了。
find . -type d -empty -exec touch {}/.gitignore \;

2017-1-3
16:48
王伍 说中兴的目录很有借鉴，apps里面是各种程序。这个都是这样做的啊。
中兴的编译貌似没有碰到什么问题，直接过了。
中兴的内核居然已经把其他的arch删除了，比较好。

15:32
git for windows 2.11以后的版本就不再支持xp系统了，只能下载一个2.10版本的用着了。

14:58
来给郑荣俊分配git权限吧。

13:56
看起来如果在linux下操作另外挂载的那个磁盘，在linux下创建的文件，在windows下是没有看见的。如果在linux弹出设备，再重新挂载，那么那些文件也就不存在了。总感觉这样做，同样一块硬盘，变成了两个独立的系统。

11：56
好像好忙碌的样子，其实也没有。

刘云 苗立双 刘咏辉 徐钢雄 华域设备启动有概率不能起来的情况：当前使用华域本身的程序，无论什么硬件都没有问题，使用通则的软件，使用华域的底板没有问题，使用通则的底板就可能会出现不启动的情况。

昨天下午林小珊还打电话来问新同事坐哪里。
2016-12-29
123上面的几个编译原来的lsdk9.2的编译器的包也是错的。

2016-12-28
8:48 123上面的gcc-4.3.3还是错的。是我上传的p11-gcc.tar.gz是错的，没有修改。
8:30 当前ath9.5仓中的json-c无法编译。

2016-12-27
sudo dpkg-reconfigure wireshark-common
sudo usermod -a -G wireshark $USER

删除这两个转发吧，还没有删除：
1 http2 8080-8080 8080-8080 192.168.1.197
2 1450 1450-1450 1450-1450 192.168.1.197

2016-12-26
15:04  qemu的configure报这样的错误：glib-2.22 gthread-2.0 is required to compile QEMU
这样： sudo apt-get install libglib2.0-dev

14:00 林小珊 说赵刚中午一个人挺可怜的。
14:37 查看了一下22上的微机登记，好多已经改变了。各种机器还存在，更换了ip继续在内网中使用。
14:48 为什么vmplayer每次都要重新编译些东西呢？


p11s也出现了某些卡不能拨号的问题。
linux 下的小狼毫为什么引入词典后没有任何变化呢，以前输入的名字都没有出现。
赵刚来入职了，颜斌说还是非常明显的。

2016-12-25
在ubuntu16下不能编译的qsdk3中的tools，可以在其makefile中增加：
HOST_CFLAGS += -std=gnu89
来解决

禁用GSSAPIAuthentication可以加快ssh的登陆
https://linux.cn/article-5851-1-rel.html

2016-12-24
昨天那个win7的虚拟机firefox又不能运行了，出现了那个什么could not load xpdom? 问题。重新安装了一个xp，发现那个passkeeper又能运行了。那么就用xp吧。而印象笔记又不能运行了。现在换了一个leanote这样的工具，能够直接导入原来的笔记，就是所有的笔记全到在一个地方了。这个笔记的有linux版本，这点比较好，而且默认笔记在只读状态，不用担心原来的笔记不小心删掉某些字符。搜索不是特别方便，没有在有搜索框的情况下加亮搜索内容。

xp下重新下载了一个sumatrapdf，这个比原来的foxit要小很多了。

2016-12-23
陈玉 离菲律宾出货还有1个半月的事件，有可能改成工业路由器的版本进行出货。

2016-12-17
./lib
./lib/valgrind
./lib/valgrind/vgpreload_core-mips32-linux.so
./lib/valgrind/default.supp
./lib/valgrind/memcheck-mips32-linux
./bin
./bin/valgrind

configure.ac:4015: error: required file 'valgrind.spec.in' not found
configure.ac:4015: error: required file 'valgrind.pc.in' not found
configure.ac:4015: error: required file 'glibc-2.X.supp.in' not found
configure.ac:4015: error: required file 'drd/scripts/download-and-build-splash2.in' not found
configure.ac:4015: error: required file 'cachegrind/cg_annotate.in' not found
configure.ac:4015: error: required file 'cachegrind/cg_diff.in' not found
configure.ac:4015: error: required file 'callgrind/callgrind_annotate.in' not found
configure.ac:4015: error: required file 'callgrind/callgrind_control.in' not found
configure.ac:4103: error: required file 'coregrind/link_tool_exe_linux.in' not found
configure.ac:4105: error: required file 'coregrind/link_tool_exe_darwin.in' not found
configure.ac:4107: error: required file 'coregrind/link_tool_exe_solaris.in' not found
configure.ac:4015: error: required file 'massif/ms_print.in' not found
configure.ac:4015: error: required file 'perf/vg_perf.in' not found
configure.ac:4015: error: required file 'tests/vg_regtest.in' not found

2016-12-16
王伍
信可模块：1 moden的版本，不同频段如何区分，不能升级错误。
		2 基线版本如何对接
		3 wifi使用我们的pa
		4 使用单口phy, 不加switch.

2016-12-15
qsdk3使用外部编译器e2fsprogs这个东西又报rpath这样的错误，改成cc中的1.42.12试试。
.codeaurora.org这个网站各种慢啊。
在openwrt_cc这个仓里面的下载成功了，再看看qsdk3。还是报一样的错误。
/usr/share/mips-gcc-4.6/staging_dir/bin/../lib/gcc/mips-openwrt-linux-uclibc/4.6.3/../../../../mips-openwrt-linux-uclibc/bin/ld: warning: libdl.so.0, needed by ../lib/libss.so, not found (try using -rpath or -rpath-link)
../lib/libss.so: undefined reference to `dlclose'
../lib/libss.so: undefined reference to `dlopen'
../lib/libss.so: undefined reference to `dlsym'
在/usr/share/mips-gcc-4.6/staging_dir/usr/lib软链接到lib，同样报错。
debugfs: $(DEBUG_OBJS) $(DEPLIBS)
        $(E) "  LD $@"
        $(Q) $(CC) $(ALL_LDFLAGS) -o debugfs $(DEBUG_OBJS) $(LIBS)



2016-12-13
好吧，再次用gcc-4.6来编译2.6.31的内核，还是停留在Staring kernel....
这使用gcc4.6编译的qsdk2版本。
drwxrwxr-x 2 jian jian     4096 12月 12 23:08 ./
drwxrwxr-x 3 jian jian     4096 12月 12 22:53 ../
-rw-rw-r-- 1 jian jian 14090240 12月 12 23:08 P53_ap123_6.7.7_161212.bin
-rw-r--r-- 1 jian jian   131072 12月 12 23:08 tozedap-router_4g_industry_ap123_data-jffs2
-rw-r--r-- 1 jian jian  4280320 12月 12 23:08 tozedap-router_4g_industry_ap123-squashfs
-rw-rw-r-- 1 jian jian    59440 12月 12 23:03 tuboot.bin
-rwxrwxr-x 1 jian jian  3026620 12月 12 23:01 vmlinux_ap123.bin*
-rw-rw-r-- 1 jian jian  1418791 12月 12 23:01 vmlinux_ap123.bin.gz
-rw-rw-r-- 1 jian jian  1048739 12月 12 23:03 vmlinux_ap123.bin.lzma
-rw-rw-r-- 1 jian jian       35 12月 12 23:01 vmlinux_ap123.info
-rw-rw-r-- 1 jian jian  1048803 12月 12 23:03 vmlinux_ap123.lzma.uImage
-rw-rw-r-- 1 jian jian  1048803 12月 12 23:08 vmlinux_routing.lzma.uImage

2016-12-12
20：12 先设置一下外部编译器：
# CONFIG_NATIVE_TOOLCHAIN is not set
CONFIG_TARGET_NAME="mipsel-openwrt-linux-uclibc"
CONFIG_TOOLCHAIN_PREFIX="mipsel-openwrt-linux-uclibc-"
CONFIG_TOOLCHAIN_ROOT="/usr/share/mips-gcc-4.6/staging_dir"
CONFIG_TOOLCHAIN_BIN_PATH="./usr/bin ./bin"
CONFIG_TOOLCHAIN_INC_PATH="./usr/include ./include"
CONFIG_TOOLCHAIN_LIB_PATH="./usr/lib ./lib"


17:49 特殊应用程序这个东西不理解为什么要搞出来，也许是可以让任何的lan ip都可以做到运行某个程序时能够监听到一些端口。但是如果两个pc同时触发了呢？那转给谁呢？

17:20 这篇文章号称实现了全部的类型
http://os.51cto.com/art/201103/249324.htm
/-"Full Cone NAT":/
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 202.96.209.111
iptables -t nat -A PREROUTING -i eth0 -j DNAT --to-destination 192.168.1.1

/-"Port Restricted Cone NAT":/
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 202.96.209.111

/-"Restricted Cone NAT":/
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 202.96.209.111
iptables -t nat -A PREROUTING -i eth0 -j DNAT --to-destination 192.168.1.1
iptables -A FORWARD -d 202.96.209.111 -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -I FORWARD 1 -s 85.214.128.86 -j ACCEPT(加入对点IP，作弊型连通)

17:16 这个文章号称实现了cone nat
https://www.larrysalibra.com/symmetric-cone-nat-using-linux-iptables/
eth1 = public ip
eth0 = lan ip
echo "1" > /proc/sys/net/ipv4/ip_forward
/sbin/iptables --flush
/sbin/iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE --random
/sbin/iptables -A FORWARD -i eth1 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
/sbin/iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT

17:12 Linux的NAT“MASQUERADE”属于对称形NAT。
http://blog.csdn.net/farrellcn/article/details/7229143
17:09 华为的某个cpe还有Cone NAT类型，Symmetric NAT两种模式的选择，还不知道linux是如何实现的。
15:42 复制staging的方式貌似不怎么好用啊，所有的东西还是在重新编译。
15:17 ubuntu 1610 server版居然没有自动有openssh-server，真奇怪。难道是虚拟机自动安装的问题？
15:10 王伍又开始催那个通用平台了。
14:43 今天这个小新笔记本的无线网卡看起来不太正常，总是无法ping到mywifi
14:42 修改后貌似要apt-get update一下。
14:41 vi 中的替换，在记录一次吧，每次都忘记：:%s#us.#cn.#
14:20 下载一个ubuntu1610server来测试一下直接复制qsdk3的staging目录是否可以编译通过吧。
14:10 gcc-4.6编译ppp的时候出现的错误：
In file included from plugin.c:53:0:
/usr/share/mips-gcc-4.6/staging_dir/bin/../lib/gcc/mips-openwrt-linux-uclibc/4.6.3/../../../../mips-openwrt-linux-uclibc/sys-include/linux/if_pppox.h:87:25: error: field 'pppol2tp' has incomplete type

11:45
11:15 任银善 张勇 讨论后面的工作：
QCA9531和AR9341需要完成事项(讨论记录)：
1、增加CFG到UCI接口；
整理原来LSDK所使用到的CFG命令，查看是否可以用QSDK的接口代替。或者直接移植CFG命令。
2、把网页换成李瑶的；
更换QSDK自带的网页，主要是配置读写部分需要整理，并进行修改。
3、4G模块支持；
QSDK已经自带4G模块的驱动接口，可以先调试一下，是否可以使用。在进行对比测试，决定是否需要移植。
4、拨号支持；
直接进行移植。
5、tozed xx.ko 加入（保留通用寄存器的读写）
保留通用寄存器读写的命令接口。
6、生产工具支持；
默认第一次烧片后，自动进入art校准模式，增加判断Flag；校准完成后，保存校准后的数据到指定的备份区。
7、校准支持；（必须pass才能写）
校准脚本配置：必须规定pass后，才能写入校准后的数据。
8、自建型号；（P22、P10p）
在QSDK中，增加P22和P10p的board type，并修改对应的netwrok、LED、Button、MAC等配置部分。
9、远程升级；
类似AC管理，需要提供可以针对单台、多台、区域、所有等AP进行升级。

qsdk里面编译wlan驱动的速度好慢啊。
昨天那个编译错误只要加上 -ldl就好了。

2016-12-11
使用gcc-4.6编译当前有这样的错误：
cd ../apps/autoset_channel && make CC=mips-linux-uclibc-gcc autoset_channel
make[1]: Entering directory `/home/jian/work/ath9.5/apps/autoset_channel'
mips-linux-uclibc-gcc -o autoset_channel -O2 -Wall -Werror -I../wireless_tools.29 main.o wlanconfig.o iw.o tlog.o cfg.o -lpthread -lm  -L../wireless_tools.29 -liw
/usr/share/mips-gcc-4.6/staging_dir/bin/../lib/gcc/mips-openwrt-linux-uclibc/4.6        .3/../../../../mips-openwrt-linux-uclibc/bin/ld: warning: libdl.so.0, needed by         /usr/share/mips-gcc-4.6/staging_dir/bin/../lib/gcc/mips-openwrt-linux-uclibc/4.6        .3/../../../../mips-openwrt-linux-uclibc/lib/libpthread.so.0, not found (try using -rpath or -rpath-link)
这个错误一点曾经碰到过，不知道怎么解决的。

git clone --bare的东西，会没有remote？奇怪啊。
push的时候碰到了：error: insufficient permission for adding an object to repository database ./objects
fatal: failed to write object
error: unpack failed: unpack-objects abnormal exit
到服务器上看到git/objects下有一些所有者是root的文件，都是2014年的。git gc也同样报错，运行sudo chown -R git:git objects 就可以了。

2016-12-10
无网络的qsdk3编译，这个算是完成了。
编译8m的程序会报错：
ssh: Could not resolve hostname qca-git01.qualcomm.com: Name or service not known
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
Makefile:281: *** Download/default is missing the FILE field..  Stop.
Package prerequisite check failed.
make[2]: *** [tmp/.prereq_packages] Error 1
make[1]: *** [prereq] Error 2
make: *** [world] Error 2

看这个qca-git01.qualcomm.com在哪里用过了：
jian@jian-OptiPlex-9020:~/work/qsdk3$ grep qca-git01.qualcomm.com * -r
qca/feeds/wlan_10_2/qca-wifi/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/wifi/$(PKG_NAME)-10.2.git
qca/feeds/qca_10_4/utils/qca-spectral-10.4/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/wifi/$(PKG_NAME).git
qca/feeds/qca_10_4/net/qca-acfg-10.4/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/wifi/$(PKG_NAME).git
qca/feeds/qca_10_4/net/qca-wrapd-10.4/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/wifi/$(PKG_NAME).git
qca/feeds/whc/qca-whc-repacd/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/whc/qca-whc-repacd
qca/feeds/wlan_10_4/net/qca-wifi-10.4/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/wifi/$(PKG_NAME).git
qca/feeds/wlan_10_4/net/qca-hostap-10.4/Makefile:PKG_SOURCE_URL:=ssh://qca-git01.qualcomm.com:29418/wifi/$(PKG_NAME).git

2016-12-9
使用gcc4.3.3编译的工业路由器qsdk版本大小：
drwxrwxr-x 2 jian jian     4096 11月 20 17:45 burn
-rw-rw-r-- 1 jian jian 26731779 11月 20 17:45 P53_6.5_161120_all.zip
drwxrwxr-x 2 jian jian     4096 11月 20 17:45 remote_update
drwxrwxr-x 2 jian jian     4096 11月 20 17:45 tftp
-rw-r--r-- 1 jian jian   131072 11月 20 17:45 tozedap-router_4g_industry_ap123_data-jffs2
-rw-r--r-- 1 jian jian  4296704 11月 20 17:45 tozedap-router_4g_industry_ap123-squashfs
-rw-rw-r-- 1 jian jian    55553 11月 20 17:43 tuboot.bin
drwxrwxr-x 2 jian jian     4096 11月 20 17:45 update
-rwxrwxr-x 1 jian jian  3080740 11月 20 17:42 vmlinux_ap123.bin
-rw-rw-r-- 1 jian jian  1413274 11月 20 17:42 vmlinux_ap123.bin.gz
-rw-rw-r-- 1 jian jian  1042725 11月 20 17:43 vmlinux_ap123.bin.lzma
-rw-rw-r-- 1 jian jian       35 11月 20 17:42 vmlinux_ap123.info
-rw-rw-r-- 1 jian jian  1042789 11月 20 17:43 vmlinux_ap123.lzma.uImage
-rw-rw-r-- 1 jian jian  1042789 11月 20 17:45 vmlinux_routing.lzma.uImage


15:41 git-daemon --reuseaddr --base-path=/opt/git --verbose --export-all 这样就可以开一个没有权限的git仓了。而且是只读的，就这样可以把
14:00 openwrt_cc和qsdk的dl放在一起
11:07 为什么123从112上复制文件的速度只有10mb，奇怪的事情。


10:36
苗立双 还是想让华域的增加一些函数，当前恢复出厂太慢了。

2016-12-8
14:40 终于把1.2换成了我这里，主要是找那个mac克隆找了好久，开始还以为是没有。还有就是速度一直限制在10m，原来是恢复出厂后有个qos?的设置限制了，奇怪的默认配置。再往前居然是恢复出厂搞了半天，192.168.1.1连不到，再次恢复还过了好久又莫名其妙的可以了。再往前，把mac写成了全0，不能连了，只好恢复出厂。不过参数已经备份下来了。
14:30 忘记去7天酒店拿发票，根本就扔在脑后了。
9:34 249ssh的速度非常慢，奇怪的事情，感觉所有的机器登录ssh都很慢。

2016-12-7
李柱栋 没有去上海，clk出来了，但是只有64k，不够slic的速度。
15:30 华为的egw2160路由器中，如果没有密码的ssid，可以设置的最大用户数就是124，如果是wpa以上的加密方式，就只能设置64个了。

11:30 和中兴微电子的人来，杨学森和许兴奎。王伍说了几个方面，全包升级，时间是否太长，flash要求是否太大。wifi是否要校准，厂测工具。底板的参考设计，网优参数，snir srnp等， volte的apn要能修改。
9:09 陈良 菲律宾的要再14日长测，想黄武今天出板和bom。姚国梁的签证没法加快，这样13日就没有人去菲律宾了。

2016-12-6
22：00 李柱栋 方陈 李柱栋非常着急pcm的clk没有出来，想去联芯调试，方陈想等板子回来。

这个puk是哪张卡的？18119992

工业路由器移植qsdk后还需要进行的工作：
wlanconfig ath0 list中又0m的显示
tozedxxx。ko需要移植到新的内核，实现看门狗，gpio， 各种灯，commreg
最好不要升级uboot，内核写死启动参数。
wifi加密方式支持
wifi功率验证
wifi距离测试
ddns, l2tp, pptp
内核中的以太网驱动看起来只有eth0了。
4g模块支持
校准支持

1 当前连续运行2天没有无线中断的情况，同样的硬件lsdk驱动连续1天后出现不定时wifi中断情况。但可以恢复。
2 使用馈线之间连接测试中，切换到单天线打流未发现出现断流情况。
3 使用联想小新笔记本无线网卡linux可以长连10多个小时，同样的笔记本，如果连m60，2个小时左右就会无法ping通，必须笔记本重新连接。

2016-12-5
15:32 route del default
route add -net 192.168.1.0/24 gw 10.8.0.2
这样来能够访问公司网络，但是不能出外网。

15:06 谢世乐写了些软件登记的信息。

14:26 qsdk3看起来编译成功了。

11:00 陈良 p21剩余的工作一个是wps的灯还需要修改，另外由于更改了拨号流程，需要大量的测试。当前由占永平进行。天线的问题当时还存在一个问题，华为的设备是两个天线接上才能切换到外置天线，中兴的是接了哪个切哪个。而我们的则是接上了一个就切了。后面改成华为的样子的。由于gpio不够，那么就只有自动模式，没有网页设置，两个都接上了就是外置，否则就是内置。
安徽的不断断线的情况，是核心网升级了，1761模块存在问题。联芯的人去过现场，改过程序后的两个点没有再出现断线的情况。后续的升级就比较复杂，主要是1761模块的版本特别多。准备只升级那些报有问题的。
7628的那个ap在陈良看来不好用，进程微信的图片无法发出去。
菲律宾的网速非常慢，存在非常多的小运营商。所以陈良认为wbs还是很有机会。

10:32 delphi7中的listview改变了column后，貌似要重启才能真的改变内容的显示。否则总是不对的。

10:20 徐钢雄带测试的来借卡，他的卡被刘云借走了，刘云的被华域的借走了。
任银善 已经上传了qsdk中的其他代码，继续编译中。


9：58 喻潇 一个工业路由器今天来发现卡不识别了。放在其他机器上可以使用，这个机器使用其他卡也可以使用。这个问题原来是这个卡存在pin码，而宽翼的模块在有pin的情况下

李柱栋 slic的驱动api看起来还比较复杂。pcm应该比较简单，就是几个语句的事情。

总感觉系统的速度有点慢，貌似把virtualbox中的win7内存改小一点就好了。

2016-12-1
11:19 重新在virtualbox中安装win7，又能发送邮件了。win7给24g空间，是不是太小了？
任银善 qsdk3.0已经可以编译。

9:26 工业路由器的wifi又恢复了，而且没有什么报错之类的。真的好难受了。

工业路由器那个wifi也连不上了，真是个悲催的日子。

邮件又开始发送不了了。换回旧版本的bat也报那个什么is not porperly address。卸载那个无线驱动也没有用。

编译qsdk出现./build_dir/target-mips_r2_uClibc-0.9.33.2/qca-legacy-uboot/ap135/mkconfig这个文件没有执行权限的错误。

2016-11-29
通过这样来把svn的仓转到本地的git:
git svn clone  http://192.168.1.123/svn/am3517sd

李柱栋 和吴曦简单的聊了一下，吴曦觉得今年太累了。李柱栋自己有一定的提升，以前确实有不在其位，不谋其政的思想。现在觉得，如果混日子，老板损失的只是一份工资，根本不算是损失，而个人损失的是青春，非常大的损失。

编译dnsmasq最新版需要COPTS=-DNO_INOTIFY


2016-11-28
把路由器的地址设置到了10.19.0.1，本地地址设置到了10.8.0.100，本来192.168.19.x也是特别的。
google.cn本身是可以访问的，可以在它里面下载chrome，不过搜索功能还是转到了hk，继续不能用。
chrome的字体很奇怪，fxiaoke这个网站更加，各种字体分开来。感觉只有xiaoke这个网站问题大一些，那就这样吧。


喻潇 出现笔记本不能连接wifi的情况，dmesg出现"not sta mode"这样的错误。同时她的iphone连接正常，上网无异常。重启后一样。我再重启后消失，但发现如果在13信道效果非常差，换6信道还行。到屏蔽房关门ping没有问题，开门非常差。徐钢雄认为是pa坏掉了。

2016-11-25
宽翼模块的mtd部分
dev:    size   erasesize  name
mtd0: 00280000 00040000 "sbl"
mtd1: 00280000 00040000 "mibib"
mtd2: 00c00000 00040000 "efs2"
mtd3: 00100000 00040000 "tz"
mtd4: 00080000 00040000 "rpm"
mtd5: 00080000 00040000 "aboot"
mtd6: 00800000 00040000 "boot"
mtd7: 01440000 00040000 "scrub"
mtd8: 037c0000 00040000 "modem"
mtd9: 01440000 00040000 "misc"
mtd10: 00700000 00040000 "recovery"
mtd11: 05040000 00040000 "fota"
mtd12: 00980000 00040000 "recoveryfs"
mtd13: 12400000 00040000 "system"


2016-11-21
在win7下这个微信客户端又占用的大量的连接，导致印象笔记没法同步。也有可能是这个笔记自己同步不了了，从任务管理器kill笔记这个进程，重新运行才好用的。
win7本身居然存在“基于unix的应用程序子系统”这样的东西。

2016-11-20
总算重新在工业路由器中编译了qsdk，当前还有art, 4g驱动, 自己的ko没有编译好。
这个地址讲述如何在ubuntu中右键打开terminal
http://www.linuxidc.com/Linux/2012-05/59565.htm
步骤其实很简单：sudo apt-get install nautilus-open-terminal 然后：nautilus -q或者重新登录。

 订单编号：600000000000008316112053273626
大三元套餐 每月仅需3元 玩出×1
17388731322
卡类型：4G小卡
号码低消：0.0
套餐：欢go大三元套餐
简亮
¥30
在线支付
WEB订单
2016-11-20 18:49:21
系统审核订单
订单详情
订单跟踪


2016-11-18
用一个ubuntu15来编译qsdk吧
/etc/apt/sources.list 这个是ubuntu的源的文件。

这个虚拟机居然只配置了4.6g的空间，有点搞了。
apt-get install make gcc g++ sharutils zip zlib1g-dev automake autoconf libtool subversion libncurses5-dev ocaml-nox

2016-11-15
今天来这个小狼毫输入法不能输入任何信息了，在任何窗口都是这样，只好重新启动win7的虚拟机。
姚国梁 p21存在不能启动的现象，如果是联芯的模块，每次都能启动，如果是宽翼的模块，就有不能启动的情况发生。串口无响应，不能ping通。
吴曦 在做双apn的时候，需要两个网卡都加入缺省路由，再加上两个无线的ssid就可以分别走两个lmi40,lim41分别出去了。

2016-11-11
在sdk9.5上尝试各种补丁，还是存在设置为单天线时很快挂掉的情况。

2016-11-10
21:10 王伍 继续讨论中间层的东西。
18:20 单总 开短会要求把7628的wifi搞好，还是有很多机会。

16:07 18109e20这个寄存器的值貌似没有办法修改，总是初始化的值。
viewreg 18109e20
3ce
/bin # echo 18109e20 3d6 > /proc/tozed/commreg
setting comm reg 18109e20 to value 3d6...
/bin # viewreg 18109e20
3ce

11：21信可模块公司来了一群人，来谈合作的事情。王伍认为他们没有做多少工作，想自己做中兴的模块。
9:10 王伍开了短会，讨论使用宽翼模块会在串口偶然吐出大量的错误信息导致系统停滞，表现为网页不能刷新的现象。苗认为是linux系统的问题，应该和宽翼无关。
p21的开机速度问题，这次需要加快。
9:00 王伍 说那个softethnet太复杂，需要专门的小组来完成才有可能。用户分级是指web,telnet,ssh的用户统一管理。


2016-11-9
单总早上说了几个事情：总结来说就是摄像头和工业路由器都有相当的市场。需要继续投入力量。
王伍继续催中间平台的事情。


2016-11-8
貌似很忙，但是事情好多都不记得了。


2016-11-7
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux.lzma.uImage&&erase 0x9f680000 +$filesize&&cp.b $fileaddr 0x9f680000 $filesize
tftp 0x80060000 tozedap-si-jffs2 && erase 0x9f050000 +0x630000&&cp.b $fileaddr 0x9f050000 $filesize

15：15 陈良 问那个wifi中继器的事情，我还不知道那个产品要做什么。

14:54 使用这个win7虚拟机复制又不能共享了，难道是设置的原因？恩，在设置中没有把剪贴板的使能打开。

14:46 iperf2在cpe上运行-s，那么在pc端要打上行就会变成一秒的时间，其他10秒都是下行。
如果编译iperf3呢，一开始是那个fp_zero没有定义的情况，其实在所有的math.h中都存在它的定义。但是它就是报没有定义。好吧，把它们的定义直接复制到那个cjson.c中，那么在link的时候出现：
.../mips-linux-uclibc/bin/ld:gcrt1.o: No such file: No such file or directory.
在这个帖子中：
https://www.linux-mips.org/archives/linux-mips/2008-12/msg00148.html
最后提问者号称要重新编译一个出来，但后面就没有了。
在这个帖子中：
http://bbs.csdn.net/topics/390723992，直接没有任何回应。

9:01 微信这个软件有些搞吧，有一大堆
  TCP    jian-3fc56876ff:4672   183.3.229.91:http      CLOSE_WAIT
  TCP    jian-3fc56876ff:4693   183.3.229.86:https     CLOSE_WAIT
  TCP    jian-3fc56876ff:4714   183.3.229.91:https     CLOSE_WAIT
  TCP    jian-3fc56876ff:4816   183.3.229.44:https     CLOSE_WAIT
  TCP    jian-3fc56876ff:4858   183.3.229.140:https    CLOSE_WAIT
  TCP    jian-3fc56876ff:4864   183.3.229.156:http     CLOSE_WAIT
  TCP    jian-3fc56876ff:4870   183.3.229.143:https    CLOSE_WAIT
  TCP    jian-3fc56876ff:4964   183.3.229.88:https     CLOSE_WAIT
  TCP    jian-3fc56876ff:4980   183.3.229.92:https     CLOSE_WAIT
  TCP    jian-3fc56876ff:4996   183.3.229.156:https    CLOSE_WAIT
导致发邮件失败。
居然还不是这个原因，仍然报错。切换到win7就可以了，看来这个xp又出问题了。难道是我关闭了某些服务导致的？还有,就是那个passkeeper在win7下可以运行，但是在xp上总是报打开那个存档文件有问题，难道win7增加了些什么东西？

姚国梁 出现的视频通过4g上传会出现不规律的停止现象，当前修改mtu从1500到1200后没有出现了。没有机会测试更多的值的情况。

2016-11-4
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-jffs2 && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 tuboot.bin && erase 0x9f000000 +0x10000&&cp.b $fileaddr 0x9f000000 $filesize

2016-11-3
昨天遗留的一些问题：
非洲一个客户不能使用xl2tp拨号上网

早上处理几件事情，苗立双那里出现的udp转发，必须重启才生效，这个是非常奇怪的现象。而tcp转发的规则是立即就又效果的。
刘云的华域模块以太网和wifi测速，发现很多情况根本没有什么速度。

为什么今天编译iperf会出现这么多错误：
Listener.cpp: In member function 'void Listener::Accept(thread_Settings*)':
Listener.cpp:430: error: invalid conversion from 'int*' to 'socklen_t*'
Listener.cpp:430: error:   initializing argument 6 of 'ssize_t recvfrom(int, void*, size_t, int, sockaddr*, socklen_t*)'
Listener.cpp:455: error: invalid conversion from 'int*' to 'socklen_t*'
Listener.cpp:455: error:   initializing argument 3 of 'int accept(int, sockaddr*, socklen_t*)'
Listener.cpp:463: error: invalid conversion from 'int*' to 'socklen_t*'
Listener.cpp:463: error:   initializing argument 3 of 'int getsockname(int, sockaddr*, socklen_t*)'
Listener.cpp: In member function 'void Listener::UDPSingleServer()':
Listener.cpp:495: error: invalid conversion from 'int*' to 'socklen_t*'
Listener.cpp:495: error:   initializing argument 6 of 'ssize_t recvfrom(int, void*, size_t, int, sockaddr*, socklen_t*)'
Listener.cpp:523: error: invalid conversion from 'int*' to 'socklen_t*'
Listener.cpp:523: error:   initializing argument 3 of 'int getsockname(int, sockaddr*, socklen_t*)'
还有：
ReportCSV.c:(.text+0xa8): undefined reference to `rpl_malloc'
Reporter.o: In function `ReportServerUDP':
好吧，总算编译过了。
感觉如果使用make BOARD_TYPE=db12x toolchain_build编译出来的编译器就会报那个ccache错误，如果直接编译就没事。


set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedcpe-ap_ap123-jffs2 && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 tuboot.bin && erase 0x9f000000 +0x10000&&cp.b $fileaddr 0x9f000000 $filesize

2016-11-2
16:20 iperf这个东西的编译需要用到g++，我现在重新编译这个编译器，出现了无数多的texi的错误，真的非常郁闷的事情。算了删除toolchain目录重新来过吧。还是不行啊，这也奇怪，本来昨天都编译通过了的。
有一个测试人员来应聘，测试过网站的，使用过mantis，禅道等工具，使用供loadrunner等自动化测试工具。要5.5k。
王伍 在产线上碰到这样的问题，启动后网络不通，通过wifi登录后发现eth0存在，但是如果ifconfig eth0 down可以，但是ifconfig eth0 up就会报错了。从网站上来看这颗芯片有多种型号，我们使用的是C，支持所谓的always on always connect特性，不知道这个特性是做什么的。有一个更新的版本从4.17到4.18，但看改动似乎没有太多的修改。
汪光华在做不停的重新启动测试，到现在似乎没有发现类似的情况。

pdca: plan do check act.

为什么会有这么多错误：
/opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/gcc-4.3.3/gcc/doc/invoke.texi:961: @itemx must follow @item
/opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/gcc-4.3.3/gcc/doc/invoke.texi:8580: @itemx must follow @item
/opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/gcc-4.3.3/gcc/doc/extend.texi:4234: @subsection seen before @end table
/opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/gcc-4.3.3/gcc/doc/extend.texi:4263: @item outside of table or list
/opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/gcc-4.3.3/gcc/doc/extend.texi:4264: @itemx outside of table or list
/opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/gcc-4.3.3/gcc/doc/extend.texi:4277: unmatched `@end table'

17:43 彭广才 王伍 问关于工业路由器重启的事情，早上测试的情况是使用tplink的9v的电源，那么就会出现把模块断电，上电而系统复位的情况。

18:41 为什么还是报这样的错误：ccache: failed to create /opt/work/ath9.5/build/gcc-4.3.3/toolchain_build_mips/ccache-2.4/cache (No such file or directory)

安装这样把makeinfo降级
wget http://ftp.gnu.org/gnu/texinfo/texinfo-4.13a.tar.gz
tar -zxvf texinfo-4.13a.tar.gz
cd texinfo-4.13
./configure
make
sudo make install

2016-11-1
刘云来请求支援。关于fota的几个开机启动检查更新等，希望由梁剑来做。

2016-10-21
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedcpe-df_ap123-jffs2 && erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 tuboot.bin && erase 0x9f000000 +0x10000&&cp.b $fileaddr 0x9f000000 $filesize
10-18
使用sort可以简单的把git中backup的文件排序。

2016-10-17
killall TZmacwriter
tzphone wdt_disable

killall valgrind ; killall -9 boa ; valgrind -v --leak-check=full --trace-children=yes --trace-children-skip=/system/bin/iptables,/system/bin/chmod,/system/bin/getprop,/data/tz_local_conf/iptables_build_all,/system/bin/sh --log-file=/tmp/11.log boa

busybox tail -f /tmp/11.log
10-15
早上增加对键盘的初始化gpio操作。

2016-10-14
一早开会，李总总体来说对研发满意，认为研发走在了公司的前列。许诺有期权等多种分配方式。
早上得到西森美康的消息，我们的打分在第一名。
下午折腾了一下valgrind，在1860平台上已经有这个软件，编译起来也没有碰到多少问题，由于tzphone现在无法从命令行简单的运行，所以如何查错还是个问题。

2016-10-12
早上做了什么，这是个问题。
彭广才：希望射频工程师能做得住，一点一点对指标，然后和天线厂家仔细对指标，花大力气把wifi性能提高。
李忠 使用9531的两个板子，在李忠那里双向打流的效果也很差，加起来只用3m。同时也认为上下行不一致，上行高于下行。

10-10
10:42 4g固定台使用最新的程序，拔掉天线，没有出现重启的情况。扣上天线，界面还是很快出现了中国移动的字样。
任银善 按照朱建文的反馈，9531无法再sdk9.5上编译。ath9.5下的9531似乎无法编译。
下午朱建文发来了驱动，应该还是原来发给我的那个吧。
宽翼的程序重新下载可用编译了，但是删除了算有的git目录又无法编译了。先不删除再编译一次看看吧。不删除任何东西，那么是可用编译通过的。
姚国梁 ip passthough貌似不好用，开始是去掉了usb0的ip后，苗立双的容错程序立即重新得到一个地址。
比较两次下载的宽翼的sdk，4个文件的md5都不相同，好吧，居然会这样。
颜斌 在72m下功率不会增加，还是10dm，也许是只有低功率的情况下增加了。

2016-10-9
早上虚拟机出现了dns变成192.168.1.45的情况。真的非常奇怪啊。
10.10在笔记本上也出现了这样的情况，感觉是我的路由器上在wan口和lan口上同时插了公司局域网网线的原因。这样会有回环吗？难道是我把公司局域网搞瘫痪了？
下午在华域，商讨的问题是，算了，刘云的那个邮件不见了。


2016-10-8
晚上王伍使用双流cpe对4g固定台进行测试，发现了奇怪的现象。cpe用馈线连接1860，cpe网口和1860网扣各接一台电脑。从cpe下面的电脑ping王伍的电脑，但是不能ping到另外一台电脑，1860上王伍的电脑和另外一台电脑更换了许多次都是这样的现象。

2016-9-30
工业路由器西森美康说路由器有不断的拨号，断开动作，到了现场发现ip并没有改变。关闭了那个第二个连接后，仍然存在，又去看什么保持连接的方式，应该是重启后就没有这样的事情了。

2016-9-29
陈良：安徽的割接已经算是顺利的通过了吧，现在河北的cpe网管问题是主要问题了。河北当前有三个问题

2016-9-28
王伍：
菲律宾的4g cpe方案要采用以9x07为主，以9531为辅助的方案，这样的做法就类似于p11套装了。认为这样的做法能比较块的出成品。
和陈玉商量，让余小虎继续斯里兰卡呆着，在十一这段时间里，629能调斯里兰卡的voip程序。
余小虎在我在成都的时候向陈玉抱怨，说公司没有很好的支持斯里兰卡的项目。
4g固定台需要增加功能：
1 增加一个ip转发的页面, 配置工具需要支持ip转发的配置，当前要把斯里兰卡电信voip服务器地址做为斯里兰卡电信的配置，要到吉林移动voip的几个地址
2 增加一个设备信息的按键，按键后读取ifconfig, route, iptables, netstat, meminfo, ps, top 等信息，下载到计算机，给以后的分析方便。
3 网页增加分析工具，包括ping和tracert

李柱栋：今天继续测试voip，发现拨打我的电话能拨通，但是我这里没有任何提示。使用天波的机器也是这样。

2016-9-27
彭广才 原来赚钱的时候成了无线部，开发了模块。打价格战容易把自己拖死。现在战线有点长。

2016-9-26
喻潇那里待机的机器4g固定台出现了不能上网的情况，那个双向箭头的图标没有了，web页面上的可用内存只有15m，cache还有50多。killall rild没有作用，killall tilc后机器重启。从logcat来看，又ril层通讯失败的样子。郑杏泉说ril层是android的，而联芯在其上又做了一层。上次网页不停的调用后，出现了问题，郑杏泉也写过一个调用的程序，感觉有时候可用，有时候有问题。

汪光华那里的机器出现状态网页点一次内存下降1m的情况。但是点击多次后，会从cache中释放到可用内存中。

王伍 如果出现内存变到cache中的情况，就非常容易出现，

2016-9-20
/sys/devices/platform/comip-wdt.0
19:26 使用吸顶ap，速度是环创的2倍。
讨论去重庆的事情。
李忠：4g固定台的wifi，在环创吸顶ap开启的时候打流会受非常大的影响。
16:09 使用环创的程序的吸顶ap，用户增加到18个，速度保持不变。
15:21 使用环创的程序的吸顶ap的速度再800-1m，还比较平稳。
陈玉发来了印度ap的logo。颜斌问要做成9341小ap的功能要多长的时间。
9:53 好吧，又拔了半天的网线。
人事来问招人的情况。
刘汉琴 说有经验的人不好招，停下来再开始会有较长的周期。苗立双请假不扣钱的事情还要再想办法。

2016-9-18
事情太多了：
王伍 早上开4g固定台的会，感觉气氛紧张。

2016-9-14
郑杏泉 free-cwap这个软件是openwrt专用的，而我们一直用的是net-cwapd这个软件，还比较复杂，貌似没有现成的bb文件。
net-snmp已经可以在windows上的软件看见相应的内容了。

吴曦 为什么ifconfig什么都没有显示了？也不知道什么时候ifconfig又变回不是busybox的ifconfig了。

赵金 发出生产的邮件，P10PF机型测试信号灯异常事宜！
昨日我司生产P10PF机型时，产线测试发现机台插上电源时信号灯出现红灯闪亮，测试2000PCS，发现68PCS不良，不良率：3.4%。
苗立双认为要么是程序的问题，要么是硬件的问题。红灯亮时，表示的时信号很差，只有一格。


早上开会。说了几个项目：
1 m60斯里兰卡的测速，感觉是斯里兰卡电信中有两派，其中反对我们的设备方提出供货的产品都要能达到75m。昨天测试的时候，关闭了天线中3个小区的2个，这样就只有1个可以使用，开始找的点，m60测速不好，拿出华为的速度也不能到75m，所以继续找，到第二个点，华为的5次测速有两次在60多，3次在80m以上。而m60平均只有60左右。
2 dialog要的volte，
这个原来答应在8月底完成，当前其实还对完成日期没有底。白俊剑发出邮件，详细说了几个可能的问题。目前分析要点：
3 p21有需求，当前卡在629上，而629在吉林和斯里兰卡都没有处理完。
4 南美项目
南美对我们的报价满意，将要进行验厂和西安测试。
5 印度小ap, 这个wifi性能还没有把握。
6 菲律宾的g20，菲律宾这个客户是优质客户，付款非常及时。有新的需求，就是要5.8g或者2.4g的cpe，还要了解清楚一下客户的需求。
7 机顶盒项目。


2016-9.13
virtualbox可以多个虚拟机同时加载某个物理硬盘。

2016-9.12
几个项目的进展

9.10
在华域，郑庆全程陪护，把net-snmp编译完成，编译的过程出现过各种错误，比如一开始就有的文件已经存在等，是否要bitbake加 -b参数等。
李瑶的网页那端看起来到没有什么问题，本来以为没有html文件的，实际上全在index.html文件中，非常大，几千行。所有的页面其实都是一个页面，控制是否隐藏。他感觉可以完成。
刘云主要讨论灯的控制由谁来完成，由于还有对按键的控制，那么觉得还是由华域来完成算了。

密:by 23110046
2016-9.9
工具升级还存在升级慢的问题，颜斌提出做一个应用程序，在用工具升级的时候下载进去，控制灯的闪烁。这样，升级操作后，可以把设备放在一边，不必等待升级过程，直接操作下一台。

王伍 使用iptables限速，限速非常没有规律。

赵金 下午请假去看眼睛。

陈华彬的ap：
开始进入的是工程模式，要设置一下,aadmin,密码adminsangfornetwork
要先把校准区搞好，否则不断重启。
好吧，以太网不能通，这搞笑了。
Sundray-AP / #ifconfig wan 192.168.19.9
Sundray-AP / #ping 192.168.19.1
PING 192.168.19.1 (192.168.19.1): 56 data bytes

--- 192.168.19.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
dmesg中有这样的错误：
[    2.480000] eth0: Atheros AG71xx at 0xb9000000, irq 4
[    3.036000] ag71xx ag71xx.0: eth0: no PHY found with phy_mask=000000ff
进去后：factest --mode -w factory

这个脚本用来查找arp表，并自动对其中的ip进行限速。
if [ -e /tmp/.rm_iplimit ] ; then
        /tmp/.rm_iplimit
       rm /tmp/.rm_iplimit
fi

#set -x
if [ "$1" = "0" ] ; then
        exit
fi


ips=$(busybox arp -a | busybox cut -d ' ' -f 2 | busybox cut -d '(' -f 2 | busybox cut -d ')' -f 1)
for  ip in $ips ;  do
echo $ip
iptables -A FORWARD -s $ip -m limit --limit $1/sec -j ACCEPT
echo iptables -D FORWARD -s $ip -m limit --limit $1/sec -j ACCEPT  >> /tmp/.rm_iplimit
iptables -A FORWARD -s $ip -j DROP
echo iptables -D FORWARD -s $ip -j DROP >> /tmp/.rm_iplimit
done

if [ -e /tmp/.rm_iplimit ] ; then
        chmod 777 /tmp/.rm_iplimit
fi


2016-9.8
关于升级失败的问题苗立双给出了如下几个方面的改进意见：
1 减少系统文件的占用，把校准文件nart.out和模块升级文件adb从系统中去处。当需要进行这样操作时，临时上传相应的文件。
2 赵金的升级工具同时使用另外一个接口查看系统运行状态，是否存在tar, update在运行，如果以上程序在运行，那么即使和李瑶的升级伺服程序通讯失败也暂时不要报失败。

郑杏泉 已经可以在9x07上编译一个应用程序。


拉美9x07应该缺如下内容：
1 lte缺参数
2 snmp
3 tr069
4 网页（管理页面）

2016-9.7
喻潇 赵金的升级程序仍然会出现升级失败的情况。

为什么当前使用4.4.7的编译器会出现 crt1.o: No such file: No such file or directory这样的错误呢。

2016-9.6
9x07中运行telnetd，可以登录，但是输入密码后要等好久才能出现命令提示。

web编译过去了，原因有几个，第一是从virtualbox复制出来的文件，居然把MAKEFILE变成了全0，奇怪的事情。第二是又是文件存在，要手工提前删除，第三是要给rpm目录下的文件增加运行权限。

工程生产p10p，使用赵金的工具升级，出现升级失败的情况。按照苗立双的分析，是因为从非只读系统到只读系统，读取sessions的位置改变，导致升级过程中赵金读取升级过程的网页判断返回的就是验证失败导致404错误，如果出现这样的错误，那么重新验证就应该可以 了。

面试一个人，一直做项目管理的。但从事行业到差不多，给邦讯供过货。去年移动室外机出了20万，室内机应该出了几百万。

整个研发只有苹果和mate8支持volte。

晚上电话给吴福得电话，他在一个机器人公司工作，但由于项目停滞，很多人已经开始离职。感觉还是非常希望更换工作，在做9342的过程中，对驱动的修改在extap模式下，修正了当客户端的mac改变时有错误。对于传输距离的问题，开始软件也改了很多，也修改了acktimeout这个参数，但后来硬件上做了电阻电容匹配，使用了陶瓷天线后，软件不用修改也可以使用。pa做到了26。薪金要求税后23k。

2016-9.5
王伍 估计volte没法让李柱栋来做了，要白俊剑他们自己完成。

徐钢雄 还有灯一定要做。
如果usermod -a -G dialout jian这样， 运行minicom就不用sudo了。

如果以太网卡不采用swap的方式，那么就没有软件去控制灯了。写gpio_function就能起作用了。不过加载usb模块的驱动后，又被占用了，还要不断写function寄存器。

姚国梁 宽翼模块的多apn程序已经发来，要进行验证了。

华域的web已经发来，但是按照编译说明还无法编译。晕死，文档中的-是中文符号。不过使用的web服务器是一个叫做Mongoose的轻量级级web服务，从网上的资料来看，是直接支持https的，可以不用额外去找其他服务器了。

张勇 有个工业路由器校准后wifi就不能启动了。

2016-9.4
virtualbox4 剪贴板失效, 原因是那个virtualbox tray没有运行。差点重新安装ubuntu。
http://blog.csdn.net/lazyclough/article/details/7485999

打电话给朱建文和陈华彬，朱对802.1x没有太多研究，陈说hostapd有很多日志，要通过日志查问题。

用户组操作的指令，原来是把“增加”组的指令输入成了“修改”组的指令，所以导致好几个问题，第一是sudo不能用了，导致不得不去到所谓的安全模式重新增加用户到sudoers中。第二是不能在界面上直接访问第二个硬盘了。第三是莫名其妙的virtualbox的usb又不能共享了。
usermod -g group loginname
强行设置某个用户所在组
usermod -G groups loginname
把某个用户改为 group(s)
usermod -a -G groups loginname
把用户添加进入某个组(s）

陈良
各地都有双apn的需求，当前李柱栋在1860上实现的双apn还没有完成，下周姚国梁计划在宽翼的模块上实现双apn。其他模块还没有计划。

张勇
在makefile中%.o:%.c *.h这样的写法，如果目录中没有一个.h文件，居然会不执行，而采用一个默认的规则去编译，找了半天。
在uboot中打开watchdog会导致内核出现一个奇怪的错误，访问一个0x7fff....的地址，从内核的map文件来看，都是从0x8000000开始的地址。只有不在uboot中喂狗了。

2016-9.3
和陈玉对了几个项目的进程：
1 菲律宾g20 主要是保证质量，不要在细节上翻船
2 m60 主要时间节点卡在629上。
3 拉美cpe 当前华域提供了最初版本的sdk，编译成功。算是开始了第一步。但由于集采的事情，项目成员还没有进入对应工作。
4 dialog volte，volte部分还没有开始，
5 印度5.8g 小ap，暂定由梁剑在广东银联完成阶段性工作，后期由谢世乐继续广东银联的情况下，来接手这个软件。

工业路由器当前了解到有三个地方需要：
西森美康
吴开莉提到的使用1761模块的
陈良提到的某个省的要求
当前需要全力把主备系统做好，达到系统稳定可靠性大幅提高后再讨论后续的要求问题。
这两天和张勇多次讨论了主备分区的方案，当前准备采用如下方式：
uboot一份, 内核，文件系统各一份，参数文件系统一份，校准区一份。为实现简单起见，其中内核，文件系统直接使用绑定的方式。9341带有sticky寄存器，特点是能在加电周期内保持不变，不受重启影响。
普通启动过程和恢复：
1 启动时，uboot判断sticky寄存器，有三种情况：0 1 2
为0，表示重新加电或者是正常启动，从1号内核，文件系统启动。寄存器写1，打开硬件看门狗。
为1，表示从1区启动失败，从2区启动，寄存器写2，打开硬件看门狗。
为2，表示从2区启动失败，从1区启动，寄存器写1，打开硬件看门狗。
正常启动后，应用程序读取sticky寄存器，得到当前启动区信息，了解自己是从那个区启动的，并记录在/tmp文件中。
为0，1: 从1区启动。把寄存器值改为0
为2: 认为1区需要升级或者修复，把2区内容复制到1区，把寄存器值改为0。

升级过程：在flash中找一个字节记录，初始化值为0xff
如果当前从1区启动时，升级写2区，在flash记录值为0xf0。
如果当前从2区启动时，升级写1区，在flash记录值为0x0f。
uboot优先判断该字节，在f0时1区启动，其他情况


2016-9.1
陈华彬发来了16m 9344的程序，上次的没有保存，在微信上就过期了。

4g固定台以太网有丢包发生：
15123 packets transmitted, 15089 received, 0% packet loss, time 15141360ms
rtt min/avg/max/mdev = 0.828/2.330/17.034/0.729 ms
而另外一个dlink的路由器：
5587 packets transmitted, 5587 received, 0% packet loss, time 5586144ms
rtt min/avg/max/mdev = 0.621/0.722/2.075/0.047 ms
17969 packets transmitted, 17969 received, 0% packet loss, time 17968949ms
rtt min/avg/max/mdev = 0.597/0.724/1.566/0.038 ms


2016-8-31
只有在虚拟机上的ubuntu1604上编译通过了9207，本身机器编译永远是arm-oe-linux-gnueabi-gcc报： fails sanity check这个错误，昨天查到一个网页说是在当前的terminal上运行了其他编译器， 关闭终端重开， 重启都没有用啊。

vi中的替换：
:%s#vivian/#sky/# 替换全部 vivian/ 为 sky/

没有安装说明中的超多的包之前， 编译还报一个文件没有找到的错误。
在笔记本上的ubuntu16安装那些9207乱七八糟的包，还爆出来什么没有找到， 只有apt-get update才继续。

那么， 在一个ubuntu server14.04上面进行编译试试吧。

印度ap的以太网卡都有丢包的现象。

在新安装的一个ubuntu1404 server的机器上能正常编译9207,难道我的机器又要重装？

刘云 mtk的vlan似乎没有起到作用。

2016-8-30
编译9x07系统， 总是有问题。现在重新安装一个虚拟机来做这个事情吧。
居然还要安装texlive-picture这样的超级大的系统。

这台机器的行为也非常奇怪了。virtualbox的剪贴板不能共用了， usb也不能到虚拟机中了， 在界面上也不能加载第二个硬盘了。只有使用mount指令，但是加载后呢， 和虚拟机中不是同步的。 奇怪的事情。

苗立双决定在9月的下半月请假了。

在ubuntu16上面编译9x07会有那个ncurses的错误， 在1404上没有，都会出sysroot已经有文件的错误。

张勇 福桥的还是想要大功率的9341或9531, 这里还没有调出来。

王伍 没有测试项目的就可以不理会。

刘云 使用了windows下的一个radius软件，可以在linux下使用命令连通，但是使用w13选择802.1x， 还是不对，从radius服务器抓包来看， 服务器收到了w13的请求包，但没有发出接受包。

白俊剑 搞定了一个单纯模块没有启动的原因， 原来是李柱栋增加在内核中增加键盘扫描时，没有考虑到i2c设备不存在的情况， 虽然设置判断了空指针，但没有做判断。

张勇 gpio的原因是config中的变量在=后面加了个空格，但在makefile文件中没有加strip，导致判断错误。

2016-8-29
王伍: 碰到整机死掉的情况，按键没有响应，秒钟也不跳动。想解决watchdog的事情。要在kernel中关闭看门狗，在程序中打开看门狗，并且在某些情况下，不使用看门狗。另外，升级的情况一定要关闭看门狗。
voip当前主要在下载网速变化的情况下的声音有问题，629的做法是在没有收到所以包的情况下进行插值，导致声音发闷。而天波的产品估计一直等所有的包收到，有一次居然延时了10秒。
苗请假需要带着电脑。

张勇：
8m的程序居然能刷16m的程序，而且能跑起来，只是跑了第一次以后，第二次启动就不对了。难道是uboot写的时候地址回环了？

翟志华：问wbs内的用户数限制的作用。

金晶 陈良总是没有空，调试程序非常麻烦。

下午 海外来找说华域模块的事情，听说时间非常长，显得非常沮丧。

给联芯的邮件
看了一下1860的看门狗，好像很复杂的样子，完全不知道如何使用。
   comip-wdt-lc1860.c里面的内容和我们原来的使用的其他平台的的看门狗有些不同，其他平台基本是
简单的做以下操作：
1 启动看门狗，比如cat /dev/watchdog
2 定时喂狗，如果超时没有喂狗，系统自动复位
3 某些时候可以关闭看门狗。echo "V" > /dev/watchdog
请问在当前平台是如何实现呢？
  我在内核中打开comip-watchdog选项后，/sys/devices/platform/comip-wdt.0中会增加
  wdt_worktype, wdt_timeout, wdt_heartbeat文件，看起来wdt_worktype是看门狗的类型，修改它
  改为reset，也没有什么现象发生，而wdt_timeout， wdt_heartbeat这两个文件内的数值查看和填写
  似乎没有什么变化


2016-8-26
来刷qsdk编译的东西吧：
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=squanshfs ro init=/sbin/init mtdparts=spi0.0:64k(u-boot),6848k(rootfs),1152k(uImage),64k(mib0),64k(ART) machtype=DB120"
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6c0000 +$filesize&&cp.b $fileaddr 0x9f6c0000 $filesize
tftp 0x80060000 openwrt-ar71xx-generic-db120-rootfs-squashfs.bin&&erase 0x9f010000 +0x6b0000&&cp.b $fileaddr 0x9f010000 $filesize
bootm 9f6c0000
这样能进入系统，但是出现这样的错误：
/etc/init.d/rcS: line 19: can't create /dev/null: Read-only file system
/etc/init.d/rcS: line 26: can't open '/dev/null'

我的用户居然没有sudo权限了，只好开机时候不断按esc， 进入recovery mode, 选择fsck那个选项， 完成提示按enter后， 再选择root的那个选项。 usermod -a -G admin jian这个指令居然说没有admin组，好吧直接改/etc/sudoers文件了。

每次重启ubuntu， /dev/sdb1和/dev/sdb的权限都会变回去，还要重新增加。

更加不对的地方在于virtualbox的剪贴版不能和ubuntu共享了。

2016-8-25
9344的试试，刷了个uboot，不能启动了。


2016-8-24
自己的9341测试的效果还是要差一些。
15:15 李忠说了几个问题：当前m20的短信中心错误的问题，把原来的那个看变量的程序实现的问题，测试的问题。
早上面试了姜涛，谈15000就直接走人了。
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=jffs2 rw init=/sbin/init mtdparts=spi0.0:64k(u-boot),6848k(rootfs),1152k(uImage),64k(mib0),64k(ART) machtype=DB120"
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6c0000 +$filesize&&cp.b $fileaddr 0x9f6c0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-jffs2&&erase 0x9f010000 +0x6b0000&&cp.b $fileaddr 0x9f010000 $filesize
bootm 9f6c0000

开始砍砍砍：
去掉：CONFIG_HAMRADIO=y
去掉pci无线不能起来了，那么我把无线的部分先换一下吧。

这个看起来是对的了：
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=jffs2 rw init=/sbin/init mtdparts=spi0.0:64k(u-boot),6976k(rootfs),1024k(uImage),64k(mib0),64k(ART) machtype=DB120"

set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-jffs2&&erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 tuboot.bin && erase 0x9f000000 +0x10000&&cp.b $fileaddr 0x9f000000 $filesize

2016-8-23
做了什么，真的不容易想起来：
继续和中试争论问题，黄礼仪等认为研发必须要先测试，而且要提供自测报告给中试。
测试了若干种限速的方法，看起来只有针对单个ip的限速有效果，其他限速方式要么没有用，要么限速效果太明显，下载速度立即变成10多k。
下午余小虎开了电话会议，他可能在斯里兰卡太孤独了。会中喻潇问几个产品哪个的优先级高。陈玉说李忠的中试人员太少了。
用买来的9531测试看起来还不错。
iptables -d INPUT -i wlan0 -m limit --limit 1000/s -j ACCEPT
iptables -D INPUT -i wlan0 -j DROP

2016-8-22
17:40好吧，怎么今天一天都在说话？
早上先是颜斌来问为什么p10p上的加功率没有作用。说要生产了。
还有泰尔实验室下面的测试要求非常高，要100个用户。还有一点，写的有信噪比改善的一条，不知道如何展示。
吴曦：周六周日腰疼，于是拿着笔记本在家里折腾，今天开始牙肿了。wifi认证的事情应该问题不大了。
郑杏泉：早上生了个儿子，7.5斤。
颜斌，李忠 有激烈的争吵，李忠认为颜斌不尊重中试。
王伍 1860在下载的时候拨打voip电话，会出现效果变差的情况。要进行限速。
下午 被和金晶和吴曦的面谈占领了。吴曦提到两点：能否多给予表扬，少进行批评。导师对个人的未来指导的太少。

晚上搞了一下1860的tc，编译iproute2中的tc，运行显示：
./tc qdisc add dev wlan0 root handle 1:0 tbf rate 400Mbit burst 1500k
Android does not support qdisc 'tbf'
发现网页有这样的现象：
中英文切换要点2次。而且也会切换lcd的显示界面，有这个必要吗？

苑德强来说巴西有日本公司“谷和电工”，买了他上一家公司的大量gpon设备，想购买wbs设备来发展山区的网络。想把gpon的snmp和wbs的snmp在一个软件上查看。应该没有问题吧。

苗立双 l2tp拨号后， cntv上的视频就没法看了。

2016-8-21
总算把qsdk中的wifi编译过去了，增加了几个参数，在生成烧片文件的时候居然报错了。先不管了。
继续下载吧:
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=jffs2 rw init=/sbin/init mtdparts=spi0.0:64k(u-boot),6976k(rootfs),1024k(uImage),64k(mib0),64k(ART) machtype=DB120"
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-jffs2&&erase 0x9f010000 +0x6d0000&&cp.b $fileaddr 0x9f010000 $filesize
这样可用运行，但是wifi不能启动。但eth0是对的，从路由器上得到了地址。
第一个报错：[  208.460000] adf: Unknown symbol register_simple_config_callback (err 0)
那么把NO_SIMPLE_CONFIG=1这个加到config中看看吧。
编译完成后，刷了jffs2为什么内核又变成crc error呢？
现在的错误变成了：[  143.360000] umac: Unknown symbol HIFDetachHTC (err 0)
终于不是这个错误了。
又来了：[   18.670000] ath_pktlog: Unknown symbol g_ol_pl_os_dep_funcs (err 0)
加上REMOVE_PKT_LOG=0这个东东看看有没有效果。

内核还是太大了，那么换下地址吧
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=jffs2 rw init=/sbin/init mtdparts=spi0.0:64k(u-boot),6848k(rootfs),1152k(uImage),64k(mib0),64k(ART) machtype=DB120"
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6c0000 +$filesize&&cp.b $fileaddr 0x9f6c0000 $filesize
tftp 0x80060000 tozedap-cp_ap123-jffs2&&erase 0x9f010000 +0x6b0000&&cp.b $fileaddr 0x9f010000 $filesize
bootm 9f6c0000

计划
姚国梁：
1.单口VoIP路由器发出程序进行测试，周一发出。
2.在新板子上修改i2c的驱动部分，四口VoIP路由器发出程序进行测试。周三发出测试。
3.配合629调试VoIP的通话，寄过去的板子周一应该收到了。
4.支持维护bm806和7100e模块程序。

白俊剑：
R10版本锁频段功能解决，R10版本稳定性使用测试，斯里兰卡要求完善：多SSID网页及终端侧、DDNS网页及终端侧、其他问题修复。

李瑶：
熟悉5寸屏安卓系统开发，自定义联系人功能

汪光华：
改bug.

刘云：
TR069服务器ACS搭建
修改客户端配置freecwmp相应参数的相应源码，修改LUA脚本使网页增加相应参数配置菜单
列出需要和网管交互的参数表

余小虎
08/15-08/21 工作总结
     1.  协调解决SLT初步测试报告中反馈的问题
     2.  测试webui/反馈问题，部分跟进
     3.  整理SLT后续待支持功能情况
     4.  R10版本编译程序提供内部测试/简单测试以太网网口
08/22-08/29 工作计划
     1. 协调项目组出满足如下条件的新版本：
       1）解决SLT初步测试所反馈的问题
       2）基础版本较为稳定
     2. 配合光华测试验证DDNS
     3. 跟进VOIP呼叫等待在斯里兰卡不生效问题
     4. 开发调试VOIP呼叫转移功能
     5. 针对可能收到的SLT报告进行内部反馈/外部确认

2016-8-19
早上好像什么都没有做啊：
和派联的冯树彬联系，感觉单总对从派联直接拿程序还是有顾忌，所以还是先选择询问的方式吧。他建立一个qq讨论组，发了一个xacs的系统来。
李总开会说斯里兰卡的事情。
白俊剑 刷ue也会出现网卡掉的情况。

下午 和泰尔实验室的人聊，单总说关于当前wifi的情况。李莉莉主要想了解当前移动准备搞wifi到货检测到底是想做什么。
张勇 改变区后，wifi总是无法启动。

晚上 徐华彬来，带来了一个9344的板子，测试的效果还可用，总速度还可用。

2016-8-18
19:28 朱建文发来的9344的qsdk的文件，貌似和9531是一样的。

18:53 http://blog.163.com/ksharp_dabu/blog/static/1954880222011102121517766/
这个文章讲述了如何使用物理硬盘做为virtualbox内部的磁盘使用，有意思的时，这时候其实linux也可以访问这个硬盘。
    将当前用户加入到vboxusers用户组sudo usermod -G vboxusers -a `whoami`
    需重新登录
    对指定的硬盘设备添加访问权限sudo chmod o+rw /dev/设备(如:/dev/sda 整块硬盘,/dev/sda1 某分区)
    建立一个虚拟硬盘镜像VBoxManage internalcommands createrawvmdk -filename ~/winxp.vmdk -rawdisk /dev/sda -partitions 1 -relative -register
    新建一虚拟机并指定上面建立好的虚拟硬盘镜像(略)

16:38 来记录一下早上的事情：
王伍 继续测试4g固定台的wifi，发现我的机器和李柱栋的机器都在windows下ping到固定台会丢包。从各个机器若干次抓包的情况来看，4g固定台收到了icmp echo包，并立即做了返回，而且空间包也出现了回包。但在windows上，会有4-5秒才在抓包的上面显示这个回包，这个时候，windows已经认为是丢包了。
姚国梁 演示了一下wps，使用android手机确实可以做到不查找ssid，不输入密码连接wifi。但苹果手机看起来没有找到没有这个功能。
电信安装iptv的人来了，说我们没有猫，只有走了。
方陈 测试mtk小ap的板子多用户的情况，貌似有很多9331能连接的用户无法连上。
刘云 问是否继续使用派联的网管。

16：37 新的9344的板子，居然任何一个口都可以接受供电。
set bootargs "console=ttyS0,115200 root=31:01 rootfstype=jffs2 rw init=/sbin/init mtdparts=spi0.0:64k(u-boot),6976k(rootfs),1024k(uImage),64k(mib0),64k(ART) machtype=DB120"
set ipaddr 192.168.19.33 && set serverip 192.168.19.100
tftp 0x80060000 vmlinux_ap123.lzma.uImage&&erase 0x9f6e0000 +$filesize&&cp.b $fileaddr 0x9f6e0000 $filesize
从qqq目录编译的kernel目录中复制.config到ath9.5中，把kernel 3.3.8也复制过去，修改配置文件改编译3.3.8，增加对jffs2中的若干种压缩算法支持，就能够在9344上起来了。
cped这个程序运行马上就重启，而且马上kernel就不对了，不能启动。mac输出的是这样的：cd:b4:e2:0c:13:a0 a1:ec:3e:88:6d:d1


2016-8-17
21:44 使用4.4.7的gcc编译���内核也无法启动。
方陈 测试mtk小ap的板子，发现使用笔记本走远的时候，速度是慢慢下降的，但是往回走时，速度一直很慢，直到某个点才突然变得很高。
14:50 金晶 汪光华 讨论时区问题，加入配置应该问题不大。
吸顶ap去掉那个lan的mirror功能
14:24 4g固定台中，原来那个掉网口的dma选项没有重新加上。
14:03 ath9.5使用p11-gcc编译器好像有问题，那些库还是0.9.30的。也许是gcc-4.3.3下面的db12x.config被改过，那个BR2_STAGING_DIR指向了固定目录。就是这个原因了。
11:54 张勇 黄武 5模的模块似乎不容易出现重启后不能枚举模块的现象，而7模的模块容易出现，接上串口都不容易出现枚举不到设备的情况。黄武认为有个地方需要上拉。
姚国梁 wps好像用几次就又不好用了。
4g 固定台出现dns转向错误，猜测是断网和重新驻网后net_config.sh重新执行了一次，把一个像lan.ip的属性setprop修改后正常了。这些属性貌似不会保持，需要每次开机重新设置。
9:10 林汉琴 来催给李总发绩效结算意见。
8:57 金晶 讨论tr069服务端的事情。

2016-8.16
9331的flash选择的是mx25l6406@sop8

17:26
set lk "tftp 0x80060000 openwrt-ar71xx-generic-vmlinux.lzma && erase 0x9f6e0000 +$filesize && cp.b $fileaddr 0x9f6e0000 $filesize"

17:16 金晶，git服务器莫名其妙的又块了。
16:57 virtualbox中如果隐藏了菜单栏，还可以使用又ctrl+home键搞出来。
16:54 开会看ac路由器的外观效果图，主要集中在包装中天线如何处理方面，如果使用可以旋转拧下来的设计，那么每个头是2块，4个天线就要8块了。
15:57 从网上搜索的情况来看，openwrt应该已经有ipsec的实现的。
15:26 测试的机器重启了，不知道是什么原因，那么就接个串口看看吧。
李总 来问刚果布的电视网的事情。
林汉琴 继续问绩效结算的事情，对其他人不扣钱很有意见。
来了一个7年经验的，编程经验太少，是我没有看清楚。
燃烧奖自荐者有余小虎， 曹拓，陈良，黄武，李柱栋，苗立双，吴曦。
郑杏泉 问为什么没有自己的tr069服务器。
金晶 问为什么现在git服务貌似很慢。有时候确实要等。
李柱栋 明天请假陪妈妈去看关节炎，后天还是周五去考科目一。

2016-8.15
王伍 开4g固定台的例会：wifi还有问题，出现连上不能用，搜不到ssid等情况。需要待机测试。
使用我的苹果手机连上后，无法上网，ping 192.168.0.1不能通。重启话机后可以上网。

刘云：说要了解商业wifi的细节。今天应该可以出山西的吸顶ap程序。

张勇：派联那里使用的机器出现了奇怪的问题，用了一个小时后，不能使用了。ssid不见了。感觉所有的参数变成了0，从网管上也看不见。ps上看client程序只有一个线程，应该没有去联网管。重新下载参数后可以使用了。
使用30版本测试，多个用户速度确实非常低，总速度只有200k。

郑杏泉：还要出一个带有默认app的iptv程序。

李瑶：要修改通讯录app，能够支持一键拨号。

2016-8.14
下周计划：
白俊剑： 1，LC1860_R09版本合并。
2，R10版本不能锁频问题、无法连接miniTT问题跟踪解决。
3，跟踪解决M60、M61问题，把中兴版本确定下来，测试验证WIFI偶发不启动、无法搜索到等问题。

陈良：海外项目跟进，4G固定台升级平台，Wbs网管统计功能修改。一共2张表要按他们的格式统计，具体的我也记不清楚了，主要是新增用户数，基站故障率这几块。

汪光华：周一到周三准备G20M菲律宾程序，后面两天1860。

刘云：1.山西吸顶AP软件跟踪和测试。2.网管程序移植。

姚国梁：  1.    在单口和四口路由器上添加ＷＰＳ功能，出完整的程序进行测试。星期三之前完成。
    ２.编写四口路由器新板子的控制ｌｅｄ灯的驱动，完成时间星期五。
    ３.配合６２９那边调试ｖｏｉｐ的通话。具体完成时间要看６２９的调试进度。
    ４.维护海外的Ｐ１１和Ｐ１０Ｐ程序。

李瑶：法语的基本完成，开始5寸屏的工作。

金晶：主要时自动升级部分和tr069的客户端。

赵金：1 完成wifi生产工具的调试，看是否有修改需求。2继续5寸屏android系统的摘机


2016-8.12
早上骆晓峰 赵金 颜斌和山西的移动一个老总， 彭立涛介绍自助。 骆晓峰讲了三个， 河北沧州营业厅， 小arm壁挂， 坐式带视频自助。 移动的人关心河北厅的布局， 坐式自助需要的条件， 小壁挂的优势。  不过对于小壁挂， 他认为方向性错误。 说是移动营业厅非常多， 无需再在社会渠道扩展。

王伍 白俊剑 李柱栋 金晶 吉林要求的双apn问题， 要改那些东西。 主要在于什么时候建立两个网络， 什么时候建立静态路由表， voip额外的服务器ip如何得到。

wifi测试早上还好， 11点多出现速率很低的情况， 但可以自动恢复。 使用29版本似乎没有碰到完全断网的情况。

ubuntu带的那个输入法， 总是在鼠标划过的时候， 清除划过的内容，  是在逗我吗？

2016-8.11

wifi测试上， 使用陈工给的bin档， 测试效果非常不理想。
把三个小网卡离开5m以上的距离， 效果变差。 30版本速度会到0， 不恢复。 29版本的效果也不好， 有到0情况， 好像还没有不恢复的情况，后来晚上了， 就没啥问题了。

工业路由器， 甲方要到深圳来考察， 同时考察的是宏电。

中午朱建文过来， 还是说要用9531， 说增加一个参数看看效果如何。

在一台新的ubuntu14.04 server上， 那个iptables就是无法编译， 报
./configure: line 11933: syntax error near unexpected token `libnfnetlink,'
./configure: line 11933: `PKG_CHECK_MODULES(libnfnetlink, libnfnetlink >= 1.0,'
这样的错误。

在bigap仓中， 改用编译好的编译器编译， 会出现复制库文件错误的情况， 是由于gcc下面的.config文件没有创建。

从一个空的ubuntu server编译，使用编译好的编译器， 需要安装
sudo apt-get install make gcc g++ sharutils zip zlib1g-dev automake autoconf libtool

编译时提示：uuencode: command not found原因是sharutils没有安装
编译的时候出现"/usr/bin/ld: cannot find -lz"错误，需要安装zlib-dev这个包，在线安装命令为：apt-get install zlib1g-dev。
./autogen.sh: 4: autoreconf: not found
  是在不同版本的 tslib 下执行 autogen.sh 产生。它们产生的原因一样,是
因为没有安装
  automake 工具,      (ubuntu 8.04)用下面的命令安装好就可以了。
  sudo apt-get install autoconf automake libtool

碰到perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:

这样：
The locale settings can be set (to en_US.UTF-8 in the example) as follows:


exportLANGUAGE=en_US.UTF-8
exportLANG=en_US.UTF-8
exportLC_ALL=en_US.UTF-8
locale-genen_US.UTF-8
dpkg-reconfigurelocales

重新登录又出现了。

2016-8.10
张勇 富桥那里的测试认为30版本很容易出现没有流量的情况， 登录进去看protmode模式是0， rts也是打开的。 从修订历史来看， 29版本后并没有对无线部分进行修改。

余小虎 发送邮件：
1.  Ubuntu下通过wifi连接到安装SLT卡的M60（无法驻网），在chromium浏览器中查看WebUI，不会卡。
2.  WIN7下通过wifi连接到安装SLT卡的M60（无法驻网），在chromium、遨游浏览器中都出现WebUI很卡，有时打卡异常；改用以太网连接，WebUI正常。
3.  WIN7下通过wifi连接到安装Dialog卡的M60（成功驻网），在chromium浏览器中查看WebUI，不会卡。

bigap如果要编译一个可以下载使用的编译器，  先把gcc-4.3.3目录中对应的config文件做如下修改：
-BR2_STAGING_DIR="$(BUILD_DIR)/staging_dir"
+BR2_STAGING_DIR="/usr/share/p11-gcc/staging_dir"
要使用绝对路径，

2016-8.9
工业路由器： 李光达发现一个无线无法连接， 软件上看各种没有问题， 在屏蔽房中也无法连接， 后来上仪器检查， 有一路射频有问题。 只有换下来使用另外一块板子。  这还导致以为是dnsmasq作为dhcp使用时， 和苗立双的脚本可能有冲突， 退回到使用udhcpd这个程序。 这个软件还是由张勇来负责吧， 不要让赵金做了。

陈玉号称又可以把m60卖到dialog， 但必须有volte， 还要在9月初就出来， 说把小虎调回来， 马上又说不行。 李柱栋说要跳过so, til等层， 直接发送soket包给rild这个程序进行控制。 郑杏泉原来都是使用so中现成的函数。  白俊剑那里列举的问题还包括远程升级支持， 二层mac过滤这两个是可以做到的。

4口voip产品 姚国梁说按键的状态不好记录， 徐刚雄说还有一个使用状态灯要控制， 就是摘机、 来电需要亮灯， 而这个状态只有629知道。

刘云 关于山西的吸顶ap， 开始以为走我们的网管， 实际还是使用派联的网管， 而且作为二层设备， 也不需要wifidog进行工作。

使用陈华彬发过来的系统， 使用dd if=art.bin of=/dev/mtd4这样的命令写校准区后， 可以正常启动了。

工业路由器： 当前测试的问题有wifi有密码无法连接， 输入超级长的密码后无法连接。

昨天： 安徽那里还是要改xl2tp程序，自己来处理多个lac， 随机选择服务器。

使用qsdk的bin档， 进入了系统， 当前在无限重启。

2016-8.4
8:50 富桥那里显示上行总速率 307050 下行 2974503 在线 1167

日志：
有机会重开工业路由器这个项目， 看得出大家都很兴奋， 相信大家有这样的热情， 加 上细致的工作， 一定能有所突破。软件方面只读系统，已经实际使用，程序数据区分开，有1860系统和openwrt可以借鉴，额外的flash这个方 面，其实王总也考虑过， 这次来把它实现吧。

atheros软件后面工作量较大的方面有两个： 一个是新的qsdk的引入， 一个是vpn的实现。

多个用户测试情况： 使用12个左右的ftp下载，派联当前的mtk平台效果还可以，徐工做的新的mtk的吸顶ap效果不错，非常稳定的有20m的速度，不过我位置上的小网卡无法连接。 后来徐工帮忙把9341吸顶ap的天线重新焊了一下，效果比昨天有很大的提高，波动比mtk的吸顶ap要大些，速度也可以20多m,  晚上更到了30-40.


2016-8.3
安徽 华为认为我们的探测导致服务器满负荷， 服务器同时连接过程是700个。
这个是王伍发出的邮件：
    移动需要提供的信息：
    1）BAS是否有过调整；
    我们的应对方案：
    1）探测L2TP的流程没有STOP消息，会BAS需要超时才能释放--------------不用给移动提；
    应对:探测L2TP的流程会增加STOP消息，避免BAS超时；
    2）CPE下挂的路由器会自动PPPOE拨号，同时CPE也会有探测BAS的动作，在BAS拥塞时，会加大BAS的负担；
     应对:PPPOE拨号时CPE探测BAS的动作,会增加时间间隔保护，初步定为3分钟，每次探测必须间隔3分钟，减轻BAS负担。
    3)L2TP 消息中的端口会改变
     应对：如果移动没有强烈要求修改，我们就不改；
   后续处理方案：
   1）如果现网还有很多设备不能上网，就分片关闭没有PPPOE用户的CPE拨号上网，减轻BAS的负担；
   2）我们会按应对方案出程序，新程序需要注意淘宝是否正常，BAS分担是否正常；

商晋川： 要接5.8g的串口，以为板子右边的六个没有接器件的焊点是串口。 实际上5.8g的串口是有3个插针的。

方城： 接好了15个终端， 刚开始还跑了起来，后面就很容易到0速度， 不过莫名其妙能恢复， 又到0 又恢复。

11:58 富桥那里显示上行总速率 937545 下行 4110922 在线 1666
14:04                                       643974         3475866        1157
15:33                                        563999         2493772       1268
18:42                                        902567        4376176       1443
20:37                                      1238860        5821261         1504

张勇 富桥反应说用户量达到10多个的时候， 新的手机连上去就会出现不断等待ip地址， 或者得到ip后不能上网的情况， 退掉在线的几个用户， 这些不能使用的用户就又可以使用了。

陈华彬 提供了几个方面的参考： 给了新的qsdk中的ini文件， 建议可以试试， 提到原来使用lsdk的软件会断流， 使用qsdk就不会断流， 使用老的qsdk会断流的， 用新的qsdk就不会断了。

日志：
安徽那里的移动核心网有内容割接出现问题， 今天陈良已经出发去那里进行交流。 华为分析认为我们的多服务器探测机制可能对他的LNS服务造成冲击，苗工分析判断如果在探测机制中增加断线消息可以有效避免。

方城搭出了10个用户的测试环境， 测试发现ftp的速度并不快， 大约在400k-1.5m之间，换上张勇带回来的环创设备的也没有什么亮点。 接上w13， 那么速度明显快很多， 有3m，但有明显的速度到0的现象，非常频繁。

2016-8.1
新的qsdk运行make menuconfig出现Build dependency: Please install the Objective Caml compiler (ocaml-nox) v3.11 or later
安装它：sudo apt-get install ocaml-nox


2016-7-22
iwconfig中的Rx invalid nwid应该是这里统计的：
    is->discard.nwid = iv_stats->is_rx_wrongbss        + iv_stats->is_rx_ssidmismatch;

2016-7-14
邓杏泉 iptv的板子是基于andriod4.4版本的，而google的tv版本的android是基于5.0版本的，所以国外的支持遥控器的tv应用都需要使用5.0以上的版本。瑞芯微的3128不支持android 5. 所以只有放弃那些app的预装。如果以后海外有量，再考虑做新的板子来支持。

5寸屏，现在还没有来硬件。可以做到把微信联系人放在桌面，一键进入联系人，但不能一键语音，因为没有对应的接口，考虑是否可以用模拟触摸位置来完成。

2016-7-13
昨天去现场，开一个用户视频用户。代维的测试还是很快，遥控器翻飞，我们基本没看清电视机的屏幕上显示的内容，就已经换成了其他内容。

从另外一个厂商的测试报告上看到，他们使用了5.7g的频段。翟志华说其他省份也碰到过这样的情况，2.4g使用2.3g，也向当地移动公司反应过，但没有下文。

今日从达州回深圳。

2016-7-11
昨天把ap的程序换了个sdk9.5的无线程序，所有频道都能看了。但测试从cpe加vlan时，所有点播都失效。抓包来看ap无线端有数据，而cpe无线端无数据。打开cpe的杂散模式也无效。

回到原来的sdk，修改一个max_snoop_entries的宏，从32改为128。所有的频道都能看了。这个宏是一个数组的下标，有空再研究一下它的用途。

2016-7-10
在达州测电视直播。

一开始5.8g不能看直播是由于5.8g的模块没有开组播功能，只在2.4g部分开了组播功能。

可以看直播后，大约有一半的频道无法看，无法出现该频道的画面。打开无线的杂散模式后，大部分频道可以观看，仍然有几个频道无法观看，只能出现1-2秒的画面。

临时编译了一个sdk9.5版本的程序，不开杂散模式也可以看到大部分的频道，仍然有些频道无法观看。

在cpe测使用hub来抓包，验证了王伍的想法，不能观看的频道虽然有直播udp数据流，但流量不足。正常需要8.8mb的流量，而不能播放时只有5.5mb。

试图在ap上侧使用hub抓包，机顶盒无法登陆。

观察ap上的以太网和无线网的数据流量，发现以太网数据流量貌似正常，而无线网的数据流量明显不足。而且出现这样的情况时，访问ap的速度变得非常慢。


另外，如果使用cpe来做小ap，当前cpe使用的eth1不能有效支持管理vlan，也就是没法上网管。硬件上要改到和吸顶ap一样，使用eth0就正常。这一点，张勇已经反复验证。

2016-7-7
翟志华：使用2.4g，播放组播可以使用。不知道5.8g是什么问题。单ap又坏掉了。

王伍 単建新：富桥还是投诉我们的距离问题。使用看信号强度的方法。

2016-6-23
张勇 富桥不愿意使用mtk方案是原来曾经使用过reltk的方案，结果在使用半年左右返修率特别高，各种重启，厂家刷各种软件都无效，最后直接放弃，富桥只好重新找了一个方案。一朝被蛇咬，十年怕井绳了。另外一个问题是支持voip中的g.723存在问题。对我们的设备当前觉得覆盖范围不够远，只有30m左右。希望改成适合走廊使用的两个方向的定向天线。

吴曦 想简单的把sysconfig放到/amt目录中。

张勇 觉得差不多移动到ath9.5了。通知姚国梁从新仓开始下载。

商晋川 和机顶盒配套使用，使用了ath9.5版本的2.4g cpe，也出现了卡顿1分钟的情况。想把一些已经升级到ap的cpe退回到cpe，结果还是挂掉了。

李瑶 下周请两天假。小孩周岁了。他自己刚刚下载了一个android的开发环境。

2016-6-22
[<c02c700c>] ath_tx_update_stats+0x54/0x4e4 [ath_dev]
[<c046f270>] ath_handle_intr_aponly+0x3fc/0x120c [umac]

2016-6-21
感觉去掉那个当对端支持n时只发n的速率的限制后，打流会好一些，王伍说如果这样要加多个设备来进行测试。可能打流的总速度就会降低了。
增加那个ack的txpower的寄存器貌似没有明显的区别。


2016-6-20
邓杏泉 在做iptv的东西，增加另外一种模块，主要是1761不支持fdd。增加的内容是要改驱动，并修改相应的at指令。还有使用usb升级要做，ota升级还在考虑。

余小虎 几个事情，4g固定台入网的事情，还有一个指标没有过，曹拓要做相应的修改才行。5寸彩屏的事情，一个是如何升级，说展讯的android升级存在问题。电源方案问题。还有一个是如何建仓问题。

金晶 似乎对如何让汪光华上手，还没有明确的计划。他总数希望由李瑶来接手这个工作。


2016-6-18
李柱栋 键盘扫描快完成了，还有和用户态通信的部分，让它可以通过select来了解到有按键。但是没有上传，也没有开分支。她在日志中写道，不能和其他的，信号量同时出发。

王伍 说了几个项目的情况：

当前需要维护的项目有p11系列产品。包括p11,p10p,p19等。4g固定台。9x07项目。5寸屏的固定台。工业路由器。iptv。


2016-6-17

白俊剑 xdos似乎没有起作用啊。在我的win7虚拟机上和白俊剑的win7机器上都没有把1860搞重启。

李柱栋 已经可以在内核中扫描按键了，按照下降延来触发，貌似上升也会触发。造成这时候去扫描按键什么也扫描不到。

熊立宇 说最后一次为档案的事情请假了。

fail commit 7c80e7b81267a3e234a3f1cfd79f5f1510bae8f6     cpe-5g2g: add files in old system
commit d1b91def4bddfcab9ceb48ed67fa9ae69d84845a     cpe-5g2g: remove usb files.
commit debace0617da46703debe1deb0144824fa76e986     cpe-5g2g: use compressed uboot.
fail commit 5e595283d87f4c9e41ebc3b6305a5cc28a9dd085     cpe-5g2g: add mac & update
commit 73b0e31e83a952316ec5980fd7c3ec42d739dd20     cpe-5g2g: add web.
commit 8a7cf2225aa57578a4240cd5b7e20b7b7acac7db     cpe-5g2g: change watchdog init value.
ok  commit dee195803bbd4c7940e462174fa7b7e7b6ff3af4     cpe-5g2g: set nart pin gpio.

白俊剑 当前和后面的工作都是负责4g固定台。4g固定台除了金晶仍然在做web方面，考虑留下吴曦和汪光华，其他人员已经陆续在退出。如果后期有特别的需要，再加入人手。

吴曦 当前在做4g固定台wifi部分和其他修改。这段时间工作能力进步有点小。

刘云 当前做w13的入库，后期加入到mtk的7628平台中。

李瑶 当前在做印度小ap的web部分。小设备的上的web基本是他完成的，前一段时间想让姚国梁和他学习一下这部分的工作，但一直没有真正能接手。李瑶曾经做过挂墙linux终端的前后台，学习能力也不错。感觉还没有发挥出他的真正的实力。

陈良 各种设备的集中网管，有交流意愿和交流能力，做的集中网管也没有出现大的问题。但和公司主要产品技术差异有些大，当前不太容易安排做某个项目的项目管理。

张勇 当前做吸顶ap和印度小ap，后面准备把9341平台的其他产品，让他和梁剑、姚国梁等人一起担负起来。并参与mtk平台。

姚国梁 前一段时间主要调了多种模块，当前在做和张勇做印度小ap。如前，希望后面能和梁剑等一起把9341平台产品担负起来。

苗立双 后期准备做9x07平台，一个新的平台。感觉他做9x07平台还是要增加一个得力的人一起做，以期望不出现担子都压在他一个人的情况。其实张勇是比较好的人选。苗立双做的工作，如果做到后期再加人，担心效果会差强人意。

金晶：4g固定台的web部分，中兴对此没有要求，但海外会对此较为重视，昨天看了一下，还有很多细节需要调整。前面也征求过白俊剑的意见，让汪光华也开始学习此部分的工作，并希望以后能接手。让金晶完成此工作后能退出，完成一直以来想完成的tr069平台的工作。

赵金：工业路由器亮衡模块支持，这个功能完成后加入到郑杏泉的工作中，郑杏泉当前有些忙不过来，也需要增加助手。加入亮衡模块其实苗立双已经完成，但是由于他的分支存在了太长时间，给赵金合并分支带来较大的困扰。

郑杏泉：当前忙mtk的openwrt平台，后面还有5寸彩屏的固话和iptv需要他参与。

余小虎：当前忙4g固定台入库的支持，后面有5寸彩屏的固话。

汪光华：4g固定台剩下工作，如前，希望能接手其中web部分。汪光华自我评价不是很高，还需要激励。

熊立宇：在4g固定台前期完成一些辅助功能，但当前4g固定台遗留工作都有些难度，他暂时较有困难继续在这个项目中，考虑将他更换到其他项目中。


2016-6-16
廖中举 贵州移动的网络重新划分的事情，昨天下午给电话到我这里，移动工作人员说他们的内部网络由于移动自身原因有所调整，提到了对ac，dhcp中继等要求做的修改，这两个问题在我们农宽设备上都不存在，就不理解为什么要找到我们来谈这些问题。于是建议先去找移动公司分管我们设备技术人员做更多的了解。后来从他的日志上来看是在服务器设置后解决了。

下午去楼顶测试，还是w13最强，到了100m仍然有1MB的速率，而9341的吸顶ap还能将就，也有几百，能看到1m。mtk的7628还不太好。

程玉：斯里兰卡已经中标，5000万的任务完成了一小半。

2016-6-15
总数把试题出了一份，已经发给王伍

刘云 不同批次的w13打流速度差别很大，同样环境下差别又20mb

Sound card support
 HID Devices
USB support
SCSI device support
Second extended fs support

下午测试了吸顶ap， w13，7628等设备，吸顶ap被摔了一下，不运行了。使用手机打流，能到8\90m。而一个7628则非常好，有时能2-4m，最高能看到5m。但另外一块板不行，走到几十米就不到100k了。

刘云 王伍还是决定使用w13去完成入网。要增加多ssid，无线用户间的隔离等。但是vlan的估计太困难了。

李柱栋 能够在内核中触发gpio中断了。

2016-6-14
赵金 还没有上传ebtables的代码和发出xdos的邮件。
金晶 网页上仍然存在比较多的问题，感觉一些基本的功能没有测试。
李柱栋 还是先编译android6吧。

在p10p上，以下脚本实现ip passthrogh
ifconfig usb0 0.0.0.0 up
route add -host 10.148.55.102 dev usb0
route add default gw 10.148.55.102
route add -host 10.148.55.101 dev br0
echo "1" > /proc/sys/net/ipv4/conf/usb0/proxy_arp
echo "1" > /proc/sys/net/ipv4/conf/br0/proxy_arp
iptables -F -t nat
iptables -t nat -I POSTROUTING -s 192.168.0.1/255.255.255.0 -o usb0 -j SNAT --to-source 10.148.55.101
所连的pc可以设置
ip  10.148.55.101
netmask  255.255.255.255
gateway 10.148.55.102
dns 221.179.38.7 120.192.165.7
也可以这样设置：
ip  192.168.0.100
netmask  255.255.255.0
gateway 192.168.0.1
dns 221.179.38.7 120.192.165.7
两种方式都可以上网。

1860上看起来也可以：
WANIP=`ifconfig lmi40 | grep inet | busybox cut -d : -f 2 | busybox cut -d ' ' -f 1`                                                                                      echo $WANIP
ifconfig lmi40 0.0.0.0 up                                                                                                                                                busybox route add -host $WANIP dev br0
busybox route add default gw dev lmi40
echo "1" > /proc/sys/net/ipv4/conf/lmi40/proxy_arp                                                                                                                        echo "1" > /proc/sys/net/ipv4/conf/br0/proxy_arp
iptables -F -t nat                                                                                                                                                        iptables -t nat -I POSTROUTING -s 192.168.0.1/255.255.255.0 -o lmi40 -j SNAT --to-source $WANIP
所连的pc可以设置
ip  10.42.39.122
netmask  255.255.255.255
dns 221.179.38.7 120.192.165.7
也可以这样设置：
ip  192.168.0.100
netmask  255.255.255.255
dns 221.179.38.7 120.192.165.7
两种方式都可以上网。
如果设置为其他网段的地址，不能上网。神奇的情况是完全不需要设置网关。没有网关，本地路由怎么走的？


2016-6-12
严俊 打了2次电话进来，打过去又没有接。还是那个偶然停顿的问题。



2016-6-8
李柱栋 还没有开始测试那个ip passthrough的脚本。也许这样的东西不应该给他搞。

王伍 金晶 白俊剑 讨论网页上锁频应该做的修改。

严俊 上次说的那个每天有半小时会卡的情况，代理商又接了一个环创的设备，也会出现卡顿，但是每次卡的时间只有2-3秒。而通则的设备可能卡的时间长达30秒到1分钟。从速度上来看，通则的设备可以高达2000k-3000k，环创的只有1800，但出现卡顿的时候，通则的只有几百，而环创的仍然有1600。

王伍 继续说l2tp的方案了，各地的voip调试太复杂了，要每个地方打开firewall等，非常麻烦。

李柱栋 对nat等网络概念还不了解。

白俊剑 sml工具的源码联芯已经给了，今天的邮件是走的流程。功能是自动组成bins文件，不用再sml工具中选择那么多。

2016-6-7
颜斌 希望富桥那里先使用25版本验证一段时间，然后再继续开发新功能。

王伍 还是希望能把sdk9.5中的无线部分迁移到原来的sdk中，这样原来的产品也可以用。否则整体迁移成本太大。

使用张勇的那个编译器有错误，他的还是用他本机编译好的。ccache中存在他机器的特定路径。

余小虎 愿意承担招聘新人的任务。

周茜来了，正在做题。题目没有做完，算了让他走了。

颜斌 陈总觉得如果用mtk做cpe便宜很多，那么不用通知市场，直接换掉。

为什么修改后的无线启动不了，切换到master似乎是好的，再来试试master。确实，master是可以正常启动的。出现的错误是Unknown symbol __floatsidf，难道里面根本没有对浮点数的支持？先用+3来吧。

富桥那里在批量升级25版本的程序了。

在楼顶测试了吸顶ap, 印度ap的板子，w13，感觉全向天线真的很差，换成吸顶ap的天线就和w13的效果差不多了。

这个也有点像ip passthrough
https://forum.openwrt.org/viewtopic.php?id=20276
watts, I have this working. It was fairly straightforward to do. The only thing I haven't done yet is to get dnsmasq to serve up the WAN IP and gateway to one client.

ifconfig ppp0 0.0.0.0
route add -net $WANIP netmask 255.255.255.255 dev br-lan
route add default ppp0
route add -host $GATEWAY dev ppp0
echo "1" > /proc/sys/net/ipv4/conf/ppp0/proxy_arp
echo "1" > /proc/sys/net/ipv4/conf/br-lan/proxy_arp

Then I assign my laptop the WAN IP and GW from the ppp connection and bam, I'm online. I've tested on Sprint and AT&T so far.



2016-6-6
郑杏泉 从明天开始请2天假，把家人送回广西待产。大约6个月了。

张勇 姚国梁 9341平台，无线当作客户端，那么密码输入错误，不会有任何提示。

李柱栋 ip passthough技术，如果在br0上增加一个虚拟接口，再增加一个dhcpc得到额外的地址，就可以实现两个设备都能被访问。

王伍 郑杏泉 iptv上要增加若干个vlan，不同的vlan做不同的用处，如果是linux，那么vconfig应该能做到，看看在android下是否可行。

余小虎 发现一个^dmrst的东西蹦出来，然后tzphone无响应，看top，tzphone占用33%，看日志，后面没有任何输出。从其他串口得到cfun已经变成了4。

小马oem9激活工具这个可以激化在虚拟机中安装的win7.

在虚拟机中运行通则终端就没有乱码，而linux本身反而有乱码，真奇怪啊。后来再看，其实也有乱码。

张勇修改了/staging_dir/usr/include/linux/fs.h，第25行增加了：这样busybox中的umount就可以编译了。
#define MNT_FORCE       0x00000001      /* Attempt to forcibily umount */
#define MNT_DETACH      0x00000002      /* Just detach from the tree */
#define MNT_EXPIRE      0x00000004      /* Mark for expiry */

2016-6-5
ubuntu linux 下建立 纯L2TP 服务端和客户端
http://blog.csdn.net/lfw19891101/article/details/7206217

mtpd编译没有问题，运行直接退出，使用logcat -s mtpd看：
I/mtpd    (17988): Using protocol l2tp
I/mtpd    (17988): Connecting to 192.168.0.50 port 1701 via br0
I/mtpd    (17988): Connection established (socket = 23)
D/mtpd    (17988): Sending SCCRQ (local_tunnel = 6909)
D/mtpd    (17988): Received SCCRP without valid challenge response
E/mtpd    (17988): Protocol error
D/mtpd    (17988): Sending STOPCCN
I/mtpd    (17988): Mtpd is terminated (status = 4)

刷ap-cp的
setenv ipaddr 192.168.19.118 && setenv serverip 192.168.19.100
tftp 0x80060000 tozedap-cp_ap123-jffs2 && erase 0x9f010000 +0x6d0000 && cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 vmlinux_ap123.ma.uImage && erase 0x9f6e0000 +$filesize && cp.b $fileaddr 0x9f6e0000 $filesize

使用这个指令来搜索局域网内的地址：
nmap -sP 192.168.1.0/24

上次王伍打电话来 有这么几件事情： volte的呼叫转移这样的补充业务，在中国移动是使用向服务器发送特定的数据包来实现，这个联芯是使用java来做的，我们没有这个标准呢，貌似需要抓包来实现。

人员方面：斯里兰卡的volte voip都要有人来接下来。金晶先把web认真做好，他水平还是有的。汪光华要压担子。吴曦没有学习的积极性。需要通过考试来给大家学习的压力。比如说在linux下的cpu占用率，内存使用情况，命令的重定向，路由，静态路由等。

在上海搞无线，发现在某些情况下cpu的主频会降下来，导致wifi速率下降。而如果永远不降，那么就发热的厉害。

还有几个问题一直拖着：ip passthrough， l2tp的直通， 9341的wifi。

2016-6-3
这个文章有在ubuntu16.04下编译 android 6
http://www.68idc.cn/help/mobilesys/other/20160530618129.html

徐刚雄 629那里说9341上的voip需要12m的空间，我们最大能使用的nor flash只能是16m的。

张勇 使用新版本的sdk，一次wifi异常都没有出现。考虑是否把那个拉的动作也去除。ifconfig ath0 down && ifconfig ath0 up对用户体验确实不好。


史朝龙 单ap中5.8g的会出问题，当前已经出了10多个站，能连接上，但是不能ping通，协议连接是未连接。其中一个站，他刚到开机是好的，半小时后不能连接。颜斌认为是速率的问题。那么改成单流的速率就可以连接了，难道是其中的一个天线出问题了？先这样处理了，速度比原来有减慢。
到另外一个基站，2.4和5.8都搜不到，但是进入系统现实没有发现问题，让他搜索一下周边ap看看。

在ath_xmit.c中ath_buf_set_rate函数中增加打印，发现所有0x8x的值，其txpower_cap，都是40。那我把假的校准值变得小一些，来打印看看吧。还是40，那么说明在ath_xmit.c中，似乎只处理iwconfig ath0 txpower设置的值。

如果在ar9300_xmit_ds.c中的ar9300_set_11n_rate_scenario中对有txpower的地方进行打印，如果eeprom中设置的是10，那么设置的值是24, 其他的设置的是34。那么我在eeprom中这样做吧：p_pwr_array[ALL_TARGET_HT20_7] = 38; 感觉没有作用啊，还是24.

张勇 下午用版本搜索了一下，确实一个wifi异常的错误都没有报。许多设备流量看起来也有不少。当前富桥升级了80多个设备。还有两个问题是：root密码要修改，程序会挂掉。那些运行时间短的，登陆上去看/proc/tozed/lastboot是reset by watchdog，这样看来应该是程序出现了非法错误。

郑杏泉 问脚本是否可以实现位操作，建议还是算了吧，脚本写运算就是坑。

2016-6-2
严峻 四川移动拉光纤到用户门口后，想用一对5.8g的cpe把信号传到用户家中，需要组播支持。当时是在ap和cpe上增加了mcastchance来支持组播通过的功能，然后有两种方式，一个是定时写寄存器，一直让所有的包通过。一种是监听组播包，每秒自己发送一个组播join包过去。两种方式好像都有问题，一直让所有的包通过，貌似是ftp下载有问题。而每秒再次发送组播join包, 有什么问题不记得了。以前的日志也没有对应的记录了。

颜斌发了一个ap-c5 2c的版本给严峻，让他自己去输入macastenance指令去测试。

李柱栋 云os和android是不同的系统，兼容了android，如果采用yunos，资料应该会比较少。

9341 voip评审， 软件方面是要对i2c器件进行模拟。

5寸彩屏的固定台：将使用android6的系统。

2016-6-1
李瑶 是否采用tplink的无线设置方式？
张勇 不小心把master rebase到了一个分支上，貌似没有办法恢复了。
李柱栋 吉林那里还有回声抑制和呼叫未接听的处理问题。
张勇 解释了一下openwrt的网络设置的基本设置。
张勇 24a的程序vlan还是有问题。

ar9300Set11nTxDesc这个函数里面的txpower看起来永远是40.

通过抓包等看数据，还是在0x87的速率上功率非常低，当强制设置到其他速率时，看起来是正常的。通过写所谓的寄存器变大时，没有效果。但如果写这些寄存器改为较小的值，确实有了限制。
抓到的包中大量存在block ack这样的包，这个包总是用24m的速率发送的。而这个速率，是ofdm的0x9这个值，但是我在程序中已经把所有的非ht20的速率都改为了ht20

2016-5-31
openwrt下的网络配置其实有些奇怪的，不过张勇、郑杏泉还是把管理vlan确定了。
郑杏泉 下载了某个软件编译成so后，网页上可以进行搜索了。
余小虎 4g固定台入网当前有两个问题，一个是不识别某个实验室的卡，一个是没有开放上网，所以其射频没有测。
严峻  有个站只有代理这个用户，测试机顶盒看直播，有时候会卡，再卡的时候，连接电脑看直播是好的。
金晶 网页改成中兴的样子，页面非常多。
夏荣平 那个带5寸屏的固定台采用什么样的flash和内存？
陈良 富桥要把部分ac放到路由器下面去，这样portal的推送压力就能被分担。然后要增加一条修改admin密码的指令。

新的ath9.5中的wlanconfig的数据结构改变了，导致取的client不断增加。

2016-5-30
/proc/net/dev中打印的貌似在net/core/dev.c中的dev_seq_show中。应该是tx_bytes这个变量吧。

现在查到ath_net80211_tx_complete这个函数在原来的sdk中有不断的调用，而新的sdk中没有。

2016-5-28
1 cenos最新版来编译ath9.5: yum install wget gcc ctags gcc-c++  sharutils
 uuencode: command not found 对应的是sharutils
2 dlink这个路由器直接不能过vlan的包，考虑淘汰它。
3 感觉win10会去掉虚拟机发出的vlan包。算了还是使用存linux系统吧。
4 来刷cpe-df吧
setenv ipaddr 192.168.19.118 && setenv serverip 192.168.19.100
tftp 0x80060000 tozedcpe-df_ap123-jffs2 && erase 0x9f010000 +0x6d0000 && cp.b $fileaddr 0x9f010000 $filesize
tftp 0x80060000 vmlinux_routing.lzma.uImage && erase 0x9f6e0000 +$filesize && cp.b $fileaddr 0x9f6e0000 $filesize
5 ft230x在win10下面终于可以使用了，要在ftdichip.com网页上下载那个vcp drivers里面的驱动。
6 为什么w11下载ap-cp的程序，无线部分会狂吐东西，下载cpe-df的就貌似没啥出来。

2016-5-27
1 富桥希望天线做修改，不要被板子挡住，徐刚雄说已经在做一个这样的板子，是mtk的。但富桥显然不会接受mtk的方案。
2 富桥按安装了一个影视城的地方，重启的非常频繁。
3 如果是使用编译好的编译器编译ath9.5，那么要安装make
4 vm12对ubuntu1404就不能自动安装了。
5 断开网络安装速度就快多了。
6 ubuntu14的apt-get貌似就很不好用了。update全是错误。也许不应该选择hk吧。
7 好像ubuntu14换到请求美国地址，同样apt-get update也无法得到数据。
8 用ubuntu14.10desktop来试试吧。它可以进行自动安装的，也许是那个ubuntu1410server有些问题，删掉，重新下载一个。
9 14.10desktop也同样没有用，就要放弃ubuntu1410了，太快了。
10 好吧，总算从网页下载的14.04server看起来还可以使用apt-get。
11 在虚拟机内3分钟编译完成。
12 在249这台32位的机器上，编译出来的gcc是无法运行的。
13 如果是ubuntu16,04还要增加zlib1g-dev这个东西。
14 王伍 在屏蔽房，9341可以到40m，在外面，一般都只有20m了。
15 赵金 ebtable编译进去后执行就是非法错。郑杏泉找了个其他版本的android中带有ebtables.
16 联想小新使用fn+f2进入cmos，因为需要修改vt这个选项。

2016-5-26
9:20 atheros平台使用预编译的编译器，还需要复制gcc下的.config文件。否则复制库时会报错。
9:29 使用预编译的，在77上不能编译。
9:30 使用预编译的，如果先make clean，又重新下载各种包了。
9:35 我自己的机器上如果重新clone，update这个程序编译过不去。
10:12 原来是少复制了一个路径，但是既然kernels中有，就改一下-I算了。
11:12 张勇 程序退出是有个printf的%写错了。有编译告警。所以要清除所有的编译告警。
11:24 在虚拟机的ubuntu16.04上也编译错误。
11:39 貌似使用了固定的目录来进行编译，真的是好悲催。

2016-5-25
有一台吸顶ap不停的重启。好像是ifconfig ath0 down && ifconfig ath0 up必然重启。
王伍： 富桥还想做一个5.8g的吸顶ap，定向天线的ap。
富桥现在对重启没有太大的意见了。相对不能使用，用户断一下，半个面包总比没有面包好。
10:36 王伍 键盘改为中断方式可以安排赵金完成。
金晶 汪光华 如何统一时区设置。
王伍 要苗立双去做9x07这个平台。
11：43 当前这个ap出现了无法连接的情况，打开iwpriv ath0 dbgLVL 0xf0000后，手机试图连接出现：     vap-0: [80:22:75:1a:60:4b]ieee80211_node_saveq_cleanup 0 sta's in ps mode
如果打开iwpriv ath0 dbgLVL 0xf00000 ，那么会出现：
vap-0: [88:32:9b:eb:96:d9]recv auth frame with algorithm 0 seq 1
vap-0: [88:32:9b:eb:96:d9]ieee80211_alloc_node: vap=0x83d3c000, nodecount=2, ni=
0x8391f000, ni_bss_node=0x8391f000 bss_ref=2
vap-0: [88:32:9b:eb:96:d9] num auth'd STAs is 65535, max is 128, rejecting new a uth
vap-0: [88:32:9b:eb:96:d9] send auth frmae
 vap-0: [88:32:9b:eb:96:d9]ieee80211_sta_leave: 0x8391f000
vap-0: [88:32:9b:eb:96:d9]node_cleanup: vap=0x83d3c000, nodecount=2, ni=0x8391f0
00, ni_bss_node=0x83a0c000 bss_ref=5
vap-0: [88:32:9b:eb:96:d9]station free
vap-0: [88:32:9b:eb:96:d9]_ieee80211_free_node: vap=0x83d3c000, nodecount=2, ni=
0x8391f000, ni_bss_node=0x83a0c000 bss_ref=4
vap-0: [88:32:9b:eb:96:d9]node_cleanup: vap=0x83d3c000, nodecount=2, ni=0x8391f0
00, ni_bss_node=0x83a0c000 bss_ref=4
如果打开iwpriv ath0 dbgLVL 0xf000000
会出现大量的vap-0:  discard unhandled information element id 74, len 14
如果打开iwpriv ath0 dbgLVL 0xf0000000
会出现大量的： vap-0: ieee80211_add_htcap_pre_ana: use HT caps IE pre-ANA

16:34 生产的来电话，说5.8g cpe升级到17c之后，搜网到100%后，有10%的机器不动了，重启也无法访问了。
富桥在阿里云上的服务器远程桌面非常容易停止响应。
17:50 刘云 原来周坦的笔记本上安装ubunut14，无线网卡没有出现。


2016-5-24
忙碌的早上。
郑杏泉：使用openwrt_cc这个最新的版本，那么无线的设置有问题。如果使用mtk给的openwrt版本，那么没有vlan的设置。其中的wlan启动脚本也比较复杂，单独运行没有效果。
赵金：使用xdos测试很快4g固定太就重启了，还没有找到有效的防止命令。
曾小星：富桥那里改回了重启次数多的配置，联不上的情况少了。但是重启也是个问题。
刘云：git clone的时候加不加最后的.git是一样的。
金晶：中兴认为web界面太丑了，干脆用中兴的模板来做吧。

2016-5-21
张勇： 目录下面全是readme.eml文件，估计是中招了。
meld中，如果一个文件没有写权限，那么箭头就不对了。
要增加模块卸载。
要增加update程序。


2016-5-20
1、看了一下dialog的测试结果，把几个没有加入的项目加入了4g固定台表中。
2、9341的无线，在富桥使用的中，还存在故障无法自动恢复的情况。考虑重新使用新的sdk来做一个。

下午了：
包雪峰：内蒙，某个地市要出特别的5.8g的程序。这个程序如何没有设置pppoe帐号，那么就没法拨号上网。
新的印度吸顶ap测速比较差。后来说是选择的信道问题，选择了6。选到13就好多了。
白俊剑 voip未授权，应该是mac不对。
张勇： 印度ap刷机后ath0不能加入网桥的问题是没有校准的原因，梁剑把cpe上已经校准的校准区写入有问题机器后，就可以了。
吴曦  还没有问无线抓包网卡是什么型号。

2016-5-19
上午的几个事情：
赵金把读写imei改为dll，并必须用ukey是可以做到的。
颜斌mtk是两层板，硬件上能否正常出来还有问题。
袁阳下午去极智联和商谈具体的生产事情。
张勇：如果上来就编译cpe-ap，那么会出现ath0无法加入网桥的情况。
白俊剑：开始测试voip，组建网络。
赵金：准备使用netstat来判断攻击ip，然后用iptables去禁止它。
张勇： 富桥反应，如果使用限速6m的配置，那么报wifi异常的次数就会减少，但联不上的情况就会增加。现在又把配置改了回去。
金晶：web可以给多个普通用户。喻潇：两个就可以了，一个超级用户，一个普通用户，普通用户用户名可以修改。
吴曦：当dhcp设置为2个用户时，第三个手机无法得到ip，断开连接中的其中一个，第三个手机马上能连上了。
金晶： linux下也可以使用adb

12:01 ar5416_11g_table中去掉cck中数据，看起来ap没有起来。
13:51 手上这个板子貌似总是启动不了无线了。
14:22 感觉编译脚本中的再加一次那个_ap123有问题，编译后程序wifi不能启动了。
15:12 烧了一个张勇编译的程序，也是这个样子。
15:40 用两个程序对比打流测试吧。使用三星手机：
nob :     23.738     9.321     6.313   16.535    7.178    15.253    avg:  13.056
normal: 12.908     4.351   10.159     8.322     9.658    12.041   avg:    9.573
nob:      23.884   23.429   18.041   18.261   18.400    18.443   avg:  17.009
normal: 15.016   14.576   11.339   16.066   14.539    12.707   avg:   14.040
nob:      20.527   18.496   12.765   12.769   12.739    10.566
normal: 17.870   13.693   12.610   12.548   12.536    12.628
后面的事情：
1、修改去掉72m等，但是颜斌抓数据包还是能看到


2016-5-18
9:10 印象笔记的搜索居然不支持搜索带空格的字符串，搜两个。
郑杏泉：派联给的openwrt里面没有wtk的内容，那和网络上下载的有什么区别。
9:21 郑杏泉 openwrt_cc中支持7628的。不过是在原来那个rt2xxx的里面。
9:53 张勇 忘了对灯的寄存器修改了。
富桥那里又没有报非常大的问题了，对重启的问题也没有再说。只有上次他们老板有些莫名其妙的咆哮。
10:06 使用我的手机，使用全sdk9.5，0.33%
10:13 那个w13居然内核报错，再也不能启动了。换一个p10p来试试吧。
10:23 使用p10p的丢包率在0.33% 7.542/13.658/106.397，似乎没有必要使用ping包工具来测试了。
10:51 富桥那里查了一下表，每天由于wifi错误重启的总次数在300-500次左右，有一个ap在15日重启了60次。
11:53 张勇 富桥反应有一批设备不能登陆。
endpoint这个要用兼容模式才能运行。
11:56 使用我的苹果手机， p10p，打流平均速度是32.229

后来的几件事情：
1、新的生产厂家需要自己做生产工具，需要提供写imei，检查imei, rssi，版本等信息。王伍坚持需要用我们提供的ukey。需要问一下赵金，是否能做一个dll，这个dll也需要ukey才能运行。
2、当前生产做最后的版本检查，还是肉眼看，赵金的工具喻潇觉得不好用，就没有发给生产。
3、富桥哪里有一个区大量的不能上网，富桥认为是vlan设置的问题。
5、颜斌想用派联的sdk，但看起来派联有抵触。
6、金晶看起来比较想做android的系统，我说还有tr069的系统等着他，有些失望的样子。


2016-5-17
金晶 脚本中的变量赋值中，等号的两边不能加空格。
刘小虎 贵州需要用农宽设备来做专线，但移动那个人也说的不是很清楚。按理来说是可以实现的。
彭广才 赛特尔同意给我们做一个板子，键盘会给我们调好。
9:50 张勇 来问extap， wds, repeat的概念。看起来应该写到ppt中去。
10:32 完全是新的sdk，那么喻潇的手机丢包率只有0.32%了，7.288/16.507/63.785ms
再来一次吧：为0了，8.017/14.980/73.281ms
再来一次吧：有电话进来了。
是不是要刷回原来的程序来试试？
11:26 金晶 想把所有的iptables脚本放成一个文件。
汪光华 赵金说下了配置后telnet服务打开失败。
张勇 led的那个程序要改动貌似有些复杂，是否要重新了一个。
喻潇的手机再测试： 0.33% 7.919/18.045/456.764ms
再次测试变成0啦： 0% 7.276/15.484/40.285ms
看起来不错啊，不知道其他方面怎么样。
13:40 使用我自己的手机则还是有2.32% 7.310/42.895/745.018
14:13 斯里兰卡的服务器地址是172.16.1.1，帐号密码是：
0113600332-2661429174143
0113600333-273142A174144
0113600334-283142B174145
0113600335-285142C174146
0113600331-2651428174142
14:48 这一次要差一些 1.32%, 8.044/100.195/1266.058
15:17 安装郑杏泉给的一个驱动后，笔记本终于可以使用sml下载工具了。
16:00 这次喻潇的手机又是0, 8.156/14.990/79.166ms
16:06 拿一个原来的设备来对比测试吧：这一次好像也是0 啊。
这一次是1.97% 8.83/33.441/1640.383
再来一次是0% 8.5/19.346/705.688
16:37 那么拿一个w11来测试吧：0.32% 7.955/36.049/598.399
再来一次吧：0% 7.978/15.829/72.333 算了，今天认为都是好的吧。
16:59 忘记写了，彭广才，p10p要做很多，希望加快校准的速度。
17:15 金晶 升级后，telnet不能进入了。
18:06 吸顶ap从加电到进入校准状态27秒，而p10p的时间是42秒。
22:00 颜斌 印度ap做成柱状灯陈玉说没有和她说，这应该是当时印度人提的需求。

2016-5-16
8:47 喻潇 还没有看李柱栋的文档。
9:01 刷了一遍机器怎么还有以前的文件？
9:07 好吧，这次出现了bummer, could not run '/sbin/getty': No such file or directory. 晕死，把擦除区扩大就可以了。
张勇 比较了当前的ap-cpe和以前的参数，看起来都是一样的。
9:40 余小虎 有一台机器打过静电就显示完全不对了。
升级了一台机器，还是网络没有启动。
10:21 金晶 修改的文件运行cool后恢复原样了，这个设计确实也存在问题。
苗立双：tr069编译有问题，但重新操作又能编译了。
10:36 朱建文 管理包改为6m发送他也没有做过，是其他厂家改的思路。
12:00 喻潇的手机连接结果是这样：丢包率2.97%  8.482/27.189/2080.179ms
13:52 77 上对perl5.22这个分支进行编译。可以编译通过了。
14:28 新的openwrt要求安装subversion，还有sudo apt-get install libssl-dev
14:48 吴曦 王伍的机器升级后wifi没有启动，后来又能启动了，这真的让人头痛啊。
15:06 张勇 不能访问加密的wifi的原因居然是brctl setfd br0 0这个脚本没有执行，真的不了解。
15:25 吴曦 怀疑是程序生成的那个脚本还没有生成的原因。
15:26 249上开始重新编译。
15:34 拿喻潇的手机来，发现无法连到这个sdk9.5编译的ap上了，从串口上看到奇怪的报错：ath_open: unable to reeset hardware; hal status 14(freq 2462 flags 0x1000)，apdown  apup无效，重新启动能看到了。
15:42 喻潇的手机， 300个包2.31% 7.844/68.242/2104.206
那么关掉wmm看看吧：关掉就没有问题，丢包0。听说关闭wmm就是g模式，那么如果开启puren那么是不是就很差。
16:28 吴曦 如果总是没有tzphone生成的文件，那么还是继续跑下去吧，不要退出了，导致网络都不能使用。
16:32 白俊剑 配置文件增加字段必须加在结构最后，但吴曦把它加到了中间。
19:20 给李光达刷的机器没有ssid出来，iwconfig看txpower是50db，设置了也没有用。ath_open: unable to reeset hardware; hal status 14(freq 2462 flags 0x1000), 刷一个完全用sdk9.5编译的就可以，不会出现问题。
20:00 张勇 梁剑 测试了ap模式下的bridge模式，上联口使用的是p10，可以互相ping通。


2016-5-14
18:48 在笔记本上串口看起来是没有乱码的，而台式机上总有那么些。
要安装那个盗版的驱动串口才能使用。

2016-5-13
10:09 给朱建文发邮件说把昨天会议他说的几点再催一下。
10:25 李柱栋 voip使用阿里云，声音还有一点点延时，收听有偶然的缺失。希望他把wiki百科或者其他方式的知识记录和共享建立起来。
李瑶 认为当前没有什么简单的东西给姚国梁来做，找些书给他。
吴曦 找到了udhcpd这个程序的位置。在external/udhcp-0.9.9中。
金晶 一天有130万的日志记录。有些文件没有更新到，应该是没有写到cool中的更新列中。我这台机器的信号显示不对，但是他的机器上看到的信号是满格。
张勇 富桥希望把网管做到linux上面，windows系统总是受到攻击。配置参数测试wifi，非常难得到对的数据，也不知道好不好是不是修改参数的结果。
熊立宇 要测试一下配置工具。
11:16 键盘还是要改为中断的方式，后期还要做掉电注销网络。
15:56 简单写了一个wlan的说明ppt。
16:23 吴曦 wlan_8192c.sh使用网页升级，总是没有执行权限。
单总 印度程序最终还是要满足客户要求。
王伍 考虑在1860上用w13的mtk芯片代替riltek芯片
16:28 atheros新的9.5版本的sdk, sudo apt-get install exuberant-ctags
16:31 atheros新的9.5版本的sdk，看起来一点要解压special这个包。
16:34 新版本编译出来的无线驱动还要小一些。
17:03 余小虎 pull --rebase出现冲突时，add后做了commit操作。应该做rebase --continue。
17:32 vim的替换   :s/vivian/sky/g 替换当前行所有 vivian 为 sky
:n,$s/vivian/sky/ 替换第 n 行开始到最后一行中每一行的第一个 vivian 为 sky
17:40 如果复制9.5的wlan过到原来的sdk中，hostapd编译错误。原来也碰到过吧。都不记得原来怎么处理的。对啊，在后来的10.1版本上碰到过。
18:05 张勇 印度小ap作为cpe时，去连接有加密的ap有问题，不能连上。
18:23  git remote add 249 ssh://jian@192.168.1.249/home/jian/work/bigap/.git 这样才能呢过连到其他机器上的仓
20:17 张勇 刷个cpe的程序可以连。
22:30 白俊剑 脚本不能用dos的工具新建，但是原来的脚本用si改都没有关系，不会出现^M这样的东西。

2016-5-12
8:56 昨天姚国梁修改了程序，在他那里master下可以编译p10p的程序了。我这里确实也编译过去了。
王伍 中兴有个实验网我们的话机注册不了。
9:06 金晶 从凌晨到现在，ap历史表11万记录，用户记录30多万。
9:17 吴曦 tzphone一起来就设置参数，无效。如果用tzphone load_wifi这样的写法那么屏幕会闪。
9:32 金晶 在linux下的si，不能输入中文，但可以在它的搜索界面中输入中文，然后复制，粘贴到代码中。
10:25 77和249上的ip命令结果还不同。ip l2tp add tunnel tunnel_id 3000 peer_tunnel_id 4000 encap udp local 1.2.3.4 remote 5.6.7.8 udp_sport 5000 udp_dport 6000这个命令，77上RTNETLINK answers: Protocol not supported，而249上直接Object "l2tp" is unknown, try "ip help".
10:29 虚拟机内的ubuntu16.04执行貌似正常，还出现了一个l2tpeth0这个网卡。
14:04 629要加spi支持。但是spi_gpio没有可以选择的地方。
王伍 l2tp可以不用管v3之类，只要能借用国外的4g网络调试程序。
金晶 已经60多万数据了，那么一天超过100万是必然的。
熊立宇 如果不加sync，那么10次有6次会没有写入配置，如果加上了，那么试过多次，没有出现过。
14:16 linux下，不知道如何使用iw改变信道。
14:26 使用wireshark开始抓包后，就可以使用sudo iwconfig wlan0 channel 11来改变信道了。
14:38 虚拟机内的ubuntu居然重新启动不超过10秒，太惊人了。完全关闭vmplayer，再开启进入的速度也是非常的快的。
15:36 吴曦 在程序中生成脚本，再wifi的脚本再调用，wlan_8192c.sh会被调用多次。当前貌似正常了。
17:27 来atheros，atheros有usb3.0的芯片是 4018+8075/2 ，价格在12美元。arm构架，4核。openwrt。便宜的是9531, 2.2$，比9341便宜。加强无线的措施有：修改control_table, 将管理帧改为6m发送，改burst值，调cwm参数。
说道atheros的缺点还有就是一定要校准，非常费人工。加上pa后功率还是不够。成本高。
18:21 李柱栋 启动的第一次以太网的mac是随机的。这应该是正常，ubi刷完之后有个fixed up过程，这样文件系统就应该没有加载了，以太网的驱动读取的是/amt中的文件。
20:15 笔记本上以太网驱动又变成5.5日的了，没事自动升级做啥？
20:41 印象笔记的网页版真的很难用。速度超慢。

面谈小结：

汪光华： 似乎对自己的评价并不高。说自己还是不够聪明。

李瑶：在武汉买了房子，可能明年撤退。提出了代码重复的太多，没有统一的接口和精简。
赵金：提出在向别人提出需要帮助时，有些人有不耐烦的时候。
张勇：早上上班的时间有些赶，能否放宽一些。
吴曦：希望公司给出盈利后给出多少来改善待遇的具体值。老婆怀孕了，需要照顾。
刘云：1一件事最好不要多个领导来催，比较影响效率。2即使没有量产的项目也应该在测试结束它，不必等到要量产的时候又手忙脚乱。
白俊剑：公司可以花小钱办大事。出差补助10年没有提高了。
李柱栋：出差补助10年没有变了。小房间有不努力的情况。知识共享。产品向智能化专业化发展。

2016-5-11
8:49 vm中跑ghost的时候，会跳找不到文件的错误。算了，还是按照那个上海政府版吧。
9:00 vm安装xp貌似也非常快啊，已经进入系统了。但在窗口模式下，它点不到内部的状态栏。还有一点，内部的网卡总是自己会断开/连接。
9:09 usb设备也没有到虚拟机中。
9:16 感觉是连接了4g固定台就会出现虚拟机网卡断开的情况。
10:13 王伍 刘子军测试10多分钟后会掉下来。
10:17 喻潇 和金晶讨论网页的问题。
http://mirrors.163.com/ 是网易的镜像站点。
10:40 张勇 9341和w13一起打流，w13几乎没有影响，9341的掉到1-2m。
使用linux下的wireshark就可以直接抓到无线包了。而且有解析。
吴曦 把dhcp换成其他网段没有试过。
10:46 来使用若干个linux的系统来测试各个产品的编译吧。先用64位的12.04吧。
10:51 吴曦 修改了dhcp参数可以ping到，测试是喻潇的机器不可以，吴曦的机器可以。
11:45 张勇 富桥的老板薛雪峰打电话过来，说用户投诉很多，经常重启的问题要解决。从金晶查数据来看从昨天开始有100多个设备出现wifi异常的情况。
13:53 ubuntu 12.04的server光盘上似乎没有git,不过现在居然还可以从apt-get来，不过要先安装写别的东西。
14:05 http://mirrors.sohu.com/还有非常早期的ubuntu版本。
14:10 在ubuntu 12.04上要安装一个gcc看起来有些困难啊。各种库没有。算了，不折腾了。要折腾也折腾新版本的linux.
15:16 ubuntu15.04看起来openswan已经没有在ubuntu的软件仓中了，看起来是有strongswan的。
15:45 bigap分支ubuntu14.04在249上成功编译cpe-8m。还有77上也试试吧。
15:47 ubuntu14.04上倒是可以apt-get install openswan。怎么变化会这么多呢？
15:52 为什么77上就不能免密码登陆呢？奇怪的事情。
16:05 bigap内，使用build目录下的make BOARD_TYPE=db12x clean会报错，而到linux的目录去，make clean就正常跑了。
16:11 廖中举来电话，移动测试单ap，设备在楼顶，在楼下搜索发现信号值很差，80多，联上后显示又有40多，可以上网。ssid使用的是唯一的字符串，没有和其他重名。
16:43 找了半天，也没有找到原来给工程的如何取扫描的日志文件的。
16:48 吴曦 如果tzphone中不对wifi进行处理，那么自动信道是可以找到不同的信道的。王伍让他在init.sh之前就设置好参数。
16:57 扫描保存的文件是temp.log，为什么那个邮件就找不到了呢？
17:10 金晶 想用select  into， delete from的方式每天修改日志记录。
17:18 给廖中举发两个邮件，一个是cpe-df 32a，一个是取log的。
17:31 颜斌未碰到过搜网很差，而连上很好的情况。把ap的txpower改为23则稍微稳定一些。
17:38 下载一个“华文楷体”的字体后，陈曦发的文档看起来正常多了。
18:10 https://hjc.im/shi-yong-strongswanda-jian-ipsecikev2-vpn/ 这个链接有strongswan的配置说明，以后再看吧。
18:19 l2tp v3 使用的文件是这个((CONFIG_L2TP_V3)) += l2tp_netlink.o，目录在net/l2tp中。
18:27 l2tp v3有三种链接方式: lns - lac lac-lac
18:58 77上编译bigap cpe8m居然用了3163秒。
18:59 如果用rename table, select into原表的方式，那么原来的依赖和约束都没有了。
19:40 http://manpages.ubuntu.com/manpages/xenial/en/man8/ip-l2tp.8.html这个链接说明无状态的l2tp。
20:57 win10的共享无论输入什么密码都过不了。
20:59 vmplayer安装ubuntu的时候什么也不用选，直接就开始安装了。这样也有一个问题，就是没法制止它安装的时候不去联网。
21:10 姚国梁那里master下面27h是可以编译的。
21:26 虚拟机器的ubuntu 16.04安装完成了。这样安装的ubuntu，其源总是跑到美国。

2016-5-10
8:58 boxes这个东西重启后貌似又能用了，但是你查看了device后，又不动了。
昨天还问了一下喻潇，她还是希望不同产品的做配置的工具分开，原来的都在一起是因为全是话机，配置项目都是一样的。
10:24 单总开会，说了几件事情。一个是移动可能在8月底完成对4g cpe和自助设备的招标。局面非常严峻。讨论是否要对新的外壳模具进行入网的问题。担心一个室外型出货量比室内型多的多，其他厂家必然有所动作，比如提高防水等级，fdd要求等。
另外一个问题是我们的成本太高，已经比其他厂家的出货价还高。供应链体系还没有建立起来。有些小厂能拿到比较好的价格。
10:29 在ubuntu 14上面，vmplayer看起来是正zlib1g-dev常的。不行把笔记本上的ubuntu换掉？
12:24 继续面谈白俊剑，赵金，汪光华。
赵金选择：苗立双，梁剑，李瑶
白俊剑选择：李柱栋，郑杏泉，余小虎。如果只选择一个人，那么是苗立双。
汪光华选择：白俊剑，吴曦，余小虎。
12:29 使用ubuntu server对bigap进行编译，需要安装的包：make gcc bison flex gettext g++ libncurses5-dev zlib1g-dev:i386 autoconf automake libtool
14:05 吴曦 问三种加载配置的方式，想对sysconfig等进行整理。
16:04 面谈只有陈良了。
刘云选择了： 苗立双 张勇 郑杏泉
李柱栋选择了：白俊剑 余小虎 郑杏泉
李瑶选择了：李柱栋 梁剑 陈良
16:06 余小虎问自动拨号，手动拨号的问题。网页上的设置是能起作用的。
20:31 苗立双发出的对姚国梁的git提交的检查，有些姚认为是不同机器的编译生成的文件不同。
22:00 那么我这里统计的结果是： 郑杏泉 李柱栋 4票， 白俊剑 苗立双 余小虎 张勇 3票 李瑶 梁剑 2票 陈良 吴曦 汪光华 1票。 金晶 赵金 刘云 为0

2016-5-9

今天貌似说了一天的话。

早上王伍说4g固定台还需要增加的功能。就说到了10点。然后呢，和张勇、王伍说wifi那个轮着发包没有起效果的问题。再是开wifi问题的会议。
下午呢，三点之前和白俊剑一起把增加的问题列入表格中，三点开始又开始说4g固定台的事情，一下子就开到了4点办。
在进行了金晶，张勇，梁剑，吴曦的面谈。
金晶希望合作的人是：郑杏泉，白俊剑，李柱栋
梁剑希望合作的人是：苗立双，李瑶，张勇
吴曦希望合作的人是：汪光华，李柱栋，张勇
张勇希望合作的人是：
苗立双终于搞了一下那个gpio的事情，原来是以太网也在操作gpio。

2016-5-8
9:42 我的机器上的box就只能安装xp的windows，其他几个, win7, deepin都失败。
9:54 mm clean貌似把所有的clean了。
10:07 ubuntu 16中的/etc/default/rcS中已经没有UTC=yes这个项目了，那么直接加上UTC=no看看吧。貌似是没有用的。
10:35 boxes中的xp不能ping但是上网是可以的，真的很奇怪啊。
10:50 在boxes中的xp安装联芯的工具，最后报"无法定位程序输入点encodepointer于动态库kernel32.dll上"，不过安装程序似乎继续了。

2016-5-7
14:39 有两台机器出现了wifi没有启动的情况，针对其中一台进行了折腾。boa没有启动, wlan0也没有出现。直接运行init.sh，没有出现昨天的那个无资源的情况。查到每个va0-4的wlan-disabled都是0，而正常的机器 都是1, 再发现boa中的那个setting.bin文件为0自己，按照mifi_start.sh中的命令，把/system/etc/mifi/boa目录下 的文件复制过来，那么就再运行init.sh，wifi就正常了。
陶嵩他们也碰到一台wifi不能起来的机器，一直都不能起来，重新刷机后正常。应该也是这个问题。
20:47 ubuntu 16 居然没有win在软件中心中。14还是可以直接装的。按照winehq主页上的安装指南，居然要600多m空间了。

2016-5-6
8:35 ubuntu 16.04上面的box貌似有usb的连接配置了。
8:38 感觉运行box的时候笔记本很难从黑屏恢复了。
8:59 让张勇改王伍的想法。
11:27 从赛特尔通讯回来。需要重新做版。
box里面安装的xp貌似卡在开机上了。
12:11 强制重启一下box中的xp，启动了，但是貌似网络不能出去。
颜斌：方陈确实有些情绪，一是感觉做的产品没有卖掉，另外是充电没有按照王伍的方式有充电显示被骂了心情不好。
12:20 /proc/sys/net/ipv4/ip_forward已经是1了。
12:30 我自己使用的机器也出现了没有wifi的情况。
13:00 eddy lin来问gpio不能控制的问题。
14:04 不能启动wifi的机器会报ifconfig: SIOCSIFFLAGS: Device or resource busy这样的错误，wlan0无法正常up
金晶 香港阿里云的服务器需要续费了。
14:27 金晶 碰到了查询拼命吃内存的情况。
吴曦 正常的机器也有cat: data/var/boa/rtl8192c/wlan0-vxd/ssid: No such file or directory这个错误。
14:49 网上有报boxes不能访问网络的，还没有找到解答。
15:22 吴曦测试了40-50次开机，每次wifi都启动了，奇怪啊。
15:27 李柱栋 如何把sip放到系统中。还是用tzphone里面的复制过程吧。
15:44 安装了vm player，出现Could not open /dev/vmmon: No such device.的错误。
15:45 刘云 看wifi看哪里呢？那么先看nvram和寄存器吧。
15:48 运行 sudo /etc/init.d/vmware start 出现 virtual machine monitor failed和 virtual ethernet failed.
16:38 李柱栋 system中的sipclient居然没有运行权限。
张勇 修改后有效果，但是4分钟后打流会停止。
eddy说还是无法控制gpio，回头要找个板子来试试。
17:08 看了一下张勇改的程序，还没有做到每个buff发一次，而是每次清空所有的buff，就已经出现了效果。如果不开，那么两个机器的速度在20和8，开了15和12。
17:34 使用徐刚熊给我的新的串口，貌似没有乱码了。
18:22 还是有些乱码的。为什么gpio 18等不受控制呢？
22:06


2016-5-5
14:06 开了一个早上的会议。主要是要增强wifi的功能。
李东风测试的结果看来还可以，还要增加对acktimeout的设置，增加对5个信道的设置。
节前键盘不响应的原因居然是扩展gpio的那个芯片送错了。
14:14 汪光华修改了中英文切换后“中国移动”显示错误的问题，每次都去查表，应该也问题不大。
14:31 廖中举电话问题单ap是否有光口。说有些单ap用了一年后速度变差，原来测速有10m的，后来测速就只有2m了，只有换设备。
16:50 在一台新的机器上编译bigap，出现了没有bison，没有termcap libary的，安装libncurses5-dev。
17:14 余小虎从网页那里下载tzphone的log结果没有下载，而且/tmp下的打包文件也是空的。
17:31 金晶 原因是压缩文件的时候使用了gzip这个文件，而这个文件是临时建立的一个链接到busybox。
17:44 继续编译，出现了这样的错误Can't use 'defined(@array)' (Maybe you should just omit the defined()?) at kernel/timeconst.pl line 373.

20:37 吴曦，喻潇，白俊剑，苗立双讨论配置加载。原来的4g cpe有三种加载配置的方式，生产工具加载、网页上传和远程网管加载。其中生产工具加载会清除保存的锁卡、锁的基站信息等数据，而网页上传加载配置不会。 生产工具加载和网页上传加载使用同样的文件名加载。而远程网管加载优先级最高。任何加载配置时，恢复默认配置，加载生产工具加载的配置，加载网管的配置。
21:08 王伍 说使用hao123连续打开网页会出现打不开网页的情况。
王伍 提出在以太网中，一种实现平均分配带宽的办法。
21:32 吴曦 又出现wifi未启动的现象。感觉是那个init.sh没有运行，所以wifi没有，dhcpd也没有运行。
21:49 win10的系统貌似不能使用下载工具啊。
22:00 刘云 p11和w13的协议分析中有个长度计数器使用了char变量，所以在包长超过256时，就有错误发生。

2016-5-4
11:59 开会讨论人员的事宜，涉及到多个人员的评论。
使用tc后，内存有泄露。暂时还没有找到原因。
14:51 使用iperf这个工具，立刻就挂掉了。
17:34 原来是判断buff满这个条件错了。

2016-5-3
13:52 李跃鹏来电话，两个问题，1个是锁小区的时候，当某个小区失效时，是在锁定的小区中继续附着吗，其实应该不是的。另外一个是锁基站的时候是否要输入频点。
早上4g固定台开会。
李总来问wifi的性能问题。
14:14 看了半天的邮件，还没有看完。
14:26 吴曦 来签两个小时的请假单。去苏州发现两个问题，一个是发射饱和，所以很难在n模式下进行传输。一个是抗干扰能力，在发包之前发送一个请求，这个不就是rts么？
14:36 继续看邮件。
14:56 单总来问wifi的问题如何继续。
15:27 张勇 使用自己写的tc那么，如果设置的比较小，打流容易重启。
单总 程总：翰达的4gcpe已经没有模块了，能不能用我们的模块顶上？
余小虎：又碰到一次花屏的情况，无法恢复。
17:56 联想v4000这个机器，总觉得win10下面显示有些灰蒙蒙的。
19:11 把popstr和pushstr加上保护，还是会挂掉。
20:38 和eddy讨论版权控制的问题。当前采用锁mac的方式，正式版本将采用后台服务器注册的方式。
白俊剑：升级搞了半天才好。还有锁机锁卡安装吉林的要求使用iccid进行计算出pin来。

2016-5-8
9:42 我的机器上的box就只能安装xp的windows，其他几个, win7, deepin都失败。
9:54 mm clean貌似把所有的clean了。
10:07 ubuntu 16中的/etc/default/rcS中已经没有UTC=yes这个项目了，那么直接加上UTC=no看看吧。貌似是没有用的。
10:35 boxes中的xp不能ping但是上网是可以的，真的很奇怪啊。
10:50 在boxes中的xp安装联芯的工具，最后报"无法定位程序输入点encodepointer于动态库kernel32.dll上"，不过安装程序似乎继续了。

2016-5-7
14:39 有两台机器出现了wifi没有启动的情况，针对其中一台进行了折腾。boa没有启动, wlan0也没有出现。直接运行init.sh，没有出现昨天的那个无资源的情况。查到每个va0-4的wlan-disabled都是0，而正常的机器都是1, 再发现boa中的那个setting.bin文件为0自己，按照mifi_start.sh中的命令，把/system/etc/mifi/boa目录下的文件复制过来，那么就再运行init.sh，wifi就正常了。
陶嵩他们也碰到一台wifi不能起来的机器，一直都不能起来，重新刷机后正常。应该也是这个问题。
20:47 ubuntu 16 居然没有win在软件中心中。14还是可以直接装的。按照winehq主页上的安装指南，居然要600多m空间了。

2016-5-6
8:35 ubuntu 16.04上面的box貌似有usb的连接配置了。
8:38 感觉运行box的时候笔记本很难从黑屏恢复了。
8:59 让张勇改王伍的想法。
11:27 从赛特尔通讯回来。需要重新做版。
box里面安装的xp貌似卡在开机上了。
12:11 强制重启一下box中的xp，启动了，但是貌似网络不能出去。
颜斌：方陈确实有些情绪，一是感觉做的产品没有卖掉，另外是充电没有按照王伍的方式有充电显示被骂了心情不好。
12:20 /proc/sys/net/ipv4/ip_forward已经是1了。
12:30 我自己使用的机器也出现了没有wifi的情况。
13:00 eddy lin来问gpio不能控制的问题。
14:04 不能启动wifi的机器会报ifconfig: SIOCSIFFLAGS: Device or resource busy这样的错误，wlan0无法正常up
金晶 香港阿里云的服务器需要续费了。
14:27 金晶 碰到了查询拼命吃内存的情况。
吴曦 正常的机器也有cat: data/var/boa/rtl8192c/wlan0-vxd/ssid: No such file or directory这个错误。
14:49 网上有报boxes不能访问网络的，还没有找到解答。
15:22 吴曦测试了40-50次开机，每次wifi都启动了，奇怪啊。
15:27 李柱栋 如何把sip放到系统中。还是用tzphone里面的复制过程吧。
15:44 安装了vm player，出现Could not open /dev/vmmon: No such device.的错误。
15:45 刘云 看wifi看哪里呢？那么先看nvram和寄存器吧。
15:48 运行 sudo /etc/init.d/vmware start 出现 virtual machine monitor failed和 virtual ethernet failed.
16:38 李柱栋 system中的sipclient居然没有运行权限。
张勇 修改后有效果，但是4分钟后打流会停止。
eddy说还是无法控制gpio，回头要找个板子来试试。
17:08 看了一下张勇改的程序，还没有做到每个buff发一次，而是每次清空所有的buff，就已经出现了效果。如果不开，那么两个机器的速度在20和8，开了15和12。
17:34 使用徐刚熊给我的新的串口，貌似没有乱码了。
18:22 还是有些乱码的。为什么gpio 18等不受控制呢？
22:06


2016-5-5
14:06 开了一个早上的会议。主要是要增强wifi的功能。
李东风测试的结果看来还可以，还要增加对acktimeout的设置，增加对5个信道的设置。
节前键盘不响应的原因居然是扩展gpio的那个芯片送错了。
14:14 汪光华修改了中英文切换后“中国移动”显示错误的问题，每次都去查表，应该也问题不大。
14:31 廖中举电话问题单ap是否有光口。说有些单ap用了一年后速度变差，原来测速有10m的，后来测速就只有2m了，只有换设备。
16:50 在一台新的机器上编译bigap，出现了没有bison，没有termcap libary的，安装libncurses5-dev。
17:14 余小虎从网页那里下载tzphone的log结果没有下载，而且/tmp下的打包文件也是空的。
17:31 金晶 原因是压缩文件的时候使用了gzip这个文件，而这个文件是临时建立的一个链接到busybox。
17:44 继续编译，出现了这样的错误Can't use 'defined(@array)' (Maybe you should just omit the defined()?) at kernel/timeconst.pl line 373.

20:37 吴曦，喻潇，白俊剑，苗立双讨论配置加载。原来的4g cpe有三种加载配置的方式，生产工具加载、网页上传和远程网管加载。其中生产工具加载会清除保存的锁卡、锁的基站信息等数据，而网页上传加载配置不会。生产工具加载和网页上传加载使用同样的文件名加载。而远程网管加载优先级最高。任何加载配置时，恢复默认配置，加载生产工具加载的配置，加载网管的配置。
21:08 王伍 说使用hao123连续打开网页会出现打不开网页的情况。
王伍 提出在以太网中，一种实现平均分配带宽的办法。
21:32 吴曦 又出现wifi未启动的现象。感觉是那个init.sh没有运行，所以wifi没有，dhcpd也没有运行。
21:49 win10的系统貌似不能使用下载工具啊。
22:00 刘云 p11和w13的协议分析中有个长度计数器使用了char变量，所以在包长超过256时，就有错误发生。

2016-5-4
11:59 开会讨论人员的事宜，涉及到多个人员的评论。
使用tc后，内存有泄露。暂时还没有找到原因。
14:51 使用iperf这个工具，立刻就挂掉了。
17:34 原来是判断buff满这个条件错了。

2016-5-3
13:52 李跃鹏来电话，两个问题，1个是锁小区的时候，当某个小区失效时，是在锁定的小区中继续附着吗，其实应该不是的。另外一个是锁基站的时候是否要输入频点。
早上4g固定台开会。
李总来问wifi的性能问题。
14:14 看了半天的邮件，还没有看完。
14:26 吴曦 来签两个小时的请假单。去苏州发现两个问题，一个是发射饱和，所以很难在n模式下进行传输。一个是抗干扰能力，在发包之前发送一个请求，这个不就是rts么？
14:36 继续看邮件。
14:56 单总来问wifi的问题如何继续。
15:27 张勇 使用自己写的tc那么，如果设置的比较小，打流容易重启。
单总 程总：翰达的4gcpe已经没有模块了，能不能用我们的模块顶上？
余小虎：又碰到一次花屏的情况，无法恢复。
17:56 联想v4000这个机器，总觉得win10下面显示有些灰蒙蒙的。
19:11 把popstr和pushstr加上保护，还是会挂掉。
20:38 和eddy讨论版权控制的问题。当前采用锁mac的方式，正式版本将采用后台服务器注册的方式。
白俊剑：升级搞了半天才好。还有锁机锁卡安装吉林的要求使用iccid进行计算出pin来。

2016-4-28
9:49 早上的速度貌似不怎么样啊，后面就还好了，三分钟平均92.1.
9:53 刷一个不带那个赋值1的试试。这个确实好像要差一些啊，居然挂了。重新测吧。
9:59 三分钟平均是86.8，那么再测一次吧。
10:07 三分钟平均89.5，再继续量一次。
10:11 这一次断过，平均值只有73.6了。
10:16 换回那个有赋值的内核。这个很快就上了90m。三分钟平均92.9
10:23 继续统计，存在掉落到一半的情况，这个是什么原因呢？换系统吧。
10:28 还是用联芯的系统来测试。内核是有赋值的那个内核，也存在曲线图挖坑的情况。
10:45 那么再刷一些联芯提供的内核试试吧。也会出现挖坑的情况。
11:06 那么用usb测试看看吧：也会出现有坑的情况，那就认为是网络的问题了？usb还是出现的少，10分钟只出现了2次。
14:17 去掉dma，貌似速度不错哦。头4分钟完美无缺。后面有挖坑现象，10分钟平均93.2
14:54 加上dma的，其实也不错，多跑跑看看。第一分钟完美。第二分钟开始挖坑了。
16:41 重新开始测试，好像还不错。三分钟平均93.2,还没有开始挖坑。4分钟开始挖了一个坑。4：28第二个。4:46第三个，5:05-5:16， 5:45-5:55，6分钟在70m了。直到10分钟。
16:56 换去掉dma的吧，速度非常差啊，只有6-70，和2点的完全不同啊。三分钟平均65.
17:04 换加上dma的再测，还是能到90的，又退回到70多了，三分钟平均71.4
17:12 换那个能到90m的吧，这个上来就是90多，18秒退回70多。三分钟平均73.7
换机器试试吧：


2016-4-27
9:07 当前测试是50m的样子，应该是昨天编译的程序吧。换一个早上最新的看看。
9:10 令人振奋啦，有70m了。三分钟平均是72.1
2016/04/26  21:25         4,023,080 kernel.nochangeotg
2016/04/26  22:29         4,023,160 kernel.nopanic
2016/04/26  22:42         4,022,608 kernel.nosb
2016/04/26  22:57         4,022,216 kernel.nogpioh
2016/04/26  23:13         4,022,128 kernel.nobattery
2016/04/26  23:28         4,021,648 kernel.nocodec
2016/04/26  23:44         4,021,792 kernel.nou2d           一分半平均53.9
2016/04/26  23:56         4,021,816 kernel.nohcd
2016/04/27  06:16         4,021,592 kernelnomodem   一分半平均53.3
2016/04/27  07:15         4,021,608 kernel.noasix          一分半平均53.3
2016/04/27  07:33         4,021,608 kernel.nocore          一分半平均69.7
2016/04/27  07:49         4,021,608 kernel.tzlcd   一分半平均70.2
2016/04/27  08:14         4,021,608 kernel.nopca953x
2016/04/27  08:29         4,021,608 kernel.noboardcomm     72.1
10:41 重新编译一个kernel.dma打开的 4分钟平均73.6

14:17 使用新的内核编译出来的，也只有70m左右。三分钟平均72.8
14:26 这就奇怪了。换个能到90m的看看。90m的就是有90m啊。三分钟平均88.2
15:01 重新编译了一次，还是只有70多。三分钟平均72.1
15:46 不管了，先刷文件系统吧。刷入ramdisk，kernel,和system，速度可达70多，感觉系统其它的影响都是比较小的。3分半的平均速率是75m。
16:00 刷回90m的还是有90m。回到linux系统中看看默认的dma是不是开的吧。
18:32 tz.tar.gz这个内核编译出来的版本，上来就有98m，不过现在降了下来。不过总能突破70m的限制。来搞个平均吧。4分钟的平均是90m，现在降到了35m，又回到了90多。
19:44 仅仅修改dma那个文件中的那个变量没用，还是73.9m
20:20 去掉那个hisc支持，速度上来了，三分钟平均94.4.
20:33 刷入ramdisk, system，貌似是一样的，三分钟平均92.2,主要问题是下载一开始比较慢，后面才能稳定到90。
20:42 使用无线就差多了，只有20-30m

2016-4-26
10:39 那个-CONFIG_COMIP_FLOWCAL=y 去掉没有问题。也许是联芯的新内核就不支持吧。
10:42 那么用联芯原始的.config加上otg和网卡来试试吧。CONFIG_USB_NET_AX8817X=y
      还是先去掉我们加上的东西。i2c器件。编译的文件是cpe5mod_1461639987.zip
11:14 这个内核没啥区别。还是只有50多。
11:25 内核里面的修改还是比较多的。还是使用加入的方法，先编出联芯的内核吧。
16:57 使用了联芯本身的内核，加上lan的驱动，速度只有70m，平均75m。
18:05 现在使用我们的内核测试，只有40多m
18:15 怎么换刚才联芯的那个，也只有40-50m了。三分钟均速38.2
18:19 来换我们的吧：47.5
18:36 测完三分钟再用前面测试到90m的来试试：当前三分钟测试的值是72m。但它有90m的时候，比如现在。
18:53 再换成我们的吧：53.5m
18:57 再换联芯的：测试1分钟，看来有70m，
19:12 果断换回我们的再测试。只有52.9额。
19:47 把联芯里面的config复制过来，测速也只有50m。三分钟平均52.7
19:53 再把能到70m的看看，还是70m的。三分钟平均：72.9
20:54 去掉bordcpe.c中的修改，保持和sdk中一样，貌似也不高。三分钟平均53m
21:32 去掉otg那个lcokwake的修改，还是一样50多。

2016-6-25
10:54 kill掉tzphone速率未见明显提升。30多。
10:57 刷一个联芯的kernel试试。刷了uboot内核.syetem，速度到了5、60m，坚持了一会儿后，现在又70多了。
11:15 再刷moden后，现在有8、90多了。过了一会，又变成6-70了。
11:21 再刷ramdisk, ramdisk_amt1, cache, userdata,重新设置仅4g，连上速度80-90，后变为70-80，换个网线，差不多。
14:04 再次测试，基本为70-80
14:12 使用留在联芯的板子，上来有95m以上，过一段时间有80多m，但一般都有85m以上。
14:16 现在就只有60多了。
14:32 重新开机测试，约3分钟后退回到70-80
      再次重新开机，使用联芯的电脑测试，2分钟后退回70-80
15:30 联芯使用另外一个程序，在留在那里的板子上跑了一次10分钟稳定在90多，有两次掉0的情况。

15:41 使用带来的两个板子中的另外一块，大约是80-90
15:44 现在是70-80.

16:12 使用上面这个板，刷新给的程序，速度可达90多。现在是85-89.
16:16 现在好像平均有90了。

16:21 把第一块板子也刷新给我的uboot和内核看看。
16:26 忘记了插卡。
16:32 前3分钟的平均速度死85，继续跑三分钟试试：这三分钟平均到90

16:40 这样，这个板子换我们的uboot来试试，上来就有90m嘛，看来和uboot没有什么关系。
16:58 那么，再把我们的kernel放进去吧，上来就只有50多了。跑3分钟试试。
17:03 最高也只有67.5，平均56.刷回去看看。
17:07 刷回联芯提供的kernel,上来是90,1分钟平均84
17:12 再刷我们的内核，看起来只有50多啊。

2016-4-24
11:23 吴曦：电脑锁在了屏蔽房。

14:45 加快的程序键盘和wifi都不正确。

15:40 王伍 使用新的无线驱动非常慢。

2016-4-23

12:25 陈良 金晶的udp server还是有问题。导致富桥的吸顶ap大量掉线。

2016-4-22

8:47 苗立双 大部分国家都是从1开始的信道。

8:53 onenote无论是注册还是用原来的用户登陆，都回到那个需要登陆的界面，难道是没有安装office？删掉吧。

8:56 王伍 要和刘子军联系去上海。

9:03 minicom可以使用这样的方式指定波特率：minicom -D /dev/ttyS0 -b 57600 -8 -c on

9:06 苗立双还差代码规范文档没有给我。

9:09 赵金发出邮件，想要实际设备模拟掉线问题。打电话来，正在躲雨。

9:43 CMD>reg w 1011008c 3ff7f7f
Address = 0xb011008c, Value = 0x 3ff7f7f
设置这个值后，w13的ipv6 邻居发现包就能过了。

郑杏泉：把tzphone加入服务中，启动时间能提升20多秒。而这个方法原来白俊剑试过是不能启动的。

10:10 看起来修改 1011008c 这个寄存器中的cpu_selection就可以了。

赵金：苏州的dtu只有两台在线了。

10:23 当前默认值是if_ra305x.c中第1164行写死的，没有任何注释说明这样设置的意义。

11:01 陈良：有个设备不能农宽的设备不能登陆，发现telnet登陆界面不同，应该不是我们的设备。

13:48 mtk发来标准包，测试也是一样的现象。

13:56 吴曦：wifi找到一些眉目，还要看下午的进展情况。

14:00 李金龙、王伍、夏荣平、颜斌开会。

赵金：dtu的服务器有问题，貌似被换掉了。

16:00 研发开会。

李柱栋那里黑龙江已经可以使用voip了。

吴曦发出wifi补丁。



2016-4-21

14:25  李柱栋来问为什么黑龙江设置了apn也没有用，既然在吉林的时候已经进行了设置，那么应该是移动给的数据有问题。

张勇：富桥还是需要一个telnet的命令界面来设置设备的参数，考虑做一个专门的程序来完成这个功能。

王伍：4g固定台还不能松劲，还要做以下功能：4g only下的短信功能、斯里兰卡的功能点、配置工具和配置参数的校验、要能看到配置参数的版本、web对上级网络不能开放、admin的密码可以配置、tr069列出功能、测试网络切换会不会有问题、大流量下时曾经出现的键盘反应慢、sip alg功能、dhcp只有少量地址的情况、省电模式、无线wps功能。

王伍：9x07的编译需要狗，还要去谈如何进行开发。

金晶：每个网页需要可以配置是否显示。

徐刚雄：派联的设备使用我的笔记本搜索不到。

陈玉：印度人发来测试情况，速度只有几百k，看图片上发送成功率非常低。

李柱栋：当前629把音频控制权全部拿去了。怕我们的程序和他强pcm设备。

15:18 当前的配置文件写法，如果文件小于结构体，那么就认为文件不对，会导致增加变量后重写配置。

15:48 李柱栋说tcpdump会出现抓包但保存的字节数为0的情况，在斯里兰卡也曾经出现，但我忘记是什么原因和如何又正常了的。

16:07 张勇、梁剑：印度的小ap还没有开始，张勇在列功能，梁剑在看以前留下的资料。

16:41 陈良，深圳这里的移动网络之间是不通的，所以感觉测试有些困难。其实可以让梁剑的程序连到本地李瑶进行测试。

白俊剑：李柱栋那里不能存tcpdump可能是关闭了log的原因，应该和设置联芯的log参数没有什么关系。

17:11 刘云：我们的程序flash放到水星的机器上跑，也存在问题，那么这样看来，硬件应该是没有问题的。

17:14 李柱栋：换了好几台机器，都没法抓包。

17:29 李柱栋：打开了界面的log，log下也没有对应的文件。

陈玉：斯里兰卡用户下周一会开始自测，需要英文版的web

17:36 mtk回邮件，说水星的产品使用的是tp自己做的vxWorks系统。

17:41 金晶，去看的是视频会议的公司。

18:01 张勇：苗立双简单的认为1信道一直都有也是不正确的。自动信道程序也没有考虑5.8的情况。

18:11 张勇：路由模式下可以数据0vlan,但是桥接模式下无法支持数据0, 管理有的情况。

李柱栋：感觉包多就能抓到，也许是操作系统有缓存。

18:26 王伍发邮件要求629加入需要生产的mac。张勇问cpe的vlan。

19:50 王伍要求去掉lcd的延时，他觉得快了，我觉得差不多。

23:00 晚上乱改了一通寄存器之后，发现可以ping通了，但是后来和刘云一起再不断重试，一直没有能够复现。
9344选择的flash是S25FL064A@SOIC16
9331的flash选择的是mx25l6406@sop8
Sequans当前用MX25U12835F@USON8

2015-12-19
1、按照http://blog.csdn.net/rudyn/article/details/38638759的做法就可以咋ubuntu 14.04上安装tftp server了，注意目录名称不要错误。

2051-12-17
1、./configure –enable-win64 这样wine在64位系统下编译。

2015-12-15
1、如果主目录的权限修改为777，那么ssh的自动登陆就失效了。

2015-12-1
cpe中这个脚本可以连接另外一个ssid。
wlanconfig ath1 create wlandev wifi0 wlanmode sta
iwconfig ath1 essid tozed-jian2
activateVAP ath1
iwpriv ath1 extap 1
ifconfig ath1 192.168.200.1

2015-11-26
这个脚本可以实现微商的vlan。
enable_dhcpd()
{
        killall udhcpd
        echo start 192.168.200.109 > /tmp/udhcpd.conf
        echo end 192.168.200.150 >> /tmp/udhcpd.conf
        echo option subnet 255.255.255.0 >> /tmp/udhcpd.conf
        echo opt router 192.168.200.1 >> /tmp/udhcpd.conf
        echo opt dns 192.168.200.1 >> /tmp/udhcpd.conf
        echo interface br200  >> /tmp/udhcpd.conf
        echo option lease 32760 >> /tmp/udhcpd.conf
        udhcpd  /tmp/udhcpd.conf
}


cleanmyway()
{
        killall macwriter
        killall wlfix
        killall ntpsupplicant
        killall flowstat
        killall checkusbnet
        killall dnsmasq
        killall udhcpc
        killall monitortool
        echo V > /proc/tozed/watchdog
        iptables -F
}


clear_vlan()
{
        echo 0 0 0 0 1 1 > /proc/tzvlan/portvid
        echo 1 0 0 0 1 1 > /proc/tzvlan/portvid
        echo 2 0 0 0 1 1 > /proc/tzvlan/portvid
        echo 3 0 0 0 1 1 > /proc/tzvlan/portvid
        echo 4 0 0 0 1 1 > /proc/tzvlan/portvid
        echo 5 0 0 0 1 1 > /proc/tzvlan/portvid

        echo clear > /proc/tzvlan/table
        ifconfig br0 0.0.0.0
        ifconfig eth1 192.168.0.1 up

}

if [ ! "$1" = "" ] ; then
        $1
        exit
fi

cleanmyway

clear_vlan
echo config vlan table....
echo 0 0 0 3 1 1 > /proc/tzvlan/portvid

#set port1
echo 1 1 2 3 100 100 > /proc/tzvlan/portvid
#set port2
echo 4 1 2 3 100 100 > /proc/tzvlan/portvid
echo 100 1 1 0 0 1 0 > /proc/tzvlan/table

#set port3
echo 3 1 2 3 200 200 > /proc/tzvlan/portvid
#set port4
echo 2 1 2 3 200 200 > /proc/tzvlan/portvid
echo 200 1 0 1 1 0 0 > /proc/tzvlan/table

brctl delif br0 eth0
brctl delif br0 eth1
brctl delif br0 ath0

vconfig add eth1 200
vconfig add eth0 200
ifconfig eth0.200 up
ifconfig eth1.200 up
wlanconfig ath1 create wlandev wifi0 wlanmode ap
iwconfig ath1 essid gogo2
activateVAP ath1
brctl addbr br200
brctl addif br200 eth1.200
brctl addif br200 ath1
ifconfig br200 192.168.200.1 up

vconfig add eth0 100
vconfig add eth1 100
brctl addbr br100
brctl addif br100 eth0.100
brctl addif br100 eth1.100
ifconfig eth0.100 up
ifconfig eth1.100 up
brctl addif br100 ath0
ifconfig br100 up

enable_dhcpd

pppoe-start eth0.200 test
iptables -F
iptables -F -t nat
iptables -A POSTROUTING -t nat -s 192.168.200.0/24 -o ppp0 -j MASQUERADE


2015-9-9
1、张勇貌似把组播服务器建立起来了。但是看起来tcp点播数据和组播数据都存在，难道是服务器设置的问题？
2、如下脚本放在apup中，貌似可以建立多个ssid，有自己的加密选项了
+
+if [ "${AP_SSID_3}" != "" ] ; then
+        wlanconfig ath2 create wlandev wifi0 wlanmode ap
+        iwconfig ath2 essid ${AP_SSID_3}
+        activateVAP ath2 br0 $AP_SECMODE_3 $AP_SECFILE_3
+fi
+
+if [ "${AP_SSID_4}" != "" ] ; then
+        wlanconfig ath3 create wlandev wifi0 wlanmode ap
+        iwconfig ath3 essid ${AP_SSID_4}
+        activateVAP ath3 br0 $AP_SECMODE_4 $AP_SECFILE_4
+fi
+

2015-9-8
1、昨天测试的可能有问题，cpe ping天线也有丢包的情况发生。
2、基本上1分钟断一次的问题是李柱栋编译时打开了新疆的宏，命令ap每分钟上报周边的干扰。
3、张勇使用2008自带的流媒体服务器，从抓包来看，对两台机器使用的两个不同的类型的包，一个是tcp 一个是udp，也是比较奇怪。

2015-9-7
1、查看多个无线加密的方法，貌似是多个文件。
2、使用cpe测试的效果比p10p好很多。

2015-8-26
1、貌似加密方式是可以用的。

2015-8-20
1、多ssid和vlan的设置看起来还有些复杂，主要是变量的设置规则。还有vlan的设置。还有多种情况，如果存在5.8g，那么组合的情况就非常非常多。典型应用有，2.4g有多个ssid，有的ssid加密，有的不加密，使用同样的数据vlan。2.4g有多个ssid，走不同的vlan。还要乘以有管理vlan，没有管理vlan的两种情况。

2015-8-19
1、在设置了mcastenchance之后，pc端收到的包就变成了组播udp包，而在设置之前，pc端收到单播包，所以代码里面的转换还真不少。

2015-8-18
1、从下面这个脚本来看，貌似只有计数寄存器有了变化。
regs="000 004 008 00c 010 014 018 01c 020 038 03c 040 044 048 04c 050\
      05c 060 080 084 088 08c 090 094 098 0d4 0p8 0e0 0e4 0e8 0ec 0f0\
      0f4 0f8 0fc 100 108 10c 114 118 11c 120 124 128 12c 130 134 138\
      13c 144 168 16c 180 1c0 1d0 1ec 1f0 1f4 1f8 1fc 200 240 244 248\
      24c 250 254 258 25c 260 270 274 278 27c 294 298 318 328 330 334\
      338 33c 35c 360 364 368 370 374 378 37c 380 384 3a4 3a8 3c8 3cc\
      800"

rm /tmp/myreg.txt -rf
for i in ${regs}
do
        echo 18108$i > /proc/tozed/commreg
        value=$(cat /proc/tozed/commreg)
        echo 18108$i $value >> /tmp/myreg.txt
done
cat /tmp/myreg.txt

2015-8-13
1、海外测试的情况，直播使用的是组播的方式，必须使用ipwriv ath0 mcastenhance 1或者2来使能组播的发送。
2、在ap上执行iwpriv ath0 medropmcast 0那么，空间抓包是udp的组播包，否则就变成了单播包。
3、问题在于，有两个cpe时，组播包貌似很快就停止了，从空间抓包来看，那么udp的包还在，但是cpe那里就收不到了，必须重新加入一次，才能继续收到，但是很快就没有了。
4、这个git备份的代码好一些
declare -a git_list=(ar_u11 L1712FP_2832_RLS L1761-DC-QUAD quacomm4004 \
ZLT2829 ar_v10.1 cpetool L1761-DC-411 MTK6261D sequans3120  ZLT_M10A_R08 bigap1 \
CSipSimpleProject L1761-DC MTK6261 sequans3220 ZLT_M10_CTA gitosis-admin \
L1761-DC-lib mv6710 snmp ZLT_M10 buildroot jian-doc L1761-DC-QUAD-BAND3_8 \
purchase  sqn_kernel_cut ZLT_M10_LC quacomm4004 bigap_web Icarm-Bus \
WiFiManager_cn WiFiManager_en weixin_api DeviceManagers dtu_server dtu \
g8201e-linux)

TOPDIR=$(pwd)
rm lastcommit.txt
for i in ${git_list[@]}
do
	echo "backup" $i
	cd ${TOPDIR}
	if [ -e $i.git ] ; then
		cd $i.git && git remote update
	else
		git clone --mirror git@192.168.1.249:$i.git && cd $i.git
	fi
	lastcommit=$(git log -1 --date=short | grep Date | cut -b 9-20)
	lastname=$( git log -1 | grep Author | cut -b 9-50)
	lastdetail=$(git log -1 | grep '    ')
	echo -e $lastcommit "\t" $i "\t\t\t" $lastname  >> ../lastcommit.txt
	echo -e $lastcommit "\t" $lastname  $lastdetail
	echo ""
done
原来的那个gitk不能看到最新的日志。


2015-8-10
1、安徽那里出现严重的问题，记录的用户名中出现^^，在我们的设备中和汉达中貌似都有，而华为的l2tp和base服务器也有，而在radio中没有。使用win10和mercury的路由器拨号都没有发现有错误的现象。
2、使用dlink dr615发现有前面多两个字符的情况。貌似和拨号用户名相关。找资料貌似没有找到相关的信息。

2015-8-6
1、编一个cpe-5g version 112的版本。
2、李柱栋的程序在发送cpe无线速率时，没有判断cpe-am的型号，导致cpe-am总是无线总是自动速率。
3、董超那里会出现从cpe访问220结果到了其他基站的情况。没有设置管理vlan。
4、本地git备份使用bare时，从远程fetch，本地的git log居然看到到还是很早的数据。而非bare的文件夹,pull下来貌似是正常的。

2015-8-5
1、终于重新把lan-l2tp运行起来了。

2015-8-4
1、改w11的烧片文件。
2、增加BUILD_LIBRARYOPT=y这个选项貌似对文件大小没有任何影响。难道说每个库中的每个函数都被调用了？而libraryopt-1.0.1这个工具貌似也没有更新。
3、写ap的规格书

2015-8-3
1、继续删除w11中的程序，压缩文件系统空间。

2015-7-31
1、9341使用4m flash 内核修改

2015-7-30
1、9341使用4m flash uboot修改

2015-7-29
1、这个脚本来备份所有的git仓
declare -a git_list=(ar_u11 busybox L1712FP_2832_RLS L1761-DC-QUAD quacomm4004 \
ZLT2829 ar_v10.1 cpetool L1761-DC-411 MTK6261D sequans3120  ZLT_M10A_R08 bigap1 \
CSipSimpleProject L1761-DC MTK6261 sequans3220 ZLT_M10_CTA gitosis-admin \
L1761-DC-lib mv6710 snmp ZLT_M10 buildroot jian-doc L1761-DC-QUAD-BAND3_8 \
purchase  sqn_kernel_cut ZLT_M10_LC quacomm4004 bigap_web Icarm-Bus \
WiFiManager_cn WiFiManager_en weixin_api DeviceManagers dtu_server dtu)

TOPDIR=$(pwd)
rm lastcommit.txt
for i in ${git_list[@]}
do
	cd ${TOPDIR}
	if [ -e $i.git ] ; then
		cd $i.git && git fetch
	else
		git clone git@192.168.1.249:$i.git --bare
	fi
	lastcommit=$(git log -1 --date=short | grep Date | cut -b 9-20)
	lastname=$( git log -1 | grep Author | cut -b 9-50)
	echo -e $lastcommit "\t" $i "\t\t\t" $lastname  >> ../lastcommit.txt
done
2、在cpe下接一个路由器，并将路由器的两个口短接，从wbs上联的电脑ping一个地址，那么路由器的灯开始狂闪。这个时候，cpe不一定能够检测到有回环发生。

2015-7-28
1、测试回环检测。

2015-7-27
1、cpe-am vlan配置无需重启。
2、cpe-am wbs远程升级测试。

2015-7-22
1、海外版wbs配置可以删除的内容。
2、ap-c1 dhcpd验证。
3、分流方案讨论

2015-7-21
1、排查白银设备停运原因。
2、cpe-am不使用配置的vlan表。

2015-7-20
1、ap-c1内核使用配置文件控制串口输出。默认允许手机接入。

2015-6-25
1、更换77上的libtool看看bigap中的iptables是否能编译过去。还是一样的，报 cannot find -lnfnetlink

2015-6-24
1、用这个来统计提交次数： git log --since=2015/6/14 --before=2015/6/20 --author=jianliang | grep commit| wc -l

2015-6-18
这个是1和其他都通，其他之间不通
cfg -a TZ_VLAN_ENABLE=1
cfg -a TZ_VLAN_PORTVID1=11
cfg -a TZ_VLAN_PORTVID2=12
cfg -a TZ_VLAN_PORTVID3=13
cfg -a TZ_VLAN_PORTVID4=14
cfg -a TZ_VLAN_TABLE_ID1=11
cfg -a TZ_VLAN_TABLE_ID2=12
cfg -a TZ_VLAN_TABLE_ID3=13
cfg -a TZ_VLAN_TABLE_PORTMAP1=1111
cfg -a TZ_VLAN_TABLE_PORTMAP2=1100
cfg -a TZ_VLAN_TABLE_PORTMAP3=1010
cfg -a TZ_VLAN_TABLE_ID4=14
cfg -a TZ_VLAN_TABLE_PORTMAP4=1001


2015-6-17
这个脚本可以实现中间两个口通，其他情况不通。
echo clear > /proc/tzvlan/table
echo 10 1 0 1 0 0 0 > /proc/tzvlan/table
echo 11 1 0 0 1 1 0 > /proc/tzvlan/table
echo 12 1 1 0 0 0 0 > /proc/tzvlan/table
echo 1  1 1 1 1 1 1 > /proc/tzvlan/table

echo 0 1 2 3 1 1 > /proc/tzvlan/portvid
echo 1 1 2 3 12 12 > /proc/tzvlan/portvid
echo 2 1 2 3 10 10 > /proc/tzvlan/portvid
echo 3 1 2 3 11 11 > /proc/tzvlan/portvid
echo 4 1 2 3 11 11 > /proc/tzvlan/portvid
这个的配置貌似也可以了
export TZ_VLAN_ENABLE=1
export TZ_VLAN_PORTVID1=10
export TZ_VLAN_PORTVID2=11
export TZ_VLAN_PORTVID3=11
export TZ_VLAN_PORTVID4=12
export TZ_VLAN_TABLE_ID1=10
export TZ_VLAN_TABLE_PORTMAP1=1000
export TZ_VLAN_TABLE_ID2=11
export TZ_VLAN_TABLE_PORTMAP2=0110
export TZ_VLAN_TABLE_ID3=12
export TZ_VLAN_TABLE_PORTMAP3=0001

这个配置是1 3， 2 4 分别互通
export TZ_VLAN_ENABLE=1
export TZ_VLAN_PORTVID1=11
export TZ_VLAN_PORTVID2=12
export TZ_VLAN_PORTVID3=11
export TZ_VLAN_PORTVID4=12
export TZ_VLAN_TABLE_ID1=11
export TZ_VLAN_TABLE_PORTMAP1=1010
export TZ_VLAN_TABLE_ID2=12
export TZ_VLAN_TABLE_PORTMAP2=0101

2015-6-16
1、还是一天的vlan

2015-6-15
1、做了一天的vlan

2015-6-12
1、李忠那个p10p已经跑了5天，拉的次数高达27次。

2015-6-11
1、查看uboot代码，看看如何修改才能不进行串口输出。

2015-6-10
1、那个comproxy可以直接运行。
2、ap-c1基本算是移植部分完成，

2015-6-9
1、测试了一天的速度，貌似也没有什么发现。

2015-6-8
1、无论是ap还是p10，换用旧版本的wlan驱动都是一样的，都存在信号值延时的现象。

2015-6-6
1、iwconfig 这个东东是从/proc/net/wireless这个文件读到信号值的，而这个文件是由内核中这个    net/wireless/wlan_getrssi(vap, &rssi_info, WLAN_RSSI_RX);函数来输出的。它调用的是设备的get_wireless_stats函数来输出。
2、在atheros系统中，这个函数是os/linux/src/ieee80211_wireless.c中的ieee80211_iw_getstats函数。它继续调用wlan_getrssi(vap, &rssi_info, WLAN_RSSI_RX); 继续调用wlan_node_getrssi， 然后是调用ic_node_getrssi这个函数指针。
3、ic_node_getrssi这个有两个地方赋值，那么来看看是那个函数吧。
4、看来是ath_net80211_node_getrssi这个函数。


2015-6-5
1、开始继续ap-c1这个东西吧。
2、李忠测试的机器还是挂了，把阈值改高一点吧。75%。

2015-6-4
1、李忠测试的机器又出现无法下载的情况，看发送成功率呢，有时候很差，有时候又恢复过55%，所以保护机制不起作用。发一个新的程序减少保护时间看看。
2、总算找到开机lan灯有一个会灭掉的原因，原来看门狗把它当作输入脚了。

2015-6-3
1、南少鹏做的9331模块10分钟重启应该是没有喂狗的原因。
2、查找atheros重启机制。

2015-6-2
1、李忠测试的机器已经运行了4天多，看起来还能正常连接，共有3次复位动作。
2、9341在某种情况下初始化内部的switch会有问题。
3、9331改成单ap程序要改的东西还是有一些的。

2015-5-29
1、http://www.doc88.com/p-51666700313.html这个文档是那个指令集。
2、李忠测试的机器貌似还是开机不久的那一次复位动作。

2015-5-28
1、给李忠的机器增加一个发送成功率降低就复位一下无线的程序。
2、查看程控电源资料。

2015-5-27
1、李忠那里测试还是会挂掉，看起来实在没有什么好办法了。加容错吧。
2、出省校准的新程序。

2015-5-26
1、为什么这个9341的板子无法从串口刷程序，uboot的情况下无法ping通，也就无法下程序。向外ping显示是对方alive的。抓包来看是收到了板子发来的tftp请求包。计算机重启看起来也没啥用。重启交换机，也没啥用。直接连接，不行。换了个tftpd程序好了，难道是我的机器中招了？
2、刷好以后报这样的错误：
JFFS2 error: (1096) jffs2_do_read_inode: requestied to read an nonexistent ino 21 iget() failed for ino #21

2015-5-25
1、ipv4的以太网包类型是0x800，而ipv6是0x86dd。
2、当使用telnet登陆到p10的ipv6地址时，traffic class 和flowlabel都是0，少了option这个域。每个包的还变小了。
3、使用telnet xxx 80 这样的方式可以连接到p10上，一个回车之后，返回了错误网页，但是，使用浏览器，写上ipv6的地址就不能访问。
4、9341只有一个uart，可以通过uboot不指定console的方式不把kernel的debug输出到串口。

2015-5-23
1、为什么p10那个校准检查的程序上传发出去的不行，而重新编译一下是好的？难道上次编译有问题？

2015-5-22
1、linux ipv6的ping6 xxx 必须增加-I指定接口，同样的，xp下好像是ping或者ping6都可以，但是要加上%x这个网络接口序列号，否则都是无法ping通的。
2、普通的tp link下面的ipv6之间是可以互通的。
3、ipv6看来放弃了端口号这个东东。

2015-5-20
1、华为cpe设备，客户端使用我的hp和另外一台tinkpad，如果使用12信道，那么效果变得很差，还能ping通，ftp几乎停止。同样的位置，使用p10，那么效果貌似差不多，ftp奇慢，还能ping通。
2、那么换到11信道两个对比看看。P10根本连不上啊。重启试试。现在hp笔记本连上了，但是thinpad就是连不上。貌似没有抓到auth的回包。

2015-5-19
1、查看生产拿来的板子：一个校准区丢失，表现是lan的mac变成了00:02:03:04:05:06、4个反复重启、还有一个不知道是什么错误。

2015-5-18
1、上周五进行的测试貌似到了第二天的凌晨就没有数据跑了，而且系统都完全挂掉，串口没有数据。

2015-5-15
1、出p10省校准程序第二个测试版。
2、p10使用新的无线驱动，终于貌似运行了，但是usb好像不能用了。

2015-5-14
1、继续移植sdk v10

2015-5-13
1、继续移植sdk v10
2、如果记录probe request的包的mac，那么记录增加的非常快。500个也满了，来看看1000个能不能满。也满了，真的能有这么多么？搞它一万个试试？一个晚上也没有满了，第二天早上4000多个。

2015-5-12
1、总是把cpe-df使用新的wlan驱动编好了，但是报错啊，报错啊。

2015-5-11
1、把atheros的sdk v10的scripts/db12x，放到当前的bigap仓中编译，那么9344上apup可以起来，而9341上就没法起来。
2、去掉那个special后，9341上也能起来了。

2015-5-9
1、完成了一个p10的校准工具最简版。

2015-5-8
1、制作p10的校准工具。

2015-5-7
1、这个是sequans当前的mtd表：
mtd0: 02000000 00010000 "spi0.0"
mtd1: 000c0000 00010000 "Bootrom"
mtd2: 00040000 00010000 "Usim"
mtd3: 00040000 00010000 "Kvs"
mtd4: 00ec0000 00010000 "kernel"
mtd5: 01000000 00010000 "region_fs"
mtd6: 00800000 00010000 "rootfs"
mtd7: 002d0000 00010000 "rootfs_data"
mtd8: 00800000 00010000 "rootfs_next"
可以看到kernel这个区居然占了一半，简直是浪费。还不能只留给kernel 5m，那样升级会过不去。留到9m的样子。貌似是可以的。

2015-5-6
1、要找个多线程支持命令行的工具来做测试。aria2c.exe这个可以，只差一点，不能把文件写入NUL
2、再来测试吧：v10.1 nob=0
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
46	40	40	43	41	40	41	41	40	44
nob=1
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
47	41	42	44	48	43	44	50	44	49
3、使用cpe-df的程序
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
39	42	38	34	31	32	34	43	37	43
使用cpe-df程序，未修改发送重试次数
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
45	42	34	34	38	34	41	34	33	32

3、现在sequans的sysupgrade又变成了：nable to perform sysupgrade during system reboot.应该是李柱栋加入的流量统计导致rcs没有退出。去掉了也不对啊。

2015-5-5
1、sdk 19413和以前的比起来相差不是太大，所以很快编译过去了，烧片也貌似正常。
2、安徽的账号应该又过期了。
3、再来进行测试吧：
v10.1 15:27
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
32.52 18.52	25.96 17.62	31.98 19.49	37.60 20.94	27.74 19.52	29.98 18.05	33.43 18.47	28.41 16.50	25.38 20.75
稍微修改了一下重试次数的代码 15:58 好了很多?
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
41.76 29.80	41.74 25.49	44.21 30.41	42.96 27.59	39.85 26.01	41.22 28.20	41.11 27.12	41.95 26.33	43.55 25.45	42.12 26.13
改回去试试：16:13，为什么变得这么差？
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
40.07 25.21	27.45 4.02	26.25 4.22	20.32 3.05	26.63 3.13	21.27 3.73	19.28 2.85	22.64 2.93	24.70 3.55	19.35 3.22
再试试稍微修改了一下重试次数的代码：16:29
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
41.67 26.04	41.88 26.68	42.08 27.36	37.52 25.74	42.15 24.56	43.00 27.76	44.00 26.62	42.77 25.64	43.68 25.71	42.79 30.22
再试试改回去的 还是要差那么一点的。
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
37.96 23.72	39.67 	40.26 25.47	36.81 28.15	42.19 22.42	37.26 23.01	39.29 25.71	37.58 24.07	41.91 24.81	39.86 24.64

4、用cpe-df的程序来测试
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
26.71 16.62	25.49 16.32	22.63 14.36	26.95 20.83	24.17 20.18	24.22 18.47	23.77 18.12	29.37 11.44	24.55 14.58	23.84 17.25
也和v10.1中做同样的修改看看 貌似好些。
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
22.63 6.86	25.67 19.52	30.05 16.93	30.62 21.13	28.28 17.01	29.32 23.36	25.91 18.42	30.43 18.70	25.94 19.53	35.10 20.77
同上，加nob=1 18:12
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
32.48 20.09	31.82 23.07	30.85 18.20	30.55 19.80	30.11 27.01	40.46 25.11	40.67 25.50	41.06 25.59	40.83 25.26	40.82 19.05

5、再用v10.1的增加了发送速率修正的来测试吧20:12
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
28.72 25.41	38.64 26.36	33.04 26.28	27.21 26.12	35.43 25.67	36.73 26.59	35.95 25.51	38.93 24.37	39.67 25.30	39.20 25.42
同上，增加nob=1 20:25
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
23.99 19.73	23.37 14.12	17.58 18.85	13.41 16.15	19.03 10.01	23.57 12.90	14.11 6.66	20.68 18.01	18.16 18.67	18.17 18.94
恢复nob=0 20:38
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
18.34 19.36	24.46 19.02	21.00 18.62	21.92 18.12	19.66 18.20	17.47 18.74	19.84 18.48	17.57 19.54	18.73 19.32	20.24 19.01
好像都不怎么样。

6、用ftp来测试看看v10.1 nob=0
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
59秒	63	58	59	61	69	74	65	56	63
nob=1
第一次	第二次	第三次	第四次	第五次	第六次	第七次	第八次	第九次	第十次
60	69	83	65	59	63	69	56	55	55



2015-5-4
1、先来测试一下sdk10.1的无线部分的测速数据。
第一次	第二次	第三次	第四次	第五次
19.54 17.71	24.39 29.18	21.55 17.05	20.79 18.97	22.67 17.60
2、为什么升级了程序以后windows需要重新输入密码？奇怪的事情。重新刷就要重新输入密码？貌似是这样。
3、貌似增加了发送速率一定为n的代码后测速
第一次	第二次	第三次	第四次	第五次
24.75 17.66	25.34 18.81	24.30 16.13	23.42 14.35	20.60 14.07
4、发送速率有+i，感觉比固定x80要好一点。
第一次	第二次	第三次	第四次	第五次
19.78 20.49	24.69 18.41	25.69 21.84	24.94 19.41	32.70 20.49
5、18:17测试
第一次	第二次	第三次	第四次	第五次
46.23 37.05	44.54 37.38	44.73 37.16	46.10 36.88	45.27 36.08
6、去掉那个发送速率的修正，基本上是原始的sdk了。
第一次	第二次	第三次	第四次	第五次
41.61 35.96	46.10 36.93	41.60 35.92	44.24 34.58	44.68 35.24
7、去掉那个发送速率的修正，加上nob=1。看起来这时候nob没有起到多大作用。
第一次	第二次	第三次	第四次	第五次
45.24 32.97	44.54 32.72	44.43 32.18	45.52 34.64	40.08 32.85
8、那么用p10的程序来测试一下吧。居然比v10.1的相差这么多？18:58。
第一次	第二次	第三次	第四次	第五次
38.19 28.82	35.05 23.65	15.60 28.21	39.73 33.23	24.10 30.59
9、用cpe-df的程序来试试吧
第一次	第二次	第三次	第四次	第五次
35.73 27.90	38.16 28.56	28.56 25.45	30.10 25.49	29.38 24.32
10、再去掉那个发送速率的修正，基本上是原始的sdk v10了。
第一次	第二次	第三次	第四次	第五次
40.08 34.36	34.17 34.50	34.89 32.59	33.91 32.57	40.05 37.73
11、去掉那个发送速率的修正，加上nob=1。
第一次	第二次	第三次	第四次	第五次
35.59 30.64	28.87 27.75	25.93 31.40	26.17 28.33	28.83 28.44
12、nob=0
第一次	第二次	第三次	第四次	第五次
33.66 32.68	36.24 31.10	35.37 30.80	21.65 29.33	35.19 30.96
13、发送速率有+i，
第一次	第二次	第三次	第四次	第五次
31.44 32.77	37.68 34.16


2015-4-30
1、分别测试cpe上使用新的sdk10的无线驱动进行测试。貌似还不如前面的版本。

2015-4-29
1、使用我桌面的p10来进行速度测试，笔记本使用网线连，speedtest 2次都是24m左右，而wifi则都是15-16m，最快的一次是17.50m。
2、使用公司网络来测试吧，貌似通过tplink的路由器对速度都会有影响： 第一次40.20,33.59
第二次：41.55 42.31 第三次：42.04 44.36
3、笔记本直接上公司网络测试：第一次：43.94 45.00 第二次：40.95 44.73 第三次：41.58 44.57貌似差别可以忽略。
4、使用陈良的那张安徽的卡就太差了，还需要拨号，只能测试到1m以下。而且他的设备还是做了锁sim卡的操作。
5、陈良的那台设备，天线平放，第一次：23.16, 3.34
以下使用使用公司网络，陈良的设备，
6、txopwer 12,第一次：31.91  19.72，第二次：33.65 18.93 第三次：34.86 23.71
7、txopwer 13，第一次：25.82 19.50 第二次：28.60 17.04 第三次：25.50 17.21
8、txopwer 11：第一次：27.79 19.65 第二次：29.89 19.53 第三次：23.68 19.84
9、txopwer 12：第一次：32.99 18.52 第二次：26.79 17.83 第三次：22.23 18.71
10、txopwer 12，rts 256；第一次：26.91 22.85 第二次：19.38 20.39 第三次：18.95 24.47
11、txopwer 12，rts off：第一次：23.59 23.19 第二次：27.97 21.05 第三次：33.25 20.11
12、txopwer 12，rts off ：第一次：36.71 23.26 第二次：33.67 24.12 第三次：30.22 22.24
13、txopwer 12，rts off  beacon_nob 0：16.56 20.73 第二次：21.10 17.37 第三次：19.53 15.66
14、txopwer 18：第一次：27.62 20.99 第二次：32.34 19.74 第三次：26.08 17.62
15、txopwer 14，0x8f8e8d8c：第一次：37.21 22.34 第二次：31.52 26.97 第三次：37.73 24.60
16、txopwer 12，0x8f8e8d8c：第一次：38.24 25.43 第二次：32.85 14.54 第三次：39.40 255.51
17、txopwer 12，0x8c8d8e8f：第一次：20.34 19.24 第二次：29.40 20.80 第三次：23.89 20.96
18、txopwer 12，0x8f8e8d8c：第一次：34.51 22.95 第二次：32.61 26.02 第三次：37.96 25.33
19、txopwer 12，0x8e8d8c8b：第一次：28.25 23.43 第二次：27.41 26.02 第三次：28.21 24.34
20、txopwer 12，0x8f8f8d8c：第一次：39.13 23.21 第二次：31.21 24.55 第三次：30.87 23.94
21、txopwer 12，rts 256,0x8f8e8d8c：第一次：35.92 27.61第二次：38.02 26.24 第三次：36.73 24.90
22、txopwer 12，rts 2346,0x8f8e8d8c：第一次：38.66 26.09第二次：37.54 26.50 第三次：36.87 26.43
23、txopwer 12，rts 2346,0x87878787：第一次：34.67 23.25 第二次：30.76 26.33 第三次：18.58 19.66
24、txopwer 12，rts 2346：第一次：32.92 14.01 第二次：20.94 16.89 第三次：26.08 23.52
25、txopwer 12 第一次：22.46 19.73 第二次：20.59 18.72 第三次：23.43 20.99
26、txopwer 12，0x8f8e8d8c：第一次：26.81 23.41 第二次：31.51 25.19 第三次：30.12 26.02
27、txopwer 12，rts 2346,0x8f8e8d8c：第一次：33,85 23.89 第二次：32.46 12.67 第三次：16.04 6.48 第四次：31.17 23.46
28、txopwer 18，rts 2346,0x8f8e8d8c：第一次：34.26 23.19 第二次：31.75 22.76 第三次：34.14 24.02
以下使用移动网络：
29、默认设置：第一次：6.32 3.04 第二次：6.91 3.33 第三次：6.72 3.50
30、0x8f8e8d8c：第一次：5.50 3.55 第二次：7.28 3.32 第三次：6.39 3.08
31、使用以太网：第一次：7.08 7.22 第二次：7.19 6.43 第三次：7.84 7.10奇怪的现象
32、再测，使用以太网：第一次：19.97 3.58 第二次：9.27 4.25
换个设备吧
33、使用以太网：第一次：20.07 0.52 第二次：17.80 2.90 第三次：18.71 2.79
34、使用无线网：第一次：14.51 2.37 第二次：14.39 2.70 第三次：14.67 3.46
35、0x8f8e8d8c：第一次：15.19 3.46 第二次：14.62 2.29 第三次：12.87 3.24
换个模块试试吧：真不容易，还要改模式。
36、使用以太网：第一次：20.48 6.04 第二次：24.18 4.89 第三次：20.75 4.87
37、使用无线网：第一次：13.94 5.53 第二次：5.36 5.79 第三次：5.71 5.39
38、0x8f8e8d8c：连不上。
39、0x87878787：第一次：16.30 4.48 第二次：10.03 5.17 第三次：13.57 5.72
40、0x87878787: iphone6 图形无法显示
41、iphone6:第一次：20.21 3.33 第二次：23.81 3.17 第三次：17.06 1.24
42、使用单流的抓包网卡：第一次：18.31 2.75 第二次：18.24 3.38 第三次：19.01 3.66
43、联想笔记本：第一次：21.84 2.57 第二次：23.86 2.87 第三次：21.45 2.87
openwrt to do list
1、编译新的(2014-12-12)sequans的sdk
2、在p10上跑起openwrt
3、Sequan使用外部编译器。
4、sequans使用网络系统时进行恢复的方法。
5、Sequans使用李瑶的网页。
6、Sequans功能：防火墙
7、Sequans功能：ipv6
8、Sequans功能：l2tp
9、在centos 6.6 64位版上编译一个编译器，作为64位系统的编译器。
10、在77上升级gcc的版本。
11、编译新的sequans 3220 sdk
12、新的3220建仓
13、使用新的设备类型文件
14、增加自定义版本文件
15、ubuntu上对3220进行编译。
16、当openwrt/kernel目录下存在一个错误的xz文件时，wget重新下载的文件会变成xz.1要强制下载的文件名。
17、找一台不能上网的机器编译一遍3220。
18、3220的sdk改为外部编译器。
19、去掉不需要的tools的编译。
20、测试同样的机器使用不同的-j参数时的编译速度。
21、从仓中删除没有使用到文件。
22、改写仓，使得内核不用每次下载。
23、Atheros平台连接wep时，对于数字密码和ascii密码，要使用不同的设置。
24、生成的文件加入版本号。
25、安徽的l2tp还要支持每个session单开tunnel功能。
26、Ap_server 使用特殊密码的方法，在pc端是否可以直接得到密码
27、改变clean的方式，使得普通的clean不会清除重新编译编译器
28、在openwrt中增加每个型号的base-files目录，方便增加不同型号自己的文件。
29、使用自己的login代替busybox使用的login，限制用户使用的指令。
30、启动sequans上对tzwww的web服务。
31、更换openwrt的banner
32、在ubunt和centos下自动判断各种包是否安装，如果没有安装就安装。
33、编译一个3110的试试。
34、修改root的密码，已经改为p18SQN
35、增加自己的配置文件。
36、p10中转发方式要记录一下用户名，以便于移动公司查找问题。
37、p10转发方式记录的pppoe用户名放到/proc/net/pppoe文件中。
38、给南少鹏的那个板子做一个系统。
39、路由系统中需要加一个内置网站黑白名单的功能，不能由网页修改。
40、在单ap上做一个黑名单功能。
41、跑一个简单的snmp试试。
42、Gpio的中断方式。
43、做一个烧录文件。
44、把新的sdk的bin和platform放到自己的git仓中试试。
45、如何升级时保留配置。
46、写一个在windows下如何进行修改bootrom的文档吧。
47、把tc修改一下，增加buff的大小，并且可以调整buff。
48、

2015-4-28
1、wlan休眠机制：wlan的每个包的Frame Control Flags中有一位是Power Management。这位为1时，表示发送此包的设备将进入休眠。在收到下一个表示已经唤醒的包之前，ap会缓存向这个设备发送的包。抓包发现以下现象：iphone的连接会使用rts/cts机制，有大量的rts/cts包，而小米的没有。speedtest使用的http协议来做速度测试，它的测试过程中，小米发送的包就貌似没有看到有休眠的迹象，而移动的测试app使用的是ftp协议，小米机器有出休眠指示。即使是在插电的情况下，小米仍然会发出休眠指示。

2015-4-27
1、123这台服务器居然报什么嵌套字缓存已满，不能上网。重启试试吧。远程的重启居然没有成功，只好到服务器位置去重启。
2、桌面上的sequans板子貌似也挂掉了，串口无响应。拔电恢复了。下午2点又没有响应了。
3、thebat貌似突然没有了公司邮箱的邮件，一开始还以为是文件被破坏而挂掉，重新增加账号还是在的。估计是运行了一个原来的bat导致的。
4、安徽报有支付宝充值错误。
5、77来编译一个带有net-snmp的程序吧。貌似找不到这个net-snmp啊。
6、给李瑶一块板子可以来做升级。
7、如果是bootrom使用u口启动的，那么在第一个出来的网卡中要禁止那个thp协议，否则就无法从pc引导板子。
8、使用小米手机测试的结果：一般、很快、一般、很快、很快。
9、android手机连接p10时，如果使用移动公司的一个smarttest的软件测试速度时只有不到5m，测试时不断有vap-0: [34:80:b3:1a:7f:b5]data pwr save q: overflow, drops (size 50)这样的信息从串口出来。把IEEE80211_NODEQ_MAX_LEN这个值从50改为250,就不会有这样错误了，速度上，有滤波器的机器可以测试到17m。

2015-4-25
1、openwrt/build_dir/target-kraken-sqn-32x0/ppp-default/ppp-2.4.5/pppd/plugins/passwordfd.so这个文件已经存在了，但是没有被openwrt的任何东西包含进去。

2015-4-24
1、突然间，启动不正常了，重新烧片一样，重新启动sequansd一样。重启试试吧。应该是有两台都安装了sequansd的计算机在同一个网络里面就会出现的问题。
2、感觉只编译某个软件，但是这个软件的更新没有进入打包的fw中啊。应该是放错了文件。

2015-4-23
1、继续修改sdk 18332

2015-4-22
1、昨天晚上10点继续升级测试，测试了209次，出现md5错误。后面的升级应该是错误的。貌似没有真正重启。
2、修改mii的bootrom看起来是好的。
3、p10当前出现奇怪的问题，如果一直ping 大包，那么过一会就ping不同，同时telnet web是可以正常访问的，而如果有其他访问ping就又通了。
4、5g的cpe正常。双流cpe正常，4.15号编译的系统。
5、将p10刷成cpe-df的程序，正常。再刷一次，还是正常。
6、把eth1从br0中取出，仍然有问题。
7、用p10编译，打开TZ_SKB_BUFF_FUNC这个选项，仍然有问题。
8、用p10编译，去掉init_proc_files这个函数调用，这样phy的操作就无效。仍然有问题。
9、用p10编译，ATH_GMAC_TXQUEUELEN=200,仍然有问题.
10、刷双流程序，关闭cped等程序，还是正常。
11、使用p10程序，ltercS中不运行任何程序，使用指令加载athr_gmac.ko，设置ip，仍然有问题。
12、使用p10程序，使用双流的athr_gmac.ko，ltercS中不运行其他程序，只加载这个ko，看起来正常。
13、在bigap_p10目录下编译的cpe-df的ko复制进去看起来也是好的。


2015-4-21
1、继续开始p11的升级测试吧。测试了292次，正常。
2、新的sdk直接复制recipe文件居然不能编译。居然要以sqn-32x0-开头才可以。
3、生成烧片文件过程貌似没有问题，等烧一片试试吧。看起来是正常的。
4、如何来升级asw呢，貌似变化了的文件非常多。
5、还要检查一下内核、openwrt两个东西的更新。

2015-4-20
1、面试张勇，陈功，谢兴桥。
2、sdk可以使用里面的khp驱动，新的bootrom，设置sequansd.xml的内容，编译的fw，是可以貌似正常的从pc上启动的。
3、把19322放入现在的git仓中，出现了cmake: /home/jian/.kraken/kbuild/host/58c6c69a04686309ee5e5126d37dd197b143171a4eaabbbc03bb467fe502c70f/staging/lib/liblzma.so.5: no version information available (required by /usr/lib/x86_64-linux-gnu/libarchive.so.13)这个错误，貌似原来也出现过这个错误，不记得怎么去掉的了。把opnewrt中的cmake加入看看？把asw删除就好了。

2015-4-17
1、编译19322的sdk.

2015-4-16
1、看远程数据和4g各数据的意义。

2015-4-15
1、sequans的mac不是写在固定的位置，而是在一个配置结构中。
2、晚上要开始升级测试。又忘记了。
3、那个addresstable可以使用了。

2015-4-14
1、升级后重启来进行测试。执行了46次，停在了准备执行awk上，但是awk其实是正常的。
2、即使是同样的密码错误的过程，windows每次报的错误也不一样。
3、升级了几个用户的内核，pppoe用户名后面有错码的应该是改好了。

2015-4-13
1、安徽有上报说有用户名错误的情况，看起来确实是存在的。
2、测试部发现一台机器无线连接p10不能得到ip，抓包的情况来看，p10发送了ip，但是windows不知道为什么不设置，关闭udhcpd，再开，一样的。关闭笔记本的无线网卡重来，一样的。设置笔记本无线网卡地址则可以ping 到www.163.com。禁用笔记本的以太网，正常了，然后就一直正常了。
3、来做一个升级的测试程序吧。李瑶做了一个，比较悲催的是，使用ie完全没有用，使用firefox可以用，但是第三次就停了下来，打开浏览器的debug选项，再次开始，三次以后就报错了，无论运行什么都变成bus error，重启直接挂掉。使用串口刷机。再来吧。刷机后表现得比较正常了。
4、成功131次后，出现了md5错误的情况，确实算的和文件中的不一样。再重来吧。firefox居然挂掉了，报错。
5、第二天早上来看，这一次运行到晚上10点，也只运行了89次，报升级失败。串口输入两个回车后，无响应了。可以ping通。telnet可以进入但是不出登陆提示。网页无响应。

2015-4-11
1、继续看python：集合。

2015-4-10
1、bin/seq-config.py这个里面貌似没有spi的配置。
2、slic的spi控制命令本身不复杂，命令 地址 数据。fxs本身有许多概念。比如

2015-4-9
1、编译pppoe-l2tp还确实不容易啊。
2、来看slic的资料吧。
LSSGR:LATA交换系统一般要求
LATA：本地接入和转送区
ITU 国际电信同盟
3、看来slic使用的是spi接口，而sequans如何支持spi还是个问题。

2015-4-8
1、对于那个用户常断线的，远程抓包应该是没有意义。因为网络断了，数据也就没法发到远程的服务器上了。
2、强制百兆和我的hp机器相连是正常的。
3、第一次升级貌似会出现某些文件没有升级到的样子。烧了原始的包，然后使用sysupgrade升级后，发现passwd等文件没有升级，还是原来的样子，而banner这个文件则升级了。再次升级后就发现都改变了，真是奇怪的现象。这样的情况有些可怕，万一现场也是这样，那么确实非常麻烦。
4、也有可能是sysupgrade试图保持/etc目录。

2015-4-7
1、李云杰那里有必须要断电重启才能恢复的设备，硬件全部更换了一套，还是这样的，而且都是中间的离线。使用220的系统恢复功能貌似对双流的板子无效。
2、112登陆进去又是白屏，发送ctl+alt+end过去，运行exploer貌似就可以了。看不出来为什么会屡次白屏。
3、刘昌那里两台p10出现密码错误的情况是由于两台机器的无线mac是一样的。
4、李柱栋那里使用sfp升级，basefile那个包居然没有升级到，串口还是直接登陆了。
5、内蒙古的测试还是有内核占用太高的问题。编一个没有netfilter的就可以了。

2015-4-2
1、在windows下执行bin\boot-config rasterize sqn3220-rd-sqn3240-b7_38\bootrom\SQN3220\SQN3220-RD-SQN3240-B7_38.py bootrom 是可以制作bootrom出来的。
2、内蒙古居然把cpe送到了泰尔实验室去做检查，原因是发了一批前年的机器给它们，低温启动有问题。
3、p10的问题是busybox有一位错了，导致awk这个指令无法退出，从而初始化usb的代码无法执行，这样出现了网页上那个at显示为红色。重写程序就没有问题了。

2015-4-1
1、貌似使用gpio里面的edge就可以实现中断。但是现在掉电检测没有接，所以也无法测试。
2、面试游超、潭灿。
3、工厂带来的两个p10都是at不通，但是据说重新刷一次程序就好了。确实是这样。

2015-3-31
1、继续写sequans how to..。
2、处理安徽一个页面设置了mtu 1400 后出现淘宝无法登陆的用户。
3、面试宋臻、黄丹。
4、折腾如何只编译openwrt中的一个软件。
5、当前p11不能使用以太网作为上网，然后pc使用pppoe拨号上网，在lcp包那里就不回包服务器。
6、能够使用lan作为外网之后，貌似正常。但测速上行时，无限报错。估计是转发函数那样写还是效率太差。

2015-3-30
1、今天做了啥，给10个人发送面试邮件，开会，写sequans how to...

2015-3-25
1、貌似ubuntu现在不能拨号了，总是说密码错。
2、高科的路由器还能拨号，但是mtu完全由参数控制，而参数还不能不设置。
3、使用cpe-5g的rp-pppoe拨号程序是可以正常拨号的，而且mtu也是1460。

2015-3-24
1、今天检查为什么王五的机器不能访问淘宝搜索网页的问题。原来是这样，xp下当网卡自动获得ip，取到的网关和dns是p11的地址时，就有这样的问题。win7正常。
2、修改dhcpd的发送规则就好了。

2015-3-23
1、周坦那里的板子sim卡可以人到了，但是必须还是用王壮给的bootrom，这样其他板子都无法检测到卡的。
2、p11从3以后的版本因为更换了内核。而内核中有些遗留的代码居然是错误的。所以导致有一个包的mru包没有替换，xp就仍然使用1480作为mtu值。

2015-3-20
1、要识别到sim真不容易，还是没有成功。

2015-3-19
1、linux强制百兆貌似只有mii-tool这个工具了。
2、设置为强制百兆貌似也没有多少作用啊。
3、遇到一个问题，如果只升级内核，会出现系统被倒回的情况。还��一个片子彻底没法启动的情况。

2015-3-18
1、今天运行为什么永远都是内存不足？昨天还是好的。
2、有卡和没有卡的表现是一样的。
3、如果使用默认的配置编译pc下的内核，那么所以可能需要的东西都会编译一遍。好长的时间啊。
4、rtl的无线模块在pc下可以编译。

2015-3-17
1、新的sdk貌似可以用了。
2、编译dialtool还有很多问题。终于编过去了。
3、网页中使用静态的cmdlib，cgi的大小是287509，而如果使用so，那么就变成了213701，貌似也没有小非常多。

2015-3-16
1、直接clone下来，切换到sdk的分支中，cool a 是正常的。而且没有发现那些个cmake的文件。那么再直接编译新的platform的试试吧。直接编译没有错，因为根本没有编译嘛。那么我先clean一下看看吧。还是可以的，不过多出来许多的cmake文件了。再运行cool a就不行了，不行了。那么删除asw， clean一下呢？看来是可以了，可以了。
2、李柱栋的限制没有限制在用户目录。
3、不行发一个编译器给李瑶，让他试试。已经找到原因，不过比较奇怪的修改。
4、为什么我的机器不能push到249了？pull好像没有问题。
5、cfg 的保存，看来是没有什么问题的。
6、其实，系统跑起来之后，usb还是能搞出一个虚拟网口的。但是看来不会去分配地址。

2015-3-15
1、北京测试发程序。

2015-3-14
1、在77上重新下载，并入18486的bin编译貌似是正常的啊。
2、108开始clone一个目录，写入一个bin，开始编译看看。
3、难道同样一个目录下不能进行两种不同的编译？总之问题非常奇怪。

2015-3-13
1、把新的sdk放进去编译，总是包错啊，非常奇怪的错误。
2、再次编译skd18486，还是要运行cool 2来下载那些文件，否则还是下载不到。

2015-3-12
1、sequans的文档中居然没有寄存器的说明。
2、/dev/at就是一个at接口设备，/dev/ttyGS0是个串口设备，可以执行at指令。

2015-3-11
1、复制新版本的bin目录到仓中，看看编译是否能通过。
2、如果能通过，使用一个全新的目录来编译，看看编译是否能通过。
3、编译后的fw是否能跑。
4、如果不选择那个lua c会怎么样？
5、使用新的sdk生成的文件，做一个烧片文件，是可以跑起来，也看到了phy，插上网线也可以显示连接，但是数据发送接收都是0。

2015-3-10
1、led使用system函数是2501字节，使用内置的fopen之类的以后，变成了2901了。变就变了吧。
2、c程序调用lua脚本并不是非常难。需要以下语句：
    L = lua_open();
    luaL_openlibs(L);
luaL_dofile(L, "/usr/bin/led.lua");
lua_getglobal(L, "flash");
lua_call(L, 0, 0);
lua_close(L);
当然这是无参数的，有参数还要增加。make要加上-llua -lm -ldl

2015-3-9
1、使用alt+enter可以在电子表格中输入换行。
2、刘云那里编译报错是因为出现了0字节的文件，wget下载失败会有个0自己的文件在那里。
3、苗立双编译报错是他的apt-get 没有正确的执行，奇怪的是他的python实际上是安装了的，不是报那个加密包的错误。
4、vim中插入时，使用set paste命令就不会乱了，否则//后面都会加上//
5、编译出错就不要去生成fw和sfp了。
6、要自动在krakan中增加启动脚本，必须以#!/bin/sh /etc/rc.common开头。

2015-3-7
1、python中有布尔类型，字符串类型，列表 [4,3.57,’abc’] 字典 {“jones”:123456, “larson”:3472289,”smith”:3471288}  集合  set([1,3,5])
2、Python的变量可以随时改变类型。
3、Python 中==比较的是两个对象的值， is比较的是相同对象。
4、Python 使用aInt, bInt = bInt, aInt 来交换两个值，不需要显示的中间变量
5、Python 的while可以带个elese
6、Python 有range这个东西。sum是预定义函数。
7、python 支持的整数大的很， 2**512000还能出来值，就是要等。
8、Python 的字符串支持负数下标，str[-1]是最后一个字母。而且支持str[1:5]这样来取子字符串。支持str[::2]这样跳着取。支持str*3来复制。
9、Python 字符串不可改变，要修改，只能产生新的来。
10、Python 有in 运算符。

2015-3-6
1、kraken使用的临时目录，这样都不知道那个luac到底是哪个。在.config也没有记录。
2、必须使用相同版本的lua，否则编译后的文件将不能执行，报这个bad header in precompiled chunk。
3、北京测试还要测一个双流、双频，所以要出一个没有filter的程序。
4、Firefox的升级居然是先从28到29，然后继续升级。29倒是直接更新到了37。

2015-3-5
1、测试李柱栋的程序，貌似正常了。
2、使用222这个地址，就没过一段时间就有一个到0的情况，换到223这里，就貌似正常，速度也非常快，一个pc就达到了7.5m以上。
3、使用iwpriv ath1 disablecoext后，颜斌那里貌似正常了。
4、Opnewrt内置了lua这个东东，看看这个东西是否能替代一下简单的程序和脚本。

2015-3-4
1、把远程桌面的快捷方式发送到桌面上，右键看属性，把目标改为：......\mstsc.exe /w:1024 /h:600 这样可以使用自定义的分辨率。
2、看看platform/tozed/sqn3220-mii-lt30/bootrom/SQN3220这个目录里面的bootrom是否可以正常的切换到fff模式下去。
3、那个supperpro500的烧录器烧sequans的芯片确实有些难度。在那个大的烧录器能烧的片子，在它上面就开始报错了。上午居然没有一个写得是对的。
4、向远程桌面发送ctrl+shift+end来代替+del。112上这样搞一下，注销后登陆进去就正常了。
6、5.8g cpe使用分群是就没有用了，原来是李柱栋发送的是双流的命令，先去掉看看。
7、现在插上sequans，默认网关又不改变了，真是奇怪的事情啊。
8、使用18486里面的share/bootrom/里面的文件放到17922中，做出来的bootrom还是不能成功升级的。那么，到18486目录里面去做吧。里面还没有默认的呢，还要解压另外一个文件。
9、5.8g cpe分群测试，3个cpe分别设置为远中近，参数为10，50，每个pc开两个进程下载，总速率略小于3m，也比较平均。这是有限速的情况，没有限速到了7m了。如果不开分时，那么速度还高一点，不过已经挂了一次了。

2015-3-3
1、把发包字节数强制减去300，那么ping包测试的貌似增加的发送字节数差不多，但是上网就很纠结了，打开网页之前：接收pc 8k p11 34k，打开网易之后，pc 2.9m 而p11高达6.2m。发送上没有原来那么变态，但是pc上300k，而p11上高达2m。
2、再用ping 1000字节看看情况，啊，如果是ping 1000的包，那么发送包的大小会爆到8192个字节。
3、认为data中的第22 23字节是实际字节数。这样改了再测网页，开网页前发送pc 111, p11 116k 打开后，pc 377k, p11 209k比 pc还要小，这就有些不对了。如果是只有ping，就显得差不多，为什么网页会错呢？
4、在p11上直接下载，抓包，貌似没有发现什么问题。

2015-3-2
1、单口的p11，xp电脑pppoe显示发送字节只有675k，发送9m，而在usb0上则高到发送10M，接收19m。
2、重来一次，重启，拨号后pc显示下行7k， 上行6k。 P11上usb0 22k, 105k。开启网易之后，pc显示7m，600k，而p11上下行16m，上行7m
3、重来，用ping吧试试。拨号后pc显示下上行16k,17k，p11上接收63k，发送197k
4、如果使用nat方式来ping，那么pc端就不那么容易看数据了，p11端发送数据刚才发生比接收多30k，现在多50k，这个差距还在增加。
5、注释掉.tx_fixup = cdc_ncm_tx_fixup,这句，那么就上不了网了。

2015-3-1
1、奇怪的问题，使用ffh方式升级那个1005的sfp升级会失败，再次升级后就不能启动了。升级1004也有问题，难道是bootrom不对？每次都报Checksum error for 'acpu/router.fff'，难道是bootrom的问题？那么用tozed-flash-image.rast这个文件试试吧。这个好像是可以升级成功的，难道是那个配置文件的flash有错误？下面是从flash启动的分配：
cat /proc/mtd
dev:    size   erasesize  name
mtd0: 02000000 00010000 "spi0.0"
mtd1: 000c0000 00010000 "Bootrom"
mtd2: 00040000 00010000 "Usim"
mtd3: 00040000 00010000 "Kvs"
mtd4: 00ec0000 00010000 "kernel"
mtd5: 01000000 00010000 "region_fs"
mtd6: 00800000 00010000 "rootfs"
mtd7: 00350000 00010000 "rootfs_data"
mtd8: 00800000 00010000 "rootfs_next"
这个是从ffh方式启动的：
cat /proc/mtd
dev:    size   erasesize  name
mtd0: 02000000 00010000 "spi0.0"
mtd1: 000c0000 00010000 "Bootrom"
mtd2: 00040000 00010000 "Usim"
mtd3: 00040000 00010000 "Kvs"
mtd4: 00ec0000 00010000 "kernel"
mtd5: 01000000 00010000 "region_fs"
如果换成我改的bootrom，使用ffh方式启动时，/proc/mtd内容是一样的。如果直接切换回fff方式，那么就会不停的重启，报以下错误：
[    9.490000] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at
 0x00530024: 0x5fa6 instead
[    9.500000] jffs2: Further such events for this erase block will not be print
ed
[    9.520000] jffs2: Old JFFS2 bitmask found at 0x00535a74
[    9.520000] jffs2: You cannot use older JFFS2 filesystems with newer kernels
[    9.550000] jffs2: Cowardly refusing to erase blocks on filesystem with no va
lid JFFS2 nodes
[    9.560000] jffs2: empty_blocks 62, bad_blocks 0, c->nr_blocks 128
[    9.570000] VFS: Cannot open root device "(null)" or unknown-block(31,6): err
or -5
[    9.570000] Please append a correct "root=" boot option; here are the availab
le partitions:
[    9.580000] 1f00           32768 mtdblock0  (driver?)
[    9.590000] 1f01             768 mtdblock1  (driver?)
[    9.590000] 1f02             256 mtdblock2  (driver?)
[    9.600000] 1f03             256 mtdblock3  (driver?)
[    9.600000] 1f04           15104 mtdblock4  (driver?)
[    9.610000] 1f05           16384 mtdblock5  (driver?)
[    9.610000] 1f06            8192 mtdblock6  (driver?)
[    9.620000] Kernel panic - not syncing: VFS: Unable to mount root fs on unkno
wn-block(31,6)
[    9.640000] Call Trace:
不能理解啊。
2、看看sqn3220-rd-sqn3240-b7_38/bootrom/SQN3220/SQN3220-RD-SQN3240-B7_38.rast这个文件怎么样吧。这个直接不能升级，升级停止在那里。过了很久还是出来了，报什么网络不可到达，奇怪啊。重启似乎还能起来。再试一次。这次和我改的bootrom结果一样了。

2015-2-14
1、那个输入的是接错了。按键可以检测到了。
2、其实还是很容易出现内存不足的情况的，特别是所谓的第一次开机，也就是关机较长时间的第一次开机。
3、sequans-gpio_1_sqn.ipk这个包似乎太简单，应该没啥用。

2015-2-13
1、gpio 41 是中间的那个灯, 0点亮，1熄灭。
2、Gpio42好像无效。量了以后是有效的，估计是灯坏掉了。
3、三色灯是这样的。
	19	20	21
橙色	0	0	0
绿色	0	0	1
橙色	0	1	0
红色	1	0	0
绿色	0	1	1
蓝色	1	0	1
红色	1	1	0
关闭	1	1	1
4、板上的apph是没有upgradebootrom这个命令的，看来pc上和目标板上的程序还不是一个啊。
5、使用原来那个update程序是可以对bootrom进行升级的，但是需要把没有写到的地方由原来的0改为0xff。

2015-2-12
1、修改的io都能有/sys/class/gpio/gpiox目录，并进行操作，改其中一个led，貌似是可以的。
2、3220地板上的phy的协商时间很长，貌似要10多秒，把pc端的接口强制为100m，会快，但是仍然不可引导。感觉是虽然显示联通了，但是数据包还是无法走的。

2015-2-11
1、王壮发来的platform是无法编译的。
2、编译新的sdk-18486
3、改一下bootrom看看io是否能出来。
4、要在线更换bootrom：
   使用指令生成bootrom.
bin/boot-config pack sqn3220-rd-sqn3240-b7_38/bootrom/SQN3220/SQN3220-RD-SQN3240-B7_38.py bootrom
   打开制作工具
   bin/seq-config.py
   上传那个mtools.fw，上传那个bootrom，继续，下载。
   把下载的文件改为default.fw放到sequans communications/firmwares中。
   Pc上运行apph，在apph中运行
   Activate panda
   Upgradebootrom false drop


2015-2-10
1、试了很久的使用那个phy，还把flash焊出了座子。

2015-2-9
删除内容	剩余	编译	Make menuconfig 	Git
drivers/gpio 下没有编译的文件		41428403	修改 ok	done

GPIO	3220PIN脚	功能说明	备注
GPIO3	N1	POW_DET 外电掉电检测
GPIO38	L2	INT_SLIC  SLIC电路中断	暂时未接
GPIO39	K1	SLIC_RESET SLIC电路复位	暂时未接
GPIO40	L1
GPIO41	M2	LED2   WIFI运行灯
GPIO42	M1	LED1   系统运行灯
GPIO18	Y10	BACKSTOR 恢复出厂设置
GPIO19	W9	LEDP1  三色信号指示灯控制蓝色灯信号
GPIO20	V9	LEDP2三色信号指示灯控制绿色灯信号
GPIO21	Y7	LEDP3三色信号指示灯控制红色灯信号
GPIO22	AA7	INT_PHY PHY中断信号	暂时未接
GPIO23	Y9	PHYRESET PHY复位信号	暂时未接
GPIO28	AA10	WIFI_EN WIFI开关


2015-2-6
1、基本可以确定ubuntu12下不能编译的原因是cmake版本不够。
2、如果使用自己的basefile，那么它会在最早写入系统，就不能起到覆盖其他文件的作用了。

2015-2-5
1、又出现了不能访问公司网络的情况，难道是sequans运行在fff的模式下就会这样？切换回去还是一样的，只好手工改路由了。
2、http://www.network-science.de/ascii/ 这个网站可以把ascii字符串改成一幅画。
3、The bat 又发不了邮件了，还是那个什么什么不是合法地址，我又做了啥？换成了新一点的版本也是一样的。这回也没有什么异常文件可以寻找了。

2015-2-4
1、李瑶增加的那个校准区操作不能在ie下显示的原因仅仅是多了一个</div>
2、77开始编译，把下载的文件放到~/.kraken/db/downloads目录下，openwrt/dl里面只做一个链接。Tools看起来没有编译，这次编译不算吧。
3、Cool的clean还不对呢，目录没有修改过来。
4、对于git,push失败后，只要简单fetch，然后再rebase  XXXX就可以了。就可以再push了，不用pull --rebase这样操作。
5、77开始编译。同上。貌似没有什么问题。
6、莫名其妙的出现一次机器不能访问公司网络的情况，ping一下发现Reply from 192.168.15.1: Destination net unreachable.拔掉sequans设备就正常了。但是看route print默认路由还是192.168.19.1奇怪的现象。
7、77上的glibc居然还是2.9版本的，太老了。
8、去年12月23日试图搞过glibc-2.20，但是最后sudo make install的时候elf/sln这个东西直接报段错误。Elf目录下的其他执行文件也有的会报段错误。
9、从日志来看，可以认为是bison,cmake两个之一导致的ubuntu 12不能编译，先把bison编译了试试吧。Bison升级后仍然是报错，那么看看cmake吧。
10、自己的板子上通过sysupgrade升级后可以运行在fff模式下。

2015-2-3
1、find . -name '*.[ch]' | wc -l 这样可以找出所有*.c *.h的文件个数。
2、在uboot中
#define AR7240_APB_BASE                 0x18000000  /* 384M */
#define AR7240_RESET_BASE               AR7240_APB_BASE+0x00060000
#define WASP_BOOTSTRAP_REG		(AR7240_RESET_BASE + 0xb0)
RST_BOOTSTRAP
0 DDR_SELECT 0x1 0 Selects DDR2
  1 Selects DDR1 (default)
3、上面是9341的，9331的是另外的寄存器。
4、77开始编译，删除了linux的include/uapi这个目录。会报这个错误include/linux/types.h:5:30: fatal error: uapi/linux/types.h: No such file or directory
5、强制9331的ddr2为1，看看uboot是否能运行。


2015-2-2
1、108这台机器为什么拒绝我的证书登录呢？难道是安装了samba?

2015-1-30
1、给刘谦发一个程序，当运行时间超过24小时，没有cpe附着时，自动复位。放到一个分支里面去吧。
2、sequans系统在ubuntu 12.04上确实不能编译。
3、编译时直接关闭终端会导致加锁，貌似要删除全部仓可以解决。执行下列指令应该也可以：find . -name ‘kraken.lock’ | xargs rm

2015-1-29
1、当要修改p10的pppoe之类的东西时，准备工作是这样的：
修改内核选择，把pppoe变成M
-CONFIG_PPPOE=y
-CONFIG_PPPOL2TP=y
+CONFIG_PPPOE=m
+CONFIG_PPPOL2TP=m
编译的指令是这样的：
make BOARD_TYPE=tozedap-router_4g CPE_CUSTOMER=CMCC lzma_uimage && cp ../linux/kernels/mips-linux-2.6.31/drivers/net/ppp*.ko /var/lib/tftpboot
在p10上的增加些脚本，加网桥：
ifconfig br0:0 192.168.19.88 up
route add -host 192.168.1.249 gw 192.168.19.1
下载内核并写入：
tftp -g 192.168.1.249 -r zImage.uImage -l /tmp/1.uImage
update /tmp/1.uImage /dev/mtd2
下载ko，并重新加载
set -x
tftp -g 192.168.1.249 -r pppol2tp.ko -l /lib/modules/2.6.31/net/pppol2tp.ko
tftp -g 192.168.1.249 -r pppox.ko -l /lib/modules/2.6.31/net/pppox.ko
tftp -g 192.168.1.249 -r pppoe.ko -l /lib/modules/2.6.31/net/pppoe.ko
killall xl2tpd
killall pppoe-server
rmmod pppol2tp
rmmod pppoe
rmmod pppox
insmod /lib/modules/2.6.31/net/pppox.ko
insmod /lib/modules/2.6.31/net/pppoe.ko
insmod /lib/modules/2.6.31/net/pppol2tp.ko
pppoe-server -I br0 -k -t anhui
这样就可以编译，下载ko。不需要不断重启了。
2、git merge是不需要clean的环境的，rebase才需要。
3、修改记录pppoe用户名，xp和win7测试貌似正常。Ubuntu下拨号貌似记录正常，超长用户名貌似正常。
4、安装一个12.04来编译一下看看吧。为什么李柱栋那里不能编译呢？

2015-1-28
1、mmc0: Got data interrupt 0x00000040 even though no data operation 居然有这样的错误报告出来。
2、给108装个samba吧，sudo apt-get install samba，然后设置共享，windows这里无论怎么输入密码都没有用啊。算了，任何人可以访问吧。但是这样没法写啊。
3、难道每次下载后重编译的内核大小会不同？试试吧：41428403，41428403，看来要用这个值作为基准值了。如果是简单的删除.config呢？应该也是一样的吧？还是41428403。
4、Dev/watchdog应该是有用的，只要cat一下，过一会就复位了。而busybox的看门狗程序在退出的时候会停止看门狗，所以是不会重启的。
5、openwrt/build_dir/target-kraken-sqn-32x0/linux-sqn/下的linux-3.6.7这个目录通过两次软连接，还是回到了kernel/linux-3.7.6来。这不是折腾吗。
6、Watchdog应该是直接编译进入内核的，这样要修改它的长度就不能用它貌似已经提供的参数化的方式。
7、CONFIG_PPPL2TP_RELAY_LCP这个参数没有打开，那么对包的截获还是在pppoe这个程序中进行的。
8、Ppp的标准是rfc 1661。


2015-1-27
1、77开始重新clone并编译，看看linux删除了部分头文件有没有影响。从编译过程和编译后的文件大小来看，貌似正常。
2、发行一个新的cpe-df 31a，主要修改有：a、修正特定情况下搜索显示错误，b、发送数据时，如果对端是n设备，只按n的速率进行发送，c、设置系统时间为2015-1-27，d、增加对数值型wep的加密支持。
3、当前3220的系统看起来不能正常处理中文。使用不同的前端字符集貌似可以创建其对应的文件，但ls显示不正常。把utf-8加上看看。加上了这几个选项还是一样的[('FAT_FS', True), ('MSDOS_FS', True), ('NLS_UTF8', True)]
4、而Atheros的系统，通过串口是可以正常创建中文目录并显示的。
5、http://www.cnblogs.com/masky/archive/2013/01/27/2878996.html 这篇文章认为是busybox做的。修改CONFIG_LAST_SUPPORTED_WCHAR=395101这个值确实可以输入”品”这个字，但是会报内存不足。算了算了。
6、李柱栋那里总是编译不了啊，编译不了。

2015-1-26
1、内核中bridge部分的代码居然没有编译，没有选择bridge功能？在网页配置了一个br0，在配置文件中也没有找到哪里出现了br0。在串口执行grep 1 /tmp/* -r 居然串口无响应了。然后又一次内存不足，开始杀进程。切换fff居然报sfp2不支持。
2、重启以后同样是SFP2 is not supported !!，我删除了什么？从脚本来看，似乎是/sfp2这个文件夹没有存在。使用1月5日的系统也是这样。使用去年12月30日的系统也是这样。从S99sfp2 这个脚本来看，是它做了一个判断，如果是从ffh启动的，就不会去mount sfp2等等动作。笔记本上的那个系统也是一样的。从3120的/init.d/sfp2这个文件来看，没有对这个东东进行判断。
3、确实不记得原来板上的系统了。
4、去掉了那个判断，看来是切换到了flash上运行，flash上的系统居然是1月12日的系统。
5、如果在flash上的系统，那么grep aa * -r，系统不会重启，但串口会停止响应。而通过ssh登陆执行，会停下，但可以终止。
6、编译了net/bp "Network stack bypass"  This acts as lighweight bridge.是不是使用了这个东东来代替网桥？貌似这个东西搜索不出多少东西来啊。看代码是使用sys/kernel/debug/bp这个目录来进行交互的。还不会用啊。
7、那么我们从fff方式，串口登陆系统的方式来试试吧。看来是重启了。第二次试，串口不动了，重开windows串口程序，又好啦。
8、现在只有3853个c文件了。

2015-1-25
1、继续精简sequans内核

2015-1-23
2、让李柱栋加入到sequans的项目来，首先要给他一些资料，还有要给他什么任务。
3、资料包括：sequans网站密码、sequans运行程序、git资料。
4、板上运行grep aa * -r会挂掉。奇怪的事情啊。一个一个目录看看
目录	执行 grep aa 目录 -r
bin  	ok
etc    	ok
lib      	ok
overlay  	无文件
rom      	ok
sbin     	ok
tmp      	报错，不会挂掉。
usr      	ok
version	ok
dev      	很久不出来，不会挂掉
init.rd  	ok
mnt      	无文件
proc     	很久不出来，不会挂掉
root     	无文件
sys     	很久不出来，不会挂掉
 tzwww    	ok
var      	报错，不会挂掉。
www	ok
这就奇怪了，奇怪了。
5、busybox1.01的grep命令没有-r选项。复制一个busybox_1.20到atheros的看看。等了很久也重启了一次，再试一次。这次貌似登陆很久。再来：17:40开始执行，17:43出dev/sdc了。17:55还没有重启。应该不算了。换为sequans系统中的busybox呢？
6、李柱栋那里说无法ping到192.168.15.1，原来是他自己的以太网卡有15的地址。

2015-1-22
1、在使用ffh是，linux传入的参数是rd_start=0x80490000 rd_size=0x00636F19 rdini
t=/init.rd rootfstype=squashfs,jffs2 sqn_sdio.max_freq=46000000 debug 而init.rd是根目录的下的一个脚本。
2、问了一下李柱栋，他原来做的更换busybox的命令行的方法是自己做了一个telnetd的程序，监听端口，自己来解析得到的命令。怎么网上现在搜不到怎么做的了？
3、在busybox增加login后，运行login会出现用户名密码提示了。再找找inittab看看。在./feeds/sequans/sequans-base-files/files/etc/inittab，自己做一个看看。

2015-1-21
2、为什么删除fs/nfsd后，编译的文件还有变化呢？.config没有改变。原来是CONFIG_UIDGID_CONVERTED=y这个东东。貌似修改init/Kconfig后还要把原来的config再复制过来，否则UIDGID_STRICT_TYPE_CHECKS这个东东又会取消。
3、Web中的图像到哪里去了？原来是images这个目录属于被忽略的。如果要只忽略当前目录的images文件夹，在.gitignore中要写成/images。
4、删掉/tzwww/http.cgi后网页的行为还是不一样的，一个是貌似进去再出来，没有cgi，只是登陆按键变灰，然后又恢复。
5、为什么有时候make menuconfig 的.config分明改变了，却没有给出需要保存的提示呢？
6、目标板上fstab这个文件指向/tmp/fstab，/tmp/fstab这个文件不存在。仓中没有fstab这个文件，那么这个文件应该是编译中生成的。在77的work/temp/sequans3220中全文本搜索看看。看来是由openwrt/package/base-files/Makefile这个文件里面的脚本做的。
7、那么同样情况创建的TZ这个文件为什么在/tmp下又存在呢，搜TZ这个文件也没有的。看来是有/etc/init.d/boot这个脚本产生的，看来这个脚本对fstab没有什么兴趣。

2015-1-20
2、把src目录所有的目录都移动到根目录。不喜欢深深深的目录结构。
3、仅仅把bin/tentacle ffh 改变那个elf是不行的，应该是内核有些区别吧。从计算机上日志来看呢，根本就没有合适的fw文件被载入，看来这样的编译3120还是有问题的。

2015-1-19
1、继续精简sequans内核

2015-1-16

2、为什么p10里面的图片都是png格式的？是李瑶自己使用的。
3、我就加了cfg 就又内存不足了？难搞了吧。原来是编译错误产生的包，这也太难了吧。

2015-1-15

2、INSTALL_CONF:=install -m0600 而在linux，install居然是一个应用程序。
3、不知道在哪里对/etc/config里面的内容进行了操作，删除了注释和多余的空行。
4、bin/kraken/openwrt.py这个脚本对init.d目录中的脚本进行处理，在目标机/etc/rc.d/增加了对应的快捷方式，而S后面的值，应该是脚本中START=xx来决定的。
5、uci的使用还是比较简单的，一般的set get，最后要commit才可以。
6、直接想define Package/tzweb_p18/install里面编译cgi看来是不行的，只有把源码复制到build_dir，写相关的makefile啦。

2015-1-14
1、继续裁剪kernel

2、git clone xxxx “dirname” 就可以指定clone后的文件名。
3、一个grep * 2003 -r 居然把sequans的系统搞重启了。
4、增加了ntpd这个包，那么对以太网的dhcp都不干活了？感觉是网口已经不通了。恢复到d9fc37374ae2eeda1180d01c4a69e179ad4c0c8a试试。不行。退到e615144caa7035e8e1728c52c0a793e33c2ed073试试，可以。Drivers/misc中有一股sequan增加的文件啊。
5、使用cento7的光盘作为6.6系统的源，会报出非常非常多的错误来。
6、来比较最后的裁剪的kernel和未裁剪的kernel编译的o文件看看，除了那些build-in.o外，只有一个drivers/video/fb_notify.o，应该没有什么用吧。
7、使用最开始的版本文件大小是
-rwxr-xr-x.   1 jian tzuser 21495959 Jan 14 20:18 vmlinux
-rw-r--r--.   1 jian tzuser 41466139 Jan 14 20:18 vmlinux.o
重新编译一次也是这么大。

2015-1-13
1、在内核的目录下find . -name '*.o' | wc -l，得到结果是1058，也就是只有1058个c文件被编译了。而其c文件则有17995个，不到1/17的文件有用。
2、只有在openwrt显示make[3] -C target/linux install的时候，linux感觉才真正编译，.o文件才迅速增加。
3、精简一下内核
4、fs/hostfs/Makefile居然和arch/um有关。
5、在特定文件中查找find . -name 'Makefile*' | xargs grep video

2015-1-12
1、使用bin/seq-config.py修改后的文件，无法进行升级操作，报这样的错误File rootfs.squashfs is not listed in the version.inf。
2、
文件名	描述
4G-EZ_ASWSoftwareDevGuide_Rev8.pdf 	Sdk 3.3.2如何编译
4G-EZ_ATCommands_ReferenceManual_Rev8.pdf	At 指令说明
4G-EZ_CLIReferenceManual-Rev3.pdf	介绍apph接受的指令
4G-EZ_DVTool-UserManual_Rev5.pdf	设计和校准工具使用方法
4G-EZ_Fujitsu_CalibProc_Rev2.pdf	校准过程说明
4G-EZ_FWConfigUserGuide-Rev1.pdf	使用bin/seq-config.py这个工具来修改sfp文件的某些参数，但该了貌似就没用了。
4G-EZ_HWPlatformUserGuide-Rev5.pdf	硬件平台使用说明，包括bootloader,配置，jtag等，应该看看。
4G-EZ_UE300mTools_RefMan_Rev4.pdf	各种测试、校准的at命令
MB86L13A_HWDesignGuidelines_Rev1.pdf	硬件设计参考文档
Release_Note_ASW2_1_0.pdf
Release_Note_ASW2_2_0 .pdf
Release_Note_LR3 3 2 PRL.pdf
Release_Note_MFW320_ASW230-MR1-15702.pdf
Release_Note_MFW_3_1_0.pdf
RN_MFW3.2_ASW2.3_PRL-14809.pdf
RN_MR1-_MFW3.2.0_ASW2.3.0-15167.pdf	软件发布文档，貌似没啥意义
Sequans Customer Portal Guide v1.pdf	Sequans网站的使用说明文档
Sequans_LTE_Troubleshooting_Guide_v1 0.pdf	Dm-tools常用issue，如何取日志等。
SequansDocOverview_Rev5.pdf	文档的文档。
SequansLTE-ScreeningProcedure-Rev3.pdf	和生产过程相关的。
SQN3120A_Pinout_Rev1.pdf	3120a Pin说明
SQN3120A-Datasheet_Rev1.pdf	3120a数据手册
SQN3120-Pinout_Rev6.pdf	3120 Pin说明
SQN3120-Datasheet_Rev6.pdf	3120数据手册
SQN3120-USB-B13_TestReport_Rev1.pdf
SQN3120-USB-B38_TestReport_Rev1.pdf
SQN3120-USB-B41_TestReport_Rev1.pdf
SQN3120-USB-B40_TestReport_Rev1.pdf	测试结果文件
SQN3140_CalibrationProcedure_Rev3a.pdf	又一个校准过程文档
SQN3140-BallmapPinlist_Rev5.pdf	3140的pin说明
SQN3140-Datasheet_Rev5.pdf	3140的数据手册
SQN3220-Datasheet_Rev3.pdf	3220的数据手册
SQN3220-PinlistBallmap_Rev3.pdf	3220的pin说明
SQN3240-Datasheet_Rev3.pdf	3240的数据手册

3、77开始编译，使用4个进程，机器时间16:23开始，17:21分编完。
4、77开始编译：使用8个进程，机器时间17:23开始，18:20 分编完。
5、77开始编译：使用2个进程，机器视觉18:46开始，20:00 分编完。
6、bin下面的pyc文件已经被存在的.gitignore忽略掉了。
7、李瑶网页中特殊密码的判断应该是在http.c中，没有完全看仔细，但是应该不会被查看页面源码就看出能用什么密码登录了。
8、cpu有几个核就用几个进程编译，多了也没有什么用。

2015-1-11
1、仅仅重新执行build命令，版本文件会做相应的修改，但不会体现到生成的fw文件中。

2015-1-10
1、使用外部编译器实际上在/lib下多了几个文件
lrwxrwxrwx    1 500      500             19 Jan  1  1970 libstdc++.so.6 -> libstdc++.so.6.0.16
-rwxr-xr-x    1 500      500         821868 Jan  1  1970 libstdc++.so.6.0.16
-rw-r--r--    1 500      500           2503 Jan  1  1970 libstdc++.so.6.0.16-gdb.py
2、使用外部编译器的系统，正常4次，异常3次。
3、如果只删除staging_dir，会在最后报找不到base-files.depends这个文件的错误。
4、使用108机器编译的系统：正常2次，异常3次。
5、在108上编译，如果使用外部编译器，那么只要编译15分钟。
6、限制使用108 7035f830cc68a525eee25e97567e9ae23cdf9d84位置编译的文件测试：正常9次。
7、108开始编译，到位置c67abf6441b79efea9fb884310b10e74ffdf9b77，修改为不使用外部编译器编译。注释是“外部编译器：编译脚本支持下载外部编译器.”这个就已经报错了。
8、77开始编译，到位置fe56aa34d00e38ecfe860c720c72ccd756879836，注释是“删除无用的目录src/asw/installer/”，修改为不是有外部编译器。编译成功啊。rm /home/jian/.kraken/kbuild/再试。
9、249开始编译，到位置81d69e6dcec0bd752bd667a1da6bc418edf44a47，注释是：编译的时候显示tozedp18，也编译成功了，难道是108的bash有问题？
10、108开始编译，位置还是c67abf6441b79efea9fb884310b10e74ffdf9b77，把那个cp命令前面加一个-，试试吧。报错，先注释掉那一行吧。编译成功。来试试吧。正常10次。
11、249到最新的位置，修改为不使用外部编译器，开始编译。


2015-1-9
1、77开始编译：src/asw/apps/app/jdm/ ok
2、108开始编译：src/asw/omadm这个目录变成了只有bin档的东西了。又来啦fatal error: gram.h ok
3、77开始编译：src/asw/apps/build/android/
4、笔记本全新centos 6.6 amd64开始编译，其系统时间为17:25，18:19编译完成，看起来ccache至少和编译器不同而不同了。这一次只用了55分钟。Ccache的目录也只有289m，没有增加多少，说明编译的过程中几乎都命中了。
5、108开始编译src/openwrt/feeds/community/sound 又来了：fatal error: gram.h
6、笔记本上把ccache放到/dev/shm/ccache中，看看ccache在内存中，编译的速度是否能快些。虚拟机系统时间：18:34开始。19:14编译完成，40分钟，少了15分钟吗，要用个新机器来试试才知道。
7、77开始编译：multimedia
8、src/openwrt/feeds/community/mail/这个目录才100多k，先不管它吧。
9、108开始编译，去掉tools中的ccache，从ccache的脚本来看，只要系统有ccache，那么就不会去编译它。所以toos/Makefile可以不修改。
10、Ccache这个东西在centos中居然没有在yum中，只好手动安装了。
11、process_cli这个函数在bin/pyu/src/cli.py中，也就是把功能、选项和参数分解再调用不同的处理过程。
12、77开始编译： src/asw/apps/host/wdc
13、linux脚本支持字符串数组，还是很方便的。
14、linux脚本中，变量赋值的等号两边是不能有空格的，又中招了一次。
15、linux脚本中 tr -d '"'命令可以去掉字符串中的引号。
16、又出现一次内存不足杀sequansd的现象，重启后又没有出来了。又出来一次。难得是偶然现象？使用去年12/30的版本试试吧：正常10次。

rm host/bin/iso -rf
rm host/share/firmware/ue/sqn31x0-fjt.fw
rm host/share/firmware/ue/sqn31x0-sqn.elf
rm host/share/firmware/ue/sqn31x0-sqn.fw
rm host/share/firmware/mtools -rf

2015-1-8
1、77开始编译src/openwrt/openwrt/target/linux/omap4 ok
2、108开始编译 src/openwrt/openwrt/target/linux/mpc52xx/ 再次出现fatal error: gram.h，这错误永远是108这台机器才会出现。不知道是这台机器硬件的原因还是64位编译器的原因。继续留意吧。ok
3、77开始编译 src/openwrt/openwrt/target/linux/mpc85xx/ ok
4、108开始编译：src/openwrt/openwrt/target/linux/mvebu/  fatal error: gram.h。
5、笔记本，新centos 6.6 32位系统，把原来的ccache放好，看看编译时间是多少。虚拟机上的时间17:33开始编译。19:13编完，完全没有起到效果啊，ccache目录从250m到了487m，难道32位系统和64位系统不同？
6、测试一下cpe-5g2g 连接wep加密的能力。
7、77开始编译：src/openwrt/openwrt/target/linux/uml/ ok
8、108开始编译：src/openwrt/openwrt/target/linux/ppc40x/ ok
9、77开始编译： src/openwrt/openwrt/target/linux/orion/ ok
10、108开始编译：src/openwrt/openwrt/target/linux/ppc44x/ ok
11、77开始编译：src/openwrt/openwrt/target/linux/pxa ok
12、77开始编译：src/openwrt/openwrt/target/linux/ramips/ ok
13、108开始编译：src/openwrt/openwrt/target/linux/sibyte ok
14、108开始编译：src/openwrt/openwrt/target/linux/realview/
15、77开始编译：src/openwrt/openwrt/target/linux/generic/patches-3.3，6，8，9 ok
16、108开始编译： src/openwrt/openwrt/package/platform/ 编译通过，但是文件明显很小。有问题。Cool clean 后还是很小，那么重新clone试试吧。这样好了，难道是做了一次rm src/openwrt/openwrt/package/操作，然后使用git checkout回来出的问题？
17、77开始编译：src/openwrt/openwrt/.sqn_deploy ok
18、77开始编译：rm src/openwrt/openwrt/package/broadcom-* ok
19、108再次编译src/openwrt/openwrt/package/platform/， 又出现了fatal error: gram.h:，这台机器真奇怪。Ok
20、host/openwrt/package/marvell-wlan-*这个目录似乎在3220的sdk中没有存在了。
21、77开始编译：src/openwrt/openwrt/package/boot/ ok
22、77开始编译；./src/openwrt/feeds/community/net/madwifi ok
23、108开始编译：./src/openwrt/feeds/community/utils/psplash ok
24、再次测试了一下atheros和中兴设备的wep方式连接，注意到以下几点：
中兴设备的密钥不可以设置为第二组。
中兴设备的那个“支持混合认证”这个东西选择了，保存后又不选择了。
中兴设备从wpa到open&shared key后，两次都无法连接了，重启后正常。
有时候ping不通要arp -ad
有时候ping不通要重启中兴设备。

2015-1-7
1、77开始编译：rm  src/asw/drivers/win32 ok
2、249开始编译：rm src/asw/drivers/macos/  ok
3、在openwrt/Config.in中增加对通则类型和版本的选项.
4、Linux mint这个东西完全是基于ubuntu啊。
5、77开始编译：rm src/asw/apps/app/androidFwUpgrade ok
6、src/asw/apps/app/cm/ 这个难道是connect manager这个程序？那么先留着吧。
7、249开始编译：rm src/asw/apps/java/ ok
8、77开始编译：openwrt/target/linux/adm5120
9、249开始编译： src/openwrt/openwrt/target/linux/adm5120 为啥两个编一样的。浪费时间啊。
10、如果/lib/ld-uClibc.so.0不是一个链接而是一个文件，那么系统就会报内存不足，并杀死sequansd这个进程。
11、77开始编译：src/openwrt/openwrt/target/linux/adm8668 ok
12、249开始编译：src/openwrt/openwrt/target/linux/amazon/ ok
13、笔记本上新安装的linux mint开始编译15:33.17:04编完。删除目录，重新clone下来17:09开始编译，看看ccache是否有作用。18:00编完。减少了约40分钟/90分钟。看起来还是非常有效果的。
14、249开始编译 rm src/openwrt/openwrt/target/linux/ar7  ok
15、77开始编译： rm  src/openwrt/openwrt/target/linux/ar71xx/ ok
16、77开始编译：src/openwrt/openwrt/target/linux/at91 ok
17、77开始编译：src/openwrt/openwrt/target/linux/atheros/ ok
18、108开始编译：src/openwrt/openwrt/target/linux/au1000/ ok
19、77开始编译src/openwrt/openwrt/target/linux/avr32/ ok
20、108开始编译：src/openwrt/openwrt/target/linux/brcm2708/ 失败，又是gram.h这个东西找不到，其实是有的，难道是某个东西没有写好？从radvd这个原始包来看，确实没有gram.h这个文件，只有gram.y这个文件，内容比较像头文件。
21、77开始编译：src/openwrt/openwrt/target/linux/cns21xx/ ok
22、笔记本开始编译： src/openwrt/openwrt/target/linux/x86 使用cool clean 18:25开始19:10编完。45分钟。考虑打包一个ccache，这样加快第一次编译的速度。
23、108开始编译：src/openwrt/openwrt/target/linux/brcm47xx/ ok
24、77开始编译：src/openwrt/openwrt/target/linux/cns3xxx/ ok
25、108开始编译：src/openwrt/openwrt/target/linux/brcm63xx/ ok
26、249 开始编译： src/openwrt/openwrt/target/linux/sparc ok
27、expr length "abcd" 使用这样的脚本来取字符串长度。
28、108开始编译：src/openwrt/openwrt/target/linux/cobalt/ ok
29、249开始编译：src/openwrt/openwrt/target/linux/ep93xx/ ok
30、77开始编译： src/openwrt/openwrt/target/linux/gemini ok
31、108开始编译：src/openwrt/openwrt/target/linux/iop32x/ ok
32、77开始编译：src/openwrt/openwrt/target/linux/ixp4xx/ ok
33、249开始编译: src/openwrt/openwrt/target/linux/kirkwood/ ok
34、108开始编译： src/openwrt/openwrt/target/linux/lantiq/ 再次出现那个头文件找不到的情况。ok
35、77开始编译：src/openwrt/openwrt/target/linux/malta ok
36、108开始编译：src/openwrt/openwrt/target/linux/mcs814x/ ok
37、249开始编译： src/openwrt/openwrt/target/linux/mpc83xx/ ok
38、108开始编译：src/openwrt/openwrt/target/linux/omap24xx/ ok
39、249开始编译：src/openwrt/openwrt/target/linux/rb532/ ok
40、77开始编译：rm src/openwrt/openwrt/target/linux/xburst/ ok

2015-1-6
1、77编译：去掉mklibs ok.
2、249编译：去掉patch ok
3、当前仓可在ubuntu server 14.04 amd64新机器上编译通过。
4、http://centos.ustc.edu.cn/ 这个地方不错能快速下载到多个linux的发行版。
5、Sed替换中存在变量，那么那个单引号就不能用了。
6、77编译：去掉patch-image ok
7、249编译：去掉e2fsprogs，报错，mtd-utils需要这个东西。
8、249编译：去掉mtd-utils，ok
9、77编译：去掉e2fsprogs ok
10、249编译：去掉xfce-macros ok
11、108编译：去掉yaffs2 ok
12、笔记本centos 6.6 64位 新机器编译通过。
13、笔记本编译：去掉flock ok
14、249编译：去掉cmake ok
15、77编译：去掉bison ok
16、77编译：去掉 xorg-macros ok
17、249编译：去掉genext2fs ok
18、在3220的sdk中protobuf这个库编译使用外部编译器不会报错啦。
19、啊，还有lib中的库还有问题。
20、77编译：去掉firmware-utils 16:48开始 17:29完成。这样都要40分钟啊。
21、249编译：去掉flex 16:54开始，17:38编完。
22、Ubuntu 14.10的git版本已经升级到了2.1
23、77编译：去掉lzma ok
24、249编译：去掉missing-macros 失败，编译radvd的时候报一个头文件没有，奇怪的事情，missing-macros里面都是些m4的文件。再编一次就好了，可能是并行的数量太多了？
25、77编译：去掉mm-macros ok
26、249编译：去掉missing-macros 重编。
27、笔记本编译使用外部编译器的版本居然也要两个小时，时间太长了。当前仓可在ubuntu server 14.10 desktop-amd64新机器上编译通过。
28、77编译：去掉patch ok
29、249编译：去掉sed ok
30、77编译：去掉m4 ok
31、249编译：rm ./src/asw/installer -rf ok

2015-1-5
1、就使用当前这个仓吧，也只有34m，这样的仓大小，还是完全可以容忍的。
2、来增加一个设备类型文件吧。
3、ubuntu上增加那个pycrypto要sudo apt-get install python-pip, sudo pip install pycryto才可以。
4、在249上编译一次居然要1小时20分钟，还是在使用了ccache的情况下。
5、开放版貌似没有用了，换到笔记本正常，换回台式机又正常，难道是usb的供电问题？奇怪。和供电没有什么关系，有时候好，有时候不行，还没有摸到规律。
6、在正常的情况下，249编译的fw是可以运行的。
7、当前仓，不连互联网是可以编译的，在77上测试通过。
8、 cat /proc/cpuinfo | grep cpu，这样看来249居然只是一个双核的处理器。77还是个4核的。
9、在笔记本上居然报什么时间不对，然后总是等啊等。
10、只把下载文件复制到~/.kraken/db/downloads目录下是没有用的，看来还要建立链接，那么就没有太大的必要了。
11、增加sqn3220-rd-sqn3240-b7_38/openwrt-cfg/tozedp18.pkg 这个文件，改成一个ecm，编译完成后的fw还是出两个网卡。
12、ubuntu在ll时，可执行的文件会带上*，多此一举吧。
13、去掉这些没用的tools scons mkimage

2015-1-4
1、如果编译的时候强行关闭机器，那么就有kraken显示lock了，还删不掉。
2、错误的在分支里做了一次git pull origin master，失败了，但是现在checkout master就变得非常麻烦了。删掉重编吧，郁闷了。
3、如果没有联网，还是有很多的工具没有下载的。一个一个补上吧。
4、如果把bin/tentacle build ... 写在脚本里面运行，那么ctrl^c是无法中断的，真是奇怪啊。
5、对于无法自动安装pycrypto这个东东的机器，手动安装方式：
wget https://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-2.6.1.tar.gz
tar xf pycrypto-2.6.1.tar.gz
cd pycrypto-2.6.1/
python setup.py build
sudo python setup.py install
6、在77上编译，出现了 /usr/lib/libstdc++.so.6: version `GLIBCXX_3.4.15' not found 这个错误，到原来编译的gcc 4.8目录， cp ./gcc-build-4.8.2/i686-pc-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6.0.18 /usr/lib，把/usr/lib/libstdc++.so.6指向它。真不知道会出什么样的问题。77这台机器应该是被折腾的面目全非了。怀疑会有一天莫名其妙的无法启动。

2014-12-31
1、1093911726。Qq申请后的好友克隆没用，也许要换一个浏览器试试。就冻结了。
2、苗立双发邮件声称的baidu搜索后无法访问，是linux pppoe拨号程序没有改变mtu的原因。
3、编译不成功可能是编译的

2014-12-30
1、貌似自己建的仓可以编译了，来修饰一下吧。
2、难道只是编译成功，合成的sfp文件和fw文件明显要小5m。感觉是文件区太小了，只有1m多，难道很多的东西没有编译？加入feeds目录中的文件后sfp貌似到8m了，不过比原来那个还是要小一点点。加上obj和share这两个目录好像也没有什么变化。
3、自己编译的fw是可以加载的。

2014-12-29
1、使用那个kraken就用吧。先做出一个能编译的仓来。
2、如果centos安装的时候选择纽约，yum的速度好慢啊。
3、如果出现no module named Crypto.Cipher ，那么要用 sudo yum install pycrypto。

2014-12-27
1、笔记本上的sdk4.1.1.0还在编译，漫长的过程，有一次出错，再编译一次又继续了，奇怪啊。
2、要脱离那个什么kraken还真的比较复杂，搞了两天了

2014-12-26
1、终于编译完成了sequans的那个sdk 4.1.1.0，它在openwrt上又包裹了一层什么kraken，完全不知道这是个什么东东。按照一般理解，它只需要提供新的几个bin档就可以了，结果变得非常复杂。它在SEQUANS-4.1.1.0-17922这个目录就不那么大了，只有2.8g，而~/.kraken目录就高达3.5g。

2014-12-25
1、做如下的测试，在如下全新系统进行编译
	Ubuntu 14.04	Centos 6.6
32位		1、对新机器来说，缺少了xz
编译成功。
64位
2、使用外部编译器，去掉gmp还是没有问题的。本来就没有编译，浪费时间。
3、busybox的date指令需要使用这样的格式date "2014-10-01 12:00:00"

2014-12-24
1、如果在tools/Makefile中去掉libtool, 那么会提示Libtool library used but `LIBTOOL' is undefined。
2、去掉m4好像是可以的。
3、笔记本上9:53开始使用外部编译器编译。可能是11：08编译完成的。时间超长啊。如果加上编译器的编译，那么时间是2小时25分。
4、这个文件 ../apps/host/sqndcc/csharp/dcc.cs为什么会改变。
5、77上删除了tmp/.host.mk这个文件
6、108上修改了一下编译选项：[*] Strip unnecessary exports from the kernel image                                                        x x  x x [*] Strip unnecessary functions from libraries，报错了，看来需要mklibs这个工具。现在报这样的错误：Exception: Cannot find lib/lib/ld-uClibc.so.0。如果使用tools/Makefile中增加mklibs，让openwrt自己编译mklibs，那么就可以编译通过了。生成的sfp文件确实小了200k，但是升级后，在目标板上仍然是3.6+4.5m的格局。算了。
7、目标版上居然有个stress，压力测试工具。删掉它看看。编译成功了，sfp文件小了一点点。
8、增加应用程序应该比较简单，可以参考那个wdtApp的。
9、内核中似乎没有加上80211q选项，但是vconfig可以正常运行，奇怪的现象。进入build_dir/target-mips-openwrt-linux-uclibc/linux-sqn31x0_sqn3120-hostless_ecm/linux-3.7.6目录再执行 make ARCH=mips menuconfig，好像不受外面的控制吧。

2014-12-23
1、按照http://xg2007524.blog.51cto.com/869106/1337465这个文章来对77的gcc进行升级。好像还是不行，看来只有升级ulibc了。
2、按照http://www.cnblogs.com/gw811/p/3676856.html这个来试试吧。
3、碰到了这个问题hese critical programs are missing or too old: as ld，那么参考这个http://blog.csdn.net/fjb2080/article/details/4777220来更换ld，安装后的ld在/usr/loacl/bin中，复制到/usr/bin里面吧。
4、继续configure ulibc，新的问题来了checking installed Linux kernel header files... missing or too old! 77这个系统真的是太老了。复制249上的/usr/include/linux目录过来
5、新的的告警是*** On GNU/Linux systems the GNU C Library should not be installed into *** /usr/local since this might make your system totally unusable.那么加上../glibc-2.20/configure --prefix=/opt/glibc-2.20试试吧。不报错了，开始make -j4编译吧。
6、/usr/include/linux/swab.h:6:22: 致命错误：asm/swab.h：没有那个文件或目录，看来复制的东西还少了些。致命错误：asm-generic/param.h：没有那个文件或目录。那么继续复制吧： scp -r jian@192.168.1.249:/usr/include/asm-generic .
 scp -r jian@192.168.1.249:/usr/include/asm .
7、make 通过了，sudo make install，这都会报错啊make[1]: *** [install-symbolic-link] Segmentation fault。


2014-12-22
1、今天来测试p10的上网，王伍测试任务连续点4个站点，就可能导致p10几乎没有速度了。正常8次。
2、source insight 对*.cc文件不解析啊。在option|preferences中的languages中的c++ language增加文件后缀就可以了。http://www.cnblogs.com/chinacloud/archive/2010/11/17/1880127.html
3、在77上使用外部编译，ERROR: CONFIG_SOFT_FLOAT is enabled but the external toolchain does not support it，这个东东曾经见到过，忘却是如何解决的了。在249上使用外部编译器也是这个错误了，奇怪。直接执行里面的gcc，报“不能执行的二进制文件”，对了，我使用的是64位系统编译的，放到32位的系统上自然是无法运行了。
4、ubuntu运行32位程序：sudo apt-get install lib32stdc++6 lib32z1 lib32z1-dev，cent os 的是yum install libgcc.i686 glibc.i686 zlib.i686

2014-12-19
1、这样做貌似就可以编译那个curl了
cp staging_dir/target-mips-openwrt-linux-uclibc/lib/libdl* staging_dir/target-mips-openwrt-linux-uclibc/usr/lib/，貌似只要这个usr/lib下有这几个文件就可以了。这几个文件复制到toolchain---的目录下是没有用的。
2、使用外部编译器还缺少了libuClibc-0.9.33.2.so这个库，真不知道这些库是怎么搞的。

2014-12-18
1、这样好像还是不行ln -s /opt/mip-gcc/lib staging_dir/target-mips-openwrt-linux-uclibc/lib，那么 ln -s /opt/mip-gcc/lib staging_dir/toolchain-mips-openwrt-linux-uclibc/lib这样试试吧。还是不行啊。
2、突然发现the bat 不能发送邮件，使用其他软件可以发送，认为不是系统的问题，把the bat 复制到其他机器，可以发送，又是系统的问题？还好thebat 有个异常，说是foxmail的某个动态库加载异常，MAPI #0: Foxmail [Foxmail]; Path: D:\Program Files\Foxmail 7.2\FMMAPI32.dll  (not valid)从注册表中搜索这个动态库，删掉相应的条目，终于可以发送了。message xxxx with subject xxxx is not properly addressed

2014-12-17
1、ld-uClibc.so.0 -> ld-uClibc-0.9.33.2.so没有了这个链接，就会出现./dropbear: not found这样的提示。

2014-12-16
1、在Sequans Communications\Firmwares只有一个default.fw的情况下，是可以从ffh方式启动的。但是自己编译的那个fw无法启动。而使用sequans提供的那个，还是无法进行升级。
2、现在做一个这样的版本，不删除多余的包，再次进行ffh方式的编译看看情况如何。这样编译后的文件还是和原来的一样大，估计没啥用。确实是一样的。
3、从网上搜索的情况来看，./dropbear: not found 这样的原因是编译器不同。复制一个没有使用外部编译器的dropbear上去，也同样报这个错误。


2014-12-15
1、ftp中出现了一个新版本的sdk，但是目录结构似乎已经改变了。找到了deploy.sh，居然在.sqn_deploy这样的隐藏目录中。
2、再次成功使用外部编译器编程成功了，错误还是和原来是一样的，网卡不通了。从串口来看，似乎许多东西没有了。如果直接设置地址进行升级呢,curl not found，奇怪啊，本身升级包并没有减少多少。/usr/bin/curl是存在的，但是执行它，还是curl not found

Atheros todo list 不用置顶了。
12、做一个每日重新全编译的脚本。
31、在cpe中，如果mcu发来的txpower过小，导致不能连接，那么要恢复原来可以连接的值。
35、在某些情况下，有遮蔽是，如果把cpe的速度不设置为自动，而是设置为手工6.5m，效果反而更好。在程序中要体现。
38、制作文件系统时，链接文件应该只比较链接文件本身，不要比较链接到的文件。
50、cpe-8m, ap增加对通用寄存器的读操作功能
54、写片文件的uboot考虑使用固定的版本。
59、在nat模式下远程升级一定是有问题的。
62、双流的cpe的makefile中编译uboot使用的还是cpe-5g的u-boot的编译方式。如果两者有区别后，再分开。
64、改写Makefile中的busybox代码，如果.config文件和需要复制的文件一样，就不要做clean操作了。
70、把9311的vlan功能放到网卡驱动中去，这样，cped的程序就能直接写一个统一的文件就好了。
71、考虑在ap中设置选项，如果系统采用的是pppoe拨号方式上网，可用完全禁止下行的广播包。
74、iptables对网桥无效的问题，或许是内核中的有的东西没有编译？
75、使用vlan时，会发生cpe访问错误的情况。
80、5g cpe的灯会狂闪。
81、ap增加加密功能
82、Ap增加多ssid功能
83、在做三流的ap时，把加密的东西加入。
84、把ap中单流双流的设置改为直接使用指令。
85、ap上报程序中，内核版本只需要读一次就可以了，不用每10秒读一次。
88、cpe中的udp端口限制还是错的。
89、beacon包中同时存在ssid(0x0)和自定义ssid（0x90）的情况下，而且数据不一样，那么cpe是否会误判？
90、beacon是否可以按照124毫秒的间隔进行发送？
102、分时的设置应该绑定到某个mac上，现在是两个不分。
104、现在ap内置的简单的tc会挂掉。

2014-12-5
1、sudo apt-get install texlive-latex-extra，这个超大啊。

2014-11-27
1、coreutils-8.23可以编译出可以使用du -hd1这样指令的du来，编译后复制src/du到原来的du就可以了，否则每次使用max-depth太麻烦。

2014-11-26
1、sequans居然要求cmake在2.8以上，也许是我从工具中删除了cmake。
2、编译docs中的东西要sudo apt-get install texlive-latex-base，好大啊。sudo apt-get install tex4ht。

2014-11-25
1、netifd这个东西是使用git的，这样你怎么去统一？在内网没有的情况去公网下载？

2014-11-24
1、openwrt中scripts/localmirrors中的地址应该是最优先下载的。这几个还是放到cfg中去复制一下吧。

2014-11-13
1、sequans的升级好像没有什么作用。
2、Openwrt的tools中存在依赖关系，所以要去掉某个tools的编译，要先查依赖关系。

2014-11-12
1、bakefile-0.2.9居然有make uninstall这个东西。

2014-11-11
1、openwrt的编译居然提示不要使用root来进行编译。

2014-11-10
1、centos 增加用户除了useradd还必须passwd后该用户才可以登陆。
2、已经有两个人报ap和路由器相连后不通的情况了。奇怪的问题。

2014-11-6
1、编译fff的还需要更多的包和gccxml这个东东。编译完成后总占用的空间为6.9G.
2、Openwrt的备份是把/etc和./var目录复制下来。
3、Sequans这个设备的可用内存少得可怜啊。

2014-11-5
1、使用tar Jcvf host.tar.xz host 压缩出来的压缩包是tar.gz格式的一半，压缩时间明显较长。
2、Sequens的openwrt编译需要bakefile的0.2.9版本，而编译这个bakefiile又需要sudo apt-get install python-dev。

2014-10-30
1、在64位的centos上编译p11，还要增加yum install zlib-devel.i686 glibc.i686这两个库，貌似这两个库都是那个mkfs.jffs2需要的。
2、现在安徽的l2tp拨号后，在ip138上得到的ip是正确的了。
3、当前使用安徽的l2tp做下行发udp包测试，可以连续发800个包貌似不丢包。如果使用以太网来测试，也差不多。
4、昨天使用以太网时，speedtest上行测试报错，今天又可以了，也许是换了PC？
5、在64位的系统上编译atheros的系统上是可以的。

2014-10-29
1、这个地址下载非常快：http://centos.ustc.edu.cn/centos/7.0.1406/isos/x86_64/
2、Centos 7在vm中安装后找不到eth0啊，升级到最新的vm也没有。
3、使用新版本的vm player，安装centos mini的时候，不可以使用简易安装，必须选最后一项。否则安装过程中会报错，安装后虚拟机无法启动。

2014-10-23
1、uboot中有dhcp的指令，可以得到地址。

2014-10-21
1、 openwrt在ubuntu上需要：sudo apt-get install libssl-dev
2、 mtd-utils-1.4.5.tar.gz这个文件已经不能从openwrt里面的脚本取了。报对方断线。
3、新的openwrt在ubuntu 14.04 64bit上可以编译，但在centos上不能编译，重新放到一个新的目录上看看吧。在新的目录上可以编译通过，奇怪了。

2014-10-20
1、9882这个芯片似乎很没有驱动的啊，从atheros和openwrt都没有出现第二个无线设备。
2、使用最新的buildroot, gcc 4.8.3 来编译atheros sdk中的内核，还是跑不起来。
3、Buildroot中，运行了make menuconfig 增加2g大文件支持后，居然要make clean之后，才能重新编译。
4、当前的openssl 需要yum install openssl-devel.i686 openssl.i686才能继续。

2014-10-16
1、从cvs导入到git中，如果存在中文文件名，那么文件名就没法在windows下正确显示了。

2014-10-15
1、在导入cvs的仓时，要在先执行一下：
git config --global i18n.commitEncoding = GB2312，然后在使用git cvsimport命令，再在.git/config文件中加入
[i18n]
       commitencoding = gbk
这样，原来提交的中文备注就可以在gitk中显示了。Git log仍然显示为乱码，就不管了。
2、gitk --all 就可以查看所有的分支了。

2014-10-14
1、sudo apt-get install git-cvs，然后就可以使用git cvsimport -v -d :pserver:user@xx.sohu.com:/var/spool/cvsroot/ test_module这样的指令来把cvs的仓库导入到git中。
2、删除所有文件，只留下.git目录后，运行git checkout * 就可以把文件还原了。

2014-10-13
1、gcc: error trying to exec 'cc1plus': execvp: No such file or directory，这个应该是要安装g++, sudo apt-get install g++
2、 File "/usr/lib/python2.7/subprocess.py", line 710, in __init__
    errread, errwrite)
  File "/usr/lib/python2.7/subprocess.py", line 1327, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory
这个居然是gperf这个东东没有安装，sudo apt-get install gperf

2014-10-11
1、这篇文章写在ubuntu上如何切换java的版本
http://blog.manishchhabra.com/2012/05/installing-oracle-sun-java-jdk-and-setting-java_home-in-ubuntu-linux/
2、如果同时存在一样的ssid，信号强度相差较大，那么cpe连到信号较好的去。从一个ap中踢掉cpe，cpe会立即连接到另外的ap。
3、Tozed-s8这个东西还必须在64bit的linux中编译？过分啊。
4、Ubuntu 和windows之间，使用git的scp速度只有2m，而是要ftp能达到网卡慢速，区别大了。网线直接连接可达30m，不过不太稳定。
5、error.GitError: config: [Errno 2] No such file or directory，这个错误应该是没有安装git-core吧。
6、prebuilts/tools/gcc-sdk/g++: line 40: prebuilts/tools/gcc-sdk/../../gcc/linux-x86/host/i686-linux-glibc2.7-4.6/bin/i686-linux-g++: No such file or directory 应该是没有安装gcc。sudo apt-get install gcc-multilib
7、libz.so.1: cannot open shared object file: No such file or directory，要安装lib32z1
8、error while loading shared libraries: libstdc++.so.6: cannot open shared object file: No such file or directory 要安装lib32stdc++6.
9、还要安装unzip，否则会报没有找到unzip，但是貌似也能过去
10、make: *** [out/host/linux-x86/obj/EXECUTABLES/aidl_intermediates/aidl_language_y.cpp] Broken pipe，装上sudo apt-get install bison flex libxml2-utils lzma zip这几个再说。
11、make -j4能快些吧。

2014-10-10
1、配置中增加这些，启用双phy。
+export ATH_GMAC_SUPPORT_DUAL_PHY=1
+export ETH_CONFIG=_s27
+export ETH_CONFIG2=_ar803x
2、ubuntu 14 有时候会使用ipv6，比如提示这样的信息
Cannot initiate the connection to ph.archive.ubuntu.com:80 (2001:d18:1:1::94). - connect (101: Network is unreachable) [IP: 2001:d18:1:1::94 80]
在/etc/sysctl.conf中增加这样的设置：
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
然后执行：sudo sysctl -p
参考：http://askubuntu.com/questions/440649/how-to-disable-ipv6-in-ubuntu-14-04
3、ubuntu 14的vnc server必须增加以下设置，才能被原来的vnc viewer所登陆：
gsettings set org.gnome.Vino require-encryption false


2014-9-29
1、使用移动的网络对时，那么貌似ntp.sjtu.edu.cn之类的更好，国外的对时地址直接不能访问。

2014-9-28
1、使用od -x filename 来用16进制查看文件内容。

2014-9-26
1、busybox的shell貌似没有Shellshock漏洞。

2014-9-24
1、继续测试安徽的l2tp吧，测试“使用安徽的l2tp server，在pc端使用测试软件按照可用的用户名密码进行不断拨号。”拨号间隔为1分钟。22：00开始，可用内存为36.3m，到26日早上还要35.6m，到27日早上还要35.2m，28日9:00还有34.8m。继续测试。

2014-9-22
1、在泰然使用的ap-cp这个，好像没个小时会断一下线，我已经把那个“流量百分比”改到了0，/tmp目录下也没有相应的文件。
2、要实现多ssid并加vlan也不是很复杂：
brctl addbr br1
makeVAP ap-wds SSID2 0:RF:6:11NGHT20
activateVAP ath1:0 br1
vconfig eth1 add 100
ifconfig eth1.100 up
brctl add if br1 eth1.100
ifconfig br2 up
那么通过SSID2 连上的，从eth1出去的包，就带有vlan 100了。
3、颜斌买的938x的网卡是可以抓到5.8g 300m情况下的ping包的。
4、把cpe-df的程序直接写到苗立双的板子上，最边上的端口就是eth0了。这个时候，最边上的口拔插，所有寄存器都没有改变，而中间三个口拔插是，寄存器都有相应的修改。如果把6xx寄存器也打出了就发现有不一样的了。

2014-9-19
1、其实改为16m所要进行的改动非常少。详细见df-16m这个分支。
2、git push origin serverfix，上传分支，git push origin :serverfix 删除服务器上的分支。

2014-9-17
1、两个phy的看来没有多少希望了。总是没有什么作用。
2、在9341上使用16m的芯片，芯片型号是mx25l2835f@sop8，必须改型号才可以烧录，否则使用原来那个8m的，擦除就过不去。
3、16m的flash直接烧录呢，似乎会导致校准区读取错误。无线启动不正确。

2014-9-16
1、今天来测试使用正式环境的正常拨号测试，测试间隔为60秒，早上9:00，可用内存为33.7m。下午3点停止测试。
2、如果只有phy27来编译，那么是可以ping通的，说明硬件上应该是没有问题的。

2014-9-15
1、今天来测试“使用自建l2tp server， xl2tpd配置同测试2，在pc端使用测试软件按照错误的用户名密码进行不断拨号。”，上午9:00开始，剩余33.9m，pc上的不停的拨号程序有时候有问题，下午2点的时候就变成不断拨号，但没有拨号的行为了。改为20秒拨号一次。下午3点的时候又出现，改为60秒一次，貌似正常了。第二天早上停止后，剩余内存34.2m。
2、在以太网卡的驱动修改Makefile.inc，当选择8035时，把s27phy也加入，设置ATH_GMAC_GE1_IS_CONNECTED=1，那么可以编译过去，设置不同的mii那么结果是这样的：
ATH_GMAC0_MII=1
ATH_GMAC1_RGMII=1	有eth0,eth1但是貌似都不通
ATH_GMAC0_RGMII=1
ATH_GMAC1_MII=1	有eth0,eth1但是貌似都不通
ATH_GMAC0_MII=1
ATH_GMAC1_MII=1	有eth0,eth1但是貌似都不通
ATH_GMAC0_RGMII=1
ATH_GMAC1_RGMII=1	有eth0,eth1但是貌似都不通
ATH_GMAC0_RGMII=1
ATH_GMAC1_GMII=1	有eth0,eth1但是貌似都不通
3、使用operwrt的内核，可以检测到线的拔出，但无法ping通。

2014-9-14
1、开始用pc端pppoe来拨号吧。10:11 剩余33.9m, 到第二天早上还要34.2m

2014-9-12
1、开始无l2tp server的情况进行测试。10:00剩余内存34.7m，第二天早上还有34.5，但是xl2tpd的statm中的占用内存有所增加

2014-9-11
1、继续测试可以拨通，xl2tpd单独拨号的情况，9:30剩余内存34m
2、列一个需要测试的表格吧
测试用例	测试结果	测试时间
1、在用户名密码错误的情况下，重复使用echo “c anhui test test” > /var/run/xl2tpd/l2tp-control 进行拨号	Xl2tpd 在处理pipe时会有没有关闭的情况，关闭pipe后，测试18小时，可用内存从22.7m到22.2m	开始2014-9-4 14:00
结束2014-9-5 8:30
2、使用自建l2tp sever，xl2tpd配置连接到自建server，使用echo “c test test test” > /var/run/xl2tpd/l2tp-control正常拨号	测试了23个小时，可用内存从开始的34m，到结束是还有34m	开始 2014-9-11 9:30
结束 2014-9-12 10:00
3、关闭自建l2tp server xl2tpd配置同测试2，同样拨号。	测试了23小时，可以内存从开始的34.7到结束的34.5
但是xl2tpd的statm中的占用内存有所增加，速度非常慢。	2014-9-12 10:00 ~2014-9-13 9:20
4、关闭自建l2tp server xl2tpd配置同测试2，在pc端使用测试软件进行不断拨号。
5、使用自建l2tp server， xl2tpd配置同测试2，在pc端使用测试软件按照错误的用户名密码进行不断拨号。	开始剩余33.9m, 到第二天早上还要34.2m
但是xl2tpd的statm中的占用内存有所增加，速度非常慢。	2014-9-15 9:00 ~ 2014-9-16 8:30
6、使用自建l2tp server， xl2tpd配置同测试2，在pc端使用测试软件按照可用的用户名密码进行不断拨号。	开始剩余33.9m, 到第二天早上还要34.2m	2014-9-14 10:11 ~2014-9-15 8:45
7、使用安徽的l2tp server，在pc端��用测试软件按照可用的用户名密码进行不断拨号。
8、使用安徽的l2tp server，在pc端使用测试软件按照可用的用户名密码进行不断拨号，同时不断ping到www.163.com


2014-9-5
1、那么今天来建立一个lns，再用xl2tpd进行测试，这样每次都能拨通，这样不停的测试看看会不会有问题。
2、openwrt的最新编译器在staging_dir/toolchain-mips_34kc_gcc-4.8-linaro_uClibc-0.9.33.2/bin

2014-9-4
1、移植了lsof也看不出什么来啊。
2、现在11:10重新测试xl2tpd程序本身，使用4秒不断拨号，密码错误。当前可用内存23m
下午2:00，还有22.7啊，应该是没有问题，这个测试还一直是没有增加内核支持的啊。重新测试吧。2:07开始，还有22.7m，到第二天早上还有22.2m，应该说xl2tpd本身在拨号不通的情况下是没有问题的了。
3、使用3.2.12的内核有奇怪的问题，如果去掉5.8g的卡，那么内核就无法启动了。这里面的机关还真的很多。

2014-9-3
2、从/proc/$pid/fd目录中可以看到当前程序使用的文件描述符，从/proc/$pid/statm中可以看到当前程序的内存使用情况。现在重新开始测试：16:05 剩余内存35m，跑到第二天早上9点，只有23m了，但是xl2tpd的statm并没有增加多少，而pppoe-server就根本没有增加。两个程序的fd也没有增加。

2014-9-2
1、即使是使用xl2tpd自己拨号，那么也会在pipe这个函数这里挂掉，先看看errno吧。
2、Openwrt终于在9344的板子上跑了起来，openwrt的设置和atheros提供的sdk中就完全不一样了。主要是需要在uboot中提供machtype=DB120 mtdparts=spi0.0:... 完整的如下：
set bootargs machtype=DB120 console=ttyS0,115200 root=31:02 init=/sbin/init rootfstype=jffs2 mtdparts=spi0.0:256k(u-boot),64k(u-boot-env),6336k(rootfs),1408k(uImage),64k(mib0),64k(ART)
3、但是openwrt的uboot还是不能运行的，是不是还有进行一些设置？

2014-9-1
1、现在来这样测试，仅使用xl2tpd进行拨号，9:16还剩36m，下午的时候报错： Unable to create password pipe for pppd。Killall xl2tpd后，内存恢复。再次运行不久又报错recvfrom returned error。如果只跑xl2tpd不断拨号，那么kill xl2tpd，内存能够恢复。
2、当前的openwrt中athros系列的内核在
build_dir/target-mips_34kc_uClibc-0.9.33.2/linux-ar71xx_generic/linux-3.10.49
目录中。原来的在
build_dir/linux-ar71xx_generic/linux-3.2.12 目录中。

2014-8-30
1、今天来测试nat的情况，9:30剩余35m，12:50还有29m了。开始只ping不拨了看看。到6点还有28.5m。开始只有pppoe的测试，18:52 还有35m。

2014-8-29
1、1分钟拨断一次，不断拨号测试跑了一天，还有19m可用内存，到底是什么占有了内存？下午2点改用10s拨断一次。下午3点，只有14m了，改为6秒一次。那么应该就和tunnel的是否释放没有关系了，因为tunnel一直都没有释放。下午4点，只有7m啦。
2、修改使得内核pppoe中不直接进行l2tp的转发，由pppoe-server转发。下午4点9m。下午5:42还有8m，那么，重启试试吧。
下午6点，36m，第二天早上9点，还有20m。和昨天差不多嘛。
3、在ap板上跑dropbear，原来/usr/sbin里面有个2014.64版本的dropbear，结果总是登陆不了。
4、减少dropbear体积：480964，

INETD_MODE	480904
ENABLE_X11FWD	480469
ENABLE_CLI_AGENTFWD	475876
ENABLE_CLI_AGENTFWD	471270
ENABLE_CLI_PROXYCMD	471207
ENABLE_CLI_NETCAT	470933
ENABLE_USER_ALGO_LIST	466568
DROPBEAR_AES256	466488
DROPBEAR_TWOFISH256	466404
DROPBEAR_TWOFISH128	461292
DROPBEAR_MD5_HMAC	457090
DROPBEAR_ECDSA	451685
DROPBEAR_CURVE25519	451390
DROPBEAR_ECDH	405900
DO_MOTD	403900
看起来并没有小很多啊，还有几个比如转发、pubkey验证、sftp等没有去掉，主要是觉得这几个功能比较实用。试试看吧：
SFTPSERVER_PATH	403756 还是可以进行scp操作的
ENABLE_CLI_LOCALTCPFWD
ENABLE_CLI_REMOTETCPFWD
ENABLE_SVR_LOCALTCPFWD
ENABLE_SVR_REMOTETCPFWD	396719
DROPBEAR_ENABLE_CTR_MODE	394341
总体来说，通过选项减少的体积不多。那么来configure的时候选项呢，option.h是原始的：
--disable-zlib	409759
 --disable-openpty --disable-syslog --disable-lastlog --disable-utmp --disable-utmpx --disable-wtmp --disable-wtmpx --disable-loginfunc --disable-pututline --disable-pututxline	404842
运行不正常，没有pty，登陆后客户端停掉。


2014-8-28
1、使用dropbear以前的版本是可以正常运行的。0.49可以，0.50可以，0.51可以，0.51可以，0.52可以，0.53可以，2011.54可以。2014.65也可以嘛，为什么2014.64不行？好像确实不可以，奇怪的问题。悲催。改为2014.65吧。
2、内核2.6.31是2009年9月9日的。

2014-8-21
1、pc通过无线连上p10，也可以正常的进行pppoe拨号并得到安徽移动的地址。

2014-8-7
1、struct iphdr这个结构看来正好不需要考虑对齐的问题。

2014-8-6
1、把一个程序里面的socket值搞出来，另外一个程序来使用，发送返回-1。

2014-8-5
1、代小龙那里说单ap升级到10a的程序后，可以拨号了，但是上不了网，后来就没有来电话了。
2、使用其他端口向安徽的l2tp发送udp消息，也同样可以通过的，应该不会判断发送端的端口号。

2014-8-4
1、贵州陈军说有些cpe必须绑定mac才能使用，而有些必须不绑定才能使用。
2、贵州程兴超折腾一个单ap，发现改变信道信号就很差了，原因是单ap产品还有滤波器存在。

2014-8-1
1、代小龙那里的单ap，设置了vlan后就不能访问220了，奇怪的现象。当设置vlan后，即使设置的地址是192.168.0.54，在pc上设置管理vlan后，还是可以通过192.168.0.54这个地址来访问到单ap的。
2、江西李刚那里有一个站，总是出现华为设备检测到回环，将我们的设备断开的现象，他发现这个站出现一个mac有回环的情况，并且已经加入了黑名单。
3、贵州程兴超要求在单ap上设置最大用户个数。

2014-7-29
1、河北的cpe测试，使用迅雷软件下载50多兆的文件，开始5秒总是比较慢。

2014-7-24
1、当程序在死循环的时候，是不能接受kill发来的消息的。
2、至少要测试这样的表格：

序号	测试操作	预期结果	结果
1	Pc 端使用错误的用户名密码拨号	不能拨通
2	Pc 端使用正确的用户名密码拨号	可以拨通
3	Pc 断线	L2tp也断线
4	Pc 端使用正确的用户名密码拨号	可以拨通
5	Kill l2tp的那个pppd	Pc 端断线


2014-7-19
1、使用passwordfd.so就可以向pppd传递用户名密码参数了。
2、使用如下方式可以在有多个出口的情况下让不同的机器走不同的出口：
内核要增加
[*] Networking support  --->
      Networking options  --->
[*]   IP: advanced router
[*]   IP: policy routing
 ip rule add from 192.168.0.93 table hp
 ip rule add from 192.168.0.22 table cpe
 ip route add 192.168.0.93/32 dev br0 src 192.168.0.1 table hp
 ip route add 192.168.0.22/32 dev br0 src 192.168.0.1 table cpe
 ip route add default via 120.193.74.108 dev ppp0 table hp
 ip route add default via 120.193.74.93 dev ppp1 table cpe
 ip route flush cache
 iptables -t nat -F
 iptables -t nat -A POSTROUTING -o ppp1 -j MASQUERADE
 iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE


2014-7-18
1、在xl2tpd.conf文件中增加多个lac段，就可以发起多个session。
2、下面的工作应该是这样，先在cpe上增加一个pppoe server，然后可以通过其他方式上网。然后修改pppoe server的代码，收到需要验证的时候，把用户名密码提取出来，提供给xl2tp，让它建立一个session， 如果建立成功，那么返回给pc用户验证成功并且也建立一个对应的设备，并使用nat方式连接两个设备。
3、有个地方的网管已经和单ap联通了。
4、现在编译ncurses-5.8确实编译不了了，奇怪啊，以前应该是可以编译的。如果使用cpe-8m
的编译器就可以编译。
5、http://wenku.baidu.com/view/11ae1bdcad51f01dc281f1c8.html xp配置pppoe server的文档，但我也不记得是怎样装上pppoe 的协议的了。

2014-7-17
1、终于在p10上调出来了xl2tpd，原因是pppd的某个代码在gethostname时时间太长，导致pppd没有进入处理过程，而对端连续发送了多次协商包后发出了短线的请求，xl2tpd就kill的pppd，所以就无法上线了。
2、使用usb0拨通后，mtu可以设置为1467，而前天测试的以太网从记录看只能设置到1372，这其中还有什么区别么？
3、oute add -host 120.210.236.221 gw 10.203.22.181 增加对某个ip的路由。

2014-7-16
1、要在现有p10上增加ppp 内核支持 增加xl2tpd， pppd 增加拨号脚本，拨号后手工设置nat，如果pc可以上网，则最简单的任务完成。
2、在cpe-df上拨号成功，但在p10上不成功，估计是ppp的支持增加的不够，先全加上再说吧。加上了好像也没有什么用啊。
3、 ./tcpdump   -i  eth0  -s  0  -w  ./tmp/pcap 可以抓包给wireshark使用。

2014-7-15
1、在sccrq中增加 PPPoE Service Relay Forward Capability AVP 和PPPoE Service Relay Response Capability AVP 这两个avp，安徽华为的服务没有相应的回应。
2、在cpe上建立一个pppoe的server，参考
http://www.howtodoityourself.org/pppoe-server-how-to-do-it-yourself.html
但由于我的机器上本来就有一个pppoe的server，所以又去找一个http://www.raspppoe.com/, 结果还是不行。
3、拿到了安徽的用户名和密码，使用windows的华为客户端和linux下的x2ltpd均拨号成功。在windows下ping www.163.com -f -l 1372 可以ping到，再大就不行了，报需要分包，而在linux下的ppp显示的mtu 是1492，但是ping 对端地址-s 1435就不能ping通了，把ppp0的mtu改为1372，1530也能ping通了，但1540的包还是不能ping到，我猜可能是对端地址不支持这样的大包来ping。


2014-7-14
1、在5.8g的cpe上测试一下信道设置是否正确
信道号	频率	比特率	重启后
153	5.765	144	ok
161	5.805	144	ok
165	5.825	144	ok
如果是单5.8g的cpe，那么永远都是使用20m的频率了，这是否合理呢？

2、安装了颜斌买的抓包网卡，居然是个pcie的，往pci上装就装不上。这个网卡确实可以抓包的。但是这个网卡看起来不能使用wireshark来抓包，会报不能进入杂散模式的错误。

3、在SCCRQ的请求包中就包含了一个Assigned Tunnel Id，看来是1，而服务器的回应中，就带上了这个id，而且也有一个Assigned Tunnel Id，这个值就大一些，应该是这样，因为服务器处理的tunnel多一些，然后客户端每次发包，带上服务器指定的tunnel id，而服务器发包，则带客户端指定的id。居然这样来指定id，貌似其他协议中非常少见。

4、在icrq请求中，指定了session id这个字段为1。物理通道号为0，设置的呼叫序列号是1，没有设置呼叫的号码，而对端的号码是8888，看来老外对8888也有特殊的偏好？这个8888似乎没有从其他包中出现。服务端在icrp中则指定了session id 为一个较大的值。客户端回应的iccn包中，tx和rx connect speed的值都是0， 私有组id为全0。这样一个session就建立完成了，以下的过程是ppp的过程了。

5、Cpe切换ssid后，应该删除以下文件：
/tmp/.rssi
/tmp/cpe_speed_mode
/tmp/.inlimit
/tmp/.outlimit

2014-7-12
#cat xl2tpd.conf
[lac testvpn]
lns = 120.210.236.221
pppoptfile = /etc/ppp/peers/test.l2tpd
hostname = ltekd
challenge = yes
require authentication = yes
name = xingyong

#cat l2tp-secrets
* * Amcc@123


2014-7-11
1、颜斌在北京测试，貌似是有的ap没有带wds功能，找了很久没有找到。
2、湖南叶巍处理一个站，以前使用正常，现在一个ap显示在线，但是为黑色，网络也显示为1g/full，但它上面的cpe不能拨号，不能ping到220。换ap板后，三个ap都可以拨号，但上网速度很慢。
3、谢文忠拿来的景德镇的三个cpe都是出现地址信息为00:000的情况。这真是个幽灵啊。
4、李刚说单ap不能访问管理vlan，应该是把ip设置成192.168.1.220的缘故。
5、安徽的l2tp使用华为的软件终于看到了第四步，还是华为的余敏发来了截图，发现是l2tp隧道名称应该是小写。

2014-7-10
1、刘谦那里在一个wds上发现有多个cpe的地址等信息出现多个00：000这样的信息，只好通过集中网管改掉它们。

2014-7-1
1、使用pppoe-3.8 + pppd 2.4.5可以拨通windows自带的pppoe server。原来是什么不可以呢？拨linux也是可以的。难道是2.4.4就不行？

2014-6-27
1、保定的测试基本结果和公司的测试差不多，ftp为6-7m，有能看到8m的时候。具体配置情况：cpe rts 256， ap固定速率，rts 1024, beacon_nob 1。

2014-6-24
1、ap-si清除了ap2的文件后，还有1.7m空间。

2014-6-23
1、ap-c5和网管相连测试，一个cpe连接，使用cped_fakepc不断做ftp下载，从周六下午跑到周一早8点，看起来一切正常。
2、Ap-c5使用中文ssid时，网管上直接是正确的中文。
3、把李柱栋文件中的cacert.pem这个文件读出来，写入一个字符串，使用x509_crt_parse这个都进去，就不会报自签的警告了。
4、邦讯的cpe的ip是192.168.1.1。Telnet为开放状态。有2个作为客户端的ssid，比较有意思。网页的速度其慢。对系统做了较大的改动，apdown和apup都不见了。网页使用登陆方式和tplink的一样。
5、单ap中的mcs改为7654，而5.8g改为13
6、生产反映单ap程序165信道时，启动是速度特别差，点击“无线配置”保存后变好，但需要每次重启都要点一次。没有理由，设置工作在每次启动后都会重做一次。从串口来看，程序确实启动的时候设置了一次，但是报错了，如果再点一下呢，就可以了。更换了参数设置中的次序后，就可以了。出ap-si程序7a。
7、Atheros sdk v10.1加入原来的系统，需要复制两个无线驱动的目录，复制一个sdk中的scripts，稍加修改就可以编译，而且运行貌似正常。还缺一个spec...的没有编译。

2014-6-21
1、ap_frequency要送“20m”而不是0？确实如此。ok
2、WireRecvNotSinglePackets这个值为什么是负值？

2013-10-29
1、这样的代码变得没有输出
		int *p;
		p = (int *)0x1900009c;
		printf("all rec byte: %p \n", p);
		printf("all rec byte: %d \n", *p);
而：printf(“%d \n”,  *(int *)0x1900009c) 程序就直接退出了。


2013-10-28
#!/bin/sh
mac=1
while [ 1 ]; do
        if [ $mac -le 10 ]; then
        echo 00:03:7f:30:00:0$mac > /proc/vap/ath0/deny
        echo 00:03:7f:30:00:0$mac > /proc/vap/ath1/deny
        else
        echo 00:03:7f:30:00:$mac > /proc/vap/ath0/deny
        echo 00:03:7f:30:00:$mac > /proc/vap/ath1/deny
        fi
        echo 00:03:7f:30:00:$mac
        mac=$((mac+1))
        if [ $mac -ge 101 ]; then
                exit;
        fi
done


2013-9-23
1、mcu程序在设置trunk时没有把ssid传下来，必须重启生效后才有效，不合理。

2013-9-18
1、cpe在没有搜索到网络的情况下，一直处于杂散模式。而搜索到之后，就一直不是杂散模式。

2013-9-17
1、[<87349764>] ar9300Set11nRateScenario+0x38c/0x84c [ath_hal]
[<87099814>] ath_buf_set_rate+0x404/0x6dc [ath_dev]
2、当ds为void *类型的指针时，强制转换必须写成这样的样子
flag = ((struct ar9300_txc *)ds)->ds_ctl11;
也就是必须再括号一次，否则编译就报错了。

2013-9-16
1、内核中可以简单的使用WARN_ON(1)显示调用堆栈。

2013-8-30
1、insmod umac 出现的是这些信息
ath_ahb: 9.2.0_U11.14 (Atheros/multi-bss)  //在os/linux/src/if_ath_ahb.c中
__ath_attach: Set global_scn[0]           //在 os/linux/src/ath_linux.c中
ACBKMinfree = 48
ACBEMinfree = 32
ACVIMinfree = 16
ACVOMinfree = 0
CABMinfree = 48
UAPSDMinfree = 0
Wasp Enterprise mode: 0x00000000
Restoring Cal data from Flash
Using Cal data from Flash 0xbfff0000
dfs_attach: use DFS enhancements
DFS min filter rssiThresh = 18
DFS max pulse dur = 151 ticks
ath_get_caps[5184] rx chainmask mismatch actual 1 sc_chainmak 0
ath_get_caps[5159] tx chainmask mismatch actual 1 sc_chainmak 0
SC Callback Registration for wifi0
wifi0: Atheros 9340: mem=0xb8100000, irq=2
ath_pci: 9.2.0_U11.14 (Atheros/multi-bss)

2013-9-3
1、echo 11111 > /proc/var/00037fd5038c ，里面取到的数据居然是0x31313131310a， 不明白这个0x0a从哪里来的。

2013-9-2
1、一直改错了文件，所以永远有奇怪的问题，郁闷啊。

2013-8-29
1、打流短包不行是要设置AMSDU为0， 9331没有这个功能，所以效果不错。
2、如果git上有多个功能性的分支，有时候要出测试版本又要组合这些功能，那么就要使用rebase这样的功能，如果随意rebase可能会有奇怪的效果，那么保险的做法是把各功能性分支先rebase到master，然后选择一个分支作为基地，另外的分支呢，要建一个分支的分支，再rebase到基地分支去，编译完成后，可以删掉分支的分支。这样就能保持功能性分支不受影响，可以继续开发。

2013-8-28
1、static const iw_handler ieee80211_priv_handlers[] = {这个数组最多只能有32个值，这是由SIOCWFIRSTPRIV这个宏的位置决定的，在内核的处理中，int dev_ioctl(struct net *net, unsigned int cmd, void __user *arg)这个函数将会限制，限制的原因在这里：内核代码include/linux/wireless.h 有如下说明：
#define SIOCIWFIRSTPRIV	0x8BE0
#define SIOCIWLASTPRIV	0x8BFF
/* Previously, we were using SIOCDEVPRIVATE, but we now have our
 * separate range because of collisions with other tools such as
 * 'mii-tool'.
 * We now have 32 commands, so a bit more space ;-).
 * Also, all 'even' commands are only usable by root and don't return the
 * content of ifr/iwr to user (but you are not obliged to use the set/get
 * convention, just use every other two command). More details in iwpriv.c.
 * And I repeat : you are not forced to use them with iwpriv, but you
 * must be compliant with it.

2013-8-27
1、ieee80211_beacon_init这个函数似乎会每30秒调用一次。
2、如果修改了主目录的权限，那么putty的自动登陆就不能用了，还好在/var/log/secure这个文件中有这样的描述：Authentication refused: bad ownership or modes for directory /home/jian

2013-8-26
1、使用nomachine的客户端连接centos，说明：http://wiki.centos.org/zh/HowTos/FreeNX
2、在77这台机器上，一直是iptables编译不了，修改其Makeifle,，注释掉#am__append_3 = utils就可以了，也不知道从autogen.sh如何产生这句话的。
3、find /var/log/ -mtime -3 找出3天内修改的文件
4、sudo mkdir /media/cdimage  ＃建立一个文件夹作为ISO挂载点
   sudo mount -o loop myfile.iso /media/cdimage   ＃挂载ISO文件，使用参数 -o loop
5、编译wine需要gnome-desktop-devel这个东东，也要下载20m的东西。
6、yum install wqy-zenhei-fonts.noarch 这样centos网页上就可以显示中文了。

2013-8-23
1、gitk . 就可以在图形界面上查看当前目录的log了。
2、昨天的问题在于做ioctl的时候传入的buff比驱动认为的要小，所以产生了内存不正常的覆盖，这样任何奇怪的问题都不奇怪了。

2013-8-22
1、发现奇怪的现象，ap程序收到第二次心跳包时，取参数就取到空值了，就重启啦。

2013-8-21
1、我机器上的centos的tftp server有问题，从cpe上下载，有些文件可以，有些文件就报Permissiion denied。奇怪的事情。把这个文件复制到windows上的tftpd目录，就可以下载了。
2、笔记本上的minicom有些奇怪，如果使用鼠标双击会发送一个0x03下去。

2013-8-20
1、有时候cpe和mcu之间没有联系上，这样cpe的信息就会出现在mcu网页的其他cpe的那个列表中。
2、几种cpe之间的flahs划分都是不一样的，这样还是不太好啊。

2013-8-19
1、即使在最新的内核代码中，br_fdb_update这个函数貌似也没有修改过，对于“这个告警”，也没有额外的处理。

2013-8-18
1、在网桥的代码中，如果在br_fdb_update中出现“own address as source address”的提示的地方把这个包丢弃，貌似没有什么作用。如果这个时候把这个if的状态设置为block，那么有奇怪的现象在于，如果启动的时候，eth1所接的口存在环接现象，那么看起来就正常起了作用，如果运行时去环接，那么就很快重启了。

2013-8-16
1、使用apup是可以产生多个ssid的，主要要修改这些参数：MAX_VAPS_PER_RADIO，这个值默认没有，要增加。AP_RADIO_ID_2，这个值原来是1，要改为0。再把AP_STARTMODE=multi，这样就出现了2个ssid，而第二个ssid占用的是5g的那个，所以这个脚本还需要修改一些地方。
2、关于brctl的stp功能，stp是要发送stp的管理包来进行判断的。如果一个网桥的两个网络接口被串接，那么stp功能是有效果的，如果一个网桥的某个网络接口下存在环接的情况，那么这个网桥的stp功能貌似是无能为力的。
3、公司测试中再次发现有ap重启后断线的情况，这时候，ap上的phy灯不亮。ap重启，mcu重启都没有作用，这样ap硬件reset一下才能用。

2013-8-15
1、写16m的flash那个文件拼接器还有问题，它的buff只开到9m，而再开大，运行的时候直接报段错误。只有动态开辟了。其实也可以考虑设置为全局变量可能也可以，局部变量应该没有那么大。
2、接入其他厂家cpe导致ap挂掉的，考虑使用cwm的功能来完成，每一个小时固定做一次的功能不知道什么时候已经去掉了，而mcu网页上也不能设置0个活跃数量，这样只有设置为1个，并且设置80%的掉落开启，不知道有没有效果啊。如果当前ap一个我们的cpe都没有，那么这个功能就很难启动了。
3、张现那里测试cmcc，发现计算机得到的ip是192.168.0.20，这是比较奇怪的事情，如果那个开始地址没有设置，就会变成这样。要改。
4、5.8g的ap启动apup1根本没有判断加密的东东，所以无论怎么设置参数都是无效的。都是未加密模式。
5、四川那边有些机器从网管的机器上不能打开mcu的网页，非常奇怪的现象。Telnet可以进去，但很多指令执行后不动了。后来发现ping1500的包过不了，应该是移动网络有个设备卡住了大一点的包，导致这样的问题。

2013-8-14
1、打印64位的值应该使用%lld，否则就不对，不对。
2、使用16m的flash看起来没有问题，但是设置到32m后，内核就在parse_cmdline_partitions这个函数中报错了，打印除master->size这个变量，发现只有8m了。看来还是要到初始化的函数中去跟踪一下。
3、在u-boot中#define ar7240_spi_send_addr(__a) 这个宏只写了24位地址，当然只能用16m了。不过修改了这里，uboot写了内核后报的是magic word错误，应该还是写错了地方。既然朱建文都说只支持16m，那就不要管这个问题了。
4、那个cpe再次发生没有分时控制的情况。这一次ps可以出现，没有停止响应，dmesg也没有发现报错的日志。看log也没有发现分时包。杀死cped后再运行，貌似正常了，但很快重启了，这个重启比较奇怪。只能猜测说也许是系统正在重启吧。
5、上传文件md5错误的问题，袁考伟做了个程序，在/tmp下生成一个4m的问题，算md5，和预先值进行比较，没有发现有错误的情况，但运行了2次，一次运行了1000多次，一次运行了100多次，最后都重启了。拆掉外壳，插上串口，再次测试了23080次，有2次错误，也没有重启。

2013-8-13
1、碰到一台奇怪的cpe，它的速度比其他cpe快，看它的分时控制是关闭的。Cpu占有率特别高，达到了7，ps后无响应，但又可以再次telnet进去，cat /proc/11??后，同样停止响应。打开日志，发现仍然收到心跳包，但没有分时包。Dmesg发现有错误发生。推测是这样的，错误发生后，系统试图重启，杀死了接收分时包的线程，但停了下来，重启没有完成。

2013-8-12
1、ap板增加5.8g双流后，发现总速度无法超过19m，而且会出现死掉的情况。死掉的情况下，如果不运行apd，是可以继续运行的。说明是apd没有能够得到运行时间而没有喂狗而造成的重启。
   去掉ebtables的支持mod，速度没有改善，但cpu占有率有所下降。
   如果修改apd程序，使得cpu占用率减少，那么貌似也可以达到不死的目的，但是速度总是上不去的。
   使用中兴的ap，可以轻松达到30m。
   使用demo板，可以达到35m。
   把demo板上的flash搞下来，放在自己的板子上，更换了gmac驱动后，速度也可以达到35m
   更换内核到原来的ap程序，也就是没有增加netfilter支持时，速度也上去了。同时单个cpe的单个下载线程的速度也从3m多提升到9m。

2013-8-6
1、如果把5.8g的cpe的内核改为不支持netfilter的内核，看不到特别的改善。

2013-8-5
1、内核和无线驱动之间不配合会导致无法连系。

2013-7-30
多次统计效益和的脚本。
IP=$1
FILE=$2
MD5=$3
ok_sum=0
fail_sum=0
while [ 1 ]; do
        tftp -g ${IP} -l ${FILE}
        MYMD5=$(md5sum ${FILE} | awk '{print $1}')
        if [ "$MD5" = "$MYMD5" ]; then
                echo ok
        ok_sum=$((ok_sum+1))
        else
                echo fail
                fail_sum=$((fail_sum+1))
        fi
        echo $ok_sum $fail_sum
done

2013-7-23
1、在vi中使用:set fo-=r 来去掉自动注释
2、Git增加仓：在249上：
   #su -git
   #cd /respisitortes
   #mkidr XXX.git
   #cd XXX.git
   #git init --bare
   然后在修改权限仓。

2013-6-20
1、busybox1.21中的brctl没有show macs功能了。

2013-6-13
1、在cpe上进行pppoe后，如果keillall pppd那么会导致cpe重启，奇怪的问题。这个kill会把所有的进程都kill掉。而killall pppoe则没有问题。

2013-4-7
1、统计iwconfig中-96次数的脚本
count=0
while true
do
echo checking...
isup=$(iwconfig ath0 | grep "Signal level=-96" | cut -c11-15)
echo $isup
if [ -z $isup ] ; then
        echo ok
else
        count=$((count+1))
fi
echo $count
sleep 1
done

2013-2-27
1、cpe-df的nat方式貌似是正确的。没有加dnsmsq这个东东。

2013-2-19
1、iwpriv wifi0 6MBAck，似乎没有对0想8108004这个寄存器进行操作，而且这个get指令居然是get5mback，神奇。如果把ath0 down up一下，寄存器的值才进行了修改。
2、如果直接修改寄存器的值，那么iwpriv得到的值就是错的，这样就无法确定到底是哪个值在起作用。

2013-1-30
1、如果在ftp软件限速400k，那么会变成355k
2、如果只有10个cpe时，下载速度很稳定，但30个cpe连接时，10个cpe下载速度也不稳定。
3、30个cpe同时下载，如果不采取措施，速度只有1m多。而采取措施，那么有降到0的情况。

2013-1-20
1、iptables -A INPUT -j DROP 有效
   iptables -A FORWARD -j DROP 无效
   ebtables -A FORWARD -j DROP 有效
2、如果ath0和eth1的两个地址在同一个网段，那么就ping不通啦。

2013-1-15
1、六塔这个站这几天反应非常慢，修改配置50k->20k空闲带宽，60s->45s,处理间隙 8->7处理个数后，测速能到达300k，而之前只要不到100k，这也是非常奇怪的事情。
2、双流的cpe改为16m就只有很少的内存，去掉pktlog这个ko，可用内存也只有1.8m。而9331的能有5-6m。

2013-1-14
1、在makefile中，变量似乎不能放在执行语句中，只能在全局定义处，否则无效，奇怪啊。
2、Sed要修改文件，使用了-i参数就不能使用>file的方式，这样写到另外一个文件可以，而写到源文件，源文件就会变空。

2013-1-7
1、人为制造环路之后，只要ping 一个不存在的ip，那么就会产生广播风暴，ap的灯狂闪，在ap上打开网桥的stp功能后，brctl stp br0 on 后，广播风暴消失。
2、当广播风暴发生时，那个抑制广播风暴的寄存器似乎没有起到多少作用。

2012-12-24
1、grep -c应该是统计个数的功能。
2、可以使用/etc/ath/killVAP  ath0来停止ath

2012-12-22
1、cpe-5g似乎不需要修改0x30这个swith的寄存器，也可以ping到1000的包。即使把这个值改到0x1bf005ee，也没有任何意义，同样到3000也ping不通。

2012-12-18
1、奇怪的问题，gpio16无法控制，而gpio14则没有问题。12也可以控制。

2012-12-17
1、增加pppoe的选项似乎不会改变gmac.ko

2012-12-10
1、在工厂测试，使用某个cpe可在1.3公里处使用，而另一个则不能，更换了不行的rcS, rc.changessid等文件，都不行。Ap端使用19a, 19c都是一样的。而在600m处，都可以正常下载。

2012-12-7
1、当ap上使用了买来的小天线后，ap版的表现就不怎么正常了。
2、即使cpe设置为4094的vlan，pc不能访问到mcu。

2012-12-3
1、如果内核中的网络参数变化，那么gmac这个驱动就会变化，如果两者不对应，那么系统就报错并停止响应了。

2012-11-29
1、如果字符串为NULL， 那么strcmp是有问题的。

2012-11-28
1、可以用-mlimit --limit-burst实现限制突发数。
2、如果mcu传来的ssid中存在空格，而记录时空格会被删掉，就会产生ap不停复位的情况。

2012-11-21
1、ebtables -A FORWARD -i ath0 -o ath1 -j DROP
ebtables -A FORWARD -i ath1 -o ath0 -j DROP
这两句能够阻隔ath0和ath0之间的包。

2012-11-20
1、iwpriv wifi1 getCountry得道国家代码，不知道这个国家代码和ath0 的countrycode有什么区别。

2012-11-19
1、有两块ap板的校准区都被擦除，奇怪的事情。

2012-11-16
1、busybox 中的ping -s参数必须在ip之前，否则无效。

2012-11-13
1、5g，如果把aus设置为20m，那么cpe显示的就是72.2m，下载速度3m多些。如果aus设置为20/40，cpe显示就是150m，下载速度可以到10。

2012-11-3
1、如果关闭双庙的半分钟cwmenable 0，改为3分钟，很快就出现不能ping通的情况。

2012-10-31
1、去掉了双庙的400k空闲选项，因为掉线严重。
2、挂墙终端，使用自己的模块，使用option.ko来加载模块，正常加载，貌似正常拨号，但不能连到服务器，使用modprobe加载，则正常。奇怪的问题。
3、挂墙终端，在一个有系统的板上，再次tar上文件系统，很快就没有可用空间了，重启后，可用空间恢复。

2012-10-11
1、如果cpe下载时，将限速值从800->20，就容易出现cpe复位的情况。从dmesg的显示来看，由于内存不足，导致某个进程开始胡乱kill，如果把cped kill掉，那么就要复位了。

2012-9-13
1、ap程序中的清除黑名单的操作，只在有客户端的情况下才会做，所以会出现没有合法用户时，黑名单愈来愈多的情况。

2012-9-7
1、编译网络驱动时要编译一下内核，否则可能会无法编译通过。
2、ap板网口设置为10m时就不能ping 出去了。

2012-9-6
1、busybox似乎没有对时程序。

2012-9-3
1、在apd中启动httpd，信息查看和客户端列表两个页面就无法打开，只有在后台运行一个脚本，由这个脚本打开httpd，就没有问题。

2012-8-31
1、当pc上有虚拟机时，命令行中brctl showmacs br0 中看不到虚拟机的ip，但上送的网管包中存在。
2、公司的机器出现mcu未收到ap的心跳包的情况，重启ap无效，vlan表正常，重启地板无效，整机断电重启，恢复。

2012-8-30
1、编译内核使用的是make BOARD_TYPE=… lzma_uimage命令。

2012-8-28
1、有一个基站的某路ap数据恢复到了athros的原始参数，但ssid似乎没有改变，没有触发我修改参数的条件，非常奇怪的现象。

2012-8-26
1、内核中ar7420居然没有对应的程序。

2012-8-20
1、搜网不能ping时，使用cwmenable指令可以立即恢复。

2012-8-18
1、如果点搜网，ping会断线，但10分钟左右会恢复。
2、在南昌抓包时发现有athors的mac

2012-8-15
1、在一个位置上，移动5m就无法ping到长包，决定更换天线角度。

2012-8-13
1、如果出现环行，网络明显不行了。

2012-8-10
1、makefile文件中在命令前加-，可以忽略命令失败。
2、wlanconfig ath0 list ap查出来的东西不全，虽然速度很快。

2012-8-8
1、jffs的文件格式有问题，下载网卡驱动ko失败后，使用串口下载整个文件系统，那个文件还是0字节，删除后重启正常了。

2012-7-24
1、ap将速度写定，似乎能解决某个cpe信号差导致的全面速度下降的问题。

2012-7-23
1、修改cpe的以太网mac，使得以太网的mac大于无线网卡的mac

2012-7-20
1、网卡的编译是enet_build
2、mcu离线应该能正常工作。

2012-7-19
1、cpe的apup是正常的，为什么ap上的apup不行呢？
2、cpe更换ap后，就通不了了，除非重启sw_main。
3、在程序中运行cfg –c容易引起参数重置。

2012-7-18
1、ap在程序中apup是有问题的，还是要去掉它。
2、9331使用的是ar7240，9344使用的是athros。
3、ap有参数重置的现象

2012-7-17
1、有些浏览器上传文件会带上目录。
2、运行了两个sw_main，把ap升级出问题了。
3、如果启动了cped后，修改了相连的ap，那么是无法向正确的地址发送mac数据的。
4、pppoe测试正常。

2012-7-16
1、cpe网桥断开再连上似乎没有什么影响，其序号是不变的。

2012-7-15
1、cpe上报的速度限制是错误的。

2012-7-14
1、192.168.1.2这个机器居然不能解析dlinkddns.com.cn的地址。
2、cpu的占有率貌似和uptime显示的是一样的。
3、cpe和ap上报的rts值应该为当前值，而不是存储值。

2012-7-13
1、如果没有收到mcu的信息，就多发几次吧。
2、某个apd程序如果自动起来，会把后来增加的参数清除，奇怪啊。
3、cpe指定升级ok

2012-7-12
1、cpeled程序中的delay没用清0，低级错误啊。
2、ap自动设置ch，自动设置mac啦。
3、设备如果自动运行apd居然有时会死掉，会死掉。
4、没用close文件时，写flash文件可能根本不操作。
5、我到电脑上delphi都不能运行啦，重启才可以，到底在做啥？

2012-7-11
1、建立base文件比较目录，完成差分包自动完成。
2、修改busybox，不再带入编译日期。在busybox.h中的BB_BANNER这个宏。
3、optbuild这个目录，在makefile中是用IMAGE_ROOT来表示的。
4、ap做升级包的时候，会有一个debug.tgz的东西每次都变化。
5、awk中本来就有length函数，如果使用脚本中的函数，是没有用的。
6、将差分文件名改为会被自动忽略的.patch。
7、apd不再自动关闭无线。
8、总共才4862行程序。

2012-7-10
1、增加在线时长和cpu占有率的上报。
2、按照要求设置mac
3、art.bin压缩情况下非常小，只有558个字节，可以考虑放进文件系统内，以防不测。

2012-7-9
1、为什么在cpe syslog中有时只有receive packed cmd=3，但没有包内容呢？
2、自动设置ch值

2012-7-6
1、使用system（tar ）出来的系统的所有者是ap71，奇怪。
2、ap cpe增加GATEWAY参数，自己用得方便一点。
3、cpe升级成功。
4、为什么所有system(tar。。。)的文件的所有者都是ap71呢？
5、需要在makefile文件中自动生成升级文件。

2012-7-5
1、内核如何增加版本呢？
2、du和df两个值是不一样的。
3、cpe发送给ap的包，在pc上也能监听到，奇怪啊。
4、mcs设置到39m以上就不通啦，有些板子又可以设置到39m。

2012-7-4
1、升级成功。
2、升级内核也没有什么问题。
3、为了方便程序，修改协议，一次下载多个升级的内容。

2012-7-3
1、update.c需要多个变量，把这些变量集中到一个结构中吧。
2、windows的网卡驱动去掉了vlanid，所以抓包的时候没有vlan 信息。Marvle Yukon这个网卡是可以通过注册表修改保留vlan信息的。
3、um这个东西在狂发arp请求包。

2012-7-2
1、把rc.led这个东东换成了程序，cpu减少了，但它依然高居榜首。
2、使用一个update.c来完成两个设备的升级吧。
3、瑞科nw336这个无线网卡是可以加入网桥的。
4、升级过程中是否应该加入额外的线程？
5、update.c如何区分是在apd中还是cped中？

2012-6-29
1、网络掉线后，升级程序似乎还在运行，并升级成功啦。
2、把top和uptime加入后，ethreg居然不好使了？
3、ap中居然没有rc.changessid，没有初始化过程。

2012-6-27
1、增加远程日志支持
2、ap增加syslog后，行为也有所变化。

2012-6-26
1、定义可变参数：
#define   LOGSTRINGS(fm,   ...)   printf(fm,__VA_ARGS__)
2、rc.led这个程序居然占用了主要的cpu
3、加入top和uptime后，ethreg这个applet居然消失了。
4、9331使用的是ar7420/gpio.c， 9344使用的是atheros/gpio.c

2012-6-25
1、cped如果长时间没有收到mcu的心跳包，那么就重新向ap发送心跳包。
2、读/version中的版本信息。

2012-6-19
1、加载光驱mount -t auto /dev/cdrom /mnt/cdrom
2、yum--disablerepo=* --enablerepo=c6-media使用光驱作为源。

2012-6-14
1、使用这个指令来修改一下vim的配色方案，默认的配色注释是蓝色的，在黑底的情况下根本看不清
 echo "colorscheme koehler" >> $HOME/.vimrc
2、又碰到一个无线无法启动的情况，下次要好好分析一下。
3、ath_bstuck_tasklet: stuck beacon; resetting (bmiss count 9)是什么意思？

2012-6-13
1、cfg中有严重的问题，cfg –a =3后，网络就无法启动啦
2、在server的文件系统中也加入version文件。
3、升级前一定要kill掉那些还在使用文件系统的程序，否则其报错会显得无穷尽。
4、使用定时器来发送cpe的心跳包。

2012-6-12
1、git status .可以快速看本目录的改变。

2012-6-8
1、如果向ti3517大量PING包，那么socket.arm.ok这个程序会占到0.3~0.7%的cpu, 0.2%的mem，但laodaverage还是3个0。
2、如果运行的是apd，那么大量ping包时在top中看不到apd。
3、昨天增加bridge显示bridge中所有的macs时，会出现一个str[0]=[] too short 的提示，为什么今天没有了。
4、可以收到李柱栋发来的包了。

2012-6-7
1、ap监听两个type时，如果使用一个全局变量socket，就不对啦。
2、使用putty时，如果在两个putty的vi中复制和粘贴，那么tab就会变成空格，而从si中向putty中的vi复制时就没有这个问题。
3、转发包为未知mac而成为时，对无线部分似乎发送的少，而在有线网络上发送的多。也许是无线网络已经被cpe狂发所占住了。
4、转发包使用有vlanid时，使用wireshark抓包时，vlan头消失了，而应该是存在的，在arm上接收上是存在vlan的。

2012-6-6
1、可以使用git-svn来下载svn仓的东西，会自动根据提交的历史来生成版本。
2、tlog.c中已经有string到mac的转换。
3、狂发包被禁止的问题，貌似如果不是发广播包就问题不大。

2012-6-5
1、如果监听是选择的是eth0，而eth0在桥内时，就监听不到包。改为监听ath0就好了。
2、set11NRates可以设置cpe的网速，这个值称为mcs。设置了这个值后，必须设置set11Nretries才能正常工作。否则一旦发包，就报连接丢失。
3、把原来做的一些东西上传了。
4、optbuild目录中的可执行文件的减少比strip还有多。

2012-6-4
1、当cpe狂发包一段时间后，就无法再发出包了，在无线监听上也没有了包的踪迹。
2、发包程序中，设置vlan后发的包是对的。
3、还有好多需要设置的参数啊。

2012-6-1
1、考虑在一个目录中写apd和cped两个程序，而网络收发包程序则ln李柱栋的文件。

2012-5-31
1、apcfg是处理默认参数的。
2、客户端和ap的进程中都看不到hostapd这样的进程，其中client端去掉hostapd也可以正常跑起来。
3、增加vlanid似乎比想象的要复制的多。
4、不同的cpe可能会有网速限制。

2012-5-30
1、设想了一个通用的发包函数，但还有结构内字节对齐的问题，所以不是很完美。

2012-5-29
1、使用李柱栋的程序，如果使用原来的broadcom的编译器编出来的程序，是无法运行的。
2、发送是正常的，但发给ap的似乎会收到两次，非常奇特的地方。

2012-5-28
1、当前程序对网络包是监听方式的，不是拦截方式的，要达到拦截的目的，似乎有些困难。
2、升级过程应该由MCU控制

2012-5-27
1、busybox的brctl中，fdb_entry中存在prot_n这个变量，记录了mac所在的端口。
2、rc.wlan只是加载了驱动。

2012-5-26
1、git可以运行git gc来减少文件的占用。
2、加入rts/cts后，性能下降了10-20%。

2012-5-25
1、昨天李柱栋所说的自定义网络类型的包不能再utag的情况出来，可能是发包程序错误。源于王伍给的原来的pppoe拨号的程序中的memcp函数多复制了一些东西出来，可能是由于内核变化后结构的大小有所变化。

2012-5-24
1、仍然会有tun0，tun1同时出现的情况。
2、git不会保留空目录，这样对有些仓会造成困扰，解决方法只有两个：在空文件夹中增加.gitignore文件，或者make时自动创建这些文件夹。
3、/proc/net/arp中有arp表，看起来也会定时删掉一些文件。
4、限速需要一种算法。
5、抓包能发现，即使没有设置rts，也会出现一些rts/cts的包，而且不仅仅是client发rts，ap发cts这么简单，ap也有可能发rts，client也有可能发cts。

2012-5-23
1、今天的测试看来限速是增加用户数的主要手段。

2012-5-22
1、无线抓包是可以抓到的。
2、busybox中带有ethreg，可以对phy的寄存器进行读写。
3、当内核中的参数和athr_gmac.ko编译时参数不一致时，加载athr_gmac.ko会挂掉。

2012-5-21
1、如果在update系统的时候rc.led还在运行，那么会不断显示jff2的错误信息

2012-5-18
1、增加了对cpe上面的led控制。
2、cpe内核增加64k空间

2012-5-17
1、在cpe中使用(sleep 60 && apup) &实现无线的延时启动会有问题，原因未知。只有直接执行apup才可以。
2、在驱动中，使用printk只能向错误控制台写，而如果是telnet等登录的控制台，就必须使用read中的pages等参数。

2012-5-16
1、cpe换为8m的flash,并增加iptables等编译，sdk中的iptables-1.4.5和1.4.5-qos都编译不了，而最新iptables-1.4.13可以编译。

2012-5-14
1、在apup里面增加对rts的控制。

2012-5-12
1、脚本中增加有线网络的速度控制。

2012-5-11
1、增加文件/proc/phys26/inlimit & outlimit，实现对cpe有线网络的速度控制。

2012-5-10
1、cpe增加文件区的空间，压缩u-boot，去掉u-boot-env区，减少kernel区。
2、去掉cpe的内核fat支持。
3、去掉cpe的内核usb支持。
4、增加cpe的txpower支持。

2012-5-9
1、cpe的jffs2文件系统删除一些不需要的文件。

2012-5-8
1、cpe支持jffs2文件系统了，原因在于u-boot中使用命令行设置参数时，这样写setenv bootargs=console=ttyS0,115200 root=31:02 rootfstype=squashfs init=/sbin/init mtdparts=ar7240-nor0:256k(u-boot),64k(u-boot-env),2752k(rootfs),896k(uImage),64k(NVRAM),64k(ART)是不行的，bootargs后面的=是不要的。教训惨痛啊。
2、增加/proc/phys26/reg文件对s26 phy的寄存器进行控制。

2012-5-4
1、mac程序对eth0, eth1写不同的mac
2、自动启动httpd –h /tzwww
3、制作cpe文件系统时，把http://192.168.1.123/svn/bigap_web中内容带上。

2012-4-28
1、update程序中，仅仅修改了一点提示的东西，就无法升级了。奇怪的问题。

2012-4-26
1、修改mac程序，无参数是读数据
2、cpe中编译增加art.ko和nart.out
3、去掉模块版本检查：修改scripts/setlocalversion文件，将git部分的代码注释掉，这样版本号中就没有乱七八糟的gxxxxxx-dirty的字样了。

2012-4-25
1、仅仅设置这个CONFIG_MODULE_FORCE_LOAD=y
# CONFIG_MODVERSIONS is not set

2012-4-24
1、自己写一个升级程序是可以的，但系统无法自己重新启动，拔电后可以的。
2、从一个简单的系统要可以编译，需要安装以下东西：git, make, gcc, bison, flex, gettext, patch, gcc-c++, ncurses-devel, sharutils, zlib-devel。

2012-4-23
1、u-boot改回千兆似乎问题依旧，不管它了，就让它在百兆跑吧。
2、9344的uboot编译似乎有些怪异，如果编译整个的代码，会编译，但不会复制到tftp的目录中去，而如果单独编译，会报没有tozedap的make目标。
3、在9344上采用dd的方式就可以升级文件系统。而在9331上，dd显示的块数也没有什么问题。
4、mtd char设备号是90，而mtdblock的设备号是31，这在dev.txt中有体现。

2012-4-22
1、把9311上的/dev/rootfs定义为快设备，可以直接进行写操作，但写到0x135c00就不写了，而整个文件的长度是17acd0。

2012-4-21
1、pc上的sscanf和9344上面的表现行为完全不同。
2、9311上存在/dev/nvram和/dev/caldata两个目录。9311的config中定义了ATH_CONFIG_NVRAM。
3、对于9311来说，要改的是eth1?
4、9311上的/dev/caldata不能直接写，而9344上的可以直接写。两个设备类型不同，一个是字符设备，一个是块设备。
5、使用ioctl可以对flash进行擦除动作。

2012-4-20
1、交换芯片上去掉一个电阻，去掉802.3的自动休眠，貌似就没有问题了。两个星期啊。
2、如果没有设置ATH_countrycode，那么就貌似在rc.wlan脚本中就会指定到美国去。
3、可以使用先擦除再写的方式来升级内核。
4、/dev/caldata中的内容就是art的内容。

2012-4-19
1、从art区开始6个字节是eth0的地址，然后是eth1的地址。而ath0的地址从0x1002的位置。参数区9344在art区0x8000位置，而9331在单独的nvram区。
2、/dev/mtd0是字符设备，而/dev/mtdblock0是块设备，映射的是同样的地址。
3、发包程序中，有线用3，无线用4，就可以广播发送数据了。有意思的情况有两个：两个无线终端之间，是无法收到的。还有就是从arm上发下来的包，ap和cpe收到的数据都在后面增加了一些数据，尚不清楚这些数据的含义。
4、iwpriv ath0 ap-bridge 0的确有用，但在网上似乎没有搜到过这个设置。

2012-4-18
1、在9344中如果使用echo 0 a100  > /proc/ar8035/reg强制到100m，那么就貌似也没有什么问题了。
2、9344中的两个mac控制器的地址是0x19000000和0x1a000000。
3、如果使用标准接法，pc使用自动获得地址，是可以得到局域网内的某个dhcp服务器的地址的。
4、art一定会编译，但不会放入文件系统。
5、INSTALL_ROOT是带有.build的目录,而IMAGE_ROOT是.optbuild的目录，它首先复制INSTALL_ROOT目录中的所有文件，然后执行了一大段操作。

2012-4-17
1、git config --global user.email jianliang@sztozed.net
git config --global user.name jianliang
2、如果把u-boot强制设置为100m，那么传文件就不会显示问题了。
3、使用无线，用电脑和ap相连，使用ping tester这个工具，共ping了1686700 lost:830 失败率为0.05%。
4、ap,cpe相连，使用teletest的测试卡来测试，仅仅能保证在2M的情况下不怎么丢失包。

2012-4-16
1、电脑之间的ping，看来是完全没有丢包的。
2、网卡驱动是linux/drivers/etherne/arthrs_gmac.ko

2012-4-15
1、许多种奇怪的现象。不写了。

2012-4-14
1、修改9寄存器改为从模式，貌似在某个位置是正常了。

2012-4-13
1、奇怪的现象是，如果在外部向9344快速ping包，那么9344向外ping包就没有什么问题，否则ping丢包就很严重。
2、u-boot传文件仍然问题很多。
3、如果去掉取寄存器的做假，还是会有网卡up之类的消息蹦出来。
4、在100m的情况下u-boot是正常的。

2012-4-12
1、编译9344时，hostap-0.7.2下没有.o文件，编译9331时，athr_hostap下没有.o文件，所以看来9344使用的是特别的athr_hostap。
2、9344的内核放在9331上是无法运行的。
3、linux的清屏指令是clear
4、使用dd指令可以成功的把flash写0，貌似没有什么作用。但如果直接写文件内容，那么就是错的，应该是和flash必须擦除有关。
5、可以使用rm dir –rf && git checkout dir/* 快速恢复文件。
6、好容易编译出来一个flash_earse，擦除非文件系统区，就能返回，否则，擦除后就没有动静了。看来要做一个非常小的系统来工作？

2012-4-11
1、服务器249的机器时间居然超前了1天，停电后linux的时间也就变成了12日，对时后发现网卡驱动编译不了了，而重新下载的东西的干净环境则还是可以编译。
2、将当前时间写入硬件：
	hwclock –systohc
3、使用s17的phy驱动的u-boot还能收到几个包，而使用803x的呢，一个都收不到。但进入linux后就好些。
4、apps目录下的hostap-0.7.2和athr_hostap目录下都有.o存在，所以不知道是用的哪个。
5、使用dd命令可以方便的将文件的一部分复制到另外一个文件。
	dd if=xxx of=xxx bs=1 skip=800 [count=900]
6、如果要仅仅编译网卡的驱动，make enet_build

2012-4-10
1、自动编译的脚本也很简单：
rm bigap -rf
git clone git@192.168.16.249:bigap
cd bigap/ar9344/build && make BOARD_TYPE=tozedcpe
cd bigap/ar9344/build && make BOARD_TYPE=db12x ETH_CONFIG=_ar803x
2、cgi的源程序在drivers/wlan/os/linux/tools目录中，有两个文件cgiMain.c和wlancfg.c两个文件组成。
3、只找到gpio13作为lan灯是在0x18104070这个寄存器来设置的，但没有找到代码中有什么地方对它进行了控制。现在可以换到gpio18来进行操作。这样三个灯是：gpio0, 17, 18 其中0这个还要在makefile中取消无线对灯的控制。

2012-4-9
1、调整了一天的phy，其实8023这个phy从本质来说只需要设置两个寄存器：debug 寄存器0和debug寄存器5，设置一下rx/tx delay。
2、把phy_reg_write和phy_reg_read这两个函数的第二个参数由0改为4，那么u-boot和内核都能读到phy id，u-boot中的两个设置语句
      phy_reg_write(unit, 0, 0x1D, 0x0);
    phy_reg_write(unit, 0, 0x1E, 0x82EE); /* 0x02EE - no delay, 0x82EE - rx delay*/
    //val = phy_reg_read(unit, 0, 0x1E);
    //printf("Debug reg 0x0 = 0x%x\n", val);
    /* delay tx_clk */
    phy_reg_write(unit, 0, 0x1D, 0x5);
    phy_reg_write(unit, 0, 0x1E, 0x2D47); /* 0x2C47 - no delay, 0x2D47 - tx delay */
  把后面的读的语句放开，也正确读到了设置的值。
3、调整其他设置模式作用不大。
4、文件系统中resolv.conf并没有搞成到可写的地方的链接。
5、把db12x中的www文件复制到ap121上是可以使用的。在db121中ap_type定义为dual，而ap121中定义为single。

2012-4-6
1、bug：使用make BOARD_TYPE=tozedcpe编译出来的文件系统没有加载网卡驱动。
2、增加makeflash，直接生成完整的tozedcpe.bin。

2012-3-31
1、9344选择的flash是S25FL064A@SOIC16
2、linux进行模块编译时，make文件的写法要注意：obj-m = 模块名.o 这里的模块名，如果和.c名称相同，而且只有一个.c文件，就可以了。如果有多个.c或者模块名和.c名字不一样，就要再加一条：模块名-objs = xxx.o xxx.o   等。
3、iwpirv ath0 wds 1这个问题呢，9331上是打开的，所以，只要9344打开就好了，这样可以解释为什么tp-link代替9344就可以用的问题，但不能解释为什么tp-link代替9331也可以使用的问题。
4、无线网络linux 下git clone的速度也能够到的2m多，相当快了。但同时ping的延时立即从2ms左右上升到了200ms多。

2012-3-30
1、设置一下iwpriv ath0 wds 1，就可以进行转发了。其实这也是比较奇怪的问题，9331上这个参数是打开的，而9344作为stand是没有打开，所以不能转发，但使用tp-link就代替9311就没有问题，这又是为什么呢？
2、9382是一块无线网卡。
3、使用openwrt编译出来的东西用不了，奇怪啊。
4、李瑶发现只有农行的卡会出问题，看程序应该是出口参数时一般300的变量不足。增加这个变量，看看情况如何。

2012-3-29
1、悲哀啊，芯片厂家的人也没有搞明白原因，他把9331上的mac地址修改后，从9331上可以ping到9344了。说回去抓包看原因。
2、下载了openwrt上面下载的dropbear，结果运行结果是symbol '__ctype_b': can't handle reloc type 0x7e，网上说是不同的uclibc编译器的原因。
3、tplink上的系统也是busybox1.01，不过它的br0使用的是ath0的mac，这有些奇怪，因为它的eth的mac也要小，难道它改了内核代码？可以自定义使用什么mac?
4、李瑶那边发现了王博程序可能有问题。

2012-3-28
1、这个脚本可以随机修改ssid
#!/bin/sh
c=$(cfg -e | grep AP_SSID | grep SSID= | grep Atheros_XSpan_2G)
c=${c% *}
if [ -z $c ] ; then
        echo ok
else
        echo must change
        ssid=$(cat /proc/sys/kernel/random/uuid)
        echo $ssid
        ssid=${ssid%-*}
        ssid=${ssid%-*}
        ssid=${ssid%-*}
        ssid=${ssid%-*}
        cfg -a AP_SSID=tozed-$ssid
        cfg -c
fi
但如果把这个脚本放在rcS中去执行，那么就没有什么效果了，每次结果都是一样的。只有考虑做一个网页，由用户去点了。
2、如果没有加载网卡的驱动，那么网卡的那个io是无法控制的，奇怪。
3、仍然存在ko版本不同的报错，奇怪啊。
4、增加了一个tozedgpio.c文件，单独控制gpio，以及为以后控制温度芯片来写程序。

2012-3-27
1、在scripts/ap121-2.6.31/config.ap121-2.6.31文件中有：
export KERNELARCH=mips
export TOOLPREFIX=mips-linux-uclibc-
而在build的Makefile 中：
export MAKEARCH=$(MAKE) ARCH=$(KERNELARCH) CROSS_COMPILE=$(TOOLPREFIX)
然后才可以对内核进行编译：
cd $(KERNELPATH) && $(MAKEARCH) $(BOARD_TYPE)$(BUILD_CONFIG)_defconfig
cd $(KERNELPATH) && $(MAKEARCH)
所以进入内核的目录直接make是无法编译的。
2、还是简单的使用
make kernel_build BOARD_TYPE=ap121-2.6.31
来编译内核吧。
这样编译的内核不会自动复制到tftp目录中去。
3、没有带modproble这个程序。
4、arch/mips/ar7240/gpio.c才是需要修改的gpio代码。
5、把相应的config.XXX 文件中的ATH_SUPPORT_LED变成0，GPIO_0就可以控制了，但那个system的gpio27一直无法控制。
6、网卡的灯还受网卡驱动的控制。
7、增加一个新的设备类型需要以下地方增加：
	u-boot/Makefile 内容
	apps/busybox-1.01/ 增加一个defconfig-xxxx文件，可以从其他defconfig文件复制。
	build/scripts/ 增加一个xxx目录，可以从其他目录复制，然后修改目录中的Makefile.xxx 和config.xxx文件名。
	rootfs/ 中增加一个xxx的目录，可以从其他目录复制。
	build/gcc-4.3.3/toolchain/cClibc/ 增加xxx.config文件，可以从其他.config文件复制。
	gcc4.3.3/ 增加xxx.config文件，可以从其他.config文件复制。
8、Makefile有时候会不理睬%.o的规则，直接按照(CC) –c –o 来编译。

2012-3-26
1、9331和9334无法连起来，而和tplink都是可以相连的。
2、貌似写gpio一定要写内核模块，否则好像无法调用内核中的函数。
3、wlanconfig ath0 list sta 可以显示连接的无线客户端。
4、ath_gpio_config_output这个函数似乎只有在/linux/drivers/ethernet/ag934x.c中使用过。这就不知道其他几个灯是在哪些代码进行控制的了。

2012-3-24
1、虚拟机可以是nat的模式，传文件可以使用ssh那个图形化工具。
2、在arch/mip/include/asm/mach_ar7420中的ar933x.h中有IO的地址定义。933x的IO地址定义在0x18040000。

2012-3-23
忙碌的一天。在生产迷你终端，碰到了问题：
1、删除configuration.ini文件后，游霖发现数据没有了，其实系统启动时在/etc/init.d/rcS中做了判断/mnt/logdisk/configuration.ini的文件判断操作，由于删除后没有成功重新启动，又做了其他操作，这些操作在读取文件时发现文件不存在，就自动生成了文件，这样就少了很多参数。
2、无线密码键盘的版本号居然显示的是0.1，而且居然是我写的。
3、游霖发现插件中reboot函数名不相同的问题，实际上是李瑶在河北的程序里面做了一个转换，而在河南的程序里面直接使用了插件里面的函数名称。
4、9331和9334两个板子都不能当做client来使用，真是奇怪。下面是apup中相应的代码：
    if [ "${AP_STARTMODE}" = "client" ]; then
        makeVAP sta-wds "$AP_SSID" 0:RF:$AP_PRIMARY_CH:$AP_CHMODE
        if [ $? != 0 ]; then
            echo "Unable to create VAP!"
            exit
        fi

        if [ "${ROOTAP_MAC}" != "" ]; then
            iwconfig ath0 ap $ROOTAP_MAC
        fi

        activateVAP ath0 br0 $AP_SECMODE $AP_SECFILE
fi

2012-3-22
1、安装openssh server 就可以在windows上面建立ssh server
2、使用tp-link可以作为客户端，其连接的pc可以连接到ap所在的网络。
3、在tp-link上使用vconfig貌似没有作用。

2012-3-21
1、下面的脚步可以统计流量信息，本质上就是不同从/proc/net/dev中得到数据后，进行平均。
#!/bin/bash
echo -n "which nic?"
#read eth
eth=eth0
echo "the nic is "$eth
echo -n "how much seconds："
#read sec
sec=10
echo "duration is "$sec" seconds， wait please..."
infirst=$(awk '/'$eth'/{print $1 }' /proc/net/dev |sed 's/'$eth'://')
outfirst=$(awk '/'$eth'/{print $10 }' /proc/net/dev)
sumfirst=$(($infirst+$outfirst))
sleep $sec"s"
inend=$(awk '/'$eth'/{print $1 }' /proc/net/dev |sed 's/'$eth'://')
outend=$(awk '/'$eth'/{print $10 }' /proc/net/dev)
sumend=$(($inend+$outend))
sum=$(($sumend-$sumfirst))
echo $sec" seconds total ："$sum"bytes"
aver=$(($sum/$sec))
echo "avrage ："$aver"bytes/sec"
2、9331上没有时钟，总是从1970年开始，也没有对时的程序。
3、所有cpe使用相同的ip，从理论上来说应该是没有问题的。
4、在77服务器上使用virtulbox安装centos后，关闭后就再也无法启动了，奇怪啊。
5、自己的脚步或程序可以放在rootfs/$(board_type)$(build_config)目录中，make的时候是原样复制到目标文件系统中。
6、写了一个简单的拼接程序，形成一个文件系统。可以一次性使用编程序写入。
7、tp-link的flash也可以直接使用mx25L3206的来读。

2012-3-20
1、编译内核是makearch就是make，首先做了一下 make $(board_type)$(buld_config)_defconfig 这样来保证可以编译不同的内核。
2、9331上的cfg和9334上的提示信息还不同。
3、boot/u-boot/tools/crc32.c和enviroment.c在make之后变成了两个符号链接。
5、貌似没有去掉那个version magic 如果文件系统和内核不是一次编译出来的，那么网卡的ko就无法加载。

2012-3-19
1、这个地方有git显示中文问题的各种解决：
http://blog.sina.com.cn/s/blog_4bf3a4fb0100uprs.html
2、git config –l 可以查看所有的git配置信息
3、9331使用apup就会重新启动。
4、build/ scripts/ap121-2.6.31/config.ap121-2.6.31文件中有文件系统的定义BUILD_TYPE的定义。
5、修改scripts/ap121-2.6.31/config.ap121-2.6.31文件中export COMPRESSED_UBOOT=1，就可以把9331的uboot换为非压缩的，并且有sav指令了。
6、李柱栋和陈良调带有证书的soap，发现证书生成时间比系统时间晚时，就会拒绝证书。
7、烧录9331的flash选择的是mx25l3206@sop8

2012-3-16
1、ar9331的文件系统是squashfs，不知道能否修改。答案是不能。
2、碰到Perhaps you should specify a branch such as 'master'. 这样的问题，需要：
git push origin master就可以了。

2012-3-9
1.svn diff –r 82:81即可显示两个版本之间的区别，但貌似没有机制来显示两个版本之间修改的文件

2012-3-7
1、centos使用sudo
yum install sudo
vi /etc/sudoers
找到root ALL(ALL) ALL，增加一行加上用户即可

2、centos的网卡ip配置文件在/etc/sysconfig/network-scripts/目录中
网关在/etc/sysconfig/network中

2012-2-2
1、centos中，yum install zlib-devel可解决zlib.h找不到的问题。
2、sudo chmod a+w /tftpboot/ 如果忽略+前面的a那么是执行是无效的。

2012-02-01
centos中yum install man-pages后就能查到函数说明。

2012-1-13
sudo ntpdate time.windows.com 即可完成对时。

2012-1-6
pppd的at指令如果存在^符号，必须在^前加\，才能正常发送

2011-11-30
1、增加另外一个ip:   ifconfig eth0:0 192.168.16.79

2、ssh登录时不使用dns反向解析：
编辑/etc/ssh/sshd_config，禁用登陆时dns反向解析
将#UseDNS yesn 改为：
UseDNS no

重启sshd服务
service sshd restart

2011-11-24
1、貌似无论如何修改yaffs的选项，都会出现firefox无法启动的现象。这个现象不是非常容易出现，但连续都不能连续重启一夜仍然正常。

2011-11-22
使用该指令来编译新的内核：
 make CROSS_COMPILE=arm-none-linux-gnueabi- ARCH=arm am3517_evm_defconfig

2011-11-21
在http://vault.centos.org/ 可下载过去的版本
(sleep 120; psplash-write "QUIT") & 延时运行程序

2011-11-19
使用以下脚本，有一天机器有时候firefox不能启动。
cat checkf
#!/bin/sh
sleep 200
while true
do
        FIREFOX=$(ps -e | grep firefox)
        FIRFFOX=${FIREFOX:0:5}
        if [ -z $FIREFOX ] ; then
                sleep 10
        else
                reboot
        fi

done

2011-11-9
printf是有默认的行缓冲的

2011-11-8
//如果不是开发终端之类的，只是串口传输数据，而不需要串口来处理，那么使用原始模式(Raw Mode)方式来通讯，设置方式如下：
       options.c_lflag  &= ~(ICANON | ECHO | ECHOE | ISIG);  /*Input*/
       options.c_oflag  &= ~OPOST;   /*Output*/

2011-10-31
#sudo route del –net 0.0.0.0						#删除缺省路由
#sudo route add –net 0.0.0.0 gw 192.168.1.2
#sudo route add –net 10.0.0.0 gw 1.1.1.1 netmask 255.0.0.0
#sudo route add –net 170.0.0.0 gw 1.1.1.1 netmask 255.0.0.0


2011-10-28
array networks的vpn
使用这份文档可以连上河南移动的vpn  http://q.pnq.cc/archives/539
array networks的支持网页也有写，不过稍许有些不同。http://support.arraynetworks.com.cn/troubleshooting/V8.4.6.0.16/

如何来做一个转发的机器呢：
#sudo route del –net 0.0.0.0						#删除缺省路由
#sudo route add 170.170.100.157 gw 1.1.1.1		#增加银联地址
suod add –net 192.168.16.0 netmask 255.255.255.0 dev eth0 #恢复本地网络

2011-10-12
man –f free 可以得到保护free的帮助列表
free (3)             - Allocate and free dynamic memory
free (1)             - Display amount of free and used memory in the system
再man 3 free 就得到了Allocate and free dynamic memory这个说明

2011-9-29
增加svn仓库中文件的可执行属性。
svn propset svn:executable on test.c
取消：
svn propdel svn:executable test.c
http://bigwhite.blogbus.com/logs/74568031.html

2011-9-8
如果在ramdisk中有几个.svn的目录，那么最后的ramdisk.tar.gz就可以到4m多，而如果没有，就要到5m多，真是奇怪啊。

2011-9-7
vi .svnignore
每种要忽略的文件加一行，如：
*.pyc
*.cash
然后
svn propset svn:ignore -F .svnignore .
svn status
清净了。

要使用\\192.168.1.112这样的东东，貌似要开启network connections这个服务

Svn st --no-ignore，当不希望有所忽略时，加这个选项。

2011-8-31
1、使用busybox带的udhcpc就可以自动获得地址。同时会修改路由和dns文件。
2、万辉写的文档可以完成河北的部署，但不能完成从源码开始的部署。
3、写卡方面，毛其桂那边电脑没有批下来，所以需要等待。

2011-8-26
1、ifconfig eth0 add 10.10.33.145 //增加一个IP，这种方法在板子上是不行的，要这样：
	ifconfig eth0:0 192.168.16.79

2011-8-25
1、使用option.ko作为串口的驱动时，有非常奇怪的现象，就是在一段时间内，模块会不响应at指令，应该是这个驱动有问题。但option.ko的主要优点是可以自动识别不同的模块，不需要每次都用modprobe来指定参数。

2、不断重新给模块上电、拨号、下电的脚本
#!/bin/sh
killall pppd
killall check3g
count=0
ok_count=0
fail_count=0
while [ $count -le 100 ]
do
        echo 0 > /dev/gpio135
        sleep 1
        echo 1 > /dev/gpio135
        sleep 15
        pppd call cmnet
        dial_delay=0
        while true #[ $dial_delay -le 60 ]
        do
                if [ -f /var/run/ppp0.pid ]
                then
                        ok_count=$(($ok_count+1))
                        sleep 2
                        break
                fi
                dial_delay=$(($dial_delay+1))
                if [ $dial_delay -gt 60 ]
                then
                        fail_count=$(($fail_count+1))
                        break
                fi
                sleep 1
        done
        count=$(($count+1))
        echo test $count times, $ok_count successed $fail_count failed
done

2011-7-6
1、方舒遇到的问

2011-7-5
1、6.27记录的脚本已经连续工作了12天，百度查询8550次。

2011-7-4
1、连续播放一天的声音，并不断kill掉它，貌似没有出现什么问题。
2、6.27记录的脚本已经连续工作了11天，百度查询7773次。
3、前天方舒打电话来说使用vbscript不能相应ocx中的事件，而使用javascript是可以的。今天问他说是证通的透露是要在ocx中建立一个窗口，窗口发的事件vbscript可以相应。

2011-7-1
1、6.27记录的脚步已经连续运行了8天，应该认为是没有什么问题了。

2011-6-27
1、我们使用 svn 作为版本管理工具。 有时同事 A 做的修改需要同事  B 去 Review, 同事 C 去提交。 今天发现，使用patch 工具可以很好的解决代码传递问题。
生成 patch:
同事 A 运行如下命令生成 patch:
svn diff > aaa.patch

应用 patch:
同事 B 运行如下命令应用 patch:
patch –p0 < ../aaa.patch

当他 review 完代码，想删除该 patch 时， 可运行：
patch –p1 -R < ../aaa.patch
http://blog.csdn.net/zjujoe/archive/2008/12/27/3622312.aspx

2、以下代码已经连续运行了4天，和以前的主要改动是删除了内存中firefox文件，重新复制了一份，kill的时候使用了-SIGTERM参数
#!/bin/sh
export DISPLAY=0:0
count=0
while true
do
   rm /media/ram/* -rf
   cp /home/root/.mozilla/firefox.000/* /home/root/.mozilla/firefox/. -rf
   firefox http://www.baidu.com/s?wd=$count&inputT=594 & > /dev/null 2>&1
   i=1
   while [ $i -le 120 ]
   do
       sleep 1
       echo -n '*'
       i=$(($i+1))
   done
   #dmesg
   cat /proc/meminfo | grep MemFree
   killall -SIGTERM firefox-bin
   count=$(($count+1))
   echo run $count times
done

3、如何让TortoiseSVN仅导出新增或修改过(变更过)的文件
http://www.subversion.org.cn/?action-viewnews-itemid-90

4、使用EXPORT_SYMBOL这个宏，就可以把内核中的函数引出，在ko中使用。

2011-6-24
1、如果使用lcp-echo-interval 和lcp-echo-failure的方式，貌似即使关闭屏蔽门，完全没有信号，也不会断线。

2011-6-23
1、原来在windows下的命令行也支持tab自动完成功能。
2、跑和讯滚动新闻的跑了2天多，由于没有显示屏，开了一下x11vnc，就不行了。
top - 08:50:51 up 2 days, 16:00,  3 users,  load average: 0.10, 0.13, 0.06
Tasks:  66 total,   1 running,  65 sleeping,   0 stopped,   0 zombie
Cpu(s): 12.5%us,  2.0%sy,  0.0%ni, 85.5%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:    250996k total,   166364k used,    84632k free,        0k buffers
Swap:        0k total,        0k used,        0k free,    71604k cached
在使用x11vnc之前，还有89M的空余内存。
3、如果使用脚本去操作watchdog，就总是会报不能关闭的错误，还是写个程序来吧。

2011-6-22
1、无线键盘使用平台需要进行的修改：
功能	负责人
数据库增加店主银联卡信息	谭凯凯
设置页面增加读取店主银联卡信息页面。	谭凯凯
2.4g插件和2.4g设备驱动交互，完成原来2.4g_app功能	王博
2.4g插件调用页面js，指示有银联缴费请求	赵金
页面js增加接口，收2.4g插件银联请求，如果不在待机界面，直接返回或调用2.4g插件接口，暂时不能操作。如果在待机界面，则进入业务处理界面	谭凯凯
增加业务处理中页面，页面只显示业务处理中，请稍等。	谭凯凯
增加无线键盘银联缴费脚本过程，在上面的页面中作以下处理：
1、	关闭键盘。
2、	使用pin密钥算pin
3、	提交银联缴费请求
4、	将结果返回2.4g插件
5、	切换页面到待机界面	谭凯凯


2、以下脚本运行了2天减去20小时，实际上只运行了30个小时不到。为什么在firefox停留的时间长反而会增加死机的概率呢？
#!/bin/sh
export DISPLAY=0:0
count=0
while true
do
   firefox http://www.baidu.com/s?wd=$count&inputT=594 & > /dev/null 2>&1
   i=1
   while [ $i -le 120 ]
   do
       sleep 1
       echo -n '*'
       i=$(($i+1))
   done
   #dmesg
   cat /proc/meminfo | grep MemFree
   killall -SIGTERM firefox-bin
   count=$(($count+1))
   echo run $count times
done

top - 22:24:27 up 2 days, 11:40,  2 users,  load average: 0.03, 0.06, 0.08
Tasks:  72 total,   1 running,  71 sleeping,   0 stopped,   0 zombie
Cpu(s):  0.3%us,  1.0%sy,  0.0%ni, 98.7%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:    250996k total,   145076k used,   105920k free,        0k buffers
Swap:        0k total,        0k used,        0k free,    72672k cached

2011-6-17
1、以下脚本支持了3天。
#!/bin/sh
export DISPLAY=0:0
count=0
while true
do
   firefox http://www.baidu.com/s?wd=$count&inputT=594 & > /dev/null 2>&1
   i=1
   while [ $i -le 15 ]
   do
       sleep 1
       echo -n '*'
       i=$(($i+1))
   done
   #dmesg
   cat /proc/meminfo | grep MemFree
   killall -SIGTERM firefox-bin
   count=$(($count+1))
   echo run $count times
done

2011-6-15
1、编译插件要在xulrunner-sdk/include/plugin/npapi.h文件中加入#define XP_UNIX

2011-6-14
1、使用firefox 3.0.1，跑了700多次开启关闭，还是崩溃了。
2、测试脚本：
#!/bin/sh
export DISPLAY=0:0
count=0
while true
do
   firefox http://www.baidu.com/s?wd=$count&inputT=594 & > /dev/null 2>&1
   i=1
   while [ $i -le 15 ]
   do
       sleep 1
       echo -n '*'
       i=$(($i+1))
   done
   #dmesg
   cat /proc/meminfo | grep MemFree
   killall -SIGTERM firefox-bin
   count=$(($count+1))
   echo run $count times
done

2011-6-13
1、在main.js中，做如下修改，就可以避免快速倒计时引起的崩溃。
showMessage : function(seconds) {
		//$('#count_down').html("剩余 <span>" + seconds + "</span> 秒");
		$('#count_down').html(seconds);
2011-6-10
1、换原来的busybox跑了11个小时，情况差不多。

2011-6-9
1、昨天晚上继续wget测试，奇怪的现象，约2个小时后，wget界面停止得到数据，“使用ssh可以连接，出现密码提示，但是连接进去后无反应，串口输入无反应，鼠标正常，拔下时串口有信息，”但拔下之后，又都变得正常。这个正常后到了10:24再看的时候，再次不正常，这次拔掉鼠标只有串口消息，但无法再正常了。此时使用ssh secure file transfer 是可以看见文件的

2011-6-8
1、从昨天起，再次使用wget，用内网连接不断去www.163.com数据，开始间隔时间1s，后来60秒，一直没事，但晚上发现：使用ssh可以连接，出现密码提示，但是连接进去后无反应，串口输入无反应，鼠标正常，拔下时串口有信息，再次插上无反应。

2011-6-7
1、wget放14小时左右死掉2次。
2、从内网连接，使用浏览器取和讯的滚动新闻死掉，而取新浪的滚动新闻没有发现死掉的情况。

2011-6-2
#!/bin/sh
export DISPLAY=0:0
count=0
while true
do
        firefox http://www.163.com & > /dev/null 2>&1
        i=1
        while [ $i -le 120 ]
        do
            sleep 1
            echo -n *
            i=$(($i+1))
        done
        #dmesg
        cat /proc/meminfo | grep MemFree
        killall firefox-bin
        count=$(($count+1))
        echo run $count times
done

2011-5-31
1、把.mozilla目录下的firefox目录改为一个链接，指向/tmp，很快就会报内存不足的错误，并死机。

2011-5-30
1、使用firefox跑了一个晚上，出现
yaffs: yaffs tragedy: no space during cache write
yaffs: yaffs tragedy: no more erased blocks
yaffs: !!!!!!!!! Allocator out !!!!!!!!!!!!!!!!!
2、nand scrub命令重新完全擦除nand

2011-5-29
ifdown eth0
ifconfig eth0 hw ether 00:e0:4c:f9:0b:8c
ifup eth0
ifconfig eth0 192.168.1.79
route add default gw 192.168.1.2

root@am3517-evm:~# cat f
#!/bin/sh
export DISPLAY=0:0
while true
do
        firefox http://www.163.com &
        for i in 1 2 3 4 5 6 7 8 9 10
        do
                sleep 10
                echo $i
        done
        dmesg
		cat /proc/meminfo
        killall firefox-bin
done

2011-5-26
1、写现金缴费部分程序。
2、赵金：可以下载更新了。
3、李柱栋：psam更新库已经发给了毛其桂，修正在某种情况下会将回显的命令字发给调用者。

2011-5-25
1、测试现金缴费流程。
2、颜斌：有块版，如果加上电池，就不能启动，未知原因。
3、李柱栋：打印机机驱动修改，不需要上层来关闭。做文件系统，加入文泉字库。
4、赵金：测试升级，发现firefox会崩溃。

2011-5-24
1、王博：上传了2.4g驱动程序。

2011-5-23
1、去珠海，对方毛其桂应该还没有开始。

2011-5-22
1、加快拨号速度，把rc5.d中的S60usbmodem删除，在rcS.d中
ln –s ../init.d/init-modem S70usbmodem
这样在登录提示之前，就可以识别到模块。

改进后的拨号脚本，先进行拨号一次，60秒后再进行循环检测。
#!/bin/sh
CONFIG_FILE=/mnt/logdisk/configuration.ini
if [ ! -f $CONFIG_FILE ] ; then
        #echo no configuration file. exit now.
        exit
fi

USE3G=$(awk  -F" " /USE3G/'{print $2}' $CONFIG_FILE)
if [ "$USE3G" != "yes" ] ; then
        #do not use 3g, exit
        exit
fi

route del default
pppd call cmnet
sleep 60

#dns1="www.163.com"
#dns2="www.baidu.com"
dns1=120.196.165.7
dns2=221.179.38.7
while true
do
       ping -s 1 -c 1 $dns1
       if [ "$?" != "0" ]
       then
           ping -s 1 -c 2 $dns2
           if [ "$?" != "0" ]
           then
              killall pppd
              //route del default
              pppd call cmnet &
              sleep 12
              sleep 50
           fi
       else
              sleep 50
       fi
done
2、写新的任务分配表。

2011-5-20
1、自动设置ip的脚步
# cat setip
#!/bin/sh
CONFIG_FILE=/mnt/logdisk/configuration.ini
if [ ! -f $CONFIG_FILE ] ; then
        #echo no configuration file. exit now.
        exit
fi
LOCAL_IP=$(awk  -F" " /ADDRESS/'{print $2}' $CONFIG_FILE)
LOCAL_NETMASK=$(awk  -F" " /NETMASK/'{ print $2}' $CONFIG_FILE)
LOCAL_GATEWAY=$(awk  -F" " /GATEWAY/'{ print $2}' $CONFIG_FILE)

if [ "$LOCAL_IP" != "" ] ; then
        #echo set ip $LOCAL_IP
        ifconfig eth0 $LOCAL_IP netmask $LOCAL_NETMASK
fi

if [ "$LOCAL_GATEWAY" != "" ] ; then
        #echo set route $LOCAL_GATEWAY
        route add default gw $LOCAL_GATEWAY
fi
2、自动拨号
#!/bin/sh
#请把dns1,dns2修改成拼得通的DNS,开机自动运行,实时监控,断线自动重拨
dns1="www.163.com"
dns2="www.baidu.com"
while true
do
       ping -s 1 -c 1 $dns1    #去PING第一个DNS
       if [ "$?" != "0" ]      #假如PING不通
       then
           ping -s 1 -c 2 $dns2  #去PING第二个DNS
           if [ "$?" != "0" ]     #假如PING不通
           then
              killall pppd         #结束PPPD进程
              pppd call cmnet & #再去拨号
              sleep 12               #等待12秒
              sleep 50            #如果是PING  DNS2通的话就直接等待5秒
           fi
       else
              sleep 50            #如果是PING  DNS1通的话就直接等待5秒（一般要设置多长时间去PING请改这里）
       fi
done


2011-5-19
做文件系统，包括：
1、修改文件日期，使用指令 find . -name '*' -exec touch {} \; 将所有文件的日期改为当前日期。
2、去掉登录界面，修改etc/sysconfig/gpelogin文件中AUTOLOGIN="false"改为"true"
3、增加mount.nfs到/sbin目录中
4、firefox加入全屏组件full_fullscreen-3.4-fx.xpi
5、减少firefox的缓存为10M
6、firefox自动启动，在/etc/X11/Xsession.d/98standard-apps文件中，最后加一行firefox &

2011-5-18
1、自动拨号取网站，断线，不断循环的脚步。
#!/bin/sh
while true
do
        echo begin dial.....
        pppd call cmnet
        sleep 30
        wget http://www.baidu.com -T 60 -t 1
        echo disconnect....
        killall pppd
        sleep 5
done
2、使用绑定td或者绑定gsm的模块程序，就可以正常的拨号和上网，如果使用自动切换的程序，就要设置mtu=900才能取得网页。

2011-5-17
1、使用otg口，模块会有不能上网的问题，把mtu改为900才行。
2、修改drivers/mmc/host/omap_hsmmc.c内的#define OMAP_MMC_MASTER_CLOCK 96000000为104000000，就可以对增加静电保护器件的板子的MMC卡了。
3、万辉：完成了通用的cgi的程序，需要在板子上测试。
4、李柱栋：半切还是有问题，只有全切了。

2011-5-12
1、使用pptp拨号总是有问题。

2011-5-10
1、开会，详细见工作安排文档
2、东信和平回邮件，需要签保密协议。
3、killall ipaq-sleep进程，仍然有黑屏动作
4、qte的界面貌似没有黑屏动作，也没有花屏的现象。

2011-5-9
1、使用多个文件系统进行测试，发现直接对/dev/fb进行操作，就可以进行对屏幕的操作，这个操作似乎没有发现有花屏的情况发生。
2、dd：内存复制 dd if=/dev/fb0 of=1，把屏幕的内容复制到文件1中。而dd if=/dev/zero of=/dev/fb把屏幕清空。

2011-5-7
1、系统不能重新启动的原因是由于在/etc/rcS.d/S03udev这个脚步中对是否是第一次运行做了判断，这个判断对后面的建立/dev中的文件时有不同。屏蔽以下代码就好了。
#如果进行了这样操作，可能有如下影响：
#如果开机未完成的情况就关机，那么/dev中的文件可能不全，ttyS0也没有能够建立，图形系统不能进入。
#if [ "$DEVCACHE" != "" ]; then
#       # Invalidate udev cache if the kernel or its bootargs/cmdline have changed
#       [ -x /bin/uname ] && /bin/uname -mrspv > /tmp/uname || touch /tmp/uname
#       [ -r /proc/cmdline ] && cat /proc/cmdline > /tmp/cmdline || touch /tmp/cmdline
#       [ -r /proc/atags ] && cat /proc/atags > /tmp/atags || touch /tmp/atags
#       if [ -e $DEVCACHE ] && \
#          cmp -s /tmp/uname /etc/udev/saved.uname && \
#          cmp -s /tmp/cmdline /etc/udev/saved.cmdline && \
#          cmp -s /tmp/atags /etc/udev/saved.atags; then
#               (cd /; tar xf $DEVCACHE > /dev/null 2>&1)
#               not_first_boot=1
#       fi
#fi
2、花屏的情况比较严重，要找一下是什么原因。

2011-5-6
1、sed –i –e /rm_work/d build/conf/local.conf 去掉local.conf中的rm_work，保留源码。
2、更换文件系统，更换内核进行测试，仍然会出现不能正常启动的情况。但如果每次复位都发生在系统启动2分钟之后（把telnet的启动前增加一个sleep，并将脚步放到后台运行，这样zmud就无法快速连上），貌似就不会出现了。
3、李柱栋：新的打印机切刀的步进能力不够，如果纸硬，步进就少，反之就多。这样要实现半切就有困难。
4、王博：可以实现按键驱动了。

2011-5-5
1、svn st –q 查看本地修改的文件
2、对于makefile中的参数，可以直接make CC=gcc来改变它的值。
3、颜斌也发现了系统不能启动的问题。
4、写了个pc下的写卡测试so给东信和平的徐晓翔，他说要一周左右的时间。

2011-5-4
1、watchdog在drivers/watchdog/omap_wdt.c中，可以把它编译为模块，但貌似是重启几次之后，linux系统就再也不能启动了。

2011-5-3
1、开会，讨论无线键盘。
2、李柱栋：完成pscm接口。（是否测试了每个卡的位置？）
3、赵金：琢磨是否要对ini文件进行优化。
4、pppd运行了4天，貌似没有断线。但其他usb口仍然有报错。
5、联系徐晓翔，说要和领导商量。

2011	-4-29
1、run-parts：运行目录中的文件。

2011-4-28
1、李柱栋：从话机程序来看，发送数据必须按照先发前5个字节，再发后面的数据的格式来发送，就可以正确的接收了。张悦玲：这是在集团测试时，卡商要求的。从智能卡7816标准上有关于过程字节的描述。
2、赵金：身份证阅读器有乱码出现。
3、王博：使用天沐的uboot可以正常显示数据，但从svn拉下来的则不能。
4、万辉：升级采用的策略是，无论什么东西需要升级了，都将终端的版本升级1，并在发行的时候，根据现场有的最低版本，来制作差分包。每个插件版本号自行处理。

2011-4-27
1、上午开会，详细内容见文档。
2、赵金：密码键盘算mac似乎很慢，在windows下使用厂商自带的动态库则很快。

2011-4-26
1、李柱栋：使用minicom可以收到串口回环的数据，而自己的程序有问题。
2、赵金：密码键盘插psam卡还有问题。
3、王博：2.4G模块能够收发数据。跳频是两方约定一个频率，如果收不到，同时增加频段或减少频段值。
4、飞天的读卡器有一种可以在pc的linux下成功驱动，并读到reset后的数据。
5、这几天usb口都没有出现什么报错的信息。

2011-4-25
1、编译netfilter，修改了若干个文件。
2、李柱栋：测试sim卡操作部分。

2011-4-23
1、由于无法使用windows下的写卡组件，要使用linux下对pcsc的支持，linux下游pscs-lite和ccid对读卡器进行支持。

2011-4-22
1、网页的问题在于，对应cgi来说，只有printf来进行输出，这样输出的内容，就已经在网页的body中。除非可以解释网页body的内容，才可以把它们填充到相应的edit框中。还有一个方法是cgi完全控制输出，包括edit等等，这样一切都在程序中搞定了。
2、晚上模块报错了，早上重新装了一下，下午又开始报错。当报错时，底板完全关电再开电，能好一会，然后又继续报错。晚上重新焊了一下芯片。
3、赵金：调整刷卡的函数。
4、李柱栋：开始搞底板的卡控制。

2011-4-21
1、拨号后，每分钟ping一个包，运行约16小时，接收数据439.9k， 发送数据110.1k，无断线，无报错。
2、得到csq等后，在程序中使用setenv是无效的，貌似source也没有用。只有记录文件了。
3、李柱栋：文件管理器可以使用了，问题是文件没有图标显示。
4、王博，颜斌：刷卡器可以刷了。反刷有一定的失败概率。
5、刷卡器没有进行三方联调。
6、本地设置页面

2011-4-20
1、把原来在broadcom下没有写完的modem程序放到ti的平台上来，也可以编译，可以运行，修改后发送了at指令。
2、赵金、李柱栋和王博搬到了一起，方便交流。
3、赵金：上传了插件的代码。
4、李柱栋：修改触摸屏为鼠标，去掉屏幕校验，增加汉字打印字库。
5、王博：可以接收2.4g模块的数据了。
6、颜斌：有一块板usb总是会报错。
7、赵金：可以写一个程序，不断填充鼠标移动消息，就可以使得屏幕不黑了。

2011-4-19
1、可能会使用512M的flash，这样的系统对于x11来说很大了，对于gnome又小了些。
2、chat的参数：-t 超时时间
			   -f 脚本文件
			   -r 错误报告文件
               -s 把输出到stderr
               -v 执行状态输出。
3、可以使用dbus，让其他应用程序知道系统的连接状态。
   把/etc/里面的dbus去掉，让firefox直接按照系统的hal的消息给出在线状态。

2011-4-18
1、firefox调用插件会将参数字符串改为utf-8编码，比较奇怪现象。
2、打印机不正确打印中文的一种情况是文件系统中没有字库。
3、如果要操作GPIO，貌似一定要写驱动文件。
4、打印机三方联调完成。
5、刷卡器未进行三方调试。
6、linux内核中，文件大小写主要集中在netfilter相关目录中。
7、低板上的usb口和8880平台模块配合比较正常，比原来的有天壤之别，而且wget也能得到数据。
8、金浪的路由器串口只能看到数据，不能输入了。应该是硬件的原因。
9、打印机图形打印正常。

2011-4-15
1、李柱栋：做打印机图片部分。
2、赵金：打印机联调还有问题。
3、王博：修改u-boot显示图片未上传，等有屏的机器来测试，看2.4G模块资料。
4、sudo ssh –D0.0.0.0:8888 –N user@host实现转发。
5、8800平台模块通过otg的usb口可以正常连上，测试20次，每次都能出串口，也能进行at，拨号，可以ping出去了，但是不能使用wget得到页面。原来不能ping出去的原因是使用的是大唐lc6311的at指令。
6、龙尚的手持机则出现reset错误。

2011-4-14
1、awk  -F"=" /mylip/'{ print $2}' my.ini 这个指令从my.ini文件中得到mylip=hello后面的hello。
2、拨号脚本的制作，考虑在后台运行一个脚本，这个脚本首先检查配置，如果使用网卡联络网络，则直接退出，否则为一个while ture do … done循环。每1分钟执行一次。如果pppd进程不存在，则开始拨号，如果pppd进程存在，则没10分钟ping 一下dns，如果能ping通，则认为网络是通，否则认为不通，重新拨号。
3、终止一个脚本需要用：killall bash，在目标板上是killall sh。如果脚本的名称是testsh, 那么killall testsh是无效的。
4、m61,8800平台模块有6/10的概率可以找到串口，并且能够拨号，一切正常。但不能ping出去，包括ppp对端的地址。
5、pppd拨号后，要在/etc/ppp/ip-up.d/08setupdns中的ACTUALCONF改为/etc/resolv.conf，同样在/etc/ip-down.d/92removedns中作修改。
6、增加+++在拨号脚本中对拨号没有什么影响。
7、m28模块拨号后，如果拔掉usb线，也无法拨号了。
8、万辉：证书和ip绑定，如果服务器ip修改，那么全部终端都要手工点击一下才可以。

2011-4-13
1、李柱栋完成了制作只需要fat分区的生产mmc盘的制作。
2、李柱栋上传多了一个uboot，删掉。
3、万辉：使用wget得到自己制作的网站有问题，应该是制作证书的问题。
4、王博：刷卡器一次open只能刷一次。不是很合理。
5、给方舒做生产写mac工具的任务

2011-4-12
1、delphi可以通过一个activex library中放置多个activex form的方式来实现，具体来说就是一个activex form做为第一层接口，增加属性printer,key等，这些属性返回的是指向printer,key等的activex form，而这些activexform又有print等方法。
2、李柱栋：打印中文正常。
3、赵金，王博：刷卡器还未完全连调。
4、和模块厂家联系。现在薛东义正在处理这个问题。

2011-4-11
1、vc下似乎无法在ocx中实现ocxobj.printer.print这样的方式。

2011-4-9
1、文件系统貌似无法使用svn进行管理，不行就手工吧。

2011-4-8
1、讨论无线键盘的方案。

2011-4-7
1、李柱栋：打印机驱动中，write函数的实现有问题，不会被调用。
2、王博：刷卡数据正确了。
3、王博：第4串口能发不能收。
4、赵金：做网站要求的取本地参数的插件。
5、万辉：在起始页中完成自动升级本地文件的操作。
6、路由器不能枚举的问题在新的m61模块上也出现，m61模块在ti上不行，但在broadcom的路由器上可以正常枚举。
7、写PRM_RSTCTRL寄存器貌似不行，不能重新启动。Uboot中的reset汇编码貌似是操作这个寄存器的。

2011-4-2
1、打印机等外设写为.ko的方式，方便日后更新。
2、由插件直接操作设备驱动形成的设备文件，如果需要接口，由插件来调用ioctrl函数来实现。
3、路由器厂家仍然是设备不能枚举的问题。
4、王博，赵金：可以在页面上进行刷卡，但一轨和3轨的数据不正确。
5、李柱栋：打印机可以操作切刀，但读打印机状态不对。
6、自己做的路由器已经有硬件资料，但软件资料还没有通过对方公司的流程。
7、遥控键盘使用2.4g的无线模块。

2011-4-1
1从网站上下载的tar.gz文件也不能正常的tar出来，不过改用7z倒是可以解压为tar文件，再tar就可以了。从下面的链接来说这不算是个错误。
https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk58780
2、网站可以通过首页来进行空闲判断，考虑在本地web中增加一个cgi重启程序，当需要重启时，网站调用这个本地web。
3、貌似新的系统有没有跑起来的情况。
4、报错的tar.gz重新tar一下就不会报错了。
5、好像复制shutdown过去也不行了。
6、李柱栋打印机可以打印了，可以打印英文，还需要切刀的资料
7、angstrom系统制作中，build/conf/local.conf中的#DISTRO   = "angstrom-2008.1"已经过期，需要修改为DISTRO   = "angstrom-2010.x"。否则bitbake回有大量的报错，并且无法进行。
8、linux系统如果需要在串口出shell，要在/etc/inittab文件的最后一行加上：
S:2345:respawn:/sbin/getty 115200 ttyS2
这样就可以从串口进入shell了。

2011-3-31
1、u-boot代码中的reset貌似是正常的，它的reset在lib_arm/reseet.c中，只有两个函数：disable_interrupts和reset_cpu，reset_cpu这个函数貌似是在cpu/arm_crotexa8/omap3中的reset.S中，是一段汇编代码。
2、由于3715文件系统中的reboot是正常的，把3715文件系统中的reboot的最终链接sbin/shutdown.sysvinit复制到3517的系统中。貌似可以重启了，也不会报非法错，但要等半分钟左右，难道也是使用watchdog？
3、web是否能知道当前空闲？
4、oe进行更新后，不能bitbake了，难道是什么东东更新了？

2011-3-30
1、内核提交的时间真长。
2、制作uImage的脚本在内核的scripts/mkuboot.sh中，但貌似有些难懂，简单的把编译好的mkimage放到usr/bin中好了。
3、makefile中的.PHONY比较强大。
4、在使用modprobe之前，要使用depmod
5、王博确定了触摸屏的转换。
6、居然出现了网络操作系统不能启动的情况。
7、oe重新编译真不容易，一个晚上还没有编译完成。
8、李柱栋可以控制打印机了，但是会复位。
9、内核文件存在用大小写区分的文件，所以在windows平台上无法下载下来。

2011-3-29
1、plm开会
2、自己编译的x-load和天漠提供的大小不相同，也不知道是啥原因。
3、u-boot开始显示的时间是在Makefile中，由date命令来写一个timestamp-autogenerated.h来完成的。
4、李柱栋可以写gpmc控制寄存器了，但操作io貌似还有问题。

2011-3-28
1、在使用nfs作为文件系统的情况下，貌似不能使用watchdog来重启了。
2、u-boot中的版本号有特殊字符。

2011-3-26
1、写任务分配表。

2011-3-25
1、#cmd 2>error_file 把错误输出定向到错误文件
   #cmd >output_file 2>errorfile 分别定向
   #cmd >output_file 2>&1 全部输出到output_file中。
2、赵金将字体选项改为中文字体后，matchbox的桌面图标可以显示中文。貌似没有文件管理器。
3、gtk3貌似要装的东西比较多。

2011-3-24
1、可以在matchbox中桌面上增加文件夹，但不能是中文。
2、使用query进行了一晚上的测试，没有发现问题
3、底板声音有，但有破音，好在使用缴费终端原来录制的声音不是非常明显。
4、底板网口ping正常。
5、新的lcd显示正常了，硬件上接反了线，通过软件设置后可以调整。
6、在linux启动参数中增加eth=xx:xx….可以利用u-boot中的参数来设置网卡的MAC，在Board-am3517evm.c (arch\arm\mach-omap2):__setup("eth=", eth_addr_setup);中有实现的方法。
7、在rc6.d中增加一个脚本，cat /dev/watchdog，就可以实行reboot后用看门狗来实现重新启动。

2011-3-23
1、外壳样子出来了，陈总提出要有按键，并去掉触摸屏，减少故障率。颜斌认为不需要在打印板上增加usb口，要使用鼠标键盘直接开面板。
2、yaffs2的速度要快一些，而且没有看到报错的信息。
3、可以使用wget直接来得到网站内容，而post的数据可以使用—post-data参数来完成。Busybox所带的wget由于当前系统采用的busybox使用的是较老的版本，不支持—post-data参数。
4、需要考虑对时功能。要测试板子上的实时钟是否准确。
5、在号码输入的网页中，需要有暗码可以进入本地数据查看和工程模式，进行维护。
6、没有找到可以把mac地址传入的linux启动选项，还要再找。
7、威盛是via technologies ，在ieee申请的mac是00-1f-f2。
8、赵金修改了/etc/matchbox/session文件，把firefox加在里面，并在后面在加上matchbox的桌面执行程序，貌似现在是正常开机即启动firefox。
9、新的屏可以看见东西了，但颜色和位置貌似有问题。

2011-3-22
1、PLM（产品周期管理？）第一次会议，确定人员安排。
2、需要做一个外接键盘输入设备，这个设备有键盘和小的液晶，带fsk发送和接收模块，当店内的挂墙设备老板给其他人代收钱时，使用这个设备进行输入号码和金额，设备将号码、金额数据加密后发送到挂墙设备，挂墙终端有服务进程监听，收到数据后，调用firefox，但不显示页面，向服务器发送页面请求数据，并将结果返回到手持设备。服务器收到请求后向boss发起现金缴费请求。结算方面是挂墙终端有工号，同营业厅终端收费方式。
3、李柱栋制作一张mmc卡就完成所有的flash操作。
4、赵金启动firefox还有问题，启动firefox后，可能会导致linux的matchbox无法启动。
5、lcd板还有问题。
6、web方面，李瑶做连接池，页面等部分，万辉做业务部分，唐凯凯（？）则做数据库连接部分。
8、新疆中标370多台，上海中标占了大头。

2011-3-21
1、yaffs2通过了3天的压力测试。这个系统有一个问题是如果是在没有umount的情况下关机，那么下次启动就需要用20多秒的时间来重新扫描。
2、网页方面原来是要使用静态网页来完成，应该使用jsp更加方便一些。

2011-3-18
任务：
赵金：给出刷卡器的接口文档给王博。
      给出写firefox插件的文档给方舒。
	  验证yaff的使用。
      在x11环境如何直接启动firefox，以及如何在matchbox上增加一个图标。还有声音的测试。

王博：按照刷卡器的接口文档写出刷卡器的接口。
	  新lcd的接口。

李柱栋：写成yaff移植的文档
      制作mmc卡，实现一卡完成对新的机器flash的无人工干预的自动完成，包括：uboot部分：写x-loader,uboot,uboot参数，内核，启动内核。内核部分：加载yaffs文件系统，格式化，写根文件系统。
      写cpld方面的驱动，包括打印机和读写智能卡。
	  设置程序：IP设置，是否使用3G拨号，apn，ip，是否使用代理。
	  Linux如何直接设置mac地址。

万辉：给出表结构
	  完成业务部分的功能

李瑶：完成连接池等功能。

2011-3-17
1、注册mac地址，http://standards.ieee.org/develop/regauth/oui/index.html， 注册费1750美元。有2^24=1677,7216个地址可用。
2、换了大电池，实时钟有时候能正常显示。
3、mac是个随机值，要写在什么地方还要考虑。
4、把gnome系统中的所有/usr/share/fonts目录下复制到x11的系统中，firefox就可以显示大字体了。
5、把CONFIG1_0这个寄存器的最后两位改为0,1,2,3，系统都会在进行sqlite压力测试中崩溃。
6、在linux系统启动后，挂载flash中的yaffs2系统是可以成功挂载，复制根文件系统后也能正常启动。但是进行sqlite压力测试后文件系统还是崩溃了。
7、firefox可以使用splash扩展，但这个扩展貌似关闭后5秒后firefox的窗口才能显示。修改/usr/bin/firefox这个脚本，在其中加入psplash显示，并通过（sleep XX, pasplash_wait ‘quit’）& 是可以基本实现splash关闭后firefox窗口就显示的目的。

2011-3-16
1、firefox有splash插件，还要试
2、3517使用gpmc作为nand的接口。
3、可以使用umount 目录 来卸载设备，而umount /dev/xxx 这样的方式在一个设备有多次mount时会报错。
4、reboot不正确。
5、使用elite pro 2gb的MMC卡进行sqlite测试，一晚上写了21万记录，貌似还没有报错。而用nand测试，只有ti提供的3715开发板能通过测试。
6、实时钟总是报电压低，小电池可能还是有问题。

2011-3-15
1、x11的系统中，浏览器字体无法变大。
2、模块先+++貌似不会回error之类的东西。

2011-3-14
有ubi_eba_init_scan: cannot reserve enough PEBs for bad PEB handling这样的警告。

uboot下，用 “nand erase clean 其他参数”能删掉部分假的坏块

2011-3-13
Ubi系统复制了一些文件后，有时会崩溃。

2011-3-12
将linux 启动参数中的console改为ttys0，linux启动时就把信息打到lcd屏幕上去了。

2011-3-11
去掉ubi系统内的将ubi转为只读的代码，ubi就可以一次进入，貌似没有什么问题。

王博在u-boot增加显示屏的代码，将屏边绿，但是貌似速度很慢。

Vsftpd增加用户：
1、修改/home/loguser.txt，增加用户名和密码
2、sudo db4.6_load -T -t hash -f /home/loguser.txt /etc/vsftpd_login.db
3、sudo chmod 600 /etc/vsftpd_login.db
4、cd /home/ftp
5、sudo mkdir xxx
6、sudo chown virtual:virtual xxx
7、sudo chmod 777
8、cd /etc/vsftpd_user_conf
9、sudo cp wuhao xxx
10、sudo vim xxx 修改其根目录
11、sudo /etc/init.d/vsftpd restart

2011-3-10
MMC卡座没有接地，所以系统认为mmc为只读状态，这样就不能从mmc mount文件系统了。

李柱栋移植yaff2，内核增加了yaff2支持，但写文件系统有问题，估计还要改u-boot。

需要测试u-boot，可以这样：
1、	把编译好的u-boot放在tftp服务器目录中
2、	在目标板输入：
tftp  81000000 u-boot.bin
go 81000000
就可以运行新的u-boot了。

2009-9-16
机器居然出了问题，只好再次重新安装。

江苏出现的是svchost.exe这个东西报错，报错后，如果点确定，还可以使用，如果点取消，则无反应。一般是直接关机。

贵州的机器现在有4台出现死机模样的问题。同样的主板已经出了较多，所以张伟不认为是主板的问题。

2009-9-14
方舒在沧州，现在遇到的问题有两个：
1、吃了一张钱后，codecash识币器变红，不再吃币，后来发现时卡币了，但界面似乎没有报错。
2、现在发卡器似乎无法发卡，而这个问题在任开元在的时候，貌似没有怎么出现。

贵州现有问题：
1、死机问题，一段时间不动后，点缴费无反应，界面的gif也不动了

江苏问题：
1、出现过一个人交费2张纸币，但只交了第一张，第二张却在下一个交费的人体现。
2、打印错误，无法打印，但退回一步后能正常。
3、出现非法错误，已经发给赵金分析。

2009-9-12
山东电信要开始上收费终端，似乎很难做。
如果使用web方式，看来必须使用java来做了。

2009-9-3
直接操作ps/2端口去查询键盘，可以检测键盘了。
2009-9-2
snmpd貌似可以运行，开始找判断键盘是否正常工作的函数，无果。
2009-9-1
继续看snmp的相关资料。
2009-8-30
找了一些snmp的资料。
2009-8-29
回深圳。
2009-8-28
上午测试了天腾的读卡器，发现读了若干张后就会错误，原来是程序发现错误后关闭了串口。
2009-8-27
折腾了一天的天翼读卡器，让它可以连续读卡，貌似是它的禁止进卡指令不能发送，否则就会死掉。
但问题是它有一张银联卡读错误。
2009-8-26
开始测试了，天翼的读卡器如果连续发允许进卡指令，那么就会把卡不断重复进、出的动作。
密码键盘的解密函数居然是个空指针，差了很久。
2009-8-25
飞到北京，其实西绒线胡同离开大巴站很近，可以走到。
2009-8-24
看snmp的资料
2009-8-23
要让ocx中再加入一个ocx，可以再ocx中增加一个对话框，将ocx放在这个对话框上，在这个对话框的构造函数中增加AfxEnableControlContainer();需要的时候,
ocx_dialog *ox = new ocx_dialog;
    //ox->DoModal();
    ox->Create(IDD_DIALOG1,this);
    ox->ShowWindow(9);
就可以实例化对话框了。


2009-9-3
使用无线网络复制文件时，会死掉。
httpd进程莫名其妙的消失了。
路由器重新启动过一次。在把笔记本的ubuntu进行升级的时候。
2009-8-24
今天又出现了可用内存到达4m的情况，路由器已经运行了4天，之前无线部分是关的，只是开了，就成了这样的情况了：
# free
              total         used         free       shared      buffers
  Mem:        13348         8416         4932            0          996
 Swap:            0            0            0
Total:        13348         8416         4932
2009-8-17
去掉linux中ipmi支持。
2009-8-14
试图使用最新的busybox，成功的编译了，但是insmod却没有找到其需要加载的库，可能是路径设置的问题。
2009-8-13
如果在busybox中配置
（1）busybox的配置
    对Telnetd的配置部分：
Networking Utilities --->
telnetd
  Support standalone telnetd (not inetd only)
linux中加入Device Drivers->Character devices->Unix98 PTY support (UNIX98_PTYS)启动后运行
＃cd /dev
# mkdir pts
# mount -t devpts devpts /dev/pts
# telnetd
这样，从其他机器就可以telnet 登录上去了。注意如果在busybox中增加login，那么就会出login提示，而无法登录。
2009-8-12
vsftpd只能上传不能删除问题
vsftpd.conf加上anon_other_write_enable=YES
虚拟用户如何实现 , 上传的文件权限为 777这样，就可以直接在资源管理器中拖拽了
2009-8-11
看《构建嵌入式linux系统》
去掉Support for Intel/Sharp flash chips,Support for AMD/Fujitsu flash chips,Support for ST (Advanced Architecture) flash chips三个选项。
2009-8-10
试图让gprs上网的灯和局域网的灯一样闪，看来有些困难。
2009-8-6
只需要安装一下manpages-dev就可以了man函数的帮助了。
udhcpd中，很晚的版本才出现hostname，而在broadcom中的另外一个版本中，则出现了hostname，但是没有static_leases，最终使用busybox中的版本，加上hostname，又参考最新的busybox中的程序，修改了static_leases的IP不能显示hostname的情况这个bug。
2009-8-5
这次安装nxserver非常奇怪，没有中文输入法了，后来发现，开一个终端窗口，运行scim就可以了，非常奇怪的现象。
安装csftpd了，配置方法基本参考这个文档：Vsftpd虚拟用户设置
2009-8-4
忙碌的一天，安装了服务器，看了移动的新标准。
2009-7-31
去掉了linux中Enable futex support选项，看看会有什么样的情况。很快就出现了Disable IRQ ＃6了，关于Enable futex support的一篇文章
2009-7-30
忽略了一个MAKE中的错误，让库优化可以继续，现在看来，貌似没有发现什么问题。
2009-7-29
花生壳貌似只要在内网的一台计算机上安装就可以解析了。
2009-7-14
sdram_init要改为0x000a，这样才能使用16m内存。
2009-7-9
发送短消息出现问题：
+CMS ERROR: 96
+HTCERROR: d,60
根据文档：
Cause no. 96: "Invalid mandatory information".
      This cause indicates that the equipment sending this cause has received a message with non‑semantical mandatory information element errors.
不是很明白。
2009-6-24
man xxx|col -b>outfile 这样可以把man中的内容打印下来，不过这样列宽似乎是和当时的终端窗口列宽是一样的。
我现在使用的域名过滤和这篇文章一样，但是他的dns53端口转向似乎没有作用。
2009-6-23
去掉了udev/test目录中的一些文件，这样在windows下也可以完整的cvs下来全部的程序了。但仍然有一个问题，linux下的cvsd似乎并不区分什么文本格式和bin格式，通通是文本格式，虽然有些文件显然是二进制文件，在linux这似乎不成什么问题，而如果使用windows客户端，则会在\r后面自动加上\n，或者相反，总之会加点东西，这对于二进制文件是致命的，有问题的。
似乎只要在filter表中增加一个forward链规则就可以阻止对某些ip的访问，那么允许呢？似乎就有些问题了。
2009-6-22
从上个周末开始，路由器应该是比较稳定了，貌似还没有死掉过。
2009-6-18
今天发现奇怪的事情，首先是75这台机器死掉了，强制关机后，nxserver也照样留下了一个僵尸连接，这次从其他机器却不能终止它，不过/usr/NX/bin/nxserver --shutdown后，就可以在客户端的admin界面中删掉它了。
2009-6-17
增加了一些网页。
2009-6-16
syslogd -R 192.168.1.74 就可以把syslogd的信息发送出来，不必写在/var/log中了。但是似乎指定了ip后，并没有自动启动syslogd。
在任何失败后，pppd都不会自动退出，也不知道是什么原因，算了，在定时器里面来杀死它吧。
2009-6-15
找到了一个source insight的绿色版，再加上wine，就可以在linux中使用source insight了。
如果要禁止访问某些网外的ip，似乎只要这样就可以了：
iptables -t nat -A POSTROUTING -d 220.162.247.149 -j DROP，这样，这个地址就无法访问了。
2009-6-12
77的共控机硬盘完蛋了，只好在55上重新建立cvs了。
find $(TARGETDIR) -name .cvsignore | xargs cvs add 这个指令真是方便啊。
2009-6-11
按需拨号也很简单，只要加一个demand就可以了。
2009-6-8
一个submit的按钮必须加上 class="button" 这个属性后，才能显示css中button对应的样子。而在css中加入input.submit这样的东西是没有用的。
2009-6-5
为什么局域网的静态路由表就没办法修改正确呢？真是奇怪阿。怎么都不对，先不管了。那个多播的设置，页面内容也写到了程序中，非常搞笑，算了，不管了。
在脚本中加入 set -x可以显示命令本身。
2009-6-4
把wan设置中的东西基本上加进去了。
broadcom中，局域网部分也有静态路由表，这个表就不知道有什么作用了。
在lc6311没有起来的情况下，由于不断的拨号，板子上的进程id号增加的很快，一天多下来已经到了17000了。
2009-6-3
加入Load all symbols for debugging/ksymoops这个选项试试。
把板子该成了内网地址后，传程序成了问题，来试试端口映射能不能做到。貌似没有什么反应。
<input type="hidden" name="wan_desc" value="<% nvram_get("wan_desc"); %>">
<div style="display:none;"><select name="wan_ifname" ><% wan_iflist(); %></select></div>
这两个句子分别对网页上的input 和select 进行隐藏。
现在来改边wan为dhcp方式。将135的dhcp打开，并只分配1个地址192.168.1.1吧。
broadcom的释放似乎没有真正释放，地址仍然是原来的地址，当然在dhcp服务器上显示的确实是消失了。
对于radio这样的input，如果没有选择他，那么在post中，是没有它的选项的，这样对于wan_pppoe这个网页，就有些复杂了。又要加上一些看不见的radio了。
2009-6-2
加上了swap，跑一个晚上看来还在坚持。
tplink中wan设置的网页应该是引导网页，在其每个页面设置的网页中，都不是跳转到左边给的连结。
使用一个简单的脚本，就可以实现网页自动转向需要的网页：
<html>
<head>
<script language="JavaScript" type="text/javascript">
<!--
function choseWanPage()
{
    var wan_proto = "<% nvram_get("wan_proto"); %>";

    if(wan_proto == "dhcp")
        location.href = "wan_dhcp.asp";
    else if(wan_proto == "static")
        location.href = "wan_static"
    else if(wan_proto == "pppoe")
        location.href = "wan_pppoe.asp";
    else if(wan_proto == "disabled")
        location.href = "wan_disabled.asp";
}
//-->
</script>
</head>
<body onload="choseWanPage()">

</body>
</html>
linux下现在有一个aolnweb提供vpn服务，使用其服务参见http://www.alonweb.com/node/3
然后：sudo /etc/init.d/openvpn stop结束服务
奇怪，今天再看dhcp的服务列表中，其过期时间就是对的了。
wan口的地址修改现在也是只能看，不能改。应该是少了第一个条件，什么connnection的。加上了，还是有问题，要使用包捕获的方式来看看了。
改一下程序，如果存在/tmp/www目录，那么httpd就在/tmp/www目录启动，如果不存在，就在/tzwww启动，这样可以少输入一些指令。如果判断一个目录是否存在呢？现看看chdir这个函数。这个函数如果返回0表示正常执行了，－1表示没有正确执行。
2009-6-1
晚上又出现了disabling irq的事情，而且内存增加到4m似乎没有那么容易复现了。
现在去掉cfi支持看看会有什么情况出现，刚刚下载的时候死掉了，复位后现在貌似还好.但是后来似乎死过若干次。
dhcp列表是显示了，但是立即就过期了，不知道是什么地方的原因。
是不是打开了dhcp server就很容易死掉？
wan的设置实际上有多个界面来处理，由于选择不同而出现不同的页面，broadcom是采用disable的方式来进行处理的，显然不是很方便，而tplink则使用不同的网页。似乎三个页面的切换也不是很难，但是对于menu来说，应该调用哪个页面才合适呢？这就是一个问题，还有一种方法就是再分一个frame，这样就比较简单了，不过这样，就需要更多个wan的页面文件了。就这么做吧，还有一些通用的设置需要在每个页面出现。
现在看来更象是哪个swap的问题，增加了它好像就不容易死掉了。
2009-5-31
这3天看来是停电了，所以也无法知道这3天的运行情况。
为什么时区的选择就能够保存，而ntpserver这些edit中的数据就不能保存了呢？现在也没有找到时区是在什么地方保存的。
如果多重新启动几次httpd，就很容易出现disbling irq的错误，不够也许今天是因为我没有打开lc6311，使得系统在不断地拨号的缘故？
时间设置忠的ntp server终于可以使用了，原因是必须把net_server这个变量要先设置，才可以设置net_server0这些变量，为什么每次都要这样设置呢？真是奇怪。
而局域网部分，可能是if_name之类的变量没有设置。要把原来的网页中的javascript脚本看看设置了一些什么样的变量。那么加上lan_ifname和lan1_ifname这两个变量后，貌似就可以修改了。
现在的文件大小是3608576。现在手工修改了一下linux的.config，去掉了其中的ehci支持。如果是选择，那么直接这两个选项就已经选择了。去掉了如果没有完全重新编译，文件的大小没有改变，但是可用内存一下子增加了很多，虽然在刚启动是也是1.6M左右，但一会儿后居然到了4M。应该不是这个原因，因为.config自动恢复了原样。是不是我没有修改它？
udhcpc -i eth0 ....这个进程难道不能杀死，多设置一次lan方面的参数就多一个在运行？
2009-5-23
再次出现了21日的那种串口无响应的情况，奇怪了。
在busybox中加入了ftpget和tar，这样，就可以在pc下编辑好网页，打包，在板子上下载，解包，还是比较方便的，比起每次重新编译，下载要方便多了。
2009-5-22
如何在ubuntu中加入ftp server FTP Server on ubuntu
如果改变了linux的选择，还是很有可能会出现死机的情况的，比如去掉了kernel .config support和prompt for developemnt and/or imcomplete code.deivers。
找到了一个叫做sdmenu的脚步，他的菜单貌似符合我的要求。
2009-5-21
今天的现象非常奇怪，开发板的其他功能似乎正常，web也能访问，td也在网，iptables工作也正常，能通过这个板子ping出去，但是串口不通了。奇怪的是75这台机器也停止了响应。
广西的维护人员打电话来说原来的那种插卡话机会出现无来电显示的情况，而且1，0等数字也会显示消失，奇怪的事情。
tplink路由器的网页菜单使用了...html?dd=ss这样的形式，这样，它后面的解析器应该是比较复杂的。
2009-5-15
仔细查看usb/core下面linux2.6.28的最新代码，还是算了，不修改那么多了，先只修改一点点用吧。
2009-5-14
找到所有某种文件并且删除他们：
find . -type d -name ".svn"|xargs rm -rf
在cvs 做import时，最后的两个参数一定要加，加上的结果是建立了第一参数的分支，建立了第二个参数的标签，不知道其设计者一定要这样做的理由。
ls -R 列出子目录中的内容。
如果不修改usb部分的代码，现在的程序上网后是必死的。
2009-5-13
似乎/tmp/下的ip-up，if-down并没有得到运行。

如果加入lc6311的初始化代码到cmtc-isp文件中，其初始化代码能得到执行，但是貌似就不能上网了。也许是由于at^dsq=0这个指令无法执行？也许可以单独写一个脚本，由chat单独运行一下看看是什么结果。
如果要pppd自动断开，试试在cmnet中加入nopersist试试是什么情况。不行，nopersist是默认的情况。
修改了pppd中在线时间统计的错误。pppd中在线时间统计错误
终于在ubuntu中安装了cvsd，有一些麻烦的地方。参看在ubuntu 9.04中安装cvsd。然后在客户端使用：
cvs -d :pserver:jl@192.168.1.77:/router import -m "first" -I ! src src initial创建一个新模块
cvs -d :pserver:jl@192.168.1.77:/router import -m "first" -I ! src src initial取出该模块
可以使用
CVSROOT=:pserver:jl@192.168.1.77:/router
export CVSROOT
来简化输入。

2009-5-12
从
http://www.linuxsir.org/bbs/thread229926.html
其中的这段描述：
You MUST disable the lines that give values for lcp-echo-interval and lcp-echo-failure or your connection will always terminate (eg after two minutes). It appears that GPRS providers do not reply to lcp echo requests but pppd normally uses these to determine if the connection is still good.
这样，就无法判断ppp是否是完好的？
以上判断应该是错误的，至少现在中国移动网络支持lcp-echo-interval and lcp-echo-failure，昨天犯了个愚蠢的错误，两个都是lcp-echo-interval了，这样当然不会自己断线了。现在的问题是虽然ppp0会消失，但是pppd并没有从进程中消失。貌似只有killall pppd来消灭它。从man中说，当ip-down,ip-up时，pppd会分别调用/etc/ppp/下面的两个同名脚本，从一上网就开始去取时间来看，貌似确实是这样的。不过板子调用的是/tmp/ppp这个目录下的，而这个目录下的这两个文件，又是链接到rc上的。
国家授时中心服务器的IP地址是(210.72.145.44)
2009-5-11
终于设置好了nxserver，设置的过程在nxserver的安装 这个文档中，终于可以不用vnc这样的工具了，速度就和本机操作一样了。
在cmnet文件中设置了moden, lcp-echo-interval 1,lcp-echo-interval 10等内容，但是并没有如同想象的那样，pppd会去自动判断是否断线而自动退出和断开ppp0。不貌似不那么容易断线了。
在3322.org上申请了一个动态的dns，jianl.3322.org，但是3322提供的linux客户端ez-ipudate必须指定网卡，对于公司这样的上网方式显然无法实现，而lynx这个命令也消失了。还有一个这样的指令可以完成这个功能：
wget "http://username:password@members.3322.org/dyndns/update?system=dyndns&hostname=yourhost.ourdomain.ext&myip=ipaddress&wildcard=OFF"
其中username,password,yourhost.ourdomain.exe要根据情况修改。
2009-5-9
下载了openwrt，编译都用了一天的时间，虽然在目标板上可以运行，但是总是重新启动，我猜可能是因为flash支持不对的原因。
再次对busybox进行了一点裁减，去掉了telnet,telnetd,clear,reset,rdate这些功能。
2009-5-8
折腾了一下freenx，但是总是连接失败，还是先算了。
broadcom中的时区设置的值非常奇怪的，按照wiki百科中关于时区 的描述，时区的写法应该非常简单，utc+n或者utc-n。中国全境使用utc+8。而broadcom使用的如同PST8PDT这样奇怪的时区描述，这些描述在这里可以找到Time Zone Table Oracle，不知道这些是什么时代遗留产物。
如果重新设置了时区，那么netconf_add_nat函数设置的转发就无效了，需要重新设置一下才可以，估计是broadcom重新设置了一下所有的参数。
2009-5-7
ubuntu重新启动的时候还会检查显示器，这样对于没有显示器的机器似乎就不太友好了。
使用netconf_add_nat函数就可以完成类似iptables命令行
iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE这样的功能。
有时候还是会死掉，真奇怪阿，难道要把usb整个换掉？
ubuntu启动的时候一定要接好显示器，否则就不起来，这样，设置了自动登录也是枉然。
2009-5-6
s这个脚本可以实现tftp的自动上传，不用再敲那么多的键盘了。
#cat s
cd mipsel-uclibc
tftp 192.168.1.1 << END
bin
put linux.trx
END

2009-5-5
按照这篇文章修改后，usb似乎好了点，试了几次，即使加上usb2.0支持，还没有碰到死掉的情况。
USB: fix interrupt disabling..
upnp实际上是一个自动的端口转发的机制，如果路由器打开了upnp，那么内网计算机的的应用程序，主要是p2p的应用程序，就可以在路由器上自动设置响应的端口转发，这样，这些应用程序就仿佛在外网上一样，而且这个过程是自动的，不需要做固定的端口映射。经过测试，如果打开了upnp，打开emule的upnp功能，那么emule就能成为高id，在路由器的upnp界面上也能看到emule设置的端口转发。很多程序都有upnp功能，bt,迅雷，msn,skype都具备，qq似乎没有。
看了一下dnsmasq，这个东东应该已经可以进行dns转发了，把网关设置成路由器地址，确实又可以进行dns解析，原来为什么不可以呢？奇怪。
路由器所有的进程貌似是重preinit这个进程开始的，而这里把preinit重新定向到了rc这个程序。
这些板子的MAC地址貌似相同，如果插到同一个局域网中，就会出乱子，即使ip不同。所以，要修改一下他们的地址比较好。
2009-5-4
如果把usb2.0的选项和其子选项3个都选上，测试的结果是：
自动复位 3次，断网10次，死机2次。
2009-4-30
仍然有一次死掉的情况出现，如果不启动syslogd，那么只出现过一次。
也许这个网页给出的是解决方案：http://lkml.org/lkml/2008/6/30/365
2009-4.29
使用v1.03版本的程序似乎会重新启动，比后面的要好一点，后面的直接死掉。难道是编译进入的ppp有问题？在pc上pc当然不会死掉或重新启动。
应该是因为选择了这个选项 EHCI HCD (USB 2.0) support的原因，去掉后，虽然上网一段时间后仍然会莫名其妙的断掉，但是路由器还没有出现死掉的情况。
linux 中查找文件内容：
grep   who   /use/local   -r
  who是pattern，如果含有特殊字符则要加上引号。
  /usr/local是local，
  -r   是option，表示所有的文件，且对子目录递归。
 Create deprecated sysfs files 这一项是否选择貌似不重要，编译和字节数相同。
万辉在make new module的时候，cvs常会给他一些新的，其他目录下的文件，这个cvs真的问题不少。
公司驱逐所有在天安宿舍的员工，原因是住在一起的人吵架吵得厉害。原来吵得疯了一个，最近一次又闹到所有公司的上层。居然有这样的事情发生。李忠就说是素质问题，提议要进公司的，先背诵了子弟规再说。
2009-4-28
经过精简的程序终于可以加上iptables，经过一个简单的设置指令
iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE
就可以实现带其他机器上网，但是dns似乎必须还要设置为移动的dns:211.136.112.50，否则dns无法实现。
拨号有时候会死掉，现在原因待查。
2009-4-25
如果在网页中设置了broadcom中的syslogd的IP和connection loging，而又没有在控制台打开syslogd，那么pppd call cmnet 将会使得它死掉。
只要拨号上过网，这个路由器就能更新时间，不过不是北京时间。
2009-4-24
配置了一下ubuntu的syslogd，时期能接受外部的数据，配置参见文档将Ubuntu配置成syslog服务器接收外部日志，但是有两个问题，首先是broadcom这个板子貌似没有发送任何数据，另外如果使用其他的udp发送程序，就是没有记录到firewall.log中，而是记录到了messages.log中。
王伍说他以前使用的是ipchains这个工具来实现路由功能，但这个工具不知道在broadcom上对应的是什么，而且在现有的ubuntu上，也没有这个工具。
从putty这个工具的源码来看，它似乎没有用任何的资源工具来做窗口，难道完全是用api来实现窗口的？
李忠发现我的miniterm和超级终端的的表现行为还有所不同，其实应该差不多，只不过我的输入命令加的是回车换行，而超级终端默认只加回车。
2009.4.23
打电话给涂柯，他说一定要有usbserial.ko库，才能驱动大唐模块的usb。
修改文件../linux/linux-2.6/drivers/usb/serial/generic.c中的
//#static __u16 vendor  = 0x05f9;
//#static __u16 product = 0xffff;
static __u16 vendor  = 0x1ab7;
static __u16 product = 0x6000;
这样，就可以识别大唐模块lc6311的usb口，并在/dev下产生6个ttyUSB*设备了。
如果把usbserial部分编译为模块的方式，那么就可以使用指令
insmod usbserial vendor=0x1ab7 product=0x6000来识别，从dmesg命令来看，确实正确的识别了，但是在/dev下，并没有产生ttyUSB设备。

修改ppp/Makefile
$(ETCDIR)/chap-secrets:
        $(INSTALL) -c -m 600 etc.ppp/chap-secrets $@
增加以下几行
        mkdir -p $(ETCDIR)/peers/
        mkdir -p $(ETCDIR)/chat/
        $(INSTALL) -c -m 600 etc.ppp/resolv.conf $(ETCDIR)/../resolv.conf
        $(INSTALL) -c -m 600 etc.ppp/cmnet $(ETCDIR)/peers/cmnet
        $(INSTALL) -c -m 600 etc.ppp/cmtc-isp $(ETCDIR)/chat/cmtc-isp
重新make install，这样这几个配置文件就会合并在linux.trx中。这几个文件的内容参见大唐提供的文档ppp_desc_Linux_USB.txt
然而，和PC上的目录不同，配置文件是保持在/tmp目录中，而不是/etc目录中，还要找一下怎么把文件放到目标板的/tmp中。所以，要在目标板上执行以下命令：
cp /etc/resolv.conf /tmp/
mkdir -p /tmp/ppp/peers
cp /etc/ppp/peers/cmnet /tmp/ppp/peers/
这样，再执行pppd call cmnet，就可以上网了。可以ping www.163.com。
如果打开syslogd，那么，就可以再/var/log/messages中看到日志。

奇怪的问题：现在目标文件有 3813376，使用tftp的时候，总是传送到3800多的时候终止了，如果复位目标板，那么就起不来了，只有再传一次才能成功的传送。每次必然如此。而且联想的机器传送几次后就必须重启才能再传，否则每次都time out。只好到本机的windows下来传。

李忠说这两天在徘徊，是把原来的话机程序直接搬还是从头重写。

彭广才对多普达的hd心仪已久，看见严斌的新手机，心里痒痒的。
2009.4.22
vim指令：y复制 p 粘贴 jhkl移动光标，u是undo
linux中的ppp支持似乎只是内核支持了ppp，而并没有再带上pppd和chat。broadcom系统中没有在配置中加入对pppd,chat的支持，但是在ppp目录中带有一份貌似完整的ppp软件包。
要增加ppp支持和libdl，所以要在router menuconfig中：
 Additional C libraries  --->
         [*] libdl
在linux内核的menuconfig中，ppp相关部分能加上的先都加上
 Device Drivers  --->
     Network device support  --->

  x x    <*>   PPP (point-to-point protocol) support                      x x
  x x    [*]     PPP multilink support (EXPERIMENTAL)                     x x
  x x    [*]     PPP filtering                                            x x
  x x    <*>     PPP support for async serial ports                       x x
  x x    <*>     PPP support for sync tty ports                           x x
  x x    <*>     PPP Deflate compression                                  x x
  x x    <*>     PPP BSD-Compress compression                             x x
  x x    <*>     PPP MPPE compression (encryption) (EXPERIMENTAL)         x x
  x x    <*>     PPP over Ethernet (EXPERIMENTAL)                         x x
  x x    <*>   SLIP (serial line) support                                 x x
  x x    [*]     CSLIP compressed headers                                 x x
  x x    [*]   Keepalive and linefill                                     x x
  x x    [*]   Six bit SLIP encapsulation

修改src/router/Makefile文件：
        $(MAKE) -C ppp/pppoecd $* INSTALLDIR=$(INSTALLDIR)/ppp
注释掉，增加一条
        $(MAKE) -C ppp $* INSTALLDIR=$(INSTALLDIR)/ppp
这样编译整个ppp，而不仅仅是pppoecd部分
运行ppp/configure，生成ppp部分的makefile文件
vim ppp/pppd/plugins/pppoe/pppoe.c 在193行最后增加一个\
vim ppp/pppd/plugins/pppoe/pppoehash.c
vim ppp/pppd/plugins/pppoe/pppoe_client.c
vim ppp/pppd/plugins/pppoe/libpppoe.c
这几个文件的#include <pppoe.h> 改成#include "pppoe.h"
修改ppp/Makefile文件，增加一行：
DESTDIR = $(INSTALLDIR)
将install: 后面的$(MANDIR)/man8 去掉
vim ppp/pppd/plugins/Makefile
将LIBDIR  = /usr/lib/pppd 改为LIBDIR  = $(INSTALLDIR)/usr/lib/pppd
vim ppp/chat/Makefile
 vim ppp/pppd/Makefile
vim ppp/pppdump/Makefile
vim ppp/pppstats/Makefile
这几个文件将$(INSTALL) -c 后面的-s去掉，并加上类似
$(STRIP) $(BINDIR)/pppd/pppd
将有关man的部分注释掉
如果install 后面有-o，-g之类的参数也去掉。
这样就可以make,make install 就可以编译一个带有pppd和chat的router。

2009.4.21
Gentoo Linux USB指南(http://www.gentoo.org/doc/zh_cn/usb-guide.xml)这份文档不错，根据这份文档的说明对linux中的各个选项加以选择：
现在选择了以下的条目：
Device Drivers  --->
     USB support  --->
             <*> Support for Host-side USB
            [*]   USB device class-devices (DEPRECATED)
             <*>   EHCI HCD (USB 2.0) support
             <*>   OHCI HCD support
            <*>   UHCI HCD (most Intel and VIA) support
            [*] USB Monitor
            USB Serial Converter support  --->
                    <*> USB Serial Converter support
                    [*]   USB Generic Serial Driver
                    <*>   USB CP2101 UART Bridge Controller
                    <*>   USB Prolific 2303 Single Port Serial Driver
这样，如果启动的时候将大唐开发板或者使用Prolific 芯片的转串口的设备，在/dev中就会增加ttyUSB0这个设备。
如果选择了usb的存储设备，加上一些文件系统的支持后，插上mmc转为u盘，清华紫光的U盘，都会报错，而插入nokia 6120c不会报错，并正确的识别了厂商，磁盘大小等信息，但并没有在/dev中增加一个sda设备。

busybox进行配置后，配置的文件在busybox-1.x/.config中，而编译时，每次都从busybox-1.x/configs/bbconfig-router这个文件复制到busybox-1.x/.config，所以设置了也无效，如果要进行busybox的裁剪，那么要把.config文件复制过去。

putty的行数设置在window标签中，容易直接去点window下面得标签，忽略其本身可以设置。

严斌买了个htc的手机，隐藏键盘，跑windows mobile，看上去还不错，3000多，他说如果是买多普达，就要7000多了。多普达就是htc在大陆的品牌。所以买htc就一定是水货，要重新刷系统。

吃饭的时候，昨天那个lcd厂家的人打电话给彭广才，彭广才说很忙，来聊天影响工作，很多人都有意见。那人问是不是李忠，彭广才说都有意见。

李忠还在折腾传真机的话机软件，终于正确的显示了汉字，但程序似乎死掉了。他发现displayChar函数被修改了，而李柱栋则否认修改了这个函数。

张悦玲火气较大，和彭广才两人互相指责对方胡扯。

2009.4.20
早上收到了Mark Lee <mark.lee@comtech.com.cn>的来信，附带了一份nvram的说明，其中有关于如何设置内存参数的值，stdram_init，设置了这个参数为0x000a后，显示的内存就有16M了，并且web访问后，wl_unit的值也是正常的0了。
测试了一下自己编译的程序的无线部分：
将公司网线插在lan中，笔记本ip设置为公司的局域网段，windows下连接后，可以正常访问局域网��但在linux下，无法连接无线网络。
测试一下路由功能：
将公司网线插在wlan中，wlan设置为公司局域网段，笔记本通过有线网卡插在lan中，ip是和公司局域网不同的私有网段。网管和dns设置为路由器lan的地址，可以正常访问公司局域网。wlan设置为135为网关和dns，135路由器不进行地址限制，则笔记本也能访问internet，135路由器进行地址限制，笔记本则不能访问internet。
可以在路由中设置端口转发，实现nat的功能。
在make menuconfig中选择了某个选项，在/dev/中出现了usb设备，但忘了是哪个了，还要好好的找一下。
胡中奇要在pc上做一个短消息发送接收的程序，就来找我做一个动态库给他，接口是encode和decode，将要发送的短消息编码成可以发生的文本和将接收的短消息解码成可读的文本。由于在pc上完成，可以做得比话机上完整，7位编码的所有字符那么都可以支持，这样就不需要为某国语言进行单独的处理，而接受的所有unicode码也都可以显示了。
下午一个液晶厂家的人来找彭广才，一直想套出一些关于通则公司对于供应商招标的一些细节出来，并谈到最佩服史玉柱，李忠立即表示史玉柱可恨，说他做的网络游戏伤害了很多青少年。又谈到三鹿，说三鹿也属于无奈之举，李忠对此嗤之以鼻，说做人的底线不能丢。显然李忠对这个人非常不满，直说他在这里打扰了工作，直到说第二次的时候，他才离去。
王伍让严斌把usb的输入和输出反一下，结果严斌折腾错了，还好还没有看见冒烟。
李忠和张悦玲都很反感做硬件的键盘线随意拉，其实这样只要在程序中建立一个对照表，不同的产品修改对照表就好了。奇怪。

2008-10-8
完成了6954b中的：挂机不挂响铃的那一陆、使用dial键代替摘挂机行为。
2008-9-24
xmodem的源程序的居然很少，找了个国内的动态库的，设置了半天，一点要在open之后才可以设置各种参数。

2008-9-6
程序貌似不会完全死掉了。现存的问题有：
1、缺失的缴费记录，有些缴费似乎没有收到，但这个现象在昨天则没有出现过。
2、没有记录终端ip，这给以后的工作有很大的不方便。
3、存在错误的发生包，也就是包错误，非常难解。

2008-8-30
程序从周二到今天还在貌似正常的运行。

2008-8-26
现在认为是程序的异常错误使得临界区未释放导致的所有缴费操作失败造成的问题。

2008-8-23
早上121这台服务器又出现问题，显示的结果是连在boss上，但passflag=0，但没有按照预想的去重新连接。
从晚上复制回来的数据库显示，是有许多的缴费都认为是boss没有返回数据，但是同一时间段，131那台服务器的缴费全部正常。

2008-8-22
上午去了营业厅，服务器没有重启，发现以下问题。
有一笔记录只有冲正记录，没有缴费记录。

2008-8-21
到石家庄，下午去了营业厅。

2008-8-7
服务程序似乎什么问题都没有了，不过如果数据库访问采用临界区的方式，显然200个客户端，20个boss接口，失败率显然是太高了，有5%左右。
cvs对delphi的程序支持的显然有些不够好，合并分支的时候总是会出问题。

2008-8-6
如果终端开300个，那么终端机器似乎受不了，或者是我写的在线程中执行的程序有问题。

2008-8-5
如果boss端开20个连接，那么失败率会下降到百分之零点几，不过今天早上服务程序又报非法错了。

2008-8-1
如果boss端开5个连接，客户端每台机器开50个客户端，那么其中一台机器的失败率率在2.88%，另外一个在2.45%。

2008-7-31
如果boss没有问题，现在的ats程序似乎比较正常了，而模拟客户端也没有那么容易报非法错误了。
15:41现在使用3台计算机，每台开了50个客户端，应该没有什么大问题了吧。

2008-7-30
ats中存在的问题是保存发送的包使用的全局变量，这似乎会引起终端挂起。
下午三点河北服务器被关闭，原因是移动网络的改造，封闭了没有备案的机器。

2008-7-29
河北的机器的新程序已经开始跑，昨天5点开始的。今天早上又有失败的缴费记录产生。

2008-7-25
查了一天的ats程序，找到一些错误。
直接使用sockt确实不是什么好主意。
河南那边机器准备好了，但是还要有3c证才能使用。

2008.7.24
如果按键是在frame中，那么就无法得到了。还需要继续分析。
河北的boss可以接受多个连接，这样程序要做比较大的改动了。王伍让万辉一天改出来，应该比较难。

2008.7.23
早上河北的服务器又崩溃了。郁闷。
终于可以截获网页上的按钮点击事件了。
和烤烟的接口中如果李忠的程序连续发送多个包，那么只会发送最后一个包。
2003-7-3
如果从TcustomMemo或TcustomRichEdit继承Terminal，画面闪烁的太厉害。

2004-12-7
for(); if();需要注意，这种情况很难被注意到，而程序肯定是不对的。

2004-9-22
如果对没有足够长度的字符串使用strcpy等函数，会死得很难看的。
当把某个BUFF增加到另外一种数据类型时，需要注意和这个BUFF联系的计数变量是否做了同样的修改。

2004-9-9
在c中，定义字符串，应该定义为最长+1，给0留下位置，否则就不能按照字符串处理，麻烦多多。

2004-9-2
应该仔细检查电缆，看看是否接错。

2004-7-9
如果循环永远只执行一次，应该检查是否写成了空循环。

2004/6/4
INT8U不可能超过256，更别说1000了。
如果不开中断，中断函数不会运行的。



2003-6-27
完成监视某个地址不停监视功能。
完善客户端功能。

2003-6-26
完成写内存数据。

2003-6-25
                  if (uartKeys.keys[i] >= 'A' )
                     addr += ( uartKeys.keys[i] - 'A' + 10 ) * power;
                  else
                     addr += ( uartKeys.keys[i] - '0' ) * power;
                  power *= 16;
文件大小是0x94b4
                  if (uartKeys.keys[i] >= 'A' )
                     addr += ( uartKeys.keys[i] - 'A' + 10 ) * pow(16,8-i);
                  else
addr += ( uartKeys.keys[i] - '0' ) * pow(16,8-i);
使用了arm251的math.h 的pow函数 功能是一样的
文件大小变成了0xa4c4
不过毕竟还是可以利用arm提供的库函数。

     完成:
     1、显示菜单，可以根据菜单提示用户输入
     2、可以动态接受需要显示的内存变量
        此功能和客户端miniTerm.exe结合使用效果最好
        和其他term，如超级终端必须自己查找变量地址，手工输入信息
    修改的文件有uart.c uart.h monitor.c

2003-6-23
下午，一个数组越界的错误查了半天，吐血。


2003-6-13
改写后的statePro函数

2003-6-5
本周重写了用户框中cpu板中的statepro函数。完成一个用户框中相互打电话的功能。
重写DialNumberAnalyse：
1、 拨一个号码后停送拨号音
2、 在拨了一位号码之后，不能在拨0－9以外。



2003-05-20
metaProducts Offline Exploerer Pro
zMud 4.6
absolute MP3 Recorder
HEML Compress
Winiso
Delphi
The bat!
Aspack
紫光拼音3.0


2003-05-18
http://www.delphibbs.com/delphibbs/dispq.asp?lid=1772610 dll退出报错

2003-05-07
我刚刚看到设计的原理部分。先摘抄：
里氏代换原则：一个软件实体如果使用的是一个基类，那么一定使用于子类，而且它根本不能察觉出子类和基类对象的区别。

依赖倒转原则：客户端依赖于抽象耦合。抽象不应该依赖于细节，细节应该依赖于抽象。要针对接口编程，不要针对实现编程。

里氏代换原则似乎好理解，在oo中的有多态性。

2003-04-26
设想这样一个系统界面：
左边是树型导航，右边是panel，在panel上根据不同的导航显示不同的form.
在工具栏有一个“打印”按钮。
当然，我们希望点击这个按钮调用的方法随当前显示form的不同而不同。
不同的form打印的情况都不相同，有的屏幕打印即可，有的需要做报表。
请实现之。

1、我原来的
procedure tform1.printButtonClick(sender:Tobjet)
begin
  if currentForm = showform1 then  //currentForm保存当前显示的窗口，为tform类型
    showform1.printIt;
  else if currentForm = showform2 then
    showform2.printIt;
.....
end;

2、使用继承和多态的方法
所有的显示form都从一个fathrForm中继承。
在fatherForm中写一个虚方法printIt
所有继承的form根据自己的情况重载这个方法。
我们再看
procedure tform1.printButtonClick(sender:Tobjet)
begin
   currentForm.printIt;//currentForm保存当前显示窗口，为tFatherForm类型
end

代码是不是简单了些，当新增加显示form时，这段代码不用改动了吧。

2003-04-22
今天用了C++builder发现可以这样写代码：
    DWORD done, length;
    Label1->Caption = 100*done / length;
这让我有些喜欢C++builder了，谁清楚这里面的原因？

还有
int hIn = open(Edit1->Text.c_str(), O_RDONLY | O_BINARY);
我花了好久的时间才知道Edit1->Text.c_str()可以把widestring转换成pchar
我是看到别人的代码才知道的。
我想问的是我怎么能从帮助里知道使用这种转换方法。


2003-04-10
更改ext.c 程序：
将void  InitCPU()中的
		MyBoardAddr = (RB0<<3)|(RB1<<2)|(RB2<<1)|RB3;
		if(MyBoardAddr==0)
			SSPADD=0x9<<1;
		else
			SSPADD=MyBoardAddr<<1;
代码提出，单独变成一个函数：void readBoardAddr()
除了供initCPC调用外，在main中也每1秒调用一次。

2003-4-6

数据库和面向对象如何衔接，我看过一本书提出这种方法：
书名字不记得了，有uml这几个字。
书中的原文早不见得了，我们以操作员管理为例吧：
我们很容易把操作员抽象成一个类：
Toperator = class
   private
     FName :String;
     FId:String;
     FdelpartmentId,FDepartmentName:String;
   public
     con..(不记得怎么拼写了) create(id:String);
   property
     name string read FName write Fname;
     departmentId : String read FdepartmentId write setDepartment;
     departmentName :String read Fdepartmentname;
   end;
这里部门做了简化，不使用一个新的类了。
改变某个操作员的部门这个担子无疑落在了setDepartment上，
它要做的事情有：
1、改变FdepartmentId、改变FdelpartmentName
2、更改数据库
按照这样，调用toperator的界面就不需要知道数据库在做什么了。
更进一步，我们是不是可以把一个form放在这个类中，来编辑
操作员属性呢？
增加一个public方法：
  procedure toperator.edit;
  begin
     with ToperatorEditForm.create(self) do
     begin
        getData(id);
        showmodal;
        if modified then //modified 是ToperatorEditForm属性
           reload;//toperater方法，重新读数据库。
     end;
  end;
这样，在操作员管理界面中，我们基本上就不太需要数据库了。
最后，为了在管理界面中列出所有的或部分操作员，必须还有一个容器类。
TOperatorContainer = class
   private
     operatorList:array of toperator;
   public
     procedure getAllOprator;
     procedure fisrt;
     ...
     procedure find(string);
     procedure findInDepartment(delpartmentId:string);//查找某个部门的人员
     procedure findOnPower(powerId:String);//查找具有某种权限的人员
     procedure findOnSalary(salary:real);//查找某个薪水的人员
     procedure view(listview);
   property

end;
这样操作员管理这个界面就彻底和数据无关了。

无论是什么样的团队开发，首先都是要有一个优秀的项目经理。
在项目初期，他要大致分析问题难度，估计开发人员数量，估计开发时间，估计开发成本。
开发中，这个人其实未必是水平最高的，但他一定要能够使得团队在没有干扰下进行工作。
最重要的是，他能协调这么些优秀的人才的关系，保证每个成员的积极性。这决不是老好
人似的人物可以解决的问题。他必须知道每个人的长处，并给予发挥，让每个人承认别人
的优点，并从中得到受益。要制止任何形式的相互攻击。
行业专家是提出需求的人，有人说用户是提出需求的人。从我的经验来看，用户站的角度
不够，他们往往只了解自己手头上的工作。你认为化2－3个月和用户交流就能得到你所想
要的需求吗？如果没有行业专家，软件公司往往要做了好几个项目之后，才自己培养了行业
专家。他了解企业内部数据的分布，数据流转和数据分析的方向。他真正站在客户的角度
描述问题，给出问题的合理解决方法。从某种意义而言，他可以不懂计算机编程。
系统分析员是个骄傲而尴尬的角色。他必须上知天文（行业需求），下知地理（编程）。
否则他的分析无异于隔山打牛。

其实最主要的是交流，角色可以残缺，变换，交流不能少。

2003-04-02
进一步的测试表明每秒中可以发两个4000的数据。这和预期的是一致的。

2003-04-01
加入和校验。才发现接收时最后两个字节时CRC校验码，程序接受了一个，甩掉了一个。但是指针和长度位未包含最后接受。加入校验时去掉这个CRC校验码，接受和发送的和校验一致了。
使用定时器来发送进行测试，每秒发送4000个没问题。正准备进一步测试，停电了。

2003-03-31
终于成功发送了。
在timer中每2ms判断一次，如果csr判断fifo为半空，则发送32字节。
增加了byte E1SendBufp4096],word E1SendHead,E1SendTrail变量作为发送缓存和指针。
发送4000个字节也没问题。
接受方面，长度增加一位来存储。

Ds21354Reg(span,HIMR)=0x54; 		发送中断的方式结果是死机
Ds21354Reg(span,HIMR)=0x51;  似乎没有作用

这是发送e1数据包的代码。
void TestLoopBack(byte span)
{
	byte i;
		for(i=0;i<200;i++)
			{
			SendPacketBuf[i]=i;//(SendPacketBuf[i]+1)&0xff;
			//SendPacketBuf[i]++;
			//HDLCSendCount[span]+=8;
			}
		//PutMsgToPool(span, 10, tempbuf);
		//HDLCSendPacket[span]++;
	SendOnePacketToPartner(span, 100);
}

下面这段代码在void SendOnePacketToPartner(byte span,byte len)中，但无法发挥作用，现在把它删除，改用中断的方式处理试试。
	byte j,count;
	if (span > 3) return;
	Disable_Int(nGLOBAL_INT);
	Ds21354Reg(span, HCR) = 0x30;
	len--;
       count = len /32 ;
        //HDLCTempBuf[14]=500>>6;
	for( j=0 ; j <= len ;j++)
	{
	 /*    for(i=0; i < 32; i++)
	     {
                 if( j*32+i >= len )
                     break;
	          Ds21354Reg(span, THFIFO) = SendPacketBuf[i + j * 32];
	          HDLCTempBuf[14]++;
	          // HDLCTempBuf[13] = i + j * 20;
	     }*/
	     Ds21354Reg(span, THFIFO) = SendPacketBuf[j];
          /* while (1)
	    {
	         //delay();
	       Ds21354Reg(span, HSR)=0xFF;
		st=Ds21354Reg(span,HSR);
    	if //(//((st & 0x04) == 0x04)  ||
		     ((st &0x02)==0x02 )// ||
		     //((st & 0x01 )==1))
	        {
	           // if ((st & 0x02) == 0x02)
	             HDLCTempBuf[12] ++;
	            //  if ((st & 0x01 )==1)
	            // HDLCTempBuf[13] ++;
			break;
	        }
	     }*/
	/*      delay();
	      delay();
	      delay();
	      delay();
	      delay();
*/
	}
       Ds21354Reg(span,HCR)=0x24;
       Ds21354Reg(span, THFIFO)=SendPacketBuf[len];
	Enable_Int(nGLOBAL_INT);

2003-3-28
ds21354中span＝1时，不能设置loop Back否则接受不正常。这是昨天莫名其妙的原因。
在hdlc发送过程中：一次发送若干个字节，以64个分组发送，发送间隔采用延时的方法时，不能完全接收数据。
在不使用延时的情况
字节数
DsE1HDLCIsr执行次数
Len+
len
E1ReceiveBuf尾指针和头指针之差
16
2
0x21
0x11
0x13
50
4
0x89
0x43
0x45
70
5
0x65
0x33
0x 35
100

0xA8
0x44
0x 43
200
6
0x13
0x4b
0x 4d
如果使用延时，对于发200个数据则每增加一个延时，多接收4个数据，超过6个后为0
如果不采用延时，采用循环读取THIR内容判断的方法，则死机，难道是判断不正确？

2003-03-27
编写ds31354控制hdlc的部分，要将发送和接受的包的大小扩大。
完成了ds21354 framer loop back 部分。
原来写的在超级终端中显示变量地址的代码可能有问题，在显示发送和接受部分时，接受部分莫名其妙的有时无法接收。无奈，只好把那一部分代码全部还原，因为不知道是什么原因。而且显示变量的地址显示的内容和直接写这个地址显示的内容不相同，所以，输入地址直接看变量内容的工作还有很多路要走。
今天拿到了商调函。
