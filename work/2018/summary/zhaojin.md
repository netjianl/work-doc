#2018总结

##一、参与的审厂：中移物联的集讯审厂工作，烽火通讯的集讯审厂工作。通过审厂,开阔了眼界,并从中学习吸取了不少宝贵经验补充自己的不足

##二、日常项目工作及各种工具程序功能的增加及修改测试工作如下：

1、生产工具:
修正P56/P58遗漏的不再检查是否是同一设备多次升级的问题
增加P53/P59不同批次模块的4G的信号检测兼容性
修正P53/P59的用户操作中WIFI 2.4G信号测试的指定WIFI SSID 被清空问题
修改v10的写MAC方式，由发AT指令改为ADB登录发指令
硬件测试中增加可设置U盘容量大小
修改可设置U盘容量大小仅可填写数字
增加可设置TF卡容量大小
P53/P59在校验成功后增加恢复出厂设置操作
增加可动态设置网络连通和断开的PING次数
修改V10的MAC设置方式，重新改为新的AT指令设置
修改V10的校验工位查询指令
修正V10的MACIMEI及校验测试选择自动选项却没有自动执行的问题
设置管理员选项里的校准测试默认内容，并设置为只读不允许修改
增加PING联网和断网的次数提示
管理员界面提供禁止V10的WIFI信号测试
p25/p27/p21M在其所有启动对接程序后增加等待2秒钟延时操作
修正M60/M61 P28模块版本校验不显示的问题
增加M60/M60/P25/P28/P21M的SSID、WIFI密码、WEB用户名及密码、WEB管理员用户名及密码的校验测试
增加校验操作完成后记录本地XLS文件
修正记录校验文件XLS文件时候的错误判断及校验文件保存路径及名称
修正重定位控件的位置，将部分涉及滑动条导致控件位置变化的代码移至初始化定位函数中
增加SSID及WIFIKEY校验的新规则（含大小写及数字）
修正动态WIFI KEY判断错误的变量
增加验证固定WEB用户密码及管理员密码
修正SSID及PWD校验结果判定颜色不改变问题
修改校验测试保存的.XLS根式文件为.X
调整校验部分WEB密码，管理员密码等下拉框的位置及大小
在SSID前缀的配置中，结尾增加单引号作为结束符号，防止SSID前缀最后一个字符是空格而被忽略
修改校验中SSID/WIFIKEY/USERNAME/USERPWD/ADMINNAME/ADMINPWD为字符串全匹配
增加compareString函数用在校验中使用，用来进行多条件判断
修改校验SSID/WIFIKEY/WEB用户名及密码的发送协议规则，去掉2个发送参数
V10在写MAC之后，增加一个AT+PWDRESET="1"操作设置WIFI密码
修正增加SSID可末尾设置空格而导致出现的加载异常
增加新设备P61
修正P25/p27的硬件测试项目的错误
一拖多程序中增加compareString函数用在校验中使用
一拖多程序中P53/P59在校验成功后增加恢复出厂设置操作
一拖多程序中增加M60/M60/P25/P28/P21M的SSID、WIFI密码、WEB用户名及密码、WEB管理员用户名及密码的校验测试
去掉校验文件导入时候判断为空的return返回，防止不继续读取后面的参数
修正P61LANMAC地址写入无效问题
去掉加载时所有的null参数，并增加默认配置
隐藏校验测试中的频宽项目，防止其在其他测试项目设置中出现
修改不再校验LTE/FDD
修改设置V10写MAC过程中，改回原来的计算方式AT+PWDRESET="2"
修改检查LTE 及TD是否校准检测，分不同设备进行判断
增加远程数据库，将测试的结果都存入数据库中
数据库总表中增加MacImeiValue字段，上传信息的时候增加相应MAC或IMEI
增加读取V10的SN号
增加F1机型
增加F1/V10的WIFI信号测试
增加V10/F1的写SN功能
增加上传测试选项
增加M60/M61,P28的上传测试选项
修改F1的校准写入参数
增加物料核对测试项目
增加物料核对连续测试功能
增加onnet设备的视频测试、配置升级及系统升级
增加找他二代宠物项目的MACIMEI工位及WIFI信号测试工位
增加找他宠物项目的烤机老化测试工位
修改ONNET 程序 加载SSH连续测试时候因为不关闭rtsp-factory-test造成端口被占用的问题
减少ONNET加载SSH登录的次数，加快测试时间
增加找他宠物机型硬件测试中的SIM卡测试、GPS定位测试、G-SENSOR测试、电池电量测试、扬声器测试、LED测试
修复找他宠物机型WIFI信号测试中的问题
修复找他宠物机型扬声器测试及G-SENSOR测试的问题
调整v10/f1的校验工位中FCLOSE的错误放置位置，防止程序运行崩溃
增加LT90机型，增加硬件测试工位
修复非ONENET设备进行SSH登录不了的问题
增加V10/F1的4G信号测试
增加找他宠物的电流测试及校验测试
去掉多余的WIFI性能测试、核对物料、核实这三个不用的测试工位
完成找他宠物的硬件测试部分、校验部分、WIFI信号检测部分的问题修正，并增加将结果上传数据库操作
完成找他宠物的gps测试
增加找他宠物硬件测试的电池容量范围定义
隐藏找他宠物WIFI信号测试不用的副天线参数及5GSSID参数输入
解绑P25/P27的WIFI信号测试的IP
解绑LT90的WIFI信号测试的IP
增加可选择检测TDD与FDD校准
增加动态加载VISA32.DLL动态库（仅64位系统可用）
隐藏找他宠物WIFI测试用户部分不存在的2.4G辅天线及5.8G天线信号测试提示
将找他宠物硬件测试提示移动位置
增加实时上传ZTCW类型校准文件
修改ZTCW电流测试等待时间
增加ZTCW上传校准信息文件后写入数据库操作
分离GPS测试为单独测试功能
ZTCW机型在做所有测试前首先检查一下校准、综测、耦合、电流、老化等各项标识
去掉老化测试项目
分离G-SENSOR测试项目
增加前置项的选择
增加V10的配置升级
增加P25M测试及硬件测试中的天线测试
修改ztcw的电流测试方式
增加硬件测试的各项选择测试功能
开放P21M的天线测试功能
增加P21K型号
增加SSID运算新规则：前缀加MAC后5位
增加V10前置项暗码测试的判断
修改P25/P27/P25M/LT90/P21M/P21K的天线测试工位不再区分主辅天线
增加LT90硬件测试中的USB测试
增加硬件测试项选择提示
p28测试4G天线的时候，增加测试成功临时标识及测试一半成功时候改变标识amt/4G_signal为outpass
增加ZTCW镭雕测试项目
ZTCW中增加MACIMEI测试工位上传信息并产生条形码功能
调整配置文件加载的方式
增加ZTCW打码测试工位
修改ZTCW校准文件判断获取的格式
去掉ZTCW单板测试时候的综测检测
在ZTCW的GPS测试成功后增加写综测标识
增加ZTCW耦合文件上传
修正ZTCW获取的SN号后面带空格问题
将ZTCW打码操作中增加写本地文件操作用于条码打印机识别打印
修正ZTCW写综测标志前的SQL错误查询取值方式
修正ZTCW上传数据库查找PathFile的错误
修正ZTCW数据库SN重复问题
增加ZTCW电流测试中电流值的下限为0.4,并只获取小数点后2位
增加P25/P27,P25M,P21M/P21K,LT90的模块校验
修改strcat_s为strcat
增加P21K校验部分的频段检验
将ZTCW上传工位增加前置项判断
将ZTCW电流工位增加前置项判断
P25/P27等机型增加WIFI双天线信号测试
MACIMEI测试管理员设置中，ZTCW机型增加禁止选择IMEI,SN等选项
一拖多程序中添完善加后来单机程序中增加的参数及测试功能
修改P53/P59/P61使用模块判断
一拖多程序中增加多串口PING判断
增加部分对P53/P59/P61遗漏的模块判断部分
一拖多程序中增加V10/F1/W19的 MACIMEI测试、校验测试、升级测试
增加P21K在MACIMEI测试中的SN及WIFI密码写入选择
修改p25^p27,p21m^p21k,p25m,lt90设备的信息上报以IMEI替代SN
去掉V10的是否进行过暗码测试检测
修正P21M^P21K在不选择上传数据库数据的时候可写不同的IMEI号
增加P21M^P21K的SN框在输入完后及自动跳转功能
增加P21M^P21K校验的自动功能
将P21M^P21K的写SN和WIFI密码功能加入到一拖多程序中
将前置项选项中的“升级”分为“升级(系统)”和“升级(配置)”，将"上传"分为"上传(校准)"和"上传(耦合)"
修改ZTCW电流值获取后判断是否小于0的比较，同时增加写入前的判断
补充上传测试中漏掉的数据库连接初始化操作
修改ZTCW的GPS测试成功标示
在发送数据库POST的所有请求后，增加判断是否返回成功
ZTCW机型在GPS测试成功后，增加发送重启指令
增加机型OK-W7
修改V10S/OK-W7的MAC写入指令及校准指令
P21K的原始IMEI在不勾选数据库的时候不做判断
去掉P21K的写WIFIKEY与写WIFIMAC的关联
增加V10S/OK-W7的NV版本获取校验功能
V10/OK-W7去掉SN号的写入，将IMEI作为SN写入到数据库中
修改V10S为网口进行测试，增加写MACIMEI,校验,4G信号测试
注销掉P53/P59/P61的SN检查操作
修改PASS提示出现、消失的时机
增加OK-W7导出配置时遗漏的“校准”选项
去掉V10S/V10/OK-W7校验工位的SN选项
P25增加频段校验
增加P10M机型
增加V10S的WIFI信号测试功能
增加V10S校准测试及校验中的校准选项
修改V10/F1/OK-W7的WIFI信号测试
增加V10/F1/OK-W7的SSID、WIFI密码的校验
增加包装工位、装箱工位、抽检工位、维修工位等测试
在提示前置项没测的时候提示具体前置项名称
增加分配铭牌工位
增加抽检工位中可选项（出箱、入盒、入箱）
增加硬件的单板测试
增加各扫码项目的标识提示
减少POST的发送和接收超时时间
修改insert into语句，不用插入全部属性项
修正关闭数据库操作存在的部分问题
修改抽检工位的出箱操作，改为允许至少抽取一个机器
增加抽检、包装、装箱等工位的机身码及盒码为空的判断
增加OK-W7写MAC IMEI后的恢复出厂设置操作
增加P21M^P21K的打码工位
增加OK-W7的SSID及WIFI KEY的校验
增加P21M/P21K/P10M/P25/P27/P25M/LT90等型号升级配置前的删除短信数据操作
增加称重工位
ZTCW修改电流测试保存电流值指令
ZTCW修改LED灯测试开关指令
修改查询前置项的方式，改为webservice方式
增加发送参数SelectStr到接口SaveDeviceCheckList中
增加F1的校验SSID及WIFI 密码
增加ZTCW的电流测试通过率最高参数设置
将所有的直连数据库查询前置项操作全部改为webservice请求方式
增加V10S的SSID、WIFI KEY、配置版本、外发软件版本、普通用户名、普通用户网页密码、高级用户名、高级用户网页密码校验
修改P21M^P21K的SN自动跳转判断，18位长度自动跳转
增加P21M/P21K/P25/P27/P10M/P25M/LT90的内部版本校验
增加P21M/P21K的SN,WIFI密码校验
增加合并P25M与P25K，增加频段校验测试
增加V10S/F1/OK-W7/V10的导出及加载校验配置文件的操作
增加P21M^P21K的打码工位
完善P56/P58上传数据程序，除了升级系统不能上传数据外，其他操作均可上传
增加P10K设备测试
修改ZTCW电流测试通过率百分比参数为浮点型，防止整型导致的除法余数为0
修改QA的装箱测试，循环取出所有的FILED为BATCH的数据后依次与要对照的值进行比较
增加F1的打码、称重、包装、抽检、维修工位
增加将F1所有数据上传数据库
增加查找生产所用的SNMACIMEI表格操作，核对要写入的SNMACIMEI是否合法
读取重量超时的时候不退出，继续循环读取
增加IMEIMSCSN工位写SN时候的长度判断
去掉F1的暗码测试
根据耦合文件变换的格式，修改ZTCW耦合文件上传前的格式判断
将打码、入盒、装箱、抽检、维修、称重工位的F1 输入参数改为IMEI
ZTCW在电流测试前增加搜网注册查询操作
增加打码工位末箱选择
修改F1的打码工位生成XLS文档内容格式
修改F1的打码、包装、装箱、抽检、维修、称重工位以SN为准
增加装箱数量最大值为20
增加可填写数据库名和密码选项
增加p25m/p25k的各项测试能使用数据库
ZTCW的 IMEIMAC工位增加上传DOID、打码工位增加DOID
去掉ZTCW在获取SN前的查找前置工位操作
增加校验工位的SSID规则，增加普通MAC后3位
去掉ZTCW的电流测试前的入网注册查询
F1型号将IMEI作为识别码写入数据库的SN字段中，SN改为直接写入DeviceSN字段中
增加GPS超时设置
增加校验校验工位的web管理员密码验证的下拉框选项，增加MAC8位密码与MAC8位密码(不含1iIl)两项
修改ZTCW的打码测试工位，增加打设备条码与打箱码的选择
增加可打印箱码中IMEI或SN超过20个的条码
修正P59的TF/USB测试不能同时插入两张卡的问题
将管理员设置中，连通性测试中漏掉的设置SSID功能重新补充上来
增加P53/P59/P61校验工位的模块硬件版本测试选项
P53/P59/P61在进行IMEI校验测试前，执行停止DIALTOOL操作，防止AT指令干扰
修改ZTCW的GSENSOR判断条件，改为三个方向同时变化
增加ZTCW的称重、装箱、维修、入盒，抽检等工位操作
修改所有Webservice发送请求，增加ClientCode字段
增加下载更新生产工具和应用配置工位的设置
修改导出当前全局配置，导出的配置将以型号、客户订单号、客户代码及测试项目为名称
增加M60/M61外置天线的4G测试
修改的部分SQL语句漏掉的ClientCode属性操作
增加P56/P58/P53/P59/P61等型号的装盒、装箱、打印、称重、抽检等操作
增加P10K的SN可选择写入操作与可选择校验操作
修改V10S外发版本校验查询指令
增加每个工位测试结果发送到指定数据表接口，为统计工位通过率做准备
修改写MAC/SN/IME/DEVICESN的JASON接口
称重工位可选择网络或串口选择，支持不联网称重
分离硬件测试中TF与USB测试，当其值设置为0或空的时候表示不测试此项
删除部分多余的代码，让每个CPP文件内容的行数小于65534行
ZTCW在写MACIMEISN之前增加可选校验SN表操作
增加可实时显示当前测试工位通过率
修正写MACIMEISN失败时候漏写的WhereStr语句
增加打码操作中，连续打码勾选后删除本地XLS文件操作
修改管理员界面遗漏的获取V10S外发版本
修改打印工位部分机型箱贴纸格式，增加SN打印项
增加漏掉的打印SN前缀
修改箱号长度为6字节
将各工位通过率查询改为点击执行按钮后
上传工位增加非PASS文件删除操作，减少文件夹中文件数量加快上传速度
MACIMEISN工位增加批次号的选择写入
修改上传工位PASS文件等待时间为5秒，并保存FAIL文件
修改上传工位PASS文件等待时间为20秒，并保存FAIL文件
修改V10校验配置导出项
增加部分设备MACIMEISN工位自动跳转到批次号框功能
修改产生的XLS文档，将ZTCW的两个IMEI属性分别改为IMEIX和IMEIY
修正将ZTCW机型将判断是否打箱码和条码的标识误当做装箱数量变量操作的问题
修改写入XLS表中箱号长度为6字节
增加P10X机型，并增加其系统升级工位
硬件测试工位P21M P21K P25M P25K P10K P10X等机型的4G天线测试增加取下天线操作
增加发送post数据返回异常的时候，重新再发送2次
修正ZTCW打码工位中清除错误箱号的问题
增大存储多个IMEI和SN的变量空间大小
增加P21K/P21M/P25K/P25M/LT90/P10M/P10K/P10X等机型的可选择校准版本进行校验
管理员界面增加机型ZY366
修改校准版本里模块SN的判断条件
修改校准版本判断里的SN判断标准，带字母的也算合格SN
去掉SQL的DEVICETYPE和CLIENTCODE的查询
增加ZY366机型的MACIMEI工位、校验工位、硬件工位测试
增加校验工位的SSID新算法：前缀MAC4位后缀
增加校验工位的WIFIKEY新算法：MAC10位、MAC10位(含大小写字符和数字)
增加M60A机型
增加V10到称重、包装、装箱、打码、抽检、维修等工位测试中
增加ZY366的包装、打码、装箱、称重、抽检、维修工位
修复M60A的硬件测试工位
增加P21K/P21M/P25K/P25M/M60/M61/P10M/P10K/P10X/M60A/LT90/P25/P27/P28等机型的WIFI性能测试
修正ZY366管理员界面测试校验工位未关SOCKET的问题，去掉管理员网页密码校验
增加批次号B的写入
修正点击按钮直接显示FAIL问题
V10S增加包装、称重、装箱、打码、抽检、维修工位
修改P21M/P21K的天线信号测试方式
将执行md5sums.exe时候命令行里c盘前的空格去掉，防止路径过长出现的空行
纠正管理员设置里校验工位弄错的频段检查标志
将新加的SSID校验算法、KEY校验算法及用户WEB密码校验算法加入到程序中
增加json post数据返回非true/false数据内容判断
去除部分冗余代码，减少代码行数
增加选择数据库时的可重写MACIMEI选项
调整用户界面所有测试成功单项返回代码，将其统一到一个函数中去
去除ZTCW之外的所有型号的LED灯手工点击PASS或FAIL的按钮操作，并将其放到所有硬件测试操作最前面执行
减少优化pushToDatabase2中的重复代码
调整按键测试时间和天线测试时间
调整部分代码中变量声明的位置，并减少冗余代码
去掉M60A升级前的启动对接程序操作
增加P21M^P21K/P25M^P25K/P10M/P10K/P10X/M60A/LT90校验部分的VOIP校验
增加GPOND机型及MACIMEI工位和校验工位
MACIMEI工位一拖多增加上传数据到服务器
增加本地IP2作为预留IP
完成写MACIMEI从数据库取数据操作
修改WIFI信号测试外部IP与 WIFI性能测试中IP冲突的问题
增加4G天线工位、校验工位的一拖多数据上传服务器操作
修改ZTCW的GPS测试
增加WIFI天线测试用仪器的方式
增加一拖多WIFI天线仪器测试
增加一拖多WIFI天线仪器测试完成后标志位的写入
增加批次号上传选择
修改漏掉的可选批次号长度参数
删除校验WEB用户名上传数据中多余的orderno
将readydeviceno=-1去掉
修改打码工位DOID格式,增加全DOID格式
修正P25K/P21K/P10K等机型批次号B上传为空的问题，改为上传模块SN号
增加定位到设备编号的语音提示
增加GPOND一拖多升级程序
暂时去掉GPOND100的MAC及SN写入判断

