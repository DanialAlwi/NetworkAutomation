import netmiko 

host = "192.168.0.1"
login_device = "cisco"
pass_device = "cisco123"
device = "cisco_ios"


connection = netmiko.ConnectHandler(ip= host, device_type= device, username= login_device, password = pass_device)

print(connection.send_command("sh ip in br"))
connection.disconnect()
