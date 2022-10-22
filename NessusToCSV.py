# Making sure all libraries are installed
try:
	import xml.etree.ElementTree as xml
except:
	print("Failed o import XML library!")
	quit()
try:
	import sys
except:
	print("Failed o import sys library!")
	quit()

# Preparing root for Nessus file
file = xml.parse(sys.argv[1])
root = file.getroot()

# Preparing output file
output = open(sys.argv[2], "w+")
output.write('HostName;HostIP;RiskFactor;Severity;Port;PluginID;PluginType;PluginName;CVE;CVSScore;CVSS3Score\n')

# Main loop which iters through all scanned hosts and selects values to write to file
for host in root.iter('ReportHost'):
	var_host_name = host.attrib['name']
	for host_ip in host.iter('tag'):
		if host_ip.attrib['name'] == 'host-ip':
			var_host_ip = host_ip.text
			
	for host_item in host.iter('ReportItem'):
		var_host_plugin_risk = host_item.find('risk_factor').text
		var_host_plugin_sev = host_item.attrib['severity']
		var_host_plugin_port =  host_item.attrib['port']
		var_host_plugin_id = host_item.attrib['pluginID']
		var_host_plugin_type =  host_item.find('plugin_type').text
		var_host_plugin_name = host_item.find('plugin_name').text
		try:
			var_host_plugin_cve = host_item.find('cve').text
		except:
			var_host_plugin_cve = "None"
		try:
			var_host_plugin_cvss = host_item.find('cvss_base_score').text
		except:
			var_host_plugin_cvss = "None"
		try:
			var_host_plugin_cvss3 = host_item.find('cvss3_base_score').text
		except:
			var_host_plugin_cvss3 = "None"
		output.write(var_host_name+';'+var_host_ip+';'+var_host_plugin_risk+';'+var_host_plugin_sev+';'+var_host_plugin_port+';'+var_host_plugin_id+';'+var_host_plugin_type+';'+var_host_plugin_name+';'+var_host_plugin_cve+';'+var_host_plugin_cvss+';'+var_host_plugin_cvss3+'\n')

# Closing output file. You know... Just in case...
output.close()

# Done :)
print("Done :)")
