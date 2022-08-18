import discord

'''
Don't use "\" as line continuation char in description. It will result in a space at the place.
Only use it after "\n" since discord removes leading space automatically.
'''
aqua = discord.Color(int("00e0e0", 16))

class help_Embed:
   available_command = ["help", "role", "color", "permission"]
   help_message = discord.Embed(title = "Help", type = "rich", color = aqua, description = 
                              "輸入\"/help <指令名稱>\"以查看指令的說明。")
   help_message.add_field(name = "指令列表", value = "\
                            > **伺服器指令**\n\
                            > /role\n\n\
                            > **其他指令**\n\
                            > /color\n\
                            > /help\n\
                            > /permission\
                            ")
   help = discord.Embed(title = "Command - /help", type = "rich", color = aqua, description = 
                            "顯示指令說明。\n\
                            > **/help [指令]**\n> \n\
                            > [指令]：欲查詢的指令名稱。")
   help.set_footer(text = "<>為必填項，[]為選填項。")
   role = discord.Embed(title = "Command - /role", type = "rich", color = aqua, description = 
                            "管理身分組。")
   role.add_field(name = "模式 - add", inline = False, value = 
                     "新增一個身分組。\n\
                        > **/role add <名稱> [身分組顏色] [分開顯示] [允許提及] [權限] [位階]**\n> \n\
                           > <名稱>：身分組名稱。\n> \n\
                           > [身分組顏色]：身分組的顏色，須為整數、色碼或顏色名稱。預設為discord的預設顏色。使用指令\"/color\"可查詢可用的顏色名稱。\n> \n\
                           > [分開顯示]：是否將身分組成員與線上成員分開顯示，須為\"true\"或\"false\"。預設為 \"false\"。\n> \n\
                           > [允許提及]：是否允許任何人提及這個身分組，須為\"true\"或\"false\"。預設為\"false\"。\n> \n\
                           > [權限]：身分組擁有的權限代碼，須為整數。預設為0。使用指令\"/permission\"可查詢權限對應的數字。\n> \n\
                           > [位階]：身分組所在位階，1為最低，須為整數。預設為1。")
   role.add_field(name = "模式 - modify", inline = False, value = 
                     "編輯一個身分組。\n\
                        > **/role modify <@身分組> <名稱> [身分組顏色] [分開顯示] [允許提及] [權限] [位階]**\n> \n\
                           > <@身分組>：欲修改的身分組。\n> \n\
                           > <名稱>：新的身分組名稱。若不修改則設為\"-1\"。若要將名稱設為\"-1\"，輸入\"\\\\-1\"。\n> \n\
                           > [身分組顏色]：新的身分組的顏色，須為整數、色碼或顏色名稱。若不修改則設為\"-1\"。使用指令\"/color\"可查詢可用的顏色名稱。\n> \n\
                           > [分開顯示]：是否將身分組成員與線上成員分開顯示，須為\"true\"或\"false\"。若不修改則設為\"-1\"。\n> \n\
                           > [允許提及]：是否允許任何人提及這個身分組，須為\"true\"或\"false\"。若不修改則設為\"-1\"。\n> \n\
                           > [權限]：身分組擁有的權限，須為整數。若不修改則設為\"-1\"。使用指令\"/permission\"可查詢權限對應的數字。\n> \n\
                           > [位階]：身分組所在位階，1為最低，須為整數。若不修改則設為\"-1\"。")
   role.add_field(name = "模式 - remove", inline = False, value = 
                     "移除一個身分組。\n\
                        > **/role remove <@身分組>**\n> \n\
                           > <@身分組>：欲移除的身分組。")
   role.add_field(name = "模式 - member", inline = False, value = 
                     "為伺服器成員新增或是移除身分組。\n\
                        > **/role member <@成員> <add|remove> <@身分組>**\n> \n\
                           > <@成員>：變更的伺服器成員。\n> \n\
                           > <@身分組>：欲移除的身分組。")
   role.set_footer(text = "<>為必填項，[]為選填項。")
   color = discord.Embed(title = "Command - color", type = "rich", color = aqua, description = 
                        "顯示可用的身分組顏色名稱。\n\
                        > **/color**")
   color.set_footer(text = "<>為必填項，[]為選填項。")
   permission = discord.Embed(title = "Command - permission", type = "rich", color = aqua, description = 
                        "查詢給定權限對應的權限代碼。\n\
                        > **/permission [權限] [權限] ...**\n> \n\
                           > [權限]：權限的編號或名稱。若未輸入任何的權限，則顯示權限列表。")
   permission.set_footer(text = "<>為必填項，[]為選填項。")
