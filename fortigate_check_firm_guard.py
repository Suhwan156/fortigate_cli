import os, time, subprocess

cmd_1 = subprocess.Popen(['cat', 'test_list'], stdout=subprocess.PIPE)
cmd_2 = subprocess.Popen(['grep', '-v', '^#'], stdin=cmd_1.stdout, stdout=subprocess.PIPE)

test_list = cmd_2.communicate()[0].decode('ascii').split('\n')

firmware_ver = " 'get system status | grep Version'"
fortiguard_ver = " 'get system fortiguard | grep expiration'"

for firewall in test_list:
    if firewall != '':
        split = firewall.split()
        result_firm = os.popen('ssh fortiapi@' + split[0] + ' -p ' + split[1] + firmware_ver).read()
        result_guard = os.popen('ssh fortiapi@' + split[0] + ' -p ' + split[1] + fortiguard_ver).read()
        print(result_firm, '\n')
        print(result_guard, '\n')
        time.sleep(1)