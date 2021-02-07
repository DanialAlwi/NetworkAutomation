import netmiko


host = "192.168.0.1"
login_device = "cisco"
pass_device = "cisco123"
device = "cisco_ios"

conn = netmiko.ConnectHandler(ip= host, device_type=device, username=login_device, password=pass_device)

interface = input("Interface : ")
ipAddr = input("ip :")
mask = input("mask :")


conf = ["int " + interface,
	"ip add " + ipAddr + " " + mask,
	"no shut",
       ]

print(conn.send_config_set(conf))
print(conn.send_command("sh ip int br"))
conn.disconnect()
