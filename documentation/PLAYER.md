# Player

## Variables
| Variable | Description | Type |
|----------|-------------|------|
| tag | The tag for the player. | String |
| name | The player's in-game name. | String |
| expLevel | The player's experience level. | Integer |
| trophies | The player's number of trophies. | Integer |
| versusTrophies | The player's number of versus trophies (builder base). | Integer |
| attackWins | The player's number of wins on attack. | Integer |
| defenseWins | The player's number of wins on defense. | Integer |
| bestTrophies | The player's highest trophies. | Integer |
| donations | The number of troops the player has donated. | Integer |
| donationsReceived | The number of troops the player has received. | Integer |
| warStars | The number of stars the player has gotten in Wars. | Integer |
| role | The member's position in their clan. | String |
| townHallLevel | The player's town hall level. | Integer |
| builderHallLevel | The player's builder hall level. | Integer |
| bestVersusTrophies | The player's highest trophies on builder base. | Integer |
| versusBattleWins | The player's amount of wins on builder base. | Integer |

## Methods
| Method | Description | Returns |
|--------|-------------|---------|
| getLeague() | Returns the league the player is in, or None. | [League](https://github.com/cree-py/cocasync/blob/master/documentation/LEAGUE.md) |
| getClan() | Returns the clan the player is in, or None. | [Clan](https://github.com/cree-py/cocasync/blob/master/documentation/CLAN.md) |
| getLegendStatistics() | Returns the player's legend statistics. | [LegendStatistics](https://github.com/cree-py/cocasync/blob/master/documentation/LEGENDSTATISTICS.md) |
| getAchievements() | Returns the player's achievements. | List of [Achievement](https://github.com/cree-py/cocasync/blob/master/documentation/ACHIEVEMENT.md) |
| getTroops() | Returns the player's troops. | List of [Troop](https://github.com/cree-py/cocasync/blob/master/documentation/TROOP.md) |
| getHeroes() | Return the player's heroes, or None. | List of [Hero](https://github.com/cree-py/cocasync/blob/master/documentation/HERO.md) |
| getSpells() | Return the player's spells, or None. | List of [Spell](https://github.com/cree-py/cocasync/blob/master/documentation/SPELL.md)
