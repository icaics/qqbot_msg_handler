#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Define import Test


def onQQMessage(bot, contact, member, content):

    """ QQBot 全局调用入口 """

    # print(bot)
    # print(contact)
    # print(member)
    # print(content)

    # 获取群名称
    group_name = str(contact)
    group_name = group_name[2:-1]
    # print(group_name)

    # 只接收指定群消息
    if contact.ctype == 'group' and group_name == Test.group_name:

        # 获得消息内容
        message = str(content)

        # 只处理触发器开头的消息
        if message.startswith(Test.group_trigger):

            # 去掉触发器
            message = message.replace(Test.group_trigger, '')

            # 去掉 空格 及 @ 符号
            message = message.replace(' ', '')
            message = message.replace('[@ME]', '')

            # 获得处理完成后，等待发送的消息
            result = handle_msg(bot, contact, member, message)

            # 消息非空则回复
            if len(result) > 0:
                bot.SendTo(contact, result)


def handle_msg(bot, contact, member, message):

    """ 处理消息程序 """

    member_name = member.name

    # 处理空消息
    if len(message) == 0:
        return '@' + member_name + ' 需要我为您做什么？\n直接发言「' + Test.group_trigger + ' 你能做什么」查看相关帮助'

    if message == '你能做什么':
        bot.SendTo(contact, Test.help)
        return

    return '收到消息：' + message
