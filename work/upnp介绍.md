# 一、共享利器UPnP
大家知道，宽带路由设备一般都是通NAT功能进行公网和内网间的共享上网的。NAT（Network Address Translator）就是网络地址转换。公网就是普通电信交换网，即现在的网通、电信、铁通等架设的骨干及分支网络，也就是外网、广域网（WAN），就是我们通常所说的Internet，它是一个遍及全世界的网络。

NAT可让局域网用户共享一个公网IP上网

内网就是私网，也就是局域网（LAN），相对于公网、广域网（WAN）而言，主要是指在小范围内的计算机互联网络，这个“小范围”可以是一个家庭宿舍、一所学校、一家公司或者是一个政府部门，可以是两三台联网电脑，也可是数千上万台联网的电脑。其上网的计算机得到的IP地址是Inetrnet上的保留地址，如：10.x.x.x、172.16.x.x至172.31.x.x、192.168.x.x三个网段的地址。  
而NAT的功用就是实现内网的IP地址与公网的地址之间的相互转换，将一个地址段的内网IP地址转换为一个或少量的公网IP地址，减少对公网IP地址的占用。这样在一个局域网内，只需要一台计算机连接上Internet，其它电脑就可以利用NAT网络地址转换共享Internet连接，让局域网内其他计算机也可以上网。
所有ISP（Internet服务提供商）提供的内网Internet接入方式，几乎都是基于NAT协议的。而宽带路由器也是其中的代表产品。但这也就带来一个问题，通过NAT转换得来的数据肯定会被路由设备按需拦截一部分。使用NAT协议，局域网内的计算机可以很顺畅的访问Internet上的资源，但Internet上的其它客户要想访问局域网内的资源却不那么轻松了。  
这是因为，局域网（LAN、私网、内网）内电脑发起的对外连接请求，路由器或网关都不会加以阻拦，但内网的特点就是无法对外打开监听端口，因此会损失所有外部发起的连接。来自广域网对局域网内电脑电脑连接的请求，路由器或网关在绝大多数情况下都会进行拦截。路由器会对来自外部想进入内部网络的信息则会进行识别、筛选，认为是安全的、有效的，才会转发给内网电脑。正是这种情况的存在，才导致了很多通过局域网上的用户P2P下载和传输不能全速。
对此，最直接的解决办法便是DMZ主机和UPnP端口映射两种办法。DMZ可以使某台特定计算机完全向互连网开放（有些应用程序需要开通多个TCP/IP接口，而DMZ就可以为电脑实现这些功能）。但相比之下，UPnP（Universal Plug and Play，通用即插即用）功能更具实用性，它可更好的在WAN和LAN间完成端口映射，实现畅通无阻的上网应用。

UPnP可让网络传输更满速

这是因为，UPnP以Internet标准和技术（例如TCP/IP、HTTP和XML）为基础，不依赖于特定的系统、编程语言或物理媒体，使这样的设备彼此可自动连接和协同工作，从而使网络（尤其是家庭网络）对更多的人成为可能。可以和任何网络媒体技术（有线或无线）协同使用。在网络控制设备的管理下，它支持任何两个设备之间的数据通讯。并且UPnP支持零配置网络及自动查找功能，设备可动态加入网络，获取IP地址，根据需要提供功能。  
如BT等P2P软件支持UPnP自动端口映射，便可以在本机上自动完成网关端口映射的操作，可以在不作任何配置的情况下自动在网关上打开对外端口，速度自然就可得到提升。

# 二、UPnP详细设置
UPnP已在DSL和Cable路由MODEM，以及各种有线和无线宽带路由器中被广泛支持，在新版Windows中也得到了支持，并在各种P2P下载软件以及MSN Messenger等通信软件中得到了应用。而该如何启用UPnP功能呢，这需要从系统、设备、相关软件三方面下手：
## 1、主流系统中的设置
支持UPnP的系统有：Windows XP SP1、SP2，Linux和Windows 2003、Vista等。
以Windows XP为例，Windows XP已对UPnP提供了完备的支持，但UPnP模块在默认状态下并没有被安装，所以将其安装上即可。

开启Windows XP对UPnP的支持

