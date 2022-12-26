import logging
from turtle import title
import logging
from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Nexia3 = Item(
    title="NEXIA 3 LTZ/AT AV-GX16AT",
    description="Электрические стеклоподъемники с функцией подъема в одно касание,"
                " подушка безопасности со стороны пассажира, литые диски, дистанционное"
                " управление аудиосистемой на руле, дополнительные громкоговорители.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="NEXIA 3",
            amount=1000000
        ),
        LabeledPrice(
            label="Delivery",
            amount=1000
        ),
        LabeledPrice(
            label="Discount",
            amount=-10000
        ),
        LabeledPrice(
            label="TAX",
            amount=10000
        )
    ],
    start_parameter="create_invoice_nexia_3",
    photo_url="https://www.autostrada.uz/wp-content/uploads/2019/09/ravon-nexia-r3-na-avtosalone-v-moskve-390x220.jpg",
    photo_size=600,
    photo_width=50,
    photo_height=60
)

Gentra = Item(
    title="Gentra Lacetti",
    description="Кондиционер, электрические стеклоподъемники, ABS, подушка безопасности водителя,"
                " стальные диски R15 (Переоборудована для работы на сжатом природном газе ",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Gentra",
            amount=1300000
        ),
        LabeledPrice(
            label="Delivery",
            amount=1000
        ),
        LabeledPrice(
            label="Discount",
            amount=-10000
        ),
        LabeledPrice(
            label="TAX",
            amount=10000
        )
    ],
    start_parameter="create_invoice_gentra",
    photo_url="https://www.autostrada.uz/wp-content/uploads/2022/08/20220618_123045-390x220.jpeg",
    photo_size=600,
    photo_width=50,
    photo_height=60,
    need_shipping_address=True,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title="Delivery",
    prices=[
        types.LabeledPrice(
            "Simple box", 0
        ),
        types.LabeledPrice(
            "Normal delivery", 100000
        ),
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id="post_fast",
    title="Delivery (VIP)",
    prices=[
        types.LabeledPrice(
            "Supper delivery box", 100000
        ),
        types.LabeledPrice(
            "Delivery within 3 days", 300000
        ),
    ]
)

PICK_UP_SHIPPING = types.ShippingOption(
    id="pickup",
    title="Go pick up",
    prices=[
        types.LabeledPrice(
            "Store pickup", -10000
        ),
    ]
)
