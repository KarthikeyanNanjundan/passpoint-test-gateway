import serial
from time import sleep
from gateway_serial import send_to_console
from gateway_serial import ser


class passpoint_library():
    def passpoint_default_values():
        print("Collecting Passpoint default values\n")
        print("dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable",
                        wait_time=1)
        sleep(1)

    def default_proxyarp_XB3():
        print("iwpriv ath8 get_proxyarp\n")
        send_to_console(ser, "iwpriv ath8 get_proxyarp", wait_time=1)
        sleep(1)
        print("\niwpriv ath9 get_proxyarp\n")
        send_to_console(ser, "iwpriv ath9 get_proxyarp", wait_time=1)
        sleep(1)

    def default_proxyarp_XB6():
        print("wifi_api wifi_getProxyArp 8\n")
        send_to_console(ser, "wifi_api wifi_getProxyArp 8", wait_time=1)
        sleep(1)
        print("\nwifi_api wifi_getProxyArp 9\n")
        send_to_console(ser, "wifi_api wifi_getProxyArp 9", wait_time=1)
        sleep(1)

        print("qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
        send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
        sleep(1)
        print("\nqcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
        send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
        sleep(1)

    def enable_xfinity():
        print("\ndmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy int 44\n")
        send_to_console(ser, "dmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy int 44", wait_time=1)
        sleep(1)
        print("\ndmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint string 68.85.15.164\n")
        send_to_console(ser, "dmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint string "
                             "68.85.15.164", wait_time=1)
        sleep(1)
        print("\ndmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint string 68.85.15.238\n")
        send_to_console(ser, "dmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint string "
                             "68.85.15.238", wait_time=1)
        sleep(1)
        print("\ndmcli eRT setvalues Device.WiFi.SSID.9.SSID string 0_Passpoint_Automation9"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.SSIDAdvertisementEnabled bool true"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.IsolationEnable bool true"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.X_CISCO_COM_EncryptionMethod string AES"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.ModeEnabled string WPA2-Enterprise"
              "dmcli eRT setvalues Device.WiFi.SSID.9.Enable bool true"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusServerIPAddr string 96.114.36.109"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusServerPort uint 1812"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'"
              "dmcli eRT setv Device.WiFi.AccessPoint.9.X_CISCO_COM_BssMaxNumSta int 6"
              "dmcli eRT setvalues Device.WiFi.SSID.10.SSID string 0_Passpoint_Automation10"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.SSIDAdvertisementEnabled bool true"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.IsolationEnable bool true"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.X_CISCO_COM_EncryptionMethod string AES"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.ModeEnabled string WPA2-Enterprise"
              "dmcli eRT setvalues Device.WiFi.SSID.10.Enable bool true"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusServerIPAddr string 96.114.36.109"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusServerPort uint 1812"
              "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'"
              "dmcli eRT setv Device.WiFi.AccessPoint.10.X_CISCO_COM_BssMaxNumSta int 5"
              "dmcli eRT setvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable bool true"
              "dmcli eRT setv Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting bool true"
              "dmcli eRT setv Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting bool true"
              "dmcli eRT getvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable\n")
        send_to_console(ser,
                        "dmcli eRT setvalues Device.WiFi.SSID.9.SSID string  0_Passpoint_Automation9; sleep 1; dmcli "
                        "eRT setvalues Device.WiFi.AccessPoint.9.SSIDAdvertisementEnabled bool true; sleep 1; dmcli "
                        "eRT setvalues Device.WiFi.AccessPoint.9.IsolationEnable bool true; sleep 1; dmcli eRT "
                        "setvalues Device.WiFi.AccessPoint.9.Security.X_CISCO_COM_EncryptionMethod string AES; sleep "
                        "1; dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.ModeEnabled string "
                        "WPA2-Enterprise; sleep 1; dmcli eRT setvalues Device.WiFi.SSID.9.Enable bool true; sleep 1; "
                        "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusServerIPAddr string "
                        "96.114.36.109; sleep 1; dmcli eRT setvalues "
                        "Device.WiFi.AccessPoint.9.Security.RadiusServerPort uint 1812; sleep 1; dmcli eRT setvalues "
                        "Device.WiFi.AccessPoint.9.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'; sleep 1; "
                        "dmcli eRT setv Device.WiFi.AccessPoint.9.X_CISCO_COM_BssMaxNumSta int 6; sleep 1;"
                        "dmcli eRT setvalues Device.WiFi.SSID.10.SSID string  0_Passpoint_Automation10; sleep 1; "
                        "dmcli eRT setvalues Device.WiFi.AccessPoint.10.SSIDAdvertisementEnabled bool true; sleep 1; "
                        "dmcli eRT setvalues Device.WiFi.AccessPoint.10.IsolationEnable bool true; sleep 1; dmcli "
                        "eRT setvalues Device.WiFi.AccessPoint.10.Security.X_CISCO_COM_EncryptionMethod string AES; "
                        "sleep 1; dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.ModeEnabled string "
                        "WPA2-Enterprise; sleep 1; dmcli eRT setvalues Device.WiFi.SSID.10.Enable bool true; sleep "
                        "1; dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusServerIPAddr string "
                        "96.114.36.109; sleep 1; dmcli eRT setvalues "
                        "Device.WiFi.AccessPoint.10.Security.RadiusServerPort uint 1812; sleep 1; dmcli eRT "
                        "setvalues Device.WiFi.AccessPoint.10.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'; "
                        "sleep 1; dmcli eRT setv Device.WiFi.AccessPoint.10.X_CISCO_COM_BssMaxNumSta int 6; sleep 1;"
                        "dmcli eRT setvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable bool true; sleep 1; "
                        "dmcli eRT setv Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting bool true; sleep 5; dmcli eRT "
                        "setv Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting bool true; sleep 5; dmcli eRT getvalues "
                        "Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable;", wait_time=30)
        sleep(30)

    def enable_interworking():
        print("\ndmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingApplySettings bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingApplySettings bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingApplySettings bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingApplySettings bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters string '{"
              "\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, \"IPv4AddressType\":3}, "
              "\"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, \"Name\": \"xfinity.com\" }]}, "
              "\"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, \"RealmEncoding\": 1, \"RealmLength\": 11, "
              "\"Realms\": \"xfinity.com\", \"EAPCount\": 1, \"EAP\": [{\"Length\": 5, \"Method\": 21, "
              "\"ParameterCount\": 1, \"AuthenticationParameter\": [{\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, "
              "\"3GPPCellularANQPElement\":{ \"GUD\":0, \"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, "
              "\"RoamingConsortiumANQPElement\": { \"OI\": [{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ "
              "\"VenueInfo\":[{ \"Length\": 7, \"Language\": \"eng\", \"Name\": \"resi\" }]}}}'\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters string "
                        "'{\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, "
                        "\"IPv4AddressType\":3}, \"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, "
                        "\"Name\": \"xfinity.com\" }]}, \"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, "
                        "\"RealmEncoding\": 1, \"RealmLength\": 11, \"Realms\": \"xfinity.com\", \"EAPCount\": 1, "
                        "\"EAP\": [{\"Length\": 5, \"Method\": 21, \"ParameterCount\": 1, \"AuthenticationParameter\": [{"
                        "\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, \"3GPPCellularANQPElement\":{ \"GUD\":0, "
                        "\"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, \"RoamingConsortiumANQPElement\": { \"OI\": ["
                        "{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ \"VenueInfo\":[{ \"Length\": 7, "
                        "\"Language\": \"eng\", \"Name\": \"resi\" }]}}}'",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters string '{"
              "\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, \"IPv4AddressType\":3}, "
              "\"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, \"Name\": \"xfinity.com\" }]}, "
              "\"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, \"RealmEncoding\": 1, \"RealmLength\": 11, "
              "\"Realms\": \"xfinity.com\", \"EAPCount\": 1, \"EAP\": [{\"Length\": 5, \"Method\": 21, "
              "\"ParameterCount\": 1, \"AuthenticationParameter\": [{\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, "
              "\"3GPPCellularANQPElement\":{ \"GUD\":0, \"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, "
              "\"RoamingConsortiumANQPElement\": { \"OI\": [{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ "
              "\"VenueInfo\":[{ \"Length\": 7, \"Language\": \"eng\", \"Name\": \"resi\" }]}}}'\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters string "
                        "'{\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, "
                        "\"IPv4AddressType\":3}, \"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, "
                        "\"Name\": \"xfinity.com\" }]}, \"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, "
                        "\"RealmEncoding\": 1, \"RealmLength\": 11, \"Realms\": \"xfinity.com\", \"EAPCount\": 1, "
                        "\"EAP\": [{\"Length\": 5, \"Method\": 21, \"ParameterCount\": 1, \"AuthenticationParameter\": [{"
                        "\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, \"3GPPCellularANQPElement\":{ \"GUD\":0, "
                        "\"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, \"RoamingConsortiumANQPElement\": { \"OI\": ["
                        "{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ \"VenueInfo\":[{ \"Length\": 7, "
                        "\"Language\": \"eng\", \"Name\": \"resi\" }]}}}'",
                        wait_time=1)
        sleep(1)

    def set_passpoint():
        print("\ndmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable bool true\n")
        send_to_console(ser,
                        "dmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable bool true\n")
        send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable bool true",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable bool true\n")
        send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable bool true",
                        wait_time=1)
        sleep(1)
        print(
            "\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters string '{\"Passpoint\":{ "
            "\"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{\"Encoding\": 0, \"NameLength\": 11, "
            "\"Name\": \"xfinity.com\"}]}, \"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, "
            "\"LanguageCode\": \"eng\", \"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{"
            "\"ProtoPort\":[{\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
            "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, \"P2pCrossConnectionDisable\":true}}}'\n")
        send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters string '{"
                             "\"Passpoint\":{ \"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{"
                             "\"Encoding\": 0, \"NameLength\": 11, \"Name\": \"xfinity.com\"}]}, "
                             "\"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, \"LanguageCode\": \"eng\", "
                             "\"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{\"ProtoPort\":[{"
                             "\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
                             "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, "
                             "\"P2pCrossConnectionDisable\":true}}}'", wait_time=1)
        sleep(1)
        print(
            "\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters string '{\"Passpoint\":{ "
            "\"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{\"Encoding\": 0, \"NameLength\": 11, "
            "\"Name\": \"xfinity.com\"}]}, \"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, "
            "\"LanguageCode\": \"eng\", \"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{"
            "\"ProtoPort\":[{\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
            "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, \"P2pCrossConnectionDisable\":true}}}'\n")
        send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters string '{"
                             "\"Passpoint\":{ \"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{"
                             "\"Encoding\": 0, \"NameLength\": 11, \"Name\": \"xfinity.com\"}]}, "
                             "\"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, \"LanguageCode\": \"eng\", "
                             "\"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{\"ProtoPort\":[{"
                             "\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
                             "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, "
                             "\"P2pCrossConnectionDisable\":true}}}'", wait_time=1)
        sleep(1)

    def get_passpoint():
        print("Collecting Passpoint default values\n")
        print("dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters",
                        wait_time=1)
        sleep(1)

    def get_tunnel():
        print("dmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint\n")
        send_to_console(ser, "dmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint",
                        wait_time=1)
        sleep(1)
        print("\ndmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint\n")
        send_to_console(ser, "dmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint",
                        wait_time=1)
        sleep(1)

    def get_proxyarp_XB3():
        print("iwpriv ath8 get_proxyarp\n")
        send_to_console(ser, "iwpriv ath8 get_proxyarp", wait_time=1)
        sleep(1)
        print("\niwpriv ath9 get_proxyarp\n")
        send_to_console(ser, "iwpriv ath9 get_proxyarp", wait_time=1)
        sleep(1)

    def get_proxyarp_XB6():
        print("wifi_api wifi_getProxyArp 8\n")
        send_to_console(ser, "wifi_api wifi_getProxyArp 8", wait_time=1)
        sleep(1)
        print("\nwifi_api wifi_getProxyArp 9\n")
        send_to_console(ser, "wifi_api wifi_getProxyArp 9", wait_time=1)
        sleep(1)

        print("qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
        send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
        sleep(1)
        print("\nqcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
        send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
        sleep(1)

    def get_WANMetrics():
        print("dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.WANMetrics\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.WANMetrics",
                        wait_time=1)
        sleep(1)
        print("dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.WANMetrics\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.WANMetrics",
                        wait_time=1)
        sleep(1)

    def get_passpoint_stats():
        print("dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Stats\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Stats", wait_time=1)
        sleep(1)
        print("dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Stats\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Stats", wait_time=1)
        sleep(1)

    def get_PAM_WiFi_log():
        print("cat /rdklogs/logs/PAMlog.txt.0 | grep -i passpoint\n")
        send_to_console(ser, "cat /rdklogs/logs/PAMlog.txt.0 | grep -i passpoint", wait_time=2)
        sleep(2)
        print("cat /rdklogs/logs/WiFilog.txt.0 | grep -i passpoint\n")
        send_to_console(ser, "cat /rdklogs/logs/WiFilog.txt.0 | grep -i passpoint", wait_time=2)
        sleep(2)

    def get_xfinity_interworking():
        print("dmcli eRT getvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable\n")
        send_to_console(ser, "dmcli eRT getvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable", wait_time=1)
        sleep(1)
        print("Checking if tunnel is up and running....\n")
        send_to_console(ser, "brctl show", wait_time=1)
        sleep(1)
        print("dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable\n")
        send_to_console(ser, "dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable",
                        wait_time=1)
        sleep(1)
        print("dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters\n")
        send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters",
                        wait_time=1)
        sleep(1)
        print("dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters\n")
        send_to_console(ser,
                        "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters",
                        wait_time=1)
        sleep(1)

    def gateway_tcpdump():
        print("\ntcpdump -i erouter0 port 1812 or 1813 or 3799 -vvvvv -w /tmp/tcpdump_Automation.pcap\n")
        send_to_console(ser, "nohup tcpdump -i erouter0 port 1812 or 1813 or 3799 -vvvvv -w "
                             "/tmp/tcpdump_Automation.pcap &", wait_time=1)
        sleep(2)
        send_to_console(ser, "nohup tcpdump -i erouter0 port radius -A -vvvvv -X -s0 | tee /tmp/tcp_dump_log.txt &",
                        wait_time=1)




# @classmethod
# def passpoint_default_values():
#     print("Collecting Passpoint default values\n")
#     print("dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable",
#                     wait_time=1)
#
#
# def default_proxyarp_XB3():
#     print("iwpriv ath8 get_proxyarp\n")
#     send_to_console(ser, "iwpriv ath8 get_proxyarp", wait_time=1)
#     print("\niwpriv ath9 get_proxyarp\n")
#     send_to_console(ser, "iwpriv ath9 get_proxyarp", wait_time=1)
#
#
# def default_proxyarp_XB6():
#     print("wifi_api wifi_getProxyArp 8\n")
#     send_to_console(ser, "wifi_api wifi_getProxyArp 8", wait_time=1)
#     print("\nwifi_api wifi_getProxyArp 9\n")
#     send_to_console(ser, "wifi_api wifi_getProxyArp 9", wait_time=1)
#
#     print("qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
#     send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
#     print("\nqcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
#     send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
#
#
# def enable_xfinity():
#     print("\ndmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy int 44\n")
#     send_to_console(ser, "dmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy int 44", wait_time=1)
#     print("\ndmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint string 68.85.15.164\n")
#     send_to_console(ser, "dmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint string "
#                          "68.85.15.164", wait_time=1)
#     print("\ndmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint string 68.85.15.238\n")
#     send_to_console(ser, "dmcli eRT setvalues Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint string "
#                          "68.85.15.238", wait_time=1)
#     print("\ndmcli eRT setvalues Device.WiFi.SSID.9.SSID string 0_Passpoint_Automation9"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.SSIDAdvertisementEnabled bool true"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.IsolationEnable bool true"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.X_CISCO_COM_EncryptionMethod string AES"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.ModeEnabled string WPA2-Enterprise"
#           "dmcli eRT setvalues Device.WiFi.SSID.9.Enable bool true"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusServerIPAddr string 96.114.36.109"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusServerPort uint 1812"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'"
#           "dmcli eRT setv Device.WiFi.AccessPoint.9.X_CISCO_COM_BssMaxNumSta int 6"
#           "dmcli eRT setvalues Device.WiFi.SSID.10.SSID string 0_Passpoint_Automation10"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.SSIDAdvertisementEnabled bool true"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.IsolationEnable bool true"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.X_CISCO_COM_EncryptionMethod string AES"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.ModeEnabled string WPA2-Enterprise"
#           "dmcli eRT setvalues Device.WiFi.SSID.10.Enable bool true"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusServerIPAddr string 96.114.36.109"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusServerPort uint 1812"
#           "dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'"
#           "dmcli eRT setv Device.WiFi.AccessPoint.10.X_CISCO_COM_BssMaxNumSta int 5"
#           "dmcli eRT setvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable bool true"
#           "dmcli eRT setv Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting bool true"
#           "dmcli eRT setv Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting bool true"
#           "dmcli eRT getvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable\n")
#     send_to_console(ser, "dmcli eRT setvalues Device.WiFi.SSID.9.SSID string  0_Passpoint_Automation9; sleep 1; dmcli "
#                          "eRT setvalues Device.WiFi.AccessPoint.9.SSIDAdvertisementEnabled bool true; sleep 1; dmcli "
#                          "eRT setvalues Device.WiFi.AccessPoint.9.IsolationEnable bool true; sleep 1; dmcli eRT "
#                          "setvalues Device.WiFi.AccessPoint.9.Security.X_CISCO_COM_EncryptionMethod string AES; sleep "
#                          "1; dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.ModeEnabled string "
#                          "WPA2-Enterprise; sleep 1; dmcli eRT setvalues Device.WiFi.SSID.9.Enable bool true; sleep 1; "
#                          "dmcli eRT setvalues Device.WiFi.AccessPoint.9.Security.RadiusServerIPAddr string "
#                          "96.114.36.109; sleep 1; dmcli eRT setvalues "
#                          "Device.WiFi.AccessPoint.9.Security.RadiusServerPort uint 1812; sleep 1; dmcli eRT setvalues "
#                          "Device.WiFi.AccessPoint.9.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'; sleep 1; "
#                          "dmcli eRT setv Device.WiFi.AccessPoint.9.X_CISCO_COM_BssMaxNumSta int 6; sleep 1;"
#                          "dmcli eRT setvalues Device.WiFi.SSID.10.SSID string  0_Passpoint_Automation10; sleep 1; "
#                          "dmcli eRT setvalues Device.WiFi.AccessPoint.10.SSIDAdvertisementEnabled bool true; sleep 1; "
#                          "dmcli eRT setvalues Device.WiFi.AccessPoint.10.IsolationEnable bool true; sleep 1; dmcli "
#                          "eRT setvalues Device.WiFi.AccessPoint.10.Security.X_CISCO_COM_EncryptionMethod string AES; "
#                          "sleep 1; dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.ModeEnabled string "
#                          "WPA2-Enterprise; sleep 1; dmcli eRT setvalues Device.WiFi.SSID.10.Enable bool true; sleep "
#                          "1; dmcli eRT setvalues Device.WiFi.AccessPoint.10.Security.RadiusServerIPAddr string "
#                          "96.114.36.109; sleep 1; dmcli eRT setvalues "
#                          "Device.WiFi.AccessPoint.10.Security.RadiusServerPort uint 1812; sleep 1; dmcli eRT "
#                          "setvalues Device.WiFi.AccessPoint.10.Security.RadiusSecret string 'tCnx3DrzP!kZfhM8vbiJ'; "
#                          "sleep 1; dmcli eRT setv Device.WiFi.AccessPoint.10.X_CISCO_COM_BssMaxNumSta int 6; sleep 1;"
#                          "dmcli eRT setvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable bool true; sleep 1; "
#                          "dmcli eRT setv Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting bool true; sleep 5; dmcli eRT "
#                          "setv Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting bool true; sleep 5; dmcli eRT getvalues "
#                          "Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable;", wait_time=1)
#
#
# def enable_interworking():
#     print("\ndmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingElement.ASRA bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingApplySettings bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingApplySettings bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingApplySettings bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingApplySettings bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters string '{"
#           "\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, \"IPv4AddressType\":3}, "
#           "\"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, \"Name\": \"xfinity.com\" }]}, "
#           "\"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, \"RealmEncoding\": 1, \"RealmLength\": 11, "
#           "\"Realms\": \"xfinity.com\", \"EAPCount\": 1, \"EAP\": [{\"Length\": 5, \"Method\": 21, "
#           "\"ParameterCount\": 1, \"AuthenticationParameter\": [{\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, "
#           "\"3GPPCellularANQPElement\":{ \"GUD\":0, \"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, "
#           "\"RoamingConsortiumANQPElement\": { \"OI\": [{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ "
#           "\"VenueInfo\":[{ \"Length\": 7, \"Language\": \"eng\", \"Name\": \"resi\" }]}}}'\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters string "
#                     "'{\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, "
#                     "\"IPv4AddressType\":3}, \"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, "
#                     "\"Name\": \"xfinity.com\" }]}, \"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, "
#                     "\"RealmEncoding\": 1, \"RealmLength\": 11, \"Realms\": \"xfinity.com\", \"EAPCount\": 1, "
#                     "\"EAP\": [{\"Length\": 5, \"Method\": 21, \"ParameterCount\": 1, \"AuthenticationParameter\": [{"
#                     "\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, \"3GPPCellularANQPElement\":{ \"GUD\":0, "
#                     "\"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, \"RoamingConsortiumANQPElement\": { \"OI\": ["
#                     "{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ \"VenueInfo\":[{ \"Length\": 7, "
#                     "\"Language\": \"eng\", \"Name\": \"resi\" }]}}}'",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters string '{"
#           "\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, \"IPv4AddressType\":3}, "
#           "\"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, \"Name\": \"xfinity.com\" }]}, "
#           "\"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, \"RealmEncoding\": 1, \"RealmLength\": 11, "
#           "\"Realms\": \"xfinity.com\", \"EAPCount\": 1, \"EAP\": [{\"Length\": 5, \"Method\": 21, "
#           "\"ParameterCount\": 1, \"AuthenticationParameter\": [{\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, "
#           "\"3GPPCellularANQPElement\":{ \"GUD\":0, \"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, "
#           "\"RoamingConsortiumANQPElement\": { \"OI\": [{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ "
#           "\"VenueInfo\":[{ \"Length\": 7, \"Language\": \"eng\", \"Name\": \"resi\" }]}}}'\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters string "
#                     "'{\"ANQP\":{ \"IPAddressTypeAvailabilityANQPElement\":{ \"IPv6AddressType\":2, "
#                     "\"IPv4AddressType\":3}, \"DomainANQPElement\":{\"DomainName\":[{\"Length\": 11, "
#                     "\"Name\": \"xfinity.com\" }]}, \"NAIRealmANQPElement\":{\"Realm\":[{\"DataFieldLength\": 20, "
#                     "\"RealmEncoding\": 1, \"RealmLength\": 11, \"Realms\": \"xfinity.com\", \"EAPCount\": 1, "
#                     "\"EAP\": [{\"Length\": 5, \"Method\": 21, \"ParameterCount\": 1, \"AuthenticationParameter\": [{"
#                     "\"Length\": 1, \"ID\": 2, \"Value\": \"01\" }]}]}]}, \"3GPPCellularANQPElement\":{ \"GUD\":0, "
#                     "\"PLMN\":[{\"MCC\": \"313\", \"MNC\": \"390\" }]}, \"RoamingConsortiumANQPElement\": { \"OI\": ["
#                     "{ \"OI\": \"506f9a\" }]}, \"VenueNameANQPElement\":{ \"VenueInfo\":[{ \"Length\": 7, "
#                     "\"Language\": \"eng\", \"Name\": \"resi\" }]}}}'",
#                     wait_time=1)
#
#
# def set_passpoint():
#     print("\ndmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable bool true\n")
#     send_to_console(ser,
#                     "dmcli eRT setv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable bool true\n")
#     send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable bool true\n")
#     send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable bool true",
#                     wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters string '{\"Passpoint\":{ "
#           "\"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{\"Encoding\": 0, \"NameLength\": 11, "
#           "\"Name\": \"xfinity.com\"}]}, \"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, "
#           "\"LanguageCode\": \"eng\", \"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{"
#           "\"ProtoPort\":[{\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
#           "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, \"P2pCrossConnectionDisable\":true}}}'\n")
#     send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters string '{"
#                          "\"Passpoint\":{ \"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{"
#                          "\"Encoding\": 0, \"NameLength\": 11, \"Name\": \"xfinity.com\"}]}, "
#                          "\"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, \"LanguageCode\": \"eng\", "
#                          "\"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{\"ProtoPort\":[{"
#                          "\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
#                          "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, "
#                          "\"P2pCrossConnectionDisable\":true}}}'", wait_time=1)
#     print("\ndmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters string '{\"Passpoint\":{ "
#           "\"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{\"Encoding\": 0, \"NameLength\": 11, "
#           "\"Name\": \"xfinity.com\"}]}, \"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, "
#           "\"LanguageCode\": \"eng\", \"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{"
#           "\"ProtoPort\":[{\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
#           "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, \"P2pCrossConnectionDisable\":true}}}'\n")
#     send_to_console(ser, "dmcli eRT setv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters string '{"
#                          "\"Passpoint\":{ \"PasspointEnable\":true, \"NAIHomeRealmANQPElement\":{\"Realms\":[{"
#                          "\"Encoding\": 0, \"NameLength\": 11, \"Name\": \"xfinity.com\"}]}, "
#                          "\"OperatorFriendlyNameANQPElement\":{\"Name\":[{\"Length\": 7, \"LanguageCode\": \"eng\", "
#                          "\"OperatorName\": \"XFINITY\"}]}, \"ConnectionCapabilityListANQPElement\":{\"ProtoPort\":[{"
#                          "\"IPProtocol\": 1, \"PortNumber\": 0, \"Status\": 1}, {\"IPProtocol\": 2, \"PortNumber\": "
#                          "0, \"Status\": 1}]}, \"GroupAddressedForwardingDisable\":true, "
#                          "\"P2pCrossConnectionDisable\":true}}}'", wait_time=1)
#
#
# def get_passpoint():
#     print("Collecting Passpoint default values\n")
#     print("dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Passpoint.Enable",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Capability",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Capability",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Enable",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Enable",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Parameters",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Parameters",
#                     wait_time=1)
#
#
# def get_tunnel():
#     print("dmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint\n")
#     send_to_console(ser, "dmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint",
#                     wait_time=1)
#     print("\ndmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint\n")
#     send_to_console(ser, "dmcli eRT getv Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint",
#                     wait_time=1)
#
#
# def get_proxyarp_XB3():
#     print("iwpriv ath8 get_proxyarp\n")
#     send_to_console(ser, "iwpriv ath8 get_proxyarp", wait_time=1)
#     print("\niwpriv ath9 get_proxyarp\n")
#     send_to_console(ser, "iwpriv ath9 get_proxyarp", wait_time=1)
#
#
# def get_proxyarp_XB6():
#     print("wifi_api wifi_getProxyArp 8\n")
#     send_to_console(ser, "wifi_api wifi_getProxyArp 8", wait_time=1)
#     print("\nwifi_api wifi_getProxyArp 9\n")
#     send_to_console(ser, "wifi_api wifi_getProxyArp 9", wait_time=1)
#
#     print("qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
#     send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
#     print("\nqcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4\n")
#     send_to_console(ser, "qcsapi_sockraw host0 00:11:22:AB:CD:EE get_proxy_arp wifi2_4", wait_time=1)
#
#
# def get_WANMetrics():
#     print("dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.WANMetrics\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.WANMetrics", wait_time=1)
#     print("dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.WANMetrics\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.WANMetrics", wait_time=1)
#
#
# def get_passpoint_stats():
#     print("dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Stats\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_Passpoint.Stats", wait_time=1)
#     print("dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Stats\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_Passpoint.Stats", wait_time=1)
#
#
# def get_PAM_WiFi_log():
#     print("cat /rdklogs/logs/PAMlog.txt.0 | grep -i passpoint\n")
#     send_to_console(ser, "cat /rdklogs/logs/PAMlog.txt.0 | grep -i passpoint", wait_time=2)
#     print("cat /rdklogs/logs/WiFilog.txt.0 | grep -i passpoint\n")
#     send_to_console(ser, "cat /rdklogs/logs/WiFilog.txt.0 | grep -i passpoint", wait_time=2)
#
#
# def get_xfinity_interworking():
#     print("dmcli eRT getvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable\n")
#     send_to_console(ser, "dmcli eRT getvalues Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable", wait_time=1)
#     print("Checking if tunnel is up and running....\n")
#     send_to_console(ser, "brctl show", wait_time=1)
#     print("dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable\n")
#     send_to_console(ser, "dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable",
#                     wait_time=1)
#     print("dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.9.X_RDKCENTRAL-COM_InterworkingService.Parameters",
#                     wait_time=1)
#     print("dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters\n")
#     send_to_console(ser, "dmcli eRT getv Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters",
#                     wait_time=1)