具体步履是：用鼠标左键依次点开“开始→控制面板→添加或删除程序”，选择“添加/删除Windows组件”，在“Windows组件向导”中选择“网络服务”，再选“详细信息”，在该界面中的“Internet网关设备发现和控制客户端”、“UPnP用户界面”或UPnP或“通用即插即用”选项前打上勾，最后点“确定”，系统将自动安装UPnP模块。  
再以最新的操作系统Windows Vista为例，Windows Vista中将UPnP改名为了“网络发现”——网络发现是一种网络设置，该设置会影响您的计算机是否可以查看（找到）网络上的其他计算机和设置，以及网络上的其他计算机是否可以查看您的计算机。  
启用“网络发现”将允许您的计算机查看其他网络计算机和设备，并允许其他网络计算机上的人可以查看您的计算机，这使共享文件和打印机变得更加容易。  Vista默认情况下，Windows防火墙阻止了网络发现功能，要启用该功能，可单击“开始→控制面板→网络和Internet”选项，单击“网络和共享中心”，单击“启用网络发现”，然后单击“应用”即可。

## 2、路由设备中的设置
出于安全考虑，多数路由器（包含带路由的各种宽带MODEM、宽带路由器和无线路由器）的UPnP功能默认都是关闭的，要想使用UPnP功能，将其开启即可。

在各种宽带路由设备中，启用UPnP功能都很方便。进入路由器的WEB配置页面，找到UPnP选项，将其设置为“开启”即可。

开启UPnP功能后，网上邻居中可见路由器名称

打开路由器的UPnP功能后，Windows便会自动找到新的UPnP硬件，并安装它。这时在网上邻居“本地网络”中便可看见该路由的名称。

## 3、P2P软件中的设置
P2P软件大多支持UPnP自动端口映射，可以在本机上自动完成网关端口映射的操作。并且多数这类软件可以在不作任何配置的情况下自动在网关上打开对外端口，让传输速度更快。  
例如在MSN Messenger中你可以查看你连接到Internet的方式以及您是否有足够的权限全速使用MSN Messenger的文件传输、语音和视频会议等功能。具体方法是在“工具”菜单上，单击“选项”，然后单击“连接”选项卡，查看“连接状态”下的信息。  
如果是以下三个选项，基本表明你可以全速连接——直接连接，表明可以完整的使用语音和视频会议功能；通用即插即用（UPnP）和网络地址转换设备（NAT），表明可以使用语音和视频对话功能，但可能会受一些外部因素的影响，如路由器性能；UPnP防火墙，表明语音、视频对话和网络摄像机功能可以使用，但文件传输速度可能会慢于你的Internet连接速度。

比特精灵对UPnP有完善的支持

除此而外，象迅雷（Thunder）、eMule VeryCD（电驴）、比特彗星（BitComet）、比特精灵（BitSpirit）、影音传送带（Net Transpor）、脱兔TuoTu等P2P软件都支持内网UPnP自动端口映射的功能（如Bitcomet的UPnP框架映射端口、eMule的UPnP随机端口映射、脱兔Tuotu的UPnP自动映射与手工添加等），并默认打开了该功能，可自动判断您的路由器是否支持UPnP自动端口映射，从而自动为用户实现UPnP端口映射。并且这类软件一般还具有独特的内网穿透的功能，能穿透防火墙，让不同局域网的用户直接建立UDP/TCP连接，大大提高内网用户的传输质量。  
以迅雷为例，新版迅雷增加了UPnP支持的NET设备类型，即其UPnP将支持更多的网络设备。有了它，我们就可以更好地突破内网限制，穿透能力更强，也能够连接到更多的资源，其下载速度自然也会更快。其设置也很简单，选择“工具→配置”，再单击“BT/端口设置”，然后在下方便可以设置“允许使用UPnP自动端口映射功能”。  
而象PPS、PPLive等P2P网络电视同样支持UPnP功能，可自动查找打开路由器中的UPnP功能。以PPS为例，其设置方法是打开PPS→工具→选项→连接设置→使用固定端口，选择“UPnP设置”页，点“查找UPnP设备”，在“启用ppstream的UPnP支持”前打勾即可。  
而PPLive的UPnP设置同样简单，在任务栏的PPLive图标上面右键单击，选择“工具→设置→网络设置”，勾选 “UPnP开启”，点击确定即可。

哪些软件正在使用UPnP在路由器中一目了然

这些软件的UPnP自动端口映射功能打开后，这些软件在使用时在路由器的UPnP界面中就可看见其相关的信息。
