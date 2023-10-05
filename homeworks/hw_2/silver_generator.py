from item_fabric import ItemFabric
from silver_reward import SilverReward


class SilverGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return SilverReward()
