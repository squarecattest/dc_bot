import discord

class permission_transfer():
    code = {"view_channel": (10, 0), 
            "1": (10, 0), 
            "manage_channel": (4, 1), 
            "2": (4, 1), 
            "manage_role": (28, 2), 
            "3": (28, 2), 
            "manage_emoji": (30, 3), 
            "4": (30, 3), 
            "view_audit_log": (7, 4), 
            "5": (7, 4), 
            "manage_webhook": (29, 5), 
            "6": (29, 5), 
            "manage_server": (5, 6), 
            "7": (5, 6), 
            "create_invite": (0, 7), 
            "8": (0, 7), 
            "change_nickname": (26, 8), 
            "9": (26, 8), 
            "manage_nickname": (27, 9), 
            "10": (27, 9), 
            "kick": (1, 10), 
            "11": (1, 10), 
            "ban": (2, 11), 
            "12": (2, 11), 
            "send_message": (11, 12), 
            "13": (11, 12), 
            "embed_link": (14, 13), 
            "14": (14, 13), 
            "attach_file": (15, 14), 
            "15": (15, 14), 
            "add_reaction": (6, 15), 
            "16": (6, 15), 
            "use_external_emoji": (18, 16), 
            "17": (18, 16), 
            "mention_everyone": (17, 17), 
            "18": (17, 17), 
            "manage_message": (13, 18), 
            "19": (13, 18), 
            "read_message_history": (16, 19), 
            "20": (16, 19), 
            "send_tts_message": (12, 20), 
            "21": (12, 20), 
            "use_command": (31, 21), 
            "22": (31, 21), 
            "connect": (20, 22), 
            "23": (20, 22), 
            "speak": (21, 23), 
            "24": (21, 23), 
            "stream": (9, 24), 
            "25": (9, 24), 
            "use_voice_activation": (25, 25), 
            "26": (25, 25), 
            "priority_speaker": (8, 26), 
            "27": (8, 26), 
            "mute": (22, 27), 
            "28": (22, 27), 
            "deafen_member": (23, 28), 
            "29": (23, 28), 
            "move_member": (24, 29), 
            "30": (24, 29), 
            "view_server_insights": (19, 30),
            "31": (19, 30), 
            "request_to_speak": (32, 31), 
            "32": (32, 31), 
            "administrator": (3, 32), 
            "33": (3, 32)
            }
    name = ["檢視頻道", "管理頻道", "管理身分組", "管理表情符號與貼圖", "檢視審核紀錄", "管理Webhooks", 
            "管理伺服器", "建立邀請", "更改暱稱", "管理暱稱", "踢出成員", "對成員停權", "發送訊息", 
            "嵌入連結", "附加檔案", "新增反應", "使用外部表情符號", "提及@everyone、@here和所有身分組", 
            "管理訊息", "讀取訊息歷史", "傳送文字朗讀訊息", "使用應用程式命令", "連接", "說話", "視訊通話", 
            "使用語音活動", "優先發言者", "將成員靜音", "讓成員拒聽", "移動成員", "檢視Server Insights", 
            "請求發言", "管理者"]
    def trans(*args: str):
        available_list = permission_transfer.code
        trans_list = ["0"] * 33
        input_list = [False] * 33
        for i in args:
            j = i.lstrip("0")
            permission, code = available_list.get(j, (None, None))
            if permission is None:
                return i
            trans_list[permission], input_list[code] = "1", True
        trans_list.reverse()
        return int("".join(trans_list), 2), "\n".join([permission_transfer.name[i] \
                                                    for i in range(33) if input_list[i]])

