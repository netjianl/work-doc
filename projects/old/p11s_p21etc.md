
#### 2019.08.26
**苗立双**   使用三旗LM923S模块开发的支持B42,B43频段的程序,使用8M FLASH,V48，为中东客户开发的程序;
升级版本到V48; 修正由于配置导出命令的输出存在双引号,导致tr069启动程序异常问题,网页上也进行了双引号的过滤;
#### 2019.08.21
**苗立双**  P11S(P11K)使用宽翼模块为中东客户开发的程序,修改版本为V18;修改使网页普通账户可以导出配置;
#### 2019.08.19
**李光达**  中东客户要发800台三旗模块，原来中东的客户基本是B09的模块程序。阿根廷客户发了几千台B11的模块程序，实网也没有反馈什么问题。现在在公司测B11+V47的话，小基站驻不上网  
**苗立双**  P21使用三旗LM923S模块为中东开发的程序,修改网页,使可以配置wifi最大发射功率;
修改说明:
- 修改软件版本为V20;
-  修改网页,使可以配置wifi最大发射功率(需向赵金要最新版本配置工具,配置"允许设置的最大wifi发射功率"); 
#### 2019.08.17
**刘永辉**  P11S 中东客户三旗模块客户反馈网页LTE状态显示正常，但是无法正常上网
#### 2019.08.12
 **毛祖潇** 在前线验证升级99%网页不更新的问题已经解决
#### 2019.08.11
**毛祖潇**  升级卡到99%网页不会自动更新 苗工预计本周出版本40.0，待下周一国内永辉和光达验证OK后前线再进一步验证
#### 2019.08.09
**苗立双**  ZLT P11S使用联芯LT10模块为斯里兰卡Dialog开发的程序V40.0;<hide>  
- 修正sip alg程序存在非法内存访问的bug;
- 优化网页升级过程,如果检测到cpe重启,则重新加载web页面;(如果升级到40.0以前的版本,则该机制不起作用)
</hide>
#### 2019.08.07
**苗立双** 9341 宽翼，LAN可设置两个网段
#### 2019.08.06
**苗立双**   P11S(P11K)使用宽翼模块为中东客户开发的程序 修改版本为V16; LAN口增加对设置第二个IP的支持;  
修改版本为V17;修正修改了第二个lan ip之后,重新进入dhcp设置界面,第二个lan ip显示不正确的bug;
#### 2019.07.22
**叶京平** 关于断网的问题，客户又抓了LOG给我们分析，下面的链接分别是SYSLOG和 DM 工具抓的LOG
#### 2019.07.18
**苗立双**  使用三旗LM923S模块开发的支持B42,B43频段的程序,使用8M FLASH,V47 <hide>  
关掉10分钟无网络则重启特性,关掉其他异常检测重启机制;
优化防火墙规则处理,增加对只允许指定ip访问的支持;
</hide>
#### 2019.07.17
**苗立双**  使用三旗LM923S模块开发的支持B42,B43频段的程序,使用8M FLASH,V46 <hide>  
- 进一步增大arp表大小;
- 合并cpe内部配置管理工具输出的配置没有带双引号引起的bug;
- 网页增加对将syslog重定向到指定服务器的支持;
</hide>
#### 2019.07.15
**苗丽双**  立陶宛Ｐ１1Ｓ v24正式版程序,使用lt10模块版本为V24;修正无法映射wan端口161的bug;
**叶京平**  客戶再測試port mapping時, 發現port 161不能正常工作
**苗立双**  立陶宛Ｐ１1Ｓ v23正式版程序,使用lt10模块;<hide>
- 网页默认关掉ping watchdog;
- 去掉网页日志中的"Search currently available networks";
- 按照客户要求,重启模块或者整个系统情况下,写入重启的时间;
- ping watchdog ping一次后等待3秒,如果成功,则不继续ping；
</hide>
#### 2019.07.08
**叶京平**  中东客户反馈我们的P11有如下反馈（重启CPE LAN口无网络，需要恢复出厂设置才能正常，）  
立陶宛 NRO361 程序还需要修改：當收到PING的echo reply後, 就不用繼續PING完剩下的次數. WatchDog的信息要加入Time stamp.正常版(不寫Flash)的PING Watchdog預設要Disable. 只有Debug版預設才要Enable.
#### 2019.07.05
**苗立双**  立陶宛Ｐ１1Ｓ v22debug程序,使用lt10模块,仅用于调试验证找问题;ping watchdog部分网页为空情况下,显示默认值;  
立陶宛Ｐ１1Ｓ v22正式版程序,使用lt10模块; ping watchdog部分网页为空情况下,显示默认值;
#### 2019.07.04
**苗立双**  使用三旗LM923S模块开发的支持B42,B43频段的程序,使用8M FLASH,V45，为中东客户开发的程序;升级版本到V45;修正网页log中经常出现"Search currently available networks"的bug
立陶宛Ｐ１1Ｓ v21debug程序,使用lt10模块,仅用于调试验证找问题;修改版本为21debug;将重启模块和重启事件写入日志中;
#### 2019.07.03
**苗立双**  立陶宛Ｐ１1Ｓ v21程序,使用lt10模块:增加对ping watchdog的支持;
#### 2019.06.17
**廖媛**  原来的p21还是丢程序比较严重。
**苗立双**  ZLT P11S使用联芯LT10模块为斯里兰卡Dialog开发的程序V39.8<hide>
- 增加对网页登录界面显示sn,imei的支持;
- 网页限制wifi ssid/密码开始结尾不能包含空格;
- 合并url过滤可能长时间不能获取指定dns对应ip的bug修改;
- tr069增加对InternetGatewayDevice.WANDevice.{i}.MNO_WANNetConfigInfo.*的支持;
</hide>
#### 2019.06.13
**苗立双**  使用三旗LM923S模块开发的支持B42,B43频段的程序,使用8M FLASH,V44 <hide>

