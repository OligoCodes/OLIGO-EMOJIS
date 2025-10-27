"""A playful, easy-to-use emoji library.

Provides categorized emoji lists and helper methods to fetch and sample emojis.

Author: OligoTech
"""
__version__ = "0.1.0"

from typing import List, Union, Optional
import random
import time


class Emojis:
    """Emoji library with categories and sampling helpers.

    Example:
        e = Emojis()
        e.list_categories()
        e.get('Smileys', 3)
        e.random()  # random emoji from any category
        e.random('Animals', 2)  # two random animals
    """

    def __init__(self, default_count: int = 1):
        self.default_count = default_count
        self.libName = "OLIGOEMOJIS LIBRARY PYNODE\n"
        self.default_speed = 0.05

        # Centralized emoji mapping by category. Keep keys normalized.
        self._categories = {
            'Smileys': [
                '😀','😁','😂','🤣','😃','😄','😅','😆','😉','😊','🙂','🙃','☺️','😇','🥰','😍','🤩','😘','😗','😚','😙',
                '😋','😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐','🤨','😐','😑','😶','😏','😒','🙄','😬','🤥','😌',
                '😴','🤤','😪','😮','😯','😲','😳','🥵','🥶','😱','😨','😰','😥','😓','🤯','🤬','😠','😡','😢','😭'
            ],

            'People': [
                '👶','🧒','👦','👧','🧑','👱‍♀️','👱‍♂️','👨','👩','🧔','👴','👵','🧓','👩‍⚕️','👨‍⚕️','👩‍🎓','👨‍🎓','👩‍🏫','👨‍🏫',
                '👩‍⚖️','👨‍⚖️','👮‍♀️','👮‍♂️','👷‍♀️','👷‍♂️','💂‍♀️','💂‍♂️','🕵️‍♀️','🕵️‍♂️','👩‍🌾','👨‍🌾','👩‍🍳','👨‍🍳','👩‍🔧','👨‍🔧',
                '👩‍🏭','👨‍🏭','👩‍💼','👨‍💼','👩‍🔬','👨‍🔬','👩‍🎤','👨‍🎤','👩‍🎨','👨‍🎨','👩‍🚒','👨‍🚒','👩‍✈️','👨‍✈️','👩‍🚀','👨‍🚀'
            ],

            'Animals': [
                '🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐸','🐵','🐔','🐧','🐦','🐤','🐣','🦆',
                '🦅','🦉','🦇','🐺','🐗','🐴','🦄','🐝','🐛','🦋','🐌','🐞','🐜','🪲','🪳','🕷️','🦂','🐢','🐍','🦎','🦖','🐙','🦑','🦐','🦀',
                '🐠','🐟','🐡','🐬','🐳','🐋','🦈','🦧','🦥','🦦','🦨','🦩'
            ],

            'Foods': [
                '🍏','🍎','🍐','🍊','🍋','🍌','🍉','🍇','🍓','🍈','🍒','🍑','🥭','🍍','🥥','🥝','🍅','🍆','🥑','🥦','🥬','🥒','🌶️','🌽',
                '🥕','🥔','🍠','🥐','🍞','🥖','🥨','🥯','🧀','🥚','🍳','🧂','🍔','🍟','🍕','🌭','🥪','🌮','🌯','🥗','🥘','🍝','🍜','🍲','🍛',
                '🍣','🍱','🥟','🦪','🍤','🍙','🍚','🍘','🍢','🍡','🍧','🍨','🍦','🥧','🍰','🎂','🧁','🍮','🍭','🍬','🍫'
            ],

            'Drinks': [
                '☕','🍵','🧃','🥤','🧋','🍺','🍻','🍷','🥂','🥃','🍸','🍹','🥤','🥛','🍼','🍶','🍾'
            ],

            'Activities': [
                '⚽','🏀','🏈','⚾','🥎','🎾','🏐','🏉','🎱','🏓','🏸','🏒','🏑','🏏','🏹','🎣','🥊','🥋','⛸️','🎿','🛷','🪂','🏂','🏄‍♀️','🏄‍♂️',
                '🏊‍♀️','🏊‍♂️','🤽‍♀️','🤽‍♂️','🚣‍♀️','🚣‍♂️','🧘‍♀️','🧘‍♂️','🏋️‍♀️','🏋️‍♂️','🚴‍♀️','🚴‍♂️','🚵‍♀️','🚵‍♂️','🎮','🎲','🧩','🎯','🎳',
                '🎹','🥁','🎸','🎻','🎺','🪕','🎬','🎤','🎧'
            ],

            'Travel': [
                '🚗','🚕','🚙','🚌','🚎','🏎️','🚓','🚑','🚒','🚐','🚚','🚛','🚜','🏍️','🛵','🚲','🛴','🛺','🚂','🚆','🚇','🚊','🚉','✈️','🛩️','🛫','🛬','🚀','🛰️','🚁','⛵','🛥️','🚢'
            ],

            'Places': [
                '🏠','🏡','🏘️','🏚️','🏗️','🏢','🏬','🏣','🏤','🏥','🏦','🏨','🏪','🏫','🏩','💒','⛪','🕌','🕍','⛩️','🛕','🕋','🗽','🗼','🏰','🏯','🏟️','🏛️','🏝️','🏜️','🏞️'
            ],

            'Objects': [
                '⌚','📱','📲','💻','⌨️','🖥️','🖨️','🕹️','🖱️','🖲️','💽','💾','💿','📀','📷','📸','📹','🎥','☎️','📞','📟','📠','📺','📻','🎙️','🎚️','🎛️','⏱️','⏲️','🧭','🧰','🔧','🔨','⚙️','💡','🔦','🏮','🧯','🛠️','🔩','🔗','🔒','🔓','🔑','🧾','📦','🛒','🧿','🪄','🔮','🧸','🧵','🪡','🧶','🪢'
            ],

            'Symbols': [
                '❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','💔','❣️','💕','💞','💓','💗','💖','✨','⭐','🌟','⚡','🔥','🎉','💯','✅','❌','❗','❓','⚠️','🚫','🔞','♻️','©️','®️','™️'
            ],

            'Flags': [
                '🏳️','🏴','🏁','🚩','🏳️‍🌈','🇺🇸','🇬🇧','🇨🇦','🇯🇵','🇫🇷','🇩🇪','🇮🇳','🇨🇳','🇰🇷','🇪🇺','🇧🇷','🇦🇺','🇳🇿','🇿🇦','🇲🇽','🇮🇹','🇪🇸','🇷🇺','🇸🇦','🇹🇷','🇦🇪','🇸🇬','🇮🇩','🇵🇭','🇹🇭','🇻🇳','🇵🇰','🇳🇬','🇪🇬'
            ]
        }

    # --- API methods ---
    def list_categories(self) -> List[str]:
        """Return a sorted list of category names."""
        return sorted(self._categories.keys())

    def get(self, category: str, q: Union[int, str] = None) -> Union[List[str], str]:
        """Return emojis from a category.

        Args:
            category: category name (case-insensitive).
            q: number of items to return, or 'all'. If None uses instance default_count.

        Returns:
            A list of emojis, or an error string when input is invalid.
        """
        if q is None:
            q = self.default_count

        key = next((k for k in self._categories if k.lower() == category.lower()), None)
        if not key:
            return f"Unknown category: {category}. Available: {', '.join(self.list_categories())}"

        items = self._categories[key]
        if isinstance(q, str) and q.lower() == 'all':
            return items.copy()
        if not isinstance(q, int):
            return "q must be an int or 'all'"
        if q <= 0:
            return []
        return items[:q] if q <= len(items) else items.copy()

    def random(self, category: Optional[str] = None, q: int = 1) -> Union[str, List[str]]:
        """Return a random emoji or list of random emojis.

        If category is None a random category will be chosen.
        For q==1 returns a single emoji (str). For q>1 returns a list of emojis.
        """
        if q <= 0:
            return []

        if category is None:
            category = random.choice(self.list_categories())

        key = next((k for k in self._categories if k.lower() == category.lower()), None)
        if not key:
            return f"Unknown category: {category}. Available: {', '.join(self.list_categories())}"

        pool = self._categories[key]
        if q == 1:
            return random.choice(pool)
        if q <= len(pool):
            return random.sample(pool, q)
        else:
            return [random.choice(pool) for _ in range(q)]

    # Backwards-compatible wrappers
    def smileys(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Smileys', q)

    def smileys_random(self):
        return self.random('Smileys', 1)

    def people(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('People', q)

    def people_random(self):
        return self.random('People', 1)

    def animals(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Animals', q)

    def animals_random(self):
        return self.random('Animals', 1)

    def foods(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Foods', q)

    def foods_random(self):
        return self.random('Foods', 1)

    def drinks(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Drinks', q)

    def drinks_random(self):
        return self.random('Drinks', 1)

    def activities(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Activities', q)

    def activities_random(self):
        return self.random('Activities', 1)

    def travel(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Travel', q)

    def travel_random(self):
        return self.random('Travel', 1)

    def places(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Places', q)

    def places_random(self):
        return self.random('Places', 1)

    def objects(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Objects', q)

    def objects_random(self):
        return self.random('Objects', 1)

    def symbols(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Symbols', q)

    def symbols_random(self):
        return self.random('Symbols', 1)

    def flags(self, q: Union[int, str] = None):
        if q is None:
            q = self.default_count
        return self.get('Flags', q)

    def flags_random(self):
        return self.random('Flags', 1)

    def categories(self) -> List[str]:
        return self.list_categories()

    def about(self) -> str:
        try:
            with open('readme.md', 'r', encoding='utf-8') as f:
                return self.libName + '\n' + f.read()
        except Exception:
            return self.libName + '\n' + 'readme.md not available'

    def author(self, t_speed: Optional[float] = None):
        if t_speed is None:
            t_speed = self.default_speed
        oligotech_ascii = r"""
  ___  _     ___ ____  ___ _____ _____ ____ _   _ 
 / _ \| |   |_ _/ ___|/ _ \_   _| ____/ ___| | | |
| | | | |    | | |  _| | | || | |  _|| |   | |_| |
| |_| | |___ | | |_| | |_| || | | |__| |___|  _  |
 \___/|_____|___\____|\___/ |_| |_____\____|_| |_|
"""
        text = 'Powered by OligoTech GH'
        for ch in text:
            print(ch, end='', flush=True)
            time.sleep(t_speed)
        print('\n')
        print(oligotech_ascii)
        return oligotech_ascii
 
