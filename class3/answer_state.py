"""
Call in behavior in Whoscall


                                            --- Full AD -----
                                           /                 \
                           --- Call End ---                   ---- Idle
                          /                \                 /      ｜
                         ｜ Answer          --- Banner AD --        ｜
Idle --- CallInComing ----                                          ｜
                          \ Not Answer                              ｜
                           --- Miss Call --- Thank -----------------/




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
        self.context.change_state(IdleState(self.context))


class MissCallState(State):
    def handle(self):
        print('未接狀態')
        self.context.change_state(ThankState(self.context))


class FullADState(State):
    def handle(self):
        print('顯示全版廣告')
        self.context.change_state(IdleState(self.context))


class BannerADState(State):
    def handle(self):
        print('顯示半版廣告')
        self.context.change_state(IdleState(self.context))


class CallEndState(State):
    def handle(self):
        print('通話結束')
        random_ad_type = random.random()
        if random_ad_type > 0.5:
            # TODO: enter FullADState
            self.context.change_state(FullADState(self.context))
        else:
            # TODO: enter BannerADState
            self.context.change_state(BannerADState(self.context))


class IncomingState(State):
    def __init__(self, context, answer=True):
        super().__init__(context)
        self.answer = answer

    def handle(self):
        print('電話響鈴中')
        if self.answer:
            # TODO: enter CallEndState
            self.context.change_state(CallEndState(self.context))
        else:
            # TODO: enter MissCallState
            self.context.change_state(MissCallState(self.context))


class Whoscall:
    def __init__(self):
        self.state = IdleState(self)

    def receive_a_call(self, answer):
        self.change_state(IncomingState(self, answer))

    def change_state(self, new_state):
        self.state = new_state
        self.state.handle()


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
