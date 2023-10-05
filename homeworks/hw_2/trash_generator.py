from item_fabric import ItemFabric
from trash_reward import TrashReward


class TrashGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return TrashReward()
