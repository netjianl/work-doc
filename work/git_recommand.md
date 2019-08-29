

# 深圳git仓管理

git clone git@192.168.1.249:gitosis-admin

## 修改人员权限 
修改gitosis.conf文件。

## 增加人员
待增加人员生成key对，公钥放到keys目录中即可。

## 删除人员
需要删除keys中的公钥和代码各代码仓列表中名字。其实不删除列表应该也可以。不过还是删了清爽。

## 增加新仓
直接在gitosis.conf中增加即可。本地仓使用git add remote origin git@192.168.1.249:xxx 后git push

## 备份代码仓
根目录下有backup脚本，将所有当前仓备份到本地。如果是第一次运行，需要很长时间。如果代码仓里面随意增加bin档等，后面的时间就更长了。


# git 代码仓管理其他建议

过去的3年时间，大家对git代码仓的使用已经熟练，技能也有提高。现为提高效率，提出以下建议：

## 1 一次编译成功原则
在全新的linux环境下，一个指令，一次选择就可以编译出对应的软件，包括升级文件和烧片文件。  
编译脚本中建议加人包括安装支持库安装，支持软件的下载（从公司ftp服务器）。  
建议交叉编译器一次性编译好，放在ftp服务器上下载，避免每个人都要编译编译器。  
建议定期使用新的虚拟机安装全新的系统，检验是否可以一次编译成功。  

## 2 编译时间最短原则
尽量减少编译时间，合理写好makefile等，编译成功后，第二次编译时间应该尽可能减少， 避免多次编译的时间浪费。  
makefile中依赖clean的做法，应该尽量避免。  
建议每个仓增加编译时间显示，直观了解浪费的时间。

## 3 分支最少原则
git的分支功能强大，容易被过度使用。建议只在以下情况使用分支：  
release分支：当出货版本时，建立release分支，方便以后给特定用户特定程序。  
试验分支：当对完成性不确定，建立试验分支。当确定后，尽快合并到master。  
对于多人在master开发容易冲突，冲突是好事，可以理解为强制交流的一种方式。  

## 4 编译后无红色文件原则
全新下载的代码仓，没有做修改的情况下，编译成功后git status代码仓应该保持clean状态，没有被修改的文件，也没有增加的未跟踪文件。直观的看，就是没有红色的文件。避免有人错误的提交冗余文件

## 5 master最少merge 原则
尽量保持master为单一直线向上，虽然linux创始人不认可rebase的做法，但是对于我们这样的小公司来说，保持master直线，还是最容易理解和跟踪代码历史的方式。

## 6 避免上传bin档原则
避免把文档，编译器，工具一股脑在塞git仓中。如果代码仓过大，导致即使是git status也会非常慢。