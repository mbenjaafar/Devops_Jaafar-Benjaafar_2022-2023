rack_struc = {
    "rack": [
        {"device": {"dev_name": "RTR1","role": "router", 
                    "interfaces": [
                        {"interface": "GigabitEthernet 0",
                        "ipaddress": "192.0.2.254",
                        "subnetmask": "255.255.255.0"},
                        {"interface": "GigabitEthernet 1",
                        "ipaddress": "10.0.1.1",
                        "subnetmask": "255.255.255.0"},
                        {"interface": "GigabitEthernet 2",
                        "ipaddress": "10.0.2.1",
                        "subnetmask": "255.255.255.0"}
                        ]
                    }
        },
        {"device": {"dev_name": "MLS1","role": "core switch", 
                    "interfaces": [
                        {"interface": "VLAN 1",
                        "ipaddress": "10.0.1.2",
                        "subnetmask": "255.255.255.0"},
                        {"interface": "VLAN 2",
                         "ipaddress": "10.0.2.1",
                         "subnetmask": "255.255.255.0"}
                        ]
                    }
        },
        {"device": {"dev_name": "MLS2","role": "core switch", 
                    "interfaces": [
                        {"interface": "VLAN 1",
                        "ipaddress": "10.0.1.3",
                        "subnetmask": "255.255.255.0"},
                        {"interface": "VLAN 2",
                         "ipaddress": "10.0.2.2",
                         "subnetmask": "255.255.255.0"}
                        ]
                    }
        },
        {"device": {"dev_name": "ASW2","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 1",
                        "ipaddress": "10.0.1.2",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW3","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 1",
                        "ipaddress": "10.0.1.3",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW4","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 1",
                        "ipaddress": "10.0.1.4",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW5","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 1",
                        "ipaddress": "10.0.1.5",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW6","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 2",
                        "ipaddress": "10.0.2.6",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW7","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 2",
                        "ipaddress": "10.0.2.7",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW8","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 2",
                        "ipaddress": "10.0.2.8",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
        {"device": {"dev_name": "ASW9","role": "acces switch", 
                    "interfaces": [
                        {"interface": "VLAN 2",
                        "ipaddress": "10.0.2.9",
                        "subnetmask": "255.255.255.0"},
                        ]
                    }
        },
    ]
}