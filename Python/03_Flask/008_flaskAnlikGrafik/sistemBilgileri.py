# https://www.thepythoncode.com/article/get-hardware-system-information-python
 
import psutil
import platform
from datetime import datetime

def birimDonusturucu(bytes, sonEK="B"):
    """
    Baytları doğru biçimine ölçeklendirme
    örn:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    etken = 1024
    for birim in ["", "K", "M", "G", "T", "P"]:
        if bytes < etken:
            return f"{bytes:.2f} {birim}{sonEK}"
        bytes /= etken

print("="*40, "Sistem Bilgisi", "="*40)
uname = platform.uname()
print(f"Sistem: {uname.system}")
print(f"Kullanıcı Adı: {uname.node}")
print(f"Sürüm: {uname.release}")
print(f"Versiyon: {uname.version}")
print(f"Makine: {uname.machine}")
print(f"İşlemci: {uname.processor}")

# Boot Zamanı
print("="*40, "Boot Zamanı", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Zamanı: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# CPU Bilgisi
print("="*40, "CPU Bilgisi", "="*40)
# Çekirdek Sayısı
print("Fiziksel Çekirdekler:", psutil.cpu_count(logical=False))
print("Bütün Çekirdekler:", psutil.cpu_count(logical=True))
# CPU Frekansı
cpufreq = psutil.cpu_freq()
print(f"Max Frekans: {cpufreq.max:.2f} Mhz")
print(f"Min Frekans: {cpufreq.min:.2f} Mhz")
print(f"Geçerli Frekans: {cpufreq.current:.2f} Mhz")
# CPU Kullanımı
print("Çekirdek Başına CPU Kullanımı:")
for i, yuzde in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Çekirdek {i}: {yuzde} %")
print(f"Toplam CPU Kullanımı: {psutil.cpu_percent()} %")

# Bellek Bilgisi
print("="*40, "Bellek Bilgisi", "="*40)
# bellek ayrıntılarını al
svmem = psutil.virtual_memory()
print(f"Toplam: {birimDonusturucu(svmem.total)}")
print(f"Mevcut: {birimDonusturucu(svmem.available)}")
print(f"Kullanılan: {birimDonusturucu(svmem.used)}")
print(f"Yüzde: {svmem.percent} %")
print("="*20, "SWAP", "="*20)
# takas belleği ayrıntılarını al (varsa)
swap = psutil.swap_memory()
print(f"Toplam: {birimDonusturucu(swap.total)}")
print(f"Boşta: {birimDonusturucu(swap.free)}")
print(f"Kullanılan: {birimDonusturucu(swap.used)}")
print(f"Yüzde: {swap.percent} %")

# Disk Bilgileri
print("="*40, "Disk Bilgileri", "="*40)
print("Bölümler ve Kullanımı:")
# disk bölümlerini al
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Cihaz: {partition.device} ===")
    print(f"  Bağlama noktası: {partition.mountpoint}")
    print(f"  Dosya sistemi türü: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # Bu disk yüzünden yakalanabilir
        # hazır değil
        continue
    print(f"  Toplam Boyut: {birimDonusturucu(partition_usage.total)}")
    print(f"  Kullanılan: {birimDonusturucu(partition_usage.used)}")
    print(f"  Boşta: {birimDonusturucu(partition_usage.free)}")
    print(f"  Yüzde: {partition_usage.percent} %")
# önyüklemeden beri IO istatistiklerini al
disk_io = psutil.disk_io_counters()
print(f"Toplam okuma: {birimDonusturucu(disk_io.read_bytes)}")
print(f"Toplam yazma: {birimDonusturucu(disk_io.write_bytes)}")

# Ağ Bilgisi
print("="*40, "Ağ Bilgisi", "="*40)
# tüm ağ arayüzlerini edinin (sanal ve fiziksel)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Arayüz: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Adresi: {address.address}")
            print(f"  Ağ Maskesi: {address.netmask}")
            print(f"  IP Yayını: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Adresi: {address.address}")
            print(f"  Ağ Maskesi: {address.netmask}")
            print(f"  MAC Yayını: {address.broadcast}")
# önyüklemeden beri IO istatistiklerini al
net_io = psutil.net_io_counters()
print(f"Gönderilen Toplam Bayt {birimDonusturucu(net_io.bytes_sent)}")
print(f"Alınan Toplam Bayt: {birimDonusturucu(net_io.bytes_recv)}")