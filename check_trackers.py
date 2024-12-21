import socket
import asyncio
import aiohttp

def is_tcp_tracker_available(address):
    try:
        host, port = address.split(":")
        #删除端口后面斜杠
        if "/" in port:
            port = port.split("/")[0]
        with socket.create_connection((host, int(port)), timeout=5):
            return True
    except Exception:
        return False

async def is_udp_tracker_available(address):
    try:
        host, port = address[6:].split(":")  # Remove "udp://" prefix
        if "/" in port:
            port = port.split("/")[0]
        port = int(port)

        loop = asyncio.get_event_loop()
        transport, protocol = await loop.create_datagram_endpoint(
            lambda: asyncio.DatagramProtocol(),
            remote_addr=(host, port)
        )
        transport.close()
        return True
    except Exception:
        return False

async def check_trackers(tracker_list):
    valid_trackers = []

    for tracker in tracker_list:
        #检查当前 tracker 是否已经是有效的 tracker
        if tracker in valid_trackers:
            continue
        print("Checking:", tracker)
        if tracker.startswith("udp://"):
            if await is_udp_tracker_available(tracker):
                valid_trackers.append(tracker)
        elif tracker.startswith("http://"):
            if is_tcp_tracker_available(tracker[7:]):
                valid_trackers.append(tracker)
        elif tracker.startswith("https://"):
            if is_tcp_tracker_available(tracker[8:]):
                valid_trackers.append(tracker)
        elif tracker.startswith("tcp://"):
            if is_tcp_tracker_available(tracker[6:]):
                valid_trackers.append(tracker)

    #返回有效的tracker
    return valid_trackers

if __name__ == "__main__":
    #读取trackers.txt文件,改成自己的路径
    with open("C:\\Users\\33192\\Desktop\\project\\check\\trackers.txt", "r") as file:
        tracker_list = [line.strip() for line in file.readlines() if line.strip()]

    valid_trackers = asyncio.run(check_trackers(tracker_list))

    print("Valid trackers:",valid_trackers.__len__())
    for tracker in valid_trackers:
        print(tracker)