增加一拖多写号工位批次号A与IMEI对比判断

2、CreateBin工具:
创建BIN文件
更改BIN文件存放路径并修改产生的MD5文件名称
先产生.ZIP文件，然后复制改名为.BIN文件

3、GPIOTEST工具：
gpio原始程序
循环Sleep时间全部改为1秒

4、KEPPWD工具：
增加导入TXT文件源功能

5、ModuleSNCheck工具
修改从机器中读取SN时的判断条件
发送数据后等500毫秒后再进行接收操作，防止接收失败

6、PostTest工具
增加压力测试POST数据到数据库功能

7、RebootTest工具
重启测试工具

8、多机升级海外工具
multi-devices tools for updating
modify some lable notices

9、ShowInformation工具
add version compatibility
add compatibility with version before 6.9
add EnodebId and CellId information
隐藏模块硬件版本
增加新版本ENODE的获取显示

10、P53Update工具
西斯美康P53升级工具
增加兼容6.7及以下程序版本的系统升级

11、mtkWifiTest工具
将PING断开2次作为真正网络断开
更改无配置时的默认TELNET用户名和密码、标准版本号
增加恢复出厂设置操作后3秒延时

12、MutiTool工具
选择固定MAC+KEY的时候，增加一个是否转换字母的选项
修正固定mac-key的不含字符选项导出配置时候的错误
增加导出和导入配置要选择设备类型
增加新SSID产生规则和WIFIKEY 的产生规则（含大小写及数字）
隐藏动态KEY规则（不含1iIlL）
增加MAC中导入批量列表与单独选择
修改提示字段内容
增加可选机型及型号
增加STRONG十位密码及MAC产生SSID的固定后缀填写
增加WIFI密码新规则10字节(8字节MAC后2位)和web密码新规则前缀IMEI4位

