from enum import Enum

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal
from typing import Optional


class ConversationStyle(Enum):
    creative = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "h3imaginative",
        "objopinion",
        "dsblhlthcrd",
        "dv3sugg",
        "autosave",
        "clgalileo",
        "gencontentv3",
    ]
    balanced = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "galileo",
        "saharagenconv5",
        "objopinion",
        "dsblhlthcrd",
        "dv3sugg",
        "autosave",
    ]
    precise = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "dv3sugg",
        "autosave",
        "iyxapbing",
        "iycapbing",
        "h3precise",
        "clgalileo",
        "gencontentv3",
        "eredirecturl",
    ]


CONVERSATION_STYLE_TYPE = Optional[
    Union[ConversationStyle, Literal["creative", "balanced", "precise"]]
]
