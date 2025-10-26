# OLIGO-EMOJIS

<p align="center">
  <img src="https://raw.githubusercontent.com/<your-username>/oligo-emojis/main/Oligo_Emojis_Logo.png" alt="Oligo-emojis logo" width="200"/>
</p>

Oligo-emojis is a lightweight, fun Python emoji utility library.

Author: OligoTech

This package provides categorized emoji lists and convenient helpers to retrieve and sample emojis for use in demos, tests, command-line fun, or UI placeholders.

## Quick demo

```python
from oligoemojis import Emojis

e = Emojis()
print(e.list_categories())
print(e.get('Smileys', 3))
print(e.random())
print(e.random('Animals', 4))
```

## API reference

Class: `Emojis(default_count: int = 1)`

- `list_categories()` -> List[str]
	- Returns a sorted list of available categories.

- `get(category: str, q: Union[int, str] = None)` -> List[str] | str
	- Returns emojis from the named category. `q` can be an int (number of items), `'all'` to get the whole list, or omitted to use the instance default.
	- Category matching is case-insensitive.

- `random(category: Optional[str] = None, q: int = 1)` -> str | List[str]
	- Returns a random emoji (when `q==1`) or a list of `q` random emojis. If `category` is `None`, a random category is selected.
	- If `q > size_of_category`, sampling is done with replacement to satisfy the count.

Compatibility helpers (keeps older API names):

- `smileys(q=None)` — returns first `q` smileys or `'all'` for all smileys.
- `smileys_random()` — returns a single random smiley.

## Categories included

Smileys, People, Animals, Foods, Drinks, Activities, Travel, Places, Objects, Symbols, Flags

## Notes

- The library is intentionally simple and dependency-free.
- It is safe to call `random` or `get` with small counts; invalid categories return a helpful message.

If you want additional emoji sets or suggestions, open an issue or submit a PR.