13、PowerOnOff工具
在DHCP判断是否连通时增加被测设备IP网段的判断

14、SMT工具
增加定位当前校验成功的站位、物料行；增加时时上传校验成功信息到数据库
增加上传物料表、站位表及核对功能
修正把站位表中的“位置”当做“站位”进行核对的错误
完成物料表和站位表的核对校验功能
更改加载的站位表部分数据显示的顺序
增加机器编码扫描输入字段
站位及机器代码框的自动跳转改为以#为结束符
站位及机器代码框的自动跳转条件改为固定5个字符长度
增大接收上传校验时候的接收区大小
增加错误站位历史提示，增加错误时候的音频报警，增加所有站位扫完提示
增加pass及fail声音播放
更改pass和fail的音频文件格式
增加站位和机器编码不为5时的循环查询
增加获取到物料编码后等待1秒
在连续测试时候，当站位和机器编码不一致时，也能继续测试
增加数据库语句操作执行失败时候的日志
增加上传IMEIMACSNLIST数据表
增加可输入数据库用户名和密码提示框
上传MACIMEISNLIST表操作中加入ClientCode，InnerSN，Iccid，Doid，Telno，Btmac等新属性
去掉MACIMEISNLIST表操作中InnerSN，Iccid，Doid，Telno，Btmac属性，将MAC改为WIFIMAC 与LANMAC属性
增加可选择插入原始表或临时表
修正导入ImeiMacSnList表后出现程序崩溃的问题
增加上传批次号表
增加物料批次号核对和批次号产生上传
增加物料批次号信息获取取代之前的板子批次号
修改上传批次号部分显示问题

