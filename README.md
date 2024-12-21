# Tracker 地址可用性检查

该脚本用于检查一组 Tracker 地址的可用性，支持 UDP 和 TCP 协议。如果你的 Tracker 地址列表非常庞大，不想一个个手动检查，可以使用此脚本自动化完成该任务。

### 安装依赖
在运行脚本之前，确保已经安装了 `aiohttp` 外部库。可以使用以下命令安装：

```pip install aiohttp```

### 使用步骤
1. 下载或创建一个包含 Tracker 地址的 trackers.txt 文件，每行一个地址。
2. 在脚本中更新 trackers.txt 文件的路径。
3. 脚本准备好后，使用以下命令运行：

```python check_trackers.py```

脚本将会检查每个地址的可用性，并在检查完毕后输出有效的地址。

### 注意事项
- 请确保 trackers.txt 文件格式正确，每行一个 Tracker 地址。
- 脚本会异步地检查多个地址，提高检查效率。
- 有效的 Tracker 地址将被打印到控制台。
