import discord
from discord.ext import commands
#from discord.utils import get
from bot_help import help_Embed
from bot_embed import result_Embed
import cmd_role
import cmd_color
import cmd_permission

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents = intents, command_prefix = "/", help_command=None)


def in_guild(ctx: commands.Context):
    if ctx.guild is not None:
        return True
    return False


def has_permission(ctx: commands.Context, required):
    author_perms = ctx.author.permissions_in(ctx.channel)
    if discord.Permissions(required) <= author_perms or discord.Permissions(1 << 3) <= author_perms:
        return True
    return False


@bot.command()
async def role(ctx: commands.Context, mode: str = None, *args: str):
    if not in_guild(ctx):
        return await ctx.send(embed = result_Embed(type = "error", code = -4))
    if not has_permission(ctx, 1 << 28):
        return await ctx.send(embed = result_Embed(type = "error", code = -3))
    if mode == None:
        return await ctx.send(embed = result_Embed(type = "error", code = -5))

    '''
    mode "add"
    add a new role
    command: /role add <name> [color] [hoist] [mentionable] [permissions] [position]
    command: /role add <名稱> [身分組顏色] [分開顯示] [允許提及] [權限] [位階]
    '''
    if mode == "add":
        length = len(args)
        if length == 0:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        name = args[0]
        attrs = [i < length - 1 for i in range(5)]
        color = cmd_role.to_color(attrs[0] and args[1])
        if color is None:
            return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[身分組顏色]",
                                                     expected_type = "整數、色碼或顏色名稱", input = args[1]))
        hoist = cmd_role.to_bool(attrs[1] and args[2])
        if hoist is None:
            return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[分開顯示]",
                                                     expected_type = "true 或 false", input = args[2]))
        mentionable = cmd_role.to_bool(attrs[2] and args[3])
        if mentionable is None:
            return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[允許提及]",
                                                     expected_type = "true 或 false", input = args[3]))
        permissions = cmd_role.to_permission(attrs[3] and args[4])
        if permissions is None:
            return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[權限]",
                                                     expected_type = "整數", input = args[4]))
        if permissions == -1:
            return await ctx.send(embed = result_Embed(type = "error", code = -8, parameter = "[權限]",
                                                     min = "0", input = args[4]))
        if permissions == -2:
            return await ctx.send(embed = result_Embed(type = "error", code = -8, parameter = "[權限]",
                                                     max = str((1 << 33) - 1), input = args[4]))
        position = cmd_role.to_position(attrs[4] and args[5])
        if position is None:
            return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[位階]",
                                                     expected_type = "整數", input = args[5]))
        if position == -1:
            return await ctx.send(embed = result_Embed(type = "error", code = -8, parameter = "[位階]",
                                                     min = "1", input = args[5]))
        if position > len(await ctx.guild.fetch_roles()):
            return await ctx.send(embed = result_Embed(command="role", type="error", code=1,
                                                     position=position))
        if length >= 7:
            return await ctx.send(embed = result_Embed(type = "error", code = -6,
                                                     excessive_args = [args[i] for i in range(6, length)]))
        if position == 1:
            try:
                new_role = await ctx.guild.create_role(name = name, color = color, permissions = permissions,
                                                       hoist = hoist, mentionable = mentionable)
            except discord.errors.Forbidden:
                return await ctx.send(embed = result_Embed(type = "error", code = -1))
            except:
                return await ctx.send(embed = result_Embed(type = "error", code = 0))
            else:
                return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 1,
                                                         role_id = new_role.id))
        else:
            try:
                new_role = await ctx.guild.create_role(name = name, color = color, permissions = permissions,
                                                       hoist = hoist, mentionable = mentionable)
                await new_role._move(position = position, reason = None)
            except discord.Forbidden:
                return await ctx.send(embed = result_Embed(type = "error", code = -1))
            except discord.HTTPException:
                return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 2,
                                                         role_id = new_role.id))
            except:
                return await ctx.send(embed = result_Embed(type = "error", code = 0))
            else:
                return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 1,
                                                         role_id = new_role.id))

    '''
    mode "modify"
    edit a role
    command: /role add <@role> [name] [color] [hoist] [mentionable] [permissions] [position]
    command: /role set <@身分組> [名稱] [身分組顏色] [分開顯示] [允許提及] [權限] [位階]
    '''
    if mode == "modify":
        length = len(args)
        if length == 0:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        try:
            role_converter = commands.RoleConverter()
            selected_role = await role_converter.convert(ctx, args[0])
        except commands.RoleNotFound:
            return await ctx.send(embed = result_Embed(type = "error", code = -9, name = "身分組",
                                                     input = args[0]))
        if length == 1:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        attrs = [i < length - 1 for i in range(6)]
        original_dict = {}
        modify_dict = {}
        if attrs[0] and args[1] != "-1":
            if args[1].startswith("\\"):
                if args[1] == "\\":
                    return await ctx.send(embed = result_Embed(type = "error",command = "role", code = 3))
                modify_dict.update({"name": args[1].split("\\", maxsplit = 1)[1]})
            else:
                modify_dict.update({"name": args[1]})
            if modify_dict.get("name") == selected_role.name:
                modify_dict.pop("name")
            else:
                original_dict.update({"name": selected_role.name})
                
        if attrs[1] and args[2] != "-1":
            modify_dict.update({"color": cmd_role.to_color(args[2])})
            if modify_dict.get("color") is None:
                return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[身分組顏色]",
                                                         expected_type = "整數、色碼或顏色名稱", input = args[2]))
            if modify_dict.get("color") == selected_role.color:
                modify_dict.pop("color")
            else:
                original_dict.update({"color": selected_role.color})
            
        if attrs[2] and args[3] != "-1":
            modify_dict.update({"hoist": cmd_role.to_bool(args[3])})
            if modify_dict.get("hoist") is None:
                return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[分開顯示]",
                                                         expected_type = "true 或 false", input = args[3]))
            if modify_dict.get("hoist") == selected_role.hoist:
                modify_dict.pop("hoist")
            else:
                original_dict.update({"hoist": selected_role.hoist})
        if attrs[3] and args[4] != "-1":
            modify_dict.update({"mentionable": cmd_role.to_bool(args[4])})
            if modify_dict.get("mentionable") is None:
                return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[允許提及]",
                                                         expected_type = "true 或 false", input = args[4]))
            if modify_dict.get("mentionable") == selected_role.mentionable:
                modify_dict.pop("mentionable")
            else:
                original_dict.update({"mentionable": selected_role.mentionable})
        if attrs[4] and args[5] != "-1":
            modify_dict.update({"permissions": cmd_role.to_permission(args[5])})
            if modify_dict.get("permissions") is None:
                return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[權限]",
                                                         expected_type = "整數", input = args[5]))
            if modify_dict.get("permissions") == -1:
                return await ctx.send(embed = result_Embed(type = "error", code = -8, parameter = "[權限]",
                                                         min = "0", input = args[5]))
            if modify_dict.get("permissions") == -2:
                return await ctx.send(embed = result_Embed(type = "error", code = -8, parameter = "[權限]",
                                                         max = str((1 << 33) - 1), input = args[5]))
            if modify_dict.get("permissions") == selected_role.permissions:
                modify_dict.pop("permissions")
            else:
                original_dict.update({"permissions": selected_role.permissions})
        if attrs[5] and args[6] != "-1":
            modify_dict.update({"position": cmd_role.to_position(args[6])})
            if modify_dict.get("position") is None:
                return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "[位階]",
                                                        expected_type = "整數", input = args[6]))
            if modify_dict.get("position") == -1:
                return await ctx.send(embed = result_Embed(type = "error", code = -8, parameter = "[位階]",
                                                        min = "1", input = args[6]))
            if modify_dict.get("position") >= len(await ctx.guild.fetch_roles()):
                return await ctx.send(embed = result_Embed(command="role", type="error", code = 1,
                                                        position = modify_dict.get("position")))
            if modify_dict.get("position") == selected_role.position:
                modify_dict.pop("position")
            else:
                original_dict.update({"position": selected_role.position})
        if length >= 8:
            return await ctx.send(embed = result_Embed(type = "error", code = -6,
                                                     excessive_args = [args[i] for i in range(7, length)]))
        if not modify_dict:
            return await ctx.send(embed = result_Embed(type = "error", command = "role", code = 2))
        try:
            await selected_role.edit(**modify_dict)
        except discord.HTTPException:
            return await ctx.send(embed = result_Embed(type = "error", code = -1))
        except:
            return await ctx.send(embed = result_Embed(type = "error", code = 0))
        else:
            return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 3, 
                                                    role_id = selected_role.id, original = original_dict, 
                                                    modified = modify_dict))

    '''
    mode "remove"
    remove a role
    command: /role remove <@role>
    command: /role remove <@身分組>
    '''
    if mode == "remove":
        length = len(args)
        if length == 0:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        try:
            role_converter = commands.RoleConverter()
            selected_role = await role_converter.convert(ctx, args[0])
        except commands.RoleNotFound:
            return await ctx.send(embed = result_Embed(type = "error", code = -9, name = "身分組",
                                                     input = args[0]))
        if length >= 2:
            return await ctx.send(embed = result_Embed(type = "error", code = -6,
                                                     excessive_args = [args[i] for i in range(1, length)]))
        selected_role_name = selected_role.name
        try:
            await selected_role.delete()
        except discord.HTTPException:
            return await ctx.send(embed = result_Embed(type = "error", code = -1))
        except:
            return await ctx.send(embed = result_Embed(type = "error", code = 0))
        else:
            return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 4, 
                                                    role_name = selected_role_name))

    '''
    mode "member"
    add a member to or remove a member from a role
    command: /role member <@user> <add|remove> <@role>
    command: /role member <@成員> <add|remove> <@身分組>
    '''
    if mode == "member":
        length = len(args)
        if length == 0:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        try:
            member_converter = commands.MemberConverter()
            selected_member = await member_converter.convert(ctx, args[0])
        except commands.MemberNotFound:
            return await ctx.send(embed = result_Embed(type = "error", code = -9, name = "成員",
                                                     input = args[0]))
        if length == 1:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        if not args[1] == "add" and not args[1] == "remove":
            return await ctx.send(embed = result_Embed(type = "error", code = -7, parameter = "<模式>",
                                                        expected_type = "\"add\"或\"remove\"", 
                                                        input = args[1]))
        if length == 2:
            return await ctx.send(embed = result_Embed(type = "error", code = -5))
        try:
            role_converter = commands.RoleConverter()
            selected_role = await role_converter.convert(ctx, args[2])
        except commands.RoleNotFound:
            return await ctx.send(embed = result_Embed(type = "error", code = -9, name = "身分組",
                                                     input = args[2]))
        if length >= 4:
            return await ctx.send(embed = result_Embed(type = "error", code = -6,
                                                     excessive_args = [args[i] for i in range(3, length)]))
        try:
            if args[1] == "add":
                if selected_role in selected_member.roles:
                    return await ctx.send(embed = result_Embed(type = "error", command = "role", code = 4))
                await selected_member.add_roles(selected_role)
                return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 5, user = selected_member, 
                                                        role = selected_role))
            if args[1] == "remove":
                if selected_role in selected_member.roles:
                    await selected_member.remove_roles(selected_role)
                    return await ctx.send(embed = result_Embed(type = "success", command = "role", code = 6, user = selected_member, 
                                                        role = selected_role))
                return await ctx.send(embed = result_Embed(type = "error", command = "role", code = 5))
        except discord.HTTPException:
            return await ctx.send(embed = result_Embed(type = "error", code = -1))
        except:
            return await ctx.send(embed = result_Embed(type = "error", code = 0))

@bot.command()
async def color(ctx: commands.Context, *args):
    if args:
        return await ctx.send(embed = result_Embed(type = "error", code = -6,
                                                    excessive_args = args))
    return await ctx.send(embed = cmd_color.Color_list.list)

@bot.command()
async def permission(ctx: commands.Context, *args):
    if not args:
        return await ctx.send(embed = cmd_permission.permission_Embed.list)
    permission = cmd_permission.permission_transfer.trans(*args)
    if isinstance(permission, str):
        return await ctx.send(embed = result_Embed(type = "error", code = -9, name = "權限名稱", input = permission))
    return await ctx.send(embed = cmd_permission.permission_Embed(*permission).query)


@bot.command()
async def help(ctx: commands.Context, command: str = None, *args):
    if command is None:
        return await ctx.send(embed = help_Embed.help_message)
    if command in help_Embed.available_command:
        if len(args) > 0:
            return await ctx.send(embed = result_Embed(type = "error", code = -6,
                                                     excessive_args = args))
        return await ctx.send(embed = eval(f"help_Embed.{command}"))
    return await ctx.send(embed = result_Embed(type = "error", code = -9, name = "指令名稱", input = command))


bot.run("")