- 修正拨号程序运行过程中,tr069程序频繁查询模块状态,可能导致拨号程序因判断错误而意外重启的bug;
- 发送at时,如果长时间在不返回,则认为已经成功返回了,继续发送下一条at;
- 合并防火墙url过滤会因为读取不到dns响应文件而出现的过滤不正常bug;
</hide>
#### 2019.06.12
**苗立双**  是因为升级ZLT_P11S_20_remote_update_2019_03_20_18_16_26.zip之后,会执行一个特殊的文件校验算法,避免有人修改我们发出的升级文件,将修改后的文件升级进去  
升级ZLT_P11S_20_remote_update_2019_03_20_18_16_26.zip之后,剩余FLASH空间很小,存在再次升级情况下,会升级失败的风险;
**胡媛媛**  我们就用这个程序出货
**苗立双**  叶京平的需求 网页上本来就支持的,在配置中开启"显示路由模式设置",然后选择Enabled即可  
中东数据连接断开的原因查证是重拨号导致，修正中。 
#### 2019.06.11
**胡媛媛**  罗斯UPVEL室外套装 显示灯错误 — 这个问题跟简工讨论过，基于公司项目太多，决定不去管。  
升级有问题 — 这个问题会影响客户的使用和管理，所以在做货之前一定要解决
**李光达**  具体问题如下：  
1. 网页升级可以成功，但是再升级P11S其他程序显示升级失败。怀疑是型号没定义导致、因为周工是直接把P21的程序移植到P11S上的  
2. 工具升级，工具没上报成功，也没上报失败，一直卡在写SYSTEM时间那里，但是等一段时间看程序编译时间那些应该是下载成功，应该是没返回什么指令给工具；再用工具升其他P11S程序，显示服务器发POST失败  
**叶京平**  客户的P21，三旗BAND42/43的模块，客户说P21不能像室外CPE P11S一样选择路由模式，能否把P21的这个选项做成跟P11S一样？  

