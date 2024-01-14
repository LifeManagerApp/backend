from collections import namedtuple

SetMoneyManageParams = namedtuple('SetMoneyManage',
                            [
                                'login',
                                'users_category_id',
                                'amount',
                                'comment',
                                'budget_type',
                                'date'
                            ]
                            )
