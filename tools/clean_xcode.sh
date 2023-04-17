# 此脚本为了清理 xcode 占用的大量磁盘资源

# 清空 CoreSimulator 缓存
rm -rf ~/Library/Developer/CoreSimulator/Caches/*
# 清空 CoreSimulator 的设备，除 device_set.plist 都删除
find ~/Library/Developer/CoreSimulator/Devices/ -mindepth 1 | grep -v device_set.plist | xargs rm -rf
# 删除 XCTestDevices 目录下的测试设备
rm -rf ~/Library/Developer/XCTestDevices/*
