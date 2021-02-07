import netmiko
import sys
import os

host = "192.168.0.1"
login_device = "cisco"
pass_device = "cisco"
devic = "cisco_ios"

int_num = 0


conn = netmiko.ConnectHandler(ip=host, device_type=device, username=login_device, password=pass_device)


while True:
  choice = input("What do you want to configure? INTERFACE -1 | BGP -2 :")

  while choice != "0":

    def basicConf():
      count = 0
      int_num = input("How many interface :")
      if int_num != "0":
        while int(int_num) > count:
          interface = input("Interface :")
          ipAddr = input("IP :")
          mask = input("Subnet Mask :")


          conf_basic = ["int " + interface,
                        "ip add " + ipAddr + " " + mask,
                        "no shut",
                       ]

          print(conn.send_config_set(conf_basic))
          count+=1
      else:
        re = sys.executable
        os.exec1(re, re, *sys.argv)



    def bgpConf():
      count1 = 0
      count2 = 0
      bgp = input("router bgp : ")
      if bgp != "0":
        n_num = input("Number of neighbor : ")
        net_num = input("Number of network : ")

        if n_num != "0":
          while int(n_num) > count1:
            neighbor = input("Enter neighbor : ")
            rem_as = input("Enter Autonomus System (AS) :")
            conf _bgp = ["router bgp " + bgp,
                         "neighbor " + neighbor + " remote-as " + rem_as,
                        ]
            print(conn.send_config_set(conf_bgp))
            count1+=1
        else:
          print("Proceed with Assign Network ")

        if net_num != "0":
          while int(net_num) > count2:
            net = input("Enter Network IP : ")
            mask1 = input("Enter Mask : ")
            conf_bgp1 = ["router bgp " + bgp,
                         "network " + net + " mask " + mask1,
                        ]
            print(conn.send_config_set(conf_bgp1))
            count2+=1
        else:

          re = sys.executable
          os.exec1(re, re, *sys.argv)
      else:
        re = sys.executable
        os.exec1(re, re, *sys.argv)


    def show():
      print(conn.send_command("sh ip int br"))



    if choice == "1":
      basicConf()

    elif choice == "2":
      basiConf() 


    else:
      print("INVALID OPTION!! ")
      show()
      conn.disconnect()
      sys.exit()


conn.disconnect()