15、配置工具
根据需求不时增加或修改新的配置选项

16、onenet程序部分
安装部署ONnet 环境，查看代码
ONNET报警部分程序修改，修改为CURL方式，并找到之前POST信心返回一直报错的原因，测试修改3种报警方式，可以正常上报了
修改ONENET程序，增加配置，并修改选择是用SD卡或NFS记录保存音视频文件程序
编写监控SD卡容量代码，并加入到ONENET程序中
查找下合并WAV格式文件的音频编辑工具和转换 wav为acc文件的工具，测试发现Cool Edit Pro 工具及Magic Free M4A AAC OGG WAV to MP3Audio Converter工具可以实现上述编译和转换
onrnet程序中编写读取.acc格式文件的接口，用以可以播放提示信息
ONENET编写测试上传SD状态函数，包括正常，无卡，卡满，卡异常等状态
查看RTSPD源码，编写一个RTSP-FACTORY-TEST程序，用于配合生产工具进行视频测试。
查找ONENET中ps一直增加的SH脚本进程问题后导致程序挂掉，修改代码将之前的全局变量FILE移到函数内改为局部变量，并去掉用于调试的打印信息；完成RTSP-FACTORY-TEST程序，并同步编写用于ONENET的视频测试生产工具，经测试可以使用。
修改编译脚本，解决rtsp-factory-test 不能编译的问题
编写onnet 上的macwriter程序，加入检测视频播放测试的对接协议程序部分
编写onnet 的macwriter 中的配置下载程序
修改测试ONNET 的MACWRITER 程序，测试配置升级，可下载并写入参数
修改onnet的macwriter 程序，修改加密配置的存放位置为/mnt/mtd