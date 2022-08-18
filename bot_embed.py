import discord

'''
Don't use "\" as line continuation char in description. It will result in a space at the place.
Only use it after "\n" since discord removes leading space automatically.
'''

class result_Embed(discord.Embed):
    def __init__(self, type: str = None, command: str = None, code: int = 0, **kwargs: str):
        self.type = "rich"
        self.url = discord.Embed.Empty
        if type == "error":
            self.title = ":no_entry: Error"
            self.color = discord.Color.red()
            if code == 0:  # Unknown
                self.description = "發生未知的錯誤。"
            elif code == -1: # Command forbidden
                self.description = "未授予指令權限。"
            elif code == -2: # Command forbidden (type#2)
                self.description = "權限不足。"
            elif code == -3: # User no permission
                self.description = "你沒有權限使用此指令。"
            elif code == -4: # Not in guild
                self.description = "你必須在伺服器使用此指令。"
            if code == -5:  # Incomplete command
                self.description = "不完整的指令。"
            elif code == -6:  # Excessive Parameters
                excessive_args = kwargs.get("excessive_args", "")
                excessive_args_string = " ".join(excessive_args)
                self.description = f'指令結尾存在多餘的參數。\n指令輸入："{excessive_args_string}"'
            elif code == -7:  # TypeError
                parameter = kwargs.get("parameter", "")
                expected_type = kwargs.get("expected_type", "")
                input = kwargs.get("input", "")
                self.description = f'**{parameter}** 應為{expected_type}。\n指令輸入："{input}"'
            elif code == -8:  # Not available value
                parameter = kwargs.get("parameter", "")
                input = kwargs.get("input", "")
                min_value = kwargs.get("min", None)
                if min_value is not None:
                    self.description = f'**{parameter}** 最小為{min_value}。\n指令輸入："{input}"'
                else:
                    max_value = kwargs.get("max", None)
                    self.description = f'**{parameter}** 最大為{max_value}。\n指令輸入："{input}"'
            elif code == -9:
                name = kwargs.get("name", "名稱")
                input = kwargs.get("input", "")
                self.description = f'未知的{name}。\n指令輸入："{input}"'
            else:
                if command == "role":
                    if code == 1:
                        position = kwargs.get("position", "")
                        self.description = f"不存在位階{position}。"
                    elif code == 2:
                        self.description = "所有屬性均未改動。"
                    elif code == 3:
                        self.description = "無效的名稱。\n指令輸入：\"\\\\\""
                    elif code == 4:
                        self.description = "成員已在該身分組內。"
                    elif code == 5:
                        self.description = "成員不在該身分組內。"

        if type == "success":
            self.title = ":white_check_mark: Success"
            self.color = discord.Color.green()
            if command == "role":
                if code == 1:
                    role_name = f'<@&{kwargs.get("role_id", "")}>'
                    self.description = f"已建立身分組{role_name}。"
                elif code == 2:
                    role_name = f'<@&{kwargs.get("role_id", "")}>'
                    self.description = f"已建立身分組{role_name}。"
                    self.add_field(name=":warning: Warning", value="位階設定失敗。")
                elif code == 3:
                    role_name = f'<@&{kwargs.get("role_id", "")}>'
                    self.description = f"已編輯身分組{role_name}。"
                    original, modified = kwargs.get("original"), kwargs.get("modified")
                    role_attr_mapping = {"name": ("名稱", lambda x: x), 
                            "color": ("顏色", lambda x: f'#{hex(x.value).lstrip("0x"):>06}'), 
                            "hoist": ("分開顯示", lambda x: str(x).lower()), 
                            "mentionable": ("允許提及", lambda x: str(x).lower()), 
                            "permissions": ("權限", lambda x: x.value),
                            "position": ("位階", lambda x: x)}
                    for i in role_attr_mapping:
                        if original.get(i) is not None:
                            self.description += f'\n{role_attr_mapping.get(i)[0]}："{role_attr_mapping.get(i)[1](original.get(i))}" -> "{role_attr_mapping.get(i)[1](modified.get(i))}"'
                elif code == 4:
                    role_name = kwargs.get("role_name", "")
                    self.description = f'已刪除身分組"{role_name}"。'
                elif code == 5:
                    user_name = f'<@{kwargs.get("user")._user.id}>'
                    role_name = f'<@&{kwargs.get("role").id}>'
                    self.description = f"已為成員{user_name}新增身分組{role_name}。"
                elif code == 6:
                    user_name = f'<@{kwargs.get("user")._user.id}>'
                    role_name = f'<@&{kwargs.get("role").id}>'
                    self.description = f"已將成員{user_name}移出身分組{role_name}。"




