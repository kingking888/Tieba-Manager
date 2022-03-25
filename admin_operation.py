# -*- coding:utf-8 -*-
import argparse
import asyncio

import tiebaBrowser as tb

if __name__ == '__main__':

    async def main():

        parser = argparse.ArgumentParser(
            description='ADMIN OPERATION', allow_abbrev=False)

        parser.add_argument('tieba_name',
                            type=str,
                            help='需要执行操作的目标贴吧吧名')
        parser.add_argument('--BDUSS_key', '-key',
                            type=str,
                            default='default',
                            help='用于获取BDUSS')

        parser.add_argument('--id', '-i',
                            type=str,
                            help='用户id（user_name或portrait）')
        parser.add_argument('--user_id', '-uid',
                            type=int,
                            help='用户user_id')
        parser.add_argument('--tid', '-t',
                            type=int,
                            default=0,
                            help='帖子tid')
        parser.add_argument('--pid', '-p',
                            type=int,
                            default=0,
                            help='帖子pid')

        parser.add_argument('--block', '-b',
                            action='store_true',
                            help='将用户封10天')
        parser.add_argument('--unblock', '-u',
                            action='store_true',
                            help='将用户解封')
        parser.add_argument('--blacklist_add', '-ba',
                            action='store_true',
                            help='将用户加入黑名单')
        parser.add_argument('--blacklist_cancel', '-bc',
                            action='store_true',
                            help='将用户解除黑名单')

        parser.add_argument('--delete', '-d',
                            action='store_true',
                            help='删除帖子')
        parser.add_argument('--recover', '-r',
                            action='store_true',
                            help='恢复帖子')
        parser.add_argument('--hide',
                            action='store_true',
                            help='屏蔽帖子')
        parser.add_argument('--unhide',
                            action='store_true',
                            help='解除屏蔽帖子')
        parser.add_argument('--good', '-g',
                            type=str,
                            default=None,
                            help='加精分区名')
        parser.add_argument('--ungood',
                            action='store_true',
                            help='解除屏蔽帖子')

        parser.add_argument('--refuse_appeals', '-ra',
                            action='store_true',
                            help='一键拒绝所有解封申诉')

        args = parser.parse_args()
        tieba_name = args.tieba_name

        async with tb.Browser(args.BDUSS_key) as brow:
            user = None
            if args.id:
                user = await brow.get_user_info(args.id)
            if args.user_id:
                user = await brow.get_basic_user_info(args.user_id)
            if user and user.portrait:
                print(user)
                if args.block:
                    await brow.block(tieba_name, user, day=10)
                if args.unblock:
                    await brow.unblock(tieba_name, user)
                if args.blacklist_add:
                    await brow.blacklist_add(tieba_name, user)
                if args.blacklist_cancel:
                    await brow.blacklist_cancel(tieba_name, user)

            tid = args.tid
            if tid:
                if args.delete:
                    await brow.del_thread(tieba_name, tid)
                if args.recover:
                    await brow.recover_thread(tieba_name, tid)
                if args.hide:
                    await brow.hide_thread(tieba_name, tid)
                if args.unhide:
                    await brow.unhide_thread(tieba_name, tid)
                if args.good is not None:
                    await brow.good(tieba_name, tid, args.good)
                if args.ungood:
                    await brow.ungood(tieba_name, tid)

            pid = args.pid
            if pid:
                if args.recover:
                    await brow.recover_post(tieba_name, pid)

            if args.refuse_appeals:
                await brow.refuse_appeals(tieba_name)

    asyncio.run(main())