class permission_Embed:
    def __init__(self, permission: int, list: str):
        self.query = discord.Embed(title = "Permission", type = "rich", color = discord.Color(int("00e0e0", 16)),
                                description = f'權限代碼為"{str(permission)}"。包含以下權限：\n\n{list}')
    list = discord.Embed(title = "Permission", type = "rich", color = discord.Color(int("00e0e0", 16)), 
                        description = "")
    list.add_field(name = "編號 - 名稱\n敘述...\n\n> 一般伺服器權限\n\u200B", inline = False, value = 
                    "**1 - view_channel**\n\
                    檢視頻道\n\
                    允許成員檢視頻道（私人頻道除外）。\n\n\
                    **2 - manage_channel**\n\
                    管理頻道\n\
                    允許成員建立、編輯或刪除頻道。\n\n\
                    **3 - manage_role**\n\
                    管理身分組\n\
                    允許成員建立、編輯或刪除比他們最高身分組還低的身分組。成員可存取的個人頻道，其權限也允許變更。\n\n\
                    **4 - manage_emoji**\n\
                    管理表情符號與貼圖\n\
                    允許成員新增或移除此伺服器的自訂表情符號貼圖。\n\n\
                    **5 - view_audit_log**\n\
                    檢視審核紀錄\n\
                    允許成員檢視誰在此伺服器做了何種變更。\n\n\
                    **6 - manage_webhook**\n\
                    管理Webhooks\n\
                    允許成員建立、編輯或刪除Webhook。Webhook能將來自其他應用程式或網站的訊息張貼至此伺服器。\n\n\
                    **7 - manage_server**\n\
                    管理伺服器\n\
                    允許成員變更此伺服器的名稱、切換地區、檢視所有邀請、新增機器人至此伺服器及建立和更新AutoMod規則。\n\u200B")
    list.add_field(name = "> 會員權限\n\u200B", inline = False, value = 
                    "**8 - create_invite**\n\
                    建立邀請\n\
                    允許成員邀請新人至此伺服器。\n\n\
                    **9 - change_nickname**\n\
                    更改暱稱\n\
                    允許成員變更自己的暱稱，這是專屬於此伺服器的自訂名稱。\n\n\
                    **10 - manage_nickname**\n\
                    管理暱稱\n\
                    允許成員變更其他成員的暱稱。\n\n\
                    **11 - kick**\n\
                    踢出成員\n\
                    允許成員移除此伺服器的其他成員。踢出的成員再收到邀請便能重新加入。\n\n\
                    **12 - ban**\n\
                    對成員停權\n\
                    允許成員對此伺服器的其他成員永久停權。\n\u200B")
    list.add_field(name = "> 文字頻道權限\n\u200B", inline = False, value = 
                    "**13 - send_message**\n\
                    發送訊息\n\
                    允許成員在文字頻道傳送訊息。\n\n\
                    **14 - embed_link**\n\
                    嵌入連結\n\
                    允許成員分享的連結在文字頻道顯示內嵌內容。\n\n\
                    **15 - attach_file**\n\
                    附加檔案\n\
                    允許成員在文字頻道上傳檔案或媒體。\n\n\
                    **16 - add_reaction**\n\
                    新增反應\n\
                    允許成員將表情符號反應新增至訊息上。停用此權限的話，成員還是可以使用訊息現有的反應。\n\n\
                    **17 - use_external_emoji**\n\
                    使用外部表情符號\n\
                    允許成員使用其他伺服器的表情符號。而他們必須是Discord Nitro會員。")
    list.add_field(name = "\u200B", inline = False, value = 
                    "**18 - mention_everyone**\n\
                    提及@everyone、@here和所有身分組\n\
                    允許成員使用@everyone、@here，也允許提及所有身分組，即使此身分組並未授權「允許任何人提及這個身分組」。\n\n\
                    **19 - manage_message**\n\
                    管理訊息\n\
                    允許成員刪除其他成員留下的訊息，也允許成員釘選任何訊息。\n\n\
                    **20 - read_message_history**\n\
                    讀取訊息歷史\n\
                    允許成員讀取頻道之前傳送的訊息。若停用此權限，成員只會看見當他們在線上且該頻道為主要畫面時傳送的訊息。\n\n\
                    **21 - send_tts_message**\n\
                    傳送文字朗讀訊息\n\
                    允許成員以/tts當作訊息開頭，傳送文字朗讀訊息，主要畫面為該頻道的任何人都能聽見這些訊息。\n\n\
                    **22 - use_command**\n\
                    使用應用程式命令\n\
                    允許成員使用應用程式命令，包含斜線命令和操作功能選單命令。\n\u200B")
    list.add_field(name = "> 語音頻道權限\n\u200B", inline = False, value = 
                    "**23 - connect**\n\
                    連接\n\
                    允許成員加入語音頻道並聽見其他人說話。\n\n\
                    **24 - speak**\n\
                    說話\n\
                    允許成員在語音頻道聊天。若停用此權限，成員將會預設為靜音，除非有人有「將成員靜音」的權限，並對他們解除靜音。\n\n\
                    **25 - stream**\n\
                    視訊通話\n\
                    允許成員在此伺服器分享影片、分享畫面或直播遊戲。\n\n\
                    **26 - use_voice_activation**\n\
                    使用語音活動\n\
                    允許成員在語音頻道直接說話聊天。若停用此權限，成員必須使用按鍵講話，對於管控有背景音或吵雜的成員很方便。\n\n\
                    **27 - priority_speaker**\n\
                    優先發言者\n\
                    允許成員在語音頻道中說話時更容易被聽見。啟用之後，不具此權限成員的發言音量會被自動降低。\n\n\
                    **28 - mute**\n\
                    將成員靜音\n\
                    允許成員替所有人將語音頻道的其他成員靜音。\n\n\
                    **29 - deafen_member**\n\
                    讓成員拒聽\n\
                    允許成員關閉語音頻道中其他成員的聽說功能，他們將無法說話，也無法聽見其他人說話。\n\n\
                    **30 - move_member**\n\
                    移動成員\n\
                    允許成員在語音頻道間移動其他成員，而擁有此權限的成員必須要能存取該語音頻道。\n\u200B")
    list.add_field(name = "> 社群伺服器權限\n\u200B", inline = False, value = 
                    "**31 - view_server_insights**\n\
                    檢視Server Insights\n\
                    允許成員檢視Server Insights，其中包含多種數據，如社群成長幅度，參與度等。\n\n\
                    **32 - request_to_speak**\n\
                    請求發言\n\
                    允許在舞台頻道中提出發言請求。舞台版主可以手動核准或拒絕所有請求。\n\u200B")
    list.add_field(name = "> 進階權限\n\u200B", inline = False, value = 
                    "**33 - administrator**\n\
                    管理者\n\
                    擁有這個權限的成員具有所有權限，可略過所有頻道特定權限或限制（例如成員可以存取所有私人頻道）。")