import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    card_article: str


card = Card(card_name='Машинка игрушка коллекционная металлическая Волшебное Королевство', card_article='150179366')
