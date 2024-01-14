from collections import namedtuple

MoneyManageHistoryParams = namedtuple('MoneyManageHistory',
                            [
                                'login',
                                'date_from',
                                'date_to',
                                'category',
                                'income'
                            ]
                            )
