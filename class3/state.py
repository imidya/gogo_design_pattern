"""
Call in behavior in Whoscall


                                                        --- Full AD -----
                                                       /                 \
                           --- Answer --- Call End ---                    ---- Idle
                          /                            \                 /
                         ｜                              --- Banner AD --
Idle --- CallInComing ----
                          \
                           --- Not Answer --- Miss Call --- Thank --- Idle




"""

import random


class State:
    def __init__(self, context):
        self.context = context

    def handle(self):
        raise NotImplementedError


class IdleState(State):
    def handle(self):
        print('待機狀態，不做任何動作')


class ThankState(State):
    def handle(self):
        print('顯示感謝畫面')
        self.context.state = IdleState(self.context)
        self.context.state.handle()


class MissCallState(State):
    def handle(self):
        print('未接狀態')
        self.context.state = ThankState(self.context)
        self.context.state.handle()


class FullADState(State):
    def handle(self):
        print('顯示全版廣告')
        self.context.state = IdleState(self.context)
        self.context.state.handle()


class BannerADState(State):
    def handle(self):
        print('顯示半版廣告')
        self.context.state = IdleState(self.context)
        self.context.state.handle()


class CallEndState(State):
    def handle(self):
        print('通話結束')
        random_ad_type = random.random()
        if random_ad_type > 0.5:
            # TODO: enter FullADState
            pass
        else:
            # TODO: enter BannerADState
            pass


class IncomingState(State):
    def __init__(self, context, answer=True):
        super().__init__(context)
        self.answer = answer

    def handle(self):
        print('電話響鈴中')
        if self.answer:
            # TODO: enter CallEndState
            pass
        else:
            # TODO: enter MissCallState
            pass


class Whoscall:
    def __init__(self):
        self.state = IdleState(self)

    def receive_a_call(self, answer):
        self.state = IncomingState(answer)


if __name__ == '__main__':
    whoscall = Whoscall()

    whoscall.receive_a_call(True)
    """Excepted Results
    電話響鈴中
    通話結束
    顯示全版廣告/顯示半版廣告
    待機狀態，不做任何動作
    """
    print('\n\n')

    whoscall.receive_a_call(False)
    """Excepted Results
    電話響鈴中
    未接狀態
    顯示感謝畫面
    待機狀態，不做任何動作
    """
