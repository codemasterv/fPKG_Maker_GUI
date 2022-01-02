## Easy Fake DLC / DLC without Extra Data Generator
## Version 2.1.0 (24.07.20)
## NOW UPDATED TO USE OPEN SOURCED PKGTOOL.EXE (from LibOrbisPkg) AND WITH PSS URL SUPPORT
## Written in python 3.5 by TheRadziu

import os, os.path
import sys
import json
import urllib.request
import errno
import shutil
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
gen_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
contentid = "EP0002-CUSA00000_00-0000000000000000"
name = "NO DLC NAME"
titleid = "CUSA00000"

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')

def parse_store_url(url):
    url = url.replace("https://", "")
    urls = url.split("/")
    contentid = urls[3]
    chihiro_url = 'https://store.playstation.com/store/api/chihiro/00_09_000/container/'+urls[1][-2:]+'/'+urls[1][:2]+'/999/'+urls[3]+'/'
    chihiro_response = urllib.request.urlopen(chihiro_url)
    chihiro_json = json.loads(chihiro_response.read().decode('utf-8'))
    if chihiro_json['skus'][0]['entitlements'][0]['packageType'] != 'PS4AL':
        print('!!!!!!!! WARNING !!!!!!!!\nPackage seems to be DLC WITH EXTRA DATA or a BUNDLE. Created fpkg is most likely to be unusable.\n!!!!!!!! WARNING !!!!!!!!')
#        if yes_no_prompt("Do you wish to continue anyway?") == False:
#           print('Aborting!')
#            sys.exit(2)
    print('----------------------------------------')
    contentid = chihiro_json['id']
    name = chihiro_json['name']
    urllib.request.urlretrieve(chihiro_json['images'][len(chihiro_json['images'])-1]['url'], "fake_dlc_temp/sce_sys/icon0.png")
    return name, contentid

if not os.path.exists('PkgTool.exe') or not os.path.exists('LibOrbisPkg.dll'):
	print("File or files \'PkgTool.exe.exe\', \'LibOrbisPkg.dll'\ are missing from current directory!!")
	sys.exit(2)
    
def yes_no_prompt(question, default="yes"):
	valid = {"yes": True, "y": True, "ye": True,
			"no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		print(question + prompt)
		choice = input('Choice: ').lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			print('Please respond with \'yes\' or \'no\'\n(or \'y\' or \'n\').')

## Precreate some directories if needed
mkdir_p(os.path.dirname('fake_dlc_temp/sce_sys/'))
if os.path.isdir("fake_dlc_pkg"):
	pass
else:
	os.mkdir('fake_dlc_pkg')
    
## decide if from url or not:
if len(sys.argv) > 1 and "https://store.playstation.com" in sys.argv[1]:
    print("!! STORE URL PARSING MODE !!\n")
    res = parse_store_url(sys.argv[1])
    name = res[0]
    contentid = res[1]
else:
    try:
        contentid = sys.argv[1]
        name = sys.argv[2]
        urllib.request.urlretrieve("https://i.imgur.com/JeaTFEX.png", "fake_dlc_temp/sce_sys/icon0.png")
        print("!! LOCAL METADATA MODE !!\n")
        if len(contentid) != 36:
            print("DLC CID IS TOO LONG OR TOO SHORT, IT HAS TO BE 36 CHARACTERS LONG, FOR EXAMPLE 'UP9000-CUSA00900_00-SPEXPANSIONDLC03'")
            shutil.rmtree('fake_dlc_temp')
            sys.exit(2)
    except:
        print("Usage for local metadata mode: {} {} {}\n".format(sys.argv[0], 'DLC_CID', '\"DLC_NAME\"'))
        print("Usage for store url parsing mode: {} {}".format(sys.argv[0], 'https://store.playstation.com/pl-pl/product/EP0002-CUSA07399_00-CRASHNSANELEVEL2'))
        shutil.rmtree('fake_dlc_temp')
        sys.exit(2)
        
GP4_template = """<?xml version="1.0"?>
<psproject xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" fmt="gp4" version="1000">
  <volume>
    <volume_type>pkg_ps4_ac_data</volume_type>
    <volume_ts>%s</volume_ts>
    <package content_id="%s" passcode="00000000000000000000000000000000" entitlement_key="00000000000000000000000000000000" />
  </volume>
  <files img_no="0">
    <file targ_path="sce_sys/icon0.png" orig_path="sce_sys\icon0.png" />
    <file targ_path="sce_sys/param.sfo" orig_path="sce_sys\param.sfo" />
  </files>
  <rootdir>
    <dir targ_name="sce_sys" />
  </rootdir>
</psproject>""" % (gen_time, contentid)

## save template as a project file
x = safe_open_w('fake_dlc_temp/fake_dlc_project.gp4')
x.write(GP4_template)
x.close()

## make and populate param.sfo
print('SFO:')
os.system('PkgTool.exe sfo_new fake_dlc_temp\sce_sys\param.sfo')
os.system('PkgTool.exe sfo_setentry --value 0x00000000 --type integer --maxsize 4 fake_dlc_temp\sce_sys\param.sfo ATTRIBUTE')
os.system('PkgTool.exe sfo_setentry --value ac --type utf8 --maxsize 4 fake_dlc_temp\sce_sys\param.sfo CATEGORY')
os.system('PkgTool.exe sfo_setentry --value ' + contentid + ' --type utf8 --maxsize 48 fake_dlc_temp\sce_sys\param.sfo CONTENT_ID')
os.system('PkgTool.exe sfo_setentry --value obs --type utf8 --maxsize 4 fake_dlc_temp\sce_sys\param.sfo FORMAT')
os.system('PkgTool.exe sfo_setentry --value \"' + name + '\" --type utf8 --maxsize 128 fake_dlc_temp\sce_sys\param.sfo TITLE')
os.system('PkgTool.exe sfo_setentry --value ' + contentid[7:16] + ' --type utf8 --maxsize 12 fake_dlc_temp\sce_sys\param.sfo TITLE_ID')
os.system('PkgTool.exe sfo_setentry --value 01.00 --type utf8 --maxsize 8 fake_dlc_temp\sce_sys\param.sfo VERSION')
print('----------------------------------------')

## build fpkg out of generated PG4 project file
if os.path.isdir("fake_dlc_pkg/" + contentid[7:16]):
	pass
else:
    os.mkdir('fake_dlc_pkg/' + contentid[7:16])
os.system('PkgTool.exe pkg_build fake_dlc_temp\\fake_dlc_project.gp4 fake_dlc_pkg/' + contentid[7:16])

## be a good boy and clean up after
shutil.rmtree('fake_dlc_temp')
print('----------------------------------------')
print('Everything is finished, quitting :)')