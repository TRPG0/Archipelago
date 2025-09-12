from . import Blasphemous2TestBase
from ..Items import item_list, Blas2Item, Blas2Mark
from typing import Union


def get_item(name: str) -> Union[Blas2Item, Blas2Mark]:
    for item in item_list:
        if item.name == name:
            return item
    return None


class TestMarkCountsDefault(Blasphemous2TestBase):
    options = { "martyrdom_xp": "vanilla" }

    def test_mark_counts(self) -> None:
        item_names = [i.name for i in self.multiworld.get_items()]

        self.assertEqual(item_names.count("Marks of Martyrdom (5)"), get_item("Marks of Martyrdom (5)").count)
        self.assertEqual(item_names.count("Marks of Martyrdom (4)"), get_item("Marks of Martyrdom (4)").count)
        self.assertEqual(item_names.count("Marks of Martyrdom (3)"), get_item("Marks of Martyrdom (3)").count)
        self.assertEqual(item_names.count("Marks of Martyrdom (2)"), get_item("Marks of Martyrdom (2)").count)
        self.assertEqual(item_names.count("Marks of Martyrdom (1)"), get_item("Marks of Martyrdom (1)").count)


class TestMarkCountsFromItems(Blasphemous2TestBase):
    options = { "martyrdom_xp": "from_items" }

    def test_mark_counts(self) -> None:
        item_names = [i.name for i in self.multiworld.get_items()]

        self.assertEqual(item_names.count("Marks of Martyrdom (5)"), get_item("Marks of Martyrdom (5)").alt_count)
        self.assertEqual(item_names.count("Marks of Martyrdom (4)"), get_item("Marks of Martyrdom (4)").alt_count)
        self.assertEqual(item_names.count("Marks of Martyrdom (3)"), get_item("Marks of Martyrdom (3)").alt_count)
        self.assertEqual(item_names.count("Marks of Martyrdom (2)"), get_item("Marks of Martyrdom (2)").alt_count)
        self.assertEqual(item_names.count("Marks of Martyrdom (1)"), get_item("Marks of Martyrdom (1)").alt_count)
