# check_trackers
Tracker地址可用性检查。使用脚本检查 Tracker 列表中的地址是否可用，包括udp以及tcp协议。<br>
苦于Tracker地址过多，不想挨个排查，使用gpt辅助生成了个批量检查的脚本，最后打印出有效地址。<br>
当前脚本使用了 aiohttp 外部库，需要提前安装 pip install aiohttp <br>
在脚本中需要将trackers.txt文件,改成自己的文件路径 <br>
修改完成后运行脚本：python check_trackers.py
