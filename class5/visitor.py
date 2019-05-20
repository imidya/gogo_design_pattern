import abc


class Customer:

    def body_massage(self):
        raise NotImplementedError()

    def foot_massage(self):
        raise NotImplementedError()

    def accept(self, visitor):
        # TODO
        pass

    def pay(self):
        print('Customer pay the money')


class NormalMember(Customer):

    def foot_massage(self):
        print('Normal Customer - Foot Massage')

    def body_massage(self):
        print('Normal Customer - Body Massage')


class VIPMember(Customer):

    def foot_massage(self):
        print('VIP Customer - Foot Massage')

    def body_massage(self):
        print('VIP Customer - Body Massage')


class Visitor(abc.ABC):

    def visit(self, customer: Customer):
        raise NotImplementedError()


class FootSeaFood(Visitor):
    # TODO


class BodySeaFood(Visitor):
    # TODO


class MassageStore:

    def do_service(self, seadfood: Visitor, customer: Customer):
        customer.accept(seadfood)
        customer.pay()
        print()


if __name__ == '__main__':
    store = MassageStore()
    foot_seafood = FootSeaFood()
    body_seafood = BodySeaFood()
    normal_customer = NormalMember()
    VIP_customer = VIPMember()

    store.do_service(foot_seafood, normal_customer)
    store.do_service(foot_seafood, VIP_customer)
    store.do_service(body_seafood, normal_customer)
    store.do_service(body_seafood, VIP_customer)
    """Excepted Result
    Normal Customer - Foot Massage
    Customer pay the money
    
    VIP Customer - Foot Massage
    Customer pay the money
    
    Normal Customer - Body Massage
    Customer pay the money
    
    VIP Customer - Body Massage
    Customer pay the money
    """